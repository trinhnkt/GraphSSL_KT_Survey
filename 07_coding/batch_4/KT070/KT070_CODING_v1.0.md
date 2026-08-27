# KT070 — Coda Denoising Code Graph Adapter Coding Record (v1.0 LOCKED)

**Paper ID:** PAPER_KT070  
**Legacy ID:** KT070  
**Title:** Denoising Programming Knowledge Tracing with a Code Graph-Based Tuning Adapter (Coda)  
**Authors:** Weibo Gao, Qi Liu, Rui Li, Yuze Zhao, Hao Wang, Linan Yue, Fangzhou Yao, Zheng Zhang  
**Venue:** KDD 2025 (ACM SIGKDD Conference on Knowledge Discovery and Data Mining, Aug. 2025)  
**DOI:** 10.1145/3690624.3709172  
**arXiv ID:** 2506.11107  
**Coder:** AI_ASSISTED (Antigravity Research-Engineering Assistant)  
**Codebook Version:** `coding_codebook_v1.0_LOCKED.md`  
**Date:** 2026-08-26  

---

# 1. PAPER Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `paper_id` | `PAPER_KT070` | AUTHOR_STATED | PUBLISHER_METADATA | ACM SIGKDD 2025 |
| `legacy_id` | `KT070` | AUTHOR_STATED | METADATA | Seed corpus identifier |
| `title` | Denoising Programming Knowledge Tracing with a Code Graph-Based Tuning Adapter | AUTHOR_STATED | PUBLISHER_METADATA | ACM KDD article title |
| `publication_year` | 2025 | AUTHOR_STATED | PUBLISHER_METADATA | KDD '25 proceedings published Aug 2025 |
| `venue` | KDD | AUTHOR_STATED | PUBLISHER_METADATA | ACM SIGKDD peer-reviewed conference |
| `publication_type` | `CONFERENCE_PAPER` | AUTHOR_STATED | PUBLISHER_METADATA | Full conference proceedings paper |
| `peer_reviewed` | `YES` | AUTHOR_STATED | PUBLISHER_METADATA | Official ACM KDD peer-reviewed publication |
| `doi` | 10.1145/3690624.3709172 | AUTHOR_STATED | PUBLISHER_METADATA | Official ACM DOI |
| `arxiv_id` | 2506.11107 | AUTHOR_STATED | PUBLISHER_METADATA | Official arXiv preprint |
| `kt_central_task` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Sequential programming response prediction & denoising state tracing |
| `G_criterion` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Cluster-aware GCN built on code graph adapter for programming KT |
| `S_criterion` | `NO` | AUTHOR_STATED | PAPER_FULLTEXT | Supervised denoising and navigation regularization loss only |
| `corpus_tier` | `PRIMARY_CORE` | REVIEWER_INFERRED | PAPER_FULLTEXT | Satisfies G-criterion (`PRIMARY_CORE`) |
| `coding_completeness` | `FULLTEXT_CODED` | REVIEWER_INFERRED | PAPER_FULLTEXT | Peer-reviewed ACM conference full text inspected |
| `third_party_implementation_available` | `YES` | METADATA | SECONDARY | Tracked in pyKT / KT benchmark repositories |

---

