# KT010 Field-Level Evidence Table (v0.4 PILOT)

This document contains the long-form field-level evidence records for paper **KT010 (GIKT)**, satisfying the schema required in Section 2 of `coding_codebook_v0.4_PILOT.md`.

## Schema
`evidence_id` | `entity_level` | `entity_id` | `field_name` | `coded_value` | `coding_basis` | `evidence_source_type` | `evidence_locator` | `evidence_note` | `source_url` | `coder_id` | `coder_type` | `coder_confidence` | `adjudication_status`

---

## Evidence Records

| evidence_id | entity_level | entity_id | field_name | coded_value | coding_basis | evidence_source_type | evidence_locator | evidence_note | source_url | coder_id | coder_type | coder_confidence | adjudication_status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| E010_001 | PAPER | PAPER_KT010 | title | GIKT: A Graph-Based Interaction Model for Knowledge Tracing | AUTHOR_STATED | PUBLISHER_METADATA | Title | Official published article title | 10.1007/978-3-030-67658-2_18 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E010_002 | PAPER | PAPER_KT010 | venue | ECML-PKDD | AUTHOR_STATED | PUBLISHER_METADATA | Conference Header | Springer LNCS Vol. 12458, pp. 299–315, 2021 | 10.1007/978-3-030-67658-2_18 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E010_003 | PAPER | PAPER_KT010 | kt_central_task | YES | AUTHOR_STATED | PAPER_FULLTEXT | Abstract & Sec. 1 | Sequential learner-state estimation & performance prediction | 10.1007/978-3-030-67658-2_18 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E010_004 | PAPER | PAPER_KT010 | G_criterion | YES | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.1 & 3.2 | Question–concept bipartite interaction graph with GCN embedding propagation | 10.1007/978-3-030-67658-2_18 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E010_005 | PAPER | PAPER_KT010 | S_criterion | NO | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.4 | Supervised cross-entropy KT loss only; no SSL pretext objective | 10.1007/978-3-030-67658-2_18 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E010_006 | PAPER | PAPER_KT010 | corpus_tier | PRIMARY_CORE | REVIEWER_INFERRED | PAPER_FULLTEXT | Protocol Section 4 | Primary core: satisfies G-criterion | Scope v1.0 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E010_007 | PAPER | PAPER_KT010 | coding_completeness | FULLTEXT_CODED | REVIEWER_INFERRED | PAPER_FULLTEXT | Full Text | Peer-reviewed ECML-PKDD proceedings paper full text thoroughly inspected | 10.1007/978-3-030-67658-2_18 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E010_008 | MODEL | MODEL_KT010_GIKT | graph_source | Q_MATRIX, CO_OCCURRENCE | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.1 | Question-concept bipartite graph derived from Q-matrix and interaction relations | 10.1007/978-3-030-67658-2_18 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E010_009 | MODEL | MODEL_KT010_GIKT | graph_provenance | PRECOMPUTED_UNCLEAR_SPLIT | REVIEWER_INFERRED | PAPER_FULLTEXT | Sec. 3.1 | Bipartite graph precomputed from dataset Q-matrix / logs | 10.1007/978-3-030-67658-2_18 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E010_010 | MODEL | MODEL_KT010_GIKT | graph_leakage_risk | POTENTIAL | REVIEWER_INFERRED | PAPER_FULLTEXT | Sec. 3.1 & Protocol Sec 7 | Precomputed question-concept bipartite adjacency without explicit train-only isolation | Codebook v0.4 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E010_011 | MODEL | MODEL_KT010_GIKT | graph_representation | ITEM_KC_BIPARTITE, KC_KC | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.1 | Bipartite graph connecting Question/Exercise nodes to Concept/Skill nodes | 10.1007/978-3-030-67658-2_18 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E010_012 | MODEL | MODEL_KT010_GIKT | directed | N | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.1 | Undirected bipartite adjacency matrix $A$ between questions and concepts | 10.1007/978-3-030-67658-2_18 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E010_013 | MODEL | MODEL_KT010_GIKT | typed_edges | N | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.1 | Single membership relation type between questions and concepts | 10.1007/978-3-030-67658-2_18 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E010_014 | MODEL | MODEL_KT010_GIKT | gnn_encoder | GCN | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.2 | Graph Convolutional Network (GCN) embedding propagation over bipartite graph | 10.1007/978-3-030-67658-2_18 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E010_015 | MODEL | MODEL_KT010_GIKT | temporal_backbone | RNN_LSTM_GRU | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.3 | LSTM sequence layer + recap interaction module | 10.1007/978-3-030-67658-2_18 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E010_016 | MODEL | MODEL_KT010_GIKT | ssl_family | NONE | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.4 | Supervised cross-entropy KT loss only | 10.1007/978-3-030-67658-2_18 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E010_017 | EXPERIMENT | EXP_KT010_MAIN | datasets | ASSISTments2009, ASSISTments2012, Statics2011, Junyi | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4.1 | Evaluated on 4 public benchmark educational datasets | 10.1007/978-3-030-67658-2_18 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E010_018 | EXPERIMENT | EXP_KT010_MAIN | n_seeds | 5 | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4.1 | Performance averaged over 5 random seeds | 10.1007/978-3-030-67658-2_18 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E010_019 | EXPERIMENT | EXP_KT010_MAIN | resampling_repeats | 1 | REVIEWER_INFERRED | PAPER_FULLTEXT | Sec. 4.1 | Single random train/test split repeated across 5 model seeds | Codebook v0.4 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E010_020 | EXPERIMENT | EXP_KT010_MAIN | repeated_run_unit | SEED_REPETITION | REVIEWER_INFERRED | PAPER_FULLTEXT | Sec. 4.1 | Seed repetition unit (CB13) | Codebook v0.4 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E010_021 | EXPERIMENT | EXP_KT010_MAIN | sparse_concept_ontology | GENERIC_DATA_SPARSITY | REVIEWER_INFERRED | PAPER_FULLTEXT | Sec. 4.3 | Addressed data sparsity generally; no zero-exposure cold-start KC split evaluated | 10.1007/978-3-030-67658-2_18 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E010_022 | EXPERIMENT | EXP_KT010_MAIN | statistical_testing | NR | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4 | DeLong test / Wilcoxon signed-rank / Holm-Bonferroni correction not reported | 10.1007/978-3-030-67658-2_18 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E010_023 | EXPERIMENT | EXP_KT010_MAIN | calibration_metrics | NR | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4 | ECE and Brier Score omitted | 10.1007/978-3-030-67658-2_18 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
