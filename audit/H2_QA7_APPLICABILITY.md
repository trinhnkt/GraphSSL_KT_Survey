# H2 — QA7 applicability

**Decision: KEEP_CURRENT.** QA7 is applicable for all 37 primary-core papers. Scores and tiers are unchanged (HIGH 11 / MODERATE 26 / LIMITED 0; mean 0.76; max = 16).

**Not a protocol change.** `SLR_PROTOCOL_v1.0_LOCKED.md` §22.1 says QA7 *may* be `NA` when a paper makes no sparse/cold-start claim. This survey does not use that NA option. `_LOCKED` files are not edited.

## What QA7 is

The QA total is **review-specific methodological evidence quality** (an evidence-quality score for the present review), not a general ranking of study quality.

QA7 is **review-specific evidence adequacy** for RQ4. It scores how informative each study’s evaluation design is for the sparse-concept and cold-start question in RQ4.

QA7 is **not** a judgment that all 37 authors claimed to “solve sparsity” or cold-start.

Do **not** use the logic: “All papers claim sparsity, therefore QA7 applies.”

Use: QA7 is applicable to all primary-core studies because RQ4 evaluates the adequacy with which each study’s evaluation protocol supports inference under sparse-concept conditions. Applicability therefore follows from the survey’s evidence lens rather than from whether the original authors explicitly claimed to solve cold-start.

A paper with a generic learner split can still receive a QA7 score for the evidence that protocol supplies for RQ4.

## Reviewer sentence if they quote protocol §22.1

The locked protocol (Sec. 22.1) permits QA7 to be coded NA when a paper makes no sparse or cold-start claim. This survey does not use that option: because RQ4 asks how well each evaluation protocol supports sparse-concept inference, QA7 is scored for all 37 primary-core papers and the applicable maximum remains 16.

## Two variables (kept separate)

| Variable | Meaning | Does it set QA7 applicability? |
|---|---|---|
| `evaluation_support_regime` | What split / support regime the paper actually ran | No |
| `sparsity_claim` | Locked ontology token for explicit sparse/cold-start focus | No |
| `QA7_applicable` | Whether this survey scores QA7 | Yes: `Y` for all 37, from the RQ4 lens |

QA7 does not score “authors claimed sparsity.” It scores strength of evidence for the survey’s sparse/cold-start research question.

## Overlay used in this survey

Derived from existing `sparse_coldstart_audit.csv` (`sparse_protocol_category`); **not** a new full-text claim recode of 37 abstracts and not written into `_LOCKED` files. Claim values are locked §16 tokens.

| n | `sparse_protocol_category` | `evaluation_support_regime` | `sparsity_claim` | `QA7_applicable` | Rule |
|---:|---|---|---|---|---|
| 32 | `SPARSE_INTERACTION_ONLY` | `GENERIC_INTERACTION_SPLIT` | `NO_EXPLICIT_FOCUS` | Y | Derived from category |
| 1 | `SPARSE_INTERACTION_ONLY` (KT035 HHSKT) | `INTERACTION_DROP_SPLIT` | `GENERIC_DATA_SPARSITY` | Y | Documented interaction-drop exception; category unchanged |
| 2 | `ITEM_COLD_START` | `ITEM_COLD_START_SPLIT` | `ITEM_COLD_START` | Y | Derived from category |
| 1 | `STRICT_KC_COLD_START` | `ZERO_EXPOSURE_KC_SPLIT` | `STRICT_KC_COLD_START` | Y | Derived from category |
| **37** | — | — | — | **Y** | — |

HHSKT remains `SPARSE_INTERACTION_ONLY` (not item or strict KC cold-start). The exception only prevents coding that paper as a generic 80/20 split after the manuscript already reports its drop protocol. We did not recode all 37 abstracts for other possible drop experiments.

Manuscript §II.D shows this 4-row summary as an unnumbered overlay (so Table III remains the graph taxonomy). Full file: `tables/H2_qa7_two_variables.csv`.
Scores: `supplementary/supplementary_quality_scores.csv` (no recomputation).
