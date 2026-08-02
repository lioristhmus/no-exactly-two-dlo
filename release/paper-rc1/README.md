# Paper freeze `paper-rc1`

This directory is the pre-formalization publication candidate for
*No Set Carries Exactly Two Dense Linear Orders without Endpoints* by
Lior Isthmus.

The canonical manuscript has the versionless filename
`no-exactly-two-dlo.md`. It was prepared from the audited working draft
`work/two-dlo/no-exactly-two-dlo-v7.md` and differs from that draft only by an
equivalent multiline typesetting of the cut-preimage set-builder formula on
page 13. The numbered mathematical statements, equation IDs, proof text, and
conclusions are unchanged.

This freeze precedes all exact-two Lean work. The included formalization index
is a planning inventory: all 45 numbered environments are marked `planned`,
none is marked proved, and no Lean Contract exists yet. It must not be cited as
evidence that the paper has been formalized.

The generated TeX and PDF use the same AMS mathematical-preprint profile as
the exact-three companion:

- `amsart`, 11pt, Letter paper;
- XeLaTeX;
- equation numbers on the right (`reqno`);
- alternating author and short-title running heads;
- right-aligned hollow proof-end squares;
- portable support for `\nhookrightarrow`;
- stable manual-reference anchors.

The canonical Markdown is the source of record. A temporary compatibility
pass promotes the visible title, subtitle, and author to Pandoc metadata,
shifts the remaining heading hierarchy by one level, and keeps the headline
abstract display anchored but unnumbered. It does not rewrite the canonical
source.

## Artifacts

- `no-exactly-two-dlo.md`: canonical frozen manuscript;
- `build/no-exactly-two-dlo.tex`: generated TeX;
- `build/no-exactly-two-dlo.pdf`: inspected 27-page PDF;
- `formalization-index.{md,json}`: pre-Lean planning inventory;
- `anchor-manifest.json`: complete paper anchor inventory;
- `PAPER-FREEZE.{md,json}`: human- and machine-readable freeze records;
- `build-report.md`: build, PDF, and link verification report;
- `SHA256SUMS`: package integrity list.

## Build

Required commands:

- Python 3;
- Pandoc;
- `pandoc-crossref` built for the installed Pandoc version;
- XeLaTeX with the standard TeX Live packages used by `amsart`.

Run:

```bash
python3 build_publication.py
```

The build performs Pandoc conversion followed by three XeLaTeX passes and
writes the TeX and PDF under `build/`. Undefined references, multiply-defined
labels, missing characters, unresolved control sequences, rerun requests, and
overfull boxes are treated as fatal in the final pass.

## Verify

Verify the checked-in artifacts before rebuilding:

```bash
shasum -a 256 -c SHA256SUMS
python3 lint_paper.py
python3 check_formalization_index.py
```

Byte-identical PDF reproduction is not claimed, even on the same host and
toolchain. Running the build may therefore replace the frozen PDF with another
successfully generated 27-page file having a different checksum. The PDF
identified by `SHA256SUMS` is the artifact that passed the all-pages visual and
structural inspection recorded here.

