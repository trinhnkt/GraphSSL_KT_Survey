# KT044 — SINKT Coding Record (v0.4 PILOT)

**Paper ID:** PAPER_KT044  
**Legacy ID:** KT044  
**Title:** SINKT: A Structure-Aware Inductive Knowledge Tracing Model with Large Language Model  
**Authors:** Lingyue Fu, Hao Guan, Kounianhua Du, Jianghao Lin, Wei Xia, Weinan Zhang, Ruiming Tang, Yasheng Wang, Yong Yu  
**Venue:** CIKM 2024 (ACM International Conference on Information and Knowledge Management, pp. 671–681, Oct. 2024)  
**DOI:** 10.1145/3627673.3679760  
**arXiv ID:** arXiv:2407.01245  
**Coder:** AI_ASSISTED (Antigravity Research-Engineering Assistant)  
**Codebook Version:** `coding_codebook_v0.4_PILOT.md`  
**Date:** 2026-08-26  

---

# 1. PAPER Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `paper_id` | `PAPER_KT044` | AUTHOR_STATED | PUBLISHER_METADATA | ACM CIKM 2024 |
| `legacy_id` | `KT044` | AUTHOR_STATED | METADATA | Seed corpus identifier |
| `title` | SINKT: A Structure-Aware Inductive Knowledge Tracing Model with Large Language Model | AUTHOR_STATED | PUBLISHER_METADATA | ACM published article title |
| `publication_year` | 2024 | AUTHOR_STATED | PUBLISHER_METADATA | CIKM 2024 proceedings published Oct 2024 |
| `venue` | CIKM | AUTHOR_STATED | PUBLISHER_METADATA | ACM CIKM Conference |
| `publication_type` | `CONFERENCE_PAPER` | AUTHOR_STATED | PUBLISHER_METADATA | Full conference proceedings paper |
| `peer_reviewed` | `YES` | AUTHOR_STATED | PUBLISHER_METADATA | Official CIKM 2024 peer-reviewed publication |
| `doi` | 10.1145/3627673.3679760 | AUTHOR_STATED | PUBLISHER_METADATA | Official ACM DOI |
| `arxiv_id` | arXiv:2407.01245 | AUTHOR_STATED | AUTHOR_SUPPLEMENT | arXiv open-access full text |
| `kt_central_task` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Sequential learner state estimation & inductive response prediction |
| `G_criterion` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Heterogeneous concept-question graph constructed with LLM semantic relation extraction & GNN layers |
| `S_criterion` | `NO` | AUTHOR_STATED | PAPER_FULLTEXT | Supervised prediction loss only; LLM used as semantic structure extractor, no SSL pretext loss |
| `corpus_tier` | `PRIMARY_CORE` | REVIEWER_INFERRED | PAPER_FULLTEXT | `PRIMARY_CORE = KT AND (GRAPH_BASED OR SELF_SUPERVISED)` — satisfies G-criterion |
| `coding_completeness` | `FULLTEXT_CODED` | REVIEWER_INFERRED | PAPER_FULLTEXT | Peer-reviewed CIKM 2024 proceedings full text inspected |
| `third_party_implementation_available` | `YES` | AUTHOR_STATED | AUTHOR_CODE | Official GitHub repository hosted by authors: `https://github.com/tubehao/SINKT` |

---

# 2. MODEL Level Coding (`MODEL_KT044_SINKT`)

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `model_id` | `MODEL_KT044_SINKT` | AUTHOR_STATED | PAPER_FULLTEXT | Primary SINKT model formulation |
| `graph_source` | `LLM_ASSISTED, SEMANTIC_TEXT, Q_MATRIX` | AUTHOR_STATED | PAPER_FULLTEXT | LLM extracts semantic dependencies & question-concept associations from text descriptions |
| `graph_provenance` | `JOINTLY_LEARNED_TRAINING` | AUTHOR_STATED | PAPER_FULLTEXT | LLM structural embeddings combined with trainable GNN attention layers |
| `graph_leakage_risk` | `LOW` | REVIEWER_INFERRED | PAPER_FULLTEXT | Target unseen KCs/questions rely strictly on text semantic descriptions; zero interaction history leakage |
| `graph_representation` | `HETEROGENEOUS_MULTI_NODE, KC_KC` | AUTHOR_STATED | PAPER_FULLTEXT | Heterogeneous question-concept graph with LLM-guided concept dependencies |
| `directed` | `Y` | AUTHOR_STATED | PAPER_FULLTEXT | Directed structural concept dependency edges derived by LLM |
| `typed_edges` | `Y` | AUTHOR_STATED | PAPER_FULLTEXT | Heterogeneous edge categories (concept-concept dependencies vs question-concept mappings) |
| `gnn_encoder` | `HETEROGENEOUS_GNN` | AUTHOR_STATED | PAPER_FULLTEXT | Heterogeneous Graph Attention Network (GAT) layers for structure-aware embedding |
| `temporal_backbone` | `SELF_ATTENTION_TRANSFORMER` | AUTHOR_STATED | PAPER_FULLTEXT | Transformer backbone tracks learner interactions over time (LLM is semantic feature provider) |
| `fusion_type` | `INPUT, CROSS_ATTENTION` | AUTHOR_STATED | PAPER_FULLTEXT | Fuses LLM semantic text features & graph representations at sequence input via attention |
| `fusion_location` | `INPUT, HIDDEN_STATE` | AUTHOR_STATED | PAPER_FULLTEXT | Injected at input embedding and Transformer attention sequence layers |
| `ssl_family` | `NONE` | AUTHOR_STATED | PAPER_FULLTEXT | Supervised prediction loss only |
| `augmentation_type` | `NO_EXPLICIT_AUGMENTATION` | AUTHOR_STATED | PAPER_FULLTEXT | No data augmentation or pretext task |
| `educational_structure_preservation` | `YES_EXPLICIT` | AUTHOR_STATED | PAPER_FULLTEXT | Preserves LLM-extracted educational concept semantics and dependency constraints |

