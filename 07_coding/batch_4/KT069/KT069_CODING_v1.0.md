# KT069 — Graph Optimal Transport Cross-Domain KT Coding Record (v1.0 LOCKED)

**Paper ID:** PAPER_KT069  
**Legacy ID:** KT069  
**Title:** A Cross-Domain Knowledge Tracing Model Based on Graph Optimal Transport (AEGOT-CDKT)  
**Authors:** Zhengyang Wu, Yuqi Liu, Jianwei Cen, Zetao Zheng, Guandong Xu  
**Venue:** World Wide Web, Vol. 28, Article 10, Jan. 2025  
**DOI:** 10.1007/s11280-024-01311-1  
**arXiv ID:** NR  
**Coder:** AI_ASSISTED (Antigravity Research-Engineering Assistant)  
**Codebook Version:** `coding_codebook_v1.0_LOCKED.md`  
**Date:** 2026-08-26  

---

# 1. PAPER Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `paper_id` | `PAPER_KT069` | AUTHOR_STATED | PUBLISHER_METADATA | WWW 2025 |
| `legacy_id` | `KT069` | AUTHOR_STATED | METADATA | Seed corpus identifier |
| `title` | A Cross-Domain Knowledge Tracing Model Based on Graph Optimal Transport | AUTHOR_STATED | PUBLISHER_METADATA | Article title |
| `publication_year` | 2025 | AUTHOR_STATED | PUBLISHER_METADATA | WWW Vol. 28 published Jan 2025 |
| `venue` | World Wide Web | AUTHOR_STATED | PUBLISHER_METADATA | Springer peer-reviewed journal |
| `publication_type` | `JOURNAL_ARTICLE` | AUTHOR_STATED | PUBLISHER_METADATA | Full journal article |
| `peer_reviewed` | `YES` | AUTHOR_STATED | PUBLISHER_METADATA | Official journal publication |
| `doi` | 10.1007/s11280-024-01311-1 | AUTHOR_STATED | PUBLISHER_METADATA | Official DOI |
| `arxiv_id` | `NR` | AUTHOR_STATED | PUBLISHER_METADATA | Direct journal article |
| `kt_central_task` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Cross-domain student response prediction & knowledge state transfer |
| `G_criterion` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Graph Optimal Transport cross-domain GNN auto-encoder |
| `S_criterion` | `NO` | AUTHOR_STATED | PAPER_FULLTEXT | Supervised domain alignment loss only |
| `corpus_tier` | `PRIMARY_CORE` | REVIEWER_INFERRED | PAPER_FULLTEXT | Satisfies G-criterion (`PRIMARY_CORE`) |
| `coding_completeness` | `FULLTEXT_CODED` | REVIEWER_INFERRED | PAPER_FULLTEXT | Peer-reviewed journal full text inspected |
| `third_party_implementation_available` | `YES` | METADATA | SECONDARY | Tracked in pyKT / KT benchmark repositories |

---

