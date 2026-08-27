# KT062 Field-Level Evidence Table (v1.0 LOCKED)

This document contains the long-form field-level evidence records for paper **KT062 (LGS-KT)**, satisfying the schema required in `coding_codebook_v1.0_LOCKED.md`.

## Schema
`evidence_id` | `entity_level` | `entity_id` | `field_name` | `coded_value` | `coding_basis` | `evidence_source_type` | `evidence_locator` | `evidence_note` | `source_url` | `coder_id` | `coder_type` | `coder_confidence` | `adjudication_status`

---

## Evidence Records

| evidence_id | entity_level | entity_id | field_name | coded_value | coding_basis | evidence_source_type | evidence_locator | evidence_note | source_url | coder_id | coder_type | coder_confidence | adjudication_status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| E062_001 | PAPER | PAPER_KT062 | title | LGS-KT: Integrating Logical and Grammatical Skills for Effective Programming Knowledge Tracing | AUTHOR_STATED | PUBLISHER_METADATA | Article Title | Published journal title | 10.1016/j.neunet.2025.107164 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E062_002 | PAPER | PAPER_KT062 | venue | Neural Networks | AUTHOR_STATED | PUBLISHER_METADATA | Journal Header | Neural Networks Vol. 185, Article 107164, 2025 | 10.1016/j.neunet.2025.107164 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E062_003 | PAPER | PAPER_KT062 | kt_central_task | YES | AUTHOR_STATED | PAPER_FULLTEXT | Abstract & Sec. 1 | Sequential programming learner response prediction & skill state tracing | 10.1016/j.neunet.2025.107164 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E062_004 | PAPER | PAPER_KT062 | G_criterion | YES | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3 & 4 | Constructs knowledge-concept similarity & AST code graph for logical/grammatical skills | 10.1016/j.neunet.2025.107164 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E062_005 | PAPER | PAPER_KT062 | S_criterion | NO | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4.4 | Supervised prediction loss only | 10.1016/j.neunet.2025.107164 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E062_006 | PAPER | PAPER_KT062 | corpus_tier | PRIMARY_CORE | REVIEWER_INFERRED | PAPER_FULLTEXT | Protocol Sec. 4 | Primary core: satisfies G-criterion | Scope v1.0 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E062_007 | PAPER | PAPER_KT062 | coding_completeness | FULLTEXT_CODED | REVIEWER_INFERRED | PAPER_FULLTEXT | Full Text | Peer-reviewed journal text fully inspected | 10.1016/j.neunet.2025.107164 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E062_008 | MODEL | MODEL_KT062_LGS_KT | graph_source | AST_CODE_GRAPH, SIMILARITY, Q_MATRIX | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.1 | Code AST graph combined with concept similarity matrix for logical & grammatical skills | 10.1016/j.neunet.2025.107164 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E062_009 | MODEL | MODEL_KT062_LGS_KT | gnn_encoder | GRAPH_CONVOLUTIONAL_NETWORK | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.2 | Graph Convolutional Network encoder over AST code graphs | 10.1016/j.neunet.2025.107164 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E062_010 | MODEL | MODEL_KT062_LGS_KT | temporal_backbone | RNN_LSTM_GRU | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.3 | GRU sequence layer for temporal programming state tracing | 10.1016/j.neunet.2025.107164 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E062_011 | MODEL | MODEL_KT062_LGS_KT | ssl_family | NONE | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4.4 | Supervised prediction loss only | 10.1016/j.neunet.2025.107164 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E062_012 | EXPERIMENT | EXP_KT062_MAIN | datasets | CodeNet, OJ, Python-Tuples | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 5.1 | Evaluated on 3 public programming educational datasets | 10.1016/j.neunet.2025.107164 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
