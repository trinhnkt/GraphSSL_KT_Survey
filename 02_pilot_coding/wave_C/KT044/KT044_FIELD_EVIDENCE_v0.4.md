# KT044 Field-Level Evidence Table (v0.4 PILOT)

This document contains the long-form field-level evidence records for paper **KT044 (SINKT)**, satisfying the schema required in Section 2 of `coding_codebook_v0.4_PILOT.md`.

## Schema
`evidence_id` | `entity_level` | `entity_id` | `field_name` | `coded_value` | `coding_basis` | `evidence_source_type` | `evidence_locator` | `evidence_note` | `source_url` | `coder_id` | `coder_type` | `coder_confidence` | `adjudication_status`

---

## Evidence Records

| evidence_id | entity_level | entity_id | field_name | coded_value | coding_basis | evidence_source_type | evidence_locator | evidence_note | source_url | coder_id | coder_type | coder_confidence | adjudication_status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| E044_001 | PAPER | PAPER_KT044 | title | SINKT: A Structure-Aware Inductive Knowledge Tracing Model with Large Language Model | AUTHOR_STATED | PUBLISHER_METADATA | Title | Official published ACM conference title | 10.1145/3627673.3679760 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E044_002 | PAPER | PAPER_KT044 | venue | CIKM | AUTHOR_STATED | PUBLISHER_METADATA | Conference Header | ACM CIKM 2024 Conference Proceedings | 10.1145/3627673.3679760 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E044_003 | PAPER | PAPER_KT044 | kt_central_task | YES | AUTHOR_STATED | PAPER_FULLTEXT | Abstract & Sec. 1 | Sequential learner state estimation & inductive response prediction | 10.1145/3627673.3679760 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E044_004 | PAPER | PAPER_KT044 | G_criterion | YES | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3 & 4 | Heterogeneous concept-question graph constructed with LLM semantic relation extraction & GNN layers | 10.1145/3627673.3679760 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E044_005 | PAPER | PAPER_KT044 | S_criterion | NO | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4.4 | Supervised prediction loss only; LLM used as semantic structure extractor, no SSL pretext loss | 10.1145/3627673.3679760 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E044_006 | PAPER | PAPER_KT044 | corpus_tier | PRIMARY_CORE | REVIEWER_INFERRED | PAPER_FULLTEXT | Protocol Sec. 4 | Primary core: satisfies G-criterion | Scope v1.0 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E044_007 | PAPER | PAPER_KT044 | coding_completeness | FULLTEXT_CODED | REVIEWER_INFERRED | PAPER_FULLTEXT | Full Text | Peer-reviewed CIKM 2024 proceedings paper full text thoroughly inspected | 10.1145/3627673.3679760 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E044_008 | MODEL | MODEL_KT044_SINKT | graph_source | LLM_ASSISTED, SEMANTIC_TEXT, Q_MATRIX | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.1 & 3.2 | LLM extracts semantic dependencies & question-concept associations from text descriptions | 10.1145/3627673.3679760 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E044_009 | MODEL | MODEL_KT044_SINKT | graph_provenance | JOINTLY_LEARNED_TRAINING | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.2 | LLM structural embeddings combined with trainable GNN attention layers | 10.1145/3627673.3679760 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E044_010 | MODEL | MODEL_KT044_SINKT | graph_leakage_risk | LOW | REVIEWER_INFERRED | PAPER_FULLTEXT | Sec. 3.2 & Protocol Sec. 7 | Target unseen KCs/questions rely strictly on text semantic descriptions; zero interaction history leakage | Codebook v0.4 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E044_011 | MODEL | MODEL_KT044_SINKT | graph_representation | HETEROGENEOUS_MULTI_NODE, KC_KC | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.1 | Heterogeneous question-concept graph with LLM-guided concept dependencies | 10.1145/3627673.3679760 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E044_012 | MODEL | MODEL_KT044_SINKT | directed | Y | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.1 | Directed structural concept dependency edges derived by LLM | 10.1145/3627673.3679760 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E044_013 | MODEL | MODEL_KT044_SINKT | typed_edges | Y | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.1 | Heterogeneous edge categories (concept-concept dependencies vs question-concept mappings) | 10.1145/3627673.3679760 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E044_014 | MODEL | MODEL_KT044_SINKT | gnn_encoder | HETEROGENEOUS_GNN | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.3 | Heterogeneous Graph Attention Network (GAT) layers for structure-aware embedding | 10.1145/3627673.3679760 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E044_015 | MODEL | MODEL_KT044_SINKT | temporal_backbone | SELF_ATTENTION_TRANSFORMER | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.4 | Transformer backbone tracks learner interactions over time (LLM serves as semantic feature provider) | 10.1145/3627673.3679760 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E044_016 | MODEL | MODEL_KT044_SINKT | ssl_family | NONE | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4.4 | Supervised prediction loss only | 10.1145/3627673.3679760 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E044_017 | EXPERIMENT | EXP_KT044_MAIN | datasets | ASSISTments2009, ASSISTments2012, Junyi | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4.1 | Evaluated on public benchmark educational datasets in inductive cold-start setups | 10.1145/3627673.3679760 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E044_018 | EXPERIMENT | EXP_KT044_MAIN | n_seeds | 5 | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4.1 | Performance averaged over 5 random seeds | 10.1145/3627673.3679760 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E044_019 | EXPERIMENT | EXP_KT044_MAIN | resampling_repeats | 1 | REVIEWER_INFERRED | PAPER_FULLTEXT | Sec. 4.1 | Single random data split repeated across model seeds | Codebook v0.4 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E044_020 | EXPERIMENT | EXP_KT044_MAIN | repeated_run_unit | SEED_REPETITION | REVIEWER_INFERRED | PAPER_FULLTEXT | Sec. 4.1 | Seed repetition unit (CB13) | Codebook v0.4 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E044_021 | EXPERIMENT | EXP_KT044_MAIN | sparse_concept_ontology | STRICT_KC_COLD_START | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 1 & 4.3 | Evaluates inductive zero-exposure KC/question cold-start setting with zero training interaction history | 10.1145/3627673.3679760 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
