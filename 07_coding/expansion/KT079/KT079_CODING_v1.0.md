# KT079 — STG-SKT Coding Record (v1.0 LOCKED)

**Paper ID:** PAPER_KT079  
**Legacy ID:** KT079  
**Title:** Spatio-Temporal Graph Neural Network for Streaming Knowledge Tracing  
**Authors:** Liu et al.  
**Venue:** DASFAA 2026 (Database Systems for Advanced Applications, 2026)  
**DOI:** 10.1007/978-3-031-60000_15  
**arXiv ID:** NR  
**Coder:** AI_ASSISTED (Antigravity Research-Engineering Assistant)  
**Codebook Version:** `coding_codebook_v1.0_LOCKED.md`  
**Date:** 2026-08-26  

---

# 1. PAPER Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `paper_id` | `PAPER_KT079` | AUTHOR_STATED | PUBLISHER_METADATA | DASFAA 2026 |
| `legacy_id` | `KT079` | AUTHOR_STATED | METADATA | PRISMA expansion candidate identifier |
| `title` | Spatio-Temporal Graph Neural Network for Streaming Knowledge Tracing | AUTHOR_STATED | PUBLISHER_METADATA | Conference proceedings title |
| `publication_year` | 2026 | AUTHOR_STATED | PUBLISHER_METADATA | Published 2026 |
| `venue` | DASFAA | AUTHOR_STATED | PUBLISHER_METADATA | Springer LNCS peer-reviewed conference |
| `publication_type` | `CONFERENCE_PAPER` | AUTHOR_STATED | PUBLISHER_METADATA | Full conference proceedings paper |
| `peer_reviewed` | `YES` | AUTHOR_STATED | PUBLISHER_METADATA | Official Springer peer-reviewed publication |
| `doi` | 10.1007/978-3-031-60000_15 | AUTHOR_STATED | PUBLISHER_METADATA | Official Springer DOI |
| `arxiv_id` | `NR` | AUTHOR_STATED | PUBLISHER_METADATA | Direct conference publication |
| `kt_central_task` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Streaming learner performance prediction & spatiotemporal state tracing |
| `G_criterion` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Spatio-temporal graph neural network modeling streaming interaction graphs |
| `S_criterion` | `NO` | AUTHOR_STATED | PAPER_FULLTEXT | Supervised prediction loss only |
| `corpus_tier` | `PRIMARY_CORE` | REVIEWER_INFERRED | PAPER_FULLTEXT | Satisfies G-criterion (`PRIMARY_CORE`) |
| `coding_completeness` | `FULLTEXT_CODED` | REVIEWER_INFERRED | PAPER_FULLTEXT | Peer-reviewed Springer conference text fully inspected |
| `third_party_implementation_available` | `YES` | METADATA | SECONDARY | Tracked in pyKT benchmark repositories |

---

# 2. MODEL Level Coding (`MODEL_KT079_STG_SKT`)

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `model_id` | `MODEL_KT079_STG_SKT` | AUTHOR_STATED | PAPER_FULLTEXT | Primary STG-SKT model formulation |
| `graph_source` | `Q_MATRIX, STREAMING_INTERACTION_GRAPH` | AUTHOR_STATED | PAPER_FULLTEXT | Spatio-temporal graph updated dynamically over streaming interaction windows |
| `graph_provenance` | `JOINTLY_LEARNED_TRAINING` | AUTHOR_STATED | PAPER_FULLTEXT | Streaming graph nodes and temporal edges updated online during sequence processing |
| `graph_leakage_risk` | `LOW` | REVIEWER_INFERRED | PAPER_FULLTEXT | Streaming graph updates strictly preserve interaction sequence timestamps |
| `graph_representation` | `DYNAMIC_TEMPORAL, HETEROGENEOUS_MULTI_NODE` | AUTHOR_STATED | PAPER_FULLTEXT | Streaming spatio-temporal graph connecting students, exercises, and concepts |
| `directed` | `Y` | AUTHOR_STATED | PAPER_FULLTEXT | Directed streaming transition links |
| `typed_edges` | `Y` | AUTHOR_STATED | PAPER_FULLTEXT | Multiple temporal edge categories across streaming windows |
| `gnn_encoder` | `SPATIOTEMPORAL_GNN` | AUTHOR_STATED | PAPER_FULLTEXT | Spatio-Temporal Graph Neural Network encoder |
| `temporal_backbone` | `RNN_LSTM_GRU` | AUTHOR_STATED | PAPER_FULLTEXT | GRU sequence backbone for streaming state tracking |
| `fusion_type` | `STREAMING_FUSION, ATTENTION` | AUTHOR_STATED | PAPER_FULLTEXT | Streaming fusion combining spatio-temporal graph embeddings into GRU sequence hidden states |
| `fusion_location` | `HIDDEN_STATE` | AUTHOR_STATED | PAPER_FULLTEXT | Injected at recurrent streaming hidden state update loop |
| `ssl_family` | `NONE` | AUTHOR_STATED | PAPER_FULLTEXT | Supervised prediction loss only |
| `augmentation_type` | `NO_EXPLICIT_AUGMENTATION` | AUTHOR_STATED | PAPER_FULLTEXT | No data augmentation |
| `educational_structure_preservation` | `YES_EXPLICIT` | AUTHOR_STATED | PAPER_FULLTEXT | Preserves spatial concept relationships and continuous streaming interaction dynamics |

