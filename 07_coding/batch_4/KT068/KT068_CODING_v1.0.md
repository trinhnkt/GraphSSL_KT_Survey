# KT068 — HKT Coding Record (v1.0 LOCKED)

**Paper ID:** PAPER_KT068  
**Legacy ID:** KT068  
**Title:** HKT: Hierarchical Structure-Based Knowledge Tracing  
**Authors:** Qing Li, Zhijun Huang, Jianwen Sun, Xin Yuan, Shengyingjie Liu, Zhonghua Yan  
**Venue:** Information Processing & Management, Vol. 62, Issue 5, Article 104206, Sept. 2025  
**DOI:** 10.1016/j.ipm.2025.104206  
**arXiv ID:** NR  
**Coder:** AI_ASSISTED (Antigravity Research-Engineering Assistant)  
**Codebook Version:** `coding_codebook_v1.0_LOCKED.md`  
**Date:** 2026-08-26  

---

# 1. PAPER Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `paper_id` | `PAPER_KT068` | AUTHOR_STATED | PUBLISHER_METADATA | IP&M 2025 |
| `legacy_id` | `KT068` | AUTHOR_STATED | METADATA | Seed corpus identifier |
| `title` | HKT: Hierarchical Structure-Based Knowledge Tracing | AUTHOR_STATED | PUBLISHER_METADATA | Article title |
| `publication_year` | 2025 | AUTHOR_STATED | PUBLISHER_METADATA | IP&M Vol. 62 published Sept 2025 |
| `venue` | Information Processing & Management | AUTHOR_STATED | PUBLISHER_METADATA | Elsevier peer-reviewed journal |
| `publication_type` | `JOURNAL_ARTICLE` | AUTHOR_STATED | PUBLISHER_METADATA | Full journal article |
| `peer_reviewed` | `YES` | AUTHOR_STATED | PUBLISHER_METADATA | Official journal publication |
| `doi` | 10.1016/j.ipm.2025.104206 | AUTHOR_STATED | PUBLISHER_METADATA | Official DOI |
| `arxiv_id` | `NR` | AUTHOR_STATED | PUBLISHER_METADATA | Direct journal article |
| `kt_central_task` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Sequential learner response prediction & hierarchical knowledge state tracking |
| `G_criterion` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Hierarchical structure-based graph neural network over domain concepts |
| `S_criterion` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Hierarchical cross-graph contrastive learning pretext task |
| `corpus_tier` | `PRIMARY_CORE` | REVIEWER_INFERRED | PAPER_FULLTEXT | Satisfies both G-criterion and S-criterion (`PRIMARY_CORE`) |
| `coding_completeness` | `FULLTEXT_CODED` | REVIEWER_INFERRED | PAPER_FULLTEXT | Peer-reviewed journal full text inspected |
| `third_party_implementation_available` | `YES` | METADATA | SECONDARY | Tracked in pyKT / KT benchmark repositories |

---

# 2. MODEL Level Coding (`MODEL_KT068_HKT`)

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `model_id` | `MODEL_KT068_HKT` | AUTHOR_STATED | PAPER_FULLTEXT | Primary HKT model formulation |
| `graph_source` | `CURRICULUM_CONCEPT_MAP, Q_MATRIX` | AUTHOR_STATED | PAPER_FULLTEXT | Hierarchical concept graph constructed from domain structure and Q-matrix |
| `graph_provenance` | `EXTERNAL_FIXED` | AUTHOR_STATED | PAPER_FULLTEXT | Domain hierarchical concept structure supplied externally |
| `graph_leakage_risk` | `LOW` | REVIEWER_INFERRED | PAPER_FULLTEXT | External pedagogical graph fixed independently of test response splits |
| `graph_representation` | `HIERARCHICAL, KC_KC` | AUTHOR_STATED | PAPER_FULLTEXT | Hierarchical concept graph representations across domain abstraction levels |
| `directed` | `Y` | AUTHOR_STATED | PAPER_FULLTEXT | Directed hierarchical parent-child links |
| `typed_edges` | `Y` | AUTHOR_STATED | PAPER_FULLTEXT | Multiple hierarchical abstraction edge types |
| `gnn_encoder` | `HETEROGENEOUS_GNN` | AUTHOR_STATED | PAPER_FULLTEXT | Hierarchical Graph Neural Network encoder |
| `temporal_backbone` | `SELF_ATTENTION_TRANSFORMER` | AUTHOR_STATED | PAPER_FULLTEXT | Attentive Transformer backbone for sequence tracing |
| `fusion_type` | `ATTENTION, CONCAT` | AUTHOR_STATED | PAPER_FULLTEXT | Fuses hierarchical graph representations into attentive sequence layers |
| `fusion_location` | `INPUT, HIDDEN_STATE, AUXILIARY_LOSS` | AUTHOR_STATED | PAPER_FULLTEXT | Input embedding, sequence hidden state, and hierarchical contrastive loss layers |
| `ssl_family` | `HIERARCHICAL_CONTRASTIVE, GRAPH_CONTRASTIVE` | AUTHOR_STATED | PAPER_FULLTEXT | Cross-graph hierarchical contrastive loss across abstraction levels |
| `augmentation_type` | `NODE_MASK, SUBGRAPH_SAMPLE` | AUTHOR_STATED | PAPER_FULLTEXT | Hierarchical graph structural perturbations |
| `educational_structure_preservation` | `YES_EXPLICIT` | AUTHOR_STATED | PAPER_FULLTEXT | Preserves domain concept hierarchy constraints across contrastive loss levels |

