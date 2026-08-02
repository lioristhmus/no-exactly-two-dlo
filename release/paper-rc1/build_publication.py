#!/usr/bin/env python3
"""Build the exact-two paper-rc1 source freeze with the AMS/XeLaTeX profile.

A temporary compatibility pass promotes the canonical Markdown's visible
title block to Pandoc metadata, shifts the remaining heading hierarchy by one
level, and keeps the abstract endpoint display unnumbered.
"""

from __future__ import annotations

import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "no-exactly-two-dlo.md"
BUILD = ROOT / "build"
STYLES = ROOT / "common" / "styles"
OUTPUT_STEM = "no-exactly-two-dlo"
SOURCE_DATE_EPOCH = "1785655928"  # 2026-08-02T07:32:08Z

TITLE = "No Set Carries Exactly Two Dense Linear Orders without Endpoints"
SUBTITLE = "A Cut-Rotation Proof in a Weak Zermelo Theory without Choice or Replacement"
AUTHOR = "Lior Isthmus"


def preprocess(text: str) -> str:
    """Adapt the manuscript's readable top matter without changing its source."""

    title_pattern = (
        r'^<div id="sec:title"></div>\n\n'
        r'# .*?\n\n'
        r'\*.*?\*\n\n'
        r'\*\*Lior Isthmus\*\*\n\n'
    )
    text, replacements = re.subn(
        title_pattern,
        "",
        text,
        count=1,
        flags=re.S,
    )
    if replacements != 1:
        raise RuntimeError("canonical title block did not match the release profile")

    metadata = f"""---
title: {TITLE}
subtitle: {SUBTITLE}
author:
  - {AUTHOR}
date: ''
---

<div id="sec:title"></div>

"""
    text = metadata + text

    abstract_marker = '<div id="sec:abstract"></div>\n\n## Abstract'
    if text.count(abstract_marker) != 1:
        raise RuntimeError("canonical abstract marker is missing or duplicated")
    text = text.replace(
        abstract_marker,
        '<div id="sec:abstract"></div>\n\n## Abstract {.unnumbered .unlisted}',
        1,
    )

    # Preserve the preceding freeze's numbering: the headline display is an
    # anchored, unnumbered display, while all other equation IDs are handled by
    # pandoc-crossref.
    lines = text.splitlines()
    output: list[str] = []
    index = 0
    converted_abstract_main = False
    while index < len(lines):
        if lines[index].strip() != "$$":
            output.append(lines[index])
            index += 1
            continue

        body: list[str] = []
        index += 1
        while index < len(lines) and not (
            lines[index].strip() == "$$"
            or re.fullmatch(
                r"\$\$\s+\{#eq:[A-Za-z0-9:-]+\}", lines[index].strip()
            )
        ):
            body.append(lines[index])
            index += 1
        if index >= len(lines):
            raise RuntimeError("unclosed display-math block")

        closing = lines[index].strip()
        label = re.fullmatch(
            r"\$\$\s+\{#(eq:[A-Za-z0-9:-]+)\}", closing
        )
        if label and label.group(1) == "eq:abstract-main":
            output.extend(
                [
                    r"\hypertarget{eq:abstract-main}{}",
                    r"\begin{equation*}",
                    *body,
                    r"\end{equation*}",
                ]
            )
            converted_abstract_main = True
        else:
            output.extend(["$$", *body, closing])
        index += 1

    if not converted_abstract_main:
        raise RuntimeError("eq:abstract-main was not converted")
    return "\n".join(output) + "\n"


def run(command: list[str], *, cwd: Path, env: dict[str, str] | None = None) -> None:
    print("+", " ".join(command))
    subprocess.run(command, cwd=cwd, env=env, check=True)


def require_tools() -> tuple[str, str, str]:
    resolved = tuple(shutil.which(name) for name in ("pandoc", "pandoc-crossref", "xelatex"))
    if any(path is None for path in resolved):
        missing = [
            name
            for name, path in zip(("pandoc", "pandoc-crossref", "xelatex"), resolved)
            if path is None
        ]
        raise RuntimeError(f"missing required tools: {', '.join(missing)}")
    return resolved  # type: ignore[return-value]


def main() -> int:
    pandoc, _crossref, xelatex = require_tools()
    BUILD.mkdir(exist_ok=True)

    with tempfile.TemporaryDirectory(prefix="no2-paper-rc1-") as temporary:
        work = Path(temporary)
        prepared = work / "prepared.md"
        tex = work / f"{OUTPUT_STEM}.tex"
        pdf = work / f"{OUTPUT_STEM}.pdf"
        prepared.write_text(preprocess(SOURCE.read_text(encoding="utf-8")), encoding="utf-8")

        pandoc_command = [
            pandoc,
            str(prepared),
            "--standalone",
            "--to=latex",
            "--from=markdown-fancy_lists+raw_tex+tex_math_dollars+raw_html+footnotes+table_captions",
            f"--resource-path={ROOT}",
            "--filter=pandoc-crossref",
            f"--lua-filter={STYLES / 'pandoc-manual-reference-anchors.lua'}",
            f"--metadata-file={STYLES / 'pandoc-arxiv-ams-en.yaml'}",
            f"--lua-filter={STYLES / 'pandoc-promote-topmatter.lua'}",
            f"--include-in-header={STYLES / 'arxiv-preamble.tex'}",
            f"--include-in-header={STYLES / 'macros.tex'}",
            "--shift-heading-level-by=-1",
            "--citeproc",
            f"--output={tex}",
        ]
        run(pandoc_command, cwd=ROOT)

        environment = os.environ.copy()
        environment.update(
            {
                "SOURCE_DATE_EPOCH": SOURCE_DATE_EPOCH,
                "TZ": "UTC",
                "TEXMFCACHE": str(work / "texmf-cache"),
                "TEXMFVAR": str(work / "texmf-var"),
                "TEXINPUTS": f"{ROOT}:",
            }
        )
        for pass_number in (1, 2, 3):
            print(f"XeLaTeX pass {pass_number}/3")
            run(
                [
                    xelatex,
                    "-halt-on-error",
                    "-file-line-error",
                    "-interaction=nonstopmode",
                    f"-output-directory={work}",
                    tex.name,
                ],
                cwd=work,
                env=environment,
            )

        if not pdf.is_file() or pdf.stat().st_size == 0:
            raise RuntimeError("XeLaTeX did not generate a PDF")

        log_text = (work / f"{OUTPUT_STEM}.log").read_text(
            encoding="utf-8", errors="replace"
        )
        fatal_warnings = (
            "undefined references",
            "multiply defined",
            "undefined control sequence",
            "missing character",
            "label(s) may have changed",
            "overfull \\hbox",
            "overfull \\vbox",
        )
        lowered = log_text.lower()
        found = [warning for warning in fatal_warnings if warning in lowered]
        if found:
            raise RuntimeError(f"release build has unresolved LaTeX warnings: {found}")

        shutil.copy2(tex, BUILD / tex.name)
        shutil.copy2(pdf, BUILD / pdf.name)

    print(f"Built {BUILD / (OUTPUT_STEM + '.tex')}")
    print(f"Built {BUILD / (OUTPUT_STEM + '.pdf')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
