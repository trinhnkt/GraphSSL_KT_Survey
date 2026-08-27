# KT011 — Bi-CLKT Coding Record (v0.4 PILOT)

**Paper ID:** PAPER_KT011  
**Legacy ID:** KT011  
**Title:** Bi-CLKT: Bi-Graph Contrastive Learning Based Knowledge Tracing  
**Authors:** Xiangyu Song, Jianxin Li, Qiuyu Lei, Wei Zhao, Yunliang Chen, Ajmal Saeed Mian  
**Venue:** Knowledge-Based Systems (Vol. 241, Article 108274, 2022)  
**DOI:** 10.1016/j.knosys.2022.108274  
**arXiv ID:** 2201.09020  
**Coder:** AI_ASSISTED (Antigravity Research-Engineering Assistant)  
**Codebook Version:** `coding_codebook_v0.4_PILOT.md`  
**Date:** 2026-08-10  

---

# 1. PAPER Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `paper_id` | `PAPER_KT011` | AUTHOR_STATED | PUBLISHER_METADATA | Elsevier / KBS 2022 |
| `legacy_id` | `KT011` | AUTHOR_STATED | METADATA | Seed corpus identifier |
| `title` | Bi-CLKT: Bi-Graph Contrastive Learning Based Knowledge Tracing | AUTHOR_STATED | PUBLISHER_METADATA | Title |
| `publication_year` | 2022 | AUTHOR_STATED | PUBLISHER_METADATA | Published 2022 |
| `venue` | Knowledge-Based Systems | AUTHOR_STATED | PUBLISHER_METADATA | Elsevier journal |
| `publication_type` | `JOURNAL_ARTICLE` | AUTHOR_STATED | PUBLISHER_METADATA | Peer-reviewed journal paper |
| `peer_reviewed` | `YES` | AUTHOR_STATED | PUBLISHER_METADATA | Official Elsevier KBS publication |
| `doi` | 10.1016/j.knosys.2022.108274 | AUTHOR_STATED | PUBLISHER_METADATA | Official DOI |
| `arxiv_id` | 2201.09020 | AUTHOR_STATED | AUTHOR_SUPPLEMENT | arXiv preprint version |
| `kt_central_task` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Sequential learner-state prediction & performance forecasting |
| `G_criterion` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Exercise-to-Exercise (E2E) relational subgraphs & concept graphs |
| `S_criterion` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Dual-level contrastive learning (node-level & graph-level contrastive losses) |
| `corpus_tier` | `PRIMARY_CORE` | REVIEWER_INFERRED | PAPER_FULLTEXT | `PRIMARY_CORE = KT AND (GRAPH_BASED OR SELF_SUPERVISED)` — satisfies BOTH |
| `coding_completeness` | `FULLTEXT_CODED` | REVIEWER_INFERRED | PAPER_FULLTEXT | Peer-reviewed publication text & arXiv full text inspected |
| `third_party_implementation_available` | `YES` | METADATA | SECONDARY | Tracked in pyKT / KTPapers repositories |

---

# 2. MODEL Level Coding

Paper KT011 evaluates two main architectural variants based on the prediction layer: `Bi-CLKT-RNN` and `Bi-CLKT-MANN`. Both share the underlying Bi-Graph contrastive representation learning framework.

