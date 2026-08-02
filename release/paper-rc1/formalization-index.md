# Formalization Planning Index

This index freezes the paper-facing statement inventory before Lean work starts.
It records planned declaration names only and makes no proof-completion claim.

- Freeze: `paper-rc1`
- Canonical source: `no-exactly-two-dlo.md`
- Canonical source SHA-256: `bec4c8b1b0f65495efb32e270e4bdcd5fe6ecafca0ca5744760b1630a51487f7`
- Formalization target: `level-IV-paper-exact-end-to-end`
- Current formalization status: **not started**
- Paper environments: 45 (`planned`: 45, `exact-proved`: 0)
- Labeled equations: 42
- Lean Contract SHA-256: **pending**

Anchor IDs are the primary paper-to-Lean keys. Numeric display labels may be
retained for readability, but the final ledger and Contract must use the anchors.

## Planned environment correspondence

| Anchor ID | Paper item | Title | Planned declaration | Planned file | Status |
| --- | --- | --- | --- | --- | --- |
| `thm:intro-reduction` | Theorem 1.1 | Exact-two structural reduction | `ExactTwoDLO.Paper.theorem_1_1` | `NoExactlyTwoDlo/Paper/Intro.lean` | planned |
| `thm:intro-cut-reversal` | Theorem 1.2 | Cut-preimage reversal | `ExactTwoDLO.Paper.theorem_1_2` | `NoExactlyTwoDlo/Paper/Intro.lean` | planned |
| `def:2-1-base-theory` | Definition 2.1 | The base theory | `ExactTwoDLO.Paper.definition_2_1` | `NoExactlyTwoDlo/Paper/Section2.lean` | planned |
| `def:2-2-spectrum` | Definition 2.2 | Finite spectrum formulas | `ExactTwoDLO.Paper.definition_2_2` | `NoExactlyTwoDlo/Paper/Section2.lean` | planned |
| `def:2-3-order-notation` | Definition 2.3 | Order notation | `ExactTwoDLO.Paper.definition_2_3` | `NoExactlyTwoDlo/Paper/Section2.lean` | planned |
| `thm:2-4-subcountable-uniqueness` | Theorem 2.4 | At-most-countable DLO uniqueness | `ExactTwoDLO.Paper.theorem_2_4` | `NoExactlyTwoDlo/Paper/Section2.lean` | planned |
| `thm:2-5-dedekind-alternative` | Theorem 2.5 | Dedekind-infinite four-type alternative | `ExactTwoDLO.Paper.theorem_2_5` | `NoExactlyTwoDlo/Paper/Section2.lean` | planned |
| `lem:2-6-automorphism-orbit` | Lemma 2.6 | A nontrivial increasing automorphism gives a countable orbit | `ExactTwoDLO.Paper.lemma_2_6` | `NoExactlyTwoDlo/Paper/Section2.lean` | planned |
| `cor:2-7-common-host` | Corollary 2.7 | Common-host self-duality criterion | `ExactTwoDLO.Paper.corollary_2_7` | `NoExactlyTwoDlo/Paper/Section2.lean` | planned |
| `lem:2-8-rigidity-convex` | Lemma 2.8 | Rigidity and reversals on convex suborders | `ExactTwoDLO.Paper.lemma_2_8` | `NoExactlyTwoDlo/Paper/Section2.lean` | planned |
| `lem:3-1-not-subcountable` | Lemma 3.1 | An exact-two carrier is not at most countable | `ExactTwoDLO.Paper.lemma_3_1` | `NoExactlyTwoDlo/Paper/Section3.lean` | planned |
| `lem:3-2-not-dedekind-infinite` | Lemma 3.2 | An exact-two carrier is not Dedekind-infinite | `ExactTwoDLO.Paper.lemma_3_2` | `NoExactlyTwoDlo/Paper/Section3.lean` | planned |
| `lem:3-3-rigidity` | Lemma 3.3 | Every exact-two DLO is rigid | `ExactTwoDLO.Paper.lemma_3_3` | `NoExactlyTwoDlo/Paper/Section3.lean` | planned |
| `lem:3-4-hereditary-dedekind` | Lemma 3.4 | Hereditary Dedekind-finiteness | `ExactTwoDLO.Paper.lemma_3_4` | `NoExactlyTwoDlo/Paper/Section3.lean` | planned |
| `def:3-5-reversal-action` | Definition 3.5 | Reversal action on the two types | `ExactTwoDLO.Paper.definition_3_5` | `NoExactlyTwoDlo/Paper/Section3.lean` | planned |
| `lem:3-6-all-selfdual-flank` | Lemma 3.6 | Symmetric flank localization when all global types are self-dual | `ExactTwoDLO.Paper.lemma_3_6` | `NoExactlyTwoDlo/Paper/Section3.lean` | planned |
| `prop:3-7-all-selfdual-dichotomy` | Proposition 3.7 | All-self-dual rigid carrier dichotomy | `ExactTwoDLO.Paper.proposition_3_7` | `NoExactlyTwoDlo/Paper/Section3.lean` | planned |
| `thm:3-8-residual-normal-form` | Theorem 3.8 | Exact-two residual normal form | `ExactTwoDLO.Paper.theorem_3_8` | `NoExactlyTwoDlo/Paper/Section3.lean` | planned |
| `def:4-1-cut-square` | Definition 4.1 | The antipodal cut square | `ExactTwoDLO.Paper.definition_4_1` | `NoExactlyTwoDlo/Paper/Section4.lean` | planned |
| `lem:4-2-cut-square-actual` | Lemma 4.2 | The cut square is actual and antipodal | `ExactTwoDLO.Paper.lemma_4_2` | `NoExactlyTwoDlo/Paper/Section4.lean` | planned |
| `lem:4-3-antipodal-coloring` | Lemma 4.3 | Antipodal two-color square | `ExactTwoDLO.Paper.lemma_4_3` | `NoExactlyTwoDlo/Paper/Section4.lean` | planned |
| `lem:4-4-selfdual-amalgamation` | Lemma 4.4 | Two rigid self-dual DLOs and one point self-dualize their union | `ExactTwoDLO.Paper.lemma_4_4` | `NoExactlyTwoDlo/Paper/Section4.lean` | planned |
| `thm:4-5-vertical-exclusion` | Theorem 4.5 | A vertical monochromatic cut edge is impossible | `ExactTwoDLO.Paper.theorem_4_5` | `NoExactlyTwoDlo/Paper/Section4.lean` | planned |
| `thm:4-6-cut-rotation-type` | Theorem 4.6 | Every cut rotation has the original type | `ExactTwoDLO.Paper.theorem_4_6` | `NoExactlyTwoDlo/Paper/Section4.lean` | planned |
| `def:5-1-cut-preimage` | Definition 5.1 | The cut-preimage map | `ExactTwoDLO.Paper.definition_5_1` | `NoExactlyTwoDlo/Paper/Section5.lean` | planned |
| `lem:5-2-ray-exchange` | Lemma 5.2 | Cut rotations exchange opposite rays | `ExactTwoDLO.Paper.lemma_5_2` | `NoExactlyTwoDlo/Paper/Section5.lean` | planned |
| `lem:5-3-delta-injective` | Lemma 5.3 | The cut-preimage map is injective | `ExactTwoDLO.Paper.lemma_5_3` | `NoExactlyTwoDlo/Paper/Section5.lean` | planned |
| `lem:5-4-delta-decreasing` | Lemma 5.4 | The cut-preimage map is strictly decreasing | `ExactTwoDLO.Paper.lemma_5_4` | `NoExactlyTwoDlo/Paper/Section5.lean` | planned |
| `cor:5-5-delta-bijective` | Corollary 5.5 | The cut-preimage map is a decreasing bijection | `ExactTwoDLO.Paper.corollary_5_5` | `NoExactlyTwoDlo/Paper/Section5.lean` | planned |
| `thm:5-6-cut-rotation-selfduality` | Theorem 5.6 | Cut-rotation self-duality theorem | `ExactTwoDLO.Paper.theorem_5_6` | `NoExactlyTwoDlo/Paper/Section5.lean` | planned |
| `thm:6-1-main` | Theorem 6.1 | No exact-two DLO spectrum | `ExactTwoDLO.Paper.theorem_6_1` | `NoExactlyTwoDlo/Paper/Section6.lean` | planned |
| `cor:6-2-two-three-gap` | Corollary 6.2 | No exact two or exact three | `ExactTwoDLO.Paper.corollary_6_2` | `NoExactlyTwoDlo/Paper/Section6.lean` | planned |
| `cor:6-3-zf` | Corollary 6.3 | ZF consequence | `ExactTwoDLO.Paper.corollary_6_3` | `NoExactlyTwoDlo/Paper/Section6.lean` | planned |
| `prop:a-1-cut-relations` | Proposition A.1 | Uniform formation of the cut rotations | `ExactTwoDLO.Paper.proposition_A_1` | `NoExactlyTwoDlo/Paper/AppendixA.lean` | planned |
| `prop:a-2-cut-table` | Proposition A.2 | The finite type table requires no Choice | `ExactTwoDLO.Paper.proposition_A_2` | `NoExactlyTwoDlo/Paper/AppendixA.lean` | planned |
| `prop:a-3-delta-graph` | Proposition A.3 | The cut-preimage graph uses no Replacement | `ExactTwoDLO.Paper.proposition_A_3` | `NoExactlyTwoDlo/Paper/AppendixA.lean` | planned |
| `prop:a-4-composites` | Proposition A.4 | The ray composites are internal maps | `ExactTwoDLO.Paper.proposition_A_4` | `NoExactlyTwoDlo/Paper/AppendixA.lean` | planned |
| `lem:b-1-reflection-split` | Lemma B.1 | Geometry of one reflection split | `ExactTwoDLO.Paper.lemma_B_1` | `NoExactlyTwoDlo/Paper/AppendixB.lean` | planned |
| `lem:b-2-singleton-placement` | Lemma B.2 | Sharp singleton placement | `ExactTwoDLO.Paper.lemma_B_2` | `NoExactlyTwoDlo/Paper/AppendixB.lean` | planned |
| `lem:b-3-child-localization` | Lemma B.3 | All-self-dual finite localization | `ExactTwoDLO.Paper.lemma_B_3` | `NoExactlyTwoDlo/Paper/AppendixB.lean` | planned |
| `def:b-4-level-state` | Definition B.4 | Complete dyadic level states | `ExactTwoDLO.Paper.definition_B_4` | `NoExactlyTwoDlo/Paper/AppendixB.lean` | planned |
| `thm:b-5-tree-actualization` | Theorem B.5 | Type-count-free dyadic actualization | `ExactTwoDLO.Paper.theorem_B_5` | `NoExactlyTwoDlo/Paper/AppendixB.lean` | planned |
| `lem:b-6-center-countability` | Lemma B.6 | The center set is at most countable | `ExactTwoDLO.Paper.lemma_B_6` | `NoExactlyTwoDlo/Paper/AppendixB.lean` | planned |
| `thm:b-7-off-center` | Theorem B.7 | An off-center point generates an injective sequence | `ExactTwoDLO.Paper.theorem_B_7` | `NoExactlyTwoDlo/Paper/AppendixB.lean` | planned |
| `cor:b-8-dyadic-dichotomy` | Corollary B.8 | Type-count-free rigid carrier dichotomy | `ExactTwoDLO.Paper.corollary_B_8` | `NoExactlyTwoDlo/Paper/AppendixB.lean` | planned |

