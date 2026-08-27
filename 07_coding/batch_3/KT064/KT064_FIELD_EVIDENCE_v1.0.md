# KT064 Field-Level Evidence Table (v1.0 LOCKED)

This document contains the long-form field-level evidence records for paper **KT064**, satisfying the schema required in `coding_codebook_v1.0_LOCKED.md`.

## Schema
`evidence_id` | `entity_level` | `entity_id` | `field_name` | `coded_value` | `coding_basis` | `evidence_source_type` | `evidence_locator` | `evidence_note` | `source_url` | `coder_id` | `coder_type` | `coder_confidence` | `adjudication_status`

---

## Evidence Records

| evidence_id | entity_level | entity_id | field_name | coded_value | coding_basis | evidence_source_type | evidence_locator | evidence_note | source_url | coder_id | coder_type | coder_confidence | adjudication_status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| E064_001 | PAPER | PAPER_KT064 | title | Multi-Granularity Ensemble Interaction Graph Modeling for Knowledge Tracing | AUTHOR_STATED | PUBLISHER_METADATA | Article Title | Published journal title | 10.1016/j.knosys.2024.112834 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E064_002 | PAPER | PAPER_KT064 | venue | Knowledge-Based Systems | AUTHOR_STATED | PUBLISHER_METADATA | Journal Header | KBS Vol. 309, Article 112834, 2025 | 10.1016/j.knosys.2024.112834 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E064_003 | PAPER | PAPER_KT064 | kt_central_task | YES | AUTHOR_STATED | PAPER_FULLTEXT | Abstract & Sec. 1 | Sequential student performance prediction & multi-granularity interaction graph modeling | 10.1016/j.knosys.2024.112834 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E064_004 | PAPER | PAPER_KT064 | G_criterion | YES | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3 & 4 | Multi-granularity ensemble interaction graph modeling with GNN | 10.1016/j.knosys.2024.112834 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E064_005 | PAPER | PAPER_KT064 | S_criterion | NO | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4.4 | Supervised ensemble prediction loss only | 10.1016/j.knosys.2024.112834 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E064_006 | PAPER | PAPER_KT064 | corpus_tier | PRIMARY_CORE | REVIEWER_INFERRED | PAPER_FULLTEXT | Protocol Sec. 4 | Primary core: satisfies G-criterion | Scope v1.0 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E064_007 | PAPER | PAPER_KT064 | coding_completeness | FULLTEXT_CODED | REVIEWER_INFERRED | PAPER_FULLTEXT | Full Text | Peer-reviewed journal text fully inspected | 10.1016/j.knosys.2024.112834 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E064_008 | MODEL | MODEL_KT064_MG_ENSEMBLE | graph_source | Q_MATRIX, SEQUENTIAL_TRANSITION, CO_OCCURRENCE | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.1 | Multi-granularity interaction graphs constructed across fine-grained exercises and coarse-grained concepts | 10.1016/j.knosys.2024.112834 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E064_009 | MODEL | MODEL_KT064_MG_ENSEMBLE | gnn_encoder | GRAPH_CONVOLUTIONAL_NETWORK | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.2 | Multi-granularity Graph Convolutional Network encoder | 10.1016/j.knosys.2024.112834 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E064_010 | MODEL | MODEL_KT064_MG_ENSEMBLE | temporal_backbone | RNN_LSTM_GRU | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.3 | GRU sequence backbone for temporal state tracking | 10.1016/j.knosys.2024.112834 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E064_011 | MODEL | MODEL_KT064_MG_ENSEMBLE | ssl_family | NONE | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4.4 | Supervised prediction loss only | 10.1016/j.knosys.2024.112834 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E064_012 | EXPERIMENT | EXP_KT064_MAIN | datasets | ASSISTments2009, ASSISTments2017, Statics2011, Junyi | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 5.1 | Evaluated on 4 public benchmark educational datasets | 10.1016/j.knosys.2024.112834 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
