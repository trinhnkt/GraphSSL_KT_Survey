# KT038 — DyGKT Coding Record (v0.4 PILOT)

**Paper ID:** PAPER_KT038  
**Legacy ID:** KT038  
**Title:** DyGKT: Dynamic Graph Learning for Knowledge Tracing  
**Authors:** Ke Cheng, Linzhi Peng, Pengyang Wang, Junchen Ye, Leilei Sun, Bowen Du  
**Venue:** KDD 2024 (ACM SIGKDD, pp. 251–262, Aug. 2024)  
**DOI:** 10.1145/3637528.3671773  
**arXiv ID:** arXiv:2407.20824  
**Coder:** AI_ASSISTED (Antigravity Research-Engineering Assistant)  
**Codebook Version:** `coding_codebook_v0.4_PILOT.md`  
**Date:** 2026-08-26  

---

# 1. PAPER Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `paper_id` | `PAPER_KT038` | AUTHOR_STATED | PUBLISHER_METADATA | ACM SIGKDD 2024 |
| `legacy_id` | `KT038` | AUTHOR_STATED | METADATA | Seed corpus identifier |
| `title` | DyGKT: Dynamic Graph Learning for Knowledge Tracing | AUTHOR_STATED | PUBLISHER_METADATA | ACM published article title |
| `publication_year` | 2024 | AUTHOR_STATED | PUBLISHER_METADATA | KDD 2024 proceedings published Aug 2024 |
| `venue` | KDD | AUTHOR_STATED | PUBLISHER_METADATA | ACM SIGKDD Conference on Knowledge Discovery and Data Mining |
| `publication_type` | `CONFERENCE_PAPER` | AUTHOR_STATED | PUBLISHER_METADATA | Full conference proceedings paper |
| `peer_reviewed` | `YES` | AUTHOR_STATED | PUBLISHER_METADATA | Official KDD 2024 peer-reviewed publication |
| `doi` | 10.1145/3637528.3671773 | AUTHOR_STATED | PUBLISHER_METADATA | Official ACM DOI |
| `arxiv_id` | arXiv:2407.20824 | AUTHOR_STATED | AUTHOR_SUPPLEMENT | arXiv open-access full text |
| `kt_central_task` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Sequential student response prediction over dynamic learning streams |
| `G_criterion` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Continuous-time dynamic question-answering graph with dynamic GNN message passing |
| `S_criterion` | `NO` | AUTHOR_STATED | PAPER_FULLTEXT | Supervised prediction loss only; no self-supervised pretext objective |
| `corpus_tier` | `PRIMARY_CORE` | REVIEWER_INFERRED | PAPER_FULLTEXT | `PRIMARY_CORE = KT AND (GRAPH_BASED OR SELF_SUPERVISED)` — satisfies G-criterion |
| `coding_completeness` | `FULLTEXT_CODED` | REVIEWER_INFERRED | PAPER_FULLTEXT | Peer-reviewed KDD paper full text inspected |
| `third_party_implementation_available` | `YES` | AUTHOR_STATED | AUTHOR_CODE | Official GitHub repository hosted by authors: `https://github.com/PengLinzhi/DyGKT` |

---

# 2. MODEL Level Coding (`MODEL_KT038_DyGKT`)

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `model_id` | `MODEL_KT038_DyGKT` | AUTHOR_STATED | PAPER_FULLTEXT | Primary DyGKT model formulation |
| `graph_source` | `LEARNED_FROM_INTERACTIONS, SEQUENTIAL_TRANSITION` | AUTHOR_STATED | PAPER_FULLTEXT | Continuous-time interaction stream constructing evolving question-answering graph |
| `graph_provenance` | `JOINTLY_LEARNED_TRAINING` | AUTHOR_STATED | PAPER_FULLTEXT | Continuous-time dynamic graph updated synchronously with student interaction events |
| `graph_leakage_risk` | `LOW` | REVIEWER_INFERRED | PAPER_FULLTEXT | Timestamped continuous-time graph update strictly preserves temporal train/test causality |
| `graph_representation` | `DYNAMIC_TEMPORAL, ITEM_ITEM` | AUTHOR_STATED | PAPER_FULLTEXT | Continuous-time dynamic graph over evolving student-question interaction states |
| `directed` | `Y` | AUTHOR_STATED | PAPER_FULLTEXT | Directed temporal interaction links from historical interactions to target query |
| `typed_edges` | `N` | AUTHOR_STATED | PAPER_FULLTEXT | Single continuous-time interaction relation type |
| `gnn_encoder` | `TEMPORAL_DYNAMIC_GNN` | AUTHOR_STATED | PAPER_FULLTEXT | Continuous-time dynamic GNN encoder with dual time encoder & multiset indicator |
| `temporal_backbone` | `TEMPORAL_GRAPH_NATIVE` | AUTHOR_STATED | PAPER_FULLTEXT | Native continuous-time dynamic graph temporal state update architecture |
| `fusion_type` | `JOINT_LATENT_STATE` | AUTHOR_STATED | PAPER_FULLTEXT | Joint temporal-graph state representation for continuous learner tracing |
| `fusion_location` | `HIDDEN_STATE` | AUTHOR_STATED | PAPER_FULLTEXT | Integrated within the temporal graph hidden state update loop |
| `ssl_family` | `NONE` | AUTHOR_STATED | PAPER_FULLTEXT | Supervised prediction loss only |
| `augmentation_type` | `NO_EXPLICIT_AUGMENTATION` | AUTHOR_STATED | PAPER_FULLTEXT | No data augmentation or pretext task |
| `educational_structure_preservation` | `YES_EXPLICIT` | AUTHOR_STATED | PAPER_FULLTEXT | Preserves exact temporal interaction timestamps and short/long-term interval semantics |

