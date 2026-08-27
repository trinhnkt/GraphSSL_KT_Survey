# KT052 — Multi-Hierarchical Capsule GNN Coding Record (v1.0 LOCKED)

**Paper ID:** PAPER_KT052  
**Legacy ID:** KT052  
**Title:** Modeling Knowledge Proficiency Using Multi-Hierarchical Capsule Graph Neural Network  
**Authors:** Zeyu He, Li Wang, Yonghong Yan  
**Venue:** Applied Intelligence, Vol. 52, Issue 7, pp. 7230–7247, May 2022  
**DOI:** 10.1007/s10489-021-02765-w  
**arXiv ID:** NR  
**Coder:** AI_ASSISTED (Antigravity Research-Engineering Assistant)  
**Codebook Version:** `coding_codebook_v1.0_LOCKED.md`  
**Date:** 2026-08-26  

---

# 1. PAPER Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `paper_id` | `PAPER_KT052` | AUTHOR_STATED | PUBLISHER_METADATA | Applied Intelligence 2022 |
| `legacy_id` | `KT052` | AUTHOR_STATED | METADATA | Seed corpus identifier |
| `title` | Modeling Knowledge Proficiency Using Multi-Hierarchical Capsule Graph Neural Network | AUTHOR_STATED | PUBLISHER_METADATA | Article title |
| `publication_year` | 2022 | AUTHOR_STATED | PUBLISHER_METADATA | Published May 2022 |
| `venue` | Applied Intelligence | AUTHOR_STATED | PUBLISHER_METADATA | Springer peer-reviewed journal |
| `publication_type` | `JOURNAL_ARTICLE` | AUTHOR_STATED | PUBLISHER_METADATA | Full journal article |
| `peer_reviewed` | `YES` | AUTHOR_STATED | PUBLISHER_METADATA | Official journal publication |
| `doi` | 10.1007/s10489-021-02765-w | AUTHOR_STATED | PUBLISHER_METADATA | Official DOI |
| `arxiv_id` | `NR` | AUTHOR_STATED | PUBLISHER_METADATA | Direct journal article |
| `kt_central_task` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Sequential student response prediction & knowledge proficiency modeling |
| `G_criterion` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Multi-hierarchical capsule graph neural network over concept/exercise structures |
| `S_criterion` | `NO` | AUTHOR_STATED | PAPER_FULLTEXT | Supervised prediction loss only |
| `corpus_tier` | `PRIMARY_CORE` | REVIEWER_INFERRED | PAPER_FULLTEXT | Satisfies G-criterion (`PRIMARY_CORE`) |
| `coding_completeness` | `FULLTEXT_CODED` | REVIEWER_INFERRED | PAPER_FULLTEXT | Peer-reviewed journal full text inspected |
| `third_party_implementation_available` | `YES` | METADATA | SECONDARY | Tracked in pyKT / KT benchmark repositories |

---

