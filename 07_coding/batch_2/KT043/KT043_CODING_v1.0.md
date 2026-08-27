# KT043 — Three-View Contrastive Graph KT Coding Record (v1.0 LOCKED)

**Paper ID:** PAPER_KT043  
**Legacy ID:** KT043  
**Title:** Weighted Heterogeneous Graph-Based Three-View Contrastive Learning for Knowledge Tracing  
**Authors:** Jianwen Sun, Shangheng Du, Zhi Liu, Fenghua Yu, Sannyuya Liu, Xiaoxuan Shen  
**Venue:** IEEE Transactions on Consumer Electronics (TCE), Vol. 70, Issue 1, pp. 2838–2847, Feb. 2024  
**DOI:** 10.1109/TCE.2023.3293953  
**arXiv ID:** NR  
**Coder:** AI_ASSISTED (Antigravity Research-Engineering Assistant)  
**Codebook Version:** `coding_codebook_v1.0_LOCKED.md`  
**Date:** 2026-08-26  

---

# 1. PAPER Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `paper_id` | `PAPER_KT043` | AUTHOR_STATED | PUBLISHER_METADATA | IEEE TCE 2024 |
| `legacy_id` | `KT043` | AUTHOR_STATED | METADATA | Seed corpus identifier |
| `title` | Weighted Heterogeneous Graph-Based Three-View Contrastive Learning for Knowledge Tracing | AUTHOR_STATED | PUBLISHER_METADATA | Article title |
| `publication_year` | 2024 | AUTHOR_STATED | PUBLISHER_METADATA | Published Feb 2024 |
| `venue` | IEEE Transactions on Consumer Electronics | AUTHOR_STATED | PUBLISHER_METADATA | IEEE peer-reviewed journal |
| `publication_type` | `JOURNAL_ARTICLE` | AUTHOR_STATED | PUBLISHER_METADATA | Full journal article |
| `peer_reviewed` | `YES` | AUTHOR_STATED | PUBLISHER_METADATA | Official IEEE journal publication |
| `doi` | 10.1109/TCE.2023.3293953 | AUTHOR_STATED | PUBLISHER_METADATA | Official IEEE DOI |
| `arxiv_id` | `NR` | AUTHOR_STATED | PUBLISHER_METADATA | Direct IEEE journal article |
| `kt_central_task` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Sequential learner performance prediction & knowledge tracing |
| `G_criterion` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Weighted heterogeneous concept-exercise graph with GNN encoder |
| `S_criterion` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Three-view self-supervised contrastive learning pretext task |
| `corpus_tier` | `PRIMARY_CORE` | REVIEWER_INFERRED | PAPER_FULLTEXT | Satisfies both G-criterion and S-criterion (`PRIMARY_CORE`) |
| `coding_completeness` | `FULLTEXT_CODED` | REVIEWER_INFERRED | PAPER_FULLTEXT | Peer-reviewed IEEE journal text fully inspected |
| `third_party_implementation_available` | `YES` | METADATA | SECONDARY | Tracked in pyKT / KT benchmark repositories |

---

