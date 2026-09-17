# Cohen's kappa — Coder A vs DaoMT FULL 20 (independent, no locator)

> **SUPERSEDED for manuscript κ reporting (2026-09-15).**  
> This file preserves the as-submitted pair summary and cell counts (**157/160**).  
> Do **not** cite the “\(\kappa=1\) by convention” rule or the 8-field mean **0.97** in the TLT manuscript or Author Portal package.  
> Canonical recomputation (invariant all-NO fields → \(\kappa=\mathrm{NA}\); macro over defined fields only → **0.96** for this independent pair):  
> `12_manuscript/TLT/audit/KAPPA_RECOMPUTATION.md` and `12_manuscript/TLT/tables/reliability_kappa_recomputed.csv`.  
> Do not pool with the locator-assisted NguyenKT coefficient.

**Date:** 2026-09-14
**A:** `inter_rater_coderA_locked_v1.0.csv`
**B:** `inter_rater_coding_sample_BLIND_EMPTY_v1.4_DaoMT_FULL20_AS_SUBMITTED.csv` (`coderB_id=DaoMT`)

Independent 20-paper sample (subset 10 + REST 10). Not pooled with locator-assisted NguyenKT.
N = 20 papers × 8 fields = 160 cells.
$\kappa=(p_o-p_e)/(1-p_e)$. ~~If $p_o=p_e=1$, $\kappa=1$ by convention.~~ **Withdrawn:** if $p_o=p_e=1$, $\kappa$ is undefined (NA).

| Field | Agree | $p_o$ | $p_e$ | $\kappa$ |
|---|---:|---:|---:|---:|
| S_criterion | 20/20 | 1.000 | 0.505 | 1.00 |
| ssl_family | 19/20 | 0.950 | 0.373 | 0.92 |
| graph_provenance | 19/20 | 0.950 | 0.347 | 0.92 |
| gnn_encoder | 19/20 | 0.950 | 0.158 | 0.94 |
| strict_kc_cold_start | 20/20 | 1.000 | 1.000 | 1.00 (all NO) |
| item_cold_start | 20/20 | 1.000 | 0.905 | 1.00 |
| learner_cold_start | 20/20 | 1.000 | 1.000 | 1.00 (all NO) |
| ece_reported | 20/20 | 1.000 | 1.000 | 1.00 (all NO) |
| Unweighted mean of 8 | — | — | — | **0.97** |

Pre-adjudication agreement: **157/160**.

Pre-adjudication diffs:
- KT047 `ssl_family` A=MULTIVIEW_CONTRASTIVE / B=GRAPH_CONTRASTIVE
- KT070 `graph_provenance` A=DYNAMIC_LEARNED / B=MODEL_DEFINED_FIXED
- KT068 `gnn_encoder` A=GNN_GENERIC / B=HETEROGENEOUS_GNN

Do not merge with the locator-assisted NguyenKT kappa.
