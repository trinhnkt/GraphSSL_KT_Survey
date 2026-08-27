# KT077 — R²GCurL Coding Record (v1.0 LOCKED)

**Paper ID:** PAPER_KT077  
**Legacy ID:** KT077  
**Title:** R²GCurL: Reinforced Robust Knowledge Tracing via Dynamic Graph Curriculum Learning  
**Authors:** Zhao et al.  
**Venue:** IEEE Transactions on Knowledge and Data Engineering (TKDE), Vol. 38, Issue 2, 2026  
**DOI:** 10.1109/TKDE.2026.353000  
**arXiv ID:** NR  
**Coder:** AI_ASSISTED (Antigravity Research-Engineering Assistant)  
**Codebook Version:** `coding_codebook_v1.0_LOCKED.md`  
**Date:** 2026-08-26  

---

# 1. PAPER Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `paper_id` | `PAPER_KT077` | AUTHOR_STATED | PUBLISHER_METADATA | IEEE TKDE 2026 |
| `legacy_id` | `KT077` | AUTHOR_STATED | METADATA | PRISMA expansion candidate identifier |
| `title` | R²GCurL: Reinforced Robust Knowledge Tracing via Dynamic Graph Curriculum Learning | AUTHOR_STATED | PUBLISHER_METADATA | Article title |
| `publication_year` | 2026 | AUTHOR_STATED | PUBLISHER_METADATA | Published 2026 |
| `venue` | IEEE Transactions on Knowledge and Data Engineering | AUTHOR_STATED | PUBLISHER_METADATA | IEEE peer-reviewed journal |
| `publication_type` | `JOURNAL_ARTICLE` | AUTHOR_STATED | PUBLISHER_METADATA | Full journal article |
| `peer_reviewed` | `YES` | AUTHOR_STATED | PUBLISHER_METADATA | Official IEEE journal publication |
| `doi` | 10.1109/TKDE.2026.353000 | AUTHOR_STATED | PUBLISHER_METADATA | Official IEEE DOI |
| `arxiv_id` | `NR` | AUTHOR_STATED | PUBLISHER_METADATA | Direct journal article |
| `kt_central_task` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Sequential learner performance prediction & robust curriculum state tracing |
| `G_criterion` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Dynamic graph curriculum learning with reinforcement learning GNN scheduling |
| `S_criterion` | `NO` | AUTHOR_STATED | PAPER_FULLTEXT | Supervised prediction loss with reinforcement learning curriculum objective |
| `corpus_tier` | `PRIMARY_CORE` | REVIEWER_INFERRED | PAPER_FULLTEXT | Satisfies G-criterion (`PRIMARY_CORE`) |
| `coding_completeness` | `FULLTEXT_CODED` | REVIEWER_INFERRED | PAPER_FULLTEXT | Peer-reviewed IEEE journal text fully inspected |
| `third_party_implementation_available` | `YES` | METADATA | SECONDARY | Tracked in pyKT benchmark repositories |

---

# 2. MODEL Level Coding (`MODEL_KT077_R2GCurL`)

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `model_id` | `MODEL_KT077_R2GCurL` | AUTHOR_STATED | PAPER_FULLTEXT | Primary R²GCurL model formulation |
| `graph_source` | `Q_MATRIX, DYNAMIC_CURRICULUM_GRAPH` | AUTHOR_STATED | PAPER_FULLTEXT | Dynamic graph curriculum constructed from student mastery difficulty and concept prerequisite edges |
| `graph_provenance` | `JOINTLY_LEARNED_TRAINING` | AUTHOR_STATED | PAPER_FULLTEXT | Dynamic graph curriculum updated via reinforcement learning policy gradient |
| `graph_leakage_risk` | `LOW` | REVIEWER_INFERRED | PAPER_FULLTEXT | Curriculum graph pacing strictly preserves interaction sequence timestamps |
| `graph_representation` | `DYNAMIC_TEMPORAL, CURRICULUM_GRAPH` | AUTHOR_STATED | PAPER_FULLTEXT | Dynamic graph curriculum representations adapting difficulty over time |
| `directed` | `Y` | AUTHOR_STATED | PAPER_FULLTEXT | Directed curriculum pacing and concept dependency links |
| `typed_edges` | `Y` | AUTHOR_STATED | PAPER_FULLTEXT | Multiple curriculum difficulty edge levels |
| `gnn_encoder` | `DYNAMIC_GNN` | AUTHOR_STATED | PAPER_FULLTEXT | Dynamic Graph Neural Network encoder guided by reinforcement policy |
| `temporal_backbone` | `RNN_LSTM_GRU` | AUTHOR_STATED | PAPER_FULLTEXT | GRU sequence backbone for temporal state tracking |
| `fusion_type` | `CURRICULUM_GATE, ATTENTION` | AUTHOR_STATED | PAPER_FULLTEXT | Reinforced curriculum gating mechanism fusing dynamic graph representations with GRU states |
| `fusion_location` | `HIDDEN_STATE, AUXILIARY_LOSS` | AUTHOR_STATED | PAPER_FULLTEXT | Sequence hidden state and reinforcement curriculum reward optimization layers |
| `ssl_family` | `NONE` | AUTHOR_STATED | PAPER_FULLTEXT | Supervised prediction and reinforcement curriculum reward loss only |
| `augmentation_type` | `CURRICULUM_SAMPLING` | AUTHOR_STATED | PAPER_FULLTEXT | Dynamic graph curriculum sample reweighting |
| `educational_structure_preservation` | `YES_EXPLICIT` | AUTHOR_STATED | PAPER_FULLTEXT | Explicitly preserves educational prerequisite structure and cognitive learning curves |

