# KT038 Field-Level Evidence Table (v0.4 PILOT)

This document contains the long-form field-level evidence records for paper **KT038 (DyGKT)**, satisfying the schema required in Section 2 of `coding_codebook_v0.4_PILOT.md`.

## Schema
`evidence_id` | `entity_level` | `entity_id` | `field_name` | `coded_value` | `coding_basis` | `evidence_source_type` | `evidence_locator` | `evidence_note` | `source_url` | `coder_id` | `coder_type` | `coder_confidence` | `adjudication_status`

---

## Evidence Records

| evidence_id | entity_level | entity_id | field_name | coded_value | coding_basis | evidence_source_type | evidence_locator | evidence_note | source_url | coder_id | coder_type | coder_confidence | adjudication_status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| E038_001 | PAPER | PAPER_KT038 | title | DyGKT: Dynamic Graph Learning for Knowledge Tracing | AUTHOR_STATED | PUBLISHER_METADATA | Title | Official published ACM conference title | 10.1145/3637528.3671773 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E038_002 | PAPER | PAPER_KT038 | venue | KDD | AUTHOR_STATED | PUBLISHER_METADATA | Conference Header | ACM SIGKDD 2024 Conference Proceedings | 10.1145/3637528.3671773 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E038_003 | PAPER | PAPER_KT038 | kt_central_task | YES | AUTHOR_STATED | PAPER_FULLTEXT | Abstract & Sec. 1 | Sequential student response prediction over dynamic learning streams | 10.1145/3637528.3671773 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E038_004 | PAPER | PAPER_KT038 | G_criterion | YES | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3 & 4 | Continuous-time dynamic question-answering graph with dynamic GNN message passing | 10.1145/3637528.3671773 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E038_005 | PAPER | PAPER_KT038 | S_criterion | NO | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4.4 | Supervised prediction loss only; no SSL pretext objective | 10.1145/3637528.3671773 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E038_006 | PAPER | PAPER_KT038 | corpus_tier | PRIMARY_CORE | REVIEWER_INFERRED | PAPER_FULLTEXT | Protocol Sec. 4 | Primary core: satisfies G-criterion | Scope v1.0 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E038_007 | PAPER | PAPER_KT038 | coding_completeness | FULLTEXT_CODED | REVIEWER_INFERRED | PAPER_FULLTEXT | Full Text | Peer-reviewed KDD 2024 proceedings paper full text thoroughly inspected | 10.1145/3637528.3671773 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E038_008 | MODEL | MODEL_KT038_DyGKT | graph_source | LEARNED_FROM_INTERACTIONS, SEQUENTIAL_TRANSITION | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.1 | Continuous-time interaction stream constructing evolving question-answering graph | 10.1145/3637528.3671773 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E038_009 | MODEL | MODEL_KT038_DyGKT | graph_provenance | JOINTLY_LEARNED_TRAINING | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.2 | Continuous-time dynamic graph updated synchronously with student interaction events | 10.1145/3637528.3671773 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E038_010 | MODEL | MODEL_KT038_DyGKT | graph_leakage_risk | LOW | REVIEWER_INFERRED | PAPER_FULLTEXT | Sec. 3.2 & Protocol Sec. 7 | Timestamped continuous-time graph update strictly preserves temporal train/test causality | Codebook v0.4 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E038_011 | MODEL | MODEL_KT038_DyGKT | graph_representation | DYNAMIC_TEMPORAL, ITEM_ITEM | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.1 | Continuous-time dynamic graph over evolving student-question interaction states | 10.1145/3637528.3671773 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E038_012 | MODEL | MODEL_KT038_DyGKT | directed | Y | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.1 | Directed temporal interaction links from historical interactions to target query | 10.1145/3637528.3671773 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E038_013 | MODEL | MODEL_KT038_DyGKT | typed_edges | N | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.1 | Single continuous-time interaction relation type | 10.1145/3637528.3671773 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E038_014 | MODEL | MODEL_KT038_DyGKT | gnn_encoder | TEMPORAL_DYNAMIC_GNN | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4.1 | Continuous-time dynamic GNN encoder with dual time encoder & multiset indicator | 10.1145/3637528.3671773 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E038_015 | MODEL | MODEL_KT038_DyGKT | temporal_backbone | TEMPORAL_GRAPH_NATIVE | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4.2 | Native continuous-time dynamic graph temporal state update architecture | 10.1145/3637528.3671773 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E038_016 | MODEL | MODEL_KT038_DyGKT | ssl_family | NONE | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4.4 | Supervised prediction loss only | 10.1145/3637528.3671773 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E038_017 | EXPERIMENT | EXP_KT038_MAIN | datasets | ASSISTments2009, ASSISTments2017, Statics2011, EdNet, Junyi | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 5.1 | Evaluated on 5 real-world benchmark educational datasets | 10.1145/3637528.3671773 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E038_018 | EXPERIMENT | EXP_KT038_MAIN | n_seeds | 5 | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 5.1 | Performance averaged over 5 random seeds | 10.1145/3637528.3671773 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E038_019 | EXPERIMENT | EXP_KT038_MAIN | resampling_repeats | 1 | REVIEWER_INFERRED | PAPER_FULLTEXT | Sec. 5.1 | Single train/test data partition repeated over 5 model seeds | Codebook v0.4 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E038_020 | EXPERIMENT | EXP_KT038_MAIN | repeated_run_unit | SEED_REPETITION | REVIEWER_INFERRED | PAPER_FULLTEXT | Sec. 5.1 | Seed repetition unit (CB13) | Codebook v0.4 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E038_021 | EXPERIMENT | EXP_KT038_MAIN | sparse_concept_ontology | GENERIC_DATA_SPARSITY | REVIEWER_INFERRED | PAPER_FULLTEXT | Sec. 1 & 5.3 | Addresses continuous data expansion; no zero-exposure cold-start KC split evaluated | 10.1145/3637528.3671773 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E038_022 | EXPERIMENT | EXP_KT038_MAIN | computational_reporting | YES_FULL | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 5.4 | Reports formal time/memory complexity and empirical runtime curves | 10.1145/3637528.3671773 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
