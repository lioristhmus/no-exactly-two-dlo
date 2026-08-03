# No Set Carries Exactly Two Dense Linear Orders without Endpoints

**Lior Isthmus** ([ORCID 0009-0004-7908-9876](https://orcid.org/0009-0004-7908-9876))

This repository is the release package for the preprint *No Set Carries
Exactly Two Dense Linear Orders without Endpoints: A Cut-Rotation Proof in a
Weak Zermelo Theory without Choice or Replacement*.

The main result is the first-order derivability statement

\[
Z_{\mathrm{sep}} \vdash \neg\exists X\,(s(X)=2),
\]

where \(s(X)=2\) means that the same carrier \(X\) supports exactly two
isomorphism classes of dense linear orders without endpoints.

## Read the paper

- [PDF](no-exactly-two-dlo.pdf)
- [Canonical Markdown source](no-exactly-two-dlo.md)
- [Paper-to-Lean correspondence](formalization-index.md)

The active freeze is [`paper-rc2`](release/paper-rc2). The four files at the
repository root are convenience copies of its manuscript, PDF, and
formalization indexes. The byte-preserved pre-formalization freeze
[`paper-rc1`](release/paper-rc1) is retained for provenance. Relative to
`paper-rc1`, `paper-rc2` adds only a Lean formalization note, an exact-two Lean
software reference, and a more specific AI-use disclosure; all 45 numbered
mathematical statements and 42 labeled equations are unchanged.

## Lean formalization

The companion formalization repository is publicly available at
[`lioristhmus/no-exactly-two-dlo-lean`](https://github.com/lioristhmus/no-exactly-two-dlo-lean).
It contains a Level IV (paper-exact end-to-end) formalization: all 45 numbered
paper items are represented, all 42 labeled equations are covered, and the
final syntactic endpoint is

```lean
ExactTwoDLO.FO.zsep_proves_not_spec2Sentence :
  Provable Zsep (∼ spec2Sentence)
```

The development reuses the frozen public exact-three formalization as a pinned
read-only dependency and adds the exact-two cut-rotation argument. The complete
release gate has also been replayed from an empty `.lake` state in a fresh
x86_64 Ubuntu 24.04 container. Formalization, local verification,
clean-environment reproducibility, and independent review are reported as
separate axes.

A separate public [Comparator repository](https://github.com/lioristhmus/no-exactly-two-dlo-comparator)
checks statement identity and permitted axioms; its ordinary Challenge and
Solution builds and default-kernel replay passed. Its guarded Linux Landrun job
also passed on hosted GitHub Actions (Ubuntu 24.04, x86_64) for the final
Comparator commit on 2026-08-03 UTC
([run 30775019145](https://github.com/lioristhmus/no-exactly-two-dlo-comparator/actions/runs/30775019145));
Project Diderot submission and a Formal Verification certificate remain pending.

## Verify the active frozen package

From `release/paper-rc2`:

```bash
shasum -a 256 -c SHA256SUMS
python3 lint_paper.py
python3 check_formalization_index.py --final
```

The checked-in PDF is the artifact that passed the recorded structural,
font-embedding, text-extraction, and all-pages visual inspection. Byte-identical
PDF rebuilding is not claimed.

## Publication status

The `paper-rc2` source, PDF, and correspondence index are frozen. The paper is
published on Zenodo under version DOI
[`10.5281/zenodo.21765207`](https://doi.org/10.5281/zenodo.21765207) and as the
[`paper-rc2` GitHub Release](https://github.com/lioristhmus/no-exactly-two-dlo/releases/tag/paper-rc2).
The companion Lean `v1.0.0` release is archived under software DOI
[`10.5281/zenodo.21765391`](https://doi.org/10.5281/zenodo.21765391).
Project Diderot submission and a Formal Verification certificate remain pending.

## License and provenance

The paper and scholarly documentation are licensed under
[CC BY 4.0](LICENSE-CC-BY-4.0.md). Build and validation scripts are licensed
under [Apache-2.0](LICENSE-APACHE-2.0). The exact scope is stated in
[`LICENSE`](LICENSE). AI-assisted work is disclosed in
[`PROVENANCE.md`](PROVENANCE.md); AI systems are not authors or rights holders.
