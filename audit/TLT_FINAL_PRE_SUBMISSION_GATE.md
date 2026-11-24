# TLT final pre-submission gate

Date: 2026-11-24.

Scope: expanded-corpus freeze + N=44 manuscript rewrite. This gate does **not** authorize Author Portal upload.

## Preconditions (locked)

| Check | Status | Evidence |
|---|---|---|
| `CORPUS_EXPANDED_AND_FROZEN` | YES | `audit/A1_EXPANDED_CORPUS_FREEZE.md`; `data/PRIMARY_CORE_EXPANDED_2026-11-24.csv` |
| `PROVENANCE_COUNTS_LOCKED` | YES | `audit/PROVENANCE_FINAL_ADJUDICATION.md` (24 / 7 / 9 / 0 on $N_G=40$) |
| Sparse / cold-start / calibration / QA counts | YES | `audit/COUNTS_EXPANDED_FINAL.md`; `tables/CALIBRATION_EXPANDED.csv` |
| `A_SCREENING_RELIABILITY_DEFENSIBLE` | YES | `audit/A_SCREENING_RELIABILITY_FINAL_GATE.md` (deposited subset only) |
| REC_0047 adjudication | YES | `05_screening/fulltext_adjudication.csv` → `PRIMARY_ADJACENT_METHOD` (COMPLETED); not primary core |

## Corpus numbers used in the manuscript

| Quantity | Value |
|---|---:|
| N | 44 |
| N_G | 40 |
| N_S | 16 |
| N_G ∩ S | 12 |
| Provenance display | 24 / 7 / 9 |
| Strict KC cold-start YES | 0/44 |
| Item cold-start YES | 1/44 (SINKT) |
| Learner cold-start YES | 2/44 (SGKT, CoSKT) |
| Interaction-drop YES | 1/44 (HCMKT; not HHSKT) |
| ECE / Brier | 0/44 |
| RMSE (prediction error, not calibration) | 14/44 |
| QA HIGH / MODERATE / LIMITED | 13 / 31 / 0 |
| QA mean (norm) | 0.7472 (~0.75 in prose) |
| Search-log identification | N_rec = 2,017 (unchanged) |
| PRISMA stage arithmetic | 750 / 140 / 103; original-path 140−103=37 (unchanged) |

## Manuscript rewrite checks

| Check | Status | Notes |
|---|---|---|
| Abstract uses N=44 and locked NG/NS/intersection | YES | `main_tlt_anonymous.tex`, `main_tlt_full.tex`, `manuscript_TLT_FORMATTED_v1.3.tex` |
| Obsolete analysis denominators `0/37`, `N_G=36`, `N_S=9` as live claims | CLEARED | Remaining “37” strings are original-path PRISMA arithmetic or legacy sensitivity wording |
| Gateway seven papers integrated (not “outside tables”) | YES | Sec. `gateway_ext` |
| HHSKT no longer coded YES for interaction-drop | YES | HCMKT is the YES paper |
| Screening reliability scoped to deposited subset | YES | TA 10/11; FT 0/1; κ NA |
| Graph-graph duplicate wording | NONE FOUND | |
| Figures updated to locked counts | YES | `fig_taxonomy_2d`, `fig_prisma_flow`, `fig_ssl_framework`, `fig_graph_construction_pipeline`, `fig_meta_analysis_charts` rebuilt |
| Page count ≤ 18 | YES | Anonymous PDF 18 pp; full PDF 18 pp (2026-11-24 rebuild) |
| Automatic submission | NO | Not performed |

## Review-fix pass (2026-11-24 evening)

| Fix | Status |
|---|---|
| `fig_meta_analysis_charts` encoder bars recount to sum 40 (14/7/6/6/2/2/3) | DONE |
| `fig_taxonomy_2d` encoder chips synced to same tallies | DONE |
| Cover letter rewritten to N=44 / 18 pages / screening subset / seven integrated | DONE |
| Abstract shortened (~207 words) on three live tex files | DONE |
| Body encoder `$n=/40$` wording synced | DONE |
| SSL figure header clarifies families-below = pre-expansion | DONE |

## Residual-fix pass (2026-11-24 night)

| Fix | Status |
|---|---|
| QA7 aligned: KT035→0, KT023→2; HIGH list swaps KT035↔KT023; mean unchanged 0.7472 | DONE (`audit/QA7_COLDSTART_ALIGNMENT_2026-11-24.md`) |
| SSL section leads with paradigm×view ($N_S=16$); four families labeled pre-expansion exclusive | DONE |
| Threats updated for QA7 sync + SSL partition scope | DONE |
| Protocol deviation DEV-20261124-01 | DONE |

## Portal prep pack (2026-11-24)

Folder: `12_manuscript/TLT/_portal_pack_2026-11-24/`

| Item | Status |
|---|---|
| Re-read anonymous PDF + cover letter (text extract + page counts) | DONE — see `01_PDF_READ_CHECK.md` |
| ORCID Khanh-Trinh + Duong (+ all five) via public API | DONE — see `02_ORCID_VERIFICATION.md` |
| Link ORCID on Author Portal | **AUTHOR ONLY** (needs IEEE login) |
| Compare to `TLT-instructions-only.pdf` | PARTIAL — compared to local `New_IEEEtran_how-to.pdf`; TLT-specific PDF not in repo |
| Supplementary + AI disclosure + originality paste text | DONE — `04_PORTAL_STATEMENTS.md`, `05_UPLOAD_LIST.md`, `supplementary_upload/` |

## Known residuals (author final review)

1. Printed Graph-KT / SSL tables remain **representative subsets**; full 40/16 rows live in supplementary / machine files.
2. No new exclusive-family partition was invented for all 16 SSL papers (correctly disclosed as paradigm×view + historical 9-paper families).
3. Author Portal: link 5 ORCIDs; download `TLT-instructions-only.pdf` for final visual compare; upload from `_portal_pack_2026-11-24`.
4. Optional narrative: who verified AI primary-coding fields; construction-split gaps.

## Final flags

- `READY_FOR_TLT_FINAL_REVIEW = YES`
- `READY_FOR_TLT_SUBMISSION = NO` until Author Portal ORCID link + optional TLT-instructions visual check are done by authors

## Live PDF paths

- `12_manuscript/TLT/main_tlt_anonymous.pdf` (18 pages)
- `12_manuscript/TLT/main_tlt_full.pdf` (18 pages)
- `12_manuscript/TLT/COVER_LETTER.pdf` (2 pages; N=44 wording)
