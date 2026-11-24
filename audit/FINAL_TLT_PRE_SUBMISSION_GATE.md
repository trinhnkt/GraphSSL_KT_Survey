# Final TLT pre-submission gate

**Date:** 2026-11-22
**Manuscript:** `12_manuscript/TLT/main_tlt_anonymous.tex` and the two sibling live files
**Clean build:** pdflatex, BibTeX, pdflatex, pdflatex on 2026-11-22. Anonymous PDF 17 pages. Full and formatted PDFs 18 pages. No undefined-citation line in the final logs. Anonymous PDF text: `0.0361` count 0, `PRISMA 2020` count 0, `0/37` count 21, Shukurlu present.

**READY_FOR_SUBMISSION = NO**

The rule for YES is that every level-A package passes and no remaining B item affects validity. A1 and A3 do not pass. B2 is still open. This file does not authorize submission.

## Level A

| Package | Gate | Evidence |
| --- | --- | --- |
| A1 Corpus | **FAIL** | The submitted set is frozen at 37 (`audit/A1_CORPUS_FREEZE_2026-11-18.md`). The coverage checks below are not all pass. |
| A3 Screening reliability | **FAIL** | `A3_KAPPA_COMPUTED = NO`. No second screener and no screening pair file (`audit/A3_SCREENING_RELIABILITY.md`). |
| A2 Calibration | **PASS** | ECE stays 0/37. The text-layer scan finds no Brier score. RMSE in 12 PDFs is reported as overall prediction error, not as ECE or Brier. |
| A4 RQ synthesis | **PASS** | RQ1, RQ2, and RQ3 are answered from coded fields. The eight Graph+SSL augmentation phrases were re-read from the PDFs. |

## Checklist