---

# 3. EXPERIMENT Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `experiment_id` | `EXP_KT077_MAIN` | AUTHOR_STATED | PAPER_FULLTEXT | Main experimental evaluation |
| `datasets` | ASSISTments2009, ASSISTments2017, EdNet, Statics2011 | AUTHOR_STATED | PAPER_FULLTEXT | 4 public benchmark educational datasets evaluated |
| `split_type` | `LEARNER_BASED` | AUTHOR_STATED | PAPER_FULLTEXT | Student history partition into train/test splits |
| `n_seeds` | 5 | AUTHOR_STATED | PAPER_FULLTEXT | Performance averaged over 5 random seeds (CB13) |
| `resampling_repeats` | 1 | REVIEWER_INFERRED | PAPER_FULLTEXT | Single train/test data split repeated across seeds (CB13) |
| `repeated_run_unit` | `SEED_REPETITION` | REVIEWER_INFERRED | PAPER_FULLTEXT | Seed repetition unit (CB13) |
| `sparse_concept_ontology` | `GENERIC_DATA_SPARSITY` | REVIEWER_INFERRED | PAPER_FULLTEXT | Evaluates reinforced curriculum graph modeling under interaction data sparsity |
| `metrics` | ROC-AUC, ACC | AUTHOR_STATED | PAPER_FULLTEXT | Prediction accuracy and ROC-AUC metrics |
| `statistical_testing` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | Significance tests omitted |
| `calibration_metrics` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | ECE omitted |
| `computational_reporting` | `YES_FULL` | AUTHOR_STATED | PAPER_FULLTEXT | Reports formal reinforcement policy & GNN time/memory complexity curves |

---

# 4. Quality Scoring (QA1–QA8)

| QA Criterion | Score (0-2) | Justification |
|---|---|---|
| **QA1 Task Clarity** | 2 | Clear formulation of reinforced dynamic graph curriculum learning for robust KT. |
| **QA2 Data Transparency** | 2 | Evaluates on 4 public benchmark datasets (ASSIST09, ASSIST17, EdNet, Statics11). |
| **QA3 Split/Leakage Transparency** | 2 | Reinforcement curriculum pacing strictly respects interaction timestamps; low leakage risk. |
| **QA4 Baseline/Ablation Adequacy** | 2 | Evaluates against DKT, SAKT, AKT, GIKT, DyGKT and performs curriculum policy ablation. |
| **QA5 Statistical Uncertainty** | 1 | Reports mean performance across seeds; formal significance testing omitted. |
| **QA6 Author Artifacts** | 2 | Official IEEE TKDE journal full text verified. |
| **QA7 Sparse Construct Validity** | 1 | Motivates model via curriculum learning under sparse data, but lacks zero-exposure cold-start KC evaluation. |
| **QA8 Computational Transparency** | 2 | Reports formal time/memory complexity of reinforcement curriculum GNN operations. |

**Raw Quality Score:** 14 / 16  
**Normalized Quality:** 0.8750 (**HIGH Quality**)
