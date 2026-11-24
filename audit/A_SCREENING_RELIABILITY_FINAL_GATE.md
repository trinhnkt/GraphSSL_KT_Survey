# A — Screening reliability final gate

Date: 2026-11-24.

## Checklist

- [x] correct GKT-CD PDF status documented (`audit/REC_0047_CORRECT_PDF_STATUS.md`, `audit/REC_0047_PDF_VERIFICATION.md`)
- [x] wrong “Graph Knowledge Tracing in Cognitive Situation” file not used
- [x] REC_0047 has two independent decisions recorded (`EXCLUDE_FULLTEXT` vs `PRIMARY_ADJACENT_METHOD`)
- [x] REC_0047 adjudication status documented (`REC_0047_ADJUDICATED = YES`)
- [x] no AI-generated adjudication (adjudicator: Nguyễn Văn Hậu)
- [x] title/abstract paired file contains only true pairs (`05_screening/inter_rater_screening.csv`, n=11)
- [x] full-text paired file contains only true pairs (`05_screening/inter_rater_fulltext.csv`, n=1)
- [x] HIDDEN is never treated as a decision category
- [x] raw agreement calculated correctly (title/abstract 10/11; full-text 0/1)
- [x] kappa calculated only when mathematically defined (both stages NA: no coder variation)
- [x] no invariant field assigned kappa = 1
- [x] reliability described as deposited-subset only
- [x] no claim that subset represents all 750/103 records
- [x] screening kappa kept separate from coding kappa
- [x] Threats contains one consolidated selection-reliability paragraph
- [x] manuscript no longer says absolutely “no screening reliability exists”

## Numbers

| Stage | n_paired | raw agreement | Cohen kappa |
|---|---:|---:|---|
| Title/abstract | 11 | 10/11 = 0.909 | NA (`UNDEFINED_NO_CODER_VARIATION`) |
| Full-text | 1 | 0/1 = 0.000 | NA (`UNDEFINED_NO_CODER_VARIATION`) |

Scope line used in the summary table: `deposited independently double-screened subset only`.

Permissible share statement: `11/42 = 26.2% of the deposited/available titled title/abstract screening subset`. Not `11/750`.

`SCREENING_RELIABILITY_SUBSET_COMPLETE = YES` in `audit/SCREENING_RELIABILITY_DEPOSITED_SUBSET.md`.

Final adjudicated label for REC_0047: `PRIMARY_ADJACENT_METHOD` (does not change pre-adjudication raw agreement 0/1).

## Final flag

**A_SCREENING_RELIABILITY_DEFENSIBLE = YES**

Human actions for REC_0047 are complete:

1. Correct GKT-CD PDF deposited and DOI/title matched.
2. Human full-text reconfirmation on that PDF (`HUMAN_SECOND_SCREEN_FULLTEXT_PHUONG1_VERIFIED.csv`).
3. Human adjudication completed by Nguyễn Văn Hậu (`PRIMARY_ADJACENT_METHOD`).

This flag means the deposited-subset screening package is auditable and defensible. It does **not** mean historical 750/103 reliability has been recovered, and it does **not** authorize automatic submission.
