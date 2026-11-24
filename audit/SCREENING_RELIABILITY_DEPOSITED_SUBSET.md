# Screening reliability — deposited independently double-screened subset

Date: 2026-11-24.

## 1. Historical limitation

A complete historical record-level ledger for all reported screening stages is not available.
The printed stage counts 750 title/abstract records and 103 full-text exclusions were not reconstructed.

## 2. Available paired subset

### Title/abstract

- n paired: 11
- denominator of available/deposited titled pool: 42
- share of that deposited pool: 11/42 = 26.2% of the deposited/available titled title/abstract screening subset
- n agree: 10; n disagree: 1
- raw agreement: 0.909091
- Cohen's kappa: NA
- kappa_status: UNDEFINED_NO_CODER_VARIATION

Coder A category counts: INCLUDE_FULLTEXT=11.

Coder B category counts: INCLUDE_FULLTEXT=10, UNCERTAIN=1.

Confusion matrix (rows = decision_A, columns = decision_B):

| decision_A \ decision_B | INCLUDE_FULLTEXT | UNCERTAIN |
|---|---:|---:|
| INCLUDE_FULLTEXT | 10 | 1 |
| UNCERTAIN | 0 | 0 |

Kappa is NA because Coder A has no category variation on this subset (all `INCLUDE_FULLTEXT`).
A numeric kappa is not forced. Raw agreement remains reportable at n = 11.

This is **not** 11/750 and is **not** described as 25% of the historical screening population.

### Full-text

- n paired: 1
- n agree: 0; n disagree: 1
- raw agreement: 0.000000
- Cohen's kappa: NA
- kappa_status: UNDEFINED_NO_CODER_VARIATION

Coder A category counts: EXCLUDE_FULLTEXT=1.

Coder B category counts: PRIMARY_ADJACENT_METHOD=1.

Confusion matrix:

| decision_A \ decision_B | EXCLUDE_FULLTEXT | PRIMARY_ADJACENT_METHOD |
|---|---:|---:|
| EXCLUDE_FULLTEXT | 0 | 1 |
| PRIMARY_ADJACENT_METHOD | 0 | 0 |

Kappa is NA because n = 1 provides no usable category variation for either coder.
Raw agreement is 0/1 on the single paired exclusion row.

## 3. REC_0047 disagreement

`EXCLUDE_FULLTEXT` versus `PRIMARY_ADJACENT_METHOD`.
Adjudication is **complete** (`REC_0047_ADJUDICATED = YES`). Adjudicator: Nguyễn Văn Hậu. Final decision: `PRIMARY_ADJACENT_METHOD`. Pre-adjudication raw agreement remains 0/1.
Correct GKT-CD PDF is deposited (`REC_0047_CORRECT_PDF_AVAILABLE = YES`): `14_references/GKT-CD Make Cognitive Diagnosis Model Enhanced by Graph-based Knowledge Tracing.pdf`. DOI and title match. Human full-text reconfirmation is complete (`NEEDS_HUMAN_FULLTEXT_VERIFICATION = NO`); sheet `05_screening/HUMAN_SECOND_SCREEN_FULLTEXT_PHUONG1_VERIFIED.csv` keeps `PRIMARY_ADJACENT_METHOD`.
The wrong Cognitive Situation PDF was not used.

## 4. Scope limitation

These coefficients characterize the deposited independently double-screened subset and are not estimates of reliability for the full historical 750-record title/abstract stage or the 103 reported full-text exclusions.

## 5. Distinguish screening from coding reliability

Screening reliability concerns inclusion/exclusion decisions. The existing 20-paper coding reliability concerns agreement on coded study attributes. The two analyses are separate and their kappas must not be pooled.

## 6. Missing evidence

- missing historical ledger for 750 / 610 / 103 stages
- unpaired title/abstract rows in this pass: 0
- unpaired full-text / extension rows logged: 7 (includes seven EXT ids with second labels but no deposited primary REC decision)
- REC_0047 adjudication completed by Nguyễn Văn Hậu (`PRIMARY_ADJACENT_METHOD`)
- correct GKT-CD PDF is deposited and human-verified

Pair files:

- `05_screening/inter_rater_screening.csv`
- `05_screening/inter_rater_fulltext.csv`
- `05_screening/inter_rater_screening_unpaired.csv`
- `05_screening/inter_rater_fulltext_unpaired.csv`
- `tables/SCREENING_RELIABILITY_SUMMARY.csv`

**SCREENING_RELIABILITY_SUBSET_COMPLETE = YES**

YES here means the paired files are valid, the calculations are reproducible, and the scope wording is the deposited subset only.
It does **not** mean the historical 750/103 screening reliability has been recovered,
and it does **not** mean REC_0047 adjudication or PDF verification is finished.