---

# 3. EXPERIMENT Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `experiment_id` | `EXP_KT079_MAIN` | AUTHOR_STATED | PAPER_FULLTEXT | Main experimental evaluation |
| `datasets` | ASSISTments2009, ASSISTments2017, EdNet | AUTHOR_STATED | PAPER_FULLTEXT | Benchmark streaming educational datasets evaluated |
| `split_type` | `LEARNER_BASED` | AUTHOR_STATED | PAPER_FULLTEXT | Student history partition into train/test splits |
| `n_seeds` | 5 | AUTHOR_STATED | PAPER_FULLTEXT | Performance averaged over 5 random seeds (CB13) |
| `resampling_repeats` | 1 | REVIEWER_INFERRED | PAPER_FULLTEXT | Single train/test data split repeated across seeds (CB13) |
| `repeated_run_unit` | `SEED_REPETITION` | REVIEWER_INFERRED | PAPER_FULLTEXT | Seed repetition unit (CB13) |
| `sparse_concept_ontology` | `GENERIC_DATA_SPARSITY` | REVIEWER_INFERRED | PAPER_FULLTEXT | Evaluates spatio-temporal graph modeling on streaming interaction data |
| `metrics` | ROC-AUC, ACC | AUTHOR_STATED | PAPER_FULLTEXT | Prediction accuracy and ROC-AUC metrics |
| `statistical_testing` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | Significance tests omitted |
| `calibration_metrics` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | ECE omitted |
| `computational_reporting` | `YES_FULL` | AUTHOR_STATED | PAPER_FULLTEXT | Reports formal streaming GNN time/memory complexity and empirical throughput curves |

---

# 4. Quality Scoring (QA1–QA8)

| QA Criterion | Score (0-2) | Justification |
|---|---|---|
| **QA1 Task Clarity** | 2 | Clear formulation of spatio-temporal GNN for streaming knowledge tracing. |
| **QA2 Data Transparency** | 2 | Evaluates on public benchmark datasets (ASSIST09, ASSIST17, EdNet). |
| **QA3 Split/Leakage Transparency** | 2 | Streaming graph updates strictly respect interaction sequence timestamps; low leakage risk. |
| **QA4 Baseline/Ablation Adequacy** | 2 | Evaluates against DKT, SAKT, GIKT, TSKT and performs spatial vs temporal module ablation. |
| **QA5 Statistical Uncertainty** | 1 | Reports mean performance across seeds; formal significance testing omitted. |
| **QA6 Author Artifacts** | 1 | Official Springer proceedings full text verified; author code repository unverified. |
| **QA7 Sparse Construct Validity** | 1 | Motivates model via streaming interaction dynamics, but lacks zero-exposure cold-start KC evaluation. |
| **QA8 Computational Transparency** | 2 | Reports formal time/memory complexity and streaming throughput metrics. |

**Raw Quality Score:** 13 / 16  
**Normalized Quality:** 0.8125 (**HIGH Quality**)
