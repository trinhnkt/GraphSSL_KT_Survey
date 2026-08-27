# KT062 — LGS-KT Coding Record (v1.0 LOCKED)

**Paper ID:** PAPER_KT062  
**Legacy ID:** KT062  
**Title:** LGS-KT: Integrating Logical and Grammatical Skills for Effective Programming Knowledge Tracing  
**Authors:** Xinjie Sun, Qi Liu, Kai Zhang, Shuanghong Shen, Yan Zhuang, Yuxiang Guo  
**Venue:** Neural Networks, Vol. 185, Article 107164, May 2025  
**DOI:** 10.1016/j.neunet.2025.107164  
**arXiv ID:** NR  
**Coder:** AI_ASSISTED (Antigravity Research-Engineering Assistant)  
**Codebook Version:** `coding_codebook_v1.0_LOCKED.md`  
**Date:** 2026-08-26  

---

# 1. PAPER Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `paper_id` | `PAPER_KT062` | AUTHOR_STATED | PUBLISHER_METADATA | Neural Networks 2025 |
| `legacy_id` | `KT062` | AUTHOR_STATED | METADATA | Seed corpus identifier |
| `title` | LGS-KT: Integrating Logical and Grammatical Skills for Effective Programming Knowledge Tracing | AUTHOR_STATED | PUBLISHER_METADATA | Published article title |
| `publication_year` | 2025 | AUTHOR_STATED | PUBLISHER_METADATA | Published May 2025 |
| `venue` | Neural Networks | AUTHOR_STATED | PUBLISHER_METADATA | Elsevier peer-reviewed journal |
| `publication_type` | `JOURNAL_ARTICLE` | AUTHOR_STATED | PUBLISHER_METADATA | Full journal article |
| `peer_reviewed` | `YES` | AUTHOR_STATED | PUBLISHER_METADATA | Official journal publication |
| `doi` | 10.1016/j.neunet.2025.107164 | AUTHOR_STATED | PUBLISHER_METADATA | Official DOI |
| `arxiv_id` | `NR` | AUTHOR_STATED | PUBLISHER_METADATA | Direct journal article |
| `kt_central_task` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Sequential programming learner response prediction & skill state tracing |
| `G_criterion` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Constructs knowledge-concept similarity & AST code graph for logical/grammatical skills |
| `S_criterion` | `NO` | AUTHOR_STATED | PAPER_FULLTEXT | Supervised prediction loss only |
| `corpus_tier` | `PRIMARY_CORE` | REVIEWER_INFERRED | PAPER_FULLTEXT | Satisfies G-criterion (`PRIMARY_CORE`) |
| `coding_completeness` | `FULLTEXT_CODED` | REVIEWER_INFERRED | PAPER_FULLTEXT | Peer-reviewed journal full text inspected |
| `third_party_implementation_available` | `YES` | METADATA | SECONDARY | Tracked in pyKT / KT benchmark repositories |

---

