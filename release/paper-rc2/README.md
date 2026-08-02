# Paper freeze `paper-rc2`

This directory is the post-formalization publication candidate for
*No Set Carries Exactly Two Dense Linear Orders without Endpoints* by
Lior Isthmus.

The versionless canonical manuscript is `no-exactly-two-dlo.md`. Relative to
the preserved `paper-rc1` source, it adds only a Level IV Lean formalization
note, an exact-two Lean software reference, and an expanded AI-use disclosure.
All 45 numbered mathematical statements and 42 labeled equations are unchanged.

The formalization index is final rather than provisional: every numbered paper
item is mapped to an actual paper-exact Lean declaration, all equations have
covering declarations, and the Contract SHA-256 is fixed. The final syntactic
endpoint is:

```lean
ExactTwoDLO.FO.zsep_proves_not_spec2Sentence :
  Provable Zsep (∼ spec2Sentence)
```

The public Lean repository is staged at
`https://github.com/lioristhmus/no-exactly-two-dlo-lean`; at the time of this
local freeze, its GitHub publication and software DOI are still pending.

## Artifacts

- `no-exactly-two-dlo.md`: canonical frozen manuscript;
- `build/no-exactly-two-dlo.tex`: generated TeX;
- `build/no-exactly-two-dlo.pdf`: inspected 27-page PDF;
- `formalization-index.{md,json}`: final 45/45 correspondence;
- `anchor-manifest.json`: complete source-anchor inventory;
- `PAPER-FREEZE.{md,json}`: freeze records;
- `build-report.md`: build, PDF, and link verification report;
- `SHA256SUMS`: complete package integrity list.

## Build

Required tools are Python 3, Pandoc, `pandoc-crossref`, and XeLaTeX. Run:

```bash
python3 build_publication.py
```

The build performs Pandoc conversion followed by three XeLaTeX passes. The
final pass rejects undefined references, multiply-defined labels, missing
characters, unresolved control sequences, rerun requests, and overfull boxes.

## Verify

Verify the frozen artifacts without rebuilding:

```bash
shasum -a 256 -c SHA256SUMS
python3 lint_paper.py
python3 check_formalization_index.py --final
```

Byte-identical PDF reproduction is not claimed. The PDF named by
`SHA256SUMS` is the artifact that passed the recorded structural and all-pages
visual inspection.
