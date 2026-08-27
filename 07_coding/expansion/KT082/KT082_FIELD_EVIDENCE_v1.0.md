# KT082 Field-Level Evidence Table (v1.0 LOCKED)

This document contains the long-form field-level evidence records for paper **KT082 (GMGAE)**, satisfying the schema required in `coding_codebook_v1.0_LOCKED.md`.

## Schema
`evidence_id` | `entity_level` | `entity_id` | `field_name` | `coded_value` | `coding_basis` | `evidence_source_type` | `evidence_locator` | `evidence_note` | `source_url` | `coder_id` | `coder_type` | `coder_confidence` | `adjudication_status`

---

## Evidence Records

| evidence_id | entity_level | entity_id | field_name | coded_value | coding_basis | evidence_source_type | evidence_locator | evidence_note | source_url | coder_id | coder_type | coder_confidence | adjudication_status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| E082_001 | PAPER | PAPER_KT082 | title | Generative Masked Graph Auto-Encoder for Knowledge Tracing | AUTHOR_STATED | PUBLISHER_METADATA | Article Title | Published conference title | 10.1145/3627673.3679900 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E082_002 | PAPER | PAPER_KT082 | venue | CIKM | AUTHOR_STATED | PUBLISHER_METADATA | Conference Header | ACM CIKM 2025 Proceedings | 10.1145/3627673.3679900 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E082_003 | PAPER | PAPER_KT082 | kt_central_task | YES | AUTHOR_STATED | PAPER_FULLTEXT | Abstract & Sec. 1 | Sequential learner response prediction & generative masked graph pre-training | 10.1145/3627673.3679900 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E082_004 | PAPER | PAPER_KT082 | G_criterion | YES | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3 & 4 | Generative masked graph auto-encoder GNN for concept structure modeling | 10.1145/3627673.3679900 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E082_005 | PAPER | PAPER_KT082 | S_criterion | YES | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4.4 | Generative masked graph pre-training pretext task | 10.1145/3627673.3679900 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E082_006 | PAPER | PAPER_KT082 | corpus_tier | PRIMARY_CORE | REVIEWER_INFERRED | PAPER_FULLTEXT | Protocol Sec. 4 | Primary core: satisfies G-criterion and S-criterion | Scope v1.0 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E082_007 | PAPER | PAPER_KT082 | coding_completeness | FULLTEXT_CODED | REVIEWER_INFERRED | PAPER_FULLTEXT | Full Text | Peer-reviewed ACM conference text fully inspected | 10.1145/3627673.3679900 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E082_008 | MODEL | MODEL_KT082_GMGAE | graph_source | Q_MATRIX, CURRICULUM_CONCEPT_MAP | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.1 | Concept interaction graph pre-trained via generative masked auto-encoding | 10.1145/3627673.3679900 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E082_009 | MODEL | MODEL_KT082_GMGAE | gnn_encoder | GRAPH_AUTOENCODER | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.2 | Generative Masked Graph Auto-Encoder (GAE) GNN encoder | 10.1145/3627673.3679900 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E082_010 | MODEL | MODEL_KT082_GMGAE | temporal_backbone | SELF_ATTENTION_TRANSFORMER | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.3 | Transformer backbone fine-tuned for sequence response tracing | 10.1145/3627673.3679900 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E082_011 | MODEL | MODEL_KT082_GMGAE | ssl_family | MASKED_PRETRAINING, GENERATIVE_RECONSTRUCTION | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4.4 | Generative masked graph node/edge reconstruction pretext task | 10.1145/3627673.3679900 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E082_012 | EXPERIMENT | EXP_KT082_MAIN | datasets | ASSISTments2009, ASSISTments2017, EdNet, Statics2011 | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 5.1 | Evaluated on 4 public benchmark educational datasets | 10.1145/3627673.3679900 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
