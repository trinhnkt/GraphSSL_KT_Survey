# KT010 — GIKT Coding Record (v0.4 PILOT)

**Paper ID:** PAPER_KT010  
**Legacy ID:** KT010  
**Title:** GIKT: A Graph-Based Interaction Model for Knowledge Tracing  
**Authors:** Yang Yang, Jian Shen, Yanru Qu, Yunfei Liu, Kerong Wang, Yaoming Zhu, Weinan Zhang, Yong Yu  
**Venue:** ECML-PKDD 2020 (Springer LNCS Vol. 12458, pp. 299–315, 2021)  
**DOI:** 10.1007/978-3-030-67658-2_18  
**arXiv ID:** arXiv:2009.05991  
**Coder:** AI_ASSISTED (Antigravity Research-Engineering Assistant)  
**Codebook Version:** `coding_codebook_v0.4_PILOT.md`  
**Date:** 2026-08-10  

---

# 1. PAPER Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `paper_id` | `PAPER_KT010` | AUTHOR_STATED | PUBLISHER_METADATA | Springer LNCS / ECML-PKDD 2020 |
| `legacy_id` | `KT010` | AUTHOR_STATED | METADATA | Seed corpus identifier |
| `title` | GIKT: A Graph-Based Interaction Model for Knowledge Tracing | AUTHOR_STATED | PUBLISHER_METADATA | Article title |
| `publication_year` | 2021 | AUTHOR_STATED | PUBLISHER_METADATA | ECML-PKDD 2020 proceedings published 2021 |
| `venue` | ECML-PKDD | AUTHOR_STATED | PUBLISHER_METADATA | Peer-reviewed conference proceedings |
| `publication_type` | `CONFERENCE_PAPER` | AUTHOR_STATED | PUBLISHER_METADATA | Full conference paper |
| `peer_reviewed` | `YES` | AUTHOR_STATED | PUBLISHER_METADATA | Official ECML-PKDD proceedings publication |
| `doi` | 10.1007/978-3-030-67658-2_18 | AUTHOR_STATED | PUBLISHER_METADATA | Official DOI |
| `arxiv_id` | arXiv:2009.05991 | AUTHOR_STATED | AUTHOR_SUPPLEMENT | arXiv preprint |
| `kt_central_task` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Sequential learner-state estimation & performance prediction |
| `G_criterion` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Question–concept bipartite interaction graph with GCN embedding propagation |
| `S_criterion` | `NO` | AUTHOR_STATED | PAPER_FULLTEXT | Supervised cross-entropy KT loss only; no SSL pretext objective |
| `corpus_tier` | `PRIMARY_CORE` | REVIEWER_INFERRED | PAPER_FULLTEXT | `PRIMARY_CORE = KT AND (GRAPH_BASED OR SELF_SUPERVISED)` — satisfies G-criterion |
| `coding_completeness` | `FULLTEXT_CODED` | REVIEWER_INFERRED | PAPER_FULLTEXT | Peer-reviewed conference full text inspected |
| `third_party_implementation_available` | `YES` | METADATA | SECONDARY | Tracked in pyKT / KTPapers repositories |

---

# 2. MODEL Level Coding (`MODEL_KT010_GIKT`)

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `model_id` | `MODEL_KT010_GIKT` | AUTHOR_STATED | PAPER_FULLTEXT | Primary GIKT model formulation |
| `graph_source` | `Q_MATRIX, CO_OCCURRENCE` | AUTHOR_STATED | PAPER_FULLTEXT | Question-concept bipartite graph derived from Q-matrix and interaction relations |
| `graph_provenance` | `PRECOMPUTED_UNCLEAR_SPLIT` | REVIEWER_INFERRED | PAPER_FULLTEXT | Bipartite graph precomputed from dataset Q-matrix / logs without explicit split isolation |
| `graph_leakage_risk` | `POTENTIAL` | REVIEWER_INFERRED | PAPER_FULLTEXT | Precomputed question-concept bipartite adjacency provenance relative to test split is unspecified |
| `graph_representation` | `ITEM_KC_BIPARTITE, KC_KC` | AUTHOR_STATED | PAPER_FULLTEXT | Bipartite graph connecting Question/Exercise nodes to Concept/Skill nodes |
| `directed` | `N` | AUTHOR_STATED | PAPER_FULLTEXT | Undirected bipartite adjacency matrix $A$ between questions and concepts |
| `typed_edges` | `N` | AUTHOR_STATED | PAPER_FULLTEXT | Single membership relation type between questions and concepts |
| `gnn_encoder` | `GCN` | AUTHOR_STATED | PAPER_FULLTEXT | Graph Convolutional Network (GCN) embedding propagation over bipartite graph |
| `temporal_backbone` | `RNN_LSTM_GRU` | AUTHOR_STATED | PAPER_FULLTEXT | LSTM sequence layer + recap interaction module |
| `fusion_type` | `ATTENTION, CONCAT` | AUTHOR_STATED | PAPER_FULLTEXT | Attention recap module fusing question-concept GCN embeddings into student hidden states |
| `fusion_location` | `HIDDEN_STATE, PREDICTION` | AUTHOR_STATED | PAPER_FULLTEXT | Infuses GCN embeddings at sequence recap and prediction steps |
| `ssl_family` | `NONE` | AUTHOR_STATED | PAPER_FULLTEXT | Supervised cross-entropy KT loss only |
| `augmentation_type` | `NO_EXPLICIT_AUGMENTATION` | AUTHOR_STATED | PAPER_FULLTEXT | No data augmentation or pretext task |
| `educational_structure_preservation` | `YES_EXPLICIT` | AUTHOR_STATED | PAPER_FULLTEXT | Preserves Question-Concept mapping constraints during GCN propagation |

