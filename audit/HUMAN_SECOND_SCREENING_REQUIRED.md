# Human second screening required

Date: 2026-11-24.
This package prepares empty sheets. It does not fill a human decision, does not copy a primary decision into the human columns, and does not compute Cohen's kappa.

**SELECTION_RELIABILITY_COMPLETE = NO**

## Records available

| File | Rows | What it is |
|---|---:|---|
| `05_screening/title_abstract_screening_v1.0.csv` | 43 | One screener label, `AI_ASSISTANT`, on every row. 42 rows have a title. 1 row is a collapsed note. |
| `06_fulltext/fulltext_screening_v1.0.csv` | 48 | One screener label, `AI_ASSISTANT`, on every row. Tiers: PRIMARY_CORE 42, PRIMARY_ADJACENT_SPARSE 3, PRIMARY_ADJACENT_METHOD 1, EXCLUDE_FULLTEXT 1, BACKGROUND 1. |
| `12_manuscript/TLT/supplementary/supplementary_prisma_exclusions.csv` | 48 | Same record ids as the full-text file. Not a separate exclusion ledger. |
| `04_deduplication/deduplication_audit_v1.0.csv` | 34 | Duplicate-group notes. Not the deduplicated record list. |
| `03_search/search_log.csv` | 16 search rows | Query totals. Not title/abstract decisions. |
| `03_search/venue_extension_candidates_v1.9.csv` | 10 | Candidates marked `TITLE_ABSTRACT_CANDIDATE_NOT_CODED` and `screening_record_found_in_repo = NO`. Not screened rows. |
| `05_screening/inter_rater_fulltext_SEVEN_BLIND_EMPTY_2026-11-23.csv` | 7 | Empty full-text sheet for seven later papers. Not the protocol sample. Decision cells are still empty. |
| `05_screening/inter_rater_fulltext_SEVEN_PHUONG_2026-11-23.csv` | 7 | A filled sheet for those same seven papers. It is not the 25 percent sample and it is not the full-text exclusion list. Its labels were not copied into the human files below. |
| `12_manuscript/TLT/supplementary/Table_S-PRISMA-5.csv` | 5 | Corpus-verification removals (KT078, KT080–KT083). Not title/abstract screening rows and not the full-text exclusion ledger. |

The 42 titled title/abstract rows are `INCLUDE_FULLTEXT`. The collapsed row is `REC_0043-REC_0140`, title `Various candidate titles`, note `Excluded 610 non-matching title/abstract records`. That note is not 610 records. It was not expanded.

The one full-text exclusion row is `REC_0047` (`EXCLUDE_FULLTEXT`). `REC_0048` is `BACKGROUND`, not `EXCLUDE_FULLTEXT`. No deposited full-text row has tier `UNCERTAIN`.

Deposited title/abstract rows do not contain abstract text. The human sheets use a DOI locator where the full-text file has a DOI for that record id. They do not contain the primary decision, the exclusion code, the screener id, or the notes that state a decision.

## Records missing

The complete 750-row record-level title/abstract ledger does not exist.

Also absent:

- `records_deduplicated.csv`
- a row list of 610 title/abstract exclusions
- a row list of 103 full-text exclusions
- `inter_rater_screening.csv`
- `inter_rater_fulltext.csv`
- any deposited title/abstract row labeled `UNCERTAIN`

The printed stage counts 750, 610, 140, and 103 are report arithmetic. They were not turned into rows.

## Sample size required

Protocol section 20.1 requires a second coder to screen 25 percent of the deduplicated records, plus every record the first coder marked `UNCERTAIN`.

That deduplicated ledger is missing, so the historical 25 percent sample was not drawn. The figure 750 was not used as a denominator and was not reconstructed.

From the records that do exist, the screenable title/abstract pool is the 42 rows that have a title. `REC_0043-REC_0140` was left out of the draw because it has no title to screen.

Prepared sample: **11** rows, which is `ceil(0.25 × 42)`. Random seed **20261113**. Draw: `random.Random(20261113).sample` on the 42 record ids sorted alphabetically, then the chosen ids written in sorted order. Uncertain rows in this file: **0**, so none were added.

File: `05_screening/HUMAN_SECOND_SCREEN_TITLE_ABSTRACT.csv`.

Record ids in that file: REC_0001, REC_0002, REC_0004, REC_0005, REC_0007, REC_0009, REC_0012, REC_0024, REC_0030, REC_0033, REC_0040.

The locator for REC_0040 is the DOI stored on the deposited full-text row, `10.24963/ijcai.2025/450`. `Table_S-PRISMA-5.csv` already records that this DOI resolves to a different paper. The sheet still carries the deposited locator. It was not replaced.

This 11-row sheet is not a 25 percent sample of a 750-row ledger. Every titled row in the source file carries the same primary label, so the sheet cannot represent exclusion decisions that were never stored as rows.

## Full-text exclusions requiring second review

Protocol section 20.2 requires a second review of every `EXCLUDE_FULLTEXT` and every full-text `UNCERTAIN`, and at least 25 percent of all full-text eligibility decisions.

Deposited `EXCLUDE_FULLTEXT` rows: **1** (`REC_0047`). Deposited full-text `UNCERTAIN` rows: **0**.

File: `05_screening/HUMAN_SECOND_SCREEN_FULLTEXT.csv` (that one row).

The 103-row full-text exclusion list is missing and was not reconstructed. One exclusion row does not meet the rule that at least 25 percent of all full-text eligibility decisions are double-screened. A 25 percent sample of the 48 deposited full-text rows was not added, because those other rows are not exclusion records and the historical eligibility ledger is absent.

## Human sheets

Both sheets use these columns:

`record_id`, `title`, `abstract_or_locator`, `primary_decision_HIDDEN_OR_SEPARATE`, `human_second_decision`, `human_exclusion_code`, `human_screener_name`, `note`.

`primary_decision_HIDDEN_OR_SEPARATE` is the token `HIDDEN` on every row. The primary label stays in `title_abstract_screening_v1.0.csv` and `fulltext_screening_v1.0.csv`.

`human_second_decision`, `human_exclusion_code`, `human_screener_name`, and `note` are empty.

Give the screener only the two human CSV files. Do not send this audit, the two source screening CSVs, the Prisma exclusion copy, or the seven-row Phương sheet. Those files show primary labels or other decisions.

The person who fills the sheets must not be an author of the survey. This assistant does not fill them.

## Whether selection reliability can be computed

No. The human decision columns are empty. Cohen's kappa was not calculated.

**SELECTION_RELIABILITY_COMPLETE = NO**