---

# 3. EXPERIMENT Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `experiment_id` | `EXP_KT038_MAIN` | AUTHOR_STATED | PAPER_FULLTEXT | Main experimental evaluation |
| `datasets` | ASSISTments2009, ASSISTments2017, Statics2011, EdNet, Junyi | AUTHOR_STATED | PAPER_FULLTEXT | 5 real-world benchmark educational datasets evaluated |
| `split_type` | `LEARNER_BASED` | AUTHOR_STATED | PAPER_FULLTEXT | Learner history partition into train/test splits |
| `n_seeds` | 5 | AUTHOR_STATED | PAPER_FULLTEXT | Evaluated across 5 random seeds (CB13) |
| `resampling_repeats` | 1 | REVIEWER_INFERRED | PAPER_FULLTEXT | Single train/test data partition repeated over 5 model seeds (CB13) |
| `repeated_run_unit` | `SEED_REPETITION` | REVIEWER_INFERRED | PAPER_FULLTEXT | Seed repetition unit (CB13) |
| `sparse_concept_ontology` | `GENERIC_DATA_SPARSITY` | REVIEWER_INFERRED | PAPER_FULLTEXT | Addresses continuous growing interaction data sparsity; no zero-exposure cold-start KC split evaluated |
| `metrics` | ROC-AUC, ACC | AUTHOR_STATED | PAPER_FULLTEXT | Prediction accuracy and ROC-AUC metrics |
| `statistical_testing` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | DeLong / Wilcoxon significance tests not formally reported |
| `calibration_metrics` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | ECE and Brier Score omitted |
| `computational_reporting` | `YES_FULL` | AUTHOR_STATED | PAPER_FULLTEXT | Formal time complexity, memory scaling, and empirical runtime efficiency curves reported |

---

# 4. Quality Scoring (QA1–QA8)

| QA Criterion | Score (0-2) | Justification |
|---|---|---|
| **QA1 Task Clarity** | 2 | Clear continuous-time dynamic graph formulation for knowledge tracing. |
| **QA2 Data Transparency** | 2 | Evaluates on 5 public benchmark datasets (ASSIST09, ASSIST17, Statics11, EdNet, Junyi). |
| **QA3 Split/Leakage Transparency** | 2 | Continuous-time dynamic temporal split explicitly preserves causal order; low leakage risk. |
| **QA4 Baseline/Ablation Adequacy** | 2 | Comprehensive comparison against standard KT baselines and extensive component ablation (time encoder & multiset indicator). |
| **QA5 Statistical Uncertainty** | 1 | Reports mean performance across 5 seeds; formal significance testing omitted. |
| **QA6 Author Artifacts** | 2 | Substantial author artifact available (official GitHub repository `https://github.com/PengLinzhi/DyGKT`). |
| **QA7 Sparse Construct Validity** | 1 | Motivates continuous data expansion and temporal interval semantics, but lacks zero-exposure KC cold-start protocol. |
| **QA8 Computational Transparency** | 2 | Reports formal time/memory complexity and empirical runtime curves. |

**Raw Quality Score:** 14 / 16  
**Normalized Quality:** 0.8750 (**HIGH Quality**)

---

# 5. Methodological Summary & Codebook Stress-Test Insights

1. **Native Dynamic Graph Coding (`DYNAMIC_TEMPORAL` & `TEMPORAL_DYNAMIC_GNN`):** DyGKT validates the codebook's continuous-time dynamic graph classification (`graph_representation = DYNAMIC_TEMPORAL`, `gnn_encoder = TEMPORAL_DYNAMIC_GNN`, `temporal_backbone = TEMPORAL_GRAPH_NATIVE`), proving that continuous-time temporal interaction graphs enter `PRIMARY_CORE`.
2. **Low Leakage Risk in Continuous Time (`LOW`):** Demonstrates that continuous-time graph updating based on interaction timestamps naturally preserves causal temporal split isolation (`graph_leakage_risk = LOW`).
3. **High Author Artifact Reproducibility (`QA6 = 2`):** Verified official author repository `https://github.com/PengLinzhi/DyGKT`.
4. **CB13 & CB16 Verification:** Verified `n_seeds = 5`, `resampling_repeats = 1` (`SEED_REPETITION`), and `coding_completeness = FULLTEXT_CODED`.
