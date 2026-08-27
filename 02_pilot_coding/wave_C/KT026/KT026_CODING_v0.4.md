# KT026 — Pre-Training Question Embeddings Coding Record (v0.4 PILOT)

**Paper ID:** PAPER_KT026  
**Legacy ID:** KT026  
**Title:** Improving Knowledge Tracing via Pre-Training Question Embeddings  
**Authors:** Yunfei Liu, Yang Yang, Xianyu Chen, Jian Shen, Haifeng Zhang, Yong Yu  
**Venue:** IJCAI 2020 (pp. 1577–1583, July 2020)  
**DOI:** 10.24963/ijcai.2020/219  
**arXiv ID:** arXiv:2012.05031  
**Coder:** AI_ASSISTED (Antigravity Research-Engineering Assistant)  
**Codebook Version:** `coding_codebook_v0.4_PILOT.md`  
**Date:** 2026-08-26  

---

# 1. PAPER Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `paper_id` | `PAPER_KT026` | AUTHOR_STATED | PUBLISHER_METADATA | IJCAI 2020 |
| `legacy_id` | `KT026` | AUTHOR_STATED | METADATA | Seed corpus identifier |
| `title` | Improving Knowledge Tracing via Pre-Training Question Embeddings | AUTHOR_STATED | PUBLISHER_METADATA | IJCAI published article title |
| `publication_year` | 2020 | AUTHOR_STATED | PUBLISHER_METADATA | IJCAI 2020 proceedings published July 2020 |
| `venue` | IJCAI | AUTHOR_STATED | PUBLISHER_METADATA | International Joint Conference on Artificial Intelligence |
| `publication_type` | `CONFERENCE_PAPER` | AUTHOR_STATED | PUBLISHER_METADATA | Full conference proceedings paper |
| `peer_reviewed` | `YES` | AUTHOR_STATED | PUBLISHER_METADATA | Official IJCAI 2020 peer-reviewed publication |
| `doi` | 10.24963/ijcai.2020/219 | AUTHOR_STATED | PUBLISHER_METADATA | Official IJCAI DOI |
| `arxiv_id` | arXiv:2012.05031 | AUTHOR_STATED | AUTHOR_SUPPLEMENT | arXiv open-access preprint |
| `kt_central_task` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Sequential learner response prediction & knowledge state tracing |
| `G_criterion` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Pre-trains question embeddings from question-skill bipartite graph using product-based neural networks |
| `S_criterion` | `NO` | REVIEWER_INFERRED | PAPER_FULLTEXT | Generic question embedding pretraining on bipartite graph, NOT a self-supervised contrastive/generative pretext task during KT sequence tracing |
| `corpus_tier` | `PRIMARY_CORE` | REVIEWER_INFERRED | PAPER_FULLTEXT | `PRIMARY_CORE = KT AND (GRAPH_BASED OR SELF_SUPERVISED)` — satisfies G-criterion via graph-derived pre-trained representations |
| `coding_completeness` | `FULLTEXT_CODED` | REVIEWER_INFERRED | PAPER_FULLTEXT | Peer-reviewed IJCAI 2020 proceedings full text inspected |
| `third_party_implementation_available` | `YES` | METADATA | SECONDARY | Tracked in pyKT / KT benchmark literature |

---

# 2. MODEL Level Coding (`MODEL_KT026_PRETRAIN`)

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `model_id` | `MODEL_KT026_PRETRAIN` | AUTHOR_STATED | PAPER_FULLTEXT | Primary Pre-trained Question Embedding KT model formulation |
| `graph_source` | `Q_MATRIX, ITEM_KC_BIPARTITE` | AUTHOR_STATED | PAPER_FULLTEXT | Question-skill bipartite graph constructed from Q-matrix and question difficulty relations |
| `graph_provenance` | `PRECOMPUTED_UNCLEAR_SPLIT` | REVIEWER_INFERRED | PAPER_FULLTEXT | Bipartite graph precomputed prior to sequence tracing without explicit train-only isolation reporting |
| `graph_leakage_risk` | `POTENTIAL` | REVIEWER_INFERRED | PAPER_FULLTEXT | Bipartite graph question difficulty/skill pre-training provenance relative to test split is unspecified |
| `graph_representation` | `ITEM_KC_BIPARTITE` | AUTHOR_STATED | PAPER_FULLTEXT | Bipartite graph connecting Question nodes to Skill/Concept nodes |
| `directed` | `N` | AUTHOR_STATED | PAPER_FULLTEXT | Undirected bipartite membership graph |
| `typed_edges` | `N` | AUTHOR_STATED | PAPER_FULLTEXT | Single question-skill mapping relation type |
| `gnn_encoder` | `NONE` | AUTHOR_STATED | PAPER_FULLTEXT | Product-based neural network (PNN) matrix factorization for pre-training embeddings (CB14: Graph-KT gateway without GNN) |
| `temporal_backbone` | `RNN_LSTM_GRU` | AUTHOR_STATED | PAPER_FULLTEXT | LSTM backbone initialized with pre-trained question embeddings |
| `fusion_type` | `GRAPH_INITIALIZATION` | AUTHOR_STATED | PAPER_FULLTEXT | Pre-trained graph representations initialize sequence embedding layer |
| `fusion_location` | `INPUT` | AUTHOR_STATED | PAPER_FULLTEXT | Injected at input layer prior to temporal sequence processing |
| `ssl_family` | `NONE` | REVIEWER_INFERRED | PAPER_FULLTEXT | Generic graph feature pre-training; no self-supervised pretext task loss during KT sequence tracing |
| `augmentation_type` | `NO_EXPLICIT_AUGMENTATION` | AUTHOR_STATED | PAPER_FULLTEXT | No data augmentation or pretext task |
| `educational_structure_preservation` | `YES_EXPLICIT` | AUTHOR_STATED | PAPER_FULLTEXT | Preserves question-skill associations and difficulty relations during pre-training |

