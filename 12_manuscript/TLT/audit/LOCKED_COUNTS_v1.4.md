# Locked manuscript counts (v1.4)

**Superseded:** 2026-09-13 by `LOCKED_COUNTS_v1.5.md` (PDF-strict recode of five cells). Keep this file as the pre-recode snapshot.

**Date:** 2026-09-13  
**Rule:** Every count in `manuscript_TLT_FORMATTED_v1.3.tex` and figure assets must come from the four CSVs below. Unique paper = `paper_id` prefix before `_Dense`/`_Trans`. KT004 is one paper.

## Sources

- `tables/graph_taxonomy.csv`
- `tables/ssl_taxonomy.csv`
- `tables/sparse_coldstart_audit.csv`
- `tables/corpus_counts.csv`

QA tier split uses `supplementary/supplementary_quality_scores.csv` only after: drop KT078 and KT080–KT083; cap QA6 at 2; recompute `normalized = raw/16`.

## Corpus

| Quantity | Value | Source |
|---|---:|---|
| Identified records | 2017 | `corpus_counts.csv` `N_IDENTIFIED` |
| Duplicates removed | 1267 | `N_DUPLICATES_REMOVED` |
| Screened | 750 | `N_SCREENED` |
| Title/abstract excluded | 610 | `N_TA_EXCLUDED` |
| Full-text assessed | 140 | `N_FULLTEXT_ASSESSED` |
| Full-text excluded | 103 | `N_FULLTEXT_EXCLUDED` |
| Primary core | 37 | `N_PRIMARY_CORE` and unique `graph_taxonomy` papers |

Database split in `N_IDENTIFIED` description: Scopus 531, WoS 344, ScienceDirect 257, SpringerLink 255, IEEE Xplore 232, ACM DL 200, arXiv 198. Protocol: six core DBs; arXiv is preprint monitoring only.

## Graph / SSL

| Quantity | Value | Rule |
|---|---:|---|
| \(N_G\) | 36 | `graph_source != NONE` |
| Sequence-only SSL | 1 | KT039 CL4KT (`graph_source=NONE`) |
| \(N_S\) | 9 | rows in `ssl_taxonomy.csv` after H1 S-criterion audit |
| \(N_{G \cap S}\) | 8 | SSL IDs except KT039 |

### Provenance (\(N_G=36\))

| `graph_provenance` | n | % of 36 |
|---|---:|---:|
| MODEL_DEFINED_FIXED | 19 | 52.8 |
| EXTERNAL_FIXED | 9 | 25.0 |
| DYNAMIC_LEARNED | 8 | 22.2 |

Do not use Expert 9 / Log 15 / Dynamic 5 / LLM 2.

### Encoder (\(N_G=36\))

| `gnn_encoder` | n |
|---|---:|
| GCN | 12 |
| GNN_GENERIC | 1 |
| GCN / generic (display group) | 13 |
| HETEROGENEOUS_GNN | 8 |
| GAT | 3 |
| HYPERGRAPH_GNN | 2 |
| DYNAMIC_GNN | 2 |
| NONE (PDKT-C KT014, CMKT KT037, PEBG KT026) | 3 |
| Other (GGNN, GRAPH_MEMORY, CAPSULE_GNN, GRAPH_OPTIMAL_TRANS, SPATIOTEMPORAL_GNN) | 5 |

### SSL families (\(N_S=9\); exclusive locked §14 tokens)

| `ssl_family` | n | papers |
|---|---:|---|
| MULTIVIEW_CONTRASTIVE | 4 | KT011, KT042, KT043, KT066 |
| GRAPH_CONTRASTIVE | 3 | KT047, KT050, KT068 |
| GRAPH_RECONSTRUCTION | 1 | KT026 |
| SEQUENCE_CONTRASTIVE | 1 | KT039 |

Do not count `GRAPH_EMBEDDING_PRETRAINING`, `HYPERGRAPH_CONTRASTIVE`, `CROSS_VIEW_CONTRASTIVE`, or `HIERARCHICAL_CONTRAST` as family codes. See `audit/SSL_FAMILY_LOCKED_ALIGNMENT.md`.

Removed from \(N_S\) (G-criterion only): KT044, KT070, KT076, KT077, KT079. See `audit/H1_SSL_CRITERION_DECISION.md`.

Do not use the old 4-family percentages (42.9 / 28.6 / 14.3 / 14.3).

## Sparse

| Quantity | Value | Papers |
|---|---:|---|
| Generic data sparsity YES | 37/37 | all rows |
| Strict KC cold-start YES | 1/37 | KT044 only |
| Item cold-start YES | 3/37 | KT026, KT044, KT076 |
| Learner cold-start YES | 0/37 | none |

## QA (capped)

| Quantity | Value |
|---|---:|
| HIGH (\(\ge 0.80\)) | 11 |
| MODERATE (0.55–0.79) | 26 |
| LIMITED | 0 |
| Mean normalized | 0.76 |

HIGH after QA6 cap: KT029, KT033, KT035, KT038, KT044, KT050, KT060, KT064, KT066, KT070, KT077.

Codebook QA names: QA1 task; QA2 data; QA3 split/provenance/leakage; QA4 baseline/ablation; QA5 statistical uncertainty; QA6 author artifacts; QA7 sparse/cold-start; QA8 compute.
