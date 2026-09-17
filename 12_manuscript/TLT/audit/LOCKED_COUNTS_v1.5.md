# Locked manuscript counts (v1.5)

**Date:** 2026-09-13  
**Supersedes:** `LOCKED_COUNTS_v1.4.md` after PDF-strict recode of five cells.  
**Evidence:** `08_quality_reliability/ADJUDICATION_FIVE_DIFFS_PDF_2026-09-13.md`  
**Rule:** Every count in `manuscript_TLT_FORMATTED_v1.3.tex` and figure assets must come from the four CSVs below. Unique paper = `paper_id` prefix before `_Dense`/`_Trans`. KT004 is one paper.

## Sources

- `tables/graph_taxonomy.csv`
- `tables/ssl_taxonomy.csv`
- `tables/sparse_coldstart_audit.csv`
- `tables/corpus_counts.csv`

QA tier split uses `supplementary/supplementary_quality_scores.csv` only after: drop KT078 and KT080–KT083; cap QA6 at 2; recompute `normalized = raw/16`.

## Recode (v1.4 → v1.5)

| Paper | Field | v1.4 | v1.5 |
|---|---|---|---|
| KT026 | item_cold_start / category | YES / ITEM_COLD_START | NO / SPARSE_INTERACTION_ONLY |
| KT031 | gnn_encoder | GCN | OTHER |
| KT044 | gnn_encoder | GCN | GAT |
| KT044 | strict_kc_cold_start / category | YES / STRICT_KC_COLD_START | NO / ITEM_COLD_START |
| KT076 | item_cold_start / category | YES / ITEM_COLD_START | NO / SPARSE_INTERACTION_ONLY |

This is not human–human \(\kappa\).

## Corpus

Unchanged from v1.4: identified 2017; screened 750; full-text 140; primary core 37.

## Graph / SSL

Unchanged: \(N_G=36\), \(N_S=9\), \(N_{G\cap S}=8\); provenance 19 / 9 / 8.

### Encoder (\(N_G=36\))

| `gnn_encoder` | n |
|---|---:|
| GCN | 10 |
| GNN_GENERIC | 1 |
| GCN / generic (display group) | 11 |
| HETEROGENEOUS_GNN | 8 |
| GAT | 4 |
| HYPERGRAPH_GNN | 2 |
| DYNAMIC_GNN | 2 |
| NONE (PDKT-C KT014, CMKT KT037, PEBG KT026) | 3 |
| Other (GGNN, GRAPH_MEMORY, CAPSULE_GNN, GRAPH_OPTIMAL_TRANS, SPATIOTEMPORAL_GNN, OTHER/KSG-AKT) | 6 |

## Sparse

| Quantity | Value | Papers |
|---|---:|---|
| Generic data sparsity YES | 37/37 | all rows |
| Strict KC cold-start YES | 0/37 | none |
| Item cold-start YES | 1/37 | KT044 only (question hold-out) |
| Learner cold-start YES | 0/37 | none |

## QA (capped)

Unchanged from v1.4: HIGH 11; MODERATE 26; mean 0.76.
