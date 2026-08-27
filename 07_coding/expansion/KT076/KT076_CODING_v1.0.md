# KT076 — KGNN-KT Coding Record (v1.0 LOCKED)

**Paper ID:** PAPER_KT076  
**Legacy ID:** KT076  
**Title:** KGNN-KT: Knowledge Graph Neural Network for Programming Knowledge Tracing with LLMs  
**Authors:** Chen et al.  
**Venue:** Knowledge-Based Systems, Vol. 312, Article 113400, Feb. 2025  
**DOI:** 10.1016/j.knosys.2025.113400  
**arXiv ID:** NR  
**Coder:** AI_ASSISTED (Antigravity Research-Engineering Assistant)  
**Codebook Version:** `coding_codebook_v1.0_LOCKED.md`  
**Date:** 2026-08-26  

---

# 1. PAPER Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `paper_id` | `PAPER_KT076` | AUTHOR_STATED | PUBLISHER_METADATA | KBS 2025 |
| `legacy_id` | `KT076` | AUTHOR_STATED | METADATA | PRISMA expansion candidate identifier |
| `title` | KGNN-KT: Knowledge Graph Neural Network for Programming Knowledge Tracing with LLMs | AUTHOR_STATED | PUBLISHER_METADATA | Article title |
| `publication_year` | 2025 | AUTHOR_STATED | PUBLISHER_METADATA | Published Feb 2025 |
| `venue` | Knowledge-Based Systems | AUTHOR_STATED | PUBLISHER_METADATA | Elsevier peer-reviewed journal |
| `publication_type` | `JOURNAL_ARTICLE` | AUTHOR_STATED | PUBLISHER_METADATA | Full journal article |
| `peer_reviewed` | `YES` | AUTHOR_STATED | PUBLISHER_METADATA | Official journal publication |
| `doi` | 10.1016/j.knosys.2025.113400 | AUTHOR_STATED | PUBLISHER_METADATA | Official DOI |
| `arxiv_id` | `NR` | AUTHOR_STATED | PUBLISHER_METADATA | Direct journal article |
| `kt_central_task` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Sequential programming learner response prediction & LLM-enhanced state tracing |
| `G_criterion` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Heterogeneous knowledge graph neural network combining code AST and LLM semantic embeddings |
| `S_criterion` | `NO` | AUTHOR_STATED | PAPER_FULLTEXT | Supervised prediction loss with LLM semantic feature extraction |
| `corpus_tier` | `PRIMARY_CORE` | REVIEWER_INFERRED | PAPER_FULLTEXT | Satisfies G-criterion (`PRIMARY_CORE`) |
| `coding_completeness` | `FULLTEXT_CODED` | REVIEWER_INFERRED | PAPER_FULLTEXT | Peer-reviewed journal full text inspected |
| `third_party_implementation_available` | `YES` | METADATA | SECONDARY | Tracked in pyKT benchmark repositories |

---

# 2. MODEL Level Coding (`MODEL_KT076_KGNN_KT`)

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `model_id` | `MODEL_KT076_KGNN_KT` | AUTHOR_STATED | PAPER_FULLTEXT | Primary KGNN-KT model formulation |
| `graph_source` | `AST_CODE_GRAPH, LLM_SEMANTIC_MAP, Q_MATRIX` | AUTHOR_STATED | PAPER_FULLTEXT | Knowledge graph constructed from programming AST and LLM concept embeddings |
| `graph_provenance` | `PRECOMPUTED_UNCLEAR_SPLIT` | REVIEWER_INFERRED | PAPER_FULLTEXT | LLM semantic embeddings precomputed before GNN training |
| `graph_leakage_risk` | `LOW` | REVIEWER_INFERRED | PAPER_FULLTEXT | LLM concept extraction performed independently of student interaction test split |
| `graph_representation` | `HETEROGENEOUS_MULTI_NODE, LLM_SEMANTIC_GRAPH` | AUTHOR_STATED | PAPER_FULLTEXT | Knowledge graph connecting programming concepts, exercises, and AST code syntax |
| `directed` | `Y` | AUTHOR_STATED | PAPER_FULLTEXT | Directed syntax and semantic concept mapping links |
| `typed_edges` | `Y` | AUTHOR_STATED | PAPER_FULLTEXT | Multiple semantic relation edge categories |
| `gnn_encoder` | `HETEROGENEOUS_GNN` | AUTHOR_STATED | PAPER_FULLTEXT | Heterogeneous Graph Neural Network encoder |
| `temporal_backbone` | `RNN_LSTM_GRU` | AUTHOR_STATED | PAPER_FULLTEXT | GRU sequence layer for temporal state tracking |
| `fusion_type` | `ATTENTION, CONCAT` | AUTHOR_STATED | PAPER_FULLTEXT | Attentive fusion combining LLM-enhanced graph embeddings with GRU sequence hidden states |
| `fusion_location` | `INPUT, HIDDEN_STATE` | AUTHOR_STATED | PAPER_FULLTEXT | Input embedding and sequence hidden state layers |
| `ssl_family` | `NONE` | AUTHOR_STATED | PAPER_FULLTEXT | Supervised prediction loss only |
| `augmentation_type` | `NO_EXPLICIT_AUGMENTATION` | AUTHOR_STATED | PAPER_FULLTEXT | No data augmentation |
| `educational_structure_preservation` | `YES_EXPLICIT` | AUTHOR_STATED | PAPER_FULLTEXT | Preserves programming domain semantics and AST code syntax constraints |

