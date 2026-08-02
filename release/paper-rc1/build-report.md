# `paper-rc1` build and inspection report

## Scope

This package freezes the exact-two manuscript immediately before Lean
formalization begins. No exact-two Lean files were created, edited, or built in
this task. The planning index inventories all 45 numbered paper environments
and 42 labeled equations, but records 45 planned declarations, 0 proved
declarations, and no Contract hash.

The canonical source was prepared from the audited `no-exactly-two-dlo-v7.md`
working draft. The first PDF build exposed one 31.7 pt overfull box in the
set-builder for the cut-preimage graph. The publication source rewrites only
that display into an equivalent multiline `aligned` form. The read-only v7
draft and the mathematical content were not changed.

## Profile

The build snapshots the author's standard AMS/XeLaTeX profile, shared with the
exact-three companion. The release-local compatibility pass is limited to the
existing top matter and heading hierarchy. It preserves the unnumbered abstract
endpoint, so numbered body equations begin at equation (1).

## Toolchain

- Pandoc 3.9.0.2
- pandoc-crossref 0.3.23
- XeTeX 0.999998, TeX Live 2026/Homebrew
- Python 3.14.5
- macOS Darwin 25.5.0 arm64
- Poppler 26.05.0 for structural checks and rendering

The Pandoc default LaTeX template used at freeze time has SHA-256
`0a182e554e971eba7c7dc025fca17616c3a81d1ffaf93a84d063c873282436f1`.

## Build result

`python3 build_publication.py` completed successfully. The third and final
XeLaTeX pass contained no undefined references, multiply-defined labels,
missing characters, unresolved control sequences, rerun requests, or overfull
boxes.

The generated PDF has:

- 27 Letter-size pages, all with zero rotation;
- title and author metadata (`Lior Isthmus`);
- no encryption, JavaScript, forms, or embedded files;
- 10 font resources, all embedded and subset, with Unicode maps;
- right-side equation numbering beginning at equation (1);
- four external link annotations, matching the four manuscript URLs.

Text extraction produced 48,591 Unicode characters with no replacement or NUL
characters. It contains the title, Theorem 6.1, both appendices, the AI-use
disclosure, and the final reference.

All 27 pages were rendered at 150 dpi and inspected. The title block, abstract,
contents, alternating running heads, page numbers, equations, tables,
proof-end squares, appendices, AI-use disclosure, and references show no
clipping, overlap, unintended blank page, or missing glyph. Page 13 was also
inspected at full resolution after the multiline repair.

## Structural, source, and link checks

- canonical manuscript: 49,989 bytes and 1,582 lines;
- stable anchors: 65, all unique;
- labeled equation IDs: 42, all unique;
- numbered paper environments: 45, with no gaps or duplicates;
- internal links and numbered references: all resolved;
- proof blocks and proof-end squares: 36/36;
- canonical manuscript lint: pass;
- planning index and anchor manifest check: pass;
- external references: 4/4 resolved with HTTP 200.

Resolved external destinations:

- exact-three paper DOI to `https://zenodo.org/records/21735262`;
- exact-three paper GitHub repository;
- exact-three Lean GitHub repository;
- exact-three Lean DOI to `https://zenodo.org/records/21729423`.

The PDF checksum identifies the inspected freeze artifact. Byte-identical PDF
reproduction is not claimed, even on the same host and toolchain. Fresh Linux
paper reproduction, Lean formalization, Git operations, and publication are
outside the scope of this freeze.

