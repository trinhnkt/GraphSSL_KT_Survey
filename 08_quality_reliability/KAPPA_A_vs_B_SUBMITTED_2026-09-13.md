# Cohen's κ — Coder A vs B as submitted

> **SUPERSEDED for manuscript κ reporting (2026-09-15).**  
> This file preserves the as-submitted pair summary and cell counts (**158/160**).  
> Do **not** cite the “\(\kappa=1\) by convention” rule or the 8-field mean **0.98** in the TLT manuscript or Author Portal package.  
> Canonical recomputation (invariant all-NO fields → \(\kappa=\mathrm{NA}\); macro over defined fields only → **0.97** for this locator-assisted pair):  
> `12_manuscript/TLT/audit/KAPPA_RECOMPUTATION.md` and `12_manuscript/TLT/tables/reliability_kappa_recomputed.csv`.

**Date:** 2026-09-13  
**A:** `inter_rater_coderA_locked_v1.0.csv` (current gold)  
**B:** `inter_rater_coding_sample_BLIND_EMPTY_v1.3_AS_SUBMITTED.csv` (before gold-align of KT011/KT026)

B used the locator pack and adopted example tokens (`coderB_id=NguyenKT`). **Not** a fully independent blind human pass. Do not describe this as independent human–human IRR.

N = 20 papers × 8 fields. Agree **158/160** (98.75\%).  
\(\kappa=(p_o-p_e)/(1-p_e)\). ~~If \(p_o=p_e=1\), \(\kappa=1\) by convention.~~ **Withdrawn:** if \(p_o=p_e=1\), \(\kappa\) is undefined (NA).

| Field | Agree | \(p_o\) | \(p_e\) | \(\kappa\) |
|---|---:|---:|---:|---:|
| S_criterion | 20/20 | 1.000 | 0.505 | 1.00 |
| ssl_family | 19/20 | 0.950 | 0.373 | 0.92 |
| graph_provenance | 19/20 | 0.950 | 0.328 | 0.93 |
| gnn_encoder | 20/20 | 1.000 | 0.150 | 1.00 |
| strict_kc_cold_start | 20/20 | 1.000 | 1.000 | 1.00 (all NO) |
| item_cold_start | 20/20 | 1.000 | 0.905 | 1.00 |
| learner_cold_start | 20/20 | 1.000 | 1.000 | 1.00 (all NO) |
| ece_reported | 20/20 | 1.000 | 1.000 | 1.00 (all NO) |
| Unweighted mean of 8 | — | — | — | **0.98** |

Pre-adjudication diffs: KT011 `ssl_family` (A MULTIVIEW / B GRAPH); KT026 `graph_provenance` (A MODEL_DEFINED / B EXTERNAL). Gold = A.

Screening/full-text pair files named in the protocol are still absent.
