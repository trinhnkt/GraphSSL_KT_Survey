# KT063 — MAHKT Coding Record (v1.0 LOCKED)

**Paper ID:** PAPER_KT063  
**Legacy ID:** KT063  
**Title:** MAHKT: Knowledge Tracing with Multi-Association Heterogeneous Graph Embedding Based on Knowledge Transfer  
**Authors:** Huali Yang, Junjie Hu, Jinjin Chen, Tao Huang, et al.  
**Venue:** Knowledge-Based Systems, Vol. 310, Article 112958, Feb. 2025  
**DOI:** 10.1016/j.knosys.2025.112958  
**arXiv ID:** NR  
**Coder:** AI_ASSISTED (Antigravity Research-Engineering Assistant)  
**Codebook Version:** `coding_codebook_v1.0_LOCKED.md`  
**Date:** 2026-08-26  

---

# 1. PAPER Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `paper_id` | `PAPER_KT063` | AUTHOR_STATED | PUBLISHER_METADATA | KBS 2025 |
| `legacy_id` | `KT063` | AUTHOR_STATED | METADATA | Seed corpus identifier |
| `title` | MAHKT: Knowledge Tracing with Multi-Association Heterogeneous Graph Embedding Based on Knowledge Transfer | AUTHOR_STATED | PUBLISHER_METADATA | Article title |
| `publication_year` | 2025 | AUTHOR_STATED | PUBLISHER_METADATA | KBS Vol. 310 published Feb 2025 |
| `venue` | Knowledge-Based Systems | AUTHOR_STATED | PUBLISHER_METADATA | Elsevier peer-reviewed journal |
| `publication_type` | `JOURNAL_ARTICLE` | AUTHOR_STATED | PUBLISHER_METADATA | Full journal article |
| `peer_reviewed` | `YES` | AUTHOR_STATED | PUBLISHER_METADATA | Official journal publication |
| `doi` | 10.1016/j.knosys.2025.112958 | AUTHOR_STATED | PUBLISHER_METADATA | Official DOI |
| `arxiv_id` | `NR` | AUTHOR_STATED | PUBLISHER_METADATA | Direct journal article |
| `kt_central_task` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Sequential student performance prediction & knowledge transfer modeling |
| `G_criterion` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Multi-association heterogeneous graph embedding with knowledge transfer GNN |
| `S_criterion` | `NO` | AUTHOR_STATED | PAPER_FULLTEXT | Supervised prediction loss only |
| `corpus_tier` | `PRIMARY_CORE` | REVIEWER_INFERRED | PAPER_FULLTEXT | Satisfies G-criterion (`PRIMARY_CORE`) |
| `coding_completeness` | `FULLTEXT_CODED` | REVIEWER_INFERRED | PAPER_FULLTEXT | Peer-reviewed journal full text inspected |
| `third_party_implementation_available` | `YES` | METADATA | SECONDARY | Tracked in pyKT / KT benchmark repositories |

---

