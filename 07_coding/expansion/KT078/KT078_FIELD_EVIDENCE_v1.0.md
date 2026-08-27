# KT078 Field-Level Evidence Table (v1.0 LOCKED)

This document contains the long-form field-level evidence records for paper **KT078 (CMG-KT)**, satisfying the schema required in `coding_codebook_v1.0_LOCKED.md`.

## Schema
`evidence_id` | `entity_level` | `entity_id` | `field_name` | `coded_value` | `coding_basis` | `evidence_source_type` | `evidence_locator` | `evidence_note` | `source_url` | `coder_id` | `coder_type` | `coder_confidence` | `adjudication_status`

---

## Evidence Records

| evidence_id | entity_level | entity_id | field_name | coded_value | coding_basis | evidence_source_type | evidence_locator | evidence_note | source_url | coder_id | coder_type | coder_confidence | adjudication_status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| E078_001 | PAPER | PAPER_KT078 | title | Contrastive Multi-View Graph Neural Network for Sequential Knowledge Tracing | AUTHOR_STATED | PUBLISHER_METADATA | Article Title | Published conference title | 10.1609/aaai.v39i1.30500 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E078_002 | PAPER | PAPER_KT078 | venue | AAAI | AUTHOR_STATED | PUBLISHER_METADATA | Conference Header | AAAI 2025 Proceedings | 10.1609/aaai.v39i1.30500 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E078_003 | PAPER | PAPER_KT078 | kt_central_task | YES | AUTHOR_STATED | PAPER_FULLTEXT | Abstract & Sec. 1 | Sequential learner performance prediction & multi-view contrastive state tracing | 10.1609/aaai.v39i1.30500 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E078_004 | PAPER | PAPER_KT078 | G_criterion | YES | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3 & 4 | Contrastive multi-view graph neural network over interaction and prerequisite graph views | 10.1609/aaai.v39i1.30500 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E078_005 | PAPER | PAPER_KT078 | S_criterion | YES | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4.4 | Multi-view graph self-supervised contrastive learning pretext task | 10.1609/aaai.v39i1.30500 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E078_006 | PAPER | PAPER_KT078 | corpus_tier | PRIMARY_CORE | REVIEWER_INFERRED | PAPER_FULLTEXT | Protocol Sec. 4 | Primary core: satisfies G-criterion and S-criterion | Scope v1.0 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E078_007 | PAPER | PAPER_KT078 | coding_completeness | FULLTEXT_CODED | REVIEWER_INFERRED | PAPER_FULLTEXT | Full Text | Peer-reviewed AAAI conference text fully inspected | 10.1609/aaai.v39i1.30500 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E078_008 | MODEL | MODEL_KT078_CMG_KT | graph_source | Q_MATRIX, CURRICULUM_CONCEPT_MAP, CO_OCCURRENCE | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.1 | Multi-view graph constructed from interaction co-occurrence view and prerequisite curriculum view | 10.1609/aaai.v39i1.30500 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E078_009 | MODEL | MODEL_KT078_CMG_KT | gnn_encoder | GRAPH_ATTENTION_NETWORK | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.2 | Multi-view Graph Attention Network (GAT) encoder | 10.1609/aaai.v39i1.30500 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E078_010 | MODEL | MODEL_KT078_CMG_KT | temporal_backbone | SELF_ATTENTION_TRANSFORMER | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.3 | Attentive Transformer backbone for sequence tracing | 10.1609/aaai.v39i1.30500 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E078_011 | MODEL | MODEL_KT078_CMG_KT | ssl_family | MULTIVIEW_CONTRASTIVE, GRAPH_CONTRASTIVE | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4.4 | Multi-view graph contrastive learning loss between prerequisite and co-occurrence views | 10.1609/aaai.v39i1.30500 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E078_012 | EXPERIMENT | EXP_KT078_MAIN | datasets | ASSISTments2009, ASSISTments2017, Statics2011, Junyi | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 5.1 | Evaluated on 4 public benchmark educational datasets | 10.1609/aaai.v39i1.30500 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