---

# 3. EXPERIMENT Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `experiment_id` | `EXP_KT026_MAIN` | AUTHOR_STATED | PAPER_FULLTEXT | Main experimental evaluation |
| `datasets` | ASSISTments2009, Statics2011, Junyi | AUTHOR_STATED | PAPER_FULLTEXT | Benchmark educational datasets evaluated |
| `split_type` | `LEARNER_BASED` | AUTHOR_STATED | PAPER_FULLTEXT | Student history partition into train/test splits |
| `n_seeds` | 5 | AUTHOR_STATED | PAPER_FULLTEXT | Evaluated over 5 random seeds (CB13) |
| `resampling_repeats` | 1 | REVIEWER_INFERRED | PAPER_FULLTEXT | Single train/test data split repeated across seeds (CB13) |
| `repeated_run_unit` | `SEED_REPETITION` | REVIEWER_INFERRED | PAPER_FULLTEXT | Seed repetition unit (CB13) |
| `sparse_concept_ontology` | `GENERIC_DATA_SPARSITY` | REVIEWER_INFERRED | PAPER_FULLTEXT | Evaluated on datasets with generic interaction sparsity; no zero-exposure cold-start KC split evaluated |
| `metrics` | ROC-AUC, ACC | AUTHOR_STATED | PAPER_FULLTEXT | Prediction accuracy and ROC-AUC metrics |
| `statistical_testing` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | DeLong / Wilcoxon significance tests not reported |
| `calibration_metrics` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | ECE and Brier Score omitted |
| `computational_reporting` | `LIMITED` | REVIEWER_INFERRED | PAPER_FULLTEXT | Reports pre-training overhead; formal scaling bounds omitted |

---

# 4. Quality Scoring (QA1–QA8)

| QA Criterion | Score (0-2) | Justification |
|---|---|---|
| **QA1 Task Clarity** | 2 | Clear formulation of graph-derived question embedding pre-training for KT. |
| **QA2 Data Transparency** | 2 | Evaluates on public benchmark datasets (ASSIST09, Statics11, Junyi). |
| **QA3 Split/Leakage Transparency** | 1 | Student train/test split reported; precomputed bipartite graph train-only isolation unverified. |
| **QA4 Baseline/Ablation Adequacy** | 2 | Evaluates against DKT, DKVMN, EKT and performs pre-training embedding component ablation. |
| **QA5 Statistical Uncertainty** | 1 | Reports mean performance across seeds; formal significance testing omitted. |
| **QA6 Author Artifacts** | 1 | Official IJCAI proceedings full text verified; official repository not author-verified. |
| **QA7 Sparse Construct Validity** | 1 | Motivates question embedding quality under sparse interactions, but lacks isolated zero-exposure KC cold-start protocol. |
| **QA8 Computational Transparency** | 1 | Mentions offline pre-training overhead; formal runtime/memory scaling bounds omitted. |

**Raw Quality Score:** 11 / 16  
**Normalized Quality:** 0.6875 (**MODERATE Quality**)

---

# 5. Methodological Summary & Codebook Stress-Test Insights

1. **Pretraining vs SSL Rule Resolution:** Stress-tests the critical codebook boundary between generic pretraining and self-supervised learning (`S_criterion`). Pre-training question embeddings from bipartite graphs via matrix factorization satisfies `G_criterion = Y` (`PRIMARY_CORE`), but receives `S_criterion = N` and `ssl_family = NONE` because it lacks an active self-supervised pretext task loss during temporal sequence modeling.
2. **Graph Initialization Fusion (`GRAPH_INITIALIZATION`):** Validates `fusion_type = GRAPH_INITIALIZATION` where graph structure pre-trains input vectors prior to temporal RNN processing.
