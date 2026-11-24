# A1 expanded corpus — freeze 2026-11-24

**CORPUS_EXPANDED_AND_FROZEN = YES**

Frozen row file: `data/PRIMARY_CORE_EXPANDED_2026-11-24.csv`  
Prior row file retained (not overwritten): `data/PRIMARY_CORE_EXPANDED_2026-11-23.csv`  
Cold-start / QA / calibration source: `audit/COUNTS_EXPANDED_FINAL.md`, `tables/CALIBRATION_EXPANDED.csv`  
Provenance source: `audit/PROVENANCE_FINAL_ADJUDICATION.md` (`PROVENANCE_COUNTS_LOCKED = YES`)

Freeze step itself did not rewrite the manuscript. On 2026-11-24 the live TLT tex/PDF package was subsequently rewritten to these locked counts (`audit/TLT_FINAL_PRE_SUBMISSION_GATE.md`). Deposited 37-row tables were not overwritten.

## Counts

| Quantity | Value |
|---|---:|
| N | 44 |
| N_G | 40 |
| N_S | 16 |
| N_G∩S | 12 |
| Check 40+16−12 | 44 |

Provenance among 40 graph papers: MODEL_DEFINED_FIXED 24, EXTERNAL_FIXED 7, DYNAMICALLY_LEARNED 9, UNCLEAR 0.

| Construct | YES | Papers |
|---|---:|---|
| interaction_drop | 1 | KT086 |
| item_cold_start | 1 | KT044 |
| learner_cold_start | 2 | KT023, KT087 |
| strict_KC_cold_start | 0 | none |
| ECE | 0 | |
| Brier | 0 | |
| RMSE | 14 | |
| calibration / reliability plot | 1 | KT039 |

QA on 44 papers (thresholds unchanged): HIGH 13, MODERATE 31, LIMITED 0, mean 0.7472.

QA7 cells for KT035 (HHSKT) and KT023 (SGKT) were aligned to the locked cold-start fields on 2026-11-24 (DEV-20261124-01). Row file `data/PRIMARY_CORE_EXPANDED_2026-11-24.csv` updated; pre-align snapshot retained as `..._PRE_QA7ALIGN.csv`.

## IDs for the seven integrated papers

KT084 DECKT, KT085 KT-Deeper, KT086 HCMKT, KT087 CoSKT, KT040 DTransformer, KT088 SP-CLKT, KT089 CLBG.

## Freeze criteria met

1. N / N_G / N_S / N_G∩S arithmetic passes.
2. Cold-start and calibration fields match the 2026-11-24 audit.
3. QA1–QA8 for the seven papers are numeric (no UNCLEAR).
4. Provenance unresolved display count = 0; KT085 locked as DYNAMICALLY_LEARNED.
5. Versioned corpus file written; prior expansion file retained.

## Still not claimed by this freeze

- Manuscript rewrite to N=44 (separate task; requires this freeze as precondition).
- Historical 750/103 screening reliability.
- Automatic submission.
