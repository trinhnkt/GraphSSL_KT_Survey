# KT029 — DGEKT Coding Record (v1.0 LOCKED)

**Paper ID:** PAPER_KT029  
**Legacy ID:** KT029  
**Title:** DGEKT: A Dual Graph Ensemble Learning Method for Knowledge Tracing  
**Authors:** Chaoran Cui, Yumo Yao, Chunyun Zhang, Hebo Ma, Yuling Ma, Zhaochun Ren, Chen Zhang, James Ko  
**Venue:** ACM Transactions on Information Systems (TOIS), Vol. 42, Issue 3, Art. 78, pp. 1–24, Jan. 2024  
**DOI:** 10.1145/3635303  
**arXiv ID:** NR  
**Coder:** AI_ASSISTED (Antigravity Research-Engineering Assistant)  
**Codebook Version:** `coding_codebook_v1.0_LOCKED.md`  
**Date:** 2026-08-26  

---

# 1. PAPER Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `paper_id` | `PAPER_KT029` | AUTHOR_STATED | PUBLISHER_METADATA | ACM TOIS 2024 |
| `legacy_id` | `KT029` | AUTHOR_STATED | METADATA | Seed corpus identifier |
| `title` | DGEKT: A Dual Graph Ensemble Learning Method for Knowledge Tracing | AUTHOR_STATED | PUBLISHER_METADATA | Published article title |
| `publication_year` | 2024 | AUTHOR_STATED | PUBLISHER_METADATA | TOIS Vol. 42 published Jan 2024 |
| `venue` | ACM Transactions on Information Systems | AUTHOR_STATED | PUBLISHER_METADATA | ACM peer-reviewed journal |
| `publication_type` | `JOURNAL_ARTICLE` | AUTHOR_STATED | PUBLISHER_METADATA | Full journal article |
| `peer_reviewed` | `YES` | AUTHOR_STATED | PUBLISHER_METADATA | Official ACM journal publication |
| `doi` | 10.1145/3635303 | AUTHOR_STATED | PUBLISHER_METADATA | Official ACM DOI |
| `arxiv_id` | `NR` | AUTHOR_STATED | PUBLISHER_METADATA | Direct journal article |
| `kt_central_task` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Sequential student performance prediction & knowledge tracing |
| `G_criterion` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Dual graph ensemble GNN architecture (static concept graph + dynamic interaction graph) |
| `S_criterion` | `NO` | AUTHOR_STATED | PAPER_FULLTEXT | Supervised ensemble prediction loss only |
| `corpus_tier` | `PRIMARY_CORE` | REVIEWER_INFERRED | PAPER_FULLTEXT | Satisfies G-criterion (`PRIMARY_CORE`) |
| `coding_completeness` | `FULLTEXT_CODED` | REVIEWER_INFERRED | PAPER_FULLTEXT | Peer-reviewed ACM journal full text inspected |
| `third_party_implementation_available` | `YES` | METADATA | SECONDARY | Tracked in pyKT / KT benchmark repositories |

---

