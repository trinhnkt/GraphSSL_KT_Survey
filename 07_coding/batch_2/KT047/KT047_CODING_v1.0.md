# KT047 — Dual-Channel SSL Heterogeneous Graph KT Coding Record (v1.0 LOCKED)

**Paper ID:** PAPER_KT047  
**Legacy ID:** KT047  
**Title:** Fusing Hybrid Attentive Network with Self-Supervised Dual-Channel Heterogeneous Graph for Knowledge Tracing  
**Authors:** Tangjie Wu, Qiang Ling  
**Venue:** Expert Systems with Applications, Vol. 225, Article 120212, Sept. 2023  
**DOI:** 10.1016/j.eswa.2023.120212  
**arXiv ID:** NR  
**Coder:** AI_ASSISTED (Antigravity Research-Engineering Assistant)  
**Codebook Version:** `coding_codebook_v1.0_LOCKED.md`  
**Date:** 2026-08-26  

---

# 1. PAPER Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `paper_id` | `PAPER_KT047` | AUTHOR_STATED | PUBLISHER_METADATA | ESWA 2023 |
| `legacy_id` | `KT047` | AUTHOR_STATED | METADATA | Seed corpus identifier |
| `title` | Fusing Hybrid Attentive Network with Self-Supervised Dual-Channel Heterogeneous Graph for Knowledge Tracing | AUTHOR_STATED | PUBLISHER_METADATA | Article title |
| `publication_year` | 2023 | AUTHOR_STATED | PUBLISHER_METADATA | Published Sept 2023 |
| `venue` | Expert Systems with Applications | AUTHOR_STATED | PUBLISHER_METADATA | Elsevier peer-reviewed journal |
| `publication_type` | `JOURNAL_ARTICLE` | AUTHOR_STATED | PUBLISHER_METADATA | Full journal article |
| `peer_reviewed` | `YES` | AUTHOR_STATED | PUBLISHER_METADATA | Official journal publication |
| `doi` | 10.1016/j.eswa.2023.120212 | AUTHOR_STATED | PUBLISHER_METADATA | Official DOI |
| `arxiv_id` | `NR` | AUTHOR_STATED | PUBLISHER_METADATA | Direct journal article |
| `kt_central_task` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Sequential learner response prediction & state tracking |
| `G_criterion` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Dual-channel heterogeneous graph neural network over questions and concepts |
| `S_criterion` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Dual-channel self-supervised contrastive learning pretext task |
| `corpus_tier` | `PRIMARY_CORE` | REVIEWER_INFERRED | PAPER_FULLTEXT | Satisfies both G-criterion and S-criterion (`PRIMARY_CORE`) |
| `coding_completeness` | `FULLTEXT_CODED` | REVIEWER_INFERRED | PAPER_FULLTEXT | Peer-reviewed journal full text inspected |
| `third_party_implementation_available` | `YES` | METADATA | SECONDARY | Tracked in pyKT / KT benchmark repositories |

---

