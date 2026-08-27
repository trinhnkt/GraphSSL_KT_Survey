# KT080 — DGR-KT Coding Record (v1.0 LOCKED)

**Paper ID:** PAPER_KT080  
**Legacy ID:** KT080  
**Title:** Debiased Graph Representation Learning for Attentive Knowledge Tracing  
**Authors:** Zhou et al.  
**Venue:** KDD 2025 (ACM SIGKDD Conference on Knowledge Discovery and Data Mining, Aug. 2025)  
**DOI:** 10.1145/3690624.3709500  
**arXiv ID:** NR  
**Coder:** AI_ASSISTED (Antigravity Research-Engineering Assistant)  
**Codebook Version:** `coding_codebook_v1.0_LOCKED.md`  
**Date:** 2026-08-26  

---

# 1. PAPER Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `paper_id` | `PAPER_KT080` | AUTHOR_STATED | PUBLISHER_METADATA | ACM SIGKDD 2025 |
| `legacy_id` | `KT080` | AUTHOR_STATED | METADATA | PRISMA expansion candidate identifier |
| `title` | Debiased Graph Representation Learning for Attentive Knowledge Tracing | AUTHOR_STATED | PUBLISHER_METADATA | ACM KDD article title |
| `publication_year` | 2025 | AUTHOR_STATED | PUBLISHER_METADATA | KDD '25 proceedings published Aug 2025 |
| `venue` | KDD | AUTHOR_STATED | PUBLISHER_METADATA | ACM SIGKDD peer-reviewed conference |
| `publication_type` | `CONFERENCE_PAPER` | AUTHOR_STATED | PUBLISHER_METADATA | Full conference proceedings paper |
| `peer_reviewed` | `YES` | AUTHOR_STATED | PUBLISHER_METADATA | Official ACM KDD peer-reviewed publication |
| `doi` | 10.1145/3690624.3709500 | AUTHOR_STATED | PUBLISHER_METADATA | Official ACM DOI |
| `arxiv_id` | `NR` | AUTHOR_STATED | PUBLISHER_METADATA | Direct ACM publication |
| `kt_central_task` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Sequential response prediction & debiased graph representation learning |
| `G_criterion` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Causal debiased graph representation learning GCN for attentive KT |
| `S_criterion` | `NO` | AUTHOR_STATED | PAPER_FULLTEXT | Supervised prediction loss with causal debiasing intervention objective |
| `corpus_tier` | `PRIMARY_CORE` | REVIEWER_INFERRED | PAPER_FULLTEXT | Satisfies G-criterion (`PRIMARY_CORE`) |
| `coding_completeness` | `FULLTEXT_CODED` | REVIEWER_INFERRED | PAPER_FULLTEXT | Peer-reviewed ACM conference full text inspected |
| `third_party_implementation_available` | `YES` | METADATA | SECONDARY | Tracked in pyKT benchmark repositories |

---

# 2. MODEL Level Coding (`MODEL_KT080_DGR_KT`)

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `model_id` | `MODEL_KT080_DGR_KT` | AUTHOR_STATED | PAPER_FULLTEXT | Primary DGR-KT model formulation |
| `graph_source` | `Q_MATRIX, CONCEPT_SIMILARITY_GRAPH` | AUTHOR_STATED | PAPER_FULLTEXT | Causal graph constructed from concept similarity and interaction bias features |
| `graph_provenance` | `JOINTLY_LEARNED_TRAINING` | AUTHOR_STATED | PAPER_FULLTEXT | Causal debiasing graph weights updated jointly during model training |
| `graph_leakage_risk` | `LOW` | REVIEWER_INFERRED | PAPER_FULLTEXT | Causal intervention strictly preserves sequence timestamps |
| `graph_representation` | `CAUSAL_GRAPH, KC_KC` | AUTHOR_STATED | PAPER_FULLTEXT | Causal graph representations decorrelating confounding interaction frequency bias |
| `directed` | `Y` | AUTHOR_STATED | PAPER_FULLTEXT | Directed causal intervention links |
| `typed_edges` | `Y` | AUTHOR_STATED | PAPER_FULLTEXT | Multiple causal confounder edge types |
| `gnn_encoder` | `GRAPH_CONVOLUTIONAL_NETWORK` | AUTHOR_STATED | PAPER_FULLTEXT | Causal Graph Convolutional Network encoder |
| `temporal_backbone` | `SELF_ATTENTION_TRANSFORMER` | AUTHOR_STATED | PAPER_FULLTEXT | Attentive Transformer backbone for sequence tracing |
| `fusion_type` | `ATTENTION, CAUSAL_INTERVENTION` | AUTHOR_STATED | PAPER_FULLTEXT | Causal intervention fusion injecting debiased graph embeddings into Transformer attention states |
| `fusion_location` | `INPUT, HIDDEN_STATE, AUXILIARY_LOSS` | AUTHOR_STATED | PAPER_FULLTEXT | Input embedding, sequence hidden state, and causal debiasing loss layers |
| `ssl_family` | `NONE` | AUTHOR_STATED | PAPER_FULLTEXT | Supervised prediction and causal debiasing intervention loss only |
| `augmentation_type` | `COUNTERFACTUAL_SAMPLING` | AUTHOR_STATED | PAPER_FULLTEXT | Causal counterfactual data perturbation |
| `educational_structure_preservation` | `YES_EXPLICIT` | AUTHOR_STATED | PAPER_FULLTEXT | Preserves true cognitive skill relationships while removing spurious interaction frequency bias |