## Model 1: `MODEL_KT011_BiCLKT_RNN`

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `model_id` | `MODEL_KT011_BiCLKT_RNN` | AUTHOR_STATED | PAPER_FULLTEXT | Primary Bi-CLKT variant using RNN prediction backbone |
| `graph_source` | `CO_OCCURRENCE` | AUTHOR_STATED | PAPER_FULLTEXT | Exercise-to-Exercise (E2E) relational subgraph & Question-KC bipartite graph |
| `graph_provenance` | `PRECOMPUTED_UNCLEAR_SPLIT` | REVIEWER_INFERRED | PAPER_FULLTEXT | Interaction graph precomputed from log data without explicit train-only isolation report |
| `graph_leakage_risk` | `POTENTIAL` | REVIEWER_INFERRED | PAPER_FULLTEXT | Precomputed E2E graph provenance relative to test sequences is unspecified |
| `graph_representation` | `ITEM_ITEM, KC_KC, ITEM_KC_BIPARTITE` | AUTHOR_STATED | PAPER_FULLTEXT | Dual-graph framing: Exercise-to-Exercise subgraphs + Concept graphs |
| `directed` | `Y` | AUTHOR_STATED | PAPER_FULLTEXT | Directed E2E relational edges based on interaction sequence order |
| `typed_edges` | `Y` | AUTHOR_STATED | PAPER_FULLTEXT | Multiple relation types (exercise-exercise transition vs exercise-concept association) |
| `gnn_encoder` | `GCN` | AUTHOR_STATED | PAPER_FULLTEXT | Subgraph GNN encoder for node-level exercise & graph-level concept representations |
| `temporal_backbone` | `RNN_LSTM_GRU` | AUTHOR_STATED | PAPER_FULLTEXT | Recurrent Neural Network (LSTM/GRU) prediction backbone |
| `fusion_type` | `CONCAT` | AUTHOR_STATED | PAPER_FULLTEXT | Concatenates contrastive exercise/concept embeddings into temporal state |
| `fusion_location` | `INPUT` | AUTHOR_STATED | PAPER_FULLTEXT | Infuses contrastive representations at model input/hidden layer |
| `ssl_family` | `MULTIVIEW_CONTRASTIVE, GRAPH_CONTRASTIVE` | AUTHOR_STATED | PAPER_FULLTEXT | Two-layer contrastive scheme: node-level exercise loss + graph-level concept loss |
| `augmentation_type` | `SUBGRAPH_SAMPLE, NODE_DROP, EDGE_DROP` | AUTHOR_STATED | PAPER_FULLTEXT | Subgraph sampling & relational perturbations for dual contrastive views |
| `educational_structure_preservation` | `YES_EXPLICIT` | AUTHOR_STATED | PAPER_FULLTEXT | Explicitly preserves exercise-concept bipartite constraints in joint loss |

## Model 2: `MODEL_KT011_BiCLKT_MANN`

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `model_id` | `MODEL_KT011_BiCLKT_MANN` | AUTHOR_STATED | PAPER_FULLTEXT | Bi-CLKT variant using Memory-Augmented Neural Network prediction backbone |
| `graph_source` | `CO_OCCURRENCE` | AUTHOR_STATED | PAPER_FULLTEXT | E2E relational subgraphs & Question-KC graph |
| `graph_provenance` | `PRECOMPUTED_UNCLEAR_SPLIT` | REVIEWER_INFERRED | PAPER_FULLTEXT | Interaction graph precomputed from dataset logs |
| `graph_leakage_risk` | `POTENTIAL` | REVIEWER_INFERRED | PAPER_FULLTEXT | Unclear temporal split isolation for precomputed adjacency |
| `graph_representation` | `ITEM_ITEM, KC_KC, ITEM_KC_BIPARTITE` | AUTHOR_STATED | PAPER_FULLTEXT | Dual-graph structure |
| `directed` | `Y` | AUTHOR_STATED | PAPER_FULLTEXT | Directed E2E transitions |
| `typed_edges` | `Y` | AUTHOR_STATED | PAPER_FULLTEXT | Typed relations across exercise subgraphs and concept graphs |
| `gnn_encoder` | `GCN` | AUTHOR_STATED | PAPER_FULLTEXT | Subgraph GNN encoder |
| `temporal_backbone` | `MEMORY_NETWORK` | AUTHOR_STATED | PAPER_FULLTEXT | Memory-Augmented Neural Network (MANN) prediction layer |
| `fusion_type` | `ATTENTION` | AUTHOR_STATED | PAPER_FULLTEXT | Memory read/write attention fusion |
| `fusion_location` | `HIDDEN_STATE` | AUTHOR_STATED | PAPER_FULLTEXT | Memory state update loop |
| `ssl_family` | `MULTIVIEW_CONTRASTIVE, GRAPH_CONTRASTIVE` | AUTHOR_STATED | PAPER_FULLTEXT | Node-level & graph-level joint contrastive loss |
| `augmentation_type` | `SUBGRAPH_SAMPLE, NODE_DROP` | AUTHOR_STATED | PAPER_FULLTEXT | Subgraph view augmentations |
| `educational_structure_preservation` | `YES_EXPLICIT` | AUTHOR_STATED | PAPER_FULLTEXT | Joint contrastive loss with structure constraints |

