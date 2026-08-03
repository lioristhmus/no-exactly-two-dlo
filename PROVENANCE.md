# Provenance and authorship

Lior Isthmus is the sole author, rights holder, and maintainer of the paper and
its accompanying materials. AI systems are disclosed as tools and are not
authors or rights holders.

The exact-two paper is a companion to *No Set Carries Exactly Three Dense
Linear Orders without Endpoints*. It imports two global spectrum results and
several elementary interfaces from that work, while supplying a distinct
cut-rotation proof for the exact-two exclusion. The companion relationship and
all imported results are identified in the manuscript.

ChatGPT assisted with mathematical exploration, counterexample search,
drafting, translation, and review. Claude Code provided substantial
human-directed assistance with Lean proof exploration, code generation,
repair, and validation. OpenAI Codex assisted with statement-fidelity audits,
final repairs, release engineering, PDF inspection, and editorial checks. Lior
Isthmus chose the mathematical claims and proof route, directed the work,
reviewed and approved the frozen content, and retains responsibility for all
claims and any remaining errors.

## Frozen source and rendering

The pre-formalization `paper-rc1` package is retained byte-for-byte. The active
`paper-rc2` freeze adds only the exact-two formalization note and reference and
the expanded AI-use disclosure. Its numbered mathematical content is unchanged.

- `paper-rc1` canonical manuscript SHA-256:
  `bec4c8b1b0f65495efb32e270e4bdcd5fe6ecafca0ca5744760b1630a51487f7`
- `paper-rc2` canonical manuscript SHA-256:
  `80a53bcfa94ea0bea2116c1268a00ddbe123311f6a05f722d75657b7b5051384`
- `paper-rc2` generated TeX SHA-256:
  `d35bd5426c53fc8fc06b61c402042aa67337e1eaac43b533e63e5f6def4e9d8b`
- `paper-rc2` generated PDF SHA-256:
  `6c54500e11f7e102933e00d8d232faa6221cbd2e1c1abd91909ae9c2c320f71e`
- Lean statement Contract SHA-256:
  `0a498a649d72274885099a065f35f430a15a51c95cebca3e5daddbdd01b6a4e9`

The root manuscript, PDF, and formalization indexes are convenience copies of
the active `paper-rc2` counterparts. Public-facing README, licensing, citation,
and provenance files are mutable release wrappers and are not part of a freeze
checksum manifest. Byte-identical PDF rebuilding is not claimed; the checked-in
artifact is protected by its release checksum.

The companion Lean release gate was independently replayed from an empty
`.lake` state in an x86_64 Ubuntu 24.04 container. This clean-environment check
is distinct from hosted CI and from independent mathematical review.

## Reserved archival identifier

Zenodo has reserved version DOI
[`10.5281/zenodo.21765207`](https://doi.org/10.5281/zenodo.21765207) for the
`paper-rc2` preprint and concept DOI
[`10.5281/zenodo.21765206`](https://doi.org/10.5281/zenodo.21765206) for its
version chain. At this revision the record is still an unpublished draft; the
reserved identifiers are recorded without claiming publication.

The public Comparator passed its ordinary Challenge and Solution builds and a
local default-kernel replay. Its guarded Linux Landrun execution also passed on
hosted GitHub Actions (Ubuntu 24.04, x86_64) on 2026-08-02 UTC
([run 30768695800](https://github.com/lioristhmus/no-exactly-two-dlo-comparator/actions/runs/30768695800)).
