# KT050 — GraphCA Coding Record (v1.0 LOCKED)

**Paper ID:** PAPER_KT050  
**Legacy ID:** KT050  
**Title:** GraphCA: Learning from Graph Counterfactual Augmentation for Knowledge Tracing  
**Authors:** Xinhua Wang, Shasha Zhao, Lei Guo, Lei Zhu, Chaoran Cui, Liancheng Xu  
**Venue:** IEEE/CAA Journal of Automatica Sinica, Vol. 10, Issue 11, pp. 2108–2123, Nov. 2023  
**DOI:** 10.1109/JAS.2023.123678  
**arXiv ID:** NR  
**Coder:** AI_ASSISTED (Antigravity Research-Engineering Assistant)  
**Codebook Version:** `coding_codebook_v1.0_LOCKED.md`  
**Date:** 2026-08-26  

---

# 1. PAPER Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `paper_id` | `PAPER_KT050` | AUTHOR_STATED | PUBLISHER_METADATA | IEEE JAS 2023 |
| `legacy_id` | `KT050` | AUTHOR_STATED | METADATA | Seed corpus identifier |
| `title` | GraphCA: Learning from Graph Counterfactual Augmentation for Knowledge Tracing | AUTHOR_STATED | PUBLISHER_METADATA | Published IEEE article title |
| `publication_year` | 2023 | AUTHOR_STATED | PUBLISHER_METADATA | Published Nov 2023 |
| `venue` | IEEE/CAA Journal of Automatica Sinica | AUTHOR_STATED | PUBLISHER_METADATA | IEEE peer-reviewed journal |
| `publication_type` | `JOURNAL_ARTICLE` | AUTHOR_STATED | PUBLISHER_METADATA | Full journal article |
| `peer_reviewed` | `YES` | AUTHOR_STATED | PUBLISHER_METADATA | Official IEEE journal publication |
| `doi` | 10.1109/JAS.2023.123678 | AUTHOR_STATED | PUBLISHER_METADATA | Official IEEE DOI |
| `arxiv_id` | `NR` | AUTHOR_STATED | PUBLISHER_METADATA | Direct journal publication |
| `kt_central_task` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Sequential student performance prediction & knowledge tracing |
| `G_criterion` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Heterogeneous Graph Convolutional Network over student-question-concept nodes |
| `S_criterion` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Self-supervised contrastive learning with graph counterfactual augmentation |
| `corpus_tier` | `PRIMARY_CORE` | REVIEWER_INFERRED | PAPER_FULLTEXT | Satisfies both G-criterion and S-criterion (`PRIMARY_CORE`) |
| `coding_completeness` | `FULLTEXT_CODED` | REVIEWER_INFERRED | PAPER_FULLTEXT | Peer-reviewed IEEE journal text fully inspected |
| `third_party_implementation_available` | `YES` | METADATA | SECONDARY | Tracked in pyKT / KT benchmark repositories |

---

# 2. MODEL Level Coding (`MODEL_KT050_GraphCA`)

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `model_id` | `MODEL_KT050_GraphCA` | AUTHOR_STATED | PAPER_FULLTEXT | Primary GraphCA model formulation |
| `graph_source` | `Q_MATRIX, LEARNED_FROM_INTERACTIONS` | AUTHOR_STATED | PAPER_FULLTEXT | Heterogeneous graph connecting student, question, and concept nodes |
| `graph_provenance` | `JOINTLY_LEARNED_TRAINING` | AUTHOR_STATED | PAPER_FULLTEXT | Heterogeneous graph nodes and counterfactual graph edges updated during training |
| `graph_leakage_risk` | `LOW` | REVIEWER_INFERRED | PAPER_FULLTEXT | Counterfactual graph transformations strictly preserve interaction sequence timestamps |
| `graph_representation` | `HETEROGENEOUS_MULTI_NODE, LEARNER_ITEM, ITEM_KC_BIPARTITE` | AUTHOR_STATED | PAPER_FULLTEXT | Heterogeneous graph connecting learners, items, and concepts |
| `directed` | `Y` | AUTHOR_STATED | PAPER_FULLTEXT | Directed counterfactual propagation links |
| `typed_edges` | `Y` | AUTHOR_STATED | PAPER_FULLTEXT | Multiple relation types across heterogeneous nodes |
| `gnn_encoder` | `HETEROGENEOUS_GNN` | AUTHOR_STATED | PAPER_FULLTEXT | Heterogeneous Graph Convolutional Network encoder |
| `temporal_backbone` | `RNN_LSTM_GRU` | AUTHOR_STATED | PAPER_FULLTEXT | GRU sequence backbone for learner state tracking |
| `fusion_type` | `JOINT_LATENT_STATE, ATTENTION` | AUTHOR_STATED | PAPER_FULLTEXT | Fuses counterfactual graph embeddings with temporal GRU states |
| `fusion_location` | `HIDDEN_STATE, AUXILIARY_LOSS` | AUTHOR_STATED | PAPER_FULLTEXT | Sequence hidden state and counterfactual contrastive loss layers |
| `ssl_family` | `GRAPH_CONTRASTIVE, MULTIVIEW_CONTRASTIVE` | AUTHOR_STATED | PAPER_FULLTEXT | Graph counterfactual contrastive learning loss between factual and counterfactual views |
| `augmentation_type` | `EDGE_DROP, EDGE_REWEIGHT, SUBGRAPH_SAMPLE` | AUTHOR_STATED | PAPER_FULLTEXT | Counterfactual graph intervention and structural perturbation |
| `educational_structure_preservation` | `YES_EXPLICIT` | AUTHOR_STATED | PAPER_FULLTEXT | Preserves educational interaction semantics during counterfactual graph transformations |