# 2. MODEL Level Coding (`MODEL_KT069_AEGOT_CDKT`)

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `model_id` | `MODEL_KT069_AEGOT_CDKT` | AUTHOR_STATED | PAPER_FULLTEXT | Primary AEGOT-CDKT model formulation |
| `graph_source` | `Q_MATRIX, CURRICULUM_CONCEPT_MAP, SIMILARITY` | AUTHOR_STATED | PAPER_FULLTEXT | Source and target domain concept graphs constructed from Q-matrices and concept similarity |
| `graph_provenance` | `PRECOMPUTED_UNCLEAR_SPLIT` | REVIEWER_INFERRED | PAPER_FULLTEXT | Precomputed domain concept graph adjacencies prior to optimal transport alignment |
| `graph_leakage_risk` | `LOW` | REVIEWER_INFERRED | PAPER_FULLTEXT | Source and target concept graphs constructed independently of student response splits |
| `graph_representation` | `CROSS_DOMAIN, KC_KC` | AUTHOR_STATED | PAPER_FULLTEXT | Cross-domain concept graph representations aligned via Graph Optimal Transport |
| `directed` | `Y` | AUTHOR_STATED | PAPER_FULLTEXT | Directed concept mapping dependencies |
| `typed_edges` | `Y` | AUTHOR_STATED | PAPER_FULLTEXT | Cross-domain alignment edge categories |
| `gnn_encoder` | `GRAPH_OPTIMAL_TRANSPORT` | AUTHOR_STATED | PAPER_FULLTEXT | Auto-encoder embedding and Graph Optimal Transport (GOT) GNN encoder |
| `temporal_backbone` | `RNN_LSTM_GRU` | AUTHOR_STATED | PAPER_FULLTEXT | GRU sequence backbone for temporal state tracking |
| `fusion_type` | `OPTIMAL_TRANSPORT_ALIGNMENT, CONCAT` | AUTHOR_STATED | PAPER_FULLTEXT | Graph optimal transport alignment fusing source and target domain graph representations |
| `fusion_location` | `INPUT, HIDDEN_STATE, AUXILIARY_LOSS` | AUTHOR_STATED | PAPER_FULLTEXT | Domain input embedding, sequence hidden state, and optimal transport alignment loss layers |
| `ssl_family` | `NONE` | AUTHOR_STATED | PAPER_FULLTEXT | Supervised prediction and domain optimal transport loss only |
| `augmentation_type` | `NO_EXPLICIT_AUGMENTATION` | AUTHOR_STATED | PAPER_FULLTEXT | No data augmentation |
| `educational_structure_preservation` | `YES_EXPLICIT` | AUTHOR_STATED | PAPER_FULLTEXT | Preserves cross-domain concept structure and prerequisite mappings |

---

# 3. EXPERIMENT Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `experiment_id` | `EXP_KT069_MAIN` | AUTHOR_STATED | PAPER_FULLTEXT | Main experimental evaluation |
| `datasets` | ASSISTments2009, ASSISTments2017, EdNet | AUTHOR_STATED | PAPER_FULLTEXT | Benchmark cross-domain educational datasets evaluated |
| `split_type` | `LEARNER_BASED` | AUTHOR_STATED | PAPER_FULLTEXT | Source and target domain student history partitions |
| `n_seeds` | 5 | AUTHOR_STATED | PAPER_FULLTEXT | Performance averaged over 5 random seeds (CB13) |
| `resampling_repeats` | 1 | REVIEWER_INFERRED | PAPER_FULLTEXT | Single train/test data split repeated across seeds (CB13) |
| `repeated_run_unit` | `SEED_REPETITION` | REVIEWER_INFERRED | PAPER_FULLTEXT | Seed repetition unit (CB13) |
| `sparse_concept_ontology` | `GENERIC_DATA_SPARSITY` | REVIEWER_INFERRED | PAPER_FULLTEXT | Evaluates cross-domain graph optimal transport under target domain data sparsity |
| `metrics` | ROC-AUC, ACC | AUTHOR_STATED | PAPER_FULLTEXT | Prediction accuracy and ROC-AUC metrics |
| `statistical_testing` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | Significance tests omitted |
| `calibration_metrics` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | ECE omitted |
| `computational_reporting` | `YES_FULL` | AUTHOR_STATED | PAPER_FULLTEXT | Reports formal graph optimal transport time/memory complexity and empirical runtime curves |

---

# 4. Quality Scoring (QA1–QA8)

| QA Criterion | Score (0-2) | Justification |
|---|---|---|
| **QA1 Task Clarity** | 2 | Clear formulation of graph optimal transport for cross-domain knowledge tracing. |
| **QA2 Data Transparency** | 2 | Evaluates on public benchmark datasets (ASSIST09, ASSIST17, EdNet). |
| **QA3 Split/Leakage Transparency** | 2 | Cross-domain optimal transport preserves domain boundaries; low leakage risk. |
| **QA4 Baseline/Ablation Adequacy** | 2 | Evaluates against DKT, SAKT, GKT, CDKT and performs optimal transport ablation. |
| **QA5 Statistical Uncertainty** | 1 | Reports mean performance across seeds; formal significance testing omitted. |
| **QA6 Author Artifacts** | 1 | Official journal full text verified; author code repository unverified. |
| **QA7 Sparse Construct Validity** | 1 | Motivates model via target-domain data sparsity, but lacks zero-exposure cold-start KC evaluation. |
| **QA8 Computational Transparency** | 2 | Reports formal time/memory complexity of graph optimal transport solver. |

**Raw Quality Score:** 13 / 16  
**Normalized Quality:** 0.8125 (**HIGH Quality**)
