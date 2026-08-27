# KT033 Field-Level Evidence Table (v1.0 LOCKED)

This document contains the long-form field-level evidence records for paper **KT033 (DGMN)**, satisfying the schema required in `coding_codebook_v1.0_LOCKED.md`.

## Schema
`evidence_id` | `entity_level` | `entity_id` | `field_name` | `coded_value` | `coding_basis` | `evidence_source_type` | `evidence_locator` | `evidence_note` | `source_url` | `coder_id` | `coder_type` | `coder_confidence` | `adjudication_status`

---

## Evidence Records

| evidence_id | entity_level | entity_id | field_name | coded_value | coding_basis | evidence_source_type | evidence_locator | evidence_note | source_url | coder_id | coder_type | coder_confidence | adjudication_status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| E033_001 | PAPER | PAPER_KT033 | title | Deep Graph Memory Networks for Forgetting-Robust Knowledge Tracing | AUTHOR_STATED | PUBLISHER_METADATA | Article Title | Published journal title | 10.1109/TKDE.2022.3206447 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E033_002 | PAPER | PAPER_KT033 | venue | IEEE Transactions on Knowledge and Data Engineering | AUTHOR_STATED | PUBLISHER_METADATA | Journal Header | IEEE TKDE Vol. 35, Issue 8, pp. 7844–7855, 2023 | 10.1109/TKDE.2022.3206447 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E033_003 | PAPER | PAPER_KT033 | kt_central_task | YES | AUTHOR_STATED | PAPER_FULLTEXT | Abstract & Sec. 1 | Sequential learner performance prediction & forgetting-robust state tracking | 10.1109/TKDE.2022.3206447 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E033_004 | PAPER | PAPER_KT033 | G_criterion | YES | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3 & 4 | Dynamic latent concept graph integrated with memory network architecture | 10.1109/TKDE.2022.3206447 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E033_005 | PAPER | PAPER_KT033 | S_criterion | NO | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4.4 | Supervised prediction loss only | 10.1109/TKDE.2022.3206447 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E033_006 | PAPER | PAPER_KT033 | corpus_tier | PRIMARY_CORE | REVIEWER_INFERRED | PAPER_FULLTEXT | Protocol Sec. 4 | Primary core: satisfies G-criterion | Scope v1.0 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E033_007 | PAPER | PAPER_KT033 | coding_completeness | FULLTEXT_CODED | REVIEWER_INFERRED | PAPER_FULLTEXT | Full Text | Peer-reviewed IEEE journal text fully inspected | 10.1109/TKDE.2022.3206447 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E033_008 | MODEL | MODEL_KT033_DGMN | graph_source | LEARNED_FROM_INTERACTIONS, Q_MATRIX | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.1 | Dynamic latent concept graph updated dynamically from student interaction history | 10.1109/TKDE.2022.3206447 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E033_009 | MODEL | MODEL_KT033_DGMN | gnn_encoder | GRAPH_MEMORY | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.2 | Graph memory encoder updating latent concept node representations | 10.1109/TKDE.2022.3206447 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E033_010 | MODEL | MODEL_KT033_DGMN | temporal_backbone | MEMORY_NETWORK | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.3 | Key-value memory network with forgetting gate mechanism | 10.1109/TKDE.2022.3206447 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E033_011 | MODEL | MODEL_KT033_DGMN | ssl_family | NONE | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4.4 | Supervised prediction loss only | 10.1109/TKDE.2022.3206447 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E033_012 | EXPERIMENT | EXP_KT033_MAIN | datasets | ASSISTments2009, ASSISTments2017, Statics2011, EdNet | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 5.1 | Evaluated on 4 public benchmark educational datasets | 10.1109/TKDE.2022.3206447 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
