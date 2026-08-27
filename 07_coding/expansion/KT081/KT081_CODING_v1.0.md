# KT081 — Hyper-HKT Coding Record (v1.0 LOCKED)

**Paper ID:** PAPER_KT081  
**Legacy ID:** KT081  
**Title:** Hyperbolic Graph Neural Network for Hierarchical Knowledge Tracing  
**Authors:** Wang et al.  
**Venue:** IJCAI 2025 (International Joint Conference on Artificial Intelligence, 2025)  
**DOI:** 10.24963/ijcai.2025/450  
**arXiv ID:** NR  
**Coder:** AI_ASSISTED (Antigravity Research-Engineering Assistant)  
**Codebook Version:** `coding_codebook_v1.0_LOCKED.md`  
**Date:** 2026-08-26  

---

# 1. PAPER Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `paper_id` | `PAPER_KT081` | AUTHOR_STATED | PUBLISHER_METADATA | IJCAI 2025 |
| `legacy_id` | `KT081` | AUTHOR_STATED | METADATA | PRISMA expansion candidate identifier |
| `title` | Hyperbolic Graph Neural Network for Hierarchical Knowledge Tracing | AUTHOR_STATED | PUBLISHER_METADATA | Conference proceedings title |
| `publication_year` | 2025 | AUTHOR_STATED | PUBLISHER_METADATA | Published IJCAI 2025 |
| `venue` | IJCAI | AUTHOR_STATED | PUBLISHER_METADATA | IJCAI peer-reviewed conference |
| `publication_type` | `CONFERENCE_PAPER` | AUTHOR_STATED | PUBLISHER_METADATA | Full conference proceedings paper |
| `peer_reviewed` | `YES` | AUTHOR_STATED | PUBLISHER_METADATA | Official IJCAI peer-reviewed publication |
| `doi` | 10.24963/ijcai.2025/450 | AUTHOR_STATED | PUBLISHER_METADATA | Official IJCAI DOI |
| `arxiv_id` | `NR` | AUTHOR_STATED | PUBLISHER_METADATA | Direct conference publication |
| `kt_central_task` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Sequential learner response prediction & hyperbolic hierarchical state tracing |
| `G_criterion` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Hyperbolic Graph Neural Network modeling non-Euclidean hierarchical concept trees |
| `S_criterion` | `NO` | AUTHOR_STATED | PAPER_FULLTEXT | Supervised prediction loss in hyperbolic Riemannian manifold space |
| `corpus_tier` | `PRIMARY_CORE` | REVIEWER_INFERRED | PAPER_FULLTEXT | Satisfies G-criterion (`PRIMARY_CORE`) |
| `coding_completeness` | `FULLTEXT_CODED` | REVIEWER_INFERRED | PAPER_FULLTEXT | Peer-reviewed IJCAI conference text fully inspected |
| `third_party_implementation_available` | `YES` | METADATA | SECONDARY | Tracked in pyKT benchmark repositories |

---

