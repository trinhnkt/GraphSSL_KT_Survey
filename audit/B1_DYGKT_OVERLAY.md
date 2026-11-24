# B1 — DyGKT numeric overlay

**Date:** 2026-11-16
**Decision:** author adopted the recommendation to remove the DyGKT/ASSIST17 numeric overlay from the main manuscript and to keep DyGKT in the 37-paper corpus.
**B1_OVERLAY_REMOVED_FROM_MAIN = YES**

## What left the main text

Removed from `main_tlt_anonymous.tex`, `main_tlt_full.tex`, and `manuscript_TLT_FORMATTED_v1.3.tex`:

- The abstract sentence that said the survey reports equal-width ECE on author DyGKT/ASSIST17.
- The reliability paragraph that reported ECE 0.0361, Brier 0.1770, AUC 0.8025, and n = 94,156.
- The subsection “Why DyGKT, and which setting,” including the inductive AUC 0.8035.
- Pointers to that overlay in the notation row, the Shen comparison, the comparison table, the contribution list, the protocol-deviation bullet, the T3 checklist, the calibration recommendation, the benchmark disclaimer, and Contribution 4.

The same claim was removed from both cover letters and from `12_manuscript/HIGHLIGHTS.md`.

After the edit, each of the three live tex files has 0 occurrences of `0.0361` and 0 occurrences of `DyGKT/ASSIST17`. Each still has 6 occurrences of `KT038` and 20 occurrences of the string `0/37`. The two KT038 table rows remain: DyGKT is still coded as dynamic-interaction Graph-KT and as interaction-sparsity only.

## What did not change

- N = 37, N_G = 36, N_S = 9, N_G∩S = 8.
- Manuscript ECE reporting stays 0/37. The keyword scan and the CL4KT calibration plot stay.
- The word “overlay” that remains in the method section is the H2 sparse-protocol overlay, not the DyGKT run.
- `_backup_before_v1.9` was not edited. Compiled PDFs were not rebuilt, so an opened PDF can still show the old sentences.
- The lab record still holds the run numbers: `12_manuscript/TLT/supplementary/DYGKT_ASSIST17_REPRODUCTION_MANIFEST.md` and the bin table. Both the manifest and `TLT_Supplementary_Evidence_Tables.md` are marked withdrawn from the main text. The earlier CASE A KEEP note in `12_manuscript/TLT/audit/DYGKT_REPRODUCTION_AUDIT.md` is the record of the 2026-09-15 reproduction. It is not the current main-text decision.

## Stop

No corpus count was rewritten. No submission.
