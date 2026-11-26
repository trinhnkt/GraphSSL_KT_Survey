# TLT revision changelog — 2026-11-25 start

Versioned work products only. Live manuscript counts **not** overwritten.

| Section / artifact | Old statement | New statement | Reason | Source file | Verification |
|---|---|---|---|---|---|
| Venue-probe 10 candidates | “not read in full / not coded” | AI full-text/OA review table created; 5 PRIMARY_CORE (1 already in N=44); 5 UNCERTAIN no PDF | Phase 1 | `05_screening/KNOWN_CANDIDATES_FULLTEXT_REVIEW_v1.csv`; `audit/KNOWN_CANDIDATES_GATEWAY_AUDIT.md` | AI_PRIMARY_REVIEW; human still REQUIRED |
| Final search update | Implied completeness risk only | Explicit `FINAL_SEARCH_UPDATE_COMPLETED = NO` | Phase 2; no DB access | `audit/FINAL_SEARCH_UPDATE_STATUS.md` | Documented |
| Corpus freeze | N=44 live | **Not refrozen** (STOP GATE) | UNCERTAIN candidates that may pass gateway | `audit/TLT_REVISION_MASTER_STATUS_2026-11-25.md` | Freeze blocked |
| Screening reliability | Manuscript subset wording | Regenerated table from deposited pairs only | Phase 4 | `tables/SCREENING_RELIABILITY_FINAL.csv` | REC_0047 matches adjudication CSV |
| Coding reliability | Emphasized AI vs NguyenKT / AI vs DaoMT | Direct NguyenKT↔DaoMT pre-adjudication κ computed | Phase 5 | `06_coding/inter_rater_human_human_20papers.csv`; `tables/HUMAN_HUMAN_CODING_RELIABILITY.csv`; `audit/HUMAN_HUMAN_KAPPA_REPORT.md` | Macro over defined fields only |
| Related work Zanellati | Absent | Metadata verified; patch pending | Phase 6 | `audit/ZANELLATI_2024_METADATA.md` | DOI verified; tex not yet edited |
| Title | Sparse-Concept Settings | Recommend Option B (lens wording) | Phase 14 | `audit/TITLE_RECOMMENDATION.md` | Author decision PENDING |
| AI disclosure | Existing Cursor sentence | Role-split draft | Phase 12 | `audit/AI_DISCLOSURE_FINAL.md` | Author approval PENDING |

## Not changed in live tex/PDF

Abstract, corpus counts, SSL taxonomy figure, Table II, Methods reliability emphasis, Conclusion — awaiting Phase 3 freeze clearance.
