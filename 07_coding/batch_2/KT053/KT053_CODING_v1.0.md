# KT053 — GASKT Coding Record (v1.0 LOCKED)

**Paper ID:** PAPER_KT053  
**Legacy ID:** KT053  
**Title:** GASKT: A Graph-Based Attentive Knowledge-Search Model for Knowledge Tracing  
**Authors:** Mengdan Wang, Chao Peng, Rui Yang, Chenchao Wang, Yao Chen, Xiaohua Yu  
**Venue:** KSEM 2021 (Springer LNCS Vol. 12815, pp. 268–279, Aug. 2021)  
**DOI:** 10.1007/978-3-030-82136-4_21  
**arXiv ID:** NR  
**Coder:** AI_ASSISTED (Antigravity Research-Engineering Assistant)  
**Codebook Version:** `coding_codebook_v1.0_LOCKED.md`  
**Date:** 2026-08-26  

---

# 1. PAPER Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `paper_id` | `PAPER_KT053` | AUTHOR_STATED | PUBLISHER_METADATA | KSEM 2021 |
| `legacy_id` | `KT053` | AUTHOR_STATED | METADATA | Seed corpus identifier |
| `title` | GASKT: A Graph-Based Attentive Knowledge-Search Model for Knowledge Tracing | AUTHOR_STATED | PUBLISHER_METADATA | Published article title |
| `publication_year` | 2021 | AUTHOR_STATED | PUBLISHER_METADATA | Published Aug 2021 |
| `venue` | KSEM | AUTHOR_STATED | PUBLISHER_METADATA | Springer LNCS conference proceedings |
| `publication_type` | `CONFERENCE_PAPER` | AUTHOR_STATED | PUBLISHER_METADATA | Full conference proceedings paper |
| `peer_reviewed` | `YES` | AUTHOR_STATED | PUBLISHER_METADATA | Official Springer peer-reviewed publication |
| `doi` | 10.1007/978-3-030-82136-4_21 | AUTHOR_STATED | PUBLISHER_METADATA | Official DOI |
| `arxiv_id` | `NR` | AUTHOR_STATED | PUBLISHER_METADATA | Direct conference publication |
| `kt_central_task` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Sequential learner response prediction & state search |
| `G_criterion` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Graph-based attentive knowledge-search model with GCN concept representation |
| `S_criterion` | `NO` | AUTHOR_STATED | PAPER_FULLTEXT | Supervised prediction loss only |
| `corpus_tier` | `PRIMARY_CORE` | REVIEWER_INFERRED | PAPER_FULLTEXT | Satisfies G-criterion (`PRIMARY_CORE`) |
| `coding_completeness` | `FULLTEXT_CODED` | REVIEWER_INFERRED | PAPER_FULLTEXT | Peer-reviewed Springer conference full text inspected |
| `third_party_implementation_available` | `YES` | METADATA | SECONDARY | Tracked in pyKT / KT benchmark repositories |

---