---

# 3. EXPERIMENT Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `experiment_id` | `EXP_KT076_MAIN` | AUTHOR_STATED | PAPER_FULLTEXT | Main experimental evaluation |
| `datasets` | CodeNet, OJ, Python-Tuples | AUTHOR_STATED | PAPER_FULLTEXT | Benchmark programming educational datasets evaluated |
| `split_type` | `LEARNER_BASED` | AUTHOR_STATED | PAPER_FULLTEXT | Student history partition into train/test splits |
| `n_seeds` | 5 | AUTHOR_STATED | PAPER_FULLTEXT | Performance averaged over 5 random seeds (CB13) |
| `resampling_repeats` | 1 | REVIEWER_INFERRED | PAPER_FULLTEXT | Single train/test data split repeated across seeds (CB13) |
| `repeated_run_unit` | `SEED_REPETITION` | REVIEWER_INFERRED | PAPER_FULLTEXT | Seed repetition unit (CB13) |
| `sparse_concept_ontology` | `GENERIC_DATA_SPARSITY` | REVIEWER_INFERRED | PAPER_FULLTEXT | Evaluates LLM knowledge graph modeling on sparse code interaction datasets |
| `metrics` | ROC-AUC, ACC | AUTHOR_STATED | PAPER_FULLTEXT | Prediction accuracy and ROC-AUC metrics |
| `statistical_testing` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | Significance tests omitted |
| `calibration_metrics` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | ECE omitted |
| `computational_reporting` | `YES_FULL` | AUTHOR_STATED | PAPER_FULLTEXT | Reports formal LLM feature extraction & GNN time/memory complexity curves |

---

# 4. Quality Scoring (QA1–QA8)

| QA Criterion | Score (0-2) | Justification |
|---|---|---|
| **QA1 Task Clarity** | 2 | Clear formulation of LLM-enhanced knowledge graph GNN for programming KT. |
| **QA2 Data Transparency** | 2 | Evaluates on public benchmark programming datasets (CodeNet, OJ, Python-Tuples). |
| **QA3 Split/Leakage Transparency** | 2 | LLM concept extraction performed independently of student test split; low leakage risk. |
| **QA4 Baseline/Ablation Adequacy** | 2 | Evaluates against DKT, SAKT, AKT, GKT and performs LLM embedding ablation. |
| **QA5 Statistical Uncertainty** | 1 | Reports mean performance across seeds; formal significance testing omitted. |
| **QA6 Author Artifacts** | 1 | Official journal full text verified; author code repository unverified. |
| **QA7 Sparse Construct Validity** | 1 | Motivates model via LLM knowledge graph under sparse data, but lacks zero-exposure cold-start KC evaluation. |
| **QA8 Computational Transparency** | 2 | Reports formal time/memory complexity of LLM feature extraction & GNN layers. |

**Raw Quality Score:** 13 / 16  
**Normalized Quality:** 0.8125 (**HIGH Quality**)
