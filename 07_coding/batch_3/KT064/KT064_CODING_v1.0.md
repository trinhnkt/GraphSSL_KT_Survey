# KT064 — Multi-Granularity Ensemble Graph Coding Record (v1.0 LOCKED)

**Paper ID:** PAPER_KT064  
**Legacy ID:** KT064  
**Title:** Multi-Granularity Ensemble Interaction Graph Modeling for Knowledge Tracing  
**Authors:** Jing Wang, Huifang Ma, Mengyuan Zhang, Lei Zhang, Liang Chang  
**Venue:** Knowledge-Based Systems, Vol. 309, Article 112834, Jan. 2025  
**DOI:** 10.1016/j.knosys.2024.112834  
**arXiv ID:** NR  
**Coder:** AI_ASSISTED (Antigravity Research-Engineering Assistant)  
**Codebook Version:** `coding_codebook_v1.0_LOCKED.md`  
**Date:** 2026-08-26  

---

# 1. PAPER Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `paper_id` | `PAPER_KT064` | AUTHOR_STATED | PUBLISHER_METADATA | KBS 2025 |
| `legacy_id` | `KT064` | AUTHOR_STATED | METADATA | Seed corpus identifier |
| `title` | Multi-Granularity Ensemble Interaction Graph Modeling for Knowledge Tracing | AUTHOR_STATED | PUBLISHER_METADATA | Article title |
| `publication_year` | 2025 | AUTHOR_STATED | PUBLISHER_METADATA | KBS Vol. 309 published Jan 2025 |
| `venue` | Knowledge-Based Systems | AUTHOR_STATED | PUBLISHER_METADATA | Elsevier peer-reviewed journal |
| `publication_type` | `JOURNAL_ARTICLE` | AUTHOR_STATED | PUBLISHER_METADATA | Full journal article |
| `peer_reviewed` | `YES` | AUTHOR_STATED | PUBLISHER_METADATA | Official journal publication |
| `doi` | 10.1016/j.knosys.2024.112834 | AUTHOR_STATED | PUBLISHER_METADATA | Official DOI |
| `arxiv_id` | `NR` | AUTHOR_STATED | PUBLISHER_METADATA | Direct journal article |
| `kt_central_task` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Sequential student performance prediction & multi-granularity interaction graph modeling |
| `G_criterion` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Multi-granularity ensemble interaction graph modeling with GNN |
| `S_criterion` | `NO` | AUTHOR_STATED | PAPER_FULLTEXT | Supervised ensemble prediction loss only |
| `corpus_tier` | `PRIMARY_CORE` | REVIEWER_INFERRED | PAPER_FULLTEXT | Satisfies G-criterion (`PRIMARY_CORE`) |
| `coding_completeness` | `FULLTEXT_CODED` | REVIEWER_INFERRED | PAPER_FULLTEXT | Peer-reviewed journal full text inspected |
| `third_party_implementation_available` | `YES` | METADATA | SECONDARY | Tracked in pyKT / KT benchmark repositories |

---

# 2. MODEL Level Coding (`MODEL_KT064_MG_ENSEMBLE`)

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `model_id` | `MODEL_KT064_MG_ENSEMBLE` | AUTHOR_STATED | PAPER_FULLTEXT | Primary Multi-Granularity Ensemble Graph KT formulation |
| `graph_source` | `Q_MATRIX, SEQUENTIAL_TRANSITION, CO_OCCURRENCE` | AUTHOR_STATED | PAPER_FULLTEXT | Multi-granularity interaction graphs constructed across fine-grained exercises and coarse-grained concepts |
| `graph_provenance` | `JOINTLY_LEARNED_TRAINING` | AUTHOR_STATED | PAPER_FULLTEXT | Multi-granularity graph node embeddings and edge transitions updated during training |
| `graph_leakage_risk` | `LOW` | REVIEWER_INFERRED | PAPER_FULLTEXT | Multi-granularity graph transitions strictly preserve interaction sequence timestamps |
| `graph_representation` | `HIERARCHICAL, MULTI_RELATIONAL, ITEM_KC_BIPARTITE` | AUTHOR_STATED | PAPER_FULLTEXT | Multi-granularity ensemble graphs capturing exercise-level and concept-level interaction dynamics |
| `directed` | `Y` | AUTHOR_STATED | PAPER_FULLTEXT | Directed interaction transition links |
| `typed_edges` | `Y` | AUTHOR_STATED | PAPER_FULLTEXT | Multiple relation types across granularity levels |
| `gnn_encoder` | `GRAPH_CONVOLUTIONAL_NETWORK` | AUTHOR_STATED | PAPER_FULLTEXT | Multi-granularity Graph Convolutional Network encoder |
| `temporal_backbone` | `RNN_LSTM_GRU` | AUTHOR_STATED | PAPER_FULLTEXT | GRU sequence backbone for temporal state tracking |
| `fusion_type` | `ENSEMBLE_WEIGHTING, ATTENTION` | AUTHOR_STATED | PAPER_FULLTEXT | Multi-granularity attentive ensemble fusion combining exercise-level and concept-level graph representations |
| `fusion_location` | `HIDDEN_STATE, PREDICTION` | AUTHOR_STATED | PAPER_FULLTEXT | Sequence hidden state and final performance prediction layers |
| `ssl_family` | `NONE` | AUTHOR_STATED | PAPER_FULLTEXT | Supervised prediction loss only |
| `augmentation_type` | `NO_EXPLICIT_AUGMENTATION` | AUTHOR_STATED | PAPER_FULLTEXT | No data augmentation |
| `educational_structure_preservation` | `YES_EXPLICIT` | AUTHOR_STATED | PAPER_FULLTEXT | Preserves fine-grained question structure and coarse-grained concept hierarchy |

