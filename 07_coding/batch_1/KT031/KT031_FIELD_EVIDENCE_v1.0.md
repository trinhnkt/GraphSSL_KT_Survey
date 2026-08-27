# KT031 Field-Level Evidence Table (v1.0 LOCKED)

This document contains the long-form field-level evidence records for paper **KT031**, satisfying the schema required in `coding_codebook_v1.0_LOCKED.md`.

## Schema
`evidence_id` | `entity_level` | `entity_id` | `field_name` | `coded_value` | `coding_basis` | `evidence_source_type` | `evidence_locator` | `evidence_note` | `source_url` | `coder_id` | `coder_type` | `coder_confidence` | `adjudication_status`

---

## Evidence Records

| evidence_id | entity_level | entity_id | field_name | coded_value | coding_basis | evidence_source_type | evidence_locator | evidence_note | source_url | coder_id | coder_type | coder_confidence | adjudication_status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| E031_001 | PAPER | PAPER_KT031 | title | Knowledge Structure Enhanced Graph Representation Learning Model for Attentive Knowledge Tracing | AUTHOR_STATED | PUBLISHER_METADATA | Article Title | Published journal title | 10.1002/int.22763 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E031_002 | PAPER | PAPER_KT031 | venue | International Journal of Intelligent Systems | AUTHOR_STATED | PUBLISHER_METADATA | Journal Header | IJIS Vol. 37, Issue 3, pp. 2012–2045, 2022 | 10.1002/int.22763 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E031_003 | PAPER | PAPER_KT031 | kt_central_task | YES | AUTHOR_STATED | PAPER_FULLTEXT | Abstract & Sec. 1 | Sequential learner response prediction & state tracking | 10.1002/int.22763 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E031_004 | PAPER | PAPER_KT031 | G_criterion | YES | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3 & 4 | Knowledge structure graph with graph neural network representation learning & attention | 10.1002/int.22763 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E031_005 | PAPER | PAPER_KT031 | S_criterion | NO | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4.4 | Supervised prediction loss only | 10.1002/int.22763 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E031_006 | PAPER | PAPER_KT031 | corpus_tier | PRIMARY_CORE | REVIEWER_INFERRED | PAPER_FULLTEXT | Protocol Sec. 4 | Primary core: satisfies G-criterion | Scope v1.0 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E031_007 | PAPER | PAPER_KT031 | coding_completeness | FULLTEXT_CODED | REVIEWER_INFERRED | PAPER_FULLTEXT | Full Text | Peer-reviewed journal text fully inspected | 10.1002/int.22763 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E031_008 | MODEL | MODEL_KT031_KSG_AKT | graph_source | CURRICULUM_CONCEPT_MAP, Q_MATRIX | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.1 | Knowledge structure concept graph constructed from Q-matrix and domain prerequisites | 10.1002/int.22763 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E031_009 | MODEL | MODEL_KT031_KSG_AKT | gnn_encoder | GCN | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.2 | Graph Convolutional Network representation encoder | 10.1002/int.22763 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E031_010 | MODEL | MODEL_KT031_KSG_AKT | temporal_backbone | SELF_ATTENTION_TRANSFORMER | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.3 | Attentive Transformer backbone for sequence tracing | 10.1002/int.22763 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E031_011 | MODEL | MODEL_KT031_KSG_AKT | ssl_family | NONE | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4.4 | Supervised prediction loss only | 10.1002/int.22763 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E031_012 | EXPERIMENT | EXP_KT031_MAIN | datasets | ASSISTments2009, ASSISTments2017, Statics2011, KDD Cup 2010 | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 5.1 | Evaluated on 4 public benchmark educational datasets | 10.1002/int.22763 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
