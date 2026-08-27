# KT033 — DGMN Coding Record (v1.0 LOCKED)

**Paper ID:** PAPER_KT033  
**Legacy ID:** KT033  
**Title:** Deep Graph Memory Networks for Forgetting-Robust Knowledge Tracing  
**Authors:** Ghodai Abdelrahman, Qing Wang  
**Venue:** IEEE Transactions on Knowledge and Data Engineering (TKDE), Vol. 35, Issue 8, pp. 7844–7855, Aug. 2023  
**DOI:** 10.1109/TKDE.2022.3206447  
**arXiv ID:** NR  
**Coder:** AI_ASSISTED (Antigravity Research-Engineering Assistant)  
**Codebook Version:** `coding_codebook_v1.0_LOCKED.md`  
**Date:** 2026-08-26  

---

# 1. PAPER Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `paper_id` | `PAPER_KT033` | AUTHOR_STATED | PUBLISHER_METADATA | IEEE TKDE 2023 |
| `legacy_id` | `KT033` | AUTHOR_STATED | METADATA | Seed corpus identifier |
| `title` | Deep Graph Memory Networks for Forgetting-Robust Knowledge Tracing | AUTHOR_STATED | PUBLISHER_METADATA | Published IEEE article title |
| `publication_year` | 2023 | AUTHOR_STATED | PUBLISHER_METADATA | TKDE journal Vol. 35 published Aug 2023 |
| `venue` | IEEE Transactions on Knowledge and Data Engineering | AUTHOR_STATED | PUBLISHER_METADATA | IEEE peer-reviewed journal |
| `publication_type` | `JOURNAL_ARTICLE` | AUTHOR_STATED | PUBLISHER_METADATA | Full journal article |
| `peer_reviewed` | `YES` | AUTHOR_STATED | PUBLISHER_METADATA | Official IEEE journal publication |
| `doi` | 10.1109/TKDE.2022.3206447 | AUTHOR_STATED | PUBLISHER_METADATA | Official IEEE DOI |
| `arxiv_id` | `NR` | AUTHOR_STATED | PUBLISHER_METADATA | Direct journal publication |
| `kt_central_task` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Sequential learner performance prediction & forgetting-robust state tracking |
| `G_criterion` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Dynamic latent concept graph integrated with memory network architecture |
| `S_criterion` | `NO` | AUTHOR_STATED | PAPER_FULLTEXT | Supervised prediction loss only |
| `corpus_tier` | `PRIMARY_CORE` | REVIEWER_INFERRED | PAPER_FULLTEXT | Satisfies G-criterion (`PRIMARY_CORE`) |
| `coding_completeness` | `FULLTEXT_CODED` | REVIEWER_INFERRED | PAPER_FULLTEXT | Peer-reviewed IEEE journal text fully inspected |
| `third_party_implementation_available` | `YES` | METADATA | SECONDARY | Tracked in pyKT / KT benchmark repositories |

---

# 2. MODEL Level Coding (`MODEL_KT033_DGMN`)

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `model_id` | `MODEL_KT033_DGMN` | AUTHOR_STATED | PAPER_FULLTEXT | Primary DGMN model formulation |
| `graph_source` | `LEARNED_FROM_INTERACTIONS, Q_MATRIX` | AUTHOR_STATED | PAPER_FULLTEXT | Dynamic latent concept graph updated dynamically from student interaction history |
| `graph_provenance` | `JOINTLY_LEARNED_TRAINING` | AUTHOR_STATED | PAPER_FULLTEXT | Dynamic latent concept graph learned jointly with memory network parameters |
| `graph_leakage_risk` | `LOW` | REVIEWER_INFERRED | PAPER_FULLTEXT | Graph state dynamically updated along interaction sequence timestamps |
| `graph_representation` | `GRAPH_MEMORY, DYNAMIC_TEMPORAL` | AUTHOR_STATED | PAPER_FULLTEXT | Dynamic latent concept graph coupled with key-value memory matrix |
| `directed` | `Y` | AUTHOR_STATED | PAPER_FULLTEXT | Directed dynamic concept influence edges |
| `typed_edges` | `N` | AUTHOR_STATED | PAPER_FULLTEXT | Single latent concept relation type |
| `gnn_encoder` | `GRAPH_MEMORY` | AUTHOR_STATED | PAPER_FULLTEXT | Graph memory encoder updating latent concept node representations |
| `temporal_backbone` | `MEMORY_NETWORK` | AUTHOR_STATED | PAPER_FULLTEXT | Key-value memory network with forgetting gate mechanism |
| `fusion_type` | `JOINT_LATENT_STATE, GATE` | AUTHOR_STATED | PAPER_FULLTEXT | Fuses dynamic graph concept embeddings with memory value readouts via forgetting gates |
| `fusion_location` | `HIDDEN_STATE` | AUTHOR_STATED | PAPER_FULLTEXT | Memory state update and readout steps |
| `ssl_family` | `NONE` | AUTHOR_STATED | PAPER_FULLTEXT | Supervised prediction loss only |
| `augmentation_type` | `NO_EXPLICIT_AUGMENTATION` | AUTHOR_STATED | PAPER_FULLTEXT | No data augmentation |
| `educational_structure_preservation` | `YES_EXPLICIT` | AUTHOR_STATED | PAPER_FULLTEXT | Preserves latent concept relations and temporal forgetting decay curves |

