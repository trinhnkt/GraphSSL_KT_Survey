# KT036 Field-Level Evidence Table (v1.0 LOCKED)

This document contains the long-form field-level evidence records for paper **KT036 (TSKT)**, satisfying the schema required in `coding_codebook_v1.0_LOCKED.md`.

## Schema
`evidence_id` | `entity_level` | `entity_id` | `field_name` | `coded_value` | `coding_basis` | `evidence_source_type` | `evidence_locator` | `evidence_note` | `source_url` | `coder_id` | `coder_type` | `coder_confidence` | `adjudication_status`

---

## Evidence Records

| evidence_id | entity_level | entity_id | field_name | coded_value | coding_basis | evidence_source_type | evidence_locator | evidence_note | source_url | coder_id | coder_type | coder_confidence | adjudication_status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| E036_001 | PAPER | PAPER_KT036 | title | Heterogeneous Graph-Based Knowledge Tracing with Spatiotemporal Evolution | AUTHOR_STATED | PUBLISHER_METADATA | Article Title | Published journal title | 10.1016/j.eswa.2023.122249 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E036_002 | PAPER | PAPER_KT036 | venue | Expert Systems with Applications | AUTHOR_STATED | PUBLISHER_METADATA | Journal Header | ESWA Vol. 238, Article 122249, 2024 | 10.1016/j.eswa.2023.122249 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E036_003 | PAPER | PAPER_KT036 | kt_central_task | YES | AUTHOR_STATED | PAPER_FULLTEXT | Abstract & Sec. 1 | Sequential learner performance prediction & spatiotemporal knowledge tracing | 10.1016/j.eswa.2023.122249 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E036_004 | PAPER | PAPER_KT036 | G_criterion | YES | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3 & 4 | Heterogeneous graph over student-exercise-concept nodes with spatiotemporal GNN evolution | 10.1016/j.eswa.2023.122249 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E036_005 | PAPER | PAPER_KT036 | S_criterion | NO | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4.4 | Supervised prediction loss only | 10.1016/j.eswa.2023.122249 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E036_006 | PAPER | PAPER_KT036 | corpus_tier | PRIMARY_CORE | REVIEWER_INFERRED | PAPER_FULLTEXT | Protocol Sec. 4 | Primary core: satisfies G-criterion | Scope v1.0 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E036_007 | PAPER | PAPER_KT036 | coding_completeness | FULLTEXT_CODED | REVIEWER_INFERRED | PAPER_FULLTEXT | Full Text | Peer-reviewed journal text fully inspected | 10.1016/j.eswa.2023.122249 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E036_008 | MODEL | MODEL_KT036_TSKT | graph_source | Q_MATRIX, CO_OCCURRENCE, SEQUENTIAL_TRANSITION | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.1 | Heterogeneous graph derived from Q-matrix, exercise co-occurrence, and interaction transitions | 10.1016/j.eswa.2023.122249 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E036_009 | MODEL | MODEL_KT036_TSKT | gnn_encoder | HETEROGENEOUS_GNN | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.2 | Heterogeneous Graph Neural Network with spatiotemporal evolution layers | 10.1016/j.eswa.2023.122249 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E036_010 | MODEL | MODEL_KT036_TSKT | temporal_backbone | RNN_LSTM_GRU | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.3 | GRU sequence backbone for temporal state tracking | 10.1016/j.eswa.2023.122249 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E036_011 | MODEL | MODEL_KT036_TSKT | ssl_family | NONE | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4.4 | Supervised prediction loss only | 10.1016/j.eswa.2023.122249 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E036_012 | EXPERIMENT | EXP_KT036_MAIN | datasets | ASSISTments2009, ASSISTments2017, Statics2011 | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 5.1 | Evaluated on 3 public benchmark educational datasets | 10.1016/j.eswa.2023.122249 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
