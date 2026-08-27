# KT067 Field-Level Evidence Table (v1.0 LOCKED)

This document contains the long-form field-level evidence records for paper **KT067**, satisfying the schema required in `coding_codebook_v1.0_LOCKED.md`.

## Schema
`evidence_id` | `entity_level` | `entity_id` | `field_name` | `coded_value` | `coding_basis` | `evidence_source_type` | `evidence_locator` | `evidence_note` | `source_url` | `coder_id` | `coder_type` | `coder_confidence` | `adjudication_status`

---

## Evidence Records

| evidence_id | entity_level | entity_id | field_name | coded_value | coding_basis | evidence_source_type | evidence_locator | evidence_note | source_url | coder_id | coder_type | coder_confidence | adjudication_status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| E067_001 | PAPER | PAPER_KT067 | title | Graph-Based Effective Knowledge Tracing via Subject Knowledge Mapping | AUTHOR_STATED | PUBLISHER_METADATA | Article Title | Published journal title | 10.1007/s10639-024-13069-0 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E067_002 | PAPER | PAPER_KT067 | venue | Education and Information Technologies | AUTHOR_STATED | PUBLISHER_METADATA | Journal Header | EAIT Vol. 30, Issue 7, pp. 9813–9840, 2025 | 10.1007/s10639-024-13069-0 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E067_003 | PAPER | PAPER_KT067 | kt_central_task | YES | AUTHOR_STATED | PAPER_FULLTEXT | Abstract & Sec. 1 | Sequential learner performance prediction & subject knowledge state tracking | 10.1007/s10639-024-13069-0 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E067_004 | PAPER | PAPER_KT067 | G_criterion | YES | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3 & 4 | Subject knowledge mapping graph GNN encoding domain concept structures | 10.1007/s10639-024-13069-0 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E067_005 | PAPER | PAPER_KT067 | S_criterion | NO | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4.4 | Supervised prediction loss only | 10.1007/s10639-024-13069-0 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E067_006 | PAPER | PAPER_KT067 | corpus_tier | PRIMARY_CORE | REVIEWER_INFERRED | PAPER_FULLTEXT | Protocol Sec. 4 | Primary core: satisfies G-criterion | Scope v1.0 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E067_007 | PAPER | PAPER_KT067 | coding_completeness | FULLTEXT_CODED | REVIEWER_INFERRED | PAPER_FULLTEXT | Full Text | Peer-reviewed journal text fully inspected | 10.1007/s10639-024-13069-0 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E067_008 | MODEL | MODEL_KT067_SKM_GKT | graph_source | CURRICULUM_CONCEPT_MAP, Q_MATRIX | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.1 | Subject knowledge mapping concept graph constructed from curriculum structure and Q-matrix | 10.1007/s10639-024-13069-0 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E067_009 | MODEL | MODEL_KT067_SKM_GKT | gnn_encoder | GRAPH_CONVOLUTIONAL_NETWORK | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.2 | Subject Knowledge Mapping Graph Convolutional Network encoder | 10.1007/s10639-024-13069-0 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E067_010 | MODEL | MODEL_KT067_SKM_GKT | temporal_backbone | RNN_LSTM_GRU | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.3 | GRU sequence layer for temporal subject state tracking | 10.1007/s10639-024-13069-0 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E067_011 | MODEL | MODEL_KT067_SKM_GKT | ssl_family | NONE | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4.4 | Supervised prediction loss only | 10.1007/s10639-024-13069-0 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E067_012 | EXPERIMENT | EXP_KT067_MAIN | datasets | ASSISTments2009, ASSISTments2017, KDD Cup 2010 | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 5.1 | Evaluated on 3 public benchmark educational datasets | 10.1007/s10639-024-13069-0 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
