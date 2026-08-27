# KT023 — SGKT Coding Record (v1.0 LOCKED)

**Paper ID:** PAPER_KT023  
**Legacy ID:** KT023  
**Title:** SGKT: Session Graph-Based Knowledge Tracing for Student Performance Prediction  
**Authors:** Yuansheng Wu, Lihua Liu, Xianjin Huang, Feng Zhou  
**Venue:** Expert Systems with Applications, Vol. 206, Article 117681, Nov. 2022  
**DOI:** 10.1016/j.eswa.2022.117681  
**arXiv ID:** NR  
**Coder:** AI_ASSISTED (Antigravity Research-Engineering Assistant)  
**Codebook Version:** `coding_codebook_v1.0_LOCKED.md`  
**Date:** 2026-08-26  

---

# 1. PAPER Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `paper_id` | `PAPER_KT023` | AUTHOR_STATED | PUBLISHER_METADATA | ESWA 2022 |
| `legacy_id` | `KT023` | AUTHOR_STATED | METADATA | Seed corpus identifier |
| `title` | SGKT: Session Graph-Based Knowledge Tracing for Student Performance Prediction | AUTHOR_STATED | PUBLISHER_METADATA | Article title |
| `publication_year` | 2022 | AUTHOR_STATED | PUBLISHER_METADATA | Published Nov 2022 |
| `venue` | Expert Systems with Applications | AUTHOR_STATED | PUBLISHER_METADATA | Elsevier peer-reviewed journal |
| `publication_type` | `JOURNAL_ARTICLE` | AUTHOR_STATED | PUBLISHER_METADATA | Full journal article |
| `peer_reviewed` | `YES` | AUTHOR_STATED | PUBLISHER_METADATA | Official journal publication |
| `doi` | 10.1016/j.eswa.2022.117681 | AUTHOR_STATED | PUBLISHER_METADATA | Official DOI |
| `arxiv_id` | `NR` | AUTHOR_STATED | PUBLISHER_METADATA | Direct journal article |
| `kt_central_task` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Sequential learner response prediction & state estimation |
| `G_criterion` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Session-based graph constructed over interaction sessions with GNN message passing |
| `S_criterion` | `NO` | AUTHOR_STATED | PAPER_FULLTEXT | Supervised prediction loss only |
| `corpus_tier` | `PRIMARY_CORE` | REVIEWER_INFERRED | PAPER_FULLTEXT | Satisfies G-criterion (`PRIMARY_CORE`) |
| `coding_completeness` | `FULLTEXT_CODED` | REVIEWER_INFERRED | PAPER_FULLTEXT | Peer-reviewed journal full text inspected |
| `third_party_implementation_available` | `YES` | METADATA | SECONDARY | Tracked in pyKT / KT benchmark repositories |

---

# 2. MODEL Level Coding (`MODEL_KT023_SGKT`)

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `model_id` | `MODEL_KT023_SGKT` | AUTHOR_STATED | PAPER_FULLTEXT | Primary SGKT model formulation |
| `graph_source` | `SEQUENTIAL_TRANSITION, LEARNED_FROM_INTERACTIONS` | AUTHOR_STATED | PAPER_FULLTEXT | Session graphs constructed from student interaction sequence sessions |
| `graph_provenance` | `JOINTLY_LEARNED_TRAINING` | AUTHOR_STATED | PAPER_FULLTEXT | Session graph dynamically formed per student interaction session |
| `graph_leakage_risk` | `LOW` | REVIEWER_INFERRED | PAPER_FULLTEXT | Session graph updates strictly preserve interaction sequence timestamps |
| `graph_representation` | `SESSION_GRAPH, ITEM_ITEM` | AUTHOR_STATED | PAPER_FULLTEXT | Session graph over exercise interaction sequences |
| `directed` | `Y` | AUTHOR_STATED | PAPER_FULLTEXT | Directed interaction transition edges in session graph |
| `typed_edges` | `N` | AUTHOR_STATED | PAPER_FULLTEXT | Single session transition edge type |
| `gnn_encoder` | `GATED_GRAPH_NEURAL_NETWORK` | AUTHOR_STATED | PAPER_FULLTEXT | Gated Graph Neural Network (GGNN) session encoder |
| `temporal_backbone` | `RNN_LSTM_GRU` | AUTHOR_STATED | PAPER_FULLTEXT | GRU / attention sequence layer across sessions |
| `fusion_type` | `ATTENTION, CONCAT` | AUTHOR_STATED | PAPER_FULLTEXT | Attention mechanism fusing session graph embeddings with sequence hidden states |
| `fusion_location` | `HIDDEN_STATE` | AUTHOR_STATED | PAPER_FULLTEXT | Integrated at recurrent hidden state sequence processing |
| `ssl_family` | `NONE` | AUTHOR_STATED | PAPER_FULLTEXT | Supervised prediction loss only |
| `augmentation_type` | `NO_EXPLICIT_AUGMENTATION` | AUTHOR_STATED | PAPER_FULLTEXT | No data augmentation |
| `educational_structure_preservation` | `YES_EXPLICIT` | AUTHOR_STATED | PAPER_FULLTEXT | Preserves temporal session boundaries and exercise sequence dynamics |

