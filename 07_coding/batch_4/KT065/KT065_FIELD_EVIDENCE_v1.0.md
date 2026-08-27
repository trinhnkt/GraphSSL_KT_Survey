# KT065 Field-Level Evidence Table (v1.0 LOCKED)

This document contains the long-form field-level evidence records for paper **KT065**, satisfying the schema required in `coding_codebook_v1.0_LOCKED.md`.

## Schema
`evidence_id` | `entity_level` | `entity_id` | `field_name` | `coded_value` | `coding_basis` | `evidence_source_type` | `evidence_locator` | `evidence_note` | `source_url` | `coder_id` | `coder_type` | `coder_confidence` | `adjudication_status`

---

## Evidence Records

| evidence_id | entity_level | entity_id | field_name | coded_value | coding_basis | evidence_source_type | evidence_locator | evidence_note | source_url | coder_id | coder_type | coder_confidence | adjudication_status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| E065_001 | PAPER | PAPER_KT065 | title | Graph Knowledge Tracing in Cognitive Situation: Validation of Classic Assertions in Cognitive Psychology | AUTHOR_STATED | PUBLISHER_METADATA | Article Title | Published journal title | 10.1016/j.knosys.2025.113281 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E065_002 | PAPER | PAPER_KT065 | venue | Knowledge-Based Systems | AUTHOR_STATED | PUBLISHER_METADATA | Journal Header | KBS Vol. 315, Article 113281, 2025 | 10.1016/j.knosys.2025.113281 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E065_003 | PAPER | PAPER_KT065 | kt_central_task | YES | AUTHOR_STATED | PAPER_FULLTEXT | Abstract & Sec. 1 | Sequential student performance prediction & cognitive situation tracing | 10.1016/j.knosys.2025.113281 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E065_004 | PAPER | PAPER_KT065 | G_criterion | YES | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3 & 4 | Cognitive situation graph neural network encoding cognitive psychology structure | 10.1016/j.knosys.2025.113281 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E065_005 | PAPER | PAPER_KT065 | S_criterion | NO | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4.4 | Supervised prediction loss only | 10.1016/j.knosys.2025.113281 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E065_006 | PAPER | PAPER_KT065 | corpus_tier | PRIMARY_CORE | REVIEWER_INFERRED | PAPER_FULLTEXT | Protocol Sec. 4 | Primary core: satisfies G-criterion | Scope v1.0 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E065_007 | PAPER | PAPER_KT065 | coding_completeness | FULLTEXT_CODED | REVIEWER_INFERRED | PAPER_FULLTEXT | Full Text | Peer-reviewed journal text fully inspected | 10.1016/j.knosys.2025.113281 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E065_008 | MODEL | MODEL_KT065_CS_GKT | graph_source | CURRICULUM_CONCEPT_MAP, Q_MATRIX | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.1 | Cognitive situation graph constructed from psychological cognitive models and Q-matrix | 10.1016/j.knosys.2025.113281 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E065_009 | MODEL | MODEL_KT065_CS_GKT | gnn_encoder | GRAPH_CONVOLUTIONAL_NETWORK | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.2 | Cognitive Situation Graph Convolutional Network encoder | 10.1016/j.knosys.2025.113281 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E065_010 | MODEL | MODEL_KT065_CS_GKT | temporal_backbone | RNN_LSTM_GRU | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.3 | GRU sequence backbone for cognitive state tracing | 10.1016/j.knosys.2025.113281 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E065_011 | MODEL | MODEL_KT065_CS_GKT | ssl_family | NONE | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4.4 | Supervised prediction loss only | 10.1016/j.knosys.2025.113281 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E065_012 | EXPERIMENT | EXP_KT065_MAIN | datasets | ASSISTments2009, ASSISTments2017, Statics2011 | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 5.1 | Evaluated on 3 public benchmark educational datasets | 10.1016/j.knosys.2025.113281 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
