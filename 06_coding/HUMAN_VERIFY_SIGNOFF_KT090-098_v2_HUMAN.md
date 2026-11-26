# HUMAN VERIFY SIGNOFF — KT090–KT098 (v2 HUMAN wet-ink)

**Status:** COMPLETED — HUMAN_VERIFIED 2026-11-26  
**Verifier recorded:** Nguyen Khanh Trinh (author wet-ink; session walkthrough with PDF/OA open).

## Header (fill)

| Field | Value |
|---|---|
| Verifier (full name) | Nguyen Khanh Trinh |
| Role | author wet-ink |
| Date | 2026-11-26 |
| Method | Open each PDF/OA extract; tick against `HUMAN_VERIFY_CHECKLIST_KT090-098_v1.md` using locators in `HUMAN_VERIFY_EVIDENCE_PACK_KT090-098_v1.md` |
| Pair files used | checklist v1 + evidence pack v1 + `PRIMARY_CORE_FINAL_v2.csv` |

## Order completed (risk order)

Tick when done:

- [x] KT092 GRKT — S=NO trap (PASS; CHANGEs=0; session continue 2026-11-26)
- [x] KT091 ExpertGraphs — EXTERNAL_FIXED (PASS; CHANGEs=0; session continue 2026-11-26)
- [x] KT095 TransKT — EXTERNAL_FIXED + S=YES (PASS; CHANGEs=0; session continue 2026-11-26)
- [x] KT098 KGS-KT — RECONSTRUCTION (OA extract) (PASS; CHANGEs=0; session continue 2026-11-26)
- [x] KT093 BiCo — RMSE YES; G∩S (PASS; CHANGEs=0; session continue 2026-11-26)
- [x] KT094 GCLFKT — own GCL (PASS; CHANGEs=0; session continue 2026-11-26)
- [x] KT096 SCDI — G∩S (PASS; CHANGEs=0; session continue 2026-11-26)
- [x] KT097 MSCL — G∩S (≠ SCDI) (PASS; CHANGEs=0; session continue 2026-11-26)
- [x] KT090 AGKT — G-only; S=NO (PASS; CHANGEs=0; encoder OTHER kept; session continue 2026-11-26)

## Per-paper roll-up

For each row: `KEEP` / `CHANGE` / `EXCLUDE`.  
If CHANGE: list field → old → new → page/§ locator.

| record_id | short | gate | CHANGEs (or 0) | critical fields PASS? | page notes |
|---|---|---|---|---|---|
| KT090 | AGKT | KEEP | 0 | YES | G-only; S=NO; encoder OTHER kept |
| KT091 | ExpertGraphs | KEEP | 0 | YES | EXTERNAL_FIXED expert-defined confirmed |
| KT092 | GRKT | KEEP | 0 | YES | S=NO confirmed (contrastive = related-work only) |
| KT093 | BiCo | KEEP | 0 | YES | RMSE YES as prediction error; G∩S CONTRASTIVE |
| KT094 | GCLFKT | KEEP | 0 | YES | own GCL + GAT; CONTRASTIVE/GRAPH |
| KT095 | TransKT | KEEP | 0 | YES | EXTERNAL_FIXED LLM concept graph; S=YES contrastive |
| KT096 | SCDI | KEEP | 0 | YES | MAGNN+GATC dual-channel SSL contrastive |
| KT097 | MSCL | KEEP | 0 | YES | MAGNN+DGCN; distinct from SCDI |
| KT098 | KGS-KT | KEEP | 0 | YES | RECONSTRUCTION NAP/ERP; OA extract |

**Critical fields** = identity PDF + KT + G + S + provenance + sparse4 + ECE/Brier/RMSE (+ SSL paradigm if S=YES).

## Expected coded values (do not change unless CHANGE logged)

| id | G | S | provenance | SSL | RMSE | sparse4 |
|---|---|---|---|---|---|---|
| KT090 | Y | N | MODEL_DEFINED_FIXED | — | N | all N |
| KT091 | Y | N | EXTERNAL_FIXED | — | N | all N |
| KT092 | Y | **N** | MODEL_DEFINED_FIXED | — | N | all N |
| KT093 | Y | Y | MODEL_DEFINED_FIXED | CONTRASTIVE / bipartite | **Y** | all N |
| KT094 | Y | Y | MODEL_DEFINED_FIXED | CONTRASTIVE / graph | N | all N |
| KT095 | Y | Y | EXTERNAL_FIXED | CONTRASTIVE | N | all N |
| KT096 | Y | Y | MODEL_DEFINED_FIXED | CONTRASTIVE / graph | N | all N |
| KT097 | Y | Y | MODEL_DEFINED_FIXED | CONTRASTIVE / graph | N | all N |
| KT098 | Y | Y | MODEL_DEFINED_FIXED | **RECONSTRUCTION** | N | all N |

## Counts after wet-ink

If all KEEP / 0 CHANGEs (expected):

- N=53 · NG=49 · NS=22 · NG∩S=18

If any CHANGE affecting G/S: recompute from `PRIMARY_CORE_FINAL_v2.csv` before touching manuscript totals.

Actual after this sheet: N=53 NG=49 NS=22 ∩=18

## Declaration (sign)

I confirm I opened the deposited PDF/OA text for each of KT090–KT098 and verified the critical fields above against the checklist. This is a human wet-ink pass, not an AI-only locator re-audit.

- Verifier signature (typed name): Nguyen Khanh Trinh
- Date: 2026-11-26

## After this file is filled

1. Fill `audit/VENUE_PROBE_HUMAN_VERIFICATION_FILLABLE.csv` (same folder instructions).
2. Run: `python audit/_apply_vx_human_verify_2026-11-26.py`  
   (updates `VENUE_PROBE_HUMAN_VERIFICATION.csv` + patches vNext wording only if status is HUMAN_VERIFIED for all 9).
3. Rebuild vNext PDF; re-open `audit/TLT_FINAL_PRE_SUBMISSION_GATE_vNext.md`.
