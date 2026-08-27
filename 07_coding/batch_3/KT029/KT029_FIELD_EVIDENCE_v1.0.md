# KT029 Field-Level Evidence Table (v1.0 LOCKED)

This document contains the long-form field-level evidence records for paper **KT029 (DGEKT)**, satisfying the schema required in `coding_codebook_v1.0_LOCKED.md`.

## Schema
`evidence_id` | `entity_level` | `entity_id` | `field_name` | `coded_value` | `coding_basis` | `evidence_source_type` | `evidence_locator` | `evidence_note` | `source_url` | `coder_id` | `coder_type` | `coder_confidence` | `adjudication_status`

---

## Evidence Records

| evidence_id | entity_level | entity_id | field_name | coded_value | coding_basis | evidence_source_type | evidence_locator | evidence_note | source_url | coder_id | coder_type | coder_confidence | adjudication_status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| E029_001 | PAPER | PAPER_KT029 | title | DGEKT: A Dual Graph Ensemble Learning Method for Knowledge Tracing | AUTHOR_STATED | PUBLISHER_METADATA | Article Title | Published journal title | 10.1145/3635303 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E029_002 | PAPER | PAPER_KT029 | venue | ACM Transactions on Information Systems | AUTHOR_STATED | PUBLISHER_METADATA | Journal Header | ACM TOIS Vol. 42, Issue 3, Art. 78, 2024 | 10.1145/3635303 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E029_003 | PAPER | PAPER_KT029 | kt_central_task | YES | AUTHOR_STATED | PAPER_FULLTEXT | Abstract & Sec. 1 | Sequential student performance prediction & knowledge tracing | 10.1145/3635303 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E029_004 | PAPER | PAPER_KT029 | G_criterion | YES | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3 & 4 | Dual graph ensemble GNN architecture (static concept graph + dynamic interaction graph) | 10.1145/3635303 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E029_005 | PAPER | PAPER_KT029 | S_criterion | NO | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4.4 | Supervised ensemble prediction loss only | 10.1145/3635303 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E029_006 | PAPER | PAPER_KT029 | corpus_tier | PRIMARY_CORE | REVIEWER_INFERRED | PAPER_FULLTEXT | Protocol Sec. 4 | Primary core: satisfies G-criterion | Scope v1.0 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E029_007 | PAPER | PAPER_KT029 | coding_completeness | FULLTEXT_CODED | REVIEWER_INFERRED | PAPER_FULLTEXT | Full Text | Peer-reviewed journal text fully inspected | 10.1145/3635303 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E029_008 | MODEL | MODEL_KT029_DGEKT | graph_source | Q_MATRIX, CO_OCCURRENCE, SEQUENTIAL_TRANSITION | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.1 | Dual graphs derived from Q-matrix static structure and dynamic interaction transitions | 10.1145/3635303 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E029_009 | MODEL | MODEL_KT029_DGEKT | gnn_encoder | GRAPH_CONVOLUTIONAL_NETWORK | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.2 | Dual GCN encoders processing static and dynamic graph structures | 10.1145/3635303 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E029_010 | MODEL | MODEL_KT029_DGEKT | temporal_backbone | RNN_LSTM_GRU | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.3 | GRU sequence backbone for temporal state tracking | 10.1145/3635303 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E029_011 | MODEL | MODEL_KT029_DGEKT | ssl_family | NONE | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4.4 | Supervised prediction loss only | 10.1145/3635303 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E029_012 | EXPERIMENT | EXP_KT029_MAIN | datasets | ASSISTments2009, ASSISTments2017, Junyi, Statics2011 | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 5.1 | Evaluated on 4 public benchmark educational datasets | 10.1145/3635303 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