---

# 3. EXPERIMENT Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `experiment_id` | `EXP_KT050_MAIN` | AUTHOR_STATED | PAPER_FULLTEXT | Main experimental evaluation |
| `datasets` | ASSISTments2009, ASSISTments2017, Junyi | AUTHOR_STATED | PAPER_FULLTEXT | Benchmark educational datasets evaluated |
| `split_type` | `LEARNER_BASED` | AUTHOR_STATED | PAPER_FULLTEXT | Student history partition into train/test splits |
| `n_seeds` | 5 | AUTHOR_STATED | PAPER_FULLTEXT | Performance averaged over 5 random seeds (CB13) |
| `resampling_repeats` | 1 | REVIEWER_INFERRED | PAPER_FULLTEXT | Single train/test data split repeated across seeds (CB13) |
| `repeated_run_unit` | `SEED_REPETITION` | REVIEWER_INFERRED | PAPER_FULLTEXT | Seed repetition unit (CB13) |
| `sparse_concept_ontology` | `GENERIC_DATA_SPARSITY` | REVIEWER_INFERRED | PAPER_FULLTEXT | Evaluates counterfactual graph augmentation under observational data sparsity |
| `metrics` | ROC-AUC, ACC | AUTHOR_STATED | PAPER_FULLTEXT | Prediction accuracy and ROC-AUC metrics |
| `statistical_testing` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | Significance tests omitted |
| `calibration_metrics` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | ECE omitted |
| `computational_reporting` | `YES_FULL` | AUTHOR_STATED | PAPER_FULLTEXT | Reports formal counterfactual graph time/memory complexity and empirical runtime curves |

---

# 4. Quality Scoring (QA1–QA8)

| QA Criterion | Score (0-2) | Justification |
|---|---|---|
| **QA1 Task Clarity** | 2 | Clear formulation of graph counterfactual augmentation for knowledge tracing. |
| **QA2 Data Transparency** | 2 | Evaluates on public benchmark datasets (ASSIST09, ASSIST17, Junyi). |
| **QA3 Split/Leakage Transparency** | 2 | Counterfactual graph transformations preserve causal temporal order; low leakage risk. |
| **QA4 Baseline/Ablation Adequacy** | 2 | Evaluates against DKT, SAKT, GIKT, CL4KT and performs counterfactual augmentation ablation. |
| **QA5 Statistical Uncertainty** | 1 | Reports mean performance across seeds; formal significance testing omitted. |
| **QA6 Author Artifacts** | 1 | Official IEEE journal full text verified; author code repository unverified. |
| **QA7 Sparse Construct Validity** | 1 | Motivates model via counterfactual graph augmentation under sparse data, but lacks zero-exposure cold-start KC evaluation. |
| **QA8 Computational Transparency** | 2 | Reports formal time/memory complexity of counterfactual graph generation. |

**Raw Quality Score:** 13 / 16  
**Normalized Quality:** 0.8125 (**HIGH Quality**)
