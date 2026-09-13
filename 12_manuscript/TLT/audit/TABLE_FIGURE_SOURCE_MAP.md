# Table, Figure, and Supplementary Source Mapping Audit
**Survey Protocol Version:** v1.0 LOCKED  
**Audit Target:** `12_manuscript/TLT/`  
**Date:** 2026-09-12  

---

## 1. Executive Summary

This document provides complete traceability mapping for all figures, tables, and supplementary materials in the manuscript for **IEEE Transactions on Learning Technologies (IEEE TLT)**. Per Task A14 rules:
- Main manuscript length is strictly maintained at **11 double-column pages** ($\le 18$ page limit).
- All quantitative figure percentages and table counts are derived strictly from underlying audited CSV files.
- All figure and table captions state explicit denominators and category overlap constraints.

---

## 2. Main Paper Table Source Map

| Table # | Table Title | LaTeX Label | Primary Source File / Script | Key Denominator | Overlap Rule |
| :---: | :--- | :--- | :--- | :---: | :--- |
| **Table 1** | Summary of Key Mathematical Notations | `tab:notation_summary` | `manuscript_TLT_STRUCTURE_v0.1.tex` | N/A | Definitions |
| **Table 2** | Comparison with Prior Knowledge Tracing Reviews | `tab:survey_comparison` | `12_manuscript/TLT/audit/TLT_POSITIONING_AUDIT.md` | $N_{\text{surveys}} = 4$ | Mutually Exclusive Columns |
| **Table 3** | Taxonomy Table 1: Graph-Based KT Models | `tab:graph_taxonomy` | `12_manuscript/TLT/tables/graph_taxonomy.csv` | $N_G = 31$ | Mutually Exclusive Primary Focus |
| **Table 4** | Taxonomy Table 2: Self-Supervised KT Models | `tab:ssl_taxonomy` | `12_manuscript/TLT/tables/ssl_taxonomy.csv` | $N_S = 14$ | Mutually Exclusive SSL Family |
| **Table 5** | Taxonomy Table 3: Sparse & Cold-Start Protocols | `tab:sparse_taxonomy` | `12_manuscript/TLT/tables/sparse_coldstart_audit.csv` | $N = 37$ | Representative Subset ($N_{\text{sub}}=13$) |

---

## 3. Main Paper Figure Source Map

| Figure # | Figure Title | Asset File Path | Underlying Data Source | Denominator & Distribution | Overlap Rule |
| :---: | :--- | :--- | :--- | :---: | :--- |
| **Figure 1** | PRISMA 2020 Flow Diagram | `figures/fig_prisma_flow.pdf` | `00_protocol/PRISMA_2020_FLOW.md` | $N_{\text{raw}} = 2,017 \rightarrow N = 37$ | Sequential Stages |
| **Figure 2** | Two-Dimensional Taxonomy Framework | `figures/fig_taxonomy_2d.pdf` | `12_manuscript/TLT/audit/TAXONOMY_GRAPH_AUDIT.md` | $N = 37$ ($N_G=31, N_S=14, N_{G\cap S}=8$) | Overlapping Paradigms |
| **Figure 3** | Four-Channel Graph Construction Pipeline | `figures/fig_graph_construction_pipeline.pdf` | `12_manuscript/TLT/tables/graph_taxonomy.csv` | $N_G = 31$ (Expert 29.0%, Log 48.4%, etc.) | Primary Channel |
| **Figure 4** | Meta-Analysis Distribution of GNN Encoders | `figures/fig_meta_analysis_charts.pdf` | `12_manuscript/TLT/tables/graph_taxonomy.csv` | $N_G = 31$ (GCN 35.5%, GAT 22.6%, etc.) | Mutually Exclusive Primary GNN |
| **Figure 5** | Taxonomy Framework of SSL Pretext Objectives | `figures/fig_ssl_framework.pdf` | `12_manuscript/TLT/tables/ssl_taxonomy.csv` | $N_S = 14$ (Multi-View 42.9%, Struct 28.6%, etc.)| Mutually Exclusive Primary SSL |

---

## 4. Supplementary Materials Inventory Map

All supplementary CSV artifacts are located in [`12_manuscript/TLT/supplementary/`](file:///g:/Other%20computers/My%20Computer/LT/Ebooks/TIEN%20SI/LUAN%20AN/GraphSSL_KT_Survey_2026/12_manuscript/TLT/supplementary/):

| Supplementary Filename | Description | Row Count | Primary Source File |
| :--- | :--- | :---: | :--- |
| **`supplementary_corpus_inventory.csv`** | Full per-paper metadata & gateway verification | $N = 37$ | `tables/graph_taxonomy.csv` |
| **`supplementary_coding_matrix.csv`** | Complete taxonomy coding matrix across dimensions | $N = 37$ | `tables/ssl_taxonomy.csv` |
| **`supplementary_quality_scores.csv`** | Itemized QA1--QA8 quality scores & total tiers | $N = 37$ | `08_quality_reliability/QUALITY_ASSESSMENT_AUDIT_v1.0.csv` |
| **`supplementary_prisma_exclusions.csv`** | Stage 2 screening full-text exclusion details | $N = 98$ | `06_fulltext/fulltext_screening_v1.0.csv` |
| **`supplementary_doi_audit.csv`** | Complete reference DOI & physical PDF deposit audit | $N = 43$ | `audit/REFERENCE_METADATA_AUDIT.csv` |

---

## 5. Caption Traceability Verification

All figure and table captions in `manuscript_TLT_STRUCTURE_v0.1.tex` have been verified to state:
1. **Explicit Denominator**: Stated as $N = 37$ (full corpus), $N_G = 31$ (Graph-KT subset), or $N_S = 14$ (SSL-KT subset).
2. **Overlap Constraint**: Stated explicitly as "categories are mutually exclusive" or "multi-label overlap allowed".

---
*End of Table, Figure, and Supplementary Source Mapping Report.*
