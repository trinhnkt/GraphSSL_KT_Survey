# KT055 Field-Level Evidence Table (v0.4 PILOT)

This document contains the long-form field-level evidence records for paper **KT055**, satisfying the schema required in Section 2 of `coding_codebook_v0.4_PILOT.md`.

## Schema
`evidence_id` | `entity_level` | `entity_id` | `field_name` | `coded_value` | `coding_basis` | `evidence_source_type` | `evidence_locator` | `evidence_note` | `source_url` | `coder_id` | `coder_type` | `coder_confidence` | `adjudication_status`

---

## Evidence Records

| evidence_id | entity_level | entity_id | field_name | coded_value | coding_basis | evidence_source_type | evidence_locator | evidence_note | source_url | coder_id | coder_type | coder_confidence | adjudication_status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| E055_001 | PAPER | PAPER_KT055 | title | GKT-CD: Make Cognitive Diagnosis Model Enhanced by Graph-Based Knowledge Tracing | AUTHOR_STATED | PUBLISHER_METADATA | Title | Official published IEEE conference title | 10.1109/IJCNN52387.2021.9533367 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E055_002 | PAPER | PAPER_KT055 | venue | IJCNN | AUTHOR_STATED | PUBLISHER_METADATA | Conference Header | IEEE IJCNN 2021 Conference Proceedings | 10.1109/IJCNN52387.2021.9533367 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E055_003 | PAPER | PAPER_KT055 | kt_central_task | NO | REVIEWER_INFERRED | PAPER_FULLTEXT | Abstract & Sec. 1 | Primary objective is static Cognitive Diagnosis (profiling student proficiency state matrix) rather than sequential KT performance prediction | 10.1109/IJCNN52387.2021.9533367 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E055_004 | PAPER | PAPER_KT055 | G_criterion | YES | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3 & 4 | Uses Gated GNN over exercise-concept graph | 10.1109/IJCNN52387.2021.9533367 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E055_005 | PAPER | PAPER_KT055 | S_criterion | NO | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4.4 | Supervised cognitive diagnosis loss | 10.1109/IJCNN52387.2021.9533367 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E055_006 | PAPER | PAPER_KT055 | corpus_tier | EXCLUDE_FULLTEXT | REVIEWER_INFERRED | PAPER_FULLTEXT | Protocol Sec. 4 | Excluded: Fails primary gateway requirement (kt_central_task = NO). Cognitive Diagnosis enhanced by Graph-KT is excluded | Scope v1.0 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E055_007 | PAPER | PAPER_KT055 | coding_completeness | FULLTEXT_CODED | REVIEWER_INFERRED | PAPER_FULLTEXT | Full Text | Peer-reviewed IJCNN 2021 full text thoroughly inspected | 10.1109/IJCNN52387.2021.9533367 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E055_008 | MODEL | MODEL_KT055_GKT_CD | graph_source | Q_MATRIX, EXPERT_PREREQUISITE | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.1 | Exercise-concept graph constructed from Q-matrix and concept dependencies | 10.1109/IJCNN52387.2021.9533367 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E055_009 | MODEL | MODEL_KT055_GKT_CD | gnn_encoder | GCN | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.2 | Gated GNN / GCN message passing | 10.1109/IJCNN52387.2021.9533367 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E055_010 | MODEL | MODEL_KT055_GKT_CD | temporal_backbone | NONE | REVIEWER_INFERRED | PAPER_FULLTEXT | Sec. 3.3 | Static Cognitive Diagnosis formulation; lacks sequential temporal state tracking backbone | 10.1109/IJCNN52387.2021.9533367 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