# 2. MODEL Level Coding (`MODEL_KT070_Coda`)

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `model_id` | `MODEL_KT070_Coda` | AUTHOR_STATED | PAPER_FULLTEXT | Primary Coda code graph tuning adapter formulation |
| `graph_source` | `AST_CODE_GRAPH, SIMILARITY, CLUSTER_GRAPH` | AUTHOR_STATED | PAPER_FULLTEXT | Cluster-aware code graph constructed from programming submissions and AST syntax structures |
| `graph_provenance` | `JOINTLY_LEARNED_TRAINING` | AUTHOR_STATED | PAPER_FULLTEXT | Cluster-aware code graph adapter updated jointly with backbone PKT model |
| `graph_leakage_risk` | `LOW` | REVIEWER_INFERRED | PAPER_FULLTEXT | Denoising code graph adapter updates strictly preserve submission sequence timestamps |
| `graph_representation` | `CODE_AST_GRAPH, CLUSTER_GRAPH, ITEM_KC_BIPARTITE` | AUTHOR_STATED | PAPER_FULLTEXT | Code AST structure graph with cluster-aware noise identification nodes |
| `directed` | `Y` | AUTHOR_STATED | PAPER_FULLTEXT | Directed AST syntax and denoising signal flow |
| `typed_edges` | `Y` | AUTHOR_STATED | PAPER_FULLTEXT | Multiple noise signal and syntax relation edge types |
| `gnn_encoder` | `GRAPH_CONVOLUTIONAL_NETWORK` | AUTHOR_STATED | PAPER_FULLTEXT | Cluster-aware Graph Convolutional Network encoder |
| `temporal_backbone` | `RNN_LSTM_GRU` | AUTHOR_STATED | PAPER_FULLTEXT | Plug-and-play adapter tuning backbone for sequential PKT models |
| `fusion_type` | `ADAPTER_TUNING, CONCAT` | AUTHOR_STATED | PAPER_FULLTEXT | Model-agnostic adapter fusion injecting code graph denoising representations into backbone PKT states |
| `fusion_location` | `INPUT, HIDDEN_STATE, AUXILIARY_LOSS` | AUTHOR_STATED | PAPER_FULLTEXT | Backbone input, hidden state, and denoising regularization loss layers |
| `ssl_family` | `NONE` | AUTHOR_STATED | PAPER_FULLTEXT | Supervised denoising and navigation regularization loss only |
| `augmentation_type` | `DENOISING_MASK` | AUTHOR_STATED | PAPER_FULLTEXT | Code submission denoising signal filtering |
| `educational_structure_preservation` | `YES_EXPLICIT` | AUTHOR_STATED | PAPER_FULLTEXT | Preserves AST code syntax constraints while filtering noisy submission signals |

---

# 3. EXPERIMENT Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `experiment_id` | `EXP_KT070_MAIN` | AUTHOR_STATED | PAPER_FULLTEXT | Main experimental evaluation |
| `datasets` | CodeNet, OJ, Python-Tuples | AUTHOR_STATED | PAPER_FULLTEXT | Benchmark programming educational datasets evaluated |
| `split_type` | `LEARNER_BASED` | AUTHOR_STATED | PAPER_FULLTEXT | Student history partition into train/test splits |
| `n_seeds` | 5 | AUTHOR_STATED | PAPER_FULLTEXT | Performance averaged over 5 random seeds (CB13) |
| `resampling_repeats` | 1 | REVIEWER_INFERRED | PAPER_FULLTEXT | Single train/test data split repeated across seeds (CB13) |
| `repeated_run_unit` | `SEED_REPETITION` | REVIEWER_INFERRED | PAPER_FULLTEXT | Seed repetition unit (CB13) |
| `sparse_concept_ontology` | `GENERIC_DATA_SPARSITY` | REVIEWER_INFERRED | PAPER_FULLTEXT | Evaluates code graph denoising under sparse and noisy submission data conditions |
| `metrics` | ROC-AUC, ACC | AUTHOR_STATED | PAPER_FULLTEXT | Prediction accuracy and ROC-AUC metrics |
| `statistical_testing` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | Significance tests omitted |
| `calibration_metrics` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | ECE omitted |
| `computational_reporting` | `YES_FULL` | AUTHOR_STATED | PAPER_FULLTEXT | Reports formal lightweight tuning adapter time/memory overhead curves |

---

# 4. Quality Scoring (QA1–QA8)

| QA Criterion | Score (0-2) | Justification |
|---|---|---|
| **QA1 Task Clarity** | 2 | Clear formulation of code graph denoising adapter for programming knowledge tracing. |
| **QA2 Data Transparency** | 2 | Evaluates on public benchmark programming datasets (CodeNet, OJ, Python-Tuples). |
| **QA3 Split/Leakage Transparency** | 2 | Denoising adapter strictly respects submission sequence timestamps; low leakage risk. |
| **QA4 Baseline/Ablation Adequacy** | 2 | Evaluates against DKT, SAKT, AKT, pyKT baselines and performs denoising module ablation. |
| **QA5 Statistical Uncertainty** | 1 | Reports mean performance across seeds; formal significance testing omitted. |
| **QA6 Author Artifacts** | 2 | Official KDD proceedings paper and arXiv preprint verified. |
| **QA7 Sparse Construct Validity** | 1 | Motivates model via submission noise and data sparsity, but lacks zero-exposure cold-start KC evaluation. |
| **QA8 Computational Transparency** | 2 | Reports formal time/memory overhead of lightweight code graph tuning adapter. |

**Raw Quality Score:** 14 / 16  
**Normalized Quality:** 0.8750 (**HIGH Quality**)