| Check | Result | Basis |
| --- | --- | --- |
| Supplementary search complete | **FAIL** | Crossref and OpenAlex were queried on 2026-11-22 (`audit/A1_OPEN_SOURCE_COVERAGE_2026-11-22.md`). ACM SRCH_001 and SRCH_002 and WoS SRCH_011 and SRCH_012 still have no rerun file. The named 2026-08-26 export files are not deposited. |
| Seed recall reported | **FAIL** | The manuscript says the legacy list of 34 records was used only for recall checking. No recall fraction is reported. `present_raw` remains NEEDS_EVIDENCE, so no x/34 sentence was written. |
| DECKT status resolved | **PASS as a decision** | DECKT stays outside the 37. It was not screened in and has no exclusion code. |
| DTransformer status resolved | **PASS as a decision** | DTransformer / KT040 stays seed background and is not in the 37. |
| Snowballing logged | **LOGGED, NOT CLOSED** | OpenAlex snowball of the nine SSL papers and Xu is in `tables/A1_SNOWBALL_OPENALEX_2026-11-22.csv`. It recovers DECKT, CoSKT, Han et al. 2024, and HCMKT. It does not assign fate codes, and the 2026-11-11 venue probe stays unscreened. |
| Final corpus frozen | **PASS for the submitted 37** | Author decision 2026-11-18. The seven candidates and the ten venue-probe papers stay out. |
| Title/abstract second screen | **FAIL** | Deposited file has 43 rows, all `AI_ASSISTANT`. The 610-exclusion sample cannot be drawn. |
| Full-text second screen | **FAIL** | Deposited file has 48 rows, all `AI_ASSISTANT`. |
| Human coder B only | **FAIL for selection** | Screening has no human second coder. The 20-paper coding κ is a different package and is not a screening κ. |
| κ mathematically valid | **FAIL for selection** | No screening κ. Coding κ on five defined fields is reported separately and is not pooled. |
| Disagreements adjudicated | **FAIL for selection** | There is no second screening decision to adjudicate. Five coding cells were adjudicated on the 20-paper sample. |
| ECE / Brier / RMSE / NLL / reliability diagram audited | **PASS** | `audit/A2_CALIBRATION_SCOPE.md` and `supplementary/calibration_rmse_textlayer_v1.10.csv`. KGNN-KT has no text layer. |
| Claims no broader than the coded field | **PASS** | The live sentence is ECE 0/37, no Brier score in the scan, and RMSE kept as overall prediction error. |
| RQ1 answered | **PASS** | Provenance, encoder, and the reporting condition for a leakage-free claim. No leakage percentage is given. |
| RQ2 answered | **PASS** | Provenance-by-encoder table and the 36-row graph table, including temporal backbone and fusion columns. |
| RQ3 answered | **PASS** | Four pretext families, \(N_S=9\), and the page-checked augmentation column. |
| No RQ answered by “not coded” | **PASS for RQ1–RQ3** | Group B is labeled as not a coded result. It is the open list under RQ6, not the answer to RQ1–RQ3. |
| Cold-start equation valid for multi-KC items | **PASS** | The filter uses \(\mathrm{KC}(x_t) \subseteq \mathcal{K}\setminus\mathcal{K}_{\mathrm{cold}}\) and states that an exercise with one cold KC is removed. The removed-interaction fraction is not computed. |
| LLM–GNN dimensions valid | **PASS by omission** | That weight equation is not in the current draft (`audit/B4_EQUATION_CHECK.md`). |
| CL4KT mechanism verified | **PASS** | `audit/B3_CL4KT_AUGMENTATION_AUDIT.md`. |
| Exact search strings available | **PASS** | Sixteen strings are in `03_search/search_log.csv`. Their logged counts sum to 2,017. The export files named in that log are not deposited. |
| Five verification removals explained | **PASS** | The manuscript names KT078 and KT080–KT083 and the 2026-09-15 Crossref result. KT076, KT077, and KT079 remain. |
| KT### system explained | **PASS** | The manuscript states that these labels are inventory identifiers, not a numbering of the 37 papers or of the 140 full-text records. |
| Internal tokens removed from the main paper | **PASS** | `MODEL_DEFINED`, `PRIMARY_CORE`, `GNN_GENERIC`, and `SPARSE_INTERACTION_ONLY` are absent from `main_tlt_anonymous.tex`. Readable names are used. |
| References verified | **FAIL** | The 2026-11-22 recheck matches the printed pages for Piech (505–513), SAKT (384–389), and pyKT (18542–18555). DGMN is still the Crossref early-access record (2022, pp. 1–13, no volume), and the Cursor URL was not re-opened. The bibliography was not edited. See `audit/B11_EXTERNAL_RECHECK_2026-11-22.md`. |
| Redundant figures removed | **PASS** | C1. The taxonomy figure remains. The paired provenance and encoder count figure does not. |
| Disclaimers consolidated | **PASS** | One Scope of Claims paragraph. Threats to Validity kept. |
| Group B shortened | **PASS** | One paragraph. It does not add a coded result. |
| Notation cleaned | **PASS** | \(N_{\mathrm{rec}}\), \(N\), and \(n\) are separated. The notation table does not repeat the 0/37 audit result. |

## Remaining B item that can affect validity

B2, the SSL codebook change, is not started. It stays a supervisor decision. If that codebook change is made, \(N_S\) can change. Until that decision is recorded, the printed \(N_S=9\) is the current coding, not a redesigned taxonomy.

The five unverified reference details do not change \(N\), \(N_G\), \(N_S\), 0/37, or 1/37. They still block the “references verified” row.

## Counts confirmed, not changed

\(N_{\mathrm{rec}}=2{,}017\), \(N=37\), \(N_G=36\), \(N_S=9\), \(N_{G\cap S}=8\), provenance display 19/8/9, strict KC cold-start 0/37, item cold-start 1/37, learner cold-start 0/37, interaction-drop evaluation 1/37, manuscript ECE 0/37.

STOP. Do not submit from this gate.