# 2. MODEL Level Coding (`MODEL_KT043_3V_CLKT`)

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `model_id` | `MODEL_KT043_3V_CLKT` | AUTHOR_STATED | PAPER_FULLTEXT | Primary Three-View Contrastive Graph KT formulation |
| `graph_source` | `Q_MATRIX, CO_OCCURRENCE, SIMILARITY` | AUTHOR_STATED | PAPER_FULLTEXT | Weighted heterogeneous graph constructed from Q-matrix, exercise co-occurrence, and concept similarity |
| `graph_provenance` | `PRECOMPUTED_UNCLEAR_SPLIT` | REVIEWER_INFERRED | PAPER_FULLTEXT | Precomputed weighted graph adjacency prior to contrastive training |
| `graph_leakage_risk` | `POTENTIAL` | REVIEWER_INFERRED | PAPER_FULLTEXT | Precomputed co-occurrence edge weights without explicit train-only split reporting |
| `graph_representation` | `HETEROGENEOUS_MULTI_NODE, ITEM_KC_BIPARTITE` | AUTHOR_STATED | PAPER_FULLTEXT | Weighted heterogeneous graph connecting questions and concepts across three views |
| `directed` | `N` | AUTHOR_STATED | PAPER_FULLTEXT | Undirected weighted heterogeneous graph adjacency |
| `typed_edges` | `Y` | AUTHOR_STATED | PAPER_FULLTEXT | Multiple relation categories across heterogeneous graph views |
| `gnn_encoder` | `HETEROGENEOUS_GNN` | AUTHOR_STATED | PAPER_FULLTEXT | Heterogeneous Graph Convolutional Network encoder |
| `temporal_backbone` | `RNN_LSTM_GRU` | AUTHOR_STATED | PAPER_FULLTEXT | GRU sequence backbone for learner state tracking |
| `fusion_type` | `ATTENTION, JOINT_LATENT_STATE` | AUTHOR_STATED | PAPER_FULLTEXT | Multi-view attentive fusion combining graph views and temporal states |
| `fusion_location` | `HIDDEN_STATE, AUXILIARY_LOSS` | AUTHOR_STATED | PAPER_FULLTEXT | Hidden state sequence layer and three-view contrastive loss optimization |
| `ssl_family` | `MULTIVIEW_CONTRASTIVE, GRAPH_CONTRASTIVE` | AUTHOR_STATED | PAPER_FULLTEXT | Three-view contrastive loss over global graph view, local graph view, and sequence view |
| `augmentation_type` | `NODE_MASK, EDGE_REWEIGHT, SUBGRAPH_SAMPLE` | AUTHOR_STATED | PAPER_FULLTEXT | Multi-view graph perturbation and edge reweighting |
| `educational_structure_preservation` | `YES_EXPLICIT` | AUTHOR_STATED | PAPER_FULLTEXT | Preserves weighted question-concept semantics across multi-view contrastive losses |

---

# 3. EXPERIMENT Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `experiment_id` | `EXP_KT043_MAIN` | AUTHOR_STATED | PAPER_FULLTEXT | Main experimental evaluation |
| `datasets` | ASSISTments2009, ASSISTments2017, Statics2011 | AUTHOR_STATED | PAPER_FULLTEXT | Public benchmark educational datasets evaluated |
| `split_type` | `LEARNER_BASED` | AUTHOR_STATED | PAPER_FULLTEXT | Learner history partition into train/test splits |
| `n_seeds` | 5 | AUTHOR_STATED | PAPER_FULLTEXT | Performance averaged over 5 random seeds (CB13) |
| `resampling_repeats` | 1 | REVIEWER_INFERRED | PAPER_FULLTEXT | Single data split repeated across model seeds (CB13) |
| `repeated_run_unit` | `SEED_REPETITION` | REVIEWER_INFERRED | PAPER_FULLTEXT | Seed repetition unit (CB13) |
| `sparse_concept_ontology` | `GENERIC_DATA_SPARSITY` | REVIEWER_INFERRED | PAPER_FULLTEXT | Evaluates three-view contrastive learning under sparse interaction conditions |
| `metrics` | ROC-AUC, ACC | AUTHOR_STATED | PAPER_FULLTEXT | Prediction accuracy and ROC-AUC metrics |
| `statistical_testing` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | Significance tests omitted |
| `calibration_metrics` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | ECE omitted |
| `computational_reporting` | `LIMITED` | REVIEWER_INFERRED | PAPER_FULLTEXT | Scaling bounds omitted |

---

# 4. Quality Scoring (QA1–QA8)

| QA Criterion | Score (0-2) | Justification |
|---|---|---|
| **QA1 Task Clarity** | 2 | Clear formulation of three-view contrastive graph learning for KT. |
| **QA2 Data Transparency** | 2 | Evaluates on public benchmark datasets (ASSIST09, ASSIST17, Statics11). |
| **QA3 Split/Leakage Transparency** | 1 | Train/test split reported; precomputed weighted graph train-only isolation unverified. |
| **QA4 Baseline/Ablation Adequacy** | 2 | Evaluates against DKT, SAKT, CL4KT, Bi-CLKT and performs three-view contrastive ablation. |
| **QA5 Statistical Uncertainty** | 1 | Reports mean performance across seeds; formal significance testing omitted. |
| **QA6 Author Artifacts** | 1 | Official IEEE journal full text verified; author code repository unverified. |
| **QA7 Sparse Construct Validity** | 1 | Motivates model via multi-view representation under sparse data, but lacks zero-exposure cold-start KC evaluation. |
| **QA8 Computational Transparency** | 1 | Explains three-view contrastive loss complexity; formal runtime scaling bounds omitted. |

**Raw Quality Score:** 11 / 16  
**Normalized Quality:** 0.6875 (**MODERATE Quality**)