# 2. MODEL Level Coding (`MODEL_KT029_DGEKT`)

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `model_id` | `MODEL_KT029_DGEKT` | AUTHOR_STATED | PAPER_FULLTEXT | Primary DGEKT model formulation |
| `graph_source` | `Q_MATRIX, CO_OCCURRENCE, SEQUENTIAL_TRANSITION` | AUTHOR_STATED | PAPER_FULLTEXT | Dual graphs derived from Q-matrix static structure and dynamic interaction transitions |
| `graph_provenance` | `JOINTLY_LEARNED_TRAINING` | AUTHOR_STATED | PAPER_FULLTEXT | Dynamic transition graph updated alongside static concept graph during training |
| `graph_leakage_risk` | `LOW` | REVIEWER_INFERRED | PAPER_FULLTEXT | Dynamic transition graph updates strictly preserve interaction sequence timestamps |
| `graph_representation` | `DUAL_GRAPH, ITEM_KC_BIPARTITE, DYNAMIC_TEMPORAL` | AUTHOR_STATED | PAPER_FULLTEXT | Dual graph representations coupling static concept domain and dynamic interaction history |
| `directed` | `Y` | AUTHOR_STATED | PAPER_FULLTEXT | Directed dynamic interaction transition edges |
| `typed_edges` | `Y` | AUTHOR_STATED | PAPER_FULLTEXT | Multiple relation types across dual graphs |
| `gnn_encoder` | `GRAPH_CONVOLUTIONAL_NETWORK` | AUTHOR_STATED | PAPER_FULLTEXT | Dual GCN encoders processing static and dynamic graph structures |
| `temporal_backbone` | `RNN_LSTM_GRU` | AUTHOR_STATED | PAPER_FULLTEXT | GRU sequence backbone for temporal state tracking |
| `fusion_type` | `ENSEMBLE_WEIGHTING, CONCAT` | AUTHOR_STATED | PAPER_FULLTEXT | Dual graph ensemble weighting fusing static and dynamic graph representations |
| `fusion_location` | `HIDDEN_STATE, PREDICTION` | AUTHOR_STATED | PAPER_FULLTEXT | Injected at recurrent sequence hidden state and output prediction layers |
| `ssl_family` | `NONE` | AUTHOR_STATED | PAPER_FULLTEXT | Supervised prediction loss only |
| `augmentation_type` | `NO_EXPLICIT_AUGMENTATION` | AUTHOR_STATED | PAPER_FULLTEXT | No data augmentation |
| `educational_structure_preservation` | `YES_EXPLICIT` | AUTHOR_STATED | PAPER_FULLTEXT | Preserves static domain structure and dynamic interaction transition constraints |

---

# 3. EXPERIMENT Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `experiment_id` | `EXP_KT029_MAIN` | AUTHOR_STATED | PAPER_FULLTEXT | Main experimental evaluation |
| `datasets` | ASSISTments2009, ASSISTments2017, Junyi, Statics2011 | AUTHOR_STATED | PAPER_FULLTEXT | 4 public benchmark educational datasets evaluated |
| `split_type` | `LEARNER_BASED` | AUTHOR_STATED | PAPER_FULLTEXT | Learner history partition into train/test splits |
| `n_seeds` | 5 | AUTHOR_STATED | PAPER_FULLTEXT | Performance averaged over 5 random seeds (CB13) |
| `resampling_repeats` | 1 | REVIEWER_INFERRED | PAPER_FULLTEXT | Single train/test data split repeated across seeds (CB13) |
| `repeated_run_unit` | `SEED_REPETITION` | REVIEWER_INFERRED | PAPER_FULLTEXT | Seed repetition unit (CB13) |
| `sparse_concept_ontology` | `GENERIC_DATA_SPARSITY` | REVIEWER_INFERRED | PAPER_FULLTEXT | Evaluates dual graph ensemble modeling under sparse interaction conditions |
| `metrics` | ROC-AUC, ACC | AUTHOR_STATED | PAPER_FULLTEXT | Prediction accuracy and ROC-AUC metrics |
| `statistical_testing` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | Significance testing details omitted |
| `calibration_metrics` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | ECE omitted |
| `computational_reporting` | `YES_FULL` | AUTHOR_STATED | PAPER_FULLTEXT | Reports formal dual graph GCN time/memory complexity and empirical scaling curves |

---

# 4. Quality Scoring (QA1–QA8)

| QA Criterion | Score (0-2) | Justification |
|---|---|---|
| **QA1 Task Clarity** | 2 | Clear formulation of dual graph ensemble learning for knowledge tracing. |
| **QA2 Data Transparency** | 2 | Evaluates on 4 public benchmark datasets (ASSIST09, ASSIST17, Junyi, Statics11). |
| **QA3 Split/Leakage Transparency** | 2 | Dynamic graph updates strictly preserve interaction sequence timestamps; low leakage risk. |
| **QA4 Baseline/Ablation Adequacy** | 2 | Evaluates against DKT, SAKT, GKT, GIKT and performs dual graph component ablation. |
| **QA5 Statistical Uncertainty** | 1 | Reports mean performance across seeds; formal significance testing omitted. |
| **QA6 Author Artifacts** | 1 | Official ACM TOIS journal full text verified; author code repository unverified. |
| **QA7 Sparse Construct Validity** | 1 | Motivates model via dual graph ensemble under sparse data, but lacks zero-exposure cold-start KC evaluation. |
| **QA8 Computational Transparency** | 2 | Reports formal time/memory complexity of dual graph GCN operations. |

**Raw Quality Score:** 13 / 16  
**Normalized Quality:** 0.8125 (**HIGH Quality**)