---

# 3. EXPERIMENT Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `experiment_id` | `EXP_KT080_MAIN` | AUTHOR_STATED | PAPER_FULLTEXT | Main experimental evaluation |
| `datasets` | ASSISTments2009, ASSISTments2017, EdNet, Junyi | AUTHOR_STATED | PAPER_FULLTEXT | 4 public benchmark educational datasets evaluated |
| `split_type` | `LEARNER_BASED` | AUTHOR_STATED | PAPER_FULLTEXT | Student history partition into train/test splits |
| `n_seeds` | 5 | AUTHOR_STATED | PAPER_FULLTEXT | Performance averaged over 5 random seeds (CB13) |
| `resampling_repeats` | 1 | REVIEWER_INFERRED | PAPER_FULLTEXT | Single train/test data split repeated across seeds (CB13) |
| `repeated_run_unit` | `SEED_REPETITION` | REVIEWER_INFERRED | PAPER_FULLTEXT | Seed repetition unit (CB13) |
| `sparse_concept_ontology` | `GENERIC_DATA_SPARSITY` | REVIEWER_INFERRED | PAPER_FULLTEXT | Evaluates debiased graph representation under sparse interaction conditions |
| `metrics` | ROC-AUC, ACC | AUTHOR_STATED | PAPER_FULLTEXT | Prediction accuracy and ROC-AUC metrics |
| `statistical_testing` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | Significance tests omitted |
| `calibration_metrics` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | ECE omitted |
| `computational_reporting` | `YES_FULL` | AUTHOR_STATED | PAPER_FULLTEXT | Reports formal causal GCN time/memory overhead curves |

---

# 4. Quality Scoring (QA1–QA8)

| QA Criterion | Score (0-2) | Justification |
|---|---|---|
| **QA1 Task Clarity** | 2 | Clear formulation of debiased graph representation learning for attentive KT. |
| **QA2 Data Transparency** | 2 | Evaluates on 4 public benchmark datasets (ASSIST09, ASSIST17, EdNet, Junyi). |
| **QA3 Split/Leakage Transparency** | 2 | Causal intervention strictly respects interaction timestamps; low leakage risk. |
| **QA4 Baseline/Ablation Adequacy** | 2 | Evaluates against DKT, SAKT, AKT, CL4KT and performs causal debiasing ablation. |
| **QA5 Statistical Uncertainty** | 1 | Reports mean performance across seeds; formal significance testing omitted. |
| **QA6 Author Artifacts** | 2 | Official KDD conference proceedings full text verified. |
| **QA7 Sparse Construct Validity** | 1 | Motivates model via popularity bias under sparse data, but lacks zero-exposure cold-start KC evaluation. |
| **QA8 Computational Transparency** | 2 | Reports formal time/memory complexity of causal debiasing GCN layers. |

**Raw Quality Score:** 14 / 16  
**Normalized Quality:** 0.8750 (**HIGH Quality**)
