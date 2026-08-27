# KT069 Field-Level Evidence Table (v1.0 LOCKED)

This document contains the long-form field-level evidence records for paper **KT069 (AEGOT-CDKT)**, satisfying the schema required in `coding_codebook_v1.0_LOCKED.md`.

## Schema
`evidence_id` | `entity_level` | `entity_id` | `field_name` | `coded_value` | `coding_basis` | `evidence_source_type` | `evidence_locator` | `evidence_note` | `source_url` | `coder_id` | `coder_type` | `coder_confidence` | `adjudication_status`

---

## Evidence Records

| evidence_id | entity_level | entity_id | field_name | coded_value | coding_basis | evidence_source_type | evidence_locator | evidence_note | source_url | coder_id | coder_type | coder_confidence | adjudication_status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| E069_001 | PAPER | PAPER_KT069 | title | A Cross-Domain Knowledge Tracing Model Based on Graph Optimal Transport | AUTHOR_STATED | PUBLISHER_METADATA | Article Title | Published journal title | 10.1007/s11280-024-01311-1 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E069_002 | PAPER | PAPER_KT069 | venue | World Wide Web | AUTHOR_STATED | PUBLISHER_METADATA | Journal Header | WWW Vol. 28, Article 10, 2025 | 10.1007/s11280-024-01311-1 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E069_003 | PAPER | PAPER_KT069 | kt_central_task | YES | AUTHOR_STATED | PAPER_FULLTEXT | Abstract & Sec. 1 | Cross-domain student response prediction & knowledge state transfer | 10.1007/s11280-024-01311-1 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E069_004 | PAPER | PAPER_KT069 | G_criterion | YES | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3 & 4 | Graph Optimal Transport cross-domain GNN auto-encoder | 10.1007/s11280-024-01311-1 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E069_005 | PAPER | PAPER_KT069 | S_criterion | NO | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4.4 | Supervised prediction loss only | 10.1007/s11280-024-01311-1 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E069_006 | PAPER | PAPER_KT069 | corpus_tier | PRIMARY_CORE | REVIEWER_INFERRED | PAPER_FULLTEXT | Protocol Sec. 4 | Primary core: satisfies G-criterion | Scope v1.0 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E069_007 | PAPER | PAPER_KT069 | coding_completeness | FULLTEXT_CODED | REVIEWER_INFERRED | PAPER_FULLTEXT | Full Text | Peer-reviewed journal text fully inspected | 10.1007/s11280-024-01311-1 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E069_008 | MODEL | MODEL_KT069_AEGOT_CDKT | graph_source | Q_MATRIX, CURRICULUM_CONCEPT_MAP, SIMILARITY | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.1 | Source and target domain concept graphs constructed from Q-matrices and concept similarity | 10.1007/s11280-024-01311-1 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E069_009 | MODEL | MODEL_KT069_AEGOT_CDKT | gnn_encoder | GRAPH_OPTIMAL_TRANSPORT | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.2 | Auto-encoder embedding and Graph Optimal Transport (GOT) GNN encoder | 10.1007/s11280-024-01311-1 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E069_010 | MODEL | MODEL_KT069_AEGOT_CDKT | temporal_backbone | RNN_LSTM_GRU | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 3.3 | GRU sequence backbone for temporal state tracking | 10.1007/s11280-024-01311-1 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E069_011 | MODEL | MODEL_KT069_AEGOT_CDKT | ssl_family | NONE | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 4.4 | Supervised prediction loss only | 10.1007/s11280-024-01311-1 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
| E069_012 | EXPERIMENT | EXP_KT069_MAIN | datasets | ASSISTments2009, ASSISTments2017, EdNet | AUTHOR_STATED | PAPER_FULLTEXT | Sec. 5.1 | Evaluated on 3 public benchmark educational datasets | 10.1007/s11280-024-01311-1 | AI_ASSISTANT | AI_ASSISTED | HIGH | ADJUDICATED |
