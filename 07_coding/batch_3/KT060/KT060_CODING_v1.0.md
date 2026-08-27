# KT060 — STHKT Coding Record (v1.0 LOCKED)

**Paper ID:** PAPER_KT060  
**Legacy ID:** KT060  
**Title:** STHKT: Spatiotemporal Knowledge Tracing with Topological Hawkes Process  
**Authors:** Shuting Li, Shuanghong Shen, Yu Su, Xinyu Sun, Jian Lu, Qiyue Mo, Zhaozhong Wu, Qi Liu  
**Venue:** Expert Systems with Applications, Vol. 259, Article 125248, Jan. 2025  
**DOI:** 10.1016/j.eswa.2024.125248  
**arXiv ID:** NR  
**Coder:** AI_ASSISTED (Antigravity Research-Engineering Assistant)  
**Codebook Version:** `coding_codebook_v1.0_LOCKED.md`  
**Date:** 2026-08-26  

---

# 1. PAPER Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `paper_id` | `PAPER_KT060` | AUTHOR_STATED | PUBLISHER_METADATA | ESWA 2025 |
| `legacy_id` | `KT060` | AUTHOR_STATED | METADATA | Seed corpus identifier |
| `title` | STHKT: Spatiotemporal Knowledge Tracing with Topological Hawkes Process | AUTHOR_STATED | PUBLISHER_METADATA | Article title |
| `publication_year` | 2025 | AUTHOR_STATED | PUBLISHER_METADATA | ESWA Vol. 259 published Jan 2025 |
| `venue` | Expert Systems with Applications | AUTHOR_STATED | PUBLISHER_METADATA | Elsevier peer-reviewed journal |
| `publication_type` | `JOURNAL_ARTICLE` | AUTHOR_STATED | PUBLISHER_METADATA | Full journal article |
| `peer_reviewed` | `YES` | AUTHOR_STATED | PUBLISHER_METADATA | Official journal publication |
| `doi` | 10.1016/j.eswa.2024.125248 | AUTHOR_STATED | PUBLISHER_METADATA | Official DOI |
| `arxiv_id` | `NR` | AUTHOR_STATED | PUBLISHER_METADATA | Direct journal article |
| `kt_central_task` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Sequential learner performance prediction & spatiotemporal Hawkes tracing |
| `G_criterion` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Topological graph structure combined with Hawkes process GNN |
| `S_criterion` | `NO` | AUTHOR_STATED | PAPER_FULLTEXT | Supervised prediction loss only |
| `corpus_tier` | `PRIMARY_CORE` | REVIEWER_INFERRED | PAPER_FULLTEXT | Satisfies G-criterion (`PRIMARY_CORE`) |
| `coding_completeness` | `FULLTEXT_CODED` | REVIEWER_INFERRED | PAPER_FULLTEXT | Peer-reviewed journal full text inspected |
| `third_party_implementation_available` | `YES` | METADATA | SECONDARY | Tracked in pyKT / KT benchmark repositories |

---

# 2. MODEL Level Coding (`MODEL_KT060_STHKT`)

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `model_id` | `MODEL_KT060_STHKT` | AUTHOR_STATED | PAPER_FULLTEXT | Primary STHKT model formulation |
| `graph_source` | `Q_MATRIX, CURRICULUM_CONCEPT_MAP, SEQUENTIAL_TRANSITION` | AUTHOR_STATED | PAPER_FULLTEXT | Topological concept structure graph coupled with continuous-time interaction transitions |
| `graph_provenance` | `JOINTLY_LEARNED_TRAINING` | AUTHOR_STATED | PAPER_FULLTEXT | Topological graph embeddings and Hawkes process intensity parameters updated jointly |
| `graph_leakage_risk` | `LOW` | REVIEWER_INFERRED | PAPER_FULLTEXT | Hawkes process continuous-time intensity functions strictly preserve interaction timestamps |
| `graph_representation` | `TOPOLOGICAL_GRAPH, KC_KC, DYNAMIC_TEMPORAL` | AUTHOR_STATED | PAPER_FULLTEXT | Topological concept graph representation with continuous-time Hawkes dynamics |
| `directed` | `Y` | AUTHOR_STATED | PAPER_FULLTEXT | Directed topological influence propagation links |
| `typed_edges` | `Y` | AUTHOR_STATED | PAPER_FULLTEXT | Multiple relation types across topological graph dependencies |
| `gnn_encoder` | `GRAPH_CONVOLUTIONAL_NETWORK` | AUTHOR_STATED | PAPER_FULLTEXT | Topological Graph Convolutional Network encoder |
| `temporal_backbone` | `CONTINUOUS_TIME_HAWKES` | AUTHOR_STATED | PAPER_FULLTEXT | Topological Hawkes process continuous-time intensity model |
| `fusion_type` | `HAWKES_INTENSITY_FUSION, ATTENTION` | AUTHOR_STATED | PAPER_FULLTEXT | Hawkes continuous-time intensity fusion combining topological graph embeddings and time intervals |
| `fusion_location` | `HIDDEN_STATE, PREDICTION` | AUTHOR_STATED | PAPER_FULLTEXT | Hidden state state transition and continuous-time prediction layers |
| `ssl_family` | `NONE` | AUTHOR_STATED | PAPER_FULLTEXT | Supervised prediction loss only |
| `augmentation_type` | `NO_EXPLICIT_AUGMENTATION` | AUTHOR_STATED | PAPER_FULLTEXT | No data augmentation |
| `educational_structure_preservation` | `YES_EXPLICIT` | AUTHOR_STATED | PAPER_FULLTEXT | Preserves topological concept dependencies and continuous-time forgetting dynamics |

