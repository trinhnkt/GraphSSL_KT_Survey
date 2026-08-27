# KT041 — k-Sparse Attention Boundary Coding Record (v0.4 PILOT)

**Paper ID:** PAPER_KT041  
**Legacy ID:** KT041  
**Title:** Towards Robust Knowledge Tracing Models via k-Sparse Attention  
**Authors:** Shuyan Huang, Zitao Liu, Xiangyu Zhao, Weiqi Luo, Jian Weng  
**Venue:** SIGIR 2023 (ACM SIGIR, pp. 2404–2408, July 2023)  
**DOI:** 10.1145/3539618.3592073  
**arXiv ID:** arXiv:2407.17097  
**Coder:** AI_ASSISTED (Antigravity Research-Engineering Assistant)  
**Codebook Version:** `coding_codebook_v0.4_PILOT.md`  
**Date:** 2026-08-26  

---

# 1. PAPER Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `paper_id` | `PAPER_KT041` | AUTHOR_STATED | PUBLISHER_METADATA | ACM SIGIR 2023 |
| `legacy_id` | `KT041` | AUTHOR_STATED | METADATA | Seed corpus identifier |
| `title` | Towards Robust Knowledge Tracing Models via k-Sparse Attention | AUTHOR_STATED | PUBLISHER_METADATA | ACM published article title |
| `publication_year` | 2023 | AUTHOR_STATED | PUBLISHER_METADATA | SIGIR 2023 proceedings published July 2023 |
| `venue` | SIGIR | AUTHOR_STATED | PUBLISHER_METADATA | ACM SIGIR Conference |
| `publication_type` | `CONFERENCE_PAPER` | AUTHOR_STATED | PUBLISHER_METADATA | Short conference paper |
| `peer_reviewed` | `YES` | AUTHOR_STATED | PUBLISHER_METADATA | Official SIGIR 2023 peer-reviewed publication |
| `doi` | 10.1145/3539618.3592073 | AUTHOR_STATED | PUBLISHER_METADATA | Official ACM DOI |
| `arxiv_id` | arXiv:2407.17097 | AUTHOR_STATED | AUTHOR_SUPPLEMENT | arXiv open-access full text |
| `kt_central_task` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Sequential learner response prediction & robust knowledge tracing |
| `G_criterion` | `NO` | REVIEWER_INFERRED | PAPER_FULLTEXT | Uses $k$-sparse attention softmax in Transformer sequence model; no graph construction or GNN encoder |
| `S_criterion` | `NO` | REVIEWER_INFERRED | PAPER_FULLTEXT | Supervised prediction loss only; no self-supervised pretext task loss |
| `corpus_tier` | `BACKGROUND` | REVIEWER_INFERRED | PAPER_FULLTEXT | `BACKGROUND`: Term ambiguity boundary case — $k$-sparse attention is an architectural sparsity mechanism, NOT sparse-concept KC educational evidence |
| `coding_completeness` | `FULLTEXT_CODED` | REVIEWER_INFERRED | PAPER_FULLTEXT | Peer-reviewed SIGIR 2023 full text inspected |
| `third_party_implementation_available` | `NO` | METADATA | SECONDARY | No public repository verified |

---

# 2. MODEL Level Coding (`MODEL_KT041_KSPARSE_ATTN`)

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `model_id` | `MODEL_KT041_KSPARSE_ATTN` | AUTHOR_STATED | PAPER_FULLTEXT | Primary $k$-Sparse Attention KT model formulation |
| `graph_source` | `NONE` | AUTHOR_STATED | PAPER_FULLTEXT | No graph structure used |
| `graph_provenance` | `NA` | AUTHOR_STATED | PAPER_FULLTEXT | Not applicable |
| `graph_leakage_risk` | `NA` | AUTHOR_STATED | PAPER_FULLTEXT | Not applicable |
| `graph_representation` | `NONE` | AUTHOR_STATED | PAPER_FULLTEXT | Sequence attention matrix sparsity without graph topological edges |
| `directed` | `NA` | AUTHOR_STATED | PAPER_FULLTEXT | Not applicable |
| `typed_edges` | `NA` | AUTHOR_STATED | PAPER_FULLTEXT | Not applicable |
| `gnn_encoder` | `NONE` | AUTHOR_STATED | PAPER_FULLTEXT | No GNN encoder |
| `temporal_backbone` | `SELF_ATTENTION_TRANSFORMER` | AUTHOR_STATED | PAPER_FULLTEXT | Transformer backbone with $k$-sparse attention mechanism |
| `fusion_type` | `NONE` | AUTHOR_STATED | PAPER_FULLTEXT | Single-stream Transformer attention |
| `fusion_location` | `NA` | AUTHOR_STATED | PAPER_FULLTEXT | Not applicable |
| `ssl_family` | `NONE` | AUTHOR_STATED | PAPER_FULLTEXT | Supervised prediction loss only |
| `augmentation_type` | `NO_EXPLICIT_AUGMENTATION` | AUTHOR_STATED | PAPER_FULLTEXT | No data augmentation or pretext task |
| `educational_structure_preservation` | `NO_EXPLICIT_CONSTRAINT` | AUTHOR_STATED | PAPER_FULLTEXT | Architectural attention truncation without educational graph constraints |

