# Adjudication: Coder A vs v1.3 (2026-09-13)

**Not for IEEE TLT §II as human–human \(\kappa\).**

B sheet: `inter_rater_coding_sample_BLIND_EMPTY_v1.3.csv` (`coderB_id=NguyenKT`).  
Rows were adopted from locator-pack readings in chat, then confirmed `ghi hết`. This is **not** an independent blind human B pass.

A: `inter_rater_coderA_locked_v1.0.csv` (PDF-strict recode; live CSVs).

N = 20 papers × 8 fields = 160 cells. Agree **155/160**.

\(\kappa=(p_o-p_e)/(1-p_e)\). If \(p_o=p_e=1\), \(\kappa=1\) by convention.

| Field | Agree | \(p_o\) | \(p_e\) | \(\kappa\) |
|---|---:|---:|---:|---:|
| S_criterion | 20/20 | 1.000 | 0.505 | **1.000** |
| ssl_family | 18/20 | 0.900 | 0.370 | **0.841** |
| graph_provenance | 18/20 | 0.900 | 0.338 | **0.849** |
| gnn_encoder | 19/20 | 0.950 | 0.158 | **0.941** |
| strict_kc_cold_start | 20/20 | 1.000 | 1.000 | **1.000** (all NO) |
| item_cold_start | 20/20 | 1.000 | 0.905 | **1.000** |
| learner_cold_start | 20/20 | 1.000 | 1.000 | **1.000** (all NO) |
| ece_reported | 20/20 | 1.000 | 1.000 | **1.000** (all NO) |
| Unweighted mean of 8 | — | — | — | **0.954** |

Do **not** copy these numbers into `manuscript_TLT_FORMATTED_v1.3.tex` §II.

## Five disagreements — gold = locked live coding

| Paper | Field | A (locked) | B (v1.3) | Gold | Why |
|---|---|---|---|---|---|
| KT011 Bi-CLKT | ssl_family | MULTIVIEW_CONTRASTIVE | GRAPH_CONTRASTIVE | **A** | Exclusive family in `ssl_taxonomy.csv` is MULTIVIEW (dual node/graph views). GRAPH is the secondary column. |
| KT047 DC-SSL | ssl_family | GRAPH_CONTRASTIVE | MULTIVIEW_CONTRASTIVE | **A** | Exclusive family is GRAPH. MULTIVIEW is secondary (dual-channel note). |
| KT026 PEBG | graph_provenance | MODEL_DEFINED_FIXED | EXTERNAL_FIXED | **A** | Live `graph_taxonomy.csv`: `Q_MATRIX_DERIVED` / MODEL_DEFINED_FIXED (incidence construction). EXTERNAL is for expert maps (PDKT-C, CMKT), not this Q-graph recipe. |
| KT070 Coda | graph_provenance | MODEL_DEFINED_FIXED | DYNAMIC_LEARNED | **A** | Live taxonomy MODEL_DEFINED_FIXED. Locator “learnable adjacency” is the code-graph adaptor, not a student-interaction topology evolving under the workpack DYNAMIC rule. Expansion `JOINTLY_LEARNED_TRAINING` is a finer codebook token, not the IRR 4-way set. |
| KT068 HKT | gnn_encoder | HETEROGENEOUS_GNN | GNN_GENERIC | **A** | `graph_taxonomy.csv` + KT068 coding Sec. 3.2: hierarchical / heterogeneous GNN. B under-specified from locator. |

No PDF fact error on S, cold-start, or ECE. Item CS remains SINKT only.

## Locked manuscript counts

Unchanged: \(N_S=9\), provenance/encoder tables, strict KC \(0/37\), item CS \(1/37\).

## Next if a §II \(\kappa\) is required

Independent human B fills a **new** empty sheet without seeing these example tokens or this file.
