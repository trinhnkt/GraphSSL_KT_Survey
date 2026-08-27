# KT070 Field-Level Evidence Table (v1.0 LOCKED)

This document contains the long-form field-level evidence records for paper **KT070 (Coda)**, satisfying the schema required in `coding_codebook_v1.0_LOCKED.md`.

## Schema
`evidence_id` | `entity_level` | `entity_id` | `field_name` | `coded_value` | `coding_basis` | `evidence_source_type` | `evidence_locator` | `evidence_note` | `source_url` | `coder_id` | `coder_type` | `coder_confidence` | `adjudication_status`

---

## Evidence Records

| evidence_id | entity_level | entity_id | field_name | coded_value | coding_basis | evidence_source_type | evidence_locator | evidence_note | source_url | coder_id | coder_type | coder_confidence | adjudication_status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| E070_001 | PAPER | PAPER_KT070 | title | Denoising Programming Knowledge Tracing with a Code Graph-Based Tuning Adapter | AUTHOR_STATED | PUBLISHER_METADATA | Article Title | Published conference title | 10.1145/3690624.3709172 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E070_002 | PAPER | PAPER_KT070 | venue | KDD | AUTHOR_STATED | PUBLISHER_METADATA | Conference Header | ACM SIGKDD 2025 Conference Proceedings | 10.1145/3690624.3709172 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E070_003 | PAPER | PAPER_KT070 | kt_central_task | YES | AUTHOR_STATED | PAPER_FULLTEXT | Abstract & Sec. 1 | Sequential programming response prediction & denoising state tracing | 10.1145/3690624.3709172 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E070_004 | PAPER | PAPER_KT070 | G_criterion | YES | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3 & 4 | Cluster-aware GCN built on code graph adapter for programming KT | 10.1145/3690624.3709172 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E070_005 | PAPER | PAPER_KT070 | S_criterion | NO | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4.4 | Supervised denoising and navigation regularization loss only | 10.1145/3690624.3709172 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E070_006 | PAPER | PAPER_KT070 | corpus_tier | PRIMARY_CORE | REVIEWER_INFERRED | PAPER_FULLTEXT | Protocol Sec. 4 | Primary core: satisfies G-criterion | Scope v1.0 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E070_007 | PAPER | PAPER_KT070 | coding_completeness | FULLTEXT_CODED | REVIEWER_INFERRED | PAPER_FULLTEXT | Full Text | Peer-reviewed ACM conference text fully inspected | 10.1145/3690624.3709172 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E070_008 | MODEL | MODEL_KT070_Coda | graph_source | AST_CODE_GRAPH, SIMILARITY, CLUSTER_GRAPH | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.1 | Cluster-aware code graph constructed from programming submissions and AST syntax structures | 10.1145/3690624.3709172 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E070_009 | MODEL | MODEL_KT070_Coda | gnn_encoder | GRAPH_CONVOLUTIONAL_NETWORK | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.2 | Cluster-aware Graph Convolutional Network encoder | 10.1145/3690624.3709172 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E070_010 | MODEL | MODEL_KT070_Coda | temporal_backbone | RNN_LSTM_GRU | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.3 | Plug-and-play adapter tuning backbone for sequential PKT models | 10.1145/3690624.3709172 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E070_011 | MODEL | MODEL_KT070_Coda | ssl_family | NONE | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4.4 | Supervised denoising and navigation regularization loss only | 10.1145/3690624.3709172 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E070_012 | EXPERIMENT | EXP_KT070_MAIN | datasets | CodeNet, OJ, Python-Tuples | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 5.1 | Evaluated on 3 public programming educational datasets | 10.1145/3690624.3709172 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
