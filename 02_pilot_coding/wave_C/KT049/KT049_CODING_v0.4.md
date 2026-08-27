# KT049 — Cold-Start LLM Coding Record (v0.4 PILOT)

**Paper ID:** PAPER_KT049  
**Legacy ID:** KT049  
**Title:** Mitigating Cold-Start Problems in Knowledge Tracing with Large Language Models: An Attribute-Aware Approach  
**Authors:** Yuxiang Guo, Shuanghong Shen, Qi Liu, Zhenya Huang, Linbo Zhu, Yu Su, Enhong Chen  
**Venue:** CIKM 2024 (ACM CIKM, pp. 682–692, Oct. 2024)  
**DOI:** 10.1145/3627673.3679664  
**arXiv ID:** NR  
**Coder:** AI_ASSISTED (Antigravity Research-Engineering Assistant)  
**Codebook Version:** `coding_codebook_v0.4_PILOT.md`  
**Date:** 2026-08-26  

---

# 1. PAPER Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `paper_id` | `PAPER_KT049` | AUTHOR_STATED | PUBLISHER_METADATA | ACM CIKM 2024 |
| `legacy_id` | `KT049` | AUTHOR_STATED | METADATA | Seed corpus identifier |
| `title` | Mitigating Cold-Start Problems in Knowledge Tracing with Large Language Models: An Attribute-Aware Approach | AUTHOR_STATED | PUBLISHER_METADATA | ACM published article title |
| `publication_year` | 2024 | AUTHOR_STATED | PUBLISHER_METADATA | CIKM 2024 proceedings published Oct 2024 |
| `venue` | CIKM | AUTHOR_STATED | PUBLISHER_METADATA | ACM CIKM Conference |
| `publication_type` | `CONFERENCE_PAPER` | AUTHOR_STATED | PUBLISHER_METADATA | Full conference proceedings paper |
| `peer_reviewed` | `YES` | AUTHOR_STATED | PUBLISHER_METADATA | Official CIKM 2024 peer-reviewed publication |
| `doi` | 10.1145/3627673.3679664 | AUTHOR_STATED | PUBLISHER_METADATA | Official ACM DOI |
| `arxiv_id` | `NR` | AUTHOR_STATED | PUBLISHER_METADATA | Published direct to CIKM proceedings |
| `kt_central_task` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Sequential learner performance prediction under cold-start conditions |
| `G_criterion` | `NO` | REVIEWER_INFERRED | PAPER_FULLTEXT | Uses LLM text attribute embeddings directly in sequence tracing without explicit graph topology or GNN encoder |
| `S_criterion` | `NO` | REVIEWER_INFERRED | PAPER_FULLTEXT | Supervised prediction loss only; no self-supervised pretext task loss |
| `corpus_tier` | `PRIMARY_ADJACENT_SPARSE` | REVIEWER_INFERRED | PAPER_FULLTEXT | `PRIMARY_ADJACENT_SPARSE`: Addresses RQ4 cold-start lens without satisfying G-criterion or S-criterion |
| `coding_completeness` | `FULLTEXT_CODED` | REVIEWER_INFERRED | PAPER_FULLTEXT | Peer-reviewed CIKM 2024 proceedings full text inspected |
| `third_party_implementation_available` | `NO` | METADATA | SECONDARY | No public repository verified |

---

# 2. MODEL Level Coding (`MODEL_KT049_LLM_ATTRIB`)

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `model_id` | `MODEL_KT049_LLM_ATTRIB` | AUTHOR_STATED | PAPER_FULLTEXT | Primary Attribute-Aware LLM KT model formulation |
| `graph_source` | `NONE` | AUTHOR_STATED | PAPER_FULLTEXT | Direct LLM question attribute text encoding without graph construction |
| `graph_provenance` | `NA` | AUTHOR_STATED | PAPER_FULLTEXT | No graph representation used |
| `graph_leakage_risk` | `NA` | AUTHOR_STATED | PAPER_FULLTEXT | No graph structure used |
| `graph_representation` | `NONE` | AUTHOR_STATED | PAPER_FULLTEXT | Text attribute embeddings without graph topological edges |
| `directed` | `NA` | AUTHOR_STATED | PAPER_FULLTEXT | Not applicable |
| `typed_edges` | `NA` | AUTHOR_STATED | PAPER_FULLTEXT | Not applicable |
| `gnn_encoder` | `NONE` | AUTHOR_STATED | PAPER_FULLTEXT | No GNN message passing |
| `temporal_backbone` | `RNN_LSTM_GRU` | AUTHOR_STATED | PAPER_FULLTEXT | Deep sequence backbone for learner state tracking |
| `fusion_type` | `CONCAT, ATTENTION` | AUTHOR_STATED | PAPER_FULLTEXT | Concatenates LLM text attribute embeddings into sequence input representations |
| `fusion_location` | `INPUT` | AUTHOR_STATED | PAPER_FULLTEXT | Injected at input representation layer |
| `ssl_family` | `NONE` | AUTHOR_STATED | PAPER_FULLTEXT | Supervised prediction loss only |
| `augmentation_type` | `NO_EXPLICIT_AUGMENTATION` | AUTHOR_STATED | PAPER_FULLTEXT | No data augmentation or pretext task |
| `educational_structure_preservation` | `NO_EXPLICIT_CONSTRAINT` | AUTHOR_STATED | PAPER_FULLTEXT | Uses LLM attribute text embeddings directly |

