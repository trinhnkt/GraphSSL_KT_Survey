# KT012 — JKT Coding Record (v1.0 LOCKED)

**Paper ID:** PAPER_KT012  
**Legacy ID:** KT012  
**Title:** JKT: A Joint Graph Convolutional Network Based Deep Knowledge Tracing  
**Authors:** Xian Song, Junxiao Liu, Fangneng Lei, Jianghao Zhou, Eric Hsiao, Yuangang Li  
**Venue:** Information Sciences, Vol. 580, pp. 510–523, Oct. 2021  
**DOI:** 10.1016/j.ins.2021.08.100  
**arXiv ID:** NR  
**Coder:** AI_ASSISTED (Antigravity Research-Engineering Assistant)  
**Codebook Version:** `coding_codebook_v1.0_LOCKED.md`  
**Date:** 2026-08-26  

---

# 1. PAPER Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `paper_id` | `PAPER_KT012` | AUTHOR_STATED | PUBLISHER_METADATA | Information Sciences 2021 |
| `legacy_id` | `KT012` | AUTHOR_STATED | METADATA | Seed corpus identifier |
| `title` | JKT: A Joint Graph Convolutional Network Based Deep Knowledge Tracing | AUTHOR_STATED | PUBLISHER_METADATA | Article title |
| `publication_year` | 2021 | AUTHOR_STATED | PUBLISHER_METADATA | Published Oct 2021 |
| `venue` | Information Sciences | AUTHOR_STATED | PUBLISHER_METADATA | Elsevier peer-reviewed journal |
| `publication_type` | `JOURNAL_ARTICLE` | AUTHOR_STATED | PUBLISHER_METADATA | Full journal article |
| `peer_reviewed` | `YES` | AUTHOR_STATED | PUBLISHER_METADATA | Official journal publication |
| `doi` | 10.1016/j.ins.2021.08.100 | AUTHOR_STATED | PUBLISHER_METADATA | Official DOI |
| `arxiv_id` | `NR` | AUTHOR_STATED | PUBLISHER_METADATA | Direct journal article |
| `kt_central_task` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Sequential learner response prediction & state estimation |
| `G_criterion` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Joint GCN over exercise-to-exercise & concept-to-concept graphs fused with Q-matrix |
| `S_criterion` | `NO` | AUTHOR_STATED | PAPER_FULLTEXT | Supervised cross-entropy prediction loss only |
| `corpus_tier` | `PRIMARY_CORE` | REVIEWER_INFERRED | PAPER_FULLTEXT | Satisfies G-criterion (`PRIMARY_CORE`) |
| `coding_completeness` | `FULLTEXT_CODED` | REVIEWER_INFERRED | PAPER_FULLTEXT | Peer-reviewed journal full text inspected |
| `third_party_implementation_available` | `YES` | METADATA | SECONDARY | Tracked in pyKT / KT benchmark literature |

---

# 2. MODEL Level Coding (`MODEL_KT012_JKT`)

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `model_id` | `MODEL_KT012_JKT` | AUTHOR_STATED | PAPER_FULLTEXT | Primary JKT model formulation |
| `graph_source` | `Q_MATRIX, CO_OCCURRENCE` | AUTHOR_STATED | PAPER_FULLTEXT | Exercise-exercise & concept-concept graphs fused with Q-matrix relations |
| `graph_provenance` | `PRECOMPUTED_UNCLEAR_SPLIT` | REVIEWER_INFERRED | PAPER_FULLTEXT | Precomputed graph adjacency matrices prior to sequence training |
| `graph_leakage_risk` | `POTENTIAL` | REVIEWER_INFERRED | PAPER_FULLTEXT | Precomputed co-occurrence adjacency without explicit train-only split isolation |
| `graph_representation` | `ITEM_ITEM, KC_KC, ITEM_KC_BIPARTITE` | AUTHOR_STATED | PAPER_FULLTEXT | Multi-graph representation linking exercises and concepts |
| `directed` | `N` | AUTHOR_STATED | PAPER_FULLTEXT | Symmetric joint GCN adjacency matrices |
| `typed_edges` | `Y` | AUTHOR_STATED | PAPER_FULLTEXT | Multiple relation types (exercise-exercise vs concept-concept vs Q-matrix) |
| `gnn_encoder` | `GCN` | AUTHOR_STATED | PAPER_FULLTEXT | Joint Graph Convolutional Network (GCN) encoder |
| `temporal_backbone` | `RNN_LSTM_GRU` | AUTHOR_STATED | PAPER_FULLTEXT | LSTM sequence layer for learner state tracing |
| `fusion_type` | `CONCAT, ATTENTION` | AUTHOR_STATED | PAPER_FULLTEXT | Attentive fusion of GCN graph embeddings into LSTM state representations |
| `fusion_location` | `INPUT, HIDDEN_STATE` | AUTHOR_STATED | PAPER_FULLTEXT | Input embedding and sequence state layers |
| `ssl_family` | `NONE` | AUTHOR_STATED | PAPER_FULLTEXT | Supervised loss only |
| `augmentation_type` | `NO_EXPLICIT_AUGMENTATION` | AUTHOR_STATED | PAPER_FULLTEXT | No data augmentation or pretext task |
| `educational_structure_preservation` | `YES_EXPLICIT` | AUTHOR_STATED | PAPER_FULLTEXT | Preserves multi-dimensional exercise-concept mapping relationships |

