# KT066 — HyperKT Coding Record (v0.4 PILOT)

**Paper ID:** PAPER_KT066  
**Legacy ID:** KT066  
**Title:** Dual-Channel Adaptive Scale Hypergraph Encoders With Cross-View Contrastive Learning for Knowledge Tracing  
**Authors:** Jiawei Li, Yuanfei Deng, Yixiu Qin, Shun Mao, Yuncheng Jiang  
**Venue:** IEEE Transactions on Neural Networks and Learning Systems (TNNLS, Vol. 36, Issue 4, pp. 6752–6766, April 2024 / 2025)  
**DOI:** 10.1109/TNNLS.2024.3386810  
**Coder:** AI_ASSISTED (Antigravity Research-Engineering Assistant)  
**Codebook Version:** `coding_codebook_v0.4_PILOT.md`  
**Date:** 2026-08-10  

---

# 1. PAPER Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `paper_id` | `PAPER_KT066` | AUTHOR_STATED | PUBLISHER_METADATA | IEEE / TNNLS 2024/2025 |
| `legacy_id` | `KT066` | AUTHOR_STATED | METADATA | Seed corpus identifier |
| `title` | Dual-Channel Adaptive Scale Hypergraph Encoders With Cross-View Contrastive Learning for Knowledge Tracing | AUTHOR_STATED | PUBLISHER_METADATA | Article title |
| `publication_year` | 2025 | AUTHOR_STATED | PUBLISHER_METADATA | IEEE TNNLS publication (online 2024, vol 2025) |
| `venue` | IEEE Transactions on Neural Networks and Learning Systems | AUTHOR_STATED | PUBLISHER_METADATA | IEEE journal |
| `publication_type` | `JOURNAL_ARTICLE` | AUTHOR_STATED | PUBLISHER_METADATA | Peer-reviewed IEEE transactions paper |
| `peer_reviewed` | `YES` | AUTHOR_STATED | PUBLISHER_METADATA | Official IEEE TNNLS publication |
| `doi` | 10.1109/TNNLS.2024.3386810 | AUTHOR_STATED | PUBLISHER_METADATA | Official DOI |
| `kt_central_task` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Sequential learner-state estimation & performance prediction |
| `G_criterion` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Dual-channel hypergraph encoders (global & local state hypergraphs) |
| `S_criterion` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Cross-view contrastive learning between state hypergraph views & transformed line graph views |
| `corpus_tier` | `PRIMARY_CORE` | REVIEWER_INFERRED | PAPER_FULLTEXT | `PRIMARY_CORE = KT AND (GRAPH_BASED OR SELF_SUPERVISED)` — satisfies BOTH |
| `coding_completeness` | `FULLTEXT_CODED` | REVIEWER_INFERRED | PAPER_FULLTEXT | Peer-reviewed IEEE transactions full text inspected |
| `third_party_implementation_available` | `YES` | METADATA | SECONDARY | Referenced in pyKT / hypergraph KT literature repositories |

---

# 2. MODEL Level Coding (`MODEL_KT066_HyperKT`)

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `model_id` | `MODEL_KT066_HyperKT` | AUTHOR_STATED | PAPER_FULLTEXT | Primary HyperKT model formulation |
| `graph_source` | `HYBRID_MULTI_SOURCE` | AUTHOR_STATED | PAPER_FULLTEXT | Interaction logs + adaptive-scale hyperedge distillation (knowledge & pattern aware) |
| `graph_provenance` | `PRECOMPUTED_UNCLEAR_SPLIT` | REVIEWER_INFERRED | PAPER_FULLTEXT | Hypergraph matrices precomputed from interaction logs without explicit temporal split report |
| `graph_leakage_risk` | `POTENTIAL` | REVIEWER_INFERRED | PAPER_FULLTEXT | Precomputed hyperedge matrix provenance relative to test split is unspecified |
| `graph_representation` | `HYPERGRAPH, MULTI_RELATIONAL` | AUTHOR_STATED | PAPER_FULLTEXT | Dual-channel hypergraphs (global pattern & local knowledge channels) + line graph dual views |
| `directed` | `N` | AUTHOR_STATED | PAPER_FULLTEXT | Hypergraph projections and line graph dual transformations operate symmetrically |
| `typed_edges` | `Y` | AUTHOR_STATED | PAPER_FULLTEXT | Distinguishes global pattern-aware hyperedges and local knowledge-aware hyperedges |
| `gnn_encoder` | `HGNN_HYPERGRAPH` | AUTHOR_STATED | PAPER_FULLTEXT | Simplified hypergraph convolution + collaborative hypergraph convolution networks |
| `temporal_backbone` | `SELF_ATTENTION_TRANSFORMER` | AUTHOR_STATED | PAPER_FULLTEXT | Transformer / attentive sequence layer for temporal state updates |
| `fusion_type` | `ATTENTION` | AUTHOR_STATED | PAPER_FULLTEXT | Multi-granularity state fusion across dual channels and temporal states |
| `fusion_location` | `HIDDEN_STATE` | AUTHOR_STATED | PAPER_FULLTEXT | Fuses dual hypergraph channel features into temporal state sequence |
| `ssl_family` | `MULTIVIEW_CONTRASTIVE, GRAPH_CONTRASTIVE` | AUTHOR_STATED | PAPER_FULLTEXT | Cross-view contrastive learning between state hypergraph views & transformed line graph views |
| `augmentation_type` | `SUBGRAPH_SAMPLE, RELATION_PERTURB` | AUTHOR_STATED | PAPER_FULLTEXT | Line-graph view transformations & adaptive hyperedge perturbations for cross-view SSL |
| `educational_structure_preservation` | `YES_EXPLICIT` | AUTHOR_STATED | PAPER_FULLTEXT | Explicitly preserves multigranularity knowledge states across global and local channels |

