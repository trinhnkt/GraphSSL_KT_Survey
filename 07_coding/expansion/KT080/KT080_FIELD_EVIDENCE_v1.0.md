# KT080 Field-Level Evidence Table (v1.0 LOCKED)

This document contains the long-form field-level evidence records for paper **KT080 (DGR-KT)**, satisfying the schema required in `coding_codebook_v1.0_LOCKED.md`.

## Schema
`evidence_id` | `entity_level` | `entity_id` | `field_name` | `coded_value` | `coding_basis` | `evidence_source_type` | `evidence_locator` | `evidence_note` | `source_url` | `coder_id` | `coder_type` | `coder_confidence` | `adjudication_status`

---

## Evidence Records

| evidence_id | entity_level | entity_id | field_name | coded_value | coding_basis | evidence_source_type | evidence_locator | evidence_note | source_url | coder_id | coder_type | coder_confidence | adjudication_status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| E080_001 | PAPER | PAPER_KT080 | title | Debiased Graph Representation Learning for Attentive Knowledge Tracing | AUTHOR_STATED | PUBLISHER_METADATA | Article Title | Published conference title | 10.1145/3690624.3709500 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E080_002 | PAPER | PAPER_KT080 | venue | KDD | AUTHOR_STATED | PUBLISHER_METADATA | Conference Header | ACM SIGKDD 2025 Proceedings | 10.1145/3690624.3709500 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E080_003 | PAPER | PAPER_KT080 | kt_central_task | YES | AUTHOR_STATED | PAPER_FULLTEXT | Abstract & Sec. 1 | Sequential response prediction & debiased graph representation learning | 10.1145/3690624.3709500 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E080_004 | PAPER | PAPER_KT080 | G_criterion | YES | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3 & 4 | Causal debiased graph representation learning GCN for attentive KT | 10.1145/3690624.3709500 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E080_005 | PAPER | PAPER_KT080 | S_criterion | NO | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4.4 | Supervised prediction loss with causal debiasing intervention objective | 10.1145/3690624.3709500 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E080_006 | PAPER | PAPER_KT080 | corpus_tier | PRIMARY_CORE | REVIEWER_INFERRED | PAPER_FULLTEXT | Protocol Sec. 4 | Primary core: satisfies G-criterion | Scope v1.0 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E080_007 | PAPER | PAPER_KT080 | coding_completeness | FULLTEXT_CODED | REVIEWER_INFERRED | PAPER_FULLTEXT | Full Text | Peer-reviewed ACM conference text fully inspected | 10.1145/3690624.3709500 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E080_008 | MODEL | MODEL_KT080_DGR_KT | graph_source | Q_MATRIX, CONCEPT_SIMILARITY_GRAPH | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.1 | Causal graph constructed from concept similarity and interaction bias features | 10.1145/3690624.3709500 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E080_009 | MODEL | MODEL_KT080_DGR_KT | gnn_encoder | GRAPH_CONVOLUTIONAL_NETWORK | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.2 | Causal Graph Convolutional Network encoder | 10.1145/3690624.3709500 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E080_010 | MODEL | MODEL_KT080_DGR_KT | temporal_backbone | SELF_ATTENTION_TRANSFORMER | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.3 | Attentive Transformer backbone for sequence tracing | 10.1145/3690624.3709500 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E080_011 | MODEL | MODEL_KT080_DGR_KT | ssl_family | NONE | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4.4 | Supervised prediction and causal debiasing intervention loss only | 10.1145/3690624.3709500 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E080_012 | EXPERIMENT | EXP_KT080_MAIN | datasets | ASSISTments2009, ASSISTments2017, EdNet, Junyi | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 5.1 | Evaluated on 4 public benchmark educational datasets | 10.1145/3690624.3709500 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
