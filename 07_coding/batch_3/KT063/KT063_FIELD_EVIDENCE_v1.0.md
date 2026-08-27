# KT063 Field-Level Evidence Table (v1.0 LOCKED)

This document contains the long-form field-level evidence records for paper **KT063 (MAHKT)**, satisfying the schema required in `coding_codebook_v1.0_LOCKED.md`.

## Schema
`evidence_id` | `entity_level` | `entity_id` | `field_name` | `coded_value` | `coding_basis` | `evidence_source_type` | `evidence_locator` | `evidence_note` | `source_url` | `coder_id` | `coder_type` | `coder_confidence` | `adjudication_status`

---

## Evidence Records

| evidence_id | entity_level | entity_id | field_name | coded_value | coding_basis | evidence_source_type | evidence_locator | evidence_note | source_url | coder_id | coder_type | coder_confidence | adjudication_status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| E063_001 | PAPER | PAPER_KT063 | title | MAHKT: Knowledge Tracing with Multi-Association Heterogeneous Graph Embedding Based on Knowledge Transfer | AUTHOR_STATED | PUBLISHER_METADATA | Article Title | Published journal title | 10.1016/j.knosys.2025.112958 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E063_002 | PAPER | PAPER_KT063 | venue | Knowledge-Based Systems | AUTHOR_STATED | PUBLISHER_METADATA | Journal Header | KBS Vol. 310, Article 112958, 2025 | 10.1016/j.knosys.2025.112958 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E063_003 | PAPER | PAPER_KT063 | kt_central_task | YES | AUTHOR_STATED | PAPER_FULLTEXT | Abstract & Sec. 1 | Sequential student performance prediction & knowledge transfer modeling | 10.1016/j.knosys.2025.112958 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E063_004 | PAPER | PAPER_KT063 | G_criterion | YES | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3 & 4 | Multi-association heterogeneous graph embedding with knowledge transfer GNN | 10.1016/j.knosys.2025.112958 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E063_005 | PAPER | PAPER_KT063 | S_criterion | NO | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4.4 | Supervised prediction loss only | 10.1016/j.knosys.2025.112958 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E063_006 | PAPER | PAPER_KT063 | corpus_tier | PRIMARY_CORE | REVIEWER_INFERRED | PAPER_FULLTEXT | Protocol Sec. 4 | Primary core: satisfies G-criterion | Scope v1.0 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E063_007 | PAPER | PAPER_KT063 | coding_completeness | FULLTEXT_CODED | REVIEWER_INFERRED | PAPER_FULLTEXT | Full Text | Peer-reviewed journal text fully inspected | 10.1016/j.knosys.2025.112958 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E063_008 | MODEL | MODEL_KT063_MAHKT | graph_source | Q_MATRIX, CURRICULUM_CONCEPT_MAP, CO_OCCURRENCE | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.1 | Multi-association heterogeneous graph connecting concepts, exercises, and knowledge transfer links | 10.1016/j.knosys.2025.112958 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E063_009 | MODEL | MODEL_KT063_MAHKT | gnn_encoder | HETEROGENEOUS_GNN | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.2 | Multi-Association Heterogeneous Graph Neural Network encoder | 10.1016/j.knosys.2025.112958 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E063_010 | MODEL | MODEL_KT063_MAHKT | temporal_backbone | RNN_LSTM_GRU | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.3 | GRU sequence backbone for temporal state tracking | 10.1016/j.knosys.2025.112958 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E063_011 | MODEL | MODEL_KT063_MAHKT | ssl_family | NONE | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4.4 | Supervised prediction loss only | 10.1016/j.knosys.2025.112958 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E063_012 | EXPERIMENT | EXP_KT063_MAIN | datasets | ASSISTments2009, ASSISTments2017, Statics2011 | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 5.1 | Evaluated on 3 public benchmark educational datasets | 10.1016/j.knosys.2025.112958 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
