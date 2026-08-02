# `paper-rc2` build and inspection report

## Scope

This package freezes the post-formalization publication candidate for
*No Set Carries Exactly Two Dense Linear Orders without Endpoints*. Relative
to the byte-preserved `paper-rc1` source, it adds only a short Level IV Lean
formalization note, an exact-two Lean software reference, and a more specific
AI-use disclosure. All 45 numbered mathematical statements, all 42 labeled
equations, and their hypotheses and conclusions are unchanged.

The final correspondence index records 45/45 paper environments as
`exact-proved`, covers 42/42 labeled equations, and fixes the Lean statement
Contract SHA-256 to
`0a498a649d72274885099a065f35f430a15a51c95cebca3e5daddbdd01b6a4e9`.
The index was cross-checked against 188 declarations resolved from the Lean
environment.

## Profile and toolchain

The build snapshots the author's standard AMS/XeLaTeX profile shared with the
exact-three companion. It preserves the unnumbered abstract endpoint, so
numbered body equations begin at equation (1).

- Pandoc 3.9.0.2
- pandoc-crossref 0.3.23
- XeTeX 0.999998, TeX Live 2026/Homebrew
- Python 3.14.5
- macOS Darwin 25.5.0 arm64
- Poppler 26.05.0 for structural checks and rendering

The Pandoc default LaTeX template used at freeze time has SHA-256
`0a182e554e971eba7c7dc025fca17616c3a81d1ffaf93a84d063c873282436f1`.

## Build result

`python3 build_publication.py` completed successfully. The final XeLaTeX pass
contained no undefined references, multiply defined labels, missing
characters, unresolved control sequences, rerun requests, or overfull boxes.

The generated PDF has:

- 27 Letter-size pages, all with zero rotation;
- title and author metadata (`Lior Isthmus`);
- no encryption, JavaScript, forms, or embedded files;
- 10 font resources, all embedded and subset, with Unicode maps;
- right-side equation numbering beginning at equation (1);
- five external link annotations and 48 internal link annotations.

Text extraction produced 40,192 Unicode characters with no replacement or NUL
characters. It contains the title, the final Lean endpoint, Theorem 6.1, both
appendices, the AI-use disclosure, and the final reference.

All 27 pages were rendered and inspected. The title block, abstract, contents,
running heads, page numbers, equations, tables, proof-end squares, appendices,
formalization note, AI-use disclosure, and references show no clipping,
overlap, unintended blank page, or missing glyph. Pages 3 and 27 were also
inspected at high resolution.

## Structural, source, and correspondence checks

- canonical manuscript: 51,166 bytes and 1,595 lines;
- stable anchors: 66, all unique;
- labeled equation IDs: 42, all unique and covered by Lean declarations;
- numbered paper environments: 45, with no gaps or duplicates;
- formalization mapping: 45/45 `exact-proved`;
- Lean declaration probe: 188/188 resolved;
- internal links and numbered references: all resolved;
- proof blocks and proof-end squares: 36/36;
- canonical manuscript lint: pass;
- final index and anchor manifest check: pass;
- Lean ledger cross-check against the final paper index: pass.

Four already published external destinations resolved during the release
inspection: the exact-three paper DOI and GitHub repository, and the
exact-three Lean DOI and GitHub repository. The fifth destination is the
reserved exact-two Lean GitHub URL; it remains pending until that repository is
published.

The PDF checksum identifies the inspected freeze artifact. Byte-identical PDF
reproduction is not claimed, even on the same host and toolchain. The checksum,
lint, final-index, and root-copy checks were replayed successfully in a
read-only, network-disabled `python:3.12-slim-bookworm` container (digest
`sha256:d50fb7611f86d04a3b0471b46d7557818d88983fc3136726336b2a4c657aa30b`).
That run verifies the frozen package but does not rebuild the PDF. Public Git
hosting, DOI registration, and independent human mathematical review remain
separate release axes.