---

# 3. EXPERIMENT Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `experiment_id` | `EXP_KT011_MAIN` | AUTHOR_STATED | PAPER_FULLTEXT | Main experimental evaluation |
| `datasets` | ASSISTments2009, ASSISTments2012, Junyi, Statics2011 | AUTHOR_STATED | PAPER_FULLTEXT | Four real-world benchmark datasets evaluated |
| `split_type` | `LEARNER_BASED` | AUTHOR_STATED | PAPER_FULLTEXT | 80/20 train/test split across student interaction histories |
| `n_seeds` | 5 | AUTHOR_STATED | PAPER_FULLTEXT | Evaluated over 5 random seeds (CB13) |
| `resampling_repeats` | 1 | REVIEWER_INFERRED | PAPER_FULLTEXT | Single fixed random split evaluated across 5 seeds (CB13) |
| `repeated_run_unit` | `SEED_REPETITION` | REVIEWER_INFERRED | PAPER_FULLTEXT | Seed repetition unit (CB13) |
| `sparse_concept_ontology` | `GENERIC_DATA_SPARSITY` | REVIEWER_INFERRED | PAPER_FULLTEXT | Evaluated on full datasets with generic sparsity; no zero-exposure cold-start KC partition |
| `metrics` | ROC-AUC, ACC, RMSE, MAE | AUTHOR_STATED | PAPER_FULLTEXT | Performance prediction metrics |
| `statistical_testing` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | DeLong test / Wilcoxon signed-rank / Holm-Bonferroni correction not reported |
| `calibration_metrics` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | ECE (Expected Calibration Error) and Brier Score not reported |
| `computational_reporting` | `LIMITED` | REVIEWER_INFERRED | PAPER_FULLTEXT | Baseline training time reported; GPU memory / scalability bounds omitted |

---

# 4. Quality Scoring (QA1–QA8)

| QA Criterion | Score (0-2) | Justification |
|---|---|---|
| **QA1 Task Clarity** | 2 | Clear formulation of KT task, exercise representations, and prediction objective. |
| **QA2 Data Transparency** | 2 | Uses 4 public benchmark datasets (ASSISTments2009, ASSISTments2012, Junyi, Statics2011). |
| **QA3 Split/Leakage Transparency** | 1 | 80/20 split reported; precomputed E2E graph temporal split isolation is unverified (`POTENTIAL` risk). |
| **QA4 Baseline/Ablation Adequacy** | 2 | Comprehensive baselines (DKT, DKVMN, SAKT, GKT, GIKT) + ablation of node/graph contrastive components. |
| **QA5 Statistical Uncertainty** | 1 | Reports average metrics across seeds; formal significance testing (DeLong/Wilcoxon) omitted. |
| **QA6 Author Artifacts** | 1 | Manuscript and arXiv preprint full texts public; code repository referenced. |
| **QA7 Sparse Construct Validity** | 1 | Mentions data sparsity motivation, but lacks isolated zero-exposure KC cold-start protocol. |
| **QA8 Computational Transparency** | 1 | Mentions GPU hardware environment; formal wall-clock scaling curves omitted. |

**Raw Quality Score:** 11 / 16  
**Normalized Quality:** 0.6875 (**MODERATE Quality**)

---

# 5. Methodological Summary & Codebook Stress-Test Insights

1. **CB14 Verification (Graph + SSL Dual Gateway):** KT011 is a textbook exemplar of a hybrid Graph-KT + SSL-KT model (`PRIMARY_CORE`). It uses explicit graph structure (E2E relational subgraphs) and dual-level self-supervised contrastive learning.
2. **CB15 Verification (`evidence_source_type`):** Full text is verified via official publisher metadata (`PUBLISHER_METADATA`) and author-hosted preprint manuscript (`PAPER_FULLTEXT`).
3. **CB13 Verification (`resampling_repeats` vs `n_seeds`):** Correctly tagged `n_seeds = 5` with `resampling_repeats = 1` (`repeated_run_unit = SEED_REPETITION`), preventing parameter overloading.
4. **CB16 Verification (`coding_completeness`):** Marked `FULLTEXT_CODED` as both peer-reviewed publication and author manuscript full texts were thoroughly inspected.
