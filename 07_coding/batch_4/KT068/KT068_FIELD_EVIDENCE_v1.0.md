# KT068 Field-Level Evidence Table (v1.0 LOCKED)

This document contains the long-form field-level evidence records for paper **KT068 (HKT)**, satisfying the schema required in `coding_codebook_v1.0_LOCKED.md`.

## Schema
`evidence_id` | `entity_level` | `entity_id` | `field_name` | `coded_value` | `coding_basis` | `evidence_source_type` | `evidence_locator` | `evidence_note` | `source_url` | `coder_id` | `coder_type` | `coder_confidence` | `adjudication_status`

---

## Evidence Records

| evidence_id | entity_level | entity_id | field_name | coded_value | coding_basis | evidence_source_type | evidence_locator | evidence_note | source_url | coder_id | coder_type | coder_confidence | adjudication_status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| E068_001 | PAPER | PAPER_KT068 | title | HKT: Hierarchical Structure-Based Knowledge Tracing | AUTHOR_STATED | PUBLISHER_METADATA | Article Title | Published journal title | 10.1016/j.ipm.2025.104206 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E068_002 | PAPER | PAPER_KT068 | venue | Information Processing & Management | AUTHOR_STATED | PUBLISHER_METADATA | Journal Header | IP&M Vol. 62, Issue 5, Article 104206, 2025 | 10.1016/j.ipm.2025.104206 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E068_003 | PAPER | PAPER_KT068 | kt_central_task | YES | AUTHOR_STATED | PAPER_FULLTEXT | Abstract & Sec. 1 | Sequential learner response prediction & hierarchical knowledge state tracking | 10.1016/j.ipm.2025.104206 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E068_004 | PAPER | PAPER_KT068 | G_criterion | YES | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3 & 4 | Hierarchical structure-based graph neural network over domain concepts | 10.1016/j.ipm.2025.104206 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E068_005 | PAPER | PAPER_KT068 | S_criterion | YES | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4.4 | Hierarchical cross-graph contrastive learning pretext task | 10.1016/j.ipm.2025.104206 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E068_006 | PAPER | PAPER_KT068 | corpus_tier | PRIMARY_CORE | REVIEWER_INFERRED | PAPER_FULLTEXT | Protocol Sec. 4 | Primary core: satisfies G-criterion and S-criterion | Scope v1.0 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E068_007 | PAPER | PAPER_KT068 | coding_completeness | FULLTEXT_CODED | REVIEWER_INFERRED | PAPER_FULLTEXT | Full Text | Peer-reviewed journal text fully inspected | 10.1016/j.ipm.2025.104206 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E068_008 | MODEL | MODEL_KT068_HKT | graph_source | CURRICULUM_CONCEPT_MAP, Q_MATRIX | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.1 | Hierarchical concept graph constructed from domain structure and Q-matrix | 10.1016/j.ipm.2025.104206 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E068_009 | MODEL | MODEL_KT068_HKT | gnn_encoder | HETEROGENEOUS_GNN | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.2 | Hierarchical Graph Neural Network encoder | 10.1016/j.ipm.2025.104206 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E068_010 | MODEL | MODEL_KT068_HKT | temporal_backbone | SELF_ATTENTION_TRANSFORMER | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.3 | Attentive Transformer backbone for sequence tracing | 10.1016/j.ipm.2025.104206 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E068_011 | MODEL | MODEL_KT068_HKT | ssl_family | HIERARCHICAL_CONTRASTIVE, GRAPH_CONTRASTIVE | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4.4 | Cross-graph hierarchical contrastive loss across abstraction levels | 10.1016/j.ipm.2025.104206 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E068_012 | EXPERIMENT | EXP_KT068_MAIN | datasets | ASSISTments2009, ASSISTments2017, EdNet | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 5.1 | Evaluated on 3 public benchmark educational datasets | 10.1016/j.ipm.2025.104206 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