---

# 3. EXPERIMENT Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `experiment_id` | `EXP_KT068_MAIN` | AUTHOR_STATED | PAPER_FULLTEXT | Main experimental evaluation |
| `datasets` | ASSISTments2009, ASSISTments2017, EdNet | AUTHOR_STATED | PAPER_FULLTEXT | Public benchmark educational datasets evaluated |
| `split_type` | `LEARNER_BASED` | AUTHOR_STATED | PAPER_FULLTEXT | Student history partition into train/test splits |
| `n_seeds` | 5 | AUTHOR_STATED | PAPER_FULLTEXT | Performance averaged over 5 random seeds (CB13) |
| `resampling_repeats` | 1 | REVIEWER_INFERRED | PAPER_FULLTEXT | Single train/test data split repeated across seeds (CB13) |
| `repeated_run_unit` | `SEED_REPETITION` | REVIEWER_INFERRED | PAPER_FULLTEXT | Seed repetition unit (CB13) |
| `sparse_concept_ontology` | `GENERIC_DATA_SPARSITY` | REVIEWER_INFERRED | PAPER_FULLTEXT | Evaluates hierarchical contrastive learning under sparse dataset conditions |
| `metrics` | ROC-AUC, ACC | AUTHOR_STATED | PAPER_FULLTEXT | Prediction accuracy and ROC-AUC metrics |
| `statistical_testing` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | Significance tests omitted |
| `calibration_metrics` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | ECE omitted |
| `computational_reporting` | `LIMITED` | REVIEWER_INFERRED | PAPER_FULLTEXT | Scaling bounds omitted |

---

# 4. Quality Scoring (QA1–QA8)

| QA Criterion | Score (0-2) | Justification |
|---|---|---|
| **QA1 Task Clarity** | 2 | Clear formulation of hierarchical structure-based contrastive learning for KT. |
| **QA2 Data Transparency** | 2 | Evaluates on public benchmark datasets (ASSIST09, ASSIST17, EdNet). |
| **QA3 Split/Leakage Transparency** | 2 | External fixed hierarchical graph independent of test split; low leakage risk. |
| **QA4 Baseline/Ablation Adequacy** | 2 | Evaluates against DKT, SAKT, CL4KT, Bi-CLKT and performs hierarchical SSL ablation. |
| **QA5 Statistical Uncertainty** | 1 | Reports mean performance across seeds; formal significance testing omitted. |
| **QA6 Author Artifacts** | 1 | Official journal full text verified; author code repository unverified. |
| **QA7 Sparse Construct Validity** | 1 | Motivates model via hierarchical graph contrastive learning under sparse data, but lacks zero-exposure cold-start KC evaluation. |
| **QA8 Computational Transparency** | 1 | Explains hierarchical GNN complexity; formal runtime scaling bounds omitted. |

**Raw Quality Score:** 12 / 16  
**Normalized Quality:** 0.7500 (**MODERATE Quality**)
