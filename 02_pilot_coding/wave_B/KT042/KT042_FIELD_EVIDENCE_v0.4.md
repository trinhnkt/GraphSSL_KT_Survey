# KT042 Field-Level Evidence Table (v0.4 PILOT)

This document contains the long-form field-level evidence records for paper **KT042 (S2-HHN)**, satisfying the schema required in Section 2 of `coding_codebook_v0.4_PILOT.md`.

## Schema
`evidence_id` | `entity_level` | `entity_id` | `field_name` | `coded_value` | `coding_basis` | `evidence_source_type` | `evidence_locator` | `evidence_note` | `source_url` | `coder_id` | `coder_type` | `coder_confidence` | `adjudication_status`

---

## Evidence Records

| evidence_id | entity_level | entity_id | field_name | coded_value | coding_basis | evidence_source_type | evidence_locator | evidence_note | source_url | coder_id | coder_type | coder_confidence | adjudication_status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| E042_001 | PAPER | PAPER_KT042 | title | Self-Supervised Heterogeneous Hypergraph Network for Knowledge Tracing | AUTHOR_STATED | PUBLISHER_METADATA | Title | Official published article title | 10.1016/j.ins.2022.12.075 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E042_002 | PAPER | PAPER_KT042 | venue | Information Sciences | AUTHOR_STATED | PUBLISHER_METADATA | Journal Header | Vol. 624, pp. 200–216, May 2023 | 10.1016/j.ins.2022.12.075 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E042_003 | PAPER | PAPER_KT042 | kt_central_task | YES | AUTHOR_STATED | PAPER_FULLTEXT | Abstract & Sec. 1 | Sequential learner state estimation & future performance prediction | 10.1016/j.ins.2022.12.075 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E042_004 | PAPER | PAPER_KT042 | G_criterion | YES | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.1 & 3.2 | Heterogeneous hypergraph modeling student-exercise-KC higher-order hyperedges | 10.1016/j.ins.2022.12.075 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E042_005 | PAPER | PAPER_KT042 | S_criterion | YES | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.3 | Self-supervised hypergraph contrastive learning maximizing agreement between hypergraph views | 10.1016/j.ins.2022.12.075 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E042_006 | PAPER | PAPER_KT042 | corpus_tier | PRIMARY_CORE | REVIEWER_INFERRED | PAPER_FULLTEXT | Protocol Section 4 | Primary core: satisfies both G-criterion and S-criterion | Scope v1.0 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E042_007 | PAPER | PAPER_KT042 | coding_completeness | FULLTEXT_CODED | REVIEWER_INFERRED | PAPER_FULLTEXT | Full Text | Peer-reviewed journal article full text thoroughly inspected | 10.1016/j.ins.2022.12.075 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E042_008 | MODEL | MODEL_KT042_S2HHN | graph_source | HYBRID_MULTI_SOURCE | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.1 | Combines interaction logs, exercise attributes, and Q-matrix concept mappings | 10.1016/j.ins.2022.12.075 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E042_009 | MODEL | MODEL_KT042_S2HHN | graph_provenance | PRECOMPUTED_UNCLEAR_SPLIT | REVIEWER_INFERRED | PAPER_FULLTEXT | Sec. 3.1 | Hypergraph incidence matrix precomputed from dataset interactions | 10.1016/j.ins.2022.12.075 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E042_010 | MODEL | MODEL_KT042_S2HHN | graph_leakage_risk | POTENTIAL | REVIEWER_INFERRED | PAPER_FULLTEXT | Sec. 3.1 & Protocol Sec 7 | Precomputed hypergraph incidence matrix without explicit train-only isolation | Codebook v0.4 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E042_011 | MODEL | MODEL_KT042_S2HHN | graph_representation | HYPERGRAPH, HETEROGENEOUS_MULTI_NODE | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.2 | Heterogeneous hypergraph connecting student, exercise, and concept nodes | 10.1016/j.ins.2022.12.075 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E042_012 | MODEL | MODEL_KT042_S2HHN | directed | N | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.2 | Hypergraph projection $H W H^T$ operates via symmetric incidence matrix | 10.1016/j.ins.2022.12.075 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E042_013 | MODEL | MODEL_KT042_S2HHN | typed_edges | Y | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.2 | Heterogeneous hyperedges distinguish different entity node combinations | 10.1016/j.ins.2022.12.075 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E042_014 | MODEL | MODEL_KT042_S2HHN | gnn_encoder | HGNN_HYPERGRAPH | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.2 | Hypergraph neural network with intra- and inter-graph attention | 10.1016/j.ins.2022.12.075 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E042_015 | MODEL | MODEL_KT042_S2HHN | temporal_backbone | RNN_LSTM_GRU | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.4 | Recurrent neural network for temporal state prediction | 10.1016/j.ins.2022.12.075 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E042_016 | MODEL | MODEL_KT042_S2HHN | ssl_family | MULTIVIEW_CONTRASTIVE, GRAPH_CONTRASTIVE | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.3 | Self-supervised contrastive learning across perturbed hypergraph views | 10.1016/j.ins.2022.12.075 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E042_017 | EXPERIMENT | EXP_KT042_MAIN | datasets | ASSISTments2009, ASSISTments2017, Statics2011 | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4.1 | Evaluated on public benchmark educational datasets | 10.1016/j.ins.2022.12.075 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E042_018 | EXPERIMENT | EXP_KT042_MAIN | n_seeds | 5 | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4.1 | Performance averaged over 5 random seeds | 10.1016/j.ins.2022.12.075 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E042_019 | EXPERIMENT | EXP_KT042_MAIN | resampling_repeats | 1 | REVIEWER_INFERRED | PAPER_FULLTEXT | Sec. 4.1 | Single random train/test split repeated across 5 model seeds | Codebook v0.4 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E042_020 | EXPERIMENT | EXP_KT042_MAIN | repeated_run_unit | SEED_REPETITION | REVIEWER_INFERRED | PAPER_FULLTEXT | Sec. 4.1 | Seed repetition unit (CB13) | Codebook v0.4 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E042_021 | EXPERIMENT | EXP_KT042_MAIN | sparse_concept_ontology | GENERIC_DATA_SPARSITY | REVIEWER_INFERRED | PAPER_FULLTEXT | Sec. 4.3 | Addressed data sparsity generally; no zero-exposure cold-start KC split evaluated | 10.1016/j.ins.2022.12.075 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E042_022 | EXPERIMENT | EXP_KT042_MAIN | statistical_testing | NR | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4 | DeLong test / Wilcoxon signed-rank / Holm-Bonferroni correction not reported | 10.1016/j.ins.2022.12.075 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E042_023 | EXPERIMENT | EXP_KT042_MAIN | calibration_metrics | NR | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4 | ECE and Brier Score omitted | 10.1016/j.ins.2022.12.075 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