---

# 3. EXPERIMENT Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `experiment_id` | `EXP_KT064_MAIN` | AUTHOR_STATED | PAPER_FULLTEXT | Main experimental evaluation |
| `datasets` | ASSISTments2009, ASSISTments2017, Statics2011, Junyi | AUTHOR_STATED | PAPER_FULLTEXT | 4 public benchmark educational datasets evaluated |
| `split_type` | `LEARNER_BASED` | AUTHOR_STATED | PAPER_FULLTEXT | Learner history partition into train/test splits |
| `n_seeds` | 5 | AUTHOR_STATED | PAPER_FULLTEXT | Performance averaged over 5 random seeds (CB13) |
| `resampling_repeats` | 1 | REVIEWER_INFERRED | PAPER_FULLTEXT | Single train/test data split repeated across seeds (CB13) |
| `repeated_run_unit` | `SEED_REPETITION` | REVIEWER_INFERRED | PAPER_FULLTEXT | Seed repetition unit (CB13) |
| `sparse_concept_ontology` | `GENERIC_DATA_SPARSITY` | REVIEWER_INFERRED | PAPER_FULLTEXT | Evaluates multi-granularity ensemble graph modeling under interaction data sparsity |
| `metrics` | ROC-AUC, ACC | AUTHOR_STATED | PAPER_FULLTEXT | Prediction accuracy and ROC-AUC metrics |
| `statistical_testing` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | Significance tests omitted |
| `calibration_metrics` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | ECE omitted |
| `computational_reporting` | `YES_FULL` | AUTHOR_STATED | PAPER_FULLTEXT | Reports formal multi-granularity GNN time/memory complexity and empirical runtime curves |

---

# 4. Quality Scoring (QA1–QA8)

| QA Criterion | Score (0-2) | Justification |
|---|---|---|
| **QA1 Task Clarity** | 2 | Clear formulation of multi-granularity ensemble interaction graph modeling for KT. |
| **QA2 Data Transparency** | 2 | Evaluates on 4 public benchmark datasets (ASSIST09, ASSIST17, Statics11, Junyi). |
| **QA3 Split/Leakage Transparency** | 2 | Multi-granularity graph transitions strictly respect interaction sequence timestamps; low leakage risk. |
| **QA4 Baseline/Ablation Adequacy** | 2 | Evaluates against DKT, SAKT, GKT, GIKT and performs granularity level ablation. |
| **QA5 Statistical Uncertainty** | 1 | Reports mean performance across seeds; formal significance testing omitted. |
| **QA6 Author Artifacts** | 1 | Official journal full text verified; author code repository unverified. |
| **QA7 Sparse Construct Validity** | 1 | Motivates model via multi-granularity representation under sparse data, but lacks zero-exposure cold-start KC evaluation. |
| **QA8 Computational Transparency** | 2 | Reports formal time/memory complexity of multi-granularity GNN layers. |

**Raw Quality Score:** 13 / 16  
**Normalized Quality:** 0.8125 (**HIGH Quality**)
