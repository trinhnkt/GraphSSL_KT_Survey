# KT041 Field-Level Evidence Table (v0.4 PILOT)

This document contains the long-form field-level evidence records for paper **KT041**, satisfying the schema required in Section 2 of `coding_codebook_v0.4_PILOT.md`.

## Schema
`evidence_id` | `entity_level` | `entity_id` | `field_name` | `coded_value` | `coding_basis` | `evidence_source_type` | `evidence_locator` | `evidence_note` | `source_url` | `coder_id` | `coder_type` | `coder_confidence` | `adjudication_status`

---

## Evidence Records

| evidence_id | entity_level | entity_id | field_name | coded_value | coding_basis | evidence_source_type | evidence_locator | evidence_note | source_url | coder_id | coder_type | coder_confidence | adjudication_status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| E041_001 | PAPER | PAPER_KT041 | title | Towards Robust Knowledge Tracing Models via k-Sparse Attention | AUTHOR_STATED | PUBLISHER_METADATA | Title | Official published ACM conference title | 10.1145/3539618.3592073 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E041_002 | PAPER | PAPER_KT041 | venue | SIGIR | AUTHOR_STATED | PUBLISHER_METADATA | Conference Header | ACM SIGIR 2023 Conference Proceedings | 10.1145/3539618.3592073 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E041_003 | PAPER | PAPER_KT041 | kt_central_task | YES | AUTHOR_STATED | PAPER_FULLTEXT | Abstract & Sec. 1 | Sequential learner response prediction & robust knowledge tracing | 10.1145/3539618.3592073 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E041_004 | PAPER | PAPER_KT041 | G_criterion | NO | REVIEWER_INFERRED | PAPER_FULLTEXT | Sec. 3 & 4 | Uses k-sparse attention softmax in Transformer sequence model; no graph construction or GNN encoder | 10.1145/3539618.3592073 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E041_005 | PAPER | PAPER_KT041 | S_criterion | NO | REVIEWER_INFERRED | PAPER_FULLTEXT | Sec. 4.4 | Supervised prediction loss only; no self-supervised pretext task loss | 10.1145/3539618.3592073 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E041_006 | PAPER | PAPER_KT041 | corpus_tier | BACKGROUND | REVIEWER_INFERRED | PAPER_FULLTEXT | Protocol Sec. 4 | Term ambiguity boundary case: k-sparse attention is an architectural sparsity mechanism, NOT sparse-concept KC educational evidence | Scope v1.0 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E041_007 | PAPER | PAPER_KT041 | coding_completeness | FULLTEXT_CODED | REVIEWER_INFERRED | PAPER_FULLTEXT | Full Text | Peer-reviewed SIGIR 2023 full text thoroughly inspected | 10.1145/3539618.3592073 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E041_008 | MODEL | MODEL_KT041_KSPARSE_ATTN | graph_source | NONE | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.1 | No graph structure used | 10.1145/3539618.3592073 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E041_009 | MODEL | MODEL_KT041_KSPARSE_ATTN | gnn_encoder | NONE | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.2 | No GNN encoder | 10.1145/3539618.3592073 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E041_010 | MODEL | MODEL_KT041_KSPARSE_ATTN | temporal_backbone | SELF_ATTENTION_TRANSFORMER | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.3 | Transformer backbone with k-sparse attention mechanism | 10.1145/3539618.3592073 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E041_011 | MODEL | MODEL_KT041_KSPARSE_ATTN | ssl_family | NONE | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4.4 | Supervised prediction loss only | 10.1145/3539618.3592073 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E041_012 | EXPERIMENT | EXP_KT041_MAIN | sparse_concept_ontology | SPARSE_ATTENTION_ARCHITECTURE | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 1 & 4.3 | Architectural k-sparse attention truncation; NOT sparse-concept KC educational data evaluation | 10.1145/3539618.3592073 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
