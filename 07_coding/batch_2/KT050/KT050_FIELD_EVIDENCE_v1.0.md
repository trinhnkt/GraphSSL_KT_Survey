# KT050 Field-Level Evidence Table (v1.0 LOCKED)

This document contains the long-form field-level evidence records for paper **KT050 (GraphCA)**, satisfying the schema required in `coding_codebook_v1.0_LOCKED.md`.

## Schema
`evidence_id` | `entity_level` | `entity_id` | `field_name` | `coded_value` | `coding_basis` | `evidence_source_type` | `evidence_locator` | `evidence_note` | `source_url` | `coder_id` | `coder_type` | `coder_confidence` | `adjudication_status`

---

## Evidence Records

| evidence_id | entity_level | entity_id | field_name | coded_value | coding_basis | evidence_source_type | evidence_locator | evidence_note | source_url | coder_id | coder_type | coder_confidence | adjudication_status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| E050_001 | PAPER | PAPER_KT050 | title | GraphCA: Learning from Graph Counterfactual Augmentation for Knowledge Tracing | AUTHOR_STATED | PUBLISHER_METADATA | Article Title | Published journal title | 10.1109/JAS.2023.123678 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E050_002 | PAPER | PAPER_KT050 | venue | IEEE/CAA Journal of Automatica Sinica | AUTHOR_STATED | PUBLISHER_METADATA | Journal Header | IEEE JAS Vol. 10, Issue 11, pp. 2108–2123, 2023 | 10.1109/JAS.2023.123678 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E050_003 | PAPER | PAPER_KT050 | kt_central_task | YES | AUTHOR_STATED | PAPER_FULLTEXT | Abstract & Sec. 1 | Sequential student performance prediction & knowledge tracing | 10.1109/JAS.2023.123678 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E050_004 | PAPER | PAPER_KT050 | G_criterion | YES | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3 & 4 | Heterogeneous Graph Convolutional Network over student-question-concept nodes | 10.1109/JAS.2023.123678 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E050_005 | PAPER | PAPER_KT050 | S_criterion | YES | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4.4 | Self-supervised contrastive learning with graph counterfactual augmentation | 10.1109/JAS.2023.123678 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E050_006 | PAPER | PAPER_KT050 | corpus_tier | PRIMARY_CORE | REVIEWER_INFERRED | PAPER_FULLTEXT | Protocol Sec. 4 | Primary core: satisfies G-criterion and S-criterion | Scope v1.0 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E050_007 | PAPER | PAPER_KT050 | coding_completeness | FULLTEXT_CODED | REVIEWER_INFERRED | PAPER_FULLTEXT | Full Text | Peer-reviewed journal text fully inspected | 10.1109/JAS.2023.123678 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E050_008 | MODEL | MODEL_KT050_GraphCA | graph_source | Q_MATRIX, LEARNED_FROM_INTERACTIONS | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.1 | Heterogeneous graph connecting student, question, and concept nodes | 10.1109/JAS.2023.123678 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E050_009 | MODEL | MODEL_KT050_GraphCA | gnn_encoder | HETEROGENEOUS_GNN | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.2 | Heterogeneous Graph Convolutional Network encoder | 10.1109/JAS.2023.123678 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E050_010 | MODEL | MODEL_KT050_GraphCA | temporal_backbone | RNN_LSTM_GRU | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.3 | GRU sequence backbone for learner state tracking | 10.1109/JAS.2023.123678 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E050_011 | MODEL | MODEL_KT050_GraphCA | ssl_family | GRAPH_CONTRASTIVE, MULTIVIEW_CONTRASTIVE | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4.4 | Graph counterfactual contrastive learning loss between factual and counterfactual views | 10.1109/JAS.2023.123678 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E050_012 | EXPERIMENT | EXP_KT050_MAIN | datasets | ASSISTments2009, ASSISTments2017, Junyi | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 5.1 | Evaluated on 3 public benchmark educational datasets | 10.1109/JAS.2023.123678 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
