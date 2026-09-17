# Kappa recomputation — invariant fields as NA

**Date:** 2026-09-15  
**Sources:** `08_quality_reliability/KAPPA_A_vs_B_SUBMITTED_2026-09-13.md`; `KAPPA_A_vs_DaoMT_FULL20_2026-09-14.md`; pair CSVs (Coder A locked vs NguyenKT AS_SUBMITTED; vs DaoMT FULL20 AS_SUBMITTED).  
**Machine table:** `tables/reliability_kappa_recomputed.csv`

## Rule

Cohen's \(\kappa = (p_o - p_e)/(1 - p_e)\).  
If \(p_o = p_e = 1\), the denominator is zero → \(\kappa\) is **undefined (NA)**, not 1.

Prior reports set \(\kappa=1\) “by convention” for all-NO fields and averaged those values into the unweighted mean. That practice is withdrawn.

## Invariant fields (both pairs)

On all 20 papers, both coders assigned the same single category:

| Field | Category | \(p_o\) | \(p_e\) | \(\kappa\) |
|---|---|---:|---:|---|
| `strict_kc_cold_start` | NO | 1.000 | 1.000 | **NA** |
| `learner_cold_start` | NO | 1.000 | 1.000 | **NA** |
| `ece_reported` | NO | 1.000 | 1.000 | **NA** |

Percent agreement on each = **100%**. These three fields are excluded from the macro-average \(\kappa\).

`item_cold_start` is **not** invariant (\(p_e=0.905\); SINKT YES present) → \(\kappa=1.00\) remains DEFINED.

## Locator-assisted (Coder A vs NguyenKT)

- Cells: 158/160 agree (98.75%).
- Field-wise DEFINED \(\kappa\): S 1.00; ssl_family 0.92; graph_provenance 0.93; gnn_encoder 1.00; item_cold_start 1.00.
- Invariant / NA fields: 3.
- **Macro-average over 5 DEFINED \(\kappa\): 0.97** \((1.00+0.92+0.93+1.00+1.00)/5\).
- Prior 8-field mean **0.98 is withdrawn** (it included three conventional \(\kappa=1\)).

## Independent blind (Coder A vs DaoMT; no locator)

- Cells: 157/160 agree.
- Field-wise DEFINED \(\kappa\): S 1.00; ssl_family 0.92; graph_provenance 0.92; gnn_encoder 0.94; item_cold_start 1.00.
- Invariant / NA fields: 3 (same as above).
- **Macro-average over 5 DEFINED \(\kappa\): 0.96** \((1.00+0.92+0.92+0.94+1.00)/5\).
- Prior 8-field mean **0.97 is withdrawn**.

## Pooling

The two designs are **not pooled**.
