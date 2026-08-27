# KT037 — CMKT Coding Record (v0.4 PILOT)

**Paper ID:** PAPER_KT037  
**Legacy ID:** KT037  
**Title:** CMKT: Concept Map Driven Knowledge Tracing  
**Authors:** Yu Lu, Penghe Chen, Yang Pian, Vincent W. Zheng  
**Venue:** IEEE Transactions on Learning Technologies (TLT), Vol. 15, Issue 4, pp. 467–480, Aug. 2022  
**DOI:** 10.1109/TLT.2022.3196355  
**arXiv ID:** NR  
**Coder:** AI_ASSISTED (Antigravity Research-Engineering Assistant)  
**Codebook Version:** `coding_codebook_v0.4_PILOT.md`  
**Date:** 2026-08-26  

---

# 1. PAPER Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `paper_id` | `PAPER_KT037` | AUTHOR_STATED | PUBLISHER_METADATA | IEEE TLT 2022 |
| `legacy_id` | `KT037` | AUTHOR_STATED | METADATA | Seed corpus identifier |
| `title` | CMKT: Concept Map Driven Knowledge Tracing | AUTHOR_STATED | PUBLISHER_METADATA | IEEE published title |
| `publication_year` | 2022 | AUTHOR_STATED | PUBLISHER_METADATA | Published Aug 2022 |
| `venue` | IEEE Transactions on Learning Technologies | AUTHOR_STATED | PUBLISHER_METADATA | Peer-reviewed IEEE journal |
| `publication_type` | `JOURNAL_ARTICLE` | AUTHOR_STATED | PUBLISHER_METADATA | Full journal article |
| `peer_reviewed` | `YES` | AUTHOR_STATED | PUBLISHER_METADATA | Official IEEE journal publication |
| `doi` | 10.1109/TLT.2022.3196355 | AUTHOR_STATED | PUBLISHER_METADATA | Official IEEE DOI |
| `arxiv_id` | `NR` | AUTHOR_STATED | PUBLISHER_METADATA | Published direct to journal; no arXiv preprint registered |
| `kt_central_task` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Sequential learner-state estimation & performance prediction |
| `G_criterion` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Educational concept map (concept ordering graph) integrated into RNN input & loss constraint |
| `S_criterion` | `NO` | AUTHOR_STATED | PAPER_FULLTEXT | Supervised cross-entropy KT loss with concept ordering constraint; no SSL pretext objective |
| `corpus_tier` | `PRIMARY_CORE` | REVIEWER_INFERRED | PAPER_FULLTEXT | `PRIMARY_CORE = KT AND (GRAPH_BASED OR SELF_SUPERVISED)` — satisfies G-criterion |
| `coding_completeness` | `FULLTEXT_CODED` | REVIEWER_INFERRED | PAPER_FULLTEXT | Peer-reviewed journal text & methodology fully inspected |
| `third_party_implementation_available` | `YES` | METADATA | SECONDARY | Tracked in pyKT / KT benchmark literature |

---

# 2. MODEL Level Coding (`MODEL_KT037_CMKT`)

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `model_id` | `MODEL_KT037_CMKT` | AUTHOR_STATED | PAPER_FULLTEXT | Primary CMKT model formulation |
| `graph_source` | `CURRICULUM_CONCEPT_MAP, EXPERT_PREREQUISITE` | AUTHOR_STATED | PAPER_FULLTEXT | Educational concept map incorporating concept ordering/prerequisite relations |
| `graph_provenance` | `EXTERNAL_FIXED` | AUTHOR_STATED | PAPER_FULLTEXT | Pedagogical concept map supplied externally as a domain structural prior |
| `graph_leakage_risk` | `LOW` | REVIEWER_INFERRED | PAPER_FULLTEXT | External pedagogical graph fixed independently of student interaction history splits |
| `graph_representation` | `KC_KC, DAG` | AUTHOR_STATED | PAPER_FULLTEXT | Concept-concept ordering pairs forming a directed concept graph |
| `directed` | `Y` | AUTHOR_STATED | PAPER_FULLTEXT | Directed pairwise ordering/prerequisite relations between concepts |
| `typed_edges` | `N` | AUTHOR_STATED | PAPER_FULLTEXT | Single ordering dependency relation type between concepts |
| `gnn_encoder` | `NONE` | AUTHOR_STATED | PAPER_FULLTEXT | Network embedding & ordering pair constraints (CB14: Graph-KT gateway without GNN) |
| `temporal_backbone` | `RNN_LSTM_GRU` | AUTHOR_STATED | PAPER_FULLTEXT | Recurrent Neural Network (RNN) sequence layer for learner state tracing |
| `fusion_type` | `INPUT, REGULARIZATION_ONLY` | AUTHOR_STATED | PAPER_FULLTEXT | Network topology embedding at input layer + concept ordering constraint loss |
| `fusion_location` | `INPUT, AUXILIARY_LOSS` | AUTHOR_STATED | PAPER_FULLTEXT | Injected into input vector representations and auxiliary loss optimization |
| `ssl_family` | `NONE` | AUTHOR_STATED | PAPER_FULLTEXT | Supervised loss with structural ordering pair constraints |
| `augmentation_type` | `NO_EXPLICIT_AUGMENTATION` | AUTHOR_STATED | PAPER_FULLTEXT | No data augmentation or pretext task |
| `educational_structure_preservation` | `YES_EXPLICIT` | AUTHOR_STATED | PAPER_FULLTEXT | Explicitly preserves concept map ordering constraints during knowledge state estimation |

