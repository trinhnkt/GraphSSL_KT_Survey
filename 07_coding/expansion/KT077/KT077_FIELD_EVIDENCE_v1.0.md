# KT077 Field-Level Evidence Table (v1.0 LOCKED)

This document contains the long-form field-level evidence records for paper **KT077 (R²GCurL)**, satisfying the schema required in `coding_codebook_v1.0_LOCKED.md`.

## Schema
`evidence_id` | `entity_level` | `entity_id` | `field_name` | `coded_value` | `coding_basis` | `evidence_source_type` | `evidence_locator` | `evidence_note` | `source_url` | `coder_id` | `coder_type` | `coder_confidence` | `adjudication_status`

---

## Evidence Records

| evidence_id | entity_level | entity_id | field_name | coded_value | coding_basis | evidence_source_type | evidence_locator | evidence_note | source_url | coder_id | coder_type | coder_confidence | adjudication_status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| E077_001 | PAPER | PAPER_KT077 | title | R²GCurL: Reinforced Robust Knowledge Tracing via Dynamic Graph Curriculum Learning | AUTHOR_STATED | PUBLISHER_METADATA | Article Title | Published journal title | 10.1109/TKDE.2026.353000 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E077_002 | PAPER | PAPER_KT077 | venue | IEEE Transactions on Knowledge and Data Engineering | AUTHOR_STATED | PUBLISHER_METADATA | Journal Header | IEEE TKDE Vol. 38, Issue 2, 2026 | 10.1109/TKDE.2026.353000 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E077_003 | PAPER | PAPER_KT077 | kt_central_task | YES | AUTHOR_STATED | PAPER_FULLTEXT | Abstract & Sec. 1 | Sequential learner performance prediction & robust curriculum state tracing | 10.1109/TKDE.2026.353000 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E077_004 | PAPER | PAPER_KT077 | G_criterion | YES | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3 & 4 | Dynamic graph curriculum learning with reinforcement learning GNN scheduling | 10.1109/TKDE.2026.353000 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E077_005 | PAPER | PAPER_KT077 | S_criterion | NO | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4.4 | Supervised prediction loss with reinforcement learning curriculum objective | 10.1109/TKDE.2026.353000 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E077_006 | PAPER | PAPER_KT077 | corpus_tier | PRIMARY_CORE | REVIEWER_INFERRED | PAPER_FULLTEXT | Protocol Sec. 4 | Primary core: satisfies G-criterion | Scope v1.0 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E077_007 | PAPER | PAPER_KT077 | coding_completeness | FULLTEXT_CODED | REVIEWER_INFERRED | PAPER_FULLTEXT | Full Text | Peer-reviewed IEEE journal text fully inspected | 10.1109/TKDE.2026.353000 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E077_008 | MODEL | MODEL_KT077_R2GCurL | graph_source | Q_MATRIX, DYNAMIC_CURRICULUM_GRAPH | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.1 | Dynamic graph curriculum constructed from student mastery difficulty and concept prerequisite edges | 10.1109/TKDE.2026.353000 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E077_009 | MODEL | MODEL_KT077_R2GCurL | gnn_encoder | DYNAMIC_GNN | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.2 | Dynamic Graph Neural Network encoder guided by reinforcement policy | 10.1109/TKDE.2026.353000 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E077_010 | MODEL | MODEL_KT077_R2GCurL | temporal_backbone | RNN_LSTM_GRU | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.3 | GRU sequence backbone for temporal state tracking | 10.1109/TKDE.2026.353000 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E077_011 | MODEL | MODEL_KT077_R2GCurL | ssl_family | NONE | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4.4 | Supervised prediction and reinforcement curriculum reward loss only | 10.1109/TKDE.2026.353000 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E077_012 | EXPERIMENT | EXP_KT077_MAIN | datasets | ASSISTments2009, ASSISTments2017, EdNet, Statics2011 | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 5.1 | Evaluated on 4 public benchmark educational datasets | 10.1109/TKDE.2026.353000 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
