# B6 jargon audit

**Date:** 2026-11-14
**Package:** B6 only. Stop after this file.
**Reviewer source:** `15. Check list/2026.11.13/NhanXet_Survey_GraphSSLKT_Trinh_2026Nov13.pdf`, item B6.

## What changed

In the three live manuscripts, internal wording was replaced with readable names:

- `Sec.~22.1` and `Sec.~14` are gone from the body.
- The word `locked` is gone from the body.
- `.csv` paths and `\path{...}` pointers are gone from the body. Those paths are listed in `12_manuscript/TLT/supplementary/Table_S-Files.csv`.
- Underscore code tokens in prose and tables (`MODEL_DEFINED_FIXED`, `SPARSE_INTERACTION_ONLY`, `GNN_GENERIC`, and the other codes in the scan) now use the readable names in `12_manuscript/TLT/supplementary/Table_S-Tokens.csv`.

The same readable names were applied in the figure sources `fig_ssl_framework.tex`, `fig_taxonomy_2d.tex`, `fig_graph_construction_pipeline.tex`, `fig_meta_analysis_charts.tex`, and `fig_prisma_flow.tex`. In `fig_ssl_framework.tex`, the two editor boxes (“Locked codebook Sec. 14 tokens only” and “Mechanism notes are not families”) were removed. The box that names SINKT, Coda, KGNN-KT, R²GCurL, and STSKT as Graph-KT only was kept.

`_backup_before_v1.9/` was not edited. Locked protocol files were not edited. Figure PDFs were not recompiled in this package, so a PDF built before this edit can still show the old boxes until the figures are compiled again.

## Counts

No corpus count was changed. In `main_tlt_anonymous.tex` after the edit, the string `0/37` still occurs 22 times. `N_G = 36`, `N_S = 9`, and `N_{G \cap S} = 8` were not rewritten.

## What remains on purpose

The gateway display still writes `PRIMARY_CORE`, `GRAPH_BASED`, and `SELF_SUPERVISED` as formula symbols. The sentence immediately after that display defines them in words. The evidence-tuple display still writes `entity_id`, `field_name`, `coded_value`, `evidence_locator`, and `evidence_note` as formula symbols.

These are not body vocabulary: query labels `Q-G`, `Q-S`, `Q-P`, `Q-R`; the Scopus `TITLE-ABS-KEY` example kept for the search table; architecture names `GCN`, `GAT`, and `GGNN`; coder labels `NguyenKT` and `DaoMT`.

## Self-check

Searched the three live manuscripts and the five figure sources named above: `locked` = 0, `.csv` = 0, `Sec. 14` = 0, `Sec. 22.1` = 0.

`B6_JARGON_COMPLETE = YES`