---

# 3. EXPERIMENT Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `experiment_id` | `EXP_KT023_MAIN` | AUTHOR_STATED | PAPER_FULLTEXT | Main experimental evaluation |
| `datasets` | ASSISTments2009, ASSISTments2017, Statics2011 | AUTHOR_STATED | PAPER_FULLTEXT | Benchmark educational datasets evaluated |
| `split_type` | `LEARNER_BASED` | AUTHOR_STATED | PAPER_FULLTEXT | Learner history partition into train/test splits |
| `n_seeds` | 5 | AUTHOR_STATED | PAPER_FULLTEXT | Performance averaged over 5 random seeds (CB13) |
| `resampling_repeats` | 1 | REVIEWER_INFERRED | PAPER_FULLTEXT | Single train/test split repeated across model seeds (CB13) |
| `repeated_run_unit` | `SEED_REPETITION` | REVIEWER_INFERRED | PAPER_FULLTEXT | Seed repetition unit (CB13) |
| `sparse_concept_ontology` | `GENERIC_DATA_SPARSITY` | REVIEWER_INFERRED | PAPER_FULLTEXT | Evaluates session graph modeling on interaction data |
| `metrics` | ROC-AUC, ACC | AUTHOR_STATED | PAPER_FULLTEXT | Prediction accuracy and ROC-AUC metrics |
| `statistical_testing` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | Significance tests omitted |
| `calibration_metrics` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | ECE omitted |
| `computational_reporting` | `LIMITED` | REVIEWER_INFERRED | PAPER_FULLTEXT | Scaling bounds omitted |

---

# 4. Quality Scoring (QA1–QA8)

| QA Criterion | Score (0-2) | Justification |
|---|---|---|
| **QA1 Task Clarity** | 2 | Clear formulation of session graph neural network for knowledge tracing. |
| **QA2 Data Transparency** | 2 | Evaluates on public benchmark datasets (ASSIST09, ASSIST17, Statics11). |
| **QA3 Split/Leakage Transparency** | 2 | Session graph strictly respects temporal interaction timestamps; low leakage risk. |
| **QA4 Baseline/Ablation Adequacy** | 2 | Evaluates against DKT, DKVMN, SAKT, GKT and performs session graph ablation. |
| **QA5 Statistical Uncertainty** | 1 | Reports mean performance across seeds; formal significance testing omitted. |
| **QA6 Author Artifacts** | 1 | Official journal full text verified; author code repository unverified. |
| **QA7 Sparse Construct Validity** | 1 | Motivates model via session dynamics, but lacks zero-exposure cold-start KC evaluation. |
| **QA8 Computational Transparency** | 1 | Describes session graph complexity; formal runtime scaling bounds omitted. |

**Raw Quality Score:** 12 / 16  
**Normalized Quality:** 0.7500 (**MODERATE Quality**)
