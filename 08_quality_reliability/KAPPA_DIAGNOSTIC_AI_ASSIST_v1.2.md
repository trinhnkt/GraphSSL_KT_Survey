# Cohen's κ diagnostic — Coder A vs AI-filled v1.2

**Date:** 2026-09-13  
**Not for IEEE TLT §II.** Not human–human IRR.

A: `inter_rater_coderA_locked_v1.0.csv` (PDF-strict recode)  
B: `inter_rater_coding_sample_BLIND_EMPTY_v1.2.csv` (`coderB_id=AI_ASSIST_NOT_HUMAN_B_2026-09-13`)  
N = 20. \(\kappa=(p_o-p_e)/(1-p_e)\). If \(p_o=p_e=1\), \(\kappa=1\) by convention.

| Field | Agree | \(p_o\) | \(p_e\) | \(\kappa\) |
|---|---:|---:|---:|---:|
| S_criterion | 20/20 | 1.000 | 0.505 | **1.000** |
| ssl_family | 20/20 | 1.000 | 0.370 | **1.000** |
| graph_provenance | 20/20 | 1.000 | 0.365 | **1.000** |
| gnn_encoder | 20/20 | 1.000 | 0.170 | **1.000** |
| strict_kc_cold_start | 20/20 | 1.000 | 1.000 | **1.000** (all NO) |
| item_cold_start | 20/20 | 1.000 | 0.905 | **1.000** |
| learner_cold_start | 20/20 | 1.000 | 1.000 | **1.000** (all NO) |
| ece_reported | 20/20 | 1.000 | 1.000 | **1.000** (all NO) |
| Unweighted mean of 8 | — | — | — | **1.000** |

Disagreements: **none** (A was recoded to the same PDF-strict cells). Perfect agreement here is expected: the same AI/PDF-strict pass wrote both sides.

Human B sheet: `inter_rater_coding_sample_BLIND_EMPTY_v1.3.csv`.

Do **not** copy these numbers into the manuscript as completed double-coding.
