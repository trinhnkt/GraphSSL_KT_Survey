# KT052 Field-Level Evidence Table (v1.0 LOCKED)

This document contains the long-form field-level evidence records for paper **KT052**, satisfying the schema required in `coding_codebook_v1.0_LOCKED.md`.

## Schema
`evidence_id` | `entity_level` | `entity_id` | `field_name` | `coded_value` | `coding_basis` | `evidence_source_type` | `evidence_locator` | `evidence_note` | `source_url` | `coder_id` | `coder_type` | `coder_confidence` | `adjudication_status`

---

## Evidence Records

| evidence_id | entity_level | entity_id | field_name | coded_value | coding_basis | evidence_source_type | evidence_locator | evidence_note | source_url | coder_id | coder_type | coder_confidence | adjudication_status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| E052_001 | PAPER | PAPER_KT052 | title | Modeling Knowledge Proficiency Using Multi-Hierarchical Capsule Graph Neural Network | AUTHOR_STATED | PUBLISHER_METADATA | Article Title | Published journal title | 10.1007/s10489-021-02765-w | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E052_002 | PAPER | PAPER_KT052 | venue | Applied Intelligence | AUTHOR_STATED | PUBLISHER_METADATA | Journal Header | Applied Intelligence Vol. 52, Issue 7, pp. 7230–7247, 2022 | 10.1007/s10489-021-02765-w | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E052_003 | PAPER | PAPER_KT052 | kt_central_task | YES | AUTHOR_STATED | PAPER_FULLTEXT | Abstract & Sec. 1 | Sequential student response prediction & knowledge proficiency modeling | 10.1007/s10489-021-02765-w | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E052_004 | PAPER | PAPER_KT052 | G_criterion | YES | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3 & 4 | Multi-hierarchical capsule graph neural network over concept/exercise structures | 10.1007/s10489-021-02765-w | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E052_005 | PAPER | PAPER_KT052 | S_criterion | NO | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4.4 | Supervised prediction loss only | 10.1007/s10489-021-02765-w | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E052_006 | PAPER | PAPER_KT052 | corpus_tier | PRIMARY_CORE | REVIEWER_INFERRED | PAPER_FULLTEXT | Protocol Sec. 4 | Primary core: satisfies G-criterion | Scope v1.0 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E052_007 | PAPER | PAPER_KT052 | coding_completeness | FULLTEXT_CODED | REVIEWER_INFERRED | PAPER_FULLTEXT | Full Text | Peer-reviewed journal text fully inspected | 10.1007/s10489-021-02765-w | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E052_008 | MODEL | MODEL_KT052_CAPSULE_GNN | graph_source | CURRICULUM_CONCEPT_MAP, Q_MATRIX | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.1 | Multi-hierarchical concept graph constructed from domain structure and Q-matrix | 10.1007/s10489-021-02765-w | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E052_009 | MODEL | MODEL_KT052_CAPSULE_GNN | gnn_encoder | GRAPH_ATTENTION_HYBRID | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.2 | Capsule Graph Neural Network encoder with routing attention | 10.1007/s10489-021-02765-w | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E052_010 | MODEL | MODEL_KT052_CAPSULE_GNN | temporal_backbone | RNN_LSTM_GRU | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.3 | LSTM sequence layer for learner state tracing | 10.1007/s10489-021-02765-w | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E052_011 | MODEL | MODEL_KT052_CAPSULE_GNN | ssl_family | NONE | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4.4 | Supervised prediction loss only | 10.1007/s10489-021-02765-w | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E052_012 | EXPERIMENT | EXP_KT052_MAIN | datasets | ASSISTments2009, ASSISTments2015, Statics2011 | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 5.1 | Evaluated on 3 public benchmark educational datasets | 10.1007/s10489-021-02765-w | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
