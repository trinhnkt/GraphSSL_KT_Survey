# PROJECT TREE & WORKSPACE DIRECTORY MAP (v1.0 LOCKED)

```text
GraphSSL_KT_Survey_2026/
├── 00_protocol/                          # Frozen protocol documents & locked schemas
│   ├── SCOPE_v1.0_LOCKED.md              # Scope definition & primary-corpus gateway rule
│   ├── RQs_v1.0_LOCKED.md                # Research Questions RQ1–RQ6 definitions
│   ├── SLR_PROTOCOL_v1.0_LOCKED.md       # Systematic review protocol & PRISMA search rules
│   ├── coding_codebook_v1.0_LOCKED.md    # 3-level coding schema (PAPER, MODEL, EXPERIMENT)
│   └── protocol_deviations.md            # Traceability log for protocol deviations
├── 01_seed_corpus/                       # Audited seed corpus records & candidate CSVs
│   └── included_papers_seed_audited_v1.0.csv
├── 02_pilot_coding/                      # Pilot Wave A, Wave B, Wave C coding records & evidence tables
├── 03_search/                            # Verbatim database search logs & PRISMA expansion report
│   ├── search_log.csv                    # 16 database query execution log across 7 databases
│   └── PRISMA_SEARCH_EXPANSION_REPORT_v1.0.md
├── 04_deduplication/                     # Automated & manual deduplication audit logs
│   └── deduplication_audit_v1.0.csv      # 4-tier match resolution log (1,185 duplicates removed)
├── 05_screening/                         # Stage 1 Title/Abstract screening decisions
│   └── title_abstract_screening_v1.0.csv # 750 deduplicated records screened
├── 06_fulltext/                          # Stage 2 Full-Text eligibility decisions
│   └── fulltext_screening_v1.0.csv       # 140 full-text articles assessed (98 excluded with EC1-EC7)
├── 07_coding/                            # Full-corpus 3-level coding records & evidence tables
│   ├── batch_1/                          # Full-corpus Batch 1 (Classic Graph-KT: KT012, KT016, KT023, KT031, KT033, KT052)
│   ├── batch_2/                          # Full-corpus Batch 2 (Advanced Graph GNN: KT036, KT043, KT047, KT050, KT053)
│   ├── batch_3/                          # Full-corpus Batch 3 (Multi-View & Dual-Graph: KT029, KT056, KT060, KT063, KT064)
│   ├── batch_4/                          # Full-corpus Batch 4 (Frontier Graph-KT: KT062, KT065, KT067, KT068, KT069, KT070)
│   ├── expansion/                        # PRISMA Expansion Coding Records (KT076, KT077, KT078, KT079, KT080, KT081, KT082, KT083)
│   └── FULL_SEED_CORPUS_CODING_SYNTHESIS_v1.0.md # Master integrated primary core synthesis (42 papers)
├── 08_quality_reliability/              # Quality assessment & inter-rater agreement audit
│   ├── QUALITY_ASSESSMENT_AUDIT_v1.0.csv # QA1–QA8 breakdown across all 42 core papers (Mean: 0.7768)
│   └── INTER_RATER_RELIABILITY_REPORT_v1.0.md # Cohen's Kappa agreement report (kappa > 0.85)
├── 09_benchmark/                         # Benchmark specifications
│   └── SPARSE_KT_BENCHMARK_SPECIFICATION_v1.0.md # pyKT-ColdStart benchmark suite specification
├── 10_analysis/                          # Meta-analysis quantitative statistics
│   └── META_ANALYSIS_STATISTICS_v1.0.md # Quantitative distributions across GNNs, Backbones, SSL & QA
├── 11_figures_tables/                    # Systematic taxonomy tables & PRISMA flowcharts
│   ├── RQ1_RQ2_GRAPH_TAXONOMY_TABLE.md   # Taxonomy Table 1: Graph Construction & GNN Architectures
│   ├── RQ3_SSL_TAXONOMY_TABLE.md         # Taxonomy Table 2: Self-Supervised Learning Objectives
│   ├── RQ4_SPARSE_CONCEPT_TABLE.md       # Taxonomy Table 3: Sparse-Concept & Cold-Start Protocols
│   └── PRISMA_2020_FLOW_DIAGRAM.md       # PRISMA 2020 Flow Diagram in Mermaid format
├── 12_manuscript/                        # Submission-ready survey manuscript package
│   ├── 00_MANUSCRIPT_OUTLINE_v1.0.md     # Master survey manuscript outline for IEEE TKDE / ACM CSUR
│   ├── SECTION_1_INTRODUCTION.md         # Section 1: Introduction & Motivation
│   ├── SECTION_2_METHODOLOGY_PRISMA.md   # Section 2: Systematic Review Methodology & PRISMA Protocol
│   ├── SECTION_3_TAXONOMY_GRAPH_KT.md    # Section 3: Graph-Based Knowledge Tracing Taxonomy
│   ├── SECTION_4_TAXONOMY_SSL_KT.md      # Section 4: Self-Supervised Knowledge Tracing Taxonomy
│   ├── SECTION_5_SPARSE_CONCEPT_EVALUATION.md # Section 5: Sparse-Concept & Cold-Start Protocols
│   ├── SECTION_6_RELIABILITY_REPRODUCIBILITY.md # Section 6: Reliability, Reproducibility & Calibration Audit
│   ├── SECTION_7_RESEARCH_AGENDA.md      # Section 7: Evidence-Derived Research Agenda (6 Pillars)
│   ├── SECTION_8_CONCLUSION.md           # Section 8: Conclusion
│   ├── FULL_SURVEY_MANUSCRIPT_v1.0.md    # Complete Monolith Survey Manuscript (Sections 1–8 Integrated)
│   ├── main_tkde.tex                     # IEEE TKDE LaTeX source code file
│   ├── references.bib                    # BibTeX bibliography database
│   └── MANUSCRIPT_VERIFICATION_REPORT_v1.0.md # Final Quality Audit & Verification Report
└── 13_supplementary/                    # Open science supplementary materials index
    └── SUPPLEMENTARY_MATERIALS_INDEX_v1.0.md # Index of all supplementary datasets & logs
```