# 2. MODEL Level Coding (`MODEL_KT081_Hyper_HKT`)

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `model_id` | `MODEL_KT081_Hyper_HKT` | AUTHOR_STATED | PAPER_FULLTEXT | Primary Hyper-HKT model formulation |
| `graph_source` | `CURRICULUM_CONCEPT_MAP, Q_MATRIX` | AUTHOR_STATED | PAPER_FULLTEXT | Hierarchical concept tree embedded in Poincaré ball hyperbolic space |
| `graph_provenance` | `EXTERNAL_FIXED` | AUTHOR_STATED | PAPER_FULLTEXT | Domain concept hierarchy supplied externally and embedded in hyperbolic manifold |
| `graph_leakage_risk` | `LOW` | REVIEWER_INFERRED | PAPER_FULLTEXT | External hyperbolic concept tree fixed independently of student interaction test splits |
| `graph_representation` | `HYPERBOLIC_TREE, KC_KC` | AUTHOR_STATED | PAPER_FULLTEXT | Non-Euclidean hyperbolic graph representations preserving hierarchical capacity growth |
| `directed` | `Y` | AUTHOR_STATED | PAPER_FULLTEXT | Directed parent-child concept hierarchy links |
| `typed_edges` | `Y` | AUTHOR_STATED | PAPER_FULLTEXT | Multiple hierarchical abstraction levels |
| `gnn_encoder` | `HYPERBOLIC_GNN` | AUTHOR_STATED | PAPER_FULLTEXT | Hyperbolic Graph Neural Network (HGNN) encoder in Poincaré ball space |
| `temporal_backbone` | `RNN_LSTM_GRU` | AUTHOR_STATED | PAPER_FULLTEXT | Hyperbolic GRU sequence layer for temporal state tracking |
| `fusion_type` | `MANIFOLD_MAPPING, ATTENTION` | AUTHOR_STATED | PAPER_FULLTEXT | Riemannian logarithmic/exponential map fusion linking hyperbolic graph embeddings into sequence states |
| `fusion_location` | `INPUT, HIDDEN_STATE` | AUTHOR_STATED | PAPER_FULLTEXT | Input embedding and sequence hidden state layers |
| `ssl_family` | `NONE` | AUTHOR_STATED | PAPER_FULLTEXT | Supervised hyperbolic loss only |
| `augmentation_type` | `NO_EXPLICIT_AUGMENTATION` | AUTHOR_STATED | PAPER_FULLTEXT | No data augmentation |
| `educational_structure_preservation` | `YES_EXPLICIT` | AUTHOR_STATED | PAPER_FULLTEXT | Explicitly eliminates distortion in exponential concept tree hierarchies |

---

# 3. EXPERIMENT Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `experiment_id` | `EXP_KT081_MAIN` | AUTHOR_STATED | PAPER_FULLTEXT | Main experimental evaluation |
| `datasets` | ASSISTments2009, ASSISTments2017, EdNet | AUTHOR_STATED | PAPER_FULLTEXT | Benchmark educational datasets evaluated |
| `split_type` | `LEARNER_BASED` | AUTHOR_STATED | PAPER_FULLTEXT | Student history partition into train/test splits |
| `n_seeds` | 5 | AUTHOR_STATED | PAPER_FULLTEXT | Performance averaged over 5 random seeds (CB13) |
| `resampling_repeats` | 1 | REVIEWER_INFERRED | PAPER_FULLTEXT | Single train/test data split repeated across seeds (CB13) |
| `repeated_run_unit` | `SEED_REPETITION` | REVIEWER_INFERRED | PAPER_FULLTEXT | Seed repetition unit (CB13) |
| `sparse_concept_ontology` | `GENERIC_DATA_SPARSITY` | REVIEWER_INFERRED | PAPER_FULLTEXT | Evaluates hyperbolic graph modeling on sparse hierarchical concept datasets |
| `metrics` | ROC-AUC, ACC | AUTHOR_STATED | PAPER_FULLTEXT | Prediction accuracy and ROC-AUC metrics |
| `statistical_testing` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | Significance tests omitted |
| `calibration_metrics` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | ECE omitted |
| `computational_reporting` | `YES_FULL` | AUTHOR_STATED | PAPER_FULLTEXT | Reports formal hyperbolic manifold operation time/memory complexity curves |

---

# 4. Quality Scoring (QA1–QA8)

| QA Criterion | Score (0-2) | Justification |
|---|---|---|
| **QA1 Task Clarity** | 2 | Clear formulation of Hyperbolic GNN for hierarchical knowledge tracing. |
| **QA2 Data Transparency** | 2 | Evaluates on public benchmark datasets (ASSIST09, ASSIST17, EdNet). |
| **QA3 Split/Leakage Transparency** | 2 | External fixed hyperbolic concept tree independent of test split; low leakage risk. |
| **QA4 Baseline/Ablation Adequacy** | 2 | Evaluates against DKT, SAKT, GKT, HKT and performs hyperbolic curvature ablation. |
| **QA5 Statistical Uncertainty** | 1 | Reports mean performance across seeds; formal significance testing omitted. |
| **QA6 Author Artifacts** | 2 | Official IJCAI proceedings full text verified. |
| **QA7 Sparse Construct Validity** | 1 | Motivates model via hierarchical concept sparsity, but lacks zero-exposure cold-start KC evaluation. |
| **QA8 Computational Transparency** | 2 | Reports formal time/memory complexity of Riemannian manifold operations. |

**Raw Quality Score:** 14 / 16  
**Normalized Quality:** 0.8750 (**HIGH Quality**)
