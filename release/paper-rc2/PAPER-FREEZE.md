# Paper Freeze Manifest

- Freeze ID: `paper-rc2`
- Frozen at: `2026-08-02T18:12:07Z`
- Status: **local post-formalization publication candidate; source and PDF frozen**
- Author: **Lior Isthmus**
- Canonical source: `no-exactly-two-dlo.md`
- Canonical SHA-256:
  `80a53bcfa94ea0bea2116c1268a00ddbe123311f6a05f722d75657b7b5051384`

## Source provenance

`paper-rc2` succeeds the byte-preserved pre-formalization freeze `paper-rc1`.
It adds a short exact-two Lean formalization note, the corresponding software
reference, and a tool-specific AI-use disclosure. The 45 numbered mathematical
statements, 42 labeled equations, hypotheses, and conclusions are unchanged.

The canonical source still contains the layout-only multiline rendering of the
cut-preimage graph introduced in `paper-rc1`. The original working draft
`work/two-dlo/no-exactly-two-dlo-v7.md` remains unmodified.

Any later source edit invalidates this freeze until the lint, Level IV index,
Lean ledger cross-check, PDF build, structural checks, full visual inspection,
and hashes are repeated.

## Status axes

| Axis | Status |
| --- | --- |
| paper source | **frozen as `paper-rc2`** |
| formalization | **Level IV; 45/45 exact-proved** |
| Lean Contract | `0a498a649d72274885099a065f35f430a15a51c95cebca3e5daddbdd01b6a4e9` |
| local paper build and checks | passed |
| PDF visual inspection | all 27 pages passed |
| Lean ledger cross-check | 45 rows and 188 declarations passed |
| clean Linux frozen-package check | **passed in a read-only, network-disabled container** |
| independent human mathematical review | not claimed |
| publication | not performed |

## Freeze metrics

| Metric | Value |
| --- | ---: |
| manuscript bytes | 51,166 |
| manuscript lines | 1,595 |
| stable anchors | 66 |
| labeled equation IDs | 42 |
| numbered body equations | 41 |
| numbered environments | 45 |
| formalization rows proved | 45/45 |
| equation coverage | 42/42 |
| PDF pages | 27 |

## Artifact hashes

- generated TeX:
  `d35bd5426c53fc8fc06b61c402042aa67337e1eaac43b533e63e5f6def4e9d8b`
- generated PDF:
  `6c54500e11f7e102933e00d8d232faa6221cbd2e1c1abd91909ae9c2c320f71e`
- formalization index (JSON):
  `29aa8c82b05780e6c8ed072692cd5d310ca48006b394a9eb944955f04309ed1a`
- formalization index (Markdown):
  `3fbf92b19868934f4cc387213235a8d96306b8d605a302d1dbdc7869a99f3905`
- anchor manifest:
  `321bfbf40ce7fe8c9d4e7c8f0587a5d44d0de7c04d743ee698386a131031776a`

`SHA256SUMS` is the complete integrity list for this freeze. Byte-identical PDF
reproduction is not claimed; the checked-in PDF is the artifact that passed the
recorded all-pages inspection.

The frozen package checks were independently replayed in the read-only,
network-disabled container image `python:3.12-slim-bookworm` (digest
`sha256:d50fb7611f86d04a3b0471b46d7557818d88983fc3136726336b2a4c657aa30b`).
This verifies checksums, lint, the final correspondence index, and the root
convenience copies; it is not a Linux PDF rebuild.
