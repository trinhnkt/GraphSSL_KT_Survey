# KT066 Field-Level Evidence Table (v0.4 PILOT)

This document contains the long-form field-level evidence records for paper **KT066 (HyperKT)**, satisfying the schema required in Section 2 of `coding_codebook_v0.4_PILOT.md`.

## Schema
`evidence_id` | `entity_level` | `entity_id` | `field_name` | `coded_value` | `coding_basis` | `evidence_source_type` | `evidence_locator` | `evidence_note` | `source_url` | `coder_id` | `coder_type` | `coder_confidence` | `adjudication_status`

---

## Evidence Records

| evidence_id | entity_level | entity_id | field_name | coded_value | coding_basis | evidence_source_type | evidence_locator | evidence_note | source_url | coder_id | coder_type | coder_confidence | adjudication_status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| E066_001 | PAPER | PAPER_KT066 | title | Dual-Channel Adaptive Scale Hypergraph Encoders With Cross-View Contrastive Learning for Knowledge Tracing | AUTHOR_STATED | PUBLISHER_METADATA | Title | Official published article title | 10.1109/TNNLS.2024.3386810 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E066_002 | PAPER | PAPER_KT066 | venue | IEEE Transactions on Neural Networks and Learning Systems | AUTHOR_STATED | PUBLISHER_METADATA | Journal Header | Vol. 36, Issue 4, pp. 6752–6766, April 2024 / 2025 | 10.1109/TNNLS.2024.3386810 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E066_003 | PAPER | PAPER_KT066 | kt_central_task | YES | AUTHOR_STATED | PAPER_FULLTEXT | Abstract & Sec. I | Sequential learner-state estimation & performance prediction | 10.1109/TNNLS.2024.3386810 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E066_004 | PAPER | PAPER_KT066 | G_criterion | YES | AUTHOR_STATED | PAPER_FULLTEXT | Sec. III-A & III-B | Dual-channel hypergraph encoders (global pattern & local knowledge channels) | 10.1109/TNNLS.2024.3386810 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E066_005 | PAPER | PAPER_KT066 | S_criterion | YES | AUTHOR_STATED | PAPER_FULLTEXT | Sec. III-C | Cross-view contrastive learning between state hypergraph views & transformed line graph views | 10.1109/TNNLS.2024.3386810 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E066_006 | PAPER | PAPER_KT066 | corpus_tier | PRIMARY_CORE | REVIEWER_INFERRED | PAPER_FULLTEXT | Protocol Section 4 | Primary core: satisfies both G-criterion and S-criterion | Scope v1.0 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E066_007 | PAPER | PAPER_KT066 | coding_completeness | FULLTEXT_CODED | REVIEWER_INFERRED | PAPER_FULLTEXT | Full Text | Peer-reviewed IEEE TNNLS journal full text thoroughly inspected | 10.1109/TNNLS.2024.3386810 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E066_008 | MODEL | MODEL_KT066_HyperKT | graph_source | HYBRID_MULTI_SOURCE | AUTHOR_STATED | PAPER_FULLTEXT | Sec. III-A | Interaction logs + adaptive-scale hyperedge distillation | 10.1109/TNNLS.2024.3386810 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E066_009 | MODEL | MODEL_KT066_HyperKT | graph_provenance | PRECOMPUTED_UNCLEAR_SPLIT | REVIEWER_INFERRED | PAPER_FULLTEXT | Sec. III-A | Hypergraph matrices precomputed from interaction logs | 10.1109/TNNLS.2024.3386810 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E066_010 | MODEL | MODEL_KT066_HyperKT | graph_leakage_risk | POTENTIAL | REVIEWER_INFERRED | PAPER_FULLTEXT | Sec. III-A & Protocol Sec 7 | Precomputed hyperedge matrix without explicit temporal train-only isolation | Codebook v0.4 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E066_011 | MODEL | MODEL_KT066_HyperKT | graph_representation | HYPERGRAPH, MULTI_RELATIONAL | AUTHOR_STATED | PAPER_FULLTEXT | Sec. III-B | Dual-channel hypergraphs + transformed line graph dual views | 10.1109/TNNLS.2024.3386810 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E066_012 | MODEL | MODEL_KT066_HyperKT | directed | N | AUTHOR_STATED | PAPER_FULLTEXT | Sec. III-B | Hypergraph projections and line graph dual transformations operate symmetrically | 10.1109/TNNLS.2024.3386810 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E066_013 | MODEL | MODEL_KT066_HyperKT | typed_edges | Y | AUTHOR_STATED | PAPER_FULLTEXT | Sec. III-B | Distinguishes global pattern-aware hyperedges and local knowledge-aware hyperedges | 10.1109/TNNLS.2024.3386810 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E066_014 | MODEL | MODEL_KT066_HyperKT | gnn_encoder | HGNN_HYPERGRAPH | AUTHOR_STATED | PAPER_FULLTEXT | Sec. III-B | Simplified hypergraph convolution + collaborative hypergraph convolution networks | 10.1109/TNNLS.2024.3386810 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E066_015 | MODEL | MODEL_KT066_HyperKT | temporal_backbone | SELF_ATTENTION_TRANSFORMER | AUTHOR_STATED | PAPER_FULLTEXT | Sec. III-D | Transformer / attentive sequence layer for temporal state updates | 10.1109/TNNLS.2024.3386810 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E066_016 | MODEL | MODEL_KT066_HyperKT | ssl_family | MULTIVIEW_CONTRASTIVE, GRAPH_CONTRASTIVE | AUTHOR_STATED | PAPER_FULLTEXT | Sec. III-C | Cross-view contrastive learning between hypergraph views and transformed line graph views | 10.1109/TNNLS.2024.3386810 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E066_017 | EXPERIMENT | EXP_KT066_MAIN | datasets | ASSISTments2009, ASSISTments2017, Statics2011, Junyi | AUTHOR_STATED | PAPER_FULLTEXT | Sec. IV-A | Evaluated on 4 public benchmark educational datasets | 10.1109/TNNLS.2024.3386810 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E066_018 | EXPERIMENT | EXP_KT066_MAIN | n_seeds | 5 | AUTHOR_STATED | PAPER_FULLTEXT | Sec. IV-A | Performance averaged over 5 random seeds | 10.1109/TNNLS.2024.3386810 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E066_019 | EXPERIMENT | EXP_KT066_MAIN | resampling_repeats | 1 | REVIEWER_INFERRED | PAPER_FULLTEXT | Sec. IV-A | Single random train/test split repeated across 5 model seeds | Codebook v0.4 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E066_020 | EXPERIMENT | EXP_KT066_MAIN | repeated_run_unit | SEED_REPETITION | REVIEWER_INFERRED | PAPER_FULLTEXT | Sec. IV-A | Seed repetition unit (CB13) | Codebook v0.4 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E066_021 | EXPERIMENT | EXP_KT066_MAIN | sparse_concept_ontology | GENERIC_DATA_SPARSITY | REVIEWER_INFERRED | PAPER_FULLTEXT | Sec. IV-C | Addressed data sparsity generally; no zero-exposure cold-start KC split evaluated | 10.1109/TNNLS.2024.3386810 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E066_022 | EXPERIMENT | EXP_KT066_MAIN | statistical_testing | NR | AUTHOR_STATED | PAPER_FULLTEXT | Sec. IV | DeLong test / Wilcoxon signed-rank / Holm-Bonferroni correction not reported | 10.1109/TNNLS.2024.3386810 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E066_023 | EXPERIMENT | EXP_KT066_MAIN | calibration_metrics | NR | AUTHOR_STATED | PAPER_FULLTEXT | Sec. IV | ECE and Brier Score omitted | 10.1109/TNNLS.2024.3386810 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
