# Locked manuscript counts (v1.8)

**Date:** 2026-11-06  
**Supersedes:** `LOCKED_COUNTS_v1.7.md` after PDF-strict provenance check of KT016 / KT036 / KT052 and QA CSV reconciliation.  
**Rule:** Counts in `main_tlt_anonymous.tex` / `main_tlt_full.tex` must match the CSVs below.

## Sources

- `tables/graph_taxonomy.csv`
- `tables/ssl_taxonomy.csv`
- `tables/sparse_coldstart_audit.csv`
- `supplementary/supplementary_quality_scores.csv` (QA6 capped; 37 rows)

## Recode (v1.7 → v1.8)

| Paper | Field | v1.7 | v1.8 | PDF basis |
|---|---|---|---|---|
| KT036 TSKT | graph_provenance | EXTERNAL_FIXED | MODEL_DEFINED_FIXED | BERT is item-text features; same-KC knowledge-space edges (Sec. 4.2–4.3.1) |
| KT036 TSKT | graph_source | TEXT_SEMANTICS | HETEROGENEOUS_SCHEMA | Same |
| KT016 SKT | display provenance | MODEL_DEFINED_FIXED | MODEL_DEFINED_FIXED (kept) | Mixed 8-way: Junyi expert; ASSISTments transition. Three-token rule keeps MODEL_DEFINED. |
| KT052 Capsule | display provenance | MODEL_DEFINED_FIXED | MODEL_DEFINED_FIXED (kept) | PDF: no expert pre-definition. 2026-08-26 coding file EXTERNAL_FIXED superseded. |

Provenance display: **19 / 8 / 9** (model-defined / external / dynamic). Three-token collapse documented as DEV-20261106-02.

## Unchanged

- Identified 2017 (search log). Stage counts 750 / 140 / 103 are search-expansion report arithmetic without a deposited row ledger (DEV-20261106-01).
- Primary core 37; $N_G=36$, $N_S=9$, $N_{G\cap S}=8$.
- Encoder totals unchanged.
- Sparse: generic 37/37; strict KC 0/37; item CS 1/37; learner CS 0/37.
- QA (capped, 37 rows): HIGH 11; MODERATE 26; mean 0.76. Identifiers: KT029, KT033, KT035, KT038, KT044, KT050, KT060, KT064, KT066, KT070, KT077.
- ECE manuscript-reporting 0/37.

## Do not

- Pool NguyenKT + DaoMT κ.
- Fabricate screening second-screener labels.
- Report `graph_leakage_risk` from v1.0 coding files (reviewer-inferred, no locators).
