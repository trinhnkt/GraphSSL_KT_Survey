# KT056 Field-Level Evidence Table (v1.0 LOCKED)

This document contains the long-form field-level evidence records for paper **KT056**, satisfying the schema required in `coding_codebook_v1.0_LOCKED.md`.

## Schema
`evidence_id` | `entity_level` | `entity_id` | `field_name` | `coded_value` | `coding_basis` | `evidence_source_type` | `evidence_locator` | `evidence_note` | `source_url` | `coder_id` | `coder_type` | `coder_confidence` | `adjudication_status`

---

## Evidence Records

| evidence_id | entity_level | entity_id | field_name | coded_value | coding_basis | evidence_source_type | evidence_locator | evidence_note | source_url | coder_id | coder_type | coder_confidence | adjudication_status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| E056_001 | PAPER | PAPER_KT056 | title | Exploring Long- and Short-Term Knowledge State Graph Representations with Adaptive Fusion for Knowledge Tracing | AUTHOR_STATED | PUBLISHER_METADATA | Article Title | Published journal title | 10.1016/j.ipm.2025.104074 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E056_002 | PAPER | PAPER_KT056 | venue | Information Processing & Management | AUTHOR_STATED | PUBLISHER_METADATA | Journal Header | IP&M Vol. 62, Issue 3, Article 104074, 2025 | 10.1016/j.ipm.2025.104074 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E056_003 | PAPER | PAPER_KT056 | kt_central_task | YES | AUTHOR_STATED | PAPER_FULLTEXT | Abstract & Sec. 1 | Sequential learner response prediction & multi-temporal state tracking | 10.1016/j.ipm.2025.104074 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E056_004 | PAPER | PAPER_KT056 | G_criterion | YES | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3 & 4 | Long- and short-term knowledge state graph representations with adaptive GNN fusion | 10.1016/j.ipm.2025.104074 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E056_005 | PAPER | PAPER_KT056 | S_criterion | NO | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4.4 | Supervised prediction loss only | 10.1016/j.ipm.2025.104074 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E056_006 | PAPER | PAPER_KT056 | corpus_tier | PRIMARY_CORE | REVIEWER_INFERRED | PAPER_FULLTEXT | Protocol Sec. 4 | Primary core: satisfies G-criterion | Scope v1.0 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E056_007 | PAPER | PAPER_KT056 | coding_completeness | FULLTEXT_CODED | REVIEWER_INFERRED | PAPER_FULLTEXT | Full Text | Peer-reviewed journal text fully inspected | 10.1016/j.ipm.2025.104074 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E056_008 | MODEL | MODEL_KT056_LST_GRAPH | graph_source | SEQUENTIAL_TRANSITION, LEARNED_FROM_INTERACTIONS | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.1 | Long-term and short-term state graphs derived from interaction sequence windows | 10.1016/j.ipm.2025.104074 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E056_009 | MODEL | MODEL_KT056_LST_GRAPH | gnn_encoder | GRAPH_ATTENTION_HYBRID | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.2 | Adaptive Graph Attention encoder for long/short-term graph fusion | 10.1016/j.ipm.2025.104074 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E056_010 | MODEL | MODEL_KT056_LST_GRAPH | temporal_backbone | RNN_LSTM_GRU | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.3 | GRU sequence backbone for temporal state tracking | 10.1016/j.ipm.2025.104074 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E056_011 | MODEL | MODEL_KT056_LST_GRAPH | ssl_family | NONE | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4.4 | Supervised prediction loss only | 10.1016/j.ipm.2025.104074 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E056_012 | EXPERIMENT | EXP_KT056_MAIN | datasets | ASSISTments2009, ASSISTments2017, EdNet | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 5.1 | Evaluated on 3 public benchmark educational datasets | 10.1016/j.ipm.2025.104074 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