---

# 3. EXPERIMENT Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `experiment_id` | `EXP_KT033_MAIN` | AUTHOR_STATED | PAPER_FULLTEXT | Main experimental evaluation |
| `datasets` | ASSISTments2009, ASSISTments2017, Statics2011, EdNet | AUTHOR_STATED | PAPER_FULLTEXT | 4 public benchmark educational datasets evaluated |
| `split_type` | `LEARNER_BASED` | AUTHOR_STATED | PAPER_FULLTEXT | Learner history partition into train/test splits |
| `n_seeds` | 5 | AUTHOR_STATED | PAPER_FULLTEXT | Performance averaged over 5 random seeds (CB13) |
| `resampling_repeats` | 1 | REVIEWER_INFERRED | PAPER_FULLTEXT | Single train/test data split repeated across seeds (CB13) |
| `repeated_run_unit` | `SEED_REPETITION` | REVIEWER_INFERRED | PAPER_FULLTEXT | Seed repetition unit (CB13) |
| `sparse_concept_ontology` | `GENERIC_DATA_SPARSITY` | REVIEWER_INFERRED | PAPER_FULLTEXT | Evaluates graph memory modeling on sparse interaction datasets |
| `metrics` | ROC-AUC, ACC | AUTHOR_STATED | PAPER_FULLTEXT | Prediction accuracy and ROC-AUC metrics |
| `statistical_testing` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | Significance testing details omitted |
| `calibration_metrics` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | ECE omitted |
| `computational_reporting` | `YES_FULL` | AUTHOR_STATED | PAPER_FULLTEXT | Reports memory matrix efficiency and empirical runtime complexity curves |

---

# 4. Quality Scoring (QA1–QA8)

| QA Criterion | Score (0-2) | Justification |
|---|---|---|
| **QA1 Task Clarity** | 2 | Clear formulation of deep graph memory network for forgetting-robust KT. |
| **QA2 Data Transparency** | 2 | Evaluates on 4 public benchmark datasets (ASSIST09, ASSIST17, Statics11, EdNet). |
| **QA3 Split/Leakage Transparency** | 2 | Dynamic graph memory update strictly respects interaction sequence timestamps; low leakage risk. |
| **QA4 Baseline/Ablation Adequacy** | 2 | Evaluates against DKT, DKVMN, SAKT, SKT and performs forgetting gate & graph memory ablation. |
| **QA5 Statistical Uncertainty** | 1 | Reports mean performance across seeds; formal significance testing omitted. |
| **QA6 Author Artifacts** | 1 | Official IEEE TKDE journal full text verified; official repository unverified. |
| **QA7 Sparse Construct Validity** | 1 | Motivates model via temporal forgetting and concept latent graph dynamics, but lacks zero-exposure cold-start KC evaluation. |
| **QA8 Computational Transparency** | 2 | Reports formal time/memory complexity of graph memory readout. |

**Raw Quality Score:** 13 / 16  
**Normalized Quality:** 0.8125 (**HIGH Quality**)
