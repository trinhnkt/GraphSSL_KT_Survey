# KT026 Field-Level Evidence Table (v0.4 PILOT)

This document contains the long-form field-level evidence records for paper **KT026**, satisfying the schema required in Section 2 of `coding_codebook_v0.4_PILOT.md`.

## Schema
`evidence_id` | `entity_level` | `entity_id` | `field_name` | `coded_value` | `coding_basis` | `evidence_source_type` | `evidence_locator` | `evidence_note` | `source_url` | `coder_id` | `coder_type` | `coder_confidence` | `adjudication_status`

---

## Evidence Records

| evidence_id | entity_level | entity_id | field_name | coded_value | coding_basis | evidence_source_type | evidence_locator | evidence_note | source_url | coder_id | coder_type | coder_confidence | adjudication_status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| E026_001 | PAPER | PAPER_KT026 | title | Improving Knowledge Tracing via Pre-Training Question Embeddings | AUTHOR_STATED | PUBLISHER_METADATA | Title | Official published IJCAI conference title | 10.24963/ijcai.2020/219 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E026_002 | PAPER | PAPER_KT026 | venue | IJCAI | AUTHOR_STATED | PUBLISHER_METADATA | Conference Header | IJCAI 2020 Conference Proceedings | 10.24963/ijcai.2020/219 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E026_003 | PAPER | PAPER_KT026 | kt_central_task | YES | AUTHOR_STATED | PAPER_FULLTEXT | Abstract & Sec. 1 | Sequential learner response prediction & knowledge state tracing | 10.24963/ijcai.2020/219 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E026_004 | PAPER | PAPER_KT026 | G_criterion | YES | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3 & 4 | Pre-trains question embeddings from question-skill bipartite graph using product-based neural networks | 10.24963/ijcai.2020/219 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E026_005 | PAPER | PAPER_KT026 | S_criterion | NO | REVIEWER_INFERRED | PAPER_FULLTEXT | Sec. 4.4 | Generic question embedding pretraining on bipartite graph, NOT a self-supervised pretext task loss during KT sequence tracing | 10.24963/ijcai.2020/219 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E026_006 | PAPER | PAPER_KT026 | corpus_tier | PRIMARY_CORE | REVIEWER_INFERRED | PAPER_FULLTEXT | Protocol Sec. 4 | Primary core: satisfies G-criterion via graph-derived pre-trained representations | Scope v1.0 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E026_007 | PAPER | PAPER_KT026 | coding_completeness | FULLTEXT_CODED | REVIEWER_INFERRED | PAPER_FULLTEXT | Full Text | Peer-reviewed IJCAI 2020 proceedings full text thoroughly inspected | 10.24963/ijcai.2020/219 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E026_008 | MODEL | MODEL_KT026_PRETRAIN | graph_source | Q_MATRIX, ITEM_KC_BIPARTITE | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.1 | Question-skill bipartite graph constructed from Q-matrix and question difficulty relations | 10.24963/ijcai.2020/219 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E026_009 | MODEL | MODEL_KT026_PRETRAIN | graph_provenance | PRECOMPUTED_UNCLEAR_SPLIT | REVIEWER_INFERRED | PAPER_FULLTEXT | Sec. 3.1 | Bipartite graph precomputed prior to sequence tracing without explicit train-only isolation reporting | 10.24963/ijcai.2020/219 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E026_010 | MODEL | MODEL_KT026_PRETRAIN | graph_leakage_risk | POTENTIAL | REVIEWER_INFERRED | PAPER_FULLTEXT | Sec. 3.1 & Protocol Sec 7 | Precomputed question-skill bipartite graph without explicit train/test isolation | Codebook v0.4 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E026_011 | MODEL | MODEL_KT026_PRETRAIN | graph_representation | ITEM_KC_BIPARTITE | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.1 | Bipartite graph connecting Question nodes to Skill/Concept nodes | 10.24963/ijcai.2020/219 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E026_012 | MODEL | MODEL_KT026_PRETRAIN | directed | N | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.1 | Undirected bipartite membership graph | 10.24963/ijcai.2020/219 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E026_013 | MODEL | MODEL_KT026_PRETRAIN | typed_edges | N | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.1 | Single question-skill mapping relation type | 10.24963/ijcai.2020/219 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E026_014 | MODEL | MODEL_KT026_PRETRAIN | gnn_encoder | NONE | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.2 | Product-based neural network (PNN) matrix factorization for pre-training embeddings | 10.24963/ijcai.2020/219 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E026_015 | MODEL | MODEL_KT026_PRETRAIN | temporal_backbone | RNN_LSTM_GRU | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.3 | LSTM backbone initialized with pre-trained question embeddings | 10.24963/ijcai.2020/219 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E026_016 | MODEL | MODEL_KT026_PRETRAIN | ssl_family | NONE | REVIEWER_INFERRED | PAPER_FULLTEXT | Sec. 4.4 | Generic graph feature pre-training; no self-supervised pretext task loss during KT sequence tracing | 10.24963/ijcai.2020/219 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E026_017 | EXPERIMENT | EXP_KT026_MAIN | datasets | ASSISTments2009, Statics2011, Junyi | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 5.1 | Evaluated on 3 benchmark educational datasets | 10.24963/ijcai.2020/219 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E026_018 | EXPERIMENT | EXP_KT026_MAIN | n_seeds | 5 | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 5.1 | Performance averaged over 5 random seeds | 10.24963/ijcai.2020/219 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E026_019 | EXPERIMENT | EXP_KT026_MAIN | resampling_repeats | 1 | REVIEWER_INFERRED | PAPER_FULLTEXT | Sec. 5.1 | Single train/test data split repeated across seeds | Codebook v0.4 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E026_020 | EXPERIMENT | EXP_KT026_MAIN | repeated_run_unit | SEED_REPETITION | REVIEWER_INFERRED | PAPER_FULLTEXT | Sec. 5.1 | Seed repetition unit (CB13) | Codebook v0.4 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