# 2. MODEL Level Coding (`MODEL_KT052_CAPSULE_GNN`)

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `model_id` | `MODEL_KT052_CAPSULE_GNN` | AUTHOR_STATED | PAPER_FULLTEXT | Primary Capsule GNN KT model formulation |
| `graph_source` | `CURRICULUM_CONCEPT_MAP, Q_MATRIX` | AUTHOR_STATED | PAPER_FULLTEXT | Multi-hierarchical concept graph constructed from domain structure and Q-matrix |
| `graph_provenance` | `EXTERNAL_FIXED` | AUTHOR_STATED | PAPER_FULLTEXT | Domain multi-hierarchical structure supplied externally |
| `graph_leakage_risk` | `LOW` | REVIEWER_INFERRED | PAPER_FULLTEXT | External pedagogical graph fixed independently of test response splits |
| `graph_representation` | `HIERARCHICAL, KC_KC` | AUTHOR_STATED | PAPER_FULLTEXT | Multi-hierarchical concept graph structure |
| `directed` | `Y` | AUTHOR_STATED | PAPER_FULLTEXT | Directed hierarchical parent-child relations |
| `typed_edges` | `Y` | AUTHOR_STATED | PAPER_FULLTEXT | Multiple hierarchical relation levels |
| `gnn_encoder` | `GRAPH_ATTENTION_HYBRID` | AUTHOR_STATED | PAPER_FULLTEXT | Capsule Graph Neural Network encoder with routing attention |
| `temporal_backbone` | `RNN_LSTM_GRU` | AUTHOR_STATED | PAPER_FULLTEXT | LSTM sequence layer for learner state tracing |
| `fusion_type` | `CONCAT, ATTENTION` | AUTHOR_STATED | PAPER_FULLTEXT | Fuses capsule graph embeddings into temporal sequence processing |
| `fusion_location` | `INPUT, HIDDEN_STATE` | AUTHOR_STATED | PAPER_FULLTEXT | Injected at input and sequence hidden state layers |
| `ssl_family` | `NONE` | AUTHOR_STATED | PAPER_FULLTEXT | Supervised prediction loss only |
| `augmentation_type` | `NO_EXPLICIT_AUGMENTATION` | AUTHOR_STATED | PAPER_FULLTEXT | No data augmentation |
| `educational_structure_preservation` | `YES_EXPLICIT` | AUTHOR_STATED | PAPER_FULLTEXT | Preserves multi-hierarchical concept dependency structures |

---

# 3. EXPERIMENT Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `experiment_id` | `EXP_KT052_MAIN` | AUTHOR_STATED | PAPER_FULLTEXT | Main experimental evaluation |
| `datasets` | ASSISTments2009, ASSISTments2015, Statics2011 | AUTHOR_STATED | PAPER_FULLTEXT | Benchmark educational datasets evaluated |
| `split_type` | `LEARNER_BASED` | AUTHOR_STATED | PAPER_FULLTEXT | Student history partition into train/test splits |
| `n_seeds` | 5 | AUTHOR_STATED | PAPER_FULLTEXT | Performance averaged over 5 random seeds (CB13) |
| `resampling_repeats` | 1 | REVIEWER_INFERRED | PAPER_FULLTEXT | Single data split repeated across model seeds (CB13) |
| `repeated_run_unit` | `SEED_REPETITION` | REVIEWER_INFERRED | PAPER_FULLTEXT | Seed repetition unit (CB13) |
| `sparse_concept_ontology` | `GENERIC_DATA_SPARSITY` | REVIEWER_INFERRED | PAPER_FULLTEXT | Evaluates hierarchical capsule GNN on interaction datasets |
| `metrics` | ROC-AUC, ACC | AUTHOR_STATED | PAPER_FULLTEXT | Prediction accuracy and ROC-AUC metrics |
| `statistical_testing` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | Significance tests omitted |
| `calibration_metrics` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | ECE omitted |
| `computational_reporting` | `LIMITED` | REVIEWER_INFERRED | PAPER_FULLTEXT | Scaling bounds omitted |

---

# 4. Quality Scoring (QA1–QA8)

| QA Criterion | Score (0-2) | Justification |
|---|---|---|
| **QA1 Task Clarity** | 2 | Clear formulation of multi-hierarchical capsule GNN for knowledge tracing. |
| **QA2 Data Transparency** | 2 | Evaluates on public benchmark datasets (ASSIST09, ASSIST15, Statics11). |
| **QA3 Split/Leakage Transparency** | 2 | External fixed hierarchical graph independent of test split; low leakage risk. |
| **QA4 Baseline/Ablation Adequacy** | 2 | Evaluates against DKT, DKVMN, SAKT, GKT and performs capsule routing ablation. |
| **QA5 Statistical Uncertainty** | 1 | Reports mean performance across seeds; formal significance testing omitted. |
| **QA6 Author Artifacts** | 1 | Official journal full text verified; author code repository unverified. |
| **QA7 Sparse Construct Validity** | 1 | Motivates model via multi-hierarchical representation, but lacks zero-exposure cold-start KC evaluation. |
| **QA8 Computational Transparency** | 1 | Describes capsule routing complexity; formal runtime scaling bounds omitted. |

**Raw Quality Score:** 12 / 16  
**Normalized Quality:** 0.7500 (**MODERATE Quality**)