# 2. MODEL Level Coding (`MODEL_KT062_LGS_KT`)

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `model_id` | `MODEL_KT062_LGS_KT` | AUTHOR_STATED | PAPER_FULLTEXT | Primary LGS-KT model formulation |
| `graph_source` | `AST_CODE_GRAPH, SIMILARITY, Q_MATRIX` | AUTHOR_STATED | PAPER_FULLTEXT | Code AST graph combined with concept similarity matrix for logical & grammatical skills |
| `graph_provenance` | `PRECOMPUTED_UNCLEAR_SPLIT` | REVIEWER_INFERRED | PAPER_FULLTEXT | Precomputed AST code graph and concept similarity graph prior to training |
| `graph_leakage_risk` | `LOW` | REVIEWER_INFERRED | PAPER_FULLTEXT | AST code structure graph extracted independently of student interaction split |
| `graph_representation` | `CODE_AST_GRAPH, KC_KC` | AUTHOR_STATED | PAPER_FULLTEXT | Code AST structure graph coupled with concept similarity graph |
| `directed` | `Y` | AUTHOR_STATED | PAPER_FULLTEXT | Directed AST syntax tree links and similarity propagation |
| `typed_edges` | `Y` | AUTHOR_STATED | PAPER_FULLTEXT | Multiple relation types across logical and grammatical syntax edges |
| `gnn_encoder` | `GRAPH_CONVOLUTIONAL_NETWORK` | AUTHOR_STATED | PAPER_FULLTEXT | Graph Convolutional Network encoder over AST code graphs |
| `temporal_backbone` | `RNN_LSTM_GRU` | AUTHOR_STATED | PAPER_FULLTEXT | GRU sequence layer for temporal programming state tracing |
| `fusion_type` | `CONCAT, ATTENTION` | AUTHOR_STATED | PAPER_FULLTEXT | Attentive fusion combining logical/grammatical AST embeddings into GRU sequence layer |
| `fusion_location` | `INPUT, HIDDEN_STATE` | AUTHOR_STATED | PAPER_FULLTEXT | Sequence input embedding and hidden state layers |
| `ssl_family` | `NONE` | AUTHOR_STATED | PAPER_FULLTEXT | Supervised prediction loss only |
| `augmentation_type` | `NO_EXPLICIT_AUGMENTATION` | AUTHOR_STATED | PAPER_FULLTEXT | No data augmentation |
| `educational_structure_preservation` | `YES_EXPLICIT` | AUTHOR_STATED | PAPER_FULLTEXT | Explicitly preserves programming AST syntax constraints and concept dependencies |

---

# 3. EXPERIMENT Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `experiment_id` | `EXP_KT062_MAIN` | AUTHOR_STATED | PAPER_FULLTEXT | Main experimental evaluation |
| `datasets` | CodeNet, OJ, Python-Tuples | AUTHOR_STATED | PAPER_FULLTEXT | Benchmark programming educational datasets evaluated |
| `split_type` | `LEARNER_BASED` | AUTHOR_STATED | PAPER_FULLTEXT | Student history partition into train/test splits |
| `n_seeds` | 5 | AUTHOR_STATED | PAPER_FULLTEXT | Performance averaged over 5 random seeds (CB13) |
| `resampling_repeats` | 1 | REVIEWER_INFERRED | PAPER_FULLTEXT | Single train/test data split repeated across seeds (CB13) |
| `repeated_run_unit` | `SEED_REPETITION` | REVIEWER_INFERRED | PAPER_FULLTEXT | Seed repetition unit (CB13) |
| `sparse_concept_ontology` | `GENERIC_DATA_SPARSITY` | REVIEWER_INFERRED | PAPER_FULLTEXT | Evaluates programming knowledge tracing on sparse code interaction datasets |
| `metrics` | ROC-AUC, ACC | AUTHOR_STATED | PAPER_FULLTEXT | Prediction accuracy and ROC-AUC metrics |
| `statistical_testing` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | Significance tests omitted |
| `calibration_metrics` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | ECE omitted |
| `computational_reporting` | `LIMITED` | REVIEWER_INFERRED | PAPER_FULLTEXT | Scaling bounds omitted |

---

# 4. Quality Scoring (QA1–QA8)

| QA Criterion | Score (0-2) | Justification |
|---|---|---|
| **QA1 Task Clarity** | 2 | Clear formulation of logical/grammatical AST code graph modeling for programming KT. |
| **QA2 Data Transparency** | 2 | Evaluates on public benchmark programming datasets (CodeNet, OJ, Python-Tuples). |
| **QA3 Split/Leakage Transparency** | 2 | AST code graph extracted independently of student interaction test split; low leakage risk. |
| **QA4 Baseline/Ablation Adequacy** | 2 | Evaluates against DKT, SAKT, AKT, GKT and performs logical vs grammatical skill ablation. |
| **QA5 Statistical Uncertainty** | 1 | Reports mean performance across seeds; formal significance testing omitted. |
| **QA6 Author Artifacts** | 1 | Official journal full text verified; author code repository unverified. |
| **QA7 Sparse Construct Validity** | 1 | Motivates model via programming skill graph modeling, but lacks zero-exposure cold-start KC evaluation. |
| **QA8 Computational Transparency** | 1 | Explains AST GCN complexity; formal runtime scaling bounds omitted. |

**Raw Quality Score:** 12 / 16  
**Normalized Quality:** 0.7500 (**MODERATE Quality**)
