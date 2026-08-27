# KT056 — Long/Short-Term State Graph Coding Record (v1.0 LOCKED)

**Paper ID:** PAPER_KT056  
**Legacy ID:** KT056  
**Title:** Exploring Long- and Short-Term Knowledge State Graph Representations with Adaptive Fusion for Knowledge Tracing  
**Authors:** Ganfeng Yu, Zhiwen Xie, Guangyou Zhou, Zhuo Zhao, Jimmy Xiangji Huang  
**Venue:** Information Processing & Management, Vol. 62, Issue 3, Article 104074, May 2025  
**DOI:** 10.1016/j.ipm.2025.104074  
**arXiv ID:** NR  
**Coder:** AI_ASSISTED (Antigravity Research-Engineering Assistant)  
**Codebook Version:** `coding_codebook_v1.0_LOCKED.md`  
**Date:** 2026-08-26  

---

# 1. PAPER Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `paper_id` | `PAPER_KT056` | AUTHOR_STATED | PUBLISHER_METADATA | IP&M 2025 |
| `legacy_id` | `KT056` | AUTHOR_STATED | METADATA | Seed corpus identifier |
| `title` | Exploring Long- and Short-Term Knowledge State Graph Representations with Adaptive Fusion for Knowledge Tracing | AUTHOR_STATED | PUBLISHER_METADATA | Published journal title |
| `publication_year` | 2025 | AUTHOR_STATED | PUBLISHER_METADATA | IP&M Vol. 62 published May 2025 |
| `venue` | Information Processing & Management | AUTHOR_STATED | PUBLISHER_METADATA | Elsevier peer-reviewed journal |
| `publication_type` | `JOURNAL_ARTICLE` | AUTHOR_STATED | PUBLISHER_METADATA | Full journal article |
| `peer_reviewed` | `YES` | AUTHOR_STATED | PUBLISHER_METADATA | Official journal publication |
| `doi` | 10.1016/j.ipm.2025.104074 | AUTHOR_STATED | PUBLISHER_METADATA | Official DOI |
| `arxiv_id` | `NR` | AUTHOR_STATED | PUBLISHER_METADATA | Direct journal article |
| `kt_central_task` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Sequential learner response prediction & multi-temporal state tracking |
| `G_criterion` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Long- and short-term knowledge state graph representations with adaptive GNN fusion |
| `S_criterion` | `NO` | AUTHOR_STATED | PAPER_FULLTEXT | Supervised prediction loss only |
| `corpus_tier` | `PRIMARY_CORE` | REVIEWER_INFERRED | PAPER_FULLTEXT | Satisfies G-criterion (`PRIMARY_CORE`) |
| `coding_completeness` | `FULLTEXT_CODED` | REVIEWER_INFERRED | PAPER_FULLTEXT | Peer-reviewed journal full text inspected |
| `third_party_implementation_available` | `YES` | METADATA | SECONDARY | Tracked in pyKT / KT benchmark repositories |

---

