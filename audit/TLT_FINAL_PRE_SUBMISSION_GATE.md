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
| Page count ≤ 18 | YES | Anonymous / full / formatted PDFs **16 pp** after compact reorg (2026-11-24/25); coded claims unchanged |
| Automatic submission | NO | Not performed |

## Review-fix pass (2026-11-24 evening)

| Fix | Status |
|---|---|
| `fig_meta_analysis_charts` encoder bars recount to sum 40 (14/7/6/6/2/2/3) | DONE |
| `fig_taxonomy_2d` encoder chips synced to same tallies | DONE |
| Cover letter rewritten to N=44 / 16 pages / screening subset / seven integrated | DONE (page count synced 2026-11-25) |
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

## Cross-version consistency (2026-11-25)

| Pair | Result |
|---|---|
| `main_tlt_anonymous.tex` ↔ `main_tlt_full.tex` ↔ `manuscript_TLT_FORMATTED_v1.3.tex` body (from abstract; identity-stripped) | **Identical** (same SHA; 0 line diffs) |
| Abstract across 3 tex | Identical |
| Table/figure labels across 3 tex | Identical |
| Cover letter locked counts vs manuscript | Aligned (N=44, NG/NS/∩, 0/44 ECE/cold-start, 16 pp) |
| Intentional diffs only | Anonymous authorship vs named ORCID + `IEEEbiographynophoto` on full/formatted |

Script: `audit/_cross_version_consistency_2026-11-25.py`.

## Final flags

- `READY_FOR_TLT_FINAL_REVIEW = YES`
- `READY_FOR_TLT_SUBMISSION = NO` until Author Portal ORCID link + optional TLT-instructions visual check are done by authors

## Live PDF paths

- `12_manuscript/TLT/main_tlt_anonymous.pdf` (16 pages)
- `12_manuscript/TLT/main_tlt_full.pdf` (16 pages)
- `12_manuscript/TLT/manuscript_TLT_FORMATTED_v1.3.pdf` (16 pages; same body as full)
- `12_manuscript/TLT/COVER_LETTER.pdf` (2 pages; N=44; states 16 pages)


## Provisional N=53 revised package (2026-11-25) — NOT live portal ship

Venue-probe full-text integration (KT090–KT098) yields provisional freeze
`CORPUS_FINAL_FREEZE = YES_PROVISIONAL_AI` (`audit/CORPUS_FINAL_FREEZE_v2.md`).

| Quantity | Value |
|---|---:|
| N | 53 |
| N_G | 49 |
| N_S | 22 |
| N_G ∩ S | 18 |
| Provenance display | 31 / 9 / 9 |
| Strict KC / item / learner / drop | 0 / 1 / 2 / 1 (per 53) |
| ECE / Brier | 0/53 |
| RMSE (prediction error) | 15/53 |

| Check | Status |
|---|---|
| Versioned revised tex + PDF (anonymous + full) | YES — `Graph_SSL_KT_TLT_REVISED_vNext_{anonymous,full}.{tex,pdf}` |
| Zanellati related-work + Table II column | YES |
| SSL taxonomy on full $N_S=22$ (contrastive 20 / recon 2) | YES |
| Principal coding κ = NguyenKT ↔ DaoMT | YES (macro κ≈0.93; AI–human Supplementary) |
| Page count ≤ 18 | YES — **16 pp** both PDFs |
| Live `main_tlt_*` overwritten to N=53 | **NO** (author decision required) |
| Cover letter / portal pack updated to N=53 | **NO** (still N=44 pack) |
| Human verify KT090–KT098 | **REQUIRED** |
| `READY_FOR_TLT_SUBMISSION` on N=53 package | **NO** |

Live portal ship remains the N=44 package above until authors explicitly promote vNext.


## Live promote N=53 (2026-11-25 night)

After KT090–KT098 locator verify (`YES_VERIFIED_AI_LOCATOR`), vNext was promoted to live ship files.

| Live file | Source |
|---|---|
| `main_tlt_anonymous.tex/pdf` | `Graph_SSL_KT_TLT_REVISED_vNext_anonymous.*` |
| `main_tlt_full.tex/pdf` | `Graph_SSL_KT_TLT_REVISED_vNext_full.*` |
| `manuscript_TLT_FORMATTED_v1.3.tex/pdf` | same body as full |
| `COVER_LETTER.tex/pdf` | rewritten N=53 / 16 pp / Zanellati / principal κ |
| N=44 backup | `12_manuscript/TLT/_pre_promote_N44_2026-11-25/` |
| Portal pack | `12_manuscript/TLT/_portal_pack_2026-11-25_N53/` |

| Quantity | Live value |
|---|---:|
| N | 53 |
| N_G | 49 |
| N_S | 22 |
| ∩ | 18 |
| Provenance | 31 / 9 / 9 |
| Pages | 16 (target ≤18) |

- `READY_FOR_TLT_FINAL_REVIEW = YES` (N=53 package)
- `READY_FOR_TLT_SUBMISSION = NO` until Author Portal ORCID link + author upload
- Automatic submission: **NO**
