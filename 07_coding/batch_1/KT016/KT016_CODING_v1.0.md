# KT016 — SKT Coding Record (v1.0 LOCKED)

**Paper ID:** PAPER_KT016  
**Legacy ID:** KT016  
**Title:** Structure-Based Knowledge Tracing: An Influence Propagation View  
**Authors:** Shiwei Tong, Qi Liu, Wei Huang, Zhenya Huang, Enhong Chen, Chuanren Liu, Haiping Ma, Shijin Wang  
**Venue:** ICDM 2020 (IEEE International Conference on Data Mining, pp. 541–550, Nov. 2020)  
**DOI:** 10.1109/ICDM50108.2020.00063  
**arXiv ID:** NR  
**Coder:** AI_ASSISTED (Antigravity Research-Engineering Assistant)  
**Codebook Version:** `coding_codebook_v1.0_LOCKED.md`  
**Date:** 2026-08-26  

---

# 1. PAPER Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `paper_id` | `PAPER_KT016` | AUTHOR_STATED | PUBLISHER_METADATA | IEEE ICDM 2020 |
| `legacy_id` | `KT016` | AUTHOR_STATED | METADATA | Seed corpus identifier |
| `title` | Structure-Based Knowledge Tracing: An Influence Propagation View | AUTHOR_STATED | PUBLISHER_METADATA | IEEE published article title |
| `publication_year` | 2020 | AUTHOR_STATED | PUBLISHER_METADATA | ICDM 2020 proceedings published Nov 2020 |
| `venue` | ICDM | AUTHOR_STATED | PUBLISHER_METADATA | IEEE Data Mining Conference |
| `publication_type` | `CONFERENCE_PAPER` | AUTHOR_STATED | PUBLISHER_METADATA | Full conference proceedings paper |
| `peer_reviewed` | `YES` | AUTHOR_STATED | PUBLISHER_METADATA | Official IEEE ICDM peer-reviewed publication |
| `doi` | 10.1109/ICDM50108.2020.00063 | AUTHOR_STATED | PUBLISHER_METADATA | Official IEEE DOI |
| `arxiv_id` | `NR` | AUTHOR_STATED | PUBLISHER_METADATA | Direct conference publication |
| `kt_central_task` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Sequential learner response prediction & concept mastery estimation |
| `G_criterion` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Knowledge structure graph with multi-relational concept links and GNN influence propagation |
| `S_criterion` | `NO` | AUTHOR_STATED | PAPER_FULLTEXT | Supervised prediction loss only; no self-supervised pretext task |
| `corpus_tier` | `PRIMARY_CORE` | REVIEWER_INFERRED | PAPER_FULLTEXT | Satisfies G-criterion (`PRIMARY_CORE`) |
| `coding_completeness` | `FULLTEXT_CODED` | REVIEWER_INFERRED | PAPER_FULLTEXT | Peer-reviewed IEEE conference full text inspected |
| `third_party_implementation_available` | `YES` | METADATA | SECONDARY | Tracked in pyKT / KT benchmark repositories |

---