---

# 3. EXPERIMENT Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `experiment_id` | `EXP_KT012_MAIN` | AUTHOR_STATED | PAPER_FULLTEXT | Main experimental evaluation |
| `datasets` | ASSISTments2009, ASSISTments2012, Statics2011, KDD Cup 2010 | AUTHOR_STATED | PAPER_FULLTEXT | 4 public benchmark educational datasets evaluated |
| `split_type` | `LEARNER_BASED` | AUTHOR_STATED | PAPER_FULLTEXT | 80/20 train/test learner split |
| `n_seeds` | 5 | AUTHOR_STATED | PAPER_FULLTEXT | Evaluated over 5 random seeds (CB13) |
| `resampling_repeats` | 1 | REVIEWER_INFERRED | PAPER_FULLTEXT | Single train/test split repeated across 5 model seeds (CB13) |
| `repeated_run_unit` | `SEED_REPETITION` | REVIEWER_INFERRED | PAPER_FULLTEXT | Seed repetition unit (CB13) |
| `sparse_concept_ontology` | `GENERIC_DATA_SPARSITY` | REVIEWER_INFERRED | PAPER_FULLTEXT | Addresses interaction data sparseness; no zero-exposure cold-start KC split evaluated |
| `metrics` | ROC-AUC, ACC | AUTHOR_STATED | PAPER_FULLTEXT | Prediction accuracy and ROC-AUC metrics |
| `statistical_testing` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | Significance testing details omitted |
| `calibration_metrics` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | ECE omitted |
| `computational_reporting` | `LIMITED` | REVIEWER_INFERRED | PAPER_FULLTEXT | Mentions GCN efficiency; scaling bounds omitted |

---

# 4. Quality Scoring (QA1–QA8)

| QA Criterion | Score (0-2) | Justification |
|---|---|---|
| **QA1 Task Clarity** | 2 | Clear formulation of joint exercise/concept GCN for knowledge tracing. |
| **QA2 Data Transparency** | 2 | Evaluates on 4 benchmark datasets (ASSIST09, ASSIST12, Statics11, KDD Cup 2010). |
| **QA3 Split/Leakage Transparency** | 1 | Split reported; precomputed joint graph train-only isolation unverified. |
| **QA4 Baseline/Ablation Adequacy** | 2 | Evaluates against DKT, DKVMN, EKT, SAKT and performs graph component ablation. |
| **QA5 Statistical Uncertainty** | 1 | Reports mean performance across seeds; formal significance testing omitted. |
| **QA6 Author Artifacts** | 1 | Official journal full text verified; official repository unverified. |
| **QA7 Sparse Construct Validity** | 1 | Motivates model via multi-relationship representation, but lacks isolated zero-exposure KC cold-start protocol. |
| **QA8 Computational Transparency** | 1 | Describes GCN layer formulation; formal runtime scaling bounds omitted. |

**Raw Quality Score:** 11 / 16  
**Normalized Quality:** 0.6875 (**MODERATE Quality**)
