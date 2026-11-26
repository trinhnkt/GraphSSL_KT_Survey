# TLT revision master status — 2026-11-25

Task: multi-phase TLT manuscript revision. **Do not auto-submit.**

## Phase checklist

| Phase | Status | Output / blocker |
|---|---|---|
| 1 Known 10 candidates | **PARTIAL** | `05_screening/KNOWN_CANDIDATES_FULLTEXT_REVIEW_v1.csv`; `audit/KNOWN_CANDIDATES_GATEWAY_AUDIT.md` — **5 UNCERTAIN (no PDF)**; 4 new AI PRIMARY_CORE not yet in freeze |
| 2 Final search update | **NO** | `audit/FINAL_SEARCH_UPDATE_STATUS.md` |
| 3 Corpus refreeze | **BLOCKED** | STOP GATE: UNCERTAIN candidates that may pass gateway |
| 4 Screening reliability | **DONE (tables)** | `tables/SCREENING_RELIABILITY_FINAL.csv` — TA 10/11 raw; FT 0/1 κ=NA; live tex not yet rewritten |
| 5 Human–human κ | **DONE (tables)** | NguyenKT↔DaoMT 155/160; macro κ(defined)=0.9262; live tex not yet rewritten |
| 6 Zanellati related work | **METADATA ONLY** | `audit/ZANELLATI_2024_METADATA.md` — tex patch pending |
| 7–11 Taxonomies / sparse / ECE / QA | BLOCKED on freeze | Do not rewrite locked counts |
| 12 AI disclosure | **DRAFT** | `audit/AI_DISCLOSURE_FINAL.md` |
| 13 References | PENDING | |
| 14 Title recommendation | **DONE** | Prefer Option B; author decision PENDING |
| 15–17 Methods/Threats/Abstract rewrite | BLOCKED on freeze | |
| 18 Tables/figures rebuild | BLOCKED on freeze | |
| 19 Page-limit check | DEFERRED | Current live PDFs 16 pp |
| 20 Final gate | **NOT_READY** | `audit/TLT_PRE_SUBMISSION_FINAL_GATE.md` |

## Current locked snapshot (unchanged; NOT regenerated)

From `data/PRIMARY_CORE_EXPANDED_2026-11-24.csv` (still authoritative until Phase 3):

- N=44, NG=40, NS=16, NG∩S=12  
- strict KC 0/44; item 1/44; learner 2/44; interaction-drop 1/44  
- ECE 0/44; Brier 0/44; RMSE 14/44  

## Blockers for READY

1. **BLOCKER_1:** VX02, VX04, VX06, VX08, VX09 remain UNCERTAIN without full PDF.  
2. **BLOCKER_2:** VX01, VX03, VX07, VX10 AI PRIMARY_CORE decisions need human verification before membership change.  
3. **BLOCKER_3:** Final six-DB search update not executed (`FINAL_SEARCH_UPDATE_COMPLETED = NO`).  
4. **BLOCKER_4:** Direct NguyenKT↔DaoMT κ not yet computed as principal reliability.  
5. **BLOCKER_5:** Zanellati et al. 2024 not yet integrated into Related Work / Table II.

## Manuscript files

Live TLT sources remain under `12_manuscript/TLT/` (not overwritten). Versioned revised manuscript **not** created yet (Phase 20 prerequisite incomplete).