---

# 3. EXPERIMENT Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `experiment_id` | `EXP_KT010_MAIN` | AUTHOR_STATED | PAPER_FULLTEXT | Main experimental evaluation |
| `datasets` | ASSISTments2009, ASSISTments2012, Statics2011, Junyi | AUTHOR_STATED | PAPER_FULLTEXT | 4 public benchmark educational datasets evaluated |
| `split_type` | `LEARNER_BASED` | AUTHOR_STATED | PAPER_FULLTEXT | 80/20 train/test split across student interaction histories |
| `n_seeds` | 5 | AUTHOR_STATED | PAPER_FULLTEXT | Evaluated over 5 random seeds (CB13) |
| `resampling_repeats` | 1 | REVIEWER_INFERRED | PAPER_FULLTEXT | Single random train/test split repeated over 5 model seeds (CB13) |
| `repeated_run_unit` | `SEED_REPETITION` | REVIEWER_INFERRED | PAPER_FULLTEXT | Seed repetition unit (CB13) |
| `sparse_concept_ontology` | `GENERIC_DATA_SPARSITY` | REVIEWER_INFERRED | PAPER_FULLTEXT | Evaluated on datasets with generic sparsity; no zero-exposure cold-start KC partition evaluated |
| `metrics` | ROC-AUC, ACC | AUTHOR_STATED | PAPER_FULLTEXT | Prediction performance metrics |
| `statistical_testing` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | DeLong test / Wilcoxon signed-rank / Holm-Bonferroni correction not reported |
| `calibration_metrics` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | ECE and Brier Score omitted |
| `computational_reporting` | `LIMITED` | REVIEWER_INFERRED | PAPER_FULLTEXT | Mentions GCN propagation efficiency; formal runtime scaling curves omitted |

---

# 4. Quality Scoring (QA1–QA8)

| QA Criterion | Score (0-2) | Justification |
|---|---|---|
| **QA1 Task Clarity** | 2 | Clear formulation of question-concept GCN interaction & recap module. |
| **QA2 Data Transparency** | 2 | Evaluates on 4 public benchmark datasets (ASSISTments2009, ASSISTments2012, Statics2011, Junyi). |
| **QA3 Split/Leakage Transparency** | 1 | 80/20 split reported; precomputed question-concept bipartite adjacency temporal split isolation is unverified. |
| **QA4 Baseline/Ablation Adequacy** | 2 | Baseline models (DKT, DKVMN, SAKT, EKT) + ablation of GCN & recap modules. |
| **QA5 Statistical Uncertainty** | 1 | Reports mean performance across seeds; formal significance testing omitted. |
| **QA6 Author Artifacts** | 1 | Peer-reviewed ECML-PKDD proceedings paper + arXiv preprint full text verified. |
| **QA7 Sparse Construct Validity** | 1 | Motivates model via data sparsity, but lacks isolated zero-exposure KC cold-start evaluation protocol. |
| **QA8 Computational Transparency** | 1 | Describes GCN layer complexity; formal runtime/memory scaling bounds omitted. |

**Raw Quality Score:** 11 / 16  
**Normalized Quality:** 0.6875 (**MODERATE Quality**)

---

# 5. Methodological Summary & Codebook Stress-Test Insights

1. **Pure Graph-KT (`PRIMARY_CORE` via G-criterion):** GIKT stress-tests the codebook's pure Graph-KT classification (`G_criterion = Y`, `S_criterion = N`), demonstrating that GCN embedding propagation over question-concept bipartite graphs cleanly enters `PRIMARY_CORE`.
2. **Bipartite Representation (`ITEM_KC_BIPARTITE`):** Validates the `ITEM_KC_BIPARTITE` graph representation and `Q_MATRIX` graph source values.
3. **CB13 Verification (`resampling_repeats` vs `n_seeds`):** Coded `n_seeds = 5` and `resampling_repeats = 1` (`SEED_REPETITION`).
4. **CB16 Verification (`coding_completeness`):** Marked `FULLTEXT_CODED` from full conference proceedings paper inspection.