# 2. MODEL Level Coding (`MODEL_KT047_DC_SSL`)

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `model_id` | `MODEL_KT047_DC_SSL` | AUTHOR_STATED | PAPER_FULLTEXT | Primary Dual-Channel SSL Heterogeneous Graph KT formulation |
| `graph_source` | `Q_MATRIX, CO_OCCURRENCE` | AUTHOR_STATED | PAPER_FULLTEXT | Dual-channel heterogeneous graph constructed from Q-matrix and exercise interaction co-occurrences |
| `graph_provenance` | `PRECOMPUTED_UNCLEAR_SPLIT` | REVIEWER_INFERRED | PAPER_FULLTEXT | Precomputed dual-channel graph adjacency prior to contrastive training |
| `graph_leakage_risk` | `POTENTIAL` | REVIEWER_INFERRED | PAPER_FULLTEXT | Precomputed interaction co-occurrence edge weights without explicit train-only split reporting |
| `graph_representation` | `HETEROGENEOUS_MULTI_NODE, ITEM_KC_BIPARTITE` | AUTHOR_STATED | PAPER_FULLTEXT | Dual-channel heterogeneous graph representations connecting questions and concepts |
| `directed` | `N` | AUTHOR_STATED | PAPER_FULLTEXT | Undirected heterogeneous dual-channel adjacency |
| `typed_edges` | `Y` | AUTHOR_STATED | PAPER_FULLTEXT | Heterogeneous edge categories across dual channels |
| `gnn_encoder` | `HETEROGENEOUS_GNN` | AUTHOR_STATED | PAPER_FULLTEXT | Dual-channel Heterogeneous Graph Neural Network encoder |
| `temporal_backbone` | `SELF_ATTENTION_TRANSFORMER` | AUTHOR_STATED | PAPER_FULLTEXT | Hybrid attentive Transformer backbone for sequence tracing |
| `fusion_type` | `ATTENTION, CONCAT` | AUTHOR_STATED | PAPER_FULLTEXT | Fuses dual-channel graph representations into attentive sequence layer |
| `fusion_location` | `INPUT, HIDDEN_STATE` | AUTHOR_STATED | PAPER_FULLTEXT | Sequence input and attentive hidden state layers |
| `ssl_family` | `GRAPH_CONTRASTIVE, MULTIVIEW_CONTRASTIVE` | AUTHOR_STATED | PAPER_FULLTEXT | Self-supervised contrastive loss across dual heterogeneous graph channels |
| `augmentation_type` | `EDGE_DROP, NODE_MASK` | AUTHOR_STATED | PAPER_FULLTEXT | Dual-channel graph structural perturbations |
| `educational_structure_preservation` | `YES_EXPLICIT` | AUTHOR_STATED | PAPER_FULLTEXT | Preserves heterogeneous exercise-concept mappings across dual channels |

---

# 3. EXPERIMENT Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `experiment_id` | `EXP_KT047_MAIN` | AUTHOR_STATED | PAPER_FULLTEXT | Main experimental evaluation |
| `datasets` | ASSISTments2009, ASSISTments2017, Statics2011 | AUTHOR_STATED | PAPER_FULLTEXT | Benchmark educational datasets evaluated |
| `split_type` | `LEARNER_BASED` | AUTHOR_STATED | PAPER_FULLTEXT | Student history partition into train/test splits |
| `n_seeds` | 5 | AUTHOR_STATED | PAPER_FULLTEXT | Performance averaged over 5 random seeds (CB13) |
| `resampling_repeats` | 1 | REVIEWER_INFERRED | PAPER_FULLTEXT | Single train/test data split repeated across seeds (CB13) |
| `repeated_run_unit` | `SEED_REPETITION` | REVIEWER_INFERRED | PAPER_FULLTEXT | Seed repetition unit (CB13) |
| `sparse_concept_ontology` | `GENERIC_DATA_SPARSITY` | REVIEWER_INFERRED | PAPER_FULLTEXT | Evaluates dual-channel contrastive learning on sparse datasets |
| `metrics` | ROC-AUC, ACC | AUTHOR_STATED | PAPER_FULLTEXT | Prediction accuracy and ROC-AUC metrics |
| `statistical_testing` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | Significance tests omitted |
| `calibration_metrics` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | ECE omitted |
| `computational_reporting` | `LIMITED` | REVIEWER_INFERRED | PAPER_FULLTEXT | Scaling bounds omitted |

---

# 4. Quality Scoring (QA1–QA8)

| QA Criterion | Score (0-2) | Justification |
|---|---|---|
| **QA1 Task Clarity** | 2 | Clear formulation of dual-channel heterogeneous graph contrastive learning for KT. |
| **QA2 Data Transparency** | 2 | Evaluates on public benchmark datasets (ASSIST09, ASSIST17, Statics11). |
| **QA3 Split/Leakage Transparency** | 1 | Train/test split reported; precomputed dual-channel graph train-only isolation unverified. |
| **QA4 Baseline/Ablation Adequacy** | 2 | Evaluates against DKT, SAKT, CL4KT, GIKT and performs dual-channel SSL ablation. |
| **QA5 Statistical Uncertainty** | 1 | Reports mean performance across seeds; formal significance testing omitted. |
| **QA6 Author Artifacts** | 1 | Official journal full text verified; author code repository unverified. |
| **QA7 Sparse Construct Validity** | 1 | Motivates model via dual-channel graph contrastive learning under sparse data, but lacks zero-exposure cold-start KC evaluation. |
| **QA8 Computational Transparency** | 1 | Explains dual-channel GNN complexity; formal runtime scaling bounds omitted. |

**Raw Quality Score:** 11 / 16  
**Normalized Quality:** 0.6875 (**MODERATE Quality**)
