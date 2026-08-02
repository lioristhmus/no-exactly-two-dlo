#!/usr/bin/env python3
"""Create and validate the exact-two paper inventory and Lean planning index.

The source-freeze phase records all paper-facing statements without pretending
that Lean proofs already exist.  A later Level IV release may replace the
planned fields with actual declarations and validate with ``--final``.
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path
import argparse
import hashlib
import json
import re


ROOT = Path(__file__).resolve().parent
PAPER = ROOT / "no-exactly-two-dlo.md"
INDEX = ROOT / "formalization-index.json"
INDEX_MD = ROOT / "formalization-index.md"
ANCHOR_MANIFEST = ROOT / "anchor-manifest.json"

ENV_RE = re.compile(
    r"^\*\*(Definition|Theorem|Proposition|Lemma|Corollary|Example|Remark|"
    r"Assumption|Heuristic|Principle)\s+"
    r"([1-7]\.[0-9]+|[AB]\.[0-9]+)\s+\(([^\n]+)\)\.\*\*$",
    re.M,
)
ANCHOR_RE = re.compile(r'^<div id="([A-Za-z0-9:-]+)"></div>$', re.M)
SECTION_RE = re.compile(r"^## (.+)$", re.M)
FENCE_RE = re.compile(
    r"^(?P<indent>[ \t]{0,3})\$\$(?:\s+\{#(?P<id>eq:[A-Za-z0-9:-]+)\})?$",
    re.M,
)
SHA_RE = re.compile(r"[0-9a-f]{64}")


def fail(message: str) -> None:
    raise AssertionError(message)


def source_sha256() -> str:
    return hashlib.sha256(PAPER.read_bytes()).hexdigest()


def line_number(text: str, position: int) -> int:
    return text.count("\n", 0, position) + 1


def preceding(items: list[re.Match[str]], position: int) -> re.Match[str] | None:
    result = None
    for item in items:
        if item.start() >= position:
            break
        result = item
    return result


def planned_location(kind: str, number: str) -> tuple[str, str, str]:
    chapter = number.split(".")[0]
    module_tail = {
        "1": "Intro",
        "2": "Section2",
        "3": "Section3",
        "4": "Section4",
        "5": "Section5",
        "6": "Section6",
        "A": "AppendixA",
        "B": "AppendixB",
    }[chapter]
    slug = number.replace(".", "_")
    declaration = f"ExactTwoDLO.Paper.{kind.lower()}_{slug}"
    module = f"NoExactlyTwoDlo.Paper.{module_tail}"
    file = f"NoExactlyTwoDlo/Paper/{module_tail}.lean"
    return declaration, module, file


def paper_environments(text: str) -> list[dict[str, object]]:
    anchors = list(ANCHOR_RE.finditer(text))
    sections = list(SECTION_RE.finditer(text))
    result: list[dict[str, object]] = []
    for match in ENV_RE.finditer(text):
        anchor = preceding(anchors, match.start())
        if anchor is None:
            fail(f"environment has no preceding anchor: {match.group(0)}")
        if text[anchor.end():match.start()].strip():
            fail(f"environment anchor is not adjacent to {match.group(1)} {match.group(2)}")
        section = preceding(sections, match.start())
        kind, number, title = match.groups()
        declaration, module, file = planned_location(kind, number)
        result.append({
            "anchor_id": anchor.group(1),
            "display_label": f"{kind} {number}",
            "title": title,
            "section": section.group(1) if section else "Front matter",
            "line": line_number(text, match.start()),
            "position": match.start(),
            "claim_id": f"paper-{anchor.group(1).replace(':', '-')}",
            "planned_lean_declaration": declaration,
            "planned_lean_module": module,
            "planned_lean_file": file,
            "actual_lean_declaration": None,
            "actual_lean_module": None,
            "actual_lean_file": None,
            "status": "planned",
        })
    return result


def paper_equations(
    text: str, environments: list[dict[str, object]]
) -> list[dict[str, object]]:
    fences = list(FENCE_RE.finditer(text))
    sections = list(SECTION_RE.finditer(text))
    if len(fences) % 2:
        fail("unbalanced display-math fences")
    result: list[dict[str, object]] = []
    for opening, closing in zip(fences[::2], fences[1::2], strict=True):
        if opening.group("id") is not None:
            fail("equation ID found on an opening fence")
        eq_id = closing.group("id")
        if eq_id is None:
            continue
        body = text[opening.end():closing.start()]
        section = preceding(sections, opening.start())
        nearest = None
        for env in environments:
            if int(env["position"]) < opening.start():
                nearest = env
            else:
                break
        result.append({
            "equation_id": eq_id,
            "section": section.group(1) if section else "Front matter",
            "nearest_environment_anchor": nearest["anchor_id"] if nearest else None,
            "nearest_environment_label": nearest["display_label"] if nearest else None,
            "line": line_number(text, opening.start()),
            "position": opening.start() + len(opening.group("indent")),
            "preview": " ".join(body.split()),
            "planned_covering_declaration": (
                "ExactTwoDLO.FO.zsep_proves_not_spec2Sentence"
                if eq_id == "eq:abstract-main"
                else nearest["planned_lean_declaration"] if nearest else None
            ),
            "actual_covering_declaration": None,
            "status": "planned-main-endpoint" if eq_id == "eq:abstract-main" else "planned-coverage",
        })
    return result


def build_anchor_manifest(text: str) -> dict[str, object]:
    environment_anchors = {
        env["anchor_id"] for env in paper_environments(text)
    }
    anchors = []
    for match in ANCHOR_RE.finditer(text):
        anchor_id = match.group(1)
        if anchor_id in environment_anchors:
            category = "numbered-environment"
        elif anchor_id.startswith("ref:"):
            category = "reference"
        elif anchor_id.startswith("sec:") or anchor_id.startswith("app:"):
            category = "section"
        else:
            category = "other"
        anchors.append({
            "anchor_id": anchor_id,
            "category": category,
            "line": line_number(text, match.start()),
            "position": match.start(),
        })
    return {
        "schema_version": 1,
        "freeze_id": "paper-rc1",
        "canonical_source": PAPER.name,
        "canonical_source_sha256": source_sha256(),
        "anchor_count": len(anchors),
        "anchors": anchors,
    }


def initialize_index(text: str) -> dict[str, object]:
    environments = paper_environments(text)
    equations = paper_equations(text, environments)
    return {
        "schema_version": 1,
        "freeze_id": "paper-rc1",
        "lifecycle": "pre-formalization-source-freeze",
        "canonical_source": PAPER.name,
        "canonical_source_sha256": source_sha256(),
        "formalization_target": "level-IV-paper-exact-end-to-end",
        "formalization_status": "not-started",
        "formalization_contract_sha256": None,
        "environment_count": len(environments),
        "equation_count": len(equations),
        "environment_status_summary": {
            "planned": len(environments),
            "exact-proved": 0,
        },
        "environments": environments,
        "equations": equations,
    }


def validate(text: str, data: dict[str, object], *, final: bool) -> None:
    if data.get("schema_version") != 1:
        fail("formalization index schema_version must be 1")
    if data.get("canonical_source") != PAPER.name:
        fail("formalization index names a different canonical source")
    if data.get("canonical_source_sha256") != source_sha256():
        fail("formalization index was generated from a different source hash")
    if data.get("formalization_target") != "level-IV-paper-exact-end-to-end":
        fail("formalization target is not Level IV")

    actual_envs = paper_environments(text)
    indexed_envs = data.get("environments")
    if not isinstance(indexed_envs, list) or len(indexed_envs) != len(actual_envs):
        fail("environment count mismatch")
    if len(actual_envs) != 45 or data.get("environment_count") != 45:
        fail(f"expected 45 paper environments, found {len(actual_envs)}")
    for actual, indexed in zip(actual_envs, indexed_envs, strict=True):
        for key in (
            "anchor_id", "display_label", "title", "section", "line", "position",
            "claim_id", "planned_lean_declaration", "planned_lean_module",
            "planned_lean_file",
        ):
            if indexed.get(key) != actual[key]:
                fail(f"environment {key} mismatch at {actual['display_label']}")
        if final:
            if indexed.get("status") != "exact-proved":
                fail(f"environment is not exact-proved: {actual['display_label']}")
            for key in (
                "actual_lean_declaration", "actual_lean_module", "actual_lean_file"
            ):
                if not indexed.get(key):
                    fail(f"final environment lacks {key}: {actual['display_label']}")
        elif indexed.get("status") != "planned":
            fail(f"source-freeze environment is not planned: {actual['display_label']}")

    planned_declarations = [env["planned_lean_declaration"] for env in indexed_envs]
    if len(planned_declarations) != len(set(planned_declarations)):
        fail("planned Lean declarations are not unique")

    actual_eqs = paper_equations(text, actual_envs)
    indexed_eqs = data.get("equations")
    if not isinstance(indexed_eqs, list) or len(indexed_eqs) != len(actual_eqs):
        fail("equation count mismatch")
    if len(actual_eqs) != 42 or data.get("equation_count") != 42:
        fail(f"expected 42 labeled equations, found {len(actual_eqs)}")
    for actual, indexed in zip(actual_eqs, indexed_eqs, strict=True):
        for key in (
            "equation_id", "section", "nearest_environment_anchor",
            "nearest_environment_label", "line", "position", "preview",
            "planned_covering_declaration",
        ):
            if indexed.get(key) != actual[key]:
                fail(f"equation {key} mismatch at {actual['equation_id']}")
        if final:
            if indexed.get("status") not in {
                "covered-by-environment", "covered-by-main-endpoint"
            }:
                fail(f"final equation lacks coverage: {actual['equation_id']}")
            if not indexed.get("actual_covering_declaration"):
                fail(f"final equation lacks covering declaration: {actual['equation_id']}")
        elif indexed.get("status") not in {"planned-coverage", "planned-main-endpoint"}:
            fail(f"source-freeze equation has invalid status: {actual['equation_id']}")

    contract = data.get("formalization_contract_sha256")
    if final:
        if data.get("lifecycle") != "level-IV-final":
            fail("final index lifecycle must be level-IV-final")
        if not isinstance(contract, str) or not SHA_RE.fullmatch(contract):
            fail("final index lacks a valid Contract SHA-256")
    else:
        if data.get("lifecycle") != "pre-formalization-source-freeze":
            fail("source-freeze lifecycle is incorrect")
        if data.get("formalization_status") != "not-started":
            fail("source-freeze must report formalization as not-started")
        if contract is not None:
            fail("source-freeze must not claim a Contract SHA-256")


def validate_anchor_manifest(text: str, data: dict[str, object]) -> None:
    expected = build_anchor_manifest(text)
    if data != expected:
        fail("anchor-manifest.json is not the deterministic source inventory")
    if data.get("anchor_count") != 65:
        fail(f"expected 65 anchors, found {data.get('anchor_count')}")
    ids = [item["anchor_id"] for item in data["anchors"]]
    duplicates = [key for key, count in Counter(ids).items() if count > 1]
    if duplicates:
        fail(f"duplicate anchor IDs: {duplicates}")


def render_markdown(data: dict[str, object]) -> str:
    lines = [
        "# Formalization Planning Index",
        "",
        "This index freezes the paper-facing statement inventory before Lean work starts.",
        "It records planned declaration names only and makes no proof-completion claim.",
        "",
        f"- Freeze: `{data['freeze_id']}`",
        f"- Canonical source: `{data['canonical_source']}`",
        f"- Canonical source SHA-256: `{data['canonical_source_sha256']}`",
        f"- Formalization target: `{data['formalization_target']}`",
        "- Current formalization status: **not started**",
        f"- Paper environments: {data['environment_count']} (`planned`: {data['environment_count']}, `exact-proved`: 0)",
        f"- Labeled equations: {data['equation_count']}",
        "- Lean Contract SHA-256: **pending**",
        "",
        "Anchor IDs are the primary paper-to-Lean keys. Numeric display labels may be",
        "retained for readability, but the final ledger and Contract must use the anchors.",
        "",
        "## Planned environment correspondence",
        "",
        "| Anchor ID | Paper item | Title | Planned declaration | Planned file | Status |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for env in data["environments"]:
        lines.append(
            f"| `{env['anchor_id']}` | {env['display_label']} | {env['title']} | "
            f"`{env['planned_lean_declaration']}` | `{env['planned_lean_file']}` | "
            f"{env['status']} |"
        )
    lines.extend([
        "",
        "## Planned equation coverage",
        "",
        "| Equation ID | Section | Nearest paper item | Planned covering declaration | Status |",
        "| --- | --- | --- | --- | --- |",
    ])
    for equation in data["equations"]:
        nearest = equation["nearest_environment_label"] or "-"
        covering = equation["planned_covering_declaration"] or "-"
        lines.append(
            f"| `{equation['equation_id']}` | {equation['section']} | {nearest} | "
            f"`{covering}` | {equation['status']} |"
        )
    lines.extend([
        "",
        "## Promotion rule",
        "",
        "The index may be promoted to `level-IV-final` only after all 45 rows resolve",
        "to actual Lean declarations with exact paper statements, all equations have",
        "covering declarations, the Contract hash is fixed, and the full build and axiom",
        "audits pass. Until then, this is an inventory and plan, not a formalization claim.",
        "",
    ])
    return "\n".join(lines)


def write_json(path: Path, data: dict[str, object]) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--initialize", action="store_true")
    parser.add_argument("--refresh-source", action="store_true")
    parser.add_argument("--write-markdown", action="store_true")
    parser.add_argument("--final", action="store_true")
    args = parser.parse_args()

    text = PAPER.read_text(encoding="utf-8")
    if args.initialize:
        if INDEX.exists() or INDEX_MD.exists() or ANCHOR_MANIFEST.exists():
            fail("refusing to initialize over an existing inventory")
        write_json(INDEX, initialize_index(text))
        write_json(ANCHOR_MANIFEST, build_anchor_manifest(text))
    if args.refresh_source:
        old_data = json.loads(INDEX.read_text(encoding="utf-8"))
        if old_data.get("lifecycle") != "pre-formalization-source-freeze":
            fail("source refresh is allowed only before formalization starts")
        if any(
            env.get("status") != "planned"
            for env in old_data.get("environments", [])
        ):
            fail("source refresh would overwrite non-planning correspondence data")
        write_json(INDEX, initialize_index(text))
        write_json(ANCHOR_MANIFEST, build_anchor_manifest(text))

    data = json.loads(INDEX.read_text(encoding="utf-8"))
    anchor_data = json.loads(ANCHOR_MANIFEST.read_text(encoding="utf-8"))
    validate(text, data, final=args.final)
    validate_anchor_manifest(text, anchor_data)
    expected_markdown = render_markdown(data)
    if args.write_markdown:
        INDEX_MD.write_text(expected_markdown, encoding="utf-8")
    elif INDEX_MD.read_text(encoding="utf-8") != expected_markdown:
        fail("formalization-index.md is not the deterministic JSON rendering")

    print(f"PASS: {INDEX.name}")
    print(f"  canonical SHA-256: {data['canonical_source_sha256']}")
    print(f"  environments: {data['environment_count']} (45/45 inventoried, 0/45 proved)")
    print(f"  equations: {data['equation_count']} (planned coverage)")
    print(f"  anchors: {anchor_data['anchor_count']}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AssertionError, FileNotFoundError, json.JSONDecodeError) as exc:
        print(f"FAIL: {exc}")
        raise SystemExit(1)
