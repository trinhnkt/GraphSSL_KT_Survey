# B10 — Relationship between the TLT survey and P0

**Date:** 2026-11-18
**B10_COMPARISON_PAGE_WRITTEN = YES**
**B10_OPTION_CHOSEN = B**
**Decision recorded:** 2026-11-18, author instruction in the revision session. Submit the survey in parallel with P0. The survey does not cite P0. Agenda A2 stays the current recommendation to report ECE and Brier.

The manuscript was not edited. P0 was not cited. N, \(N_G\), \(N_S\), 0/37, and 1/37 were not changed. A2 already matched option B, so no sentence was rewritten.

## Sources

- Reviewer note, pages 15–16 and the source list on page 20: `15. Check list/2026.11.13/NhanXet_Survey_GraphSSLKT_Trinh_2026Nov13.pdf` (PGS.TS. Nguyễn Văn Hậu, 13/11/2026). Text extract: `audit/_b10_reviewer_extract.txt`.
- Live survey text read for this page: `12_manuscript/TLT/main_tlt_anonymous.tex` (research questions, T3, recommendations, agenda A1–A2, contributions). The same claims are in `main_tlt_full.tex` and `manuscript_TLT_FORMATTED_v1.3.tex`.

The P0 manuscript is not in this repository. A filename search under `D:\TRINH` found no file for that title. Cells in the P0 column are only what the 13/11/2026 note states. They are not a reading of P0.

## What the note calls P0

Title quoted by the reviewer: “When Overall AUC Hides Miscalibration: Evaluating Knowledge Tracing on Rarely Practiced Knowledge Components”.

Status in that note: being prepared for submission to IJIET, double-blind. This repository has no later acceptance, rejection, or submission receipt. The note also says the P0 draft declares Cursor, Grok, and Claude, and that Yan et al., arXiv:2606.14123, is cited in P0. Those two statements were not re-checked against a P0 file.

The reviewer summarizes P0’s central point as measuring calibration by knowledge-component frequency band. The numeric bands named in the B1 remedy (`<20`, `20–100`, `100–500`, `>500`) are the reviewer’s proposed expansion of a survey experiment. They are not copied here as P0’s method.

## Comparison

| Dimension | Survey (this TLT manuscript) | P0 (reviewer note only; manuscript not read) |
|---|---|---|
| Research question | Six questions on graph provenance and encoders, SSL pretext, sparse-concept and cold-start coding, reproducibility and calibration reporting, and the agenda that follows. The paper is a coding survey of published Graph/SSL-KT protocols. | Title: overall AUC can hide miscalibration, evaluated on rarely practiced knowledge components. The note does not quote a formal research-question list. |
| Corpus/data | Primary core of 37 Graph/SSL-KT papers, search-log sum 2,017, window through 2026-07-31. No new student-log experiment in the main text. | Not stated. No dataset list, sample size, or model list is in the note. |
| Method | Code published protocols. Agenda item A1 specifies a zero-exposure KC split (`pyKT-ColdStart`) and states that this paper does not report an executed run. | Reviewer: the work P0 has done is calibration measurement by KC frequency band. Procedure, models, and bins were not read. |
| Calibration | Manuscript ECE reporting is 0/37. Contribution 4 also says a keyword scan finds no Brier score and one calibration plot (CL4KT). Agenda A2 recommends ECE, Brier, and temperature scaling for future papers. T3 withholds a GO for acting on \(P(r=1)\) until ECE or Brier is reported on the decision split. | Reviewer: calibration by KC frequency band is P0’s content, and the removed DyGKT overlay was set aside partly because that experiment already belongs to P0. No ECE or Brier value from P0 is recorded here. |
| Sparse KC | Strict KC cold-start is 0/37. Item cold-start is 1/37 (SINKT). A1 defines zero training exposure, which is a different cut from “rarely practiced” as worded in the P0 title. The note does not say whether P0’s rare KCs include a zero-exposure split. | Title names rarely practiced knowledge components. The note does not define the frequency cut. |
| Contribution | Coding of graph provenance, SSL pretext, separated cold-start constructs, the 0/37 ECE reporting audit, and the T1–T3 evidence checklist. | Reviewer: an empirical calibration evaluation on rarely practiced KCs, where overall AUC can hide miscalibration. Exact claims, tables, and results were not read. |
| Overlap | A2 and T3 treat missing ECE/Brier as an open reporting gap and as a reason not to act on \(P(r=1)\). The reviewer says that gap is the work P0 has already done. A1 remains a zero-exposure benchmark specification, not that measurement. | Same reviewer statement: survey agenda A1–A2 and verdict T3 coincide with P0’s central point. Whether A1’s zero-exposure split is inside P0 is not stated. |
| Planned submission | IEEE TLT manuscript under revision in this repository. No submission date is recorded in the sources for this page. | Note of 13/11/2026: being prepared for IJIET, double-blind. No calendar date is given. |

## Overlap in one sentence

The survey tells a learning engineer that this Graph/SSL corpus does not report ECE, so \(P(r=1)\) is not evidence enough for skipping practice or assigning remediation. The reviewer says P0 already measures that calibration problem on rarely practiced knowledge components. Citing P0, or rewriting A2 as if the gap were filled, waits on the supervisor.

## Decision

**Chosen: B.** Submit in parallel. The survey does not cite P0. Agenda A2 keeps the recommendation to report ECE and Brier.

Checked on 2026-11-18 in `main_tlt_anonymous.tex`, `main_tlt_full.tex`, and `manuscript_TLT_FORMATTED_v1.3.tex`. A2 states that 0/37 manuscripts report ECE, recommends temperature scaling as a reporting practice, and says ECE and Brier are evaluated on the test set. A search of `12_manuscript` found no mention of P0, IJIET, arXiv:2606.14123, or KC frequency bands. The cover letters and highlights likewise do not name P0. That is the parallel-submission record: the editor letter does not cite P0.

Options A and C were not applied. A would cite P0 after an IJIET decision. C would add an anonymous citation.

The reviewer noted that two papers from the same group can carry the same calibration message without citing each other. Option B accepts that position. A later citation of P0 waits until P0’s double-blind review is no longer at risk and a separate decision says to add the citation.

## Stop

`B10_OPTION_CHOSEN = B`

VIII-A2 stays as written. No further B10 edit unless that decision is changed in writing.
