# KT037 Field-Level Evidence Table (v0.4 PILOT)

This document contains the long-form field-level evidence records for paper **KT037 (CMKT)**, satisfying the schema required in Section 2 of `coding_codebook_v0.4_PILOT.md`.

## Schema
`evidence_id` | `entity_level` | `entity_id` | `field_name` | `coded_value` | `coding_basis` | `evidence_source_type` | `evidence_locator` | `evidence_note` | `source_url` | `coder_id` | `coder_type` | `coder_confidence` | `adjudication_status`

---

## Evidence Records

| evidence_id | entity_level | entity_id | field_name | coded_value | coding_basis | evidence_source_type | evidence_locator | evidence_note | source_url | coder_id | coder_type | coder_confidence | adjudication_status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| E037_001 | PAPER | PAPER_KT037 | title | CMKT: Concept Map Driven Knowledge Tracing | AUTHOR_STATED | PUBLISHER_METADATA | Article Title | Official published journal title | 10.1109/TLT.2022.3196355 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E037_002 | PAPER | PAPER_KT037 | venue | IEEE Transactions on Learning Technologies | AUTHOR_STATED | PUBLISHER_METADATA | Journal Header | IEEE TLT Vol. 15, Issue 4, pp. 467–480, Aug 2022 | 10.1109/TLT.2022.3196355 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E037_003 | PAPER | PAPER_KT037 | kt_central_task | YES | AUTHOR_STATED | PAPER_FULLTEXT | Abstract & Sec. I | Sequential learner knowledge state estimation and future performance prediction | 10.1109/TLT.2022.3196355 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E037_004 | PAPER | PAPER_KT037 | G_criterion | YES | AUTHOR_STATED | PAPER_FULLTEXT | Sec. III & IV | Concept map topology embedding and pairwise ordering constraints in RNN KT | 10.1109/TLT.2022.3196355 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E037_005 | PAPER | PAPER_KT037 | S_criterion | NO | AUTHOR_STATED | PAPER_FULLTEXT | Sec. III.D | Supervised cross-entropy KT loss + concept map ordering constraint; no SSL pretext task | 10.1109/TLT.2022.3196355 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E037_006 | PAPER | PAPER_KT037 | corpus_tier | PRIMARY_CORE | REVIEWER_INFERRED | PAPER_FULLTEXT | Protocol Sec. 4 | Satisfies G-criterion (Graph-Based KT) | Scope v1.0 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E037_007 | PAPER | PAPER_KT037 | coding_completeness | FULLTEXT_CODED | REVIEWER_INFERRED | PAPER_FULLTEXT | Full Text | Peer-reviewed IEEE TLT journal text & methodology fully inspected | 10.1109/TLT.2022.3196355 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E037_008 | MODEL | MODEL_KT037_CMKT | graph_source | CURRICULUM_CONCEPT_MAP, EXPERT_PREREQUISITE | AUTHOR_STATED | PAPER_FULLTEXT | Sec. III.A | Educational concept map specifying concept ordering / prerequisite relations | 10.1109/TLT.2022.3196355 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E037_009 | MODEL | MODEL_KT037_CMKT | graph_provenance | EXTERNAL_FIXED | AUTHOR_STATED | PAPER_FULLTEXT | Sec. III.A | Concept map provided externally as pedagogical domain prior | 10.1109/TLT.2022.3196355 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E037_010 | MODEL | MODEL_KT037_CMKT | graph_leakage_risk | LOW | REVIEWER_INFERRED | PAPER_FULLTEXT | Sec. III.A & Protocol Sec. 7 | External concept map independent of interaction data train/test splits | Codebook v0.4 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E037_011 | MODEL | MODEL_KT037_CMKT | graph_representation | KC_KC, DAG | AUTHOR_STATED | PAPER_FULLTEXT | Sec. III.A | Directed pairwise ordering constraints between knowledge concepts | 10.1109/TLT.2022.3196355 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E037_012 | MODEL | MODEL_KT037_CMKT | directed | Y | AUTHOR_STATED | PAPER_FULLTEXT | Sec. III.A | Directed ordering pairs between concept nodes | 10.1109/TLT.2022.3196355 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E037_013 | MODEL | MODEL_KT037_CMKT | typed_edges | N | AUTHOR_STATED | PAPER_FULLTEXT | Sec. III.A | Single relation type representing concept ordering dependencies | 10.1109/TLT.2022.3196355 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E037_014 | MODEL | MODEL_KT037_CMKT | gnn_encoder | NONE | AUTHOR_STATED | PAPER_FULLTEXT | Sec. III.B | Uses network embedding and ordering loss constraints rather than GNN message-passing | 10.1109/TLT.2022.3196355 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E037_015 | MODEL | MODEL_KT037_CMKT | temporal_backbone | RNN_LSTM_GRU | AUTHOR_STATED | PAPER_FULLTEXT | Sec. III.C | Recurrent Neural Network (RNN) sequence layer for learner state tracking | 10.1109/TLT.2022.3196355 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E037_016 | MODEL | MODEL_KT037_CMKT | ssl_family | NONE | AUTHOR_STATED | PAPER_FULLTEXT | Sec. III.D | Supervised cross-entropy KT loss + ordering pair structural loss | 10.1109/TLT.2022.3196355 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E037_017 | EXPERIMENT | EXP_KT037_MAIN | datasets | ASSISTments2009, Junyi | AUTHOR_STATED | PAPER_FULLTEXT | Sec. IV.A | Evaluated on public benchmark educational datasets | 10.1109/TLT.2022.3196355 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E037_018 | EXPERIMENT | EXP_KT037_MAIN | n_seeds | 5 | AUTHOR_STATED | PAPER_FULLTEXT | Sec. IV.B | Performance averaged over 5 random initialization seeds | 10.1109/TLT.2022.3196355 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E037_019 | EXPERIMENT | EXP_KT037_MAIN | resampling_repeats | 1 | REVIEWER_INFERRED | PAPER_FULLTEXT | Sec. IV.B | Single random train/test data split repeated across 5 model seeds | Codebook v0.4 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E037_020 | EXPERIMENT | EXP_KT037_MAIN | repeated_run_unit | SEED_REPETITION | REVIEWER_INFERRED | PAPER_FULLTEXT | Sec. IV.B | Seed repetition unit (CB13) | Codebook v0.4 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E037_021 | EXPERIMENT | EXP_KT037_MAIN | sparse_concept_ontology | GENERIC_DATA_SPARSITY | REVIEWER_INFERRED | PAPER_FULLTEXT | Sec. I & IV.C | Addresses learner interaction data sparseness; no zero-exposure cold-start KC split evaluated | 10.1109/TLT.2022.3196355 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E037_022 | EXPERIMENT | EXP_KT037_MAIN | statistical_testing | NR | AUTHOR_STATED | PAPER_FULLTEXT | Sec. IV | Significance testing details omitted | 10.1109/TLT.2022.3196355 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E037_023 | EXPERIMENT | EXP_KT037_MAIN | calibration_metrics | NR | AUTHOR_STATED | PAPER_FULLTEXT | Sec. IV | ECE and Brier Score omitted | 10.1109/TLT.2022.3196355 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