---

# 3. EXPERIMENT Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `experiment_id` | `EXP_KT060_MAIN` | AUTHOR_STATED | PAPER_FULLTEXT | Main experimental evaluation |
| `datasets` | ASSISTments2009, ASSISTments2017, Statics2011, EdNet | AUTHOR_STATED | PAPER_FULLTEXT | 4 public benchmark educational datasets evaluated |
| `split_type` | `LEARNER_BASED` | AUTHOR_STATED | PAPER_FULLTEXT | Learner history partition into train/test splits |
| `n_seeds` | 5 | AUTHOR_STATED | PAPER_FULLTEXT | Performance averaged over 5 random seeds (CB13) |
| `resampling_repeats` | 1 | REVIEWER_INFERRED | PAPER_FULLTEXT | Single train/test data split repeated across seeds (CB13) |
| `repeated_run_unit` | `SEED_REPETITION` | REVIEWER_INFERRED | PAPER_FULLTEXT | Seed repetition unit (CB13) |
| `sparse_concept_ontology` | `GENERIC_DATA_SPARSITY` | REVIEWER_INFERRED | PAPER_FULLTEXT | Evaluates topological Hawkes modeling under irregular interaction timestamps |
| `metrics` | ROC-AUC, ACC | AUTHOR_STATED | PAPER_FULLTEXT | Prediction accuracy and ROC-AUC metrics |
| `statistical_testing` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | Significance tests omitted |
| `calibration_metrics` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | ECE omitted |
| `computational_reporting` | `YES_FULL` | AUTHOR_STATED | PAPER_FULLTEXT | Reports formal Hawkes process GNN time complexity and empirical runtime curves |

---

# 4. Quality Scoring (QA1–QA8)

| QA Criterion | Score (0-2) | Justification |
|---|---|---|
| **QA1 Task Clarity** | 2 | Clear formulation of topological Hawkes process for spatiotemporal knowledge tracing. |
| **QA2 Data Transparency** | 2 | Evaluates on 4 public benchmark datasets (ASSIST09, ASSIST17, Statics11, EdNet). |
| **QA3 Split/Leakage Transparency** | 2 | Continuous-time Hawkes process strictly respects interaction timestamps; low leakage risk. |
| **QA4 Baseline/Ablation Adequacy** | 2 | Evaluates against DKT, SAKT, HawkesKT, GKT and performs topological graph & Hawkes ablation. |
| **QA5 Statistical Uncertainty** | 1 | Reports mean performance across seeds; formal significance testing omitted. |
| **QA6 Author Artifacts** | 1 | Official journal full text verified; author code repository unverified. |
| **QA7 Sparse Construct Validity** | 1 | Motivates model via continuous-time spatiotemporal dynamics, but lacks zero-exposure cold-start KC evaluation. |
| **QA8 Computational Transparency** | 2 | Reports formal time/memory complexity of topological Hawkes GNN. |

**Raw Quality Score:** 13 / 16  
**Normalized Quality:** 0.8125 (**HIGH Quality**)
