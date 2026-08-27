# KT031 — Knowledge Structure Graph Coding Record (v1.0 LOCKED)

**Paper ID:** PAPER_KT031  
**Legacy ID:** KT031  
**Title:** Knowledge Structure Enhanced Graph Representation Learning Model for Attentive Knowledge Tracing  
**Authors:** Wenbin Gan, Yuan Sun, Yi Sun  
**Venue:** International Journal of Intelligent Systems (IJIS), Vol. 37, Issue 3, pp. 2012–2045, March 2022  
**DOI:** 10.1002/int.22763  
**arXiv ID:** NR  
**Coder:** AI_ASSISTED (Antigravity Research-Engineering Assistant)  
**Codebook Version:** `coding_codebook_v1.0_LOCKED.md`  
**Date:** 2026-08-26  

---

# 1. PAPER Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `paper_id` | `PAPER_KT031` | AUTHOR_STATED | PUBLISHER_METADATA | IJIS 2022 |
| `legacy_id` | `KT031` | AUTHOR_STATED | METADATA | Seed corpus identifier |
| `title` | Knowledge Structure Enhanced Graph Representation Learning Model for Attentive Knowledge Tracing | AUTHOR_STATED | PUBLISHER_METADATA | Article title |
| `publication_year` | 2022 | AUTHOR_STATED | PUBLISHER_METADATA | Published March 2022 |
| `venue` | International Journal of Intelligent Systems | AUTHOR_STATED | PUBLISHER_METADATA | Wiley peer-reviewed journal |
| `publication_type` | `JOURNAL_ARTICLE` | AUTHOR_STATED | PUBLISHER_METADATA | Full journal article |
| `peer_reviewed` | `YES` | AUTHOR_STATED | PUBLISHER_METADATA | Official journal publication |
| `doi` | 10.1002/int.22763 | AUTHOR_STATED | PUBLISHER_METADATA | Official DOI |
| `arxiv_id` | `NR` | AUTHOR_STATED | PUBLISHER_METADATA | Direct journal article |
| `kt_central_task` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Sequential learner response prediction & state tracking |
| `G_criterion` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Knowledge structure graph with graph neural network representation learning & attention |
| `S_criterion` | `NO` | AUTHOR_STATED | PAPER_FULLTEXT | Supervised prediction loss only |
| `corpus_tier` | `PRIMARY_CORE` | REVIEWER_INFERRED | PAPER_FULLTEXT | Satisfies G-criterion (`PRIMARY_CORE`) |
| `coding_completeness` | `FULLTEXT_CODED` | REVIEWER_INFERRED | PAPER_FULLTEXT | Peer-reviewed journal full text inspected |
| `third_party_implementation_available` | `YES` | METADATA | SECONDARY | Tracked in pyKT / KT benchmark repositories |

---

# 2. MODEL Level Coding (`MODEL_KT031_KSG_AKT`)

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `model_id` | `MODEL_KT031_KSG_AKT` | AUTHOR_STATED | PAPER_FULLTEXT | Primary Knowledge Structure Graph AKT formulation |
| `graph_source` | `CURRICULUM_CONCEPT_MAP, Q_MATRIX` | AUTHOR_STATED | PAPER_FULLTEXT | Knowledge structure concept graph constructed from Q-matrix and domain prerequisites |
| `graph_provenance` | `EXTERNAL_FIXED` | AUTHOR_STATED | PAPER_FULLTEXT | Domain knowledge structure supplied externally |
| `graph_leakage_risk` | `LOW` | REVIEWER_INFERRED | PAPER_FULLTEXT | External pedagogical graph fixed independently of test response splits |
| `graph_representation` | `KC_KC, ITEM_KC_BIPARTITE` | AUTHOR_STATED | PAPER_FULLTEXT | Knowledge concept structure graph linked to questions |
| `directed` | `Y` | AUTHOR_STATED | PAPER_FULLTEXT | Directed knowledge structure dependency relations |
| `typed_edges` | `N` | AUTHOR_STATED | PAPER_FULLTEXT | Single structural dependency edge type |
| `gnn_encoder` | `GCN` | AUTHOR_STATED | PAPER_FULLTEXT | Graph Convolutional Network representation encoder |
| `temporal_backbone` | `SELF_ATTENTION_TRANSFORMER` | AUTHOR_STATED | PAPER_FULLTEXT | Attentive Transformer backbone for sequence tracing |
| `fusion_type` | `CONCAT, ATTENTION` | AUTHOR_STATED | PAPER_FULLTEXT | Fuses GCN knowledge structure embeddings into attentive sequence representations |
| `fusion_location` | `INPUT, HIDDEN_STATE` | AUTHOR_STATED | PAPER_FULLTEXT | Input embedding and sequence attention layers |
| `ssl_family` | `NONE` | AUTHOR_STATED | PAPER_FULLTEXT | Supervised prediction loss only |
| `augmentation_type` | `NO_EXPLICIT_AUGMENTATION` | AUTHOR_STATED | PAPER_FULLTEXT | No data augmentation |
| `educational_structure_preservation` | `YES_EXPLICIT` | AUTHOR_STATED | PAPER_FULLTEXT | Preserves domain knowledge structure mapping and prerequisite constraints |

