# KT055 — Task Eligibility Exclusion Coding Record (v0.4 PILOT)

**Paper ID:** PAPER_KT055  
**Legacy ID:** KT055  
**Title:** GKT-CD: Make Cognitive Diagnosis Model Enhanced by Graph-Based Knowledge Tracing  
**Authors:** Junrui Zhang, Yun Mo, Changzhi Chen, Xiaofeng He  
**Venue:** IJCNN 2021 (IEEE IJCNN, pp. 1–8, July 2021)  
**DOI:** 10.1109/IJCNN52387.2021.9533367  
**arXiv ID:** NR  
**Coder:** AI_ASSISTED (Antigravity Research-Engineering Assistant)  
**Codebook Version:** `coding_codebook_v0.4_PILOT.md`  
**Date:** 2026-08-26  

---

# 1. PAPER Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `paper_id` | `PAPER_KT055` | AUTHOR_STATED | PUBLISHER_METADATA | IEEE IJCNN 2021 |
| `legacy_id` | `KT055` | AUTHOR_STATED | METADATA | Seed corpus identifier |
| `title` | GKT-CD: Make Cognitive Diagnosis Model Enhanced by Graph-Based Knowledge Tracing | AUTHOR_STATED | PUBLISHER_METADATA | IEEE published article title |
| `publication_year` | 2021 | AUTHOR_STATED | PUBLISHER_METADATA | IJCNN 2021 proceedings published July 2021 |
| `venue` | IJCNN | AUTHOR_STATED | PUBLISHER_METADATA | IEEE International Joint Conference on Neural Networks |
| `publication_type` | `CONFERENCE_PAPER` | AUTHOR_STATED | PUBLISHER_METADATA | Full conference proceedings paper |
| `peer_reviewed` | `YES` | AUTHOR_STATED | PUBLISHER_METADATA | Official IEEE IJCNN 2021 peer-reviewed publication |
| `doi` | 10.1109/IJCNN52387.2021.9533367 | AUTHOR_STATED | PUBLISHER_METADATA | Official IEEE DOI |
| `arxiv_id` | `NR` | AUTHOR_STATED | PUBLISHER_METADATA | Published direct to IEEE Xplore |
| `kt_central_task` | `NO` | REVIEWER_INFERRED | PAPER_FULLTEXT | Primary objective is static Cognitive Diagnosis (profiling student proficiency state matrix) rather than sequential KT performance prediction |
| `G_criterion` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Uses Gated GNN over exercise-concept graph |
| `S_criterion` | `NO` | AUTHOR_STATED | PAPER_FULLTEXT | Supervised cognitive diagnosis loss |
| `corpus_tier` | `EXCLUDE_FULLTEXT` | REVIEWER_INFERRED | PAPER_FULLTEXT | `EXCLUDE_FULLTEXT`: Fails primary gateway requirement (`kt_central_task = NO`). Cognitive Diagnosis enhanced by Graph-KT is excluded |
| `coding_completeness` | `FULLTEXT_CODED` | REVIEWER_INFERRED | PAPER_FULLTEXT | Peer-reviewed IJCNN 2021 proceedings full text inspected |
| `third_party_implementation_available` | `NO` | METADATA | SECONDARY | No public repository verified |

---

# 2. MODEL Level Coding (`MODEL_KT055_GKT_CD`)

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `model_id` | `MODEL_KT055_GKT_CD` | AUTHOR_STATED | PAPER_FULLTEXT | Primary GKT-CD model formulation |
| `graph_source` | `Q_MATRIX, EXPERT_PREREQUISITE` | AUTHOR_STATED | PAPER_FULLTEXT | Exercise-concept graph constructed from Q-matrix and concept dependencies |
| `graph_provenance` | `EXTERNAL_FIXED` | AUTHOR_STATED | PAPER_FULLTEXT | Q-matrix concept graph fixed externally |
| `graph_leakage_risk` | `LOW` | REVIEWER_INFERRED | PAPER_FULLTEXT | External Q-matrix independent of response splits |
| `graph_representation` | `ITEM_KC_BIPARTITE, KC_KC` | AUTHOR_STATED | PAPER_FULLTEXT | Exercise-concept bipartite graph with concept links |
| `directed` | `Y` | AUTHOR_STATED | PAPER_FULLTEXT | Directed Gated GNN propagation |
| `typed_edges` | `N` | AUTHOR_STATED | PAPER_FULLTEXT | Single relation type |
| `gnn_encoder` | `GCN` | AUTHOR_STATED | PAPER_FULLTEXT | Gated GNN / GCN message passing |
| `temporal_backbone` | `NONE` | REVIEWER_INFERRED | PAPER_FULLTEXT | Static Cognitive Diagnosis formulation; lacks sequential temporal state tracking backbone |
| `fusion_type` | `CONCAT` | AUTHOR_STATED | PAPER_FULLTEXT | Fuses GNN concept embeddings into cognitive diagnosis output layer |
| `fusion_location` | `PREDICTION` | AUTHOR_STATED | PAPER_FULLTEXT | Diagnostic output layer |
| `ssl_family` | `NONE` | AUTHOR_STATED | PAPER_FULLTEXT | Supervised loss only |
| `augmentation_type` | `NO_EXPLICIT_AUGMENTATION` | AUTHOR_STATED | PAPER_FULLTEXT | No data augmentation |
| `educational_structure_preservation` | `YES_EXPLICIT` | AUTHOR_STATED | PAPER_FULLTEXT | Preserves Q-matrix mapping constraints |

