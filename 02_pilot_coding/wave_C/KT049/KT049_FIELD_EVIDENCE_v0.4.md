# KT049 Field-Level Evidence Table (v0.4 PILOT)

This document contains the long-form field-level evidence records for paper **KT049**, satisfying the schema required in Section 2 of `coding_codebook_v0.4_PILOT.md`.

## Schema
`evidence_id` | `entity_level` | `entity_id` | `field_name` | `coded_value` | `coding_basis` | `evidence_source_type` | `evidence_locator` | `evidence_note` | `source_url` | `coder_id` | `coder_type` | `coder_confidence` | `adjudication_status`

---

## Evidence Records

| evidence_id | entity_level | entity_id | field_name | coded_value | coding_basis | evidence_source_type | evidence_locator | evidence_note | source_url | coder_id | coder_type | coder_confidence | adjudication_status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| E049_001 | PAPER | PAPER_KT049 | title | Mitigating Cold-Start Problems in Knowledge Tracing with Large Language Models: An Attribute-Aware Approach | AUTHOR_STATED | PUBLISHER_METADATA | Title | Official published ACM conference title | 10.1145/3627673.3679664 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E049_002 | PAPER | PAPER_KT049 | venue | CIKM | AUTHOR_STATED | PUBLISHER_METADATA | Conference Header | ACM CIKM 2024 Conference Proceedings | 10.1145/3627673.3679664 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E049_003 | PAPER | PAPER_KT049 | kt_central_task | YES | AUTHOR_STATED | PAPER_FULLTEXT | Abstract & Sec. 1 | Sequential learner performance prediction under cold-start conditions | 10.1145/3627673.3679664 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E049_004 | PAPER | PAPER_KT049 | G_criterion | NO | REVIEWER_INFERRED | PAPER_FULLTEXT | Sec. 3 & 4 | Uses LLM text attribute embeddings directly in sequence tracing without explicit graph topology or GNN encoder | 10.1145/3627673.3679664 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E049_005 | PAPER | PAPER_KT049 | S_criterion | NO | REVIEWER_INFERRED | PAPER_FULLTEXT | Sec. 4.4 | Supervised prediction loss only; no self-supervised pretext task loss | 10.1145/3627673.3679664 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E049_006 | PAPER | PAPER_KT049 | corpus_tier | PRIMARY_ADJACENT_SPARSE | REVIEWER_INFERRED | PAPER_FULLTEXT | Protocol Sec. 4 | Primary adjacent sparse case: addresses RQ4 cold-start lens without satisfying G-criterion or S-criterion | Scope v1.0 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E049_007 | PAPER | PAPER_KT049 | coding_completeness | FULLTEXT_CODED | REVIEWER_INFERRED | PAPER_FULLTEXT | Full Text | Peer-reviewed CIKM 2024 proceedings paper full text thoroughly inspected | 10.1145/3627673.3679664 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E049_008 | MODEL | MODEL_KT049_LLM_ATTRIB | graph_source | NONE | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.1 | Direct LLM question attribute text encoding without graph construction | 10.1145/3627673.3679664 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E049_009 | MODEL | MODEL_KT049_LLM_ATTRIB | graph_representation | NONE | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.1 | Text attribute embeddings without graph topological edges | 10.1145/3627673.3679664 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E049_010 | MODEL | MODEL_KT049_LLM_ATTRIB | gnn_encoder | NONE | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.2 | No GNN message passing | 10.1145/3627673.3679664 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E049_011 | MODEL | MODEL_KT049_LLM_ATTRIB | temporal_backbone | RNN_LSTM_GRU | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.3 | Deep sequence backbone for learner state tracking | 10.1145/3627673.3679664 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E049_012 | MODEL | MODEL_KT049_LLM_ATTRIB | ssl_family | NONE | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4.4 | Supervised prediction loss only | 10.1145/3627673.3679664 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E049_013 | EXPERIMENT | EXP_KT049_MAIN | datasets | ASSISTments2009, ASSISTments2012, EPub | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4.1 | Real-world benchmark educational datasets evaluated in cold-start settings | 10.1145/3627673.3679664 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E049_014 | EXPERIMENT | EXP_KT049_MAIN | sparse_concept_ontology | ITEM_COLD_START, STRICT_KC_COLD_START | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 1 & 4.3 | Evaluates zero-exposure item and KC cold-start scenarios using LLM textual attributes | 10.1145/3627673.3679664 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