---

# 3. EXPERIMENT Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `experiment_id` | `EXP_KT037_MAIN` | AUTHOR_STATED | PAPER_FULLTEXT | Main experimental evaluation |
| `datasets` | ASSISTments2009, Junyi | AUTHOR_STATED | PAPER_FULLTEXT | Public benchmark educational datasets evaluated |
| `split_type` | `LEARNER_BASED` | AUTHOR_STATED | PAPER_FULLTEXT | Learner history partition into train/test sets |
| `n_seeds` | 5 | AUTHOR_STATED | PAPER_FULLTEXT | Evaluated over 5 random seeds (CB13) |
| `resampling_repeats` | 1 | REVIEWER_INFERRED | PAPER_FULLTEXT | Single random data split repeated across seeds (CB13) |
| `repeated_run_unit` | `SEED_REPETITION` | REVIEWER_INFERRED | PAPER_FULLTEXT | Seed repetition unit (CB13) |
| `sparse_concept_ontology` | `GENERIC_DATA_SPARSITY` | REVIEWER_INFERRED | PAPER_FULLTEXT | Addresses learner interaction data sparseness; no zero-exposure cold-start KC partition evaluated |
| `metrics` | ROC-AUC, ACC | AUTHOR_STATED | PAPER_FULLTEXT | Prediction performance metrics |
| `statistical_testing` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | Significance testing details omitted |
| `calibration_metrics` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | ECE and Brier Score omitted |
| `computational_reporting` | `LIMITED` | REVIEWER_INFERRED | PAPER_FULLTEXT | Mentions concept map embedding efficiency; formal scaling curves omitted |

---

# 4. Quality Scoring (QA1–QA8)

| QA Criterion | Score (0-2) | Justification |
|---|---|---|
| **QA1 Task Clarity** | 2 | Clear formulation of concept map integration into RNN knowledge tracing. |
| **QA2 Data Transparency** | 2 | Evaluates on public benchmark datasets (ASSISTments, Junyi). |
| **QA3 Split/Leakage Transparency** | 2 | External fixed concept map independent of test interaction split; low leakage risk. |
| **QA4 Baseline/Ablation Adequacy** | 2 | Compares against standard KT baselines and performs concept map ablation. |
| **QA5 Statistical Uncertainty** | 1 | Reports mean performance across 5 seeds; formal significance tests omitted. |
| **QA6 Author Artifacts** | 1 | Official IEEE journal full text verified; official repository not author-verified. |
| **QA7 Sparse Construct Validity** | 1 | Motivates model via interaction data sparseness, but lacks isolated zero-exposure KC cold-start protocol. |
| **QA8 Computational Transparency** | 1 | Explains network embedding and constraint complexity; formal runtime/memory scaling bounds omitted. |

**Raw Quality Score:** 12 / 16  
**Normalized Quality:** 0.7500 (**MODERATE Quality**)

---

# 5. Methodological Summary & Codebook Stress-Test Insights

1. **Graph-KT Gateway without GNN (CB14 Application):** CMKT stress-tests the CB14 rule. It does not use a message-passing GNN encoder (`gnn_encoder = NONE`), but uses an external concept map graph (`CURRICULUM_CONCEPT_MAP`) via network embedding features and ordering pair loss constraints, qualifying cleanly for `G_criterion = YES` and `PRIMARY_CORE`.
2. **External Fixed Provenance (`EXTERNAL_FIXED`):** Validates external curriculum/expert concept maps as a low-leakage-risk graph source (`graph_provenance = EXTERNAL_FIXED`, `graph_leakage_risk = LOW`).
3. **Data Sparseness Lens (`GENERIC_DATA_SPARSITY`):** Addresses learner interaction data sparseness through structural pedagogical priors without evaluating a zero-exposure KC cold-start benchmark.
4. **CB13 Verification (`resampling_repeats` vs `n_seeds`):** Coded `n_seeds = 5` and `resampling_repeats = 1` (`SEED_REPETITION`).
