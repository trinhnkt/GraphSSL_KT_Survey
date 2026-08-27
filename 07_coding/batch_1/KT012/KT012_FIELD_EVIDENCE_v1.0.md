# KT012 Field-Level Evidence Table (v1.0 LOCKED)

This document contains the long-form field-level evidence records for paper **KT012 (JKT)**, satisfying the schema required in `coding_codebook_v1.0_LOCKED.md`.

## Schema
`evidence_id` | `entity_level` | `entity_id` | `field_name` | `coded_value` | `coding_basis` | `evidence_source_type` | `evidence_locator` | `evidence_note` | `source_url` | `coder_id` | `coder_type` | `coder_confidence` | `adjudication_status`

---

## Evidence Records

| evidence_id | entity_level | entity_id | field_name | coded_value | coding_basis | evidence_source_type | evidence_locator | evidence_note | source_url | coder_id | coder_type | coder_confidence | adjudication_status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| E012_001 | PAPER | PAPER_KT012 | title | JKT: A Joint Graph Convolutional Network Based Deep Knowledge Tracing | AUTHOR_STATED | PUBLISHER_METADATA | Article Title | Published journal title | 10.1016/j.ins.2021.08.100 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E012_002 | PAPER | PAPER_KT012 | venue | Information Sciences | AUTHOR_STATED | PUBLISHER_METADATA | Journal Header | Information Sciences Vol. 580, pp. 510–523, 2021 | 10.1016/j.ins.2021.08.100 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E012_003 | PAPER | PAPER_KT012 | kt_central_task | YES | AUTHOR_STATED | PAPER_FULLTEXT | Abstract & Sec. 1 | Sequential learner response prediction & state estimation | 10.1016/j.ins.2021.08.100 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E012_004 | PAPER | PAPER_KT012 | G_criterion | YES | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3 & 4 | Joint GCN over exercise-to-exercise & concept-to-concept graphs fused with Q-matrix | 10.1016/j.ins.2021.08.100 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E012_005 | PAPER | PAPER_KT012 | S_criterion | NO | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4.4 | Supervised cross-entropy prediction loss only | 10.1016/j.ins.2021.08.100 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E012_006 | PAPER | PAPER_KT012 | corpus_tier | PRIMARY_CORE | REVIEWER_INFERRED | PAPER_FULLTEXT | Protocol Sec. 4 | Primary core: satisfies G-criterion | Scope v1.0 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E012_007 | PAPER | PAPER_KT012 | coding_completeness | FULLTEXT_CODED | REVIEWER_INFERRED | PAPER_FULLTEXT | Full Text | Peer-reviewed journal text fully inspected | 10.1016/j.ins.2021.08.100 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E012_008 | MODEL | MODEL_KT012_JKT | graph_source | Q_MATRIX, CO_OCCURRENCE | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.1 | Exercise-exercise & concept-concept graphs fused with Q-matrix relations | 10.1016/j.ins.2021.08.100 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E012_009 | MODEL | MODEL_KT012_JKT | gnn_encoder | GCN | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.2 | Joint Graph Convolutional Network (GCN) encoder | 10.1016/j.ins.2021.08.100 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E012_010 | MODEL | MODEL_KT012_JKT | temporal_backbone | RNN_LSTM_GRU | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.3 | LSTM sequence layer for learner state tracing | 10.1016/j.ins.2021.08.100 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E012_011 | MODEL | MODEL_KT012_JKT | ssl_family | NONE | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4.4 | Supervised loss only | 10.1016/j.ins.2021.08.100 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E012_012 | EXPERIMENT | EXP_KT012_MAIN | datasets | ASSISTments2009, ASSISTments2012, Statics2011, KDD Cup 2010 | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 5.1 | Evaluated on 4 public benchmark educational datasets | 10.1016/j.ins.2021.08.100 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