## Planned equation coverage

| Equation ID | Section | Nearest paper item | Planned covering declaration | Status |
| --- | --- | --- | --- | --- |
| `eq:abstract-main` | Abstract | - | `ExactTwoDLO.FO.zsep_proves_not_spec2Sentence` | planned-main-endpoint |
| `eq:finite-spectrum-formula` | 2. Formal setting and imported results | Definition 2.2 | `ExactTwoDLO.Paper.definition_2_2` | planned-coverage |
| `eq:subcountable-uniqueness` | 2. Formal setting and imported results | Theorem 2.4 | `ExactTwoDLO.Paper.theorem_2_4` | planned-coverage |
| `eq:dedekind-alternative` | 2. Formal setting and imported results | Theorem 2.5 | `ExactTwoDLO.Paper.theorem_2_5` | planned-coverage |
| `eq:automorphism-orbit` | 2. Formal setting and imported results | Lemma 2.6 | `ExactTwoDLO.Paper.lemma_2_6` | planned-coverage |
| `eq:common-host` | 2. Formal setting and imported results | Corollary 2.7 | `ExactTwoDLO.Paper.corollary_2_7` | planned-coverage |
| `eq:all-selfdual-flank` | 3. Exact-two structural reduction | Lemma 3.6 | `ExactTwoDLO.Paper.lemma_3_6` | planned-coverage |
| `eq:exact-two-residual` | 3. Exact-two structural reduction | Theorem 3.8 | `ExactTwoDLO.Paper.theorem_3_8` | planned-coverage |
| `eq:cut-rotation` | 4. The one-point cut square | Definition 4.1 | `ExactTwoDLO.Paper.definition_4_1` | planned-coverage |
| `eq:cut-square-antipodal` | 4. The one-point cut square | Lemma 4.2 | `ExactTwoDLO.Paper.lemma_4_2` | planned-coverage |
| `eq:selfdual-amalgamation-map` | 4. The one-point cut square | Lemma 4.4 | `ExactTwoDLO.Paper.lemma_4_4` | planned-coverage |
| `eq:all-cut-rotations` | 4. The one-point cut square | Theorem 4.6 | `ExactTwoDLO.Paper.theorem_4_6` | planned-coverage |
| `eq:hereditary-dedekind-finiteness` | 5. The cut-preimage reversal | Theorem 4.6 | `ExactTwoDLO.Paper.theorem_4_6` | planned-coverage |
| `eq:rotation-hypothesis` | 5. The cut-preimage reversal | Theorem 4.6 | `ExactTwoDLO.Paper.theorem_4_6` | planned-coverage |
| `eq:cut-preimage` | 5. The cut-preimage reversal | Definition 5.1 | `ExactTwoDLO.Paper.definition_5_1` | planned-coverage |
| `eq:cut-preimage-graph` | 5. The cut-preimage reversal | Definition 5.1 | `ExactTwoDLO.Paper.definition_5_1` | planned-coverage |
| `eq:left-to-right-ray` | 5. The cut-preimage reversal | Lemma 5.2 | `ExactTwoDLO.Paper.lemma_5_2` | planned-coverage |
| `eq:right-to-left-ray` | 5. The cut-preimage reversal | Lemma 5.2 | `ExactTwoDLO.Paper.lemma_5_2` | planned-coverage |
| `eq:delta-decreasing` | 5. The cut-preimage reversal | Lemma 5.4 | `ExactTwoDLO.Paper.lemma_5_4` | planned-coverage |
| `eq:proper-ray-selfmap` | 5. The cut-preimage reversal | Lemma 5.4 | `ExactTwoDLO.Paper.lemma_5_4` | planned-coverage |
| `eq:proper-ray-selfmap-range` | 5. The cut-preimage reversal | Lemma 5.4 | `ExactTwoDLO.Paper.lemma_5_4` | planned-coverage |
| `eq:delta-anti-isomorphism` | 5. The cut-preimage reversal | Theorem 5.6 | `ExactTwoDLO.Paper.theorem_5_6` | planned-coverage |
| `eq:main-theorem` | 6. Exact-two exclusion | Theorem 6.1 | `ExactTwoDLO.Paper.theorem_6_1` | planned-coverage |
| `eq:two-three-gap` | 6. Exact-two exclusion | Corollary 6.2 | `ExactTwoDLO.Paper.corollary_6_2` | planned-coverage |
| `eq:typefree-singleton-placement` | Appendix B. A type-count-free dyadic reflection engine | Lemma B.2 | `ExactTwoDLO.Paper.lemma_B_2` | planned-coverage |
| `eq:typefree-root-decomposition` | Appendix B. A type-count-free dyadic reflection engine | Lemma B.2 | `ExactTwoDLO.Paper.lemma_B_2` | planned-coverage |
| `eq:typefree-child-selfdual` | Appendix B. A type-count-free dyadic reflection engine | Lemma B.3 | `ExactTwoDLO.Paper.lemma_B_3` | planned-coverage |
| `eq:typefree-remaining-cell-ranking` | Appendix B. A type-count-free dyadic reflection engine | Lemma B.3 | `ExactTwoDLO.Paper.lemma_B_3` | planned-coverage |
| `eq:typefree-localized-complement` | Appendix B. A type-count-free dyadic reflection engine | Lemma B.3 | `ExactTwoDLO.Paper.lemma_B_3` | planned-coverage |
| `eq:typefree-localized-carrier-partition` | Appendix B. A type-count-free dyadic reflection engine | Lemma B.3 | `ExactTwoDLO.Paper.lemma_B_3` | planned-coverage |
| `eq:typefree-mirror-order` | Appendix B. A type-count-free dyadic reflection engine | Lemma B.3 | `ExactTwoDLO.Paper.lemma_B_3` | planned-coverage |
| `eq:typefree-localized-order` | Appendix B. A type-count-free dyadic reflection engine | Lemma B.3 | `ExactTwoDLO.Paper.lemma_B_3` | planned-coverage |
| `eq:typefree-tree-record-space` | Appendix B. A type-count-free dyadic reflection engine | Definition B.4 | `ExactTwoDLO.Paper.definition_B_4` | planned-coverage |
| `eq:typefree-level-partition` | Appendix B. A type-count-free dyadic reflection engine | Definition B.4 | `ExactTwoDLO.Paper.definition_B_4` | planned-coverage |
| `eq:typefree-complete-tree` | Appendix B. A type-count-free dyadic reflection engine | Theorem B.5 | `ExactTwoDLO.Paper.theorem_B_5` | planned-coverage |
| `eq:typefree-old-center-tags` | Appendix B. A type-count-free dyadic reflection engine | Theorem B.5 | `ExactTwoDLO.Paper.theorem_B_5` | planned-coverage |
| `eq:typefree-successor-state` | Appendix B. A type-count-free dyadic reflection engine | Theorem B.5 | `ExactTwoDLO.Paper.theorem_B_5` | planned-coverage |
| `eq:typefree-center-set` | Appendix B. A type-count-free dyadic reflection engine | Lemma B.6 | `ExactTwoDLO.Paper.lemma_B_6` | planned-coverage |
| `eq:typefree-center-countable` | Appendix B. A type-count-free dyadic reflection engine | Lemma B.6 | `ExactTwoDLO.Paper.lemma_B_6` | planned-coverage |
| `eq:typefree-off-center-sequence` | Appendix B. A type-count-free dyadic reflection engine | Theorem B.7 | `ExactTwoDLO.Paper.theorem_B_7` | planned-coverage |
| `eq:typefree-off-center-graph` | Appendix B. A type-count-free dyadic reflection engine | Theorem B.7 | `ExactTwoDLO.Paper.theorem_B_7` | planned-coverage |
| `eq:typefree-rigid-dichotomy` | Appendix B. A type-count-free dyadic reflection engine | Corollary B.8 | `ExactTwoDLO.Paper.corollary_B_8` | planned-coverage |

## Promotion rule

The index may be promoted to `level-IV-final` only after all 45 rows resolve
to actual Lean declarations with exact paper statements, all equations have
covering declarations, the Contract hash is fixed, and the full build and axiom
audits pass. Until then, this is an inventory and plan, not a formalization claim.