---

# 3. EXPERIMENT Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `experiment_id` | `EXP_KT049_MAIN` | AUTHOR_STATED | PAPER_FULLTEXT | Main experimental evaluation |
| `datasets` | ASSISTments2009, ASSISTments2012, EPub | AUTHOR_STATED | PAPER_FULLTEXT | Real-world benchmark educational datasets evaluated in cold-start settings |
| `split_type` | `ITEM_KC_COLD_START` | AUTHOR_STATED | PAPER_FULLTEXT | Zero-exposure question/KC cold-start split evaluating unseen items |
| `n_seeds` | 5 | AUTHOR_STATED | PAPER_FULLTEXT | Performance averaged over 5 random seeds (CB13) |
| `resampling_repeats` | 1 | REVIEWER_INFERRED | PAPER_FULLTEXT | Single train/test data split repeated across model seeds (CB13) |
| `repeated_run_unit` | `SEED_REPETITION` | REVIEWER_INFERRED | PAPER_FULLTEXT | Seed repetition unit (CB13) |
| `sparse_concept_ontology` | `ITEM_COLD_START, STRICT_KC_COLD_START` | AUTHOR_STATED | PAPER_FULLTEXT | Evaluates zero-exposure item and KC cold-start scenarios using LLM textual attributes |
| `metrics` | ROC-AUC, ACC | AUTHOR_STATED | PAPER_FULLTEXT | Prediction accuracy and ROC-AUC metrics |
| `statistical_testing` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | Significance testing details omitted |
| `calibration_metrics` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | ECE and Brier Score omitted |
| `computational_reporting` | `LIMITED` | REVIEWER_INFERRED | PAPER_FULLTEXT | Mentions LLM text prompt processing; formal scaling bounds omitted |

---

# 4. Quality Scoring (QA1–QA8)

| QA Criterion | Score (0-2) | Justification |
|---|---|---|
| **QA1 Task Clarity** | 2 | Clear formulation of LLM attribute-aware cold-start knowledge tracing. |
| **QA2 Data Transparency** | 2 | Evaluates on public benchmark datasets (ASSIST09, ASSIST12, EPub). |
| **QA3 Split/Leakage Transparency** | 2 | Zero-exposure cold-start evaluation protocol explicitly reported. |
| **QA4 Baseline/Ablation Adequacy** | 2 | Evaluates against standard KT baselines and performs LLM attribute ablation. |
| **QA5 Statistical Uncertainty** | 1 | Reports mean performance across seeds; formal significance testing omitted. |
| **QA6 Author Artifacts** | 1 | Peer-reviewed CIKM proceedings full text verified; author code repository unverified. |
| **QA7 Sparse Construct Validity** | 2 | Strong construct validity for cold-start evaluation without forcing Graph/SSL gateway. |
| **QA8 Computational Transparency** | 1 | Describes LLM attribute prompt extraction; formal runtime scaling bounds omitted. |

**Raw Quality Score:** 13 / 16  
**Normalized Quality:** 0.8125 (**HIGH Quality**)

---

# 5. Methodological Summary & Codebook Stress-Test Insights

1. **`PRIMARY_ADJACENT_SPARSE` Gateway Enforcement:** KT049 provides a clear test for the survey's gateway rules. It addresses the sparse-concept / cold-start lens (RQ4) via LLM attribute embeddings (`ITEM_COLD_START`), but does **not** use a GNN/graph mechanism (`G_criterion = N`) or an SSL pretext task (`S_criterion = N`). It is correctly classified as `PRIMARY_ADJACENT_SPARSE`, serving as contextual evidence for RQ4 without distorting the primary Graph/SSL gateway counts.
