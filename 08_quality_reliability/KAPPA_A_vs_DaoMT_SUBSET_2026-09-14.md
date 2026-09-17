# Cohen's kappa — Coder A vs DaoMT subset

> **SUPERSEDED for manuscript κ reporting (2026-09-15).**  
> Intermediate 10-paper subset only. Prefer FULL20 for the independent-pass claim.  
> Do **not** cite the “\(\kappa=1\) by convention” rule or the 8-field mean **0.95** in the TLT manuscript or Author Portal package.  
> Canonical FULL20 recomputation: `12_manuscript/TLT/audit/KAPPA_RECOMPUTATION.md` and `12_manuscript/TLT/tables/reliability_kappa_recomputed.csv`.

**Date:** 2026-09-14
**A:** `inter_rater_coderA_locked_v1.0.csv`
**B:** `inter_rater_coding_sample_BLIND_EMPTY_v1.4_DaoMT.csv` (`coderB_id=DaoMT`)

Independent 10-paper subset. Not pooled with locator-assisted NguyenKT.
N = 10 papers × 8 fields = 80 cells.
$\kappa=(p_o-p_e)/(1-p_e)$. ~~If $p_o=p_e=1$, $\kappa=1$ by convention.~~ **Withdrawn:** if $p_o=p_e=1$, $\kappa$ is undefined (NA).

| Field | Agree | $p_o$ | $p_e$ | $\kappa$ |
|---|---:|---:|---:|---:|
| S_criterion | 10/10 | 1.000 | 0.500 | 1.00 |
| ssl_family | 9/10 | 0.900 | 0.310 | 0.86 |
| graph_provenance | 9/10 | 0.900 | 0.370 | 0.84 |
| gnn_encoder | 9/10 | 0.900 | 0.220 | 0.87 |
| strict_kc_cold_start | 10/10 | 1.000 | 1.000 | 1.00 (all NO) |
| item_cold_start | 10/10 | 1.000 | 0.820 | 1.00 |
| learner_cold_start | 10/10 | 1.000 | 1.000 | 1.00 (all NO) |
| ece_reported | 10/10 | 1.000 | 1.000 | 1.00 (all NO) |
| Unweighted mean of 8 | — | — | — | **0.95** |

Pre-adjudication agreement: **77/80**.

Pre-adjudication diffs:
- KT047 `ssl_family` A=MULTIVIEW_CONTRASTIVE / B=GRAPH_CONTRASTIVE
- KT070 `graph_provenance` A=DYNAMIC_LEARNED / B=MODEL_DEFINED_FIXED
- KT068 `gnn_encoder` A=GNN_GENERIC / B=HETEROGENEOUS_GNN

Do not merge this coefficient with the 20-paper locator-assisted kappa.