# 2. MODEL Level Coding (`MODEL_KT053_GASKT`)

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `model_id` | `MODEL_KT053_GASKT` | AUTHOR_STATED | PAPER_FULLTEXT | Primary GASKT model formulation |
| `graph_source` | `Q_MATRIX, CO_OCCURRENCE` | AUTHOR_STATED | PAPER_FULLTEXT | Concept dependency graph constructed from Q-matrix and interaction co-occurrences |
| `graph_provenance` | `PRECOMPUTED_UNCLEAR_SPLIT` | REVIEWER_INFERRED | PAPER_FULLTEXT | Precomputed concept graph adjacency prior to sequence search |
| `graph_leakage_risk` | `POTENTIAL` | REVIEWER_INFERRED | PAPER_FULLTEXT | Precomputed co-occurrence graph adjacency without explicit train-only split reporting |
| `graph_representation` | `KC_KC, ITEM_KC_BIPARTITE` | AUTHOR_STATED | PAPER_FULLTEXT | Concept dependency graph linked to exercises |
| `directed` | `N` | AUTHOR_STATED | PAPER_FULLTEXT | Undirected concept graph adjacency |
| `typed_edges` | `N` | AUTHOR_STATED | PAPER_FULLTEXT | Single concept dependency relation type |
| `gnn_encoder` | `GCN` | AUTHOR_STATED | PAPER_FULLTEXT | Graph Convolutional Network encoder |
| `temporal_backbone` | `SELF_ATTENTION_TRANSFORMER` | AUTHOR_STATED | PAPER_FULLTEXT | Attentive knowledge-search Transformer backbone |
| `fusion_type` | `ATTENTION, CROSS_ATTENTION` | AUTHOR_STATED | PAPER_FULLTEXT | Cross-attention mechanism fusing GCN concept representations into sequence search layer |
| `fusion_location` | `INPUT, HIDDEN_STATE` | AUTHOR_STATED | PAPER_FULLTEXT | Input embedding and sequence attention layers |
| `ssl_family` | `NONE` | AUTHOR_STATED | PAPER_FULLTEXT | Supervised prediction loss only |
| `augmentation_type` | `NO_EXPLICIT_AUGMENTATION` | AUTHOR_STATED | PAPER_FULLTEXT | No data augmentation |
| `educational_structure_preservation` | `YES_EXPLICIT` | AUTHOR_STATED | PAPER_FULLTEXT | Preserves concept mapping constraints during attentive graph knowledge search |

---

# 3. EXPERIMENT Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `experiment_id` | `EXP_KT053_MAIN` | AUTHOR_STATED | PAPER_FULLTEXT | Main experimental evaluation |
| `datasets` | ASSISTments2009, ASSISTments2012, Statics2011 | AUTHOR_STATED | PAPER_FULLTEXT | Benchmark educational datasets evaluated |
| `split_type` | `LEARNER_BASED` | AUTHOR_STATED | PAPER_FULLTEXT | Learner history partition into train/test splits |
| `n_seeds` | 5 | AUTHOR_STATED | PAPER_FULLTEXT | Performance averaged over 5 random seeds (CB13) |
| `resampling_repeats` | 1 | REVIEWER_INFERRED | PAPER_FULLTEXT | Single data split repeated across model seeds (CB13) |
| `repeated_run_unit` | `SEED_REPETITION` | REVIEWER_INFERRED | PAPER_FULLTEXT | Seed repetition unit (CB13) |
| `sparse_concept_ontology` | `GENERIC_DATA_SPARSITY` | REVIEWER_INFERRED | PAPER_FULLTEXT | Evaluates graph knowledge search on interaction datasets |
| `metrics` | ROC-AUC, ACC | AUTHOR_STATED | PAPER_FULLTEXT | Prediction accuracy and ROC-AUC metrics |
| `statistical_testing` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | Significance tests omitted |
| `calibration_metrics` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | ECE omitted |
| `computational_reporting` | `LIMITED` | REVIEWER_INFERRED | PAPER_FULLTEXT | Scaling bounds omitted |

---

# 4. Quality Scoring (QA1–QA8)

| QA Criterion | Score (0-2) | Justification |
|---|---|---|
| **QA1 Task Clarity** | 2 | Clear formulation of graph-based attentive knowledge-search for KT. |
| **QA2 Data Transparency** | 2 | Evaluates on public benchmark datasets (ASSIST09, ASSIST12, Statics11). |
| **QA3 Split/Leakage Transparency** | 1 | Train/test split reported; precomputed concept graph train-only isolation unverified. |
| **QA4 Baseline/Ablation Adequacy** | 2 | Evaluates against DKT, SAKT, AKT, GKT and performs graph search component ablation. |
| **QA5 Statistical Uncertainty** | 1 | Reports mean performance across seeds; formal significance testing omitted. |
| **QA6 Author Artifacts** | 1 | Official Springer proceedings full text verified; author code repository unverified. |
| **QA7 Sparse Construct Validity** | 1 | Motivates model via graph knowledge search, but lacks zero-exposure cold-start KC evaluation. |
| **QA8 Computational Transparency** | 1 | Explains GCN complexity; formal runtime scaling bounds omitted. |

**Raw Quality Score:** 11 / 16  
**Normalized Quality:** 0.6875 (**MODERATE Quality**)
