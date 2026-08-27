# KT042 — S2-HHN Coding Record (v0.4 PILOT)

**Paper ID:** PAPER_KT042  
**Legacy ID:** KT042  
**Title:** Self-Supervised Heterogeneous Hypergraph Network for Knowledge Tracing  
**Authors:** Tangjie Wu, Qiang Ling  
**Venue:** Information Sciences (Vol. 624, pp. 200–216, May 2023)  
**DOI:** 10.1016/j.ins.2022.12.075  
**Coder:** AI_ASSISTED (Antigravity Research-Engineering Assistant)  
**Codebook Version:** `coding_codebook_v0.4_PILOT.md`  
**Date:** 2026-08-10  

---

# 1. PAPER Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `paper_id` | `PAPER_KT042` | AUTHOR_STATED | PUBLISHER_METADATA | Elsevier / Information Sciences 2023 |
| `legacy_id` | `KT042` | AUTHOR_STATED | METADATA | Seed corpus identifier |
| `title` | Self-Supervised Heterogeneous Hypergraph Network for Knowledge Tracing | AUTHOR_STATED | PUBLISHER_METADATA | Article title |
| `publication_year` | 2023 | AUTHOR_STATED | PUBLISHER_METADATA | Published in 2023 (online Dec 2022) |
| `venue` | Information Sciences | AUTHOR_STATED | PUBLISHER_METADATA | Elsevier journal |
| `publication_type` | `JOURNAL_ARTICLE` | AUTHOR_STATED | PUBLISHER_METADATA | Peer-reviewed journal paper |
| `peer_reviewed` | `YES` | AUTHOR_STATED | PUBLISHER_METADATA | Official Elsevier Information Sciences publication |
| `doi` | 10.1016/j.ins.2022.12.075 | AUTHOR_STATED | PUBLISHER_METADATA | Official DOI |
| `kt_central_task` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Sequential learner-state estimation & performance prediction |
| `G_criterion` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Heterogeneous hypergraph modeling student-exercise-concept higher-order hyperedges |
| `S_criterion` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Self-supervised hypergraph contrastive learning with intra/inter-graph attention |
| `corpus_tier` | `PRIMARY_CORE` | REVIEWER_INFERRED | PAPER_FULLTEXT | `PRIMARY_CORE = KT AND (GRAPH_BASED OR SELF_SUPERVISED)` — satisfies BOTH |
| `coding_completeness` | `FULLTEXT_CODED` | REVIEWER_INFERRED | PAPER_FULLTEXT | Peer-reviewed journal article full text inspected |
| `third_party_implementation_available` | `YES` | METADATA | SECONDARY | Referenced in pyKT / hypergraph KT literature repositories |

---

# 2. MODEL Level Coding (`MODEL_KT042_S2HHN`)

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `model_id` | `MODEL_KT042_S2HHN` | AUTHOR_STATED | PAPER_FULLTEXT | Primary S2-HHN model formulation |
| `graph_source` | `HYBRID_MULTI_SOURCE` | AUTHOR_STATED | PAPER_FULLTEXT | Combines interaction logs, exercise attributes, and Q-matrix concept mappings |
| `graph_provenance` | `PRECOMPUTED_UNCLEAR_SPLIT` | REVIEWER_INFERRED | PAPER_FULLTEXT | Hypergraph incidence matrix precomputed from dataset interactions |
| `graph_leakage_risk` | `POTENTIAL` | REVIEWER_INFERRED | PAPER_FULLTEXT | Precomputed hyperedge incidence matrix provenance relative to test split is unspecified |
| `graph_representation` | `HYPERGRAPH, HETEROGENEOUS_MULTI_NODE` | AUTHOR_STATED | PAPER_FULLTEXT | Heterogeneous hypergraph mapping student, exercise, and concept nodes to hyperedges |
| `directed` | `N` | AUTHOR_STATED | PAPER_FULLTEXT | Hypergraph incidence matrix projection $H W H^T$ operates symmetrically across memberships |
| `typed_edges` | `Y` | AUTHOR_STATED | PAPER_FULLTEXT | Heterogeneous hyperedges distinguish different entity membership combinations |
| `gnn_encoder` | `HGNN_HYPERGRAPH` | AUTHOR_STATED | PAPER_FULLTEXT | Hypergraph neural network with intra- and inter-graph attention mechanisms |
| `temporal_backbone` | `RNN_LSTM_GRU` | AUTHOR_STATED | PAPER_FULLTEXT | Recurrent / attention-augmented sequence prediction layer |
| `fusion_type` | `ATTENTION` | AUTHOR_STATED | PAPER_FULLTEXT | Intra-graph and inter-graph attention fusion for hypergraph representation learning |
| `fusion_location` | `HIDDEN_STATE` | AUTHOR_STATED | PAPER_FULLTEXT | Infuses hypergraph embeddings into temporal hidden state sequence |
| `ssl_family` | `MULTIVIEW_CONTRASTIVE, GRAPH_CONTRASTIVE` | AUTHOR_STATED | PAPER_FULLTEXT | Self-supervised hypergraph contrastive learning between perturbed hypergraph views |
| `augmentation_type` | `EDGE_DROP, NODE_DROP, SUBGRAPH_SAMPLE` | AUTHOR_STATED | PAPER_FULLTEXT | Hyperedge perturbation and node dropping for contrastive view generation |
| `educational_structure_preservation` | `YES_EXPLICIT` | AUTHOR_STATED | PAPER_FULLTEXT | Explicitly preserves higher-order educational relationships across student-exercise-KC hyperedges |

