# Cohen's κ diagnostic — Coder A vs adopted draft

**Date:** 2026-09-13  
**Not for IEEE TLT §II.** Not human–human IRR.  
A: `inter_rater_coderA_locked_v1.0.csv`  
B: `inter_rater_coding_sample_BLIND_v1.0.csv` (`coderB_id=HUMAN_ADOPTED_AI_DRAFT_2026-09-13`)  
N = 20 papers. Formula: \(\kappa=(p_o-p_e)/(1-p_e)\). If \(p_o=p_e=1\) (all labels identical), report \(\kappa=1\) by convention (undefined 0/0).

| Field | Agree | \(p_o\) | \(p_e\) | \(\kappa\) |
|---|---:|---:|---:|---:|
| S_criterion | 20/20 | 1.000 | 0.505 | **1.000** |
| ssl_family | 20/20 | 1.000 | 0.370 | **1.000** |
| graph_provenance | 20/20 | 1.000 | 0.365 | **1.000** |
| gnn_encoder | 18/20 | 0.900 | 0.175 | **0.879** |
| strict_kc_cold_start | 19/20 | 0.950 | 0.950 | **0.000** |
| item_cold_start | 18/20 | 0.900 | 0.815 | **0.459** |
| learner_cold_start | 20/20 | 1.000 | 1.000 | **1.000** (all NO) |
| ece_reported | 20/20 | 1.000 | 1.000 | **1.000** (all NO) |
| Unweighted mean of 8 | — | — | — | **0.792** |

## Disagreements (5 cells)

| Paper | Field | A | B (PDF-strict draft) |
|---|---|---|---|
| KT031 | gnn_encoder | GCN | OTHER |
| KT044 | gnn_encoder | GCN | GAT |
| KT044 | strict_kc_cold_start | YES | NO |
| KT026 | item_cold_start | YES | NO |
| KT076 | item_cold_start | YES | NO |

`strict_kc` \(\kappa=0\) is the prevalence paradox: 19/20 agree NO, one YES/NO clash on KT044.

Do **not** copy these numbers into the manuscript as completed double-coding.