---

# 3. EXPERIMENT Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `experiment_id` | `EXP_KT066_MAIN` | AUTHOR_STATED | PAPER_FULLTEXT | Main experimental evaluation |
| `datasets` | ASSISTments2009, ASSISTments2017, Statics2011, Junyi | AUTHOR_STATED | PAPER_FULLTEXT | Benchmark educational datasets evaluated |
| `split_type` | `LEARNER_BASED` | AUTHOR_STATED | PAPER_FULLTEXT | 80/20 train/test split across student histories |
| `n_seeds` | 5 | AUTHOR_STATED | PAPER_FULLTEXT | Evaluated over 5 random seeds (CB13) |
| `resampling_repeats` | 1 | REVIEWER_INFERRED | PAPER_FULLTEXT | Single random split repeated over 5 model seeds (CB13) |
| `repeated_run_unit` | `SEED_REPETITION` | REVIEWER_INFERRED | PAPER_FULLTEXT | Seed repetition unit (CB13) |
| `sparse_concept_ontology` | `GENERIC_DATA_SPARSITY` | REVIEWER_INFERRED | PAPER_FULLTEXT | Evaluated on full datasets under generic data sparsity; no zero-exposure cold-start KC split |
| `metrics` | ROC-AUC, ACC | AUTHOR_STATED | PAPER_FULLTEXT | Prediction performance metrics |
| `statistical_testing` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | DeLong test / Wilcoxon signed-rank / Holm-Bonferroni correction not reported |
| `calibration_metrics` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | ECE and Brier Score omitted |
| `computational_reporting` | `LIMITED` | REVIEWER_INFERRED | PAPER_FULLTEXT | Mentions hypergraph convolution efficiency; formal memory/scaling curves omitted |

---

# 4. Quality Scoring (QA1–QA8)

| QA Criterion | Score (0-2) | Justification |
|---|---|---|
| **QA1 Task Clarity** | 2 | Clear formulation of dual-channel hypergraph KT & cross-view contrastive learning task. |
| **QA2 Data Transparency** | 2 | Evaluates on 4 standard public benchmark datasets (ASSISTments2009, ASSISTments2017, Statics2011, Junyi). |
| **QA3 Split/Leakage Transparency** | 1 | 80/20 split reported; precomputed hypergraph matrices temporal split isolation is unverified. |
| **QA4 Baseline/Ablation Adequacy** | 2 | Comprehensive baselines + extensive ablation of dual hypergraph channels & cross-view SSL. |
| **QA5 Statistical Uncertainty** | 1 | Reports mean metrics across seeds; formal non-parametric significance testing omitted. |
| **QA6 Author Artifacts** | 1 | IEEE TNNLS peer-reviewed journal article full text verified. |
| **QA7 Sparse Construct Validity** | 1 | Motivates model via data sparsity, but lacks isolated zero-exposure KC cold-start evaluation protocol. |
| **QA8 Computational Transparency** | 1 | Describes hypergraph and line-graph complexity; formal runtime/memory scaling curves omitted. |

**Raw Quality Score:** 11 / 16  
**Normalized Quality:** 0.6875 (**MODERATE Quality**)

---

# 5. Methodological Summary & Codebook Stress-Test Insights

1. **Cross-View Hypergraph Contrastive Learning:** KT066 stress-tests the SSL cross-view contrastive family (`MULTIVIEW_CONTRASTIVE`) where hypergraph views are contrasted against dual line-graph transformations.
2. **Dual-Channel Encoder (`HGNN_HYPERGRAPH`):** Combines simplified and collaborative hypergraph convolution networks across global pattern and local knowledge channels.
3. **CB13 Verification (`resampling_repeats` vs `n_seeds`):** Coded `n_seeds = 5` and `resampling_repeats = 1` (`SEED_REPETITION`).
4. **CB16 Verification (`coding_completeness`):** Marked `FULLTEXT_CODED` from full IEEE TNNLS journal paper inspection.