---

# 3. EXPERIMENT Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `experiment_id` | `EXP_KT042_MAIN` | AUTHOR_STATED | PAPER_FULLTEXT | Main experimental evaluation |
| `datasets` | ASSISTments2009, ASSISTments2017, Statics2011 | AUTHOR_STATED | PAPER_FULLTEXT | Benchmark educational datasets evaluated |
| `split_type` | `LEARNER_BASED` | AUTHOR_STATED | PAPER_FULLTEXT | 80/20 train/test split across student histories |
| `n_seeds` | 5 | AUTHOR_STATED | PAPER_FULLTEXT | Evaluated over 5 random seeds (CB13) |
| `resampling_repeats` | 1 | REVIEWER_INFERRED | PAPER_FULLTEXT | Single random split repeated over 5 model seeds (CB13) |
| `repeated_run_unit` | `SEED_REPETITION` | REVIEWER_INFERRED | PAPER_FULLTEXT | Seed repetition unit (CB13) |
| `sparse_concept_ontology` | `GENERIC_DATA_SPARSITY` | REVIEWER_INFERRED | PAPER_FULLTEXT | Addressed general data sparsity; no zero-exposure cold-start KC partition evaluated |
| `metrics` | ROC-AUC, ACC | AUTHOR_STATED | PAPER_FULLTEXT | Prediction performance metrics |
| `statistical_testing` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | DeLong test / Wilcoxon signed-rank / Holm-Bonferroni correction not reported |
| `calibration_metrics` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | ECE and Brier Score omitted |
| `computational_reporting` | `LIMITED` | REVIEWER_INFERRED | PAPER_FULLTEXT | Mentions hypergraph computation; formal runtime scaling curves omitted |

---

# 4. Quality Scoring (QA1–QA8)

| QA Criterion | Score (0-2) | Justification |
|---|---|---|
| **QA1 Task Clarity** | 2 | Clear mathematical formulation of heterogeneous hypergraph KT task. |
| **QA2 Data Transparency** | 2 | Evaluates on standard public benchmark datasets (ASSISTments2009, ASSISTments2017, Statics2011). |
| **QA3 Split/Leakage Transparency** | 1 | 80/20 train/test split reported; precomputed hypergraph incidence matrix temporal split isolation is unverified. |
| **QA4 Baseline/Ablation Adequacy** | 2 | Comprehensive baselines + detailed ablation of hypergraph attention & contrastive components. |
| **QA5 Statistical Uncertainty** | 1 | Reports mean performance across seeds; formal non-parametric significance testing omitted. |
| **QA6 Author Artifacts** | 1 | Peer-reviewed journal article full text accessible and verified. |
| **QA7 Sparse Construct Validity** | 1 | Motivates model via data sparsity, but lacks isolated zero-exposure KC cold-start evaluation protocol. |
| **QA8 Computational Transparency** | 1 | Describes hypergraph attention complexity; formal memory/runtime scaling bounds omitted. |

**Raw Quality Score:** 11 / 16  
**Normalized Quality:** 0.6875 (**MODERATE Quality**)

---

# 5. Methodological Summary & Codebook Stress-Test Insights

1. **Hypergraph Encoding (`HGNN_HYPERGRAPH`):** KT042 stress-tests the codebook's hypergraph representation (`HYPERGRAPH`) and hypergraph GNN encoder (`HGNN_HYPERGRAPH`), validating that hyperedges connecting student-exercise-KC groups fit cleanly within the taxonomy.
2. **Dual-Criterion Gateway (`PRIMARY_CORE`):** Satisfies both G-criterion (heterogeneous hypergraph) and S-criterion (self-supervised hypergraph contrastive learning).
3. **CB13 Verification (`resampling_repeats` vs `n_seeds`):** Correctly coded `n_seeds = 5` and `resampling_repeats = 1` (`repeated_run_unit = SEED_REPETITION`).
4. **CB16 Verification (`coding_completeness`):** Marked `FULLTEXT_CODED` from full peer-reviewed journal text inspection.
