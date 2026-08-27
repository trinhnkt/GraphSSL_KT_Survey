# KT036 — TSKT Coding Record (v1.0 LOCKED)

**Paper ID:** PAPER_KT036  
**Legacy ID:** KT036  
**Title:** Heterogeneous Graph-Based Knowledge Tracing with Spatiotemporal Evolution  
**Authors:** Yang Yang, Xianyu Chen, Jian Shen, Haifeng Zhang, Yong Yu  
**Venue:** Expert Systems with Applications, Vol. 238, Article 122249, March 2024  
**DOI:** 10.1016/j.eswa.2023.122249  
**arXiv ID:** NR  
**Coder:** AI_ASSISTED (Antigravity Research-Engineering Assistant)  
**Codebook Version:** `coding_codebook_v1.0_LOCKED.md`  
**Date:** 2026-08-26  

---

# 1. PAPER Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `paper_id` | `PAPER_KT036` | AUTHOR_STATED | PUBLISHER_METADATA | ESWA 2024 |
| `legacy_id` | `KT036` | AUTHOR_STATED | METADATA | Seed corpus identifier |
| `title` | Heterogeneous Graph-Based Knowledge Tracing with Spatiotemporal Evolution | AUTHOR_STATED | PUBLISHER_METADATA | Article title |
| `publication_year` | 2024 | AUTHOR_STATED | PUBLISHER_METADATA | Published March 2024 |
| `venue` | Expert Systems with Applications | AUTHOR_STATED | PUBLISHER_METADATA | Elsevier peer-reviewed journal |
| `publication_type` | `JOURNAL_ARTICLE` | AUTHOR_STATED | PUBLISHER_METADATA | Full journal article |
| `peer_reviewed` | `YES` | AUTHOR_STATED | PUBLISHER_METADATA | Official journal publication |
| `doi` | 10.1016/j.eswa.2023.122249 | AUTHOR_STATED | PUBLISHER_METADATA | Official DOI |
| `arxiv_id` | `NR` | AUTHOR_STATED | PUBLISHER_METADATA | Direct journal article |
| `kt_central_task` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Sequential learner performance prediction & spatiotemporal knowledge tracing |
| `G_criterion` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Heterogeneous graph over student-exercise-concept nodes with spatiotemporal GNN evolution |
| `S_criterion` | `NO` | AUTHOR_STATED | PAPER_FULLTEXT | Supervised prediction loss only |
| `corpus_tier` | `PRIMARY_CORE` | REVIEWER_INFERRED | PAPER_FULLTEXT | Satisfies G-criterion (`PRIMARY_CORE`) |
| `coding_completeness` | `FULLTEXT_CODED` | REVIEWER_INFERRED | PAPER_FULLTEXT | Peer-reviewed journal full text inspected |
| `third_party_implementation_available` | `YES` | METADATA | SECONDARY | Tracked in pyKT / KT benchmark repositories |

---

# 2. MODEL Level Coding (`MODEL_KT036_TSKT`)

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `model_id` | `MODEL_KT036_TSKT` | AUTHOR_STATED | PAPER_FULLTEXT | Primary TSKT model formulation |
| `graph_source` | `Q_MATRIX, CO_OCCURRENCE, SEQUENTIAL_TRANSITION` | AUTHOR_STATED | PAPER_FULLTEXT | Heterogeneous graph derived from Q-matrix, exercise co-occurrence, and interaction transitions |
| `graph_provenance` | `JOINTLY_LEARNED_TRAINING` | AUTHOR_STATED | PAPER_FULLTEXT | Heterogeneous graph nodes and temporal edges updated dynamically |
| `graph_leakage_risk` | `LOW` | REVIEWER_INFERRED | PAPER_FULLTEXT | Spatiotemporal graph evolution strictly respects interaction timestamps |
| `graph_representation` | `HETEROGENEOUS_MULTI_NODE, DYNAMIC_TEMPORAL` | AUTHOR_STATED | PAPER_FULLTEXT | Heterogeneous spatiotemporal graph connecting student, exercise, and concept nodes |
| `directed` | `Y` | AUTHOR_STATED | PAPER_FULLTEXT | Directed spatiotemporal transition links |
| `typed_edges` | `Y` | AUTHOR_STATED | PAPER_FULLTEXT | Multiple relation types across heterogeneous nodes |
| `gnn_encoder` | `HETEROGENEOUS_GNN` | AUTHOR_STATED | PAPER_FULLTEXT | Heterogeneous Graph Neural Network with spatiotemporal evolution layers |
| `temporal_backbone` | `RNN_LSTM_GRU` | AUTHOR_STATED | PAPER_FULLTEXT | GRU sequence backbone for temporal state tracking |
| `fusion_type` | `ATTENTION, CONCAT` | AUTHOR_STATED | PAPER_FULLTEXT | Attentive fusion of spatiotemporal graph embeddings with temporal GRU states |
| `fusion_location` | `HIDDEN_STATE` | AUTHOR_STATED | PAPER_FULLTEXT | Injected at recurrent sequence hidden state update loop |
| `ssl_family` | `NONE` | AUTHOR_STATED | PAPER_FULLTEXT | Supervised prediction loss only |
| `augmentation_type` | `NO_EXPLICIT_AUGMENTATION` | AUTHOR_STATED | PAPER_FULLTEXT | No data augmentation |
| `educational_structure_preservation` | `YES_EXPLICIT` | AUTHOR_STATED | PAPER_FULLTEXT | Preserves spatial concept relationships and temporal learning evolution |

