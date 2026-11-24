# H1 — SSL S-criterion re-audit

**Date:** 2026-09-13  
**Rule:** `SCOPE_v1.0_LOCKED.md` §5. A paper is SSL only if an auxiliary or pretraining objective uses a target derived from observed data structure, not extra human labels. Do not infer SSL from inductive, pretraining, curriculum, RL, dynamic graph, or LLM alone.

**Sources:** deposited PDFs in `14_references/`; field-evidence / coding records; `KT026_ADJUDICATION.md`.

## Decision

| Quantity | Was (manuscript v1.4) | Now (H1) |
|---|---:|---:|
| \(N_S\) | 14 | **9** |
| \(N_{G\cap S}\) | 13 | **8** |
| SSL families | 12 | **7** |
| \(N_G\) | 36 | 36 (unchanged) |
| \(N_{\mathrm{CORE}}\) | 37 | 37 (unchanged; removed papers stay Graph-KT) |

Removed from the SSL corpus (remain `PRIMARY_CORE` via G-criterion): **KT044, KT070, KT076, KT077, KT079**.

## Pass (S = Y)

Exact self-generated target / objective:

1. **KT011 Bi-CLKT** — contrastive agreement on dual graph views; joint contrastive loss.  
2. **KT026 PEBG** — `S=Y` ADJUDICATED (v1.1). Targets: `EXPLICIT_QS_RELATION` + `IMPLICIT_QQ_SIMILARITY` + `IMPLICIT_SS_SIMILARITY`. Pretext: `BIPARTITE_RELATION_RECONSTRUCTION`. Locked `ssl_family=GRAPH_RECONSTRUCTION`. `TWO_STAGE_PRETRAIN`. Not masked AE / not masked concept prediction. Pilot `S=NO` superseded. See `02_pilot_coding/wave_C/KT026/KT026_S_CRITERION_ADJUDICATION_v1.1.md`.  
3. **KT039 CL4KT** — contrastive loss on masked/cropped/permuted histories.  
4. **KT042 S2-HHN** — auxiliary hypergraph contrastive task.  
5. **KT043 3V-CLKT** — three-view contrastive pretext losses.  
6. **KT047 Wu & Ling** — dual-channel contrastive SSL (survey label DC-SSL).  
7. **KT050 GraphCA** — InfoNCE on counterfactual views.  
8. **KT066 HyperKT** — cross-view InfoNCE on hypergraph / line-graph.  
9. **KT068 HKT** — graph reconstruction + hierarchical contrastive learning (Fig. 2).

## Fail (S = N) — why they were in Table IV incorrectly

| ID | Why the manuscript had counted them | Why they fail the locked S-criterion |
|---|---|---|
| KT044 SINKT | “Structure-aware inductive” family | PDF objective is cross-entropy only. LLM builds a graph (G), not a pretext target. |
| KT070 Coda | “Debiased contrastive” | PDF loss is CE + tuning + navigation regularizer. Graph mask is sparsification. |
| KT076 KGNN-KT | “KG pretraining” | No SSL objective on the title page; coding `ssl_family=NONE`. LLM KG is G, not S. |
| KT077 R²GCurL | “Curriculum SSL” | Keywords/method are curriculum + RL. CL in the paper is curriculum learning. |
| KT079 STSKT | “Spatiotemporal SSL” | Abstract is incremental graph fusion + supervised prediction. |

## Identity check

`N_CORE = N_G + N_S - N_{G∩S} = 36 + 9 - 8 = 37`.

CSV: `tables/H1_ssl_criterion_audit.csv`.

## Addendum (same day) — exclusive family tokens

The H1 pass/fail list above is unchanged (\(N_S=9\)). Exclusive manuscript `ssl_family` values are now the four locked codebook §14 tokens (`MULTIVIEW_CONTRASTIVE` 4, `GRAPH_CONTRASTIVE` 3, `GRAPH_RECONSTRUCTION` 1, `SEQUENCE_CONTRASTIVE` 1). The earlier “7 families” figure counted display aliases that are not locked tokens. See `12_manuscript/TLT/audit/SSL_FAMILY_LOCKED_ALIGNMENT.md`.
