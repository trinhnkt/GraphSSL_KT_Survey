# Score-improvement actions and open blockers (2026-11-03)

Scope: actions taken after the contribution review (score ~6.5/10). No locked file edited. No label fabricated. Headline counts unchanged (`0/37` ECE, `0/37` strict KC, `1/37` item CS, provenance 18/9/9, kappa 0.97 / 0.96 not pooled).

## A. Done in the manuscript (`main_tlt_anonymous.tex`, `main_tlt_full.tex`, `manuscript_TLT_FORMATTED_v1.3.tex`)

| # | Change | Reason |
|---|---|---|
| 1 | Group B (B1-B4) cut from four subsubsections with equations to one paragraph; notation row for `W` removed | Nothing in B is a coded result; equations pulled the paper away from an audit |
| 2 | RQ1 reworded to what is measured (provenance, encoder, reporting condition for a leakage-free claim) | RQ1 asked for leakage risk, which is not measured |
| 3 | Sec. III-E states RQ1 scope and that `graph_leakage_risk` values are not reported (see C2) | Avoid implying a measured leakage rate |
| 4 | "mean 0.76" corrected: it is the corpus mean, not the MODERATE-tier mean (MODERATE mean is about 0.73) | Misattribution |
| 5 | QA7 applicability sensitivity added to Sec. VI | Protocol Sec. 22.1 allows `NA`; headline tiers depend on that choice |
| 6 | Abstract: inclusion was not second-screened; reliability only for the 20-paper coding sample | Matches what the repository supports |

QA7 sensitivity result (components from `supplementary_quality_scores.csv`, QA6 capped at 2):

- Primary (QA7 applicable for all 37): 11 HIGH / 26 MODERATE / 0 LIMITED, mean 0.757.
- QA7 `NA` for the 35 papers with no cold-start claim (HHSKT and SINKT keep QA7): 31 HIGH / 6 MODERATE / 0 LIMITED, mean 0.858. 20 papers change tier; none moves down.
- Per-paper table: `supplementary/supplementary_quality_scores_v2_QA7_sensitivity.csv`.

## B. Not done (cannot be done by the assistant)

1. **Second-screener IRR for title/abstract and full-text.** Needs a second human screener and real labels. Do not create labels. Until then the paper must keep the "not second-screened" wording.
2. **Locator-level recoding of "train-only graph stated".** Needs page-level reading of each log-derived Graph-KT paper (PDFs in `14_references/`).
3. **Submission PDFs not rebuilt.** `main_tlt_anonymous.tex` and `main_tlt_full.tex` compile cleanly to a temp directory (0 LaTeX errors, no large overfull boxes), but the PDFs in the package were not overwritten. Rebuild after C1-C5 are settled.

## C. Findings that need an author decision before submission

**C1. Screening records do not document the PRISMA flow and name an AI screener.**
`05_screening/title_abstract_screening_v1.0.csv` has 43 records and `06_fulltext/fulltext_screening_v1.0.csv` has 48; every row has `screener_id = AI_ASSISTANT`. The manuscript reports 750 deduplicated, 140 full-text, 37 included, and says decisions were made by "a primary screener" with team consensus; the Acknowledgment says all inclusion decisions were made by the authors. These statements need to be reconciled with who actually screened and where the 750/140 decision records are. I did not edit the screener wording because I cannot establish the fact.

**C2. `graph_leakage_risk` values in `07_coding/*_CODING_v1.0.md` are not reportable.**
They are `REVIEWER_INFERRED`, use near-templated notes, and carry no page locators. Example: nearly all non-`POTENTIAL` rows read "LOW".

**C3. v1.0 coding files disagree with the manuscript taxonomy table.**
Examples (coding file vs `tables/graph_taxonomy.csv`):

| Paper | v1.0 coding file `graph_provenance` | Manuscript table |
|---|---|---|
| KT016 SKT | `EXTERNAL_FIXED` | Model-defined |
| KT052 Capsule GNN | `EXTERNAL_FIXED` | Model-defined |
| KT036 TSKT | `JOINTLY_LEARNED_TRAINING` (title also differs: "Spatiotemporal Evolution") | External (text semantics) |

The v1.0 files date from 2026-08-26 and may be superseded by the PDF-strict recode of 2026-09-13, but the repository does not say which is authoritative. Confirm against the PDFs before submission, because 18/9/9 depends on it.

**C4. Provenance categories are collapsed relative to the locked codebook.**
The codebook has eight `graph_provenance` values, including `FULL_DATA_INFERRED` and `PRECOMPUTED_UNCLEAR_SPLIT`, and defines `MODEL_DEFINED_FIXED` as not inferred from interaction data. The manuscript uses three values and describes `MODEL_DEFINED_FIXED` as including co-occurrence constructions. If co-occurrence graphs are built from logs, they may belong in a data-inferred class, which would change both the 18/9/9 split and the leakage discussion. Not verified against the papers.

**C5. `supplementary/supplementary_quality_scores.csv` is stale.**
`raw_score`/`tier` do not equal the component sum for KT010, KT012 (raw 11 vs 10), KT069, KT076, KT079 (13 vs 12, listed HIGH), KT070, KT077 (14 vs 13), and QA6 is uncapped for KT038, KT066. The manuscript counts (11 HIGH / 26 MODERATE) match the capped component sums, so the manuscript is right and the released CSV is wrong. Replace it in the supplementary package with the v2 file, or regenerate.

## D. Expected effect on the review score

Closing A moved the paper from about 6.5 to about 7. Sequence 1--5 (2026-11-06) closed C1 (wording, not a new ledger), C3 (PDF lock), C4 (display-collapse deviation), C5 (QA CSV), and rebuilt PDFs. Remaining path to 7.5--8 is B1 (human second screener) plus locator-level train-only coding (B2).