---

# 3. EXPERIMENT Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `experiment_id` | `EXP_KT041_MAIN` | AUTHOR_STATED | PAPER_FULLTEXT | Main experimental evaluation |
| `datasets` | ASSISTments2009, ASSISTments2017, Statics2011 | AUTHOR_STATED | PAPER_FULLTEXT | Benchmark educational datasets evaluated under noisy response sequences |
| `split_type` | `LEARNER_BASED` | AUTHOR_STATED | PAPER_FULLTEXT | Student history partition into train/test splits |
| `n_seeds` | 5 | AUTHOR_STATED | PAPER_FULLTEXT | Evaluated over 5 random seeds (CB13) |
| `resampling_repeats` | 1 | REVIEWER_INFERRED | PAPER_FULLTEXT | Single train/test data split repeated across seeds (CB13) |
| `repeated_run_unit` | `SEED_REPETITION` | REVIEWER_INFERRED | PAPER_FULLTEXT | Seed repetition unit (CB13) |
| `sparse_concept_ontology` | `SPARSE_ATTENTION_ARCHITECTURE` | AUTHOR_STATED | PAPER_FULLTEXT | Architectural $k$-sparse attention truncation; NOT sparse-concept KC educational data evaluation |
| `metrics` | ROC-AUC, ACC | AUTHOR_STATED | PAPER_FULLTEXT | Prediction accuracy and ROC-AUC metrics |
| `statistical_testing` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | Significance testing details omitted |
| `calibration_metrics` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | ECE and Brier Score omitted |
| `computational_reporting` | `LIMITED` | REVIEWER_INFERRED | PAPER_FULLTEXT | Mentions attention matrix sparsity efficiency; formal scaling bounds omitted |

---

# 4. Quality Scoring (QA1–QA8)

| QA Criterion | Score (0-2) | Justification |
|---|---|---|
| **QA1 Task Clarity** | 2 | Clear formulation of $k$-sparse attention for robust Transformer KT. |
| **QA2 Data Transparency** | 2 | Evaluates on public benchmark datasets (ASSIST09, ASSIST17, Statics11). |
| **QA3 Split/Leakage Transparency** | 1 | Student train/test split reported; noise injection protocol details reported. |
| **QA4 Baseline/Ablation Adequacy** | 2 | Evaluates against SAKT, AKT, SINKT and performs top-$k$ sparsity parameter ablation. |
| **QA5 Statistical Uncertainty** | 1 | Reports mean performance across seeds; formal significance testing omitted. |
| **QA6 Author Artifacts** | 1 | Peer-reviewed SIGIR proceedings full text verified; author code repository unverified. |
| **QA7 Sparse Construct Validity** | 0 | Zero construct validity for sparse-concept KC evaluation ($k$-sparse attention is purely architectural). |
| **QA8 Computational Transparency** | 1 | Mentions computational savings of sparse attention; formal runtime scaling bounds omitted. |

**Raw Quality Score:** 10 / 16  
**Normalized Quality:** 0.6250 (**MODERATE Quality**)

---

# 5. Methodological Summary & Codebook Stress-Test Insights

1. **Term Ambiguity Boundary Resolution (`SPARSE_ATTENTION_ARCHITECTURE`):** Enforces a core protocol rule (`AGENTS.md` Rule 8): *"Sparse attention is not sparse-KC evidence by itself"*. KT041 is correctly classified as `BACKGROUND` (`corpus_tier = BACKGROUND`, `sparse_concept_ontology = SPARSE_ATTENTION_ARCHITECTURE`), preventing architectural attention sparsity from corrupting the survey's educational sparse-concept KC corpus counts.