# 2. MODEL Level Coding (`MODEL_KT056_LST_GRAPH`)

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `model_id` | `MODEL_KT056_LST_GRAPH` | AUTHOR_STATED | PAPER_FULLTEXT | Primary Long/Short-Term State Graph KT formulation |
| `graph_source` | `SEQUENTIAL_TRANSITION, LEARNED_FROM_INTERACTIONS` | AUTHOR_STATED | PAPER_FULLTEXT | Long-term and short-term state graphs derived from interaction sequence windows |
| `graph_provenance` | `JOINTLY_LEARNED_TRAINING` | AUTHOR_STATED | PAPER_FULLTEXT | Long/short-term graph representations updated dynamically along interaction windows |
| `graph_leakage_risk` | `LOW` | REVIEWER_INFERRED | PAPER_FULLTEXT | Windowed graph representations strictly preserve interaction sequence timestamps |
| `graph_representation` | `DYNAMIC_TEMPORAL, DUAL_GRAPH` | AUTHOR_STATED | PAPER_FULLTEXT | Dual-scale long/short-term state graphs representing learner knowledge dynamics |
| `directed` | `Y` | AUTHOR_STATED | PAPER_FULLTEXT | Directed temporal transition edges across windows |
| `typed_edges` | `Y` | AUTHOR_STATED | PAPER_FULLTEXT | Multiple temporal scale relation types |
| `gnn_encoder` | `GRAPH_ATTENTION_HYBRID` | AUTHOR_STATED | PAPER_FULLTEXT | Adaptive Graph Attention encoder for long/short-term graph fusion |
| `temporal_backbone` | `RNN_LSTM_GRU` | AUTHOR_STATED | PAPER_FULLTEXT | GRU sequence backbone for temporal state tracking |
| `fusion_type` | `ADAPTIVE_FUSION, ATTENTION` | AUTHOR_STATED | PAPER_FULLTEXT | Adaptive temporal dynamics fusion gate combining long-term and short-term graph states |
| `fusion_location` | `HIDDEN_STATE` | AUTHOR_STATED | PAPER_FULLTEXT | Injected at recurrent sequence hidden state update step |
| `ssl_family` | `NONE` | AUTHOR_STATED | PAPER_FULLTEXT | Supervised prediction loss only |
| `augmentation_type` | `NO_EXPLICIT_AUGMENTATION` | AUTHOR_STATED | PAPER_FULLTEXT | No data augmentation |
| `educational_structure_preservation` | `YES_EXPLICIT` | AUTHOR_STATED | PAPER_FULLTEXT | Preserves multi-temporal scale learning memory and decay constraints |

---

# 3. EXPERIMENT Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `experiment_id` | `EXP_KT056_MAIN` | AUTHOR_STATED | PAPER_FULLTEXT | Main experimental evaluation |
| `datasets` | ASSISTments2009, ASSISTments2017, EdNet | AUTHOR_STATED | PAPER_FULLTEXT | Benchmark educational datasets evaluated |
| `split_type` | `LEARNER_BASED` | AUTHOR_STATED | PAPER_FULLTEXT | Student history partition into train/test splits |
| `n_seeds` | 5 | AUTHOR_STATED | PAPER_FULLTEXT | Performance averaged over 5 random seeds (CB13) |
| `resampling_repeats` | 1 | REVIEWER_INFERRED | PAPER_FULLTEXT | Single train/test data split repeated across seeds (CB13) |
| `repeated_run_unit` | `SEED_REPETITION` | REVIEWER_INFERRED | PAPER_FULLTEXT | Seed repetition unit (CB13) |
| `sparse_concept_ontology` | `GENERIC_DATA_SPARSITY` | REVIEWER_INFERRED | PAPER_FULLTEXT | Evaluates long/short-term state graph modeling on interaction data |
| `metrics` | ROC-AUC, ACC | AUTHOR_STATED | PAPER_FULLTEXT | Prediction accuracy and ROC-AUC metrics |
| `statistical_testing` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | Significance tests omitted |
| `calibration_metrics` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | ECE omitted |
| `computational_reporting` | `LIMITED` | REVIEWER_INFERRED | PAPER_FULLTEXT | Scaling bounds omitted |

---

# 4. Quality Scoring (QA1–QA8)

| QA Criterion | Score (0-2) | Justification |
|---|---|---|
| **QA1 Task Clarity** | 2 | Clear formulation of long/short-term state graph representations with adaptive temporal dynamics. |
| **QA2 Data Transparency** | 2 | Evaluates on public benchmark datasets (ASSIST09, ASSIST17, EdNet). |
| **QA3 Split/Leakage Transparency** | 2 | Windowed temporal graph representations strictly respect interaction sequence timestamps; low leakage risk. |
| **QA4 Baseline/Ablation Adequacy** | 2 | Evaluates against DKT, SAKT, AKT, GKT and performs long-term vs short-term graph ablation. |
| **QA5 Statistical Uncertainty** | 1 | Reports mean performance across seeds; formal significance testing omitted. |
| **QA6 Author Artifacts** | 1 | Official journal full text verified; author code repository unverified. |
| **QA7 Sparse Construct Validity** | 1 | Motivates model via multi-temporal state graph modeling, but lacks zero-exposure cold-start KC evaluation. |
| **QA8 Computational Transparency** | 1 | Explains adaptive GNN fusion complexity; formal runtime scaling bounds omitted. |

**Raw Quality Score:** 12 / 16  
**Normalized Quality:** 0.7500 (**MODERATE Quality**)
