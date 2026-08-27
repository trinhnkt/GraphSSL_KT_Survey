# KT060 Field-Level Evidence Table (v1.0 LOCKED)

This document contains the long-form field-level evidence records for paper **KT060 (STHKT)**, satisfying the schema required in `coding_codebook_v1.0_LOCKED.md`.

## Schema
`evidence_id` | `entity_level` | `entity_id` | `field_name` | `coded_value` | `coding_basis` | `evidence_source_type` | `evidence_locator` | `evidence_note` | `source_url` | `coder_id` | `coder_type` | `coder_confidence` | `adjudication_status`

---

## Evidence Records

| evidence_id | entity_level | entity_id | field_name | coded_value | coding_basis | evidence_source_type | evidence_locator | evidence_note | source_url | coder_id | coder_type | coder_confidence | adjudication_status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| E060_001 | PAPER | PAPER_KT060 | title | STHKT: Spatiotemporal Knowledge Tracing with Topological Hawkes Process | AUTHOR_STATED | PUBLISHER_METADATA | Article Title | Published journal title | 10.1016/j.eswa.2024.125248 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E060_002 | PAPER | PAPER_KT060 | venue | Expert Systems with Applications | AUTHOR_STATED | PUBLISHER_METADATA | Journal Header | ESWA Vol. 259, Article 125248, 2025 | 10.1016/j.eswa.2024.125248 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E060_003 | PAPER | PAPER_KT060 | kt_central_task | YES | AUTHOR_STATED | PAPER_FULLTEXT | Abstract & Sec. 1 | Sequential learner performance prediction & spatiotemporal Hawkes tracing | 10.1016/j.eswa.2024.125248 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E060_004 | PAPER | PAPER_KT060 | G_criterion | YES | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3 & 4 | Topological graph structure combined with Hawkes process GNN | 10.1016/j.eswa.2024.125248 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E060_005 | PAPER | PAPER_KT060 | S_criterion | NO | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4.4 | Supervised prediction loss only | 10.1016/j.eswa.2024.125248 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E060_006 | PAPER | PAPER_KT060 | corpus_tier | PRIMARY_CORE | REVIEWER_INFERRED | PAPER_FULLTEXT | Protocol Sec. 4 | Primary core: satisfies G-criterion | Scope v1.0 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E060_007 | PAPER | PAPER_KT060 | coding_completeness | FULLTEXT_CODED | REVIEWER_INFERRED | PAPER_FULLTEXT | Full Text | Peer-reviewed journal text fully inspected | 10.1016/j.eswa.2024.125248 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E060_008 | MODEL | MODEL_KT060_STHKT | graph_source | Q_MATRIX, CURRICULUM_CONCEPT_MAP, SEQUENTIAL_TRANSITION | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.1 | Topological concept structure graph coupled with continuous-time interaction transitions | 10.1016/j.eswa.2024.125248 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E060_009 | MODEL | MODEL_KT060_STHKT | gnn_encoder | GRAPH_CONVOLUTIONAL_NETWORK | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.2 | Topological Graph Convolutional Network encoder | 10.1016/j.eswa.2024.125248 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E060_010 | MODEL | MODEL_KT060_STHKT | temporal_backbone | CONTINUOUS_TIME_HAWKES | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.3 | Topological Hawkes process continuous-time intensity model | 10.1016/j.eswa.2024.125248 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E060_011 | MODEL | MODEL_KT060_STHKT | ssl_family | NONE | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4.4 | Supervised prediction loss only | 10.1016/j.eswa.2024.125248 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E060_012 | EXPERIMENT | EXP_KT060_MAIN | datasets | ASSISTments2009, ASSISTments2017, Statics2011, EdNet | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 5.1 | Evaluated on 4 public benchmark educational datasets | 10.1016/j.eswa.2024.125248 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
