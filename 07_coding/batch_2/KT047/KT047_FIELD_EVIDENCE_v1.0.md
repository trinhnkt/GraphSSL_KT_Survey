# KT047 Field-Level Evidence Table (v1.0 LOCKED)

This document contains the long-form field-level evidence records for paper **KT047**, satisfying the schema required in `coding_codebook_v1.0_LOCKED.md`.

## Schema
`evidence_id` | `entity_level` | `entity_id` | `field_name` | `coded_value` | `coding_basis` | `evidence_source_type` | `evidence_locator` | `evidence_note` | `source_url` | `coder_id` | `coder_type` | `coder_confidence` | `adjudication_status`

---

## Evidence Records

| evidence_id | entity_level | entity_id | field_name | coded_value | coding_basis | evidence_source_type | evidence_locator | evidence_note | source_url | coder_id | coder_type | coder_confidence | adjudication_status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| E047_001 | PAPER | PAPER_KT047 | title | Fusing Hybrid Attentive Network with Self-Supervised Dual-Channel Heterogeneous Graph for Knowledge Tracing | AUTHOR_STATED | PUBLISHER_METADATA | Article Title | Published journal title | 10.1016/j.eswa.2023.120212 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E047_002 | PAPER | PAPER_KT047 | venue | Expert Systems with Applications | AUTHOR_STATED | PUBLISHER_METADATA | Journal Header | ESWA Vol. 225, Article 120212, 2023 | 10.1016/j.eswa.2023.120212 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E047_003 | PAPER | PAPER_KT047 | kt_central_task | YES | AUTHOR_STATED | PAPER_FULLTEXT | Abstract & Sec. 1 | Sequential learner response prediction & state tracking | 10.1016/j.eswa.2023.120212 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E047_004 | PAPER | PAPER_KT047 | G_criterion | YES | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3 & 4 | Dual-channel heterogeneous graph neural network over questions and concepts | 10.1016/j.eswa.2023.120212 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E047_005 | PAPER | PAPER_KT047 | S_criterion | YES | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4.4 | Dual-channel self-supervised contrastive learning pretext task | 10.1016/j.eswa.2023.120212 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E047_006 | PAPER | PAPER_KT047 | corpus_tier | PRIMARY_CORE | REVIEWER_INFERRED | PAPER_FULLTEXT | Protocol Sec. 4 | Primary core: satisfies G-criterion and S-criterion | Scope v1.0 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E047_007 | PAPER | PAPER_KT047 | coding_completeness | FULLTEXT_CODED | REVIEWER_INFERRED | PAPER_FULLTEXT | Full Text | Peer-reviewed journal text fully inspected | 10.1016/j.eswa.2023.120212 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E047_008 | MODEL | MODEL_KT047_DC_SSL | graph_source | Q_MATRIX, CO_OCCURRENCE | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.1 | Dual-channel heterogeneous graph constructed from Q-matrix and exercise interaction co-occurrences | 10.1016/j.eswa.2023.120212 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E047_009 | MODEL | MODEL_KT047_DC_SSL | gnn_encoder | HETEROGENEOUS_GNN | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.2 | Dual-channel Heterogeneous Graph Neural Network encoder | 10.1016/j.eswa.2023.120212 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E047_010 | MODEL | MODEL_KT047_DC_SSL | temporal_backbone | SELF_ATTENTION_TRANSFORMER | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.3 | Hybrid attentive Transformer backbone for sequence tracing | 10.1016/j.eswa.2023.120212 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E047_011 | MODEL | MODEL_KT047_DC_SSL | ssl_family | GRAPH_CONTRASTIVE, MULTIVIEW_CONTRASTIVE | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4.4 | Self-supervised contrastive loss across dual heterogeneous graph channels | 10.1016/j.eswa.2023.120212 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E047_012 | EXPERIMENT | EXP_KT047_MAIN | datasets | ASSISTments2009, ASSISTments2017, Statics2011 | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 5.1 | Evaluated on 3 public benchmark educational datasets | 10.1016/j.eswa.2023.120212 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
