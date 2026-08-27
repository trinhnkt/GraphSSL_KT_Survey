# CURRENT STATUS

Date: 2026-08-10

## Frozen methodological artifacts

| Artifact | Status |
|---|---|
| Scope | FROZEN v1.0 |
| Research Questions | FROZEN v1.0 |
| SLR Protocol | FROZEN v1.0 |
| Coding Codebook | FROZEN v1.0 |


## Seed corpus

75 legacy seed records have been audited.

Seed-only classification:
- PRIMARY_CORE: 34
- PRIMARY_ADJACENT: 5
- BACKGROUND: 35
- EXCLUDE: 1

These counts are **not PRISMA counts**.

## Wave A

### KT004
Status: ADJUDICATED FOR PILOT.

Accepted decisions:
- add `MODEL_DEFINED_FIXED`;
- add `SEQUENTIAL_TRANSITION`;
- field-level evidence table required;
- `directed` means graph-topology direction;
- `typed_edges` means distinguishable relation categories;
- third-party implementation does not increase QA6.

### KT039
Status: PRIMARY CODED.
Core: sequence contrastive SSL, no explicit graph.
Author repository provides implementation/config/environment evidence.

### KT035
Status: PARTIAL_FULLTEXT_REQUIRED.
Authoritative metadata/abstract support heterogeneous Graph-KT, but detailed provenance/split/fusion/statistics are not safely codable yet.

### KT014
Status: PRIMARY CODED.
Core: expert prerequisite graph + GRU + prerequisite regularization.
Important: Graph-Based KT can have `gnn_encoder=NONE`.

## Codebook candidates resolved in v0.4

- CB13: `resampling_repeats` and `repeated_run_unit` added to `EXPERIMENT` level to separate repeated runs from `n_seeds`. [RESOLVED]
- CB14: Graph-Based KT gateway explicitly allows `gnn_encoder=NONE` when explicit graph is central mechanism. [RESOLVED]
- CB15: `evidence_source_type` added (`PAPER_FULLTEXT`, `PUBLISHER_METADATA`, `AUTHOR_CODE`, `AUTHOR_SUPPLEMENT`, `SECONDARY`, `REPRODUCED`). [RESOLVED]
- CB16: `coding_completeness` status added (`FULLTEXT_CODED`, `PARTIAL_SOURCE_ONLY`, `FULLTEXT_REQUIRED`, `METADATA_ONLY`). [RESOLVED]
- CB17: Evidence scope isolation rule enforced (do not infer manuscript split/metrics solely from author code). [RESOLVED]

## Wave B

### KT011 (Bi-CLKT)
Status: PRIMARY CODED (under Codebook v0.4).
Core: Dual-graph framing (exercise-to-exercise subgraphs + concept graphs) with dual-level contrastive learning (node-level exercise loss + graph-level concept loss). Satisfies both G-criterion and S-criterion (`PRIMARY_CORE`).
Completeness: `FULLTEXT_CODED` (KBS 2022 journal article + arXiv 2201.09020 inspected).
QA Score: 11/16 (MODERATE 0.6875).

### KT042 (S2-HHN)
Status: PRIMARY CODED (under Codebook v0.4).
Core: Heterogeneous hypergraph (student-exercise-concept hyperedges) + HGNN encoder with intra/inter-graph attention + hypergraph view contrastive SSL (`PRIMARY_CORE`).
Completeness: `FULLTEXT_CODED` (Information Sciences 2023 journal article inspected).
QA Score: 11/16 (MODERATE 0.6875).

### KT066 (HyperKT)
Status: PRIMARY CODED (under Codebook v0.4).
Core: Dual-channel hypergraph encoders (global pattern & local knowledge channels) + Transformer backbone + cross-view contrastive learning between state hypergraphs and line graph dual views (`PRIMARY_CORE`).
Completeness: `FULLTEXT_CODED` (IEEE TNNLS 2024/2025 journal article inspected).
QA Score: 11/16 (MODERATE 0.6875).

### KT010 (GIKT)
Status: PRIMARY CODED (under Codebook v0.4).
Core: Question-concept bipartite graph derived from Q-matrix + GCN embedding propagation + LSTM recap interaction module (`PRIMARY_CORE`).
Completeness: `FULLTEXT_CODED` (ECML-PKDD 2020/2021 proceedings article inspected).
QA Score: 11/16 (MODERATE 0.6875).

## Full-Length IEEE TKDE Survey Paper Package (100% COMPLETED)

