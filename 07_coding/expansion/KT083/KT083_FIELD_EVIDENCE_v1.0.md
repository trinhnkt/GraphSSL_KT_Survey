# KT083 Field-Level Evidence Table (v1.0 LOCKED)

This document contains the long-form field-level evidence records for paper **KT083 (DV-HGCL)**, satisfying the schema required in `coding_codebook_v1.0_LOCKED.md`.

## Schema
`evidence_id` | `entity_level` | `entity_id` | `field_name` | `coded_value` | `coding_basis` | `evidence_source_type` | `evidence_locator` | `evidence_note` | `source_url` | `coder_id` | `coder_type` | `coder_confidence` | `adjudication_status`

---

## Evidence Records

| evidence_id | entity_level | entity_id | field_name | coded_value | coding_basis | evidence_source_type | evidence_locator | evidence_note | source_url | coder_id | coder_type | coder_confidence | adjudication_status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| E083_001 | PAPER | PAPER_KT083 | title | Dual-View Heterogeneous Graph Contrastive Learning for Knowledge Tracing | AUTHOR_STATED | PUBLISHER_METADATA | Article Title | Published journal title | 10.1016/j.neunet.2026.107500 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E083_002 | PAPER | PAPER_KT083 | venue | Neural Networks | AUTHOR_STATED | PUBLISHER_METADATA | Journal Header | Neural Networks Vol. 182, Article 107500, 2026 | 10.1016/j.neunet.2026.107500 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E083_003 | PAPER | PAPER_KT083 | kt_central_task | YES | AUTHOR_STATED | PAPER_FULLTEXT | Abstract & Sec. 1 | Sequential learner response prediction & dual-view heterogeneous contrastive state tracing | 10.1016/j.neunet.2026.107500 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E083_004 | PAPER | PAPER_KT083 | G_criterion | YES | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3 & 4 | Dual-view heterogeneous graph neural network over question and concept graphs | 10.1016/j.neunet.2026.107500 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E083_005 | PAPER | PAPER_KT083 | S_criterion | YES | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4.4 | Dual-view heterogeneous graph contrastive learning pretext task | 10.1016/j.neunet.2026.107500 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E083_006 | PAPER | PAPER_KT083 | corpus_tier | PRIMARY_CORE | REVIEWER_INFERRED | PAPER_FULLTEXT | Protocol Sec. 4 | Primary core: satisfies G-criterion and S-criterion | Scope v1.0 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E083_007 | PAPER | PAPER_KT083 | coding_completeness | FULLTEXT_CODED | REVIEWER_INFERRED | PAPER_FULLTEXT | Full Text | Peer-reviewed journal text fully inspected | 10.1016/j.neunet.2026.107500 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E083_008 | MODEL | MODEL_KT083_DV_HGCL | graph_source | Q_MATRIX, CURRICULUM_CONCEPT_MAP, SIMILARITY | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.1 | Dual-view heterogeneous graph constructed from question-level and concept-level structural views | 10.1016/j.neunet.2026.107500 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E083_009 | MODEL | MODEL_KT083_DV_HGCL | gnn_encoder | HETEROGENEOUS_GNN | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.2 | Dual-view Heterogeneous Graph Neural Network encoder | 10.1016/j.neunet.2026.107500 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E083_010 | MODEL | MODEL_KT083_DV_HGCL | temporal_backbone | RNN_LSTM_GRU | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.3 | GRU sequence backbone for temporal state tracking | 10.1016/j.neunet.2026.107500 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E083_011 | MODEL | MODEL_KT083_DV_HGCL | ssl_family | GRAPH_CONTRASTIVE, MULTIVIEW_CONTRASTIVE | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4.4 | Cross-view heterogeneous contrastive loss between question and concept graph views | 10.1016/j.neunet.2026.107500 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E083_012 | EXPERIMENT | EXP_KT083_MAIN | datasets | ASSISTments2009, ASSISTments2017, EdNet | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 5.1 | Evaluated on 3 public benchmark educational datasets | 10.1016/j.neunet.2026.107500 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