---

# 3. EXPERIMENT Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `experiment_id` | `EXP_KT055_MAIN` | AUTHOR_STATED | PAPER_FULLTEXT | Main experimental evaluation |
| `datasets` | ASSISTments2009, Junyi | AUTHOR_STATED | PAPER_FULLTEXT | Benchmark educational datasets evaluated for cognitive diagnosis accuracy |
| `split_type` | `LEARNER_BASED` | AUTHOR_STATED | PAPER_FULLTEXT | Train/test response split |
| `n_seeds` | 5 | AUTHOR_STATED | PAPER_FULLTEXT | Evaluated over 5 random seeds (CB13) |
| `resampling_repeats` | 1 | REVIEWER_INFERRED | PAPER_FULLTEXT | Single train/test data split repeated across seeds |
| `repeated_run_unit` | `SEED_REPETITION` | REVIEWER_INFERRED | PAPER_FULLTEXT | Seed repetition unit (CB13) |
| `sparse_concept_ontology` | `GENERIC_DATA_SPARSITY` | REVIEWER_INFERRED | PAPER_FULLTEXT | Evaluated on generic datasets |
| `metrics` | RMSE, ACC, AUC | AUTHOR_STATED | PAPER_FULLTEXT | Diagnostic prediction accuracy |
| `statistical_testing` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | Significance testing details omitted |
| `calibration_metrics` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | ECE omitted |
| `computational_reporting` | `LIMITED` | REVIEWER_INFERRED | PAPER_FULLTEXT | Scaling bounds omitted |

---

# 4. Quality Scoring (QA1–QA8)

| QA Criterion | Score (0-2) | Justification |
|---|---|---|
| **QA1 Task Clarity** | 2 | Clear formulation of GNN-enhanced cognitive diagnosis. |
| **QA2 Data Transparency** | 2 | Evaluates on public benchmark datasets (ASSIST09, Junyi). |
| **QA3 Split/Leakage Transparency** | 1 | Split reported; precomputed graph isolation details omitted. |
| **QA4 Baseline/Ablation Adequacy** | 2 | Evaluates against CD models (DINA, NCDM) and KT models (DKT, GKT). |
| **QA5 Statistical Uncertainty** | 1 | Reports mean performance; significance tests omitted. |
| **QA6 Author Artifacts** | 1 | Peer-reviewed IJCNN proceedings full text verified. |
| **QA7 Sparse Construct Validity** | 1 | Mentions data sparsity generally; lacks isolated cold-start KC evaluation. |
| **QA8 Computational Transparency** | 1 | Scaling bounds omitted. |

**Raw Quality Score:** 11 / 16  
**Normalized Quality:** 0.6875 (**MODERATE Quality**)

---

# 5. Methodological Summary & Codebook Stress-Test Insights

1. **Task Eligibility Exclusion Logic (`EXCLUDE_FULLTEXT`):** Enforces a critical boundary rule. Even though KT055 uses a GNN (`G_criterion = Y`), its primary prediction task is static Cognitive Diagnosis (profiling student proficiency state vector) rather than sequential Knowledge Tracing performance prediction (`kt_central_task = NO`). It is correctly classified as `EXCLUDE_FULLTEXT`, proving that GNN enhancement of non-KT tasks is excluded from the primary survey corpus.
