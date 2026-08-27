# KT011 Field-Level Evidence Table (v0.4 PILOT)

This document contains the long-form field-level evidence records for paper **KT011 (Bi-CLKT)**, satisfying the schema required in Section 2 of `coding_codebook_v0.4_PILOT.md`.

## Schema
`evidence_id` | `entity_level` | `entity_id` | `field_name` | `coded_value` | `coding_basis` | `evidence_source_type` | `evidence_locator` | `evidence_note` | `source_url` | `coder_id` | `coder_type` | `coder_confidence` | `adjudication_status`

---

## Evidence Records

| evidence_id | entity_level | entity_id | field_name | coded_value | coding_basis | evidence_source_type | evidence_locator | evidence_note | source_url | coder_id | coder_type | coder_confidence | adjudication_status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| E011_001 | PAPER | PAPER_KT011 | title | Bi-CLKT: Bi-Graph Contrastive Learning Based Knowledge Tracing | AUTHOR_STATED | PUBLISHER_METADATA | Title | Official published article title | 10.1016/j.knosys.2022.108274 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E011_002 | PAPER | PAPER_KT011 | venue | Knowledge-Based Systems | AUTHOR_STATED | PUBLISHER_METADATA | Journal Header | Vol. 241, Article 108274 | 10.1016/j.knosys.2022.108274 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E011_003 | PAPER | PAPER_KT011 | kt_central_task | YES | AUTHOR_STATED | PAPER_FULLTEXT | Abstract & Sec. 1 | Model predicts student responses to future exercises | arXiv:2201.09020 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E011_004 | PAPER | PAPER_KT011 | G_criterion | YES | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.1 & 3.2 | Constructs exercise-to-exercise (E2E) relational subgraphs and concept graphs | arXiv:2201.09020 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E011_005 | PAPER | PAPER_KT011 | S_criterion | YES | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.3 & 3.4 | Employs dual node-level & graph-level contrastive learning losses | arXiv:2201.09020 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E011_006 | PAPER | PAPER_KT011 | corpus_tier | PRIMARY_CORE | REVIEWER_INFERRED | PAPER_FULLTEXT | Protocol Section 4 | Primary core: satisfies both G-criterion and S-criterion | Scope v1.0 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E011_007 | PAPER | PAPER_KT011 | coding_completeness | FULLTEXT_CODED | REVIEWER_INFERRED | PAPER_FULLTEXT | Full Text | Peer-reviewed journal text and arXiv manuscript thoroughly inspected | arXiv:2201.09020 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E011_008 | MODEL | MODEL_KT011_BiCLKT_RNN | graph_source | CO_OCCURRENCE | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.1 | E2E subgraph constructed from exercise interaction co-occurrences | arXiv:2201.09020 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E011_009 | MODEL | MODEL_KT011_BiCLKT_RNN | graph_provenance | PRECOMPUTED_UNCLEAR_SPLIT | REVIEWER_INFERRED | PAPER_FULLTEXT | Sec. 3.1 | Precomputed from interaction logs; temporal train/test split isolation not explicit | arXiv:2201.09020 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E011_010 | MODEL | MODEL_KT011_BiCLKT_RNN | graph_leakage_risk | POTENTIAL | REVIEWER_INFERRED | PAPER_FULLTEXT | Sec. 3.1 & Protocol Sec 7 | Precomputed graph without train-only guarantee carries potential leakage risk | Codebook v0.4 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E011_011 | MODEL | MODEL_KT011_BiCLKT_RNN | graph_representation | ITEM_ITEM, KC_KC, ITEM_KC_BIPARTITE | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.2 | Bi-graph structure linking exercise subgraphs and concept graphs | arXiv:2201.09020 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E011_012 | MODEL | MODEL_KT011_BiCLKT_RNN | directed | Y | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.1 | Directed edges in exercise-to-exercise subgraphs based on transition order | arXiv:2201.09020 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E011_013 | MODEL | MODEL_KT011_BiCLKT_RNN | typed_edges | Y | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.2 | Distinguishes exercise-exercise relations and exercise-concept relations | arXiv:2201.09020 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E011_014 | MODEL | MODEL_KT011_BiCLKT_RNN | gnn_encoder | GCN | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.2 | Subgraph GNN encoder for exercise/concept node embeddings | arXiv:2201.09020 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E011_015 | MODEL | MODEL_KT011_BiCLKT_RNN | temporal_backbone | RNN_LSTM_GRU | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.5 | Recurrent network (RNN/LSTM) for state tracking | arXiv:2201.09020 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E011_016 | MODEL | MODEL_KT011_BiCLKT_RNN | ssl_family | MULTIVIEW_CONTRASTIVE, GRAPH_CONTRASTIVE | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.3 & 3.4 | Dual node-level exercise loss + graph-level concept contrastive loss | arXiv:2201.09020 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E011_017 | EXPERIMENT | EXP_KT011_MAIN | datasets | ASSISTments2009, ASSISTments2012, Junyi, Statics2011 | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4.1 | Evaluated on 4 public benchmark datasets | arXiv:2201.09020 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E011_018 | EXPERIMENT | EXP_KT011_MAIN | n_seeds | 5 | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4.1 | Average performance reported over 5 random seeds | arXiv:2201.09020 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E011_019 | EXPERIMENT | EXP_KT011_MAIN | resampling_repeats | 1 | REVIEWER_INFERRED | PAPER_FULLTEXT | Sec. 4.1 | Single random train/test split repeated over 5 model seeds | Codebook v0.4 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E011_020 | EXPERIMENT | EXP_KT011_MAIN | repeated_run_unit | SEED_REPETITION | REVIEWER_INFERRED | PAPER_FULLTEXT | Sec. 4.1 | Model seed repetition unit (CB13) | Codebook v0.4 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E011_021 | EXPERIMENT | EXP_KT011_MAIN | sparse_concept_ontology | GENERIC_DATA_SPARSITY | REVIEWER_INFERRED | PAPER_FULLTEXT | Sec. 4.3 | Data sparsity mentioned as general motivation; no zero-exposure cold-start KC evaluation | arXiv:2201.09020 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E011_022 | EXPERIMENT | EXP_KT011_MAIN | statistical_testing | NR | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4 | DeLong test / Wilcoxon signed-rank / Holm-Bonferroni correction not reported | arXiv:2201.09020 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E011_023 | EXPERIMENT | EXP_KT011_MAIN | calibration_metrics | NR | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4 | ECE and Brier Score omitted | arXiv:2201.09020 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