---

# 3. EXPERIMENT Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `experiment_id` | `EXP_KT036_MAIN` | AUTHOR_STATED | PAPER_FULLTEXT | Main experimental evaluation |
| `datasets` | ASSISTments2009, ASSISTments2017, Statics2011 | AUTHOR_STATED | PAPER_FULLTEXT | Benchmark educational datasets evaluated |
| `split_type` | `LEARNER_BASED` | AUTHOR_STATED | PAPER_FULLTEXT | Learner history partition into train/test splits |
| `n_seeds` | 5 | AUTHOR_STATED | PAPER_FULLTEXT | Performance averaged over 5 random seeds (CB13) |
| `resampling_repeats` | 1 | REVIEWER_INFERRED | PAPER_FULLTEXT | Single train/test split repeated across seeds (CB13) |
| `repeated_run_unit` | `SEED_REPETITION` | REVIEWER_INFERRED | PAPER_FULLTEXT | Seed repetition unit (CB13) |
| `sparse_concept_ontology` | `GENERIC_DATA_SPARSITY` | REVIEWER_INFERRED | PAPER_FULLTEXT | Evaluates spatiotemporal graph modeling on sparse interaction datasets |
| `metrics` | ROC-AUC, ACC | AUTHOR_STATED | PAPER_FULLTEXT | Prediction accuracy and ROC-AUC metrics |
| `statistical_testing` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | Significance testing details omitted |
| `calibration_metrics` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | ECE omitted |
| `computational_reporting` | `LIMITED` | REVIEWER_INFERRED | PAPER_FULLTEXT | Mentions spatiotemporal graph efficiency; scaling bounds omitted |

---

# 4. Quality Scoring (QA1–QA8)

| QA Criterion | Score (0-2) | Justification |
|---|---|---|
| **QA1 Task Clarity** | 2 | Clear formulation of heterogeneous spatiotemporal graph neural network for KT. |
| **QA2 Data Transparency** | 2 | Evaluates on public benchmark datasets (ASSIST09, ASSIST17, Statics11). |
| **QA3 Split/Leakage Transparency** | 2 | Spatiotemporal graph evolution respects temporal timestamps; low leakage risk. |
| **QA4 Baseline/Ablation Adequacy** | 2 | Evaluates against DKT, DKVMN, SAKT, GIKT and performs spatial/temporal module ablation. |
| **QA5 Statistical Uncertainty** | 1 | Reports mean performance across seeds; formal significance testing omitted. |
| **QA6 Author Artifacts** | 1 | Official journal full text verified; author code repository unverified. |
| **QA7 Sparse Construct Validity** | 1 | Motivates model via spatiotemporal concept evolution, but lacks zero-exposure cold-start KC evaluation. |
| **QA8 Computational Transparency** | 1 | Explains spatiotemporal GNN complexity; formal runtime scaling bounds omitted. |

**Raw Quality Score:** 12 / 16  
**Normalized Quality:** 0.7500 (**MODERATE Quality**)
