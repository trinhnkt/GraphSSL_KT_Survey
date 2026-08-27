# KT023 Field-Level Evidence Table (v1.0 LOCKED)

This document contains the long-form field-level evidence records for paper **KT023 (SGKT)**, satisfying the schema required in `coding_codebook_v1.0_LOCKED.md`.

## Schema
`evidence_id` | `entity_level` | `entity_id` | `field_name` | `coded_value` | `coding_basis` | `evidence_source_type` | `evidence_locator` | `evidence_note` | `source_url` | `coder_id` | `coder_type` | `coder_confidence` | `adjudication_status`

---

## Evidence Records

| evidence_id | entity_level | entity_id | field_name | coded_value | coding_basis | evidence_source_type | evidence_locator | evidence_note | source_url | coder_id | coder_type | coder_confidence | adjudication_status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| E023_001 | PAPER | PAPER_KT023 | title | SGKT: Session Graph-Based Knowledge Tracing for Student Performance Prediction | AUTHOR_STATED | PUBLISHER_METADATA | Article Title | Published journal title | 10.1016/j.eswa.2022.117681 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E023_002 | PAPER | PAPER_KT023 | venue | Expert Systems with Applications | AUTHOR_STATED | PUBLISHER_METADATA | Journal Header | ESWA Vol. 206, Article 117681, 2022 | 10.1016/j.eswa.2022.117681 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E023_003 | PAPER | PAPER_KT023 | kt_central_task | YES | AUTHOR_STATED | PAPER_FULLTEXT | Abstract & Sec. 1 | Sequential learner response prediction & state estimation | 10.1016/j.eswa.2022.117681 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E023_004 | PAPER | PAPER_KT023 | G_criterion | YES | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3 & 4 | Session-based graph constructed over interaction sessions with GNN message passing | 10.1016/j.eswa.2022.117681 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E023_005 | PAPER | PAPER_KT023 | S_criterion | NO | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4.4 | Supervised prediction loss only | 10.1016/j.eswa.2022.117681 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E023_006 | PAPER | PAPER_KT023 | corpus_tier | PRIMARY_CORE | REVIEWER_INFERRED | PAPER_FULLTEXT | Protocol Sec. 4 | Primary core: satisfies G-criterion | Scope v1.0 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E023_007 | PAPER | PAPER_KT023 | coding_completeness | FULLTEXT_CODED | REVIEWER_INFERRED | PAPER_FULLTEXT | Full Text | Peer-reviewed journal text fully inspected | 10.1016/j.eswa.2022.117681 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E023_008 | MODEL | MODEL_KT023_SGKT | graph_source | SEQUENTIAL_TRANSITION, LEARNED_FROM_INTERACTIONS | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.1 | Session graphs constructed from student interaction sequence sessions | 10.1016/j.eswa.2022.117681 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E023_009 | MODEL | MODEL_KT023_SGKT | gnn_encoder | GATED_GRAPH_NEURAL_NETWORK | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.2 | Gated Graph Neural Network (GGNN) session encoder | 10.1016/j.eswa.2022.117681 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E023_010 | MODEL | MODEL_KT023_SGKT | temporal_backbone | RNN_LSTM_GRU | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.3 | GRU / attention sequence layer across sessions | 10.1016/j.eswa.2022.117681 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E023_011 | MODEL | MODEL_KT023_SGKT | ssl_family | NONE | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4.4 | Supervised prediction loss only | 10.1016/j.eswa.2022.117681 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E023_012 | EXPERIMENT | EXP_KT023_MAIN | datasets | ASSISTments2009, ASSISTments2017, Statics2011 | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 5.1 | Evaluated on 3 public benchmark educational datasets | 10.1016/j.eswa.2022.117681 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