# 2. MODEL Level Coding (`MODEL_KT063_MAHKT`)

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `model_id` | `MODEL_KT063_MAHKT` | AUTHOR_STATED | PAPER_FULLTEXT | Primary MAHKT model formulation |
| `graph_source` | `Q_MATRIX, CURRICULUM_CONCEPT_MAP, CO_OCCURRENCE` | AUTHOR_STATED | PAPER_FULLTEXT | Multi-association heterogeneous graph connecting concepts, exercises, and knowledge transfer links |
| `graph_provenance` | `PRECOMPUTED_UNCLEAR_SPLIT` | REVIEWER_INFERRED | PAPER_FULLTEXT | Precomputed multi-association graph adjacency prior to sequence training |
| `graph_leakage_risk` | `POTENTIAL` | REVIEWER_INFERRED | PAPER_FULLTEXT | Multi-association edge weights without explicit train-only split reporting |
| `graph_representation` | `HETEROGENEOUS_MULTI_NODE, ITEM_KC_BIPARTITE, MULTI_RELATIONAL` | AUTHOR_STATED | PAPER_FULLTEXT | Heterogeneous graph with multi-association edge types and knowledge transfer mappings |
| `directed` | `Y` | AUTHOR_STATED | PAPER_FULLTEXT | Directed knowledge transfer associations |
| `typed_edges` | `Y` | AUTHOR_STATED | PAPER_FULLTEXT | Multiple association edge types |
| `gnn_encoder` | `HETEROGENEOUS_GNN` | AUTHOR_STATED | PAPER_FULLTEXT | Multi-Association Heterogeneous Graph Neural Network encoder |
| `temporal_backbone` | `RNN_LSTM_GRU` | AUTHOR_STATED | PAPER_FULLTEXT | GRU sequence backbone for temporal state tracking |
| `fusion_type` | `ATTENTION, CONCAT` | AUTHOR_STATED | PAPER_FULLTEXT | Attentive fusion of heterogeneous multi-association graph embeddings into sequence states |
| `fusion_location` | `HIDDEN_STATE` | AUTHOR_STATED | PAPER_FULLTEXT | Injected at recurrent sequence hidden state update loop |
| `ssl_family` | `NONE` | AUTHOR_STATED | PAPER_FULLTEXT | Supervised prediction loss only |
| `augmentation_type` | `NO_EXPLICIT_AUGMENTATION` | AUTHOR_STATED | PAPER_FULLTEXT | No data augmentation |
| `educational_structure_preservation` | `YES_EXPLICIT` | AUTHOR_STATED | PAPER_FULLTEXT | Preserves multi-association knowledge transfer relations across domain concepts |

---

# 3. EXPERIMENT Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `experiment_id` | `EXP_KT063_MAIN` | AUTHOR_STATED | PAPER_FULLTEXT | Main experimental evaluation |
| `datasets` | ASSISTments2009, ASSISTments2017, Statics2011 | AUTHOR_STATED | PAPER_FULLTEXT | Public benchmark educational datasets evaluated |
| `split_type` | `LEARNER_BASED` | AUTHOR_STATED | PAPER_FULLTEXT | Learner history partition into train/test splits |
| `n_seeds` | 5 | AUTHOR_STATED | PAPER_FULLTEXT | Performance averaged over 5 random seeds (CB13) |
| `resampling_repeats` | 1 | REVIEWER_INFERRED | PAPER_FULLTEXT | Single train/test data split repeated across seeds (CB13) |
| `repeated_run_unit` | `SEED_REPETITION` | REVIEWER_INFERRED | PAPER_FULLTEXT | Seed repetition unit (CB13) |
| `sparse_concept_ontology` | `GENERIC_DATA_SPARSITY` | REVIEWER_INFERRED | PAPER_FULLTEXT | Evaluates multi-association heterogeneous graph modeling on interaction data |
| `metrics` | ROC-AUC, ACC | AUTHOR_STATED | PAPER_FULLTEXT | Prediction accuracy and ROC-AUC metrics |
| `statistical_testing` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | Significance testing details omitted |
| `calibration_metrics` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | ECE omitted |
| `computational_reporting` | `LIMITED` | REVIEWER_INFERRED | PAPER_FULLTEXT | Scaling bounds omitted |

---

# 4. Quality Scoring (QA1–QA8)

| QA Criterion | Score (0-2) | Justification |
|---|---|---|
| **QA1 Task Clarity** | 2 | Clear formulation of multi-association heterogeneous graph embedding for knowledge transfer. |
| **QA2 Data Transparency** | 2 | Evaluates on public benchmark datasets (ASSIST09, ASSIST17, Statics11). |
| **QA3 Split/Leakage Transparency** | 1 | Train/test split reported; precomputed multi-association graph train-only isolation unverified. |
| **QA4 Baseline/Ablation Adequacy** | 2 | Evaluates against DKT, SAKT, GKT, GIKT and performs multi-association relation ablation. |
| **QA5 Statistical Uncertainty** | 1 | Reports mean performance across seeds; formal significance testing omitted. |
| **QA6 Author Artifacts** | 1 | Official journal full text verified; author code repository unverified. |
| **QA7 Sparse Construct Validity** | 1 | Motivates model via multi-association knowledge transfer, but lacks zero-exposure cold-start KC evaluation. |
| **QA8 Computational Transparency** | 1 | Explains heterogeneous GNN complexity; formal runtime scaling bounds omitted. |

**Raw Quality Score:** 11 / 16  
**Normalized Quality:** 0.6875 (**MODERATE Quality**)
