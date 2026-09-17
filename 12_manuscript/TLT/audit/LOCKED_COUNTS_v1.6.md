# Locked manuscript counts (v1.6)

**Date:** 2026-09-13  
**Supersedes:** `LOCKED_COUNTS_v1.5.md` after PDF-strict recode of two A-vs-B cells.  
**Evidence:** `08_quality_reliability/ADJUDICATION_FIVE_CELLS_PDF_2026-09-13.md`  
**Rule:** Every count in `manuscript_TLT_FORMATTED_v1.3.tex` and figure assets must come from the four CSVs below. Unique paper = `paper_id` prefix before `_Dense`/`_Trans`. KT004 is one paper.

## Sources

- `tables/graph_taxonomy.csv`
- `tables/ssl_taxonomy.csv`
- `tables/sparse_coldstart_audit.csv`
- `tables/corpus_counts.csv`

QA tier split uses `supplementary/supplementary_quality_scores.csv` only after: drop KT078 and KT080–KT083; cap QA6 at 2; recompute `normalized = raw/16`.

## Recode (v1.5 → v1.6)

| Paper | Field | v1.5 | v1.6 |
|---|---|---|---|
| KT070 Coda | graph_provenance | MODEL_DEFINED_FIXED | DYNAMIC_LEARNED |
| KT068 HKT | gnn_encoder | HETEROGENEOUS_GNN | GNN_GENERIC |

PDF: Coda §3.1.1 learnable \(A_u\) that changes with \(W\); HKT §4.2–4.3 attention on KHT/KAG (no heterogeneous GNN). This is not human–human \(\kappa\).

Family cells KT011/KT047 and PEBG provenance were **not** changed (exclusive-family rule / Q-matrix collapse).

## Corpus

Unchanged: identified 2017; screened 750; full-text 140; primary core 37.

## Graph / SSL

Unchanged: \(N_G=36\), \(N_S=9\), \(N_{G\cap S}=8\).  
Provenance: **18 / 9 / 9** (model-defined / external / dynamic).

### Encoder (\(N_G=36\))

| `gnn_encoder` | n |
|---|---:|
| GCN | 10 |
| GNN_GENERIC | 2 (GKT, HKT) |
| GCN / generic (display group) | 12 |
| HETEROGENEOUS_GNN | 7 |
| GAT | 4 |
| HYPERGRAPH_GNN | 2 |
| DYNAMIC_GNN | 2 |
| NONE (PDKT-C KT014, CMKT KT037, PEBG KT026) | 3 |
| Other (GGNN, GRAPH_MEMORY, CAPSULE_GNN, GRAPH_OPTIMAL_TRANS, SPATIOTEMPORAL_GNN, OTHER/KSG-AKT) | 6 |

## Sparse

Unchanged from v1.5: generic sparsity 37/37; strict KC YES 0/37; item CS YES 1/37 (SINKT); learner CS YES 0/37.

## QA (capped)

Unchanged: HIGH 11; MODERATE 26; mean 0.76.
