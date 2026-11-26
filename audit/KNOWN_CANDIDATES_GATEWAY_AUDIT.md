# Known candidates gateway audit (venue probe VX01–VX10)

**Date:** 2026-11-25 (updated after full PDF drop)  
**Review file:** `05_screening/KNOWN_CANDIDATES_FULLTEXT_REVIEW_v1.csv`  
**Reviewer_type:** `AI_PRIMARY_REVIEW` for all rows (human verification still REQUIRED except VX05 already-in-core)

## Totals

| Metric | Count |
|---|---:|
| Total candidates | **10** |
| PRIMARY_CORE | **10** |
| Already in N=44 freeze | **1** (VX05 = KT086 HCMKT) |
| New PRIMARY_CORE not yet in freeze | **9** (VX01, VX02, VX03, VX04, VX06, VX07, VX08, VX09, VX10) |
| PRIMARY_ADJACENT_* | **0** |
| EXCLUDE_FULLTEXT | **0** |
| UNCERTAIN | **0** |
| Missing PDF | **0** (VX10 = OA HTML extract) |

## Per-candidate

| ID | G | S | Decision | Local PDF |
|---|---|---|---|---|
| VX01 AGKT | Y | N | PRIMARY_CORE | `VX01_AGKT.pdf` |
| VX02 Expert graphs | Y | N | PRIMARY_CORE | `VX02_ExpertGraphs_LAS2024.pdf` |
| VX03 GRKT | Y | N | PRIMARY_CORE | `VX03_GRKT.pdf` |
| VX04 BiCo | Y | Y | PRIMARY_CORE | `VX04_BiCo.pdf` |
| VX05 HCMKT | Y | Y | PRIMARY_CORE (in core) | `VX05_HCMKT.pdf` |
| VX06 GCLFKT | Y | Y | PRIMARY_CORE | `VX06_GCLFKT.pdf` |
| VX07 TransKT | Y | Y | PRIMARY_CORE | `VX07_TransKT.pdf` |
| VX08 SCDI | Y | Y | PRIMARY_CORE | `VX08_SCDI.pdf` |
| VX09 MSCL | Y | Y | PRIMARY_CORE | `VX09_MSCL.pdf` |
| VX10 KGS-KT | Y | Y | PRIMARY_CORE | OA HTML extract |

## STOP GATE status

Missing-PDF UNCERTAIN blockers: **cleared**.

Remaining before `CORPUS_FINAL_FREEZE = YES`:

1. Full PAPER-level coding of the 9 new PRIMARY_CORE rows (provenance, encoder, SSL axes, sparse/cold-start, ECE/Brier/RMSE, QA).  
2. Human verification of AI gateway labels (recommended).  
3. Regenerate N / NG / NS / NG∩S from the final coding table (no manual forcing).

## Provisional membership arithmetic (gateway only; not frozen)

If all 9 new rows enter after coding:

- ΔG ≈ +9 (all have GRAPH_BASED=YES)  
- ΔS ≈ +6 (VX04,06,07,08,09,10)  
- Δ(G∩S) ≈ +6  
- Provisional N ≈ 44+9 = **53** (subject to coding confirmation)

Do **not** use these provisional numbers in the live manuscript until `06_coding/PRIMARY_CORE_FINAL_v2.csv` is written and checked.
