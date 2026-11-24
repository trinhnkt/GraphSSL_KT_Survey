# Adjudication — A vs DaoMT subset (3 diffs)

**Date:** 2026-09-14  
**A:** `inter_rater_coderA_locked_v1.0.csv` (locked gold)  
**B:** `inter_rater_coding_sample_BLIND_EMPTY_v1.4_DaoMT_AS_SUBMITTED.csv`  
**Pre-adjudication:** 77/80; mean κ 0.95 (`KAPPA_A_vs_DaoMT_SUBSET_2026-09-14.md`)

| # | Paper | Field | A (gold) | DaoMT | Verdict | Why |
|---|---|---|---|---|---|---|
| 1 | KT047 DC-SSL | ssl_family | MULTIVIEW_CONTRASTIVE | GRAPH_CONTRASTIVE | **Keep A** | PDF: contrast via **two channels** of DHGN (= two views). Both tokens fit; exclusive rule aligned with KT011 → MULTIVIEW. GRAPH is secondary. |
| 2 | KT070 Coda | graph_provenance | DYNAMIC_LEARNED | MODEL_DEFINED_FIXED | **Keep A** | PDF §3.1.1: learnable \(A_u\) that **changes with \(W\)**. `MODEL_DEFINED_FIXED` forbids jointly learned topology. |
| 3 | KT068 HKT | gnn_encoder | GNN_GENERIC | HETEROGENEOUS_GNN | **Keep A** | PDF §4.2–4.3: attention on KHT/KAG; no hetero GNN / RGCN / HGT named. Heterogeneous *graphs* ≠ `HETEROGENEOUS_GNN` encoder. |

**Gold after adjudication:** A on all three cells. No live CSV / manuscript count change.

**Reporting:** Independent subset κ remains **as-submitted** 77/80 (mean 0.95). Do not recompute κ after forcing B to gold. Do not pool with NguyenKT locator κ.

Sources: `_adj_extract/KT047.txt`, `KT070.txt`, `KT068.txt`; `ADJUDICATION_FIVE_CELLS_PDF_2026-09-13.md`; `LOCKED_COUNTS_v1.7.md`.
