#!/usr/bin/env python3
from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent
PAPER = ROOT / "no-exactly-two-dlo.md"

ENV_NAMES = (
    "Definition", "Theorem", "Proposition", "Lemma", "Corollary",
    "Example", "Remark", "Assumption", "Heuristic", "Principle",
)
ENV_RE = re.compile(
    rf"^\*\*({'|'.join(ENV_NAMES)})\s+([1-7]\.[0-9]+|[AB]\.[0-9]+)\s+\(([^\n]+)\)\.\*\*$",
    re.M,
)
ANCHOR_RE = re.compile(r'^<div id="([A-Za-z0-9:-]+)"></div>$', re.M)
EQ_ID_RE = re.compile(r'\{#(eq:[A-Za-z0-9:-]+)\}')
EQ_REF_RE = re.compile(r'\\eqref\{(eq:[A-Za-z0-9:-]+)\}')
LINK_RE = re.compile(r'\]\(#([A-Za-z0-9:-]+)\)')


def fail(message: str) -> None:
    raise AssertionError(message)


def main() -> int:
    text = PAPER.read_text(encoding="utf-8")
    lines = text.splitlines()

    # Front matter and post-formalization freeze policy.
    if PAPER.name != "no-exactly-two-dlo.md":
        fail("Canonical source filename must not contain a working revision")
    if "**Lior Isthmus**" not in text:
        fail("Author line is missing")
    for forbidden in (
        "Revision 7", "Revision 6", "Revision 1", "Internal review status",
        "Independent human verification is pending", "ORCID",
        "## 0.", "no-exactly-two-dlo-v7.md",
    ):
        if forbidden in text:
            fail(f"Forbidden public-candidate string: {forbidden}")

    required_release_markers = (
        '<div id="sec:title"></div>',
        '<div id="sec:abstract"></div>',
        '<div id="sec:ai-disclosure"></div>',
        "## AI-use disclosure {.unnumbered .unlisted}",
        '<div id="ref:isthmus2026a"></div>',
        '<div id="ref:isthmus2026b"></div>',
        '<div id="ref:isthmus2026c"></div>',
        "https://doi.org/10.5281/zenodo.21735262",
        "https://doi.org/10.5281/zenodo.21729423",
        "ExactTwoDLO.FO.zsep_proves_not_spec2Sentence",
        "https://github.com/lioristhmus/no-exactly-two-dlo-lean",
        "AI systems are tools, not authors.",
    )
    for marker in required_release_markers:
        if text.count(marker) != 1:
            fail(f"Required paper-rc2 marker missing or duplicated: {marker}")
    if text.index("## Abstract") > text.index("\\tableofcontents"):
        fail("The table of contents must follow the abstract")
    if text.index("\\tableofcontents") > text.index("## 1. Introduction"):
        fail("The table of contents must precede the introduction")

    # Section structure.
    expected_sections = [
        "## 1. Introduction",
        "## 2. Formal setting and imported results",
        "## 3. Exact-two structural reduction",
        "## 4. The one-point cut square",
        "## 5. The cut-preimage reversal",
        "## 6. Exact-two exclusion",
        "## 7. Scope and further questions",
        "## Appendix A. Weak-theory audit of the new construction",
        "## Appendix B. A type-count-free dyadic reflection engine",
        "## AI-use disclosure {.unnumbered .unlisted}",
        "## References",
    ]
    positions = []
    for heading in expected_sections:
        if text.count(heading) != 1:
            fail(f"Heading missing or duplicated: {heading}")
        positions.append(text.index(heading))
    if positions != sorted(positions):
        fail("Section order is incorrect")

    # Anchor hygiene.
    anchors = ANCHOR_RE.findall(text)
    duplicates = [a for a, n in Counter(anchors).items() if n > 1]
    if duplicates:
        fail(f"Duplicate anchors: {duplicates}")
    for idx, line in enumerate(lines[:-1]):
        if re.fullmatch(r'<div id="[A-Za-z0-9:-]+"></div>', line):
            if lines[idx + 1].strip():
                fail(f"Anchor not followed by blank line at line {idx + 1}")

    # Equation IDs and references.
    eq_ids = EQ_ID_RE.findall(text)
    eq_dups = [e for e, n in Counter(eq_ids).items() if n > 1]
    if eq_dups:
        fail(f"Duplicate equation IDs: {eq_dups}")
    missing_eq = sorted(set(EQ_REF_RE.findall(text)) - set(eq_ids))
    if missing_eq:
        fail(f"Missing equation targets: {missing_eq}")
    missing_links = sorted(set(LINK_RE.findall(text)) - set(anchors) - set(eq_ids))
    if missing_links:
        fail(f"Missing internal-link targets: {missing_links}")

    # Theorem/definition numbering: one sequence per numbered section/appendix.
    envs = list(ENV_RE.finditer(text))
    if not envs:
        fail("No theorem environments found")
    by_chapter: dict[str, list[int]] = defaultdict(list)
    declarations: set[str] = set()
    for m in envs:
        kind, number, _title = m.groups()
        chapter, local = number.split(".")
        by_chapter[chapter].append(int(local))
        declarations.add(f"{kind} {number}")
    expected_chapters = {"1", "2", "3", "4", "5", "6", "A", "B"}
    if set(by_chapter) != expected_chapters:
        fail(f"Unexpected environment chapters: {sorted(by_chapter)}")
    expected_counts = {
        "1": 2, "2": 8, "3": 8, "4": 6,
        "5": 6, "6": 3, "A": 4, "B": 8,
    }
    actual_counts = {chapter: len(nums) for chapter, nums in by_chapter.items()}
    if actual_counts != expected_counts:
        fail(f"Environment count changed: {actual_counts}")
    for chapter, nums in by_chapter.items():
        expected = list(range(1, len(nums) + 1))
        if nums != expected:
            fail(f"Environment numbering failure in chapter {chapter}: {nums}")

    # Every environment must have an immediately preceding anchor (allow one blank line).
    for m in envs:
        line_no = text.count("\n", 0, m.start())
        j = line_no - 1
        while j >= 0 and not lines[j].strip():
            j -= 1
        if j < 0 or not re.fullmatch(r'<div id="[A-Za-z0-9:-]+"></div>', lines[j]):
            fail(f"Environment lacks preceding anchor near line {line_no + 1}: {m.group(0)}")

    # References to this paper's environments resolve.  Remove bibliography
    # links first so labels quoted from the exact-three companion are not
    # mistaken for local declarations (some numbers intentionally collide).
    reference_text = re.sub(r"\[[^\]]+\]\(#ref:[^)]+\)", "", text)
    ref_re = re.compile(
        rf"\b({'|'.join(ENV_NAMES)})\s+([1-7]\.[0-9]+|[AB]\.[0-9]+)\b"
    )
    unknown = set()
    for kind, number in ref_re.findall(reference_text):
        label = f"{kind} {number}"
        if label not in declarations:
            unknown.add(label)
    if unknown:
        fail(f"References to undeclared environments: {sorted(unknown)}")

    # Plural/compound references, including comma lists and ranges.
    plural_to_singular = {
        "Definitions": "Definition",
        "Theorems": "Theorem",
        "Propositions": "Proposition",
        "Lemmas": "Lemma",
        "Corollaries": "Corollary",
        "Remarks": "Remark",
    }
    plural_ref_re = re.compile(
        r"\b(Definitions|Theorems|Propositions|Lemmas|Corollaries|Remarks)\s+"
        r"((?:[1-7AB]\.[0-9]+)(?:\s*(?:,\s*(?:and\s+)?|and\s+|[–-]\s*)"
        r"[1-7AB]\.[0-9]+)*)"
    )
    compound_unknown = set()
    for plural, body in plural_ref_re.findall(reference_text):
        singular = plural_to_singular[plural]
        for chapter, local in re.findall(r"([1-7AB])\.([0-9]+)", body):
            label = f"{singular} {chapter}.{local}"
            if label not in declarations:
                compound_unknown.add(label)
    if compound_unknown:
        fail(f"Compound references to undeclared environments: {sorted(compound_unknown)}")

    # MathJax/Markdown safety subset.
    for forbidden in ("\\tag{", "\\[", "\\]", "\\(", "\\)"):
        if forbidden in text:
            fail(f"Forbidden TeX delimiter or tag: {forbidden}")
    fence_lines = [i for i, line in enumerate(lines, 1) if "$$" in line]
    for i in fence_lines:
        stripped = lines[i - 1].strip()
        if stripped != "$$" and not re.fullmatch(r'\$\$\s+\{#eq:[A-Za-z0-9:-]+\}', stripped):
            fail(f"Display-math fence is not on its own line at line {i}: {lines[i-1]}")
    if len(fence_lines) % 2:
        fail("Unbalanced display-math fences")

    in_math = False
    for i, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped == "$$" or re.fullmatch(r'\$\$\s+\{#eq:[A-Za-z0-9:-]+\}', stripped):
            in_math = not in_math
            continue
        if in_math and re.match(r'^ {0,3}(\* |- |\+ |\d+\.\s)', line):
            fail(f"Markdown list trigger inside display math at line {i}")
    if in_math:
        fail("Display-math state did not close")

    # Environment style and proof labels.
    bad_heading = re.search(r'^####\s*(?:' + '|'.join(ENV_NAMES) + r'|Proof)\b', text, re.M)
    if bad_heading:
        fail(f"Theorem environment encoded as Markdown heading: {bad_heading.group(0)}")
    if re.search(r'^\*\*Proof', text, re.M):
        fail("Bold Proof label found; use *Proof.*")
    if re.search(r'^\*Proof\*(?!\.)', text, re.M):
        fail("Proof label without period")

    # Equation label placement: labels must be on the closing fence line.
    for i, line in enumerate(lines, 1):
        if "{#eq:" in line and not re.fullmatch(r'\$\$\s+\{#eq:[A-Za-z0-9:-]+\}', line.strip()):
            fail(f"Equation ID is not attached to closing fence at line {i}")

    # Canonical-source markers.
    if "# No Set Carries Exactly Two Dense Linear Orders without Endpoints" not in text:
        fail("Title is missing")
    if "**Keywords.**" not in text or "**2020 Mathematics Subject Classification.**" not in text:
        fail("Keywords or MSC line is missing")

    print(f"PASS: {PAPER.name}")
    print(f"  lines: {len(lines)}")
    print(f"  anchors: {len(anchors)}")
    print(f"  equation IDs: {len(eq_ids)}")
    print(f"  environments: {len(envs)} (45 expected)")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