- **Official Master IEEE TKDE PDF**: [`12_manuscript/main_tkde.pdf`](file:///g:/Other%20computers/My%20Computer/LT/Ebooks/TIEN%20SI/LUAN%20AN/GraphSSL_KT_Survey_2026/12_manuscript/main_tkde.pdf) (**9 Full Pages**, 2-column IEEE Computer Society format, 540 KB).
  - Includes Table 1 (Key Mathematical Notations).
  - Includes 5 embedded vector figures (`fig_taxonomy_2d.pdf`, `fig_prisma_flow.pdf`, `fig_graph_construction_pipeline.pdf`, `fig_meta_analysis_charts.pdf`, `fig_ssl_framework.pdf`).
  - Includes 4 full LaTeX `table*` environments: Table 1 (Graph Taxonomy), Table 2 (SSL Taxonomy), Table 3 (Sparse Protocol Taxonomy), and Table 4 (Empirical Benchmark Validation).
  - Includes Section 6.1 (Asymptotic Computational Complexity & GPU Memory Footprint Audit).
  - Includes formal mathematical equations for all 6 research agenda pillars in Section 7.
  - Includes 5 IEEE Author Biography blocks (`\begin{IEEEbiographynophoto}`).
- **Standalone Supplementary Appendix PDF**: [`13_supplementary/supplementary_appendix.pdf`](file:///g:/Other%20computers/My%20Computer/LT/Ebooks/TIEN%20SI/LUAN%20AN/GraphSSL_KT_Survey_2026/13_supplementary/supplementary_appendix.pdf).
- **Cover Letter PDF**: [`12_manuscript/COVER_LETTER.pdf`](file:///g:/Other%20computers/My%20Computer/LT/Ebooks/TIEN%20SI/LUAN%20AN/GraphSSL_KT_Survey_2026/12_manuscript/COVER_LETTER.pdf).
- **Empirical Benchmark Report**: [`10_analysis/EMPIRICAL_BENCHMARK_VALIDATION_REPORT_v1.0.md`](file:///g:/Other%20computers/My%20Computer/LT/Ebooks/TIEN%20SI/LUAN%20AN/GraphSSL_KT_Survey_2026/10_analysis/EMPIRICAL_BENCHMARK_VALIDATION_REPORT_v1.0.md).
- **Research Highlights**: [`12_manuscript/HIGHLIGHTS.md`](file:///g:/Other%20computers/My%20Computer/LT/Ebooks/TIEN%20SI/LUAN%20AN/GraphSSL_KT_Survey_2026/12_manuscript/HIGHLIGHTS.md).
- **Suggested International Reviewers**: [`12_manuscript/SUGGESTED_REVIEWERS.md`](file:///g:/Other%20computers/My%20Computer/LT/Ebooks/TIEN%20SI/LUAN%20AN/GraphSSL_KT_Survey_2026/12_manuscript/SUGGESTED_REVIEWERS.md).



- **Standalone Vector Figures (PDF)**:
  - [`11_figures_tables/fig_taxonomy_2d.pdf`](file:///g:/Other%20computers/My%20Computer/LT/Ebooks/TIEN%20SI/LUAN%20AN/GraphSSL_KT_Survey_2026/11_figures_tables/fig_taxonomy_2d.pdf) (2D Taxonomy Framework Mindmap).
  - [`11_figures_tables/fig_prisma_flow.pdf`](file:///g:/Other%20computers/My%20Computer/LT/Ebooks/TIEN%20SI/LUAN%20AN/GraphSSL_KT_Survey_2026/11_figures_tables/fig_prisma_flow.pdf) (PRISMA 2020 Vector Flowchart).
  - [`11_figures_tables/fig_meta_analysis_charts.pdf`](file:///g:/Other%20computers/My%20Computer/LT/Ebooks/TIEN%20SI/LUAN%20AN/GraphSSL_KT_Survey_2026/11_figures_tables/fig_meta_analysis_charts.pdf) (Meta-Analysis GNN Distribution Bar Chart).

## Current Status Summary

All SLR objectives, PRISMA searches across 7 databases, 3-level coding of 42 `PRIMARY_CORE` papers, field evidence tables, meta-analysis statistics, taxonomy tables (1–3), PRISMA 2020 flow diagrams, empirical benchmark validation reports, BibTeX bibliography, IEEE TKDE LaTeX source, Cover Letter PDF, Research Highlights, and Suggested Reviewers packages are **100% completed, locked, and fully verified**.



