---

# 3. EXPERIMENT Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `experiment_id` | `EXP_KT044_MAIN` | AUTHOR_STATED | PAPER_FULLTEXT | Main experimental evaluation |
| `datasets` | ASSISTments2009, ASSISTments2012, Junyi | AUTHOR_STATED | PAPER_FULLTEXT | Benchmark educational datasets evaluated in inductive cold-start setups |
| `split_type` | `LEARNER_BASED, ITEM_KC_COLD_START` | AUTHOR_STATED | PAPER_FULLTEXT | Evaluates both standard student splits and inductive zero-exposure question/concept cold-start splits |
| `n_seeds` | 5 | AUTHOR_STATED | PAPER_FULLTEXT | Evaluated across 5 random seeds (CB13) |
| `resampling_repeats` | 1 | REVIEWER_INFERRED | PAPER_FULLTEXT | Single random data split repeated across model seeds (CB13) |
| `repeated_run_unit` | `SEED_REPETITION` | REVIEWER_INFERRED | PAPER_FULLTEXT | Seed repetition unit (CB13) |
| `sparse_concept_ontology` | `STRICT_KC_COLD_START` | AUTHOR_STATED | PAPER_FULLTEXT | Evaluates inductive zero-exposure KC/question cold-start setting with zero training interaction history |
| `metrics` | ROC-AUC, ACC | AUTHOR_STATED | PAPER_FULLTEXT | Prediction accuracy and ROC-AUC metrics |
| `statistical_testing` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | Significance tests omitted |
| `calibration_metrics` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | ECE and Brier Score omitted |
| `computational_reporting` | `LIMITED` | REVIEWER_INFERRED | PAPER_FULLTEXT | Mentions LLM offline embedding extraction efficiency; formal scaling bounds omitted |

---

# 4. Quality Scoring (QA1–QA8)

| QA Criterion | Score (0-2) | Justification |
|---|---|---|
| **QA1 Task Clarity** | 2 | Clear formulation of structure-aware inductive knowledge tracing with LLM. |
| **QA2 Data Transparency** | 2 | Evaluates on public benchmark datasets (ASSIST09, ASSIST12, Junyi). |
| **QA3 Split/Leakage Transparency** | 2 | Zero-exposure inductive cold-start protocol explicitly isolates test items/KCs from training interactions. |
| **QA4 Baseline/Ablation Adequacy** | 2 | Evaluates against transductive/inductive KT baselines and conducts LLM/graph component ablations. |
| **QA5 Statistical Uncertainty** | 1 | Reports mean performance across seeds; formal significance testing omitted. |
| **QA6 Author Artifacts** | 2 | Substantial author artifact available (official GitHub repository `https://github.com/tubehao/SINKT`). |
| **QA7 Sparse Construct Validity** | 2 | Rigorous construct validity for `STRICT_KC_COLD_START` via inductive zero-exposure evaluation. |
| **QA8 Computational Transparency** | 1 | Describes LLM feature extraction workflow; formal runtime/memory scaling bounds omitted. |

**Raw Quality Score:** 14 / 16  
**Normalized Quality:** 0.8750 (**HIGH Quality**)

---

# 5. Methodological Summary & Codebook Stress-Test Insights

1. **Strict KC Cold-Start Construct Validity (`STRICT_KC_COLD_START`):** SINKT provides a gold-standard benchmark for `STRICT_KC_COLD_START`, demonstrating zero-exposure training interaction splits where target held-out KCs/questions rely strictly on LLM semantic representations.
2. **LLM Feature Provider vs Temporal Backbone Rule:** Validates Rule 2 of Wave C. The LLM acts as an auxiliary semantic feature provider (`graph_source = LLM_ASSISTED, SEMANTIC_TEXT`), while the `temporal_backbone` remains `SELF_ATTENTION_TRANSFORMER`.
3. **Inductive Heterogeneous Graph Representation (`HETEROGENEOUS_MULTI_NODE`):** Demonstrates how heterogeneous GNNs (`gnn_encoder = HETEROGENEOUS_GNN`) propagate LLM-extracted concept dependencies to new unseen items.
4. **High Reproducibility (`QA6 = 2`):** Verified official author repository `https://github.com/tubehao/SINKT`.
