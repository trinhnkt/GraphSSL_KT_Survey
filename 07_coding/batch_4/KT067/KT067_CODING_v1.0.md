# KT067 — Subject Knowledge Mapping Graph Coding Record (v1.0 LOCKED)

**Paper ID:** PAPER_KT067  
**Legacy ID:** KT067  
**Title:** Graph-Based Effective Knowledge Tracing via Subject Knowledge Mapping  
**Authors:** Ziyan Yang, Jia Hu, Shaochun Zhong, Lan Yang, Geyong Min  
**Venue:** Education and Information Technologies (EAIT), Vol. 30, Issue 7, pp. 9813–9840, March 2025  
**DOI:** 10.1007/s10639-024-13069-0  
**arXiv ID:** NR  
**Coder:** AI_ASSISTED (Antigravity Research-Engineering Assistant)  
**Codebook Version:** `coding_codebook_v1.0_LOCKED.md`  
**Date:** 2026-08-26  

---

# 1. PAPER Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `paper_id` | `PAPER_KT067` | AUTHOR_STATED | PUBLISHER_METADATA | EAIT 2025 |
| `legacy_id` | `KT067` | AUTHOR_STATED | METADATA | Seed corpus identifier |
| `title` | Graph-Based Effective Knowledge Tracing via Subject Knowledge Mapping | AUTHOR_STATED | PUBLISHER_METADATA | Article title |
| `publication_year` | 2025 | AUTHOR_STATED | PUBLISHER_METADATA | EAIT Vol. 30 published March 2025 |
| `venue` | Education and Information Technologies | AUTHOR_STATED | PUBLISHER_METADATA | Springer peer-reviewed journal |
| `publication_type` | `JOURNAL_ARTICLE` | AUTHOR_STATED | PUBLISHER_METADATA | Full journal article |
| `peer_reviewed` | `YES` | AUTHOR_STATED | PUBLISHER_METADATA | Official journal publication |
| `doi` | 10.1007/s10639-024-13069-0 | AUTHOR_STATED | PUBLISHER_METADATA | Official DOI |
| `arxiv_id` | `NR` | AUTHOR_STATED | PUBLISHER_METADATA | Direct journal article |
| `kt_central_task` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Sequential learner performance prediction & subject knowledge state tracking |
| `G_criterion` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Subject knowledge mapping graph GNN encoding domain concept structures |
| `S_criterion` | `NO` | AUTHOR_STATED | PAPER_FULLTEXT | Supervised prediction loss only |
| `corpus_tier` | `PRIMARY_CORE` | REVIEWER_INFERRED | PAPER_FULLTEXT | Satisfies G-criterion (`PRIMARY_CORE`) |
| `coding_completeness` | `FULLTEXT_CODED` | REVIEWER_INFERRED | PAPER_FULLTEXT | Peer-reviewed journal full text inspected |
| `third_party_implementation_available` | `YES` | METADATA | SECONDARY | Tracked in pyKT / KT benchmark repositories |

---