# 2. MODEL Level Coding (`MODEL_KT016_SKT`)

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `model_id` | `MODEL_KT016_SKT` | AUTHOR_STATED | PAPER_FULLTEXT | Primary SKT model formulation |
| `graph_source` | `CURRICULUM_CONCEPT_MAP, Q_MATRIX` | AUTHOR_STATED | PAPER_FULLTEXT | Educational knowledge structure graph specifying concept relations (prerequisite/similarity) |
| `graph_provenance` | `EXTERNAL_FIXED` | AUTHOR_STATED | PAPER_FULLTEXT | Pedagogical knowledge structure supplied externally |
| `graph_leakage_risk` | `LOW` | REVIEWER_INFERRED | PAPER_FULLTEXT | External pedagogical graph fixed independently of student response splits |
| `graph_representation` | `KC_KC, MULTI_RELATIONAL` | AUTHOR_STATED | PAPER_FULLTEXT | Multi-relational concept graph specifying directed influence propagation edges |
| `directed` | `Y` | AUTHOR_STATED | PAPER_FULLTEXT | Directed influence propagation relations between concepts |
| `typed_edges` | `Y` | AUTHOR_STATED | PAPER_FULLTEXT | Multiple concept relation types (prerequisite vs similarity influence) |
| `gnn_encoder` | `GRAPH_ATTENTION_HYBRID` | AUTHOR_STATED | PAPER_FULLTEXT | Influence propagation GNN encoder with attentive message passing |
| `temporal_backbone` | `RNN_LSTM_GRU` | AUTHOR_STATED | PAPER_FULLTEXT | GRU sequence layer for temporal learner state tracking |
| `fusion_type` | `MESSAGE_PASSING_IN_PREDICTION_LOOP, ATTENTION` | AUTHOR_STATED | PAPER_FULLTEXT | Fuses influence propagation embeddings into temporal state transition and prediction loop |
| `fusion_location` | `HIDDEN_STATE, PREDICTION` | AUTHOR_STATED | PAPER_FULLTEXT | Injected at recurrent hidden state and prediction steps |
| `ssl_family` | `NONE` | AUTHOR_STATED | PAPER_FULLTEXT | Supervised prediction loss only |
| `augmentation_type` | `NO_EXPLICIT_AUGMENTATION` | AUTHOR_STATED | PAPER_FULLTEXT | No data augmentation |
| `educational_structure_preservation` | `YES_EXPLICIT` | AUTHOR_STATED | PAPER_FULLTEXT | Explicitly models educational influence propagation constraints across concepts |

---

# 3. EXPERIMENT Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `experiment_id` | `EXP_KT016_MAIN` | AUTHOR_STATED | PAPER_FULLTEXT | Main experimental evaluation |
| `datasets` | ASSISTments2009, ASSISTments2015, Junyi | AUTHOR_STATED | PAPER_FULLTEXT | Benchmark educational datasets evaluated |
| `split_type` | `LEARNER_BASED` | AUTHOR_STATED | PAPER_FULLTEXT | Learner history partition into train/test splits |
| `n_seeds` | 5 | AUTHOR_STATED | PAPER_FULLTEXT | Performance averaged over 5 random seeds (CB13) |
| `resampling_repeats` | 1 | REVIEWER_INFERRED | PAPER_FULLTEXT | Single data split repeated across model seeds (CB13) |
| `repeated_run_unit` | `SEED_REPETITION` | REVIEWER_INFERRED | PAPER_FULLTEXT | Seed repetition unit (CB13) |
| `sparse_concept_ontology` | `GENERIC_DATA_SPARSITY` | REVIEWER_INFERRED | PAPER_FULLTEXT | Evaluates influence propagation on sparse interaction datasets |
| `metrics` | ROC-AUC, ACC | AUTHOR_STATED | PAPER_FULLTEXT | Prediction accuracy and ROC-AUC metrics |
| `statistical_testing` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | Significance tests omitted |
| `calibration_metrics` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | ECE omitted |
| `computational_reporting` | `LIMITED` | REVIEWER_INFERRED | PAPER_FULLTEXT | Mentions influence propagation efficiency; formal scaling bounds omitted |

---

# 4. Quality Scoring (QA1–QA8)

| QA Criterion | Score (0-2) | Justification |
|---|---|---|
| **QA1 Task Clarity** | 2 | Clear influence propagation view on knowledge structure graph for KT. |
| **QA2 Data Transparency** | 2 | Evaluates on public benchmark datasets (ASSIST09, ASSIST15, Junyi). |
| **QA3 Split/Leakage Transparency** | 2 | External fixed knowledge structure graph independent of test interaction split. |
| **QA4 Baseline/Ablation Adequacy** | 2 | Evaluates against DKT, DKVMN, EKT, GKT and performs influence relation ablation. |
| **QA5 Statistical Uncertainty** | 1 | Reports mean performance across seeds; formal significance testing omitted. |
| **QA6 Author Artifacts** | 1 | Peer-reviewed IEEE proceedings full text verified; official repository unverified. |
| **QA7 Sparse Construct Validity** | 1 | Motivates model via multi-relational concept influence, but lacks zero-exposure cold-start KC evaluation. |
| **QA8 Computational Transparency** | 1 | Explains influence propagation complexity; formal runtime scaling bounds omitted. |

**Raw Quality Score:** 12 / 16  
**Normalized Quality:** 0.7500 (**MODERATE Quality**)
