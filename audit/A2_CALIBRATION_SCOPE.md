# A2 — Calibration scope of the 0/37 ECE claim

**Date:** 2026-11-20
**A2_T3_NARROWED = YES**
**ECE reporting count unchanged:** 0/37
**Locked codebook not edited.**

## What was already scanned

`12_manuscript/TLT/supplementary/calibration_keyword_scan_v1.9.csv` records a text-layer scan of the deposited PDFs for ECE, calibration strings, reliability-diagram or calibration-plot strings, Brier, and NLL or log-loss. KGNN-KT has no extractable text layer. Among the 36 scanned primary-core PDFs, ECE is 0 and Brier is 0. CL4KT is the only primary-core PDF with a calibration plot (`Figure 7: Calibration binned by predictions on assist09`) and that plot has no summary statistic. Other `calibrat-` hits are citations of a calibrated Q-matrix. NLL strings in the earlier note are training objectives.

That scan did not include RMSE. The 2026-11-20 follow-up did.

## RMSE follow-up

Same 37 primary-core PDFs. Pattern: `RMSE` or `root-mean-square` / `root mean square`. Script: `audit/_a2_rmse_scan.py`. Contexts: `audit/_a2_rmse_contexts.txt`. Rows: `12_manuscript/TLT/supplementary/calibration_rmse_textlayer_v1.10.csv`.

Twelve PDFs contain the strings. In each, the surrounding text reports RMSE beside AUC or accuracy (sometimes also MAE or F1) as an overall prediction error. CL4KT is one of the twelve and is also the calibration-plot paper. PDKT-C describes the prediction as a value between 0 and 1 and then uses MAE and RMSE. The contexts do not call RMSE an ECE or a Brier score. Separate files outside the deposited PDF were not opened.

## Manuscript change

T3, the formative-assessment row, Recommendation 3, agenda A2, Contribution 4, and the abstract now say that the twelve RMSE reports are overall prediction errors and that an ECE or Brier report on the tutoring split is still absent. The recommendation to report ECE and Brier is unchanged. P0 is not cited.

## Not done

No new field was added to `coding_codebook_v1.0_LOCKED.md`. The twelve-row file is the survey record of this scan. N, N_G, N_S, and 1/37 were not changed.