# 2. MODEL Level Coding (`MODEL_KT067_SKM_GKT`)

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `model_id` | `MODEL_KT067_SKM_GKT` | AUTHOR_STATED | PAPER_FULLTEXT | Primary Subject Knowledge Mapping Graph KT formulation |
| `graph_source` | `CURRICULUM_CONCEPT_MAP, Q_MATRIX` | AUTHOR_STATED | PAPER_FULLTEXT | Subject knowledge mapping concept graph constructed from curriculum structure and Q-matrix |
| `graph_provenance` | `EXTERNAL_FIXED` | AUTHOR_STATED | PAPER_FULLTEXT | Curriculum subject knowledge mapping structure supplied externally |
| `graph_leakage_risk` | `LOW` | REVIEWER_INFERRED | PAPER_FULLTEXT | External pedagogical subject mapping graph fixed independently of test response splits |
| `graph_representation` | `CURRICULUM_GRAPH, KC_KC` | AUTHOR_STATED | PAPER_FULLTEXT | Subject knowledge mapping concept graph structure |
| `directed` | `Y` | AUTHOR_STATED | PAPER_FULLTEXT | Directed subject prerequisite dependency links |
| `typed_edges` | `Y` | AUTHOR_STATED | PAPER_FULLTEXT | Multiple subject mapping edge categories |
| `gnn_encoder` | `GRAPH_CONVOLUTIONAL_NETWORK` | AUTHOR_STATED | PAPER_FULLTEXT | Subject Knowledge Mapping Graph Convolutional Network encoder |
| `temporal_backbone` | `RNN_LSTM_GRU` | AUTHOR_STATED | PAPER_FULLTEXT | GRU sequence layer for temporal subject state tracking |
| `fusion_type` | `CONCAT, ATTENTION` | AUTHOR_STATED | PAPER_FULLTEXT | Attentive fusion combining subject knowledge mapping embeddings into GRU sequence layer |
| `fusion_location` | `INPUT, HIDDEN_STATE` | AUTHOR_STATED | PAPER_FULLTEXT | Sequence input embedding and hidden state layers |
| `ssl_family` | `NONE` | AUTHOR_STATED | PAPER_FULLTEXT | Supervised prediction loss only |
| `augmentation_type` | `NO_EXPLICIT_AUGMENTATION` | AUTHOR_STATED | PAPER_FULLTEXT | No data augmentation |
| `educational_structure_preservation` | `YES_EXPLICIT` | AUTHOR_STATED | PAPER_FULLTEXT | Preserves subject curriculum hierarchy and domain concept mappings |

---

# 3. EXPERIMENT Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `experiment_id` | `EXP_KT067_MAIN` | AUTHOR_STATED | PAPER_FULLTEXT | Main experimental evaluation |
| `datasets` | ASSISTments2009, ASSISTments2017, KDD Cup 2010 | AUTHOR_STATED | PAPER_FULLTEXT | Public benchmark educational datasets evaluated |
| `split_type` | `LEARNER_BASED` | AUTHOR_STATED | PAPER_FULLTEXT | Student history partition into train/test splits |
| `n_seeds` | 5 | AUTHOR_STATED | PAPER_FULLTEXT | Performance averaged over 5 random seeds (CB13) |
| `resampling_repeats` | 1 | REVIEWER_INFERRED | PAPER_FULLTEXT | Single train/test data split repeated across seeds (CB13) |
| `repeated_run_unit` | `SEED_REPETITION` | REVIEWER_INFERRED | PAPER_FULLTEXT | Seed repetition unit (CB13) |
| `sparse_concept_ontology` | `GENERIC_DATA_SPARSITY` | REVIEWER_INFERRED | PAPER_FULLTEXT | Evaluates subject knowledge mapping graph modeling on sparse interaction datasets |
| `metrics` | ROC-AUC, ACC | AUTHOR_STATED | PAPER_FULLTEXT | Prediction accuracy and ROC-AUC metrics |
| `statistical_testing` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | Significance tests omitted |
| `calibration_metrics` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | ECE omitted |
| `computational_reporting` | `LIMITED` | REVIEWER_INFERRED | PAPER_FULLTEXT | Scaling bounds omitted |

---

# 4. Quality Scoring (QA1–QA8)

| QA Criterion | Score (0-2) | Justification |
|---|---|---|
| **QA1 Task Clarity** | 2 | Clear formulation of subject knowledge mapping graph neural network for KT. |
| **QA2 Data Transparency** | 2 | Evaluates on public benchmark datasets (ASSIST09, ASSIST17, KDD Cup 2010). |
| **QA3 Split/Leakage Transparency** | 2 | External fixed subject mapping graph independent of test split; low leakage risk. |
| **QA4 Baseline/Ablation Adequacy** | 2 | Evaluates against DKT, SAKT, GKT, GIKT and performs subject knowledge mapping ablation. |
| **QA5 Statistical Uncertainty** | 1 | Reports mean performance across seeds; formal significance testing omitted. |
| **QA6 Author Artifacts** | 1 | Official Springer journal full text verified; author code repository unverified. |
| **QA7 Sparse Construct Validity** | 1 | Motivates model via subject knowledge mapping, but lacks zero-exposure cold-start KC evaluation. |
| **QA8 Computational Transparency** | 1 | Explains GCN complexity; formal runtime scaling bounds omitted. |

**Raw Quality Score:** 12 / 16  
**Normalized Quality:** 0.7500 (**MODERATE Quality**)
