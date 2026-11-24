# C1--C3 — figures, notation, and QA display (2026-11-22)

Corpus stays \(N=37\). No count was changed. The locked codebook was not edited.

## C1

The taxonomy figure stays in the main text. The paired figure that printed provenance \(19/8/9\) beside the encoder bar chart was removed. Those two panels repeated counts already stated in the taxonomy caption, the provenance list, and the provenance-by-encoder table.

The encoder totals remain the rightmost column of that table. `figures/fig_meta_analysis_charts.pdf` is named in `12_manuscript/TLT/supplementary/README.md` and is not printed beside the provenance counts. `figures/fig_graph_construction_pipeline.pdf` is also omitted from the main text. Neither PDF was deleted.

## C2

| Symbol | Meaning in the live manuscript |
| --- | --- |
| \(N_{\mathrm{rec}}\) | Raw search-log records, \(2{,}017\) |
| \(N\) | Primary-core papers |
| \(n\) | A stated sample, or the number of predictions in the ECE sum |

The notation table no longer defines \(h_k^t\) or \(\mathbf{Z}^{(v)}\), which were not used in an equation. The ECE row no longer repeats the \(0/37\) audit result. The PRISMA figure source uses \(N_{\mathrm{rec}}\) for the search-log total. Highlights and both cover letters use the same symbol for that total.

## C3

Item counts are from `12_manuscript/TLT/supplementary/supplementary_quality_scores.csv` (37 rows; each raw score equals the sum of the eight items):

| Item | 0 | 1 | 2 |
| --- | --- | --- | --- |
| QA1 | 0 | 0 | 37 |
| QA2 | 0 | 0 | 37 |
| QA3 | 0 | 6 | 31 |
| QA4 | 0 | 0 | 37 |
| QA5 | 0 | 37 | 0 |
| QA6 | 0 | 26 | 11 |
| QA7 | 35 | 0 | 2 |
| QA8 | 0 | 5 | 32 |

QA7 \(=2\) is KT035 (HHSKT) and KT044 (SINKT). Tiers stay 11 HIGH, 26 MODERATE, 0 LIMITED, mean \(0.76\). No threshold was lowered.

`tables/sparse_coldstart_audit.csv` records `generic_data_sparsity=YES` on all 37 rows. The main text states that this field does not separate papers and is not a synthesis variable. The v1.9 sparse file already omits that column. The representative sparse table notes that previously said “Generic sparsity only” now say “Interaction sparsity only.” The YES/NO columns were not edited.
