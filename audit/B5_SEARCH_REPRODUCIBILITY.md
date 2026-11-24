# B5 — Search reproducibility

**Date:** 2026-11-13. **Scope:** this package only. No locked file was edited. N, N_G, N_S, N_{G∩S}, 0/37, and 1/37 were not changed. DyGKT was not removed. P0 was not cited.

## 1. Table S-Search

`12_manuscript/TLT/supplementary/Table_S-Search.csv` is copied from `03_search/search_log.csv`.

| Check | Result |
|---|---|
| Rows | 16 (SRCH_001–SRCH_016) |
| Columns required by the brief | database, exact_query, search_fields, filters, run_date, returned_records |
| Extra columns | search_id, query_family, logged_export_filename, notes |
| Run date | 2026-08-26 on every row |
| Sum of returned_records | 2,017 (142+58+168+64+185+72+194+61+286+112+248+96+135+63+88+45) |
| Export files on disk | Not deposited. Counts are the logged totals, not a recount. |

The `notes` column records the two defects already written in `audit/A1_QUERY_GAP_ANALYSIS.md`:

- Q-G and Q-S term lists are not the same across databases.
- The arXiv strings (SRCH_013, SRCH_014) use `OR`, so a title containing "knowledge tracing" matches without a graph or self-supervised term.

## 2. Main text

The same three edits are in `main_tlt_anonymous.tex`, `main_tlt_full.tex`, and `manuscript_TLT_FORMATTED_v1.3.tex`.

- Literature-search subsection: the Scopus Q-S string (SRCH_010, 112 records) is quoted, and the other fifteen strings are pointed to Supplementary Table S-Search, including the two defects.
- PRISMA subsection: the five removed identifiers are named, with the reason recorded in Supplementary Table S-PRISMA-5, and the KT### identifier system is explained.
- QA paragraph: the old sentence "Extra inventory IDs KT078 and KT080–KT083 are excluded" now points at that verification table.

An index entry is in `TLT_Supplementary_Evidence_Tables.md`, section 8b.

## 3. The five removals (from the deposited table only)

Source: `12_manuscript/TLT/supplementary/Table_S-PRISMA-5.csv`. B5 did not re-query Crossref. The 2026-09-15 check is used as recorded.

| ID | Recorded problem |
|---|---|
| KT078 | Claimed DOI `10.1609/aaai.v39i1.30500` recorded as Crossref HTTP 404; no PDF in `14_references/` |
| KT080 | Claimed DOI `10.1145/3690624.3709500` recorded as Crossref HTTP 404; no PDF |
| KT081 | Claimed DOI `10.24963/ijcai.2025/450` recorded as resolving to a different paper |
| KT082 | Claimed DOI `10.1145/3627673.3679900` recorded as resolving to a different paper |
| KT083 | Claimed DOI `10.1016/j.neunet.2026.107500` recorded as Crossref HTTP 404; no PDF |

Each row in that table says the record had been marked `INCLUDE_FULLTEXT` and was dropped when a legacy set of 42 was reconciled to the locked set of 37. Whether those five titles exist under different DOIs is **NEEDS_EVIDENCE**. B5 does not assert that the papers do not exist, only that the deposited verification rejected the claimed DOI.

## 4. Why the KT### labels have gaps

- The labels that remain in the coded core include KT076, KT077, and KT079 (`tables/sparse_coldstart_audit_v1.9.csv` and `tables/graph_taxonomy.csv`).
- KT078 and KT080–KT083 are the five rows of Table S-PRISMA-5.
- So the gap is the five removed expansion identifiers, not a missing KT079.
- The labels are inventory identifiers from the seed file and the expansion coding folders. They are not a numbering of the 140 full-text records and not a renumbering of the 37 papers.
- A step-by-step assignment log that would show when each identifier was issued is **not deposited** (**NEEDS_EVIDENCE** for the assignment procedure itself).

## 5. What this package does not do

- It does not rerun the 16 searches. An outsider still cannot confirm that Scopus returns a count near 531 until someone runs SRCH_009–SRCH_016 and deposits the exports.
- It does not change the corpus or any locked count.

B5_SEARCH_TABLE_COMPLETE = YES