---

# 3. EXPERIMENT Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `experiment_id` | `EXP_KT031_MAIN` | AUTHOR_STATED | PAPER_FULLTEXT | Main experimental evaluation |
| `datasets` | ASSISTments2009, ASSISTments2017, Statics2011, KDD Cup 2010 | AUTHOR_STATED | PAPER_FULLTEXT | 4 public benchmark educational datasets evaluated |
| `split_type` | `LEARNER_BASED` | AUTHOR_STATED | PAPER_FULLTEXT | Student history partition into train/test splits |
| `n_seeds` | 5 | AUTHOR_STATED | PAPER_FULLTEXT | Performance averaged over 5 random seeds (CB13) |
| `resampling_repeats` | 1 | REVIEWER_INFERRED | PAPER_FULLTEXT | Single train/test data split repeated across seeds (CB13) |
| `repeated_run_unit` | `SEED_REPETITION` | REVIEWER_INFERRED | PAPER_FULLTEXT | Seed repetition unit (CB13) |
| `sparse_concept_ontology` | `GENERIC_DATA_SPARSITY` | REVIEWER_INFERRED | PAPER_FULLTEXT | Addresses interaction data sparseness through knowledge structure priors |
| `metrics` | ROC-AUC, ACC | AUTHOR_STATED | PAPER_FULLTEXT | Prediction accuracy and ROC-AUC metrics |
| `statistical_testing` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | Significance testing details omitted |
| `calibration_metrics` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | ECE omitted |
| `computational_reporting` | `LIMITED` | REVIEWER_INFERRED | PAPER_FULLTEXT | Scaling bounds omitted |

---

# 4. Quality Scoring (QA1–QA8)

| QA Criterion | Score (0-2) | Justification |
|---|---|---|
| **QA1 Task Clarity** | 2 | Clear formulation of knowledge structure GNN enhancement for attentive KT. |
| **QA2 Data Transparency** | 2 | Evaluates on 4 public benchmark datasets (ASSIST09, ASSIST17, Statics11, KDD Cup 2010). |
| **QA3 Split/Leakage Transparency** | 2 | External fixed knowledge structure graph independent of test split; low leakage risk. |
| **QA4 Baseline/Ablation Adequacy** | 2 | Evaluates against DKT, SAKT, AKT, GKT and performs knowledge structure ablation. |
| **QA5 Statistical Uncertainty** | 1 | Reports mean performance across seeds; formal significance testing omitted. |
| **QA6 Author Artifacts** | 1 | Official journal full text verified; author code repository unverified. |
| **QA7 Sparse Construct Validity** | 1 | Motivates model via knowledge structure augmentation under sparse data, but lacks zero-exposure cold-start KC evaluation. |
| **QA8 Computational Transparency** | 1 | Describes GCN layer complexity; formal runtime scaling bounds omitted. |

**Raw Quality Score:** 12 / 16  
**Normalized Quality:** 0.7500 (**MODERATE Quality**)
