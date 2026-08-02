# Paper Freeze Manifest

- Freeze ID: `paper-rc1`
- Frozen at: `2026-08-02T07:32:08Z`
- Status: **local pre-formalization publication candidate; source and PDF frozen**
- Author: **Lior Isthmus**
- Canonical source: `no-exactly-two-dlo.md`
- Canonical SHA-256:
  `bec4c8b1b0f65495efb32e270e4bdcd5fe6ecafca0ca5744760b1630a51487f7`

## Source provenance

The immediate source was the read-only working draft
`work/two-dlo/no-exactly-two-dlo-v7.md`, SHA-256
`cbbd9862ab814c75ec6fa2de6592d7bda1cca71ac77a8af3b65a6d57214f48e5`.
The working draft itself was not modified.

The canonical publication source makes one layout-only adjustment: the
set-builder defining the graph of the cut-preimage map is written with an
`aligned` multiline body. This eliminated a 31.7 pt overfull box on PDF page
13. The rewritten display is logically equivalent; all 45 numbered
environments, all 42 equation IDs, and all mathematical conclusions are
unchanged.

Any later source edit, including an editorial edit, invalidates this source
freeze until the lint, index, build, structural PDF checks, and full visual
inspection are repeated and the hashes are updated.

## Status axes

| Axis | Status |
| --- | --- |
| paper source | **frozen as `paper-rc1`** |
| local paper build and checks | passed |
| PDF visual inspection | all 27 pages passed |
| formalization target | Level IV - paper-exact end-to-end |
| formalization actual status | **not started; 0/45 proved** |
| Lean Contract | pending; not created |
| fresh Linux paper build | not run; outside this freeze task |
| review | self-assessed with independent read-only inventory audits |
| independent human mathematical review | not claimed |
| publication | not performed |

## Freeze metrics

| Metric | Value |
| --- | ---: |
| manuscript bytes | 49,989 |
| manuscript lines | 1,582 |
| stable anchors | 65 |
| labeled equation IDs | 42 |
| numbered body equations | 41 |
| numbered environments | 45 |
| formalization rows inventoried | 45/45 |
| formalization rows proved | 0/45 |
| PDF pages | 27 |

## Artifact hashes

- generated TeX:
  `d67013ffc4399c8f0feab6ce19eca00a221e26647775024d94e0e760954553b1`
- generated PDF:
  `071538dd4b64ce74935a97e43aa974e098ef885302367f63ce6fd1062b23617b`
- formalization planning index (JSON):
  `5f733002596af3e523f05ff19fdfea7eb2fba743e01b174dec1d97357a2889ac`
- formalization planning index (Markdown):
  `9c6f739dc108a038e621222370f8a657bc5e5abce21a7625b8ac165730e57bd3`
- anchor manifest:
  `505de131f4ce64bdb33013eb4955312f3a4e021ea361aebd63be6a37b372eba2`

`SHA256SUMS` is the complete integrity list for the package. Byte-identical PDF
reproduction is not claimed; the checked-in PDF is the frozen, inspected
publication-candidate artifact.

