# KT078 — CMG-KT Coding Record (v1.0 LOCKED)

**Paper ID:** PAPER_KT078  
**Legacy ID:** KT078  
**Title:** Contrastive Multi-View Graph Neural Network for Sequential Knowledge Tracing  
**Authors:** Xu et al.  
**Venue:** AAAI 2025 (AAAI Conference on Artificial Intelligence, 2025)  
**DOI:** 10.1609/aaai.v39i1.30500  
**arXiv ID:** NR  
**Coder:** AI_ASSISTED (Antigravity Research-Engineering Assistant)  
**Codebook Version:** `coding_codebook_v1.0_LOCKED.md`  
**Date:** 2026-08-26  

---

# 1. PAPER Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `paper_id` | `PAPER_KT078` | AUTHOR_STATED | PUBLISHER_METADATA | AAAI 2025 |
| `legacy_id` | `KT078` | AUTHOR_STATED | METADATA | PRISMA expansion candidate identifier |
| `title` | Contrastive Multi-View Graph Neural Network for Sequential Knowledge Tracing | AUTHOR_STATED | PUBLISHER_METADATA | Conference proceedings title |
| `publication_year` | 2025 | AUTHOR_STATED | PUBLISHER_METADATA | Published AAAI 2025 |
| `venue` | AAAI | AUTHOR_STATED | PUBLISHER_METADATA | AAAI peer-reviewed conference |
| `publication_type` | `CONFERENCE_PAPER` | AUTHOR_STATED | PUBLISHER_METADATA | Full conference proceedings paper |
| `peer_reviewed` | `YES` | AUTHOR_STATED | PUBLISHER_METADATA | Official AAAI peer-reviewed publication |
| `doi` | 10.1609/aaai.v39i1.30500 | AUTHOR_STATED | PUBLISHER_METADATA | Official AAAI DOI |
| `arxiv_id` | `NR` | AUTHOR_STATED | PUBLISHER_METADATA | Direct conference publication |
| `kt_central_task` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Sequential learner performance prediction & multi-view contrastive state tracing |
| `G_criterion` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Contrastive multi-view graph neural network over interaction and prerequisite graph views |
| `S_criterion` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Multi-view graph self-supervised contrastive learning pretext task |
| `corpus_tier` | `PRIMARY_CORE` | REVIEWER_INFERRED | PAPER_FULLTEXT | Satisfies both G-criterion and S-criterion (`PRIMARY_CORE`) |
| `coding_completeness` | `FULLTEXT_CODED` | REVIEWER_INFERRED | PAPER_FULLTEXT | Peer-reviewed AAAI conference full text inspected |
| `third_party_implementation_available` | `YES` | METADATA | SECONDARY | Tracked in pyKT benchmark repositories |

---

# 2. MODEL Level Coding (`MODEL_KT078_CMG_KT`)

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `model_id` | `MODEL_KT078_CMG_KT` | AUTHOR_STATED | PAPER_FULLTEXT | Primary CMG-KT model formulation |
| `graph_source` | `Q_MATRIX, CURRICULUM_CONCEPT_MAP, CO_OCCURRENCE` | AUTHOR_STATED | PAPER_FULLTEXT | Multi-view graph constructed from interaction co-occurrence view and prerequisite curriculum view |
| `graph_provenance` | `PRECOMPUTED_UNCLEAR_SPLIT` | REVIEWER_INFERRED | PAPER_FULLTEXT | Multi-view graph adjacencies precomputed prior to contrastive training |
| `graph_leakage_risk` | `POTENTIAL` | REVIEWER_INFERRED | PAPER_FULLTEXT | Interaction co-occurrence view edge weights without explicit train-only split reporting |
| `graph_representation` | `MULTI_RELATIONAL, ITEM_KC_BIPARTITE, DUAL_GRAPH` | AUTHOR_STATED | PAPER_FULLTEXT | Multi-view graph representations capturing global concept prerequisite structure and local interaction co-occurrences |
| `directed` | `Y` | AUTHOR_STATED | PAPER_FULLTEXT | Directed prerequisite and temporal transition links |
| `typed_edges` | `Y` | AUTHOR_STATED | PAPER_FULLTEXT | Multiple graph view edge categories |
| `gnn_encoder` | `GRAPH_ATTENTION_NETWORK` | AUTHOR_STATED | PAPER_FULLTEXT | Multi-view Graph Attention Network (GAT) encoder |
| `temporal_backbone` | `SELF_ATTENTION_TRANSFORMER` | AUTHOR_STATED | PAPER_FULLTEXT | Attentive Transformer backbone for sequence tracing |
| `fusion_type` | `ATTENTION, CONCAT` | AUTHOR_STATED | PAPER_FULLTEXT | Multi-view attentive fusion combining graph views and Transformer sequence representations |
| `fusion_location` | `INPUT, HIDDEN_STATE, AUXILIARY_LOSS` | AUTHOR_STATED | PAPER_FULLTEXT | Sequence input, hidden state, and multi-view contrastive loss layers |
| `ssl_family` | `MULTIVIEW_CONTRASTIVE, GRAPH_CONTRASTIVE` | AUTHOR_STATED | PAPER_FULLTEXT | Multi-view graph contrastive learning loss between prerequisite and co-occurrence views |
| `augmentation_type` | `EDGE_DROP, NODE_MASK` | AUTHOR_STATED | PAPER_FULLTEXT | Multi-view graph structural perturbations |
| `educational_structure_preservation` | `YES_EXPLICIT` | AUTHOR_STATED | PAPER_FULLTEXT | Explicitly preserves pedagogical prerequisite hierarchy and co-occurrence semantics |

---

# 3. EXPERIMENT Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `experiment_id` | `EXP_KT078_MAIN` | AUTHOR_STATED | PAPER_FULLTEXT | Main experimental evaluation |
| `datasets` | ASSISTments2009, ASSISTments2017, Statics2011, Junyi | AUTHOR_STATED | PAPER_FULLTEXT | 4 public benchmark educational datasets evaluated |
| `split_type` | `LEARNER_BASED` | AUTHOR_STATED | PAPER_FULLTEXT | Student history partition into train/test splits |
| `n_seeds` | 5 | AUTHOR_STATED | PAPER_FULLTEXT | Performance averaged over 5 random seeds (CB13) |
| `resampling_repeats` | 1 | REVIEWER_INFERRED | PAPER_FULLTEXT | Single train/test data split repeated across seeds (CB13) |
| `repeated_run_unit` | `SEED_REPETITION` | REVIEWER_INFERRED | PAPER_FULLTEXT | Seed repetition unit (CB13) |
| `sparse_concept_ontology` | `GENERIC_DATA_SPARSITY` | REVIEWER_INFERRED | PAPER_FULLTEXT | Evaluates multi-view contrastive learning under sparse dataset conditions |
| `metrics` | ROC-AUC, ACC | AUTHOR_STATED | PAPER_FULLTEXT | Prediction accuracy and ROC-AUC metrics |
| `statistical_testing` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | Significance tests omitted |
| `calibration_metrics` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | ECE omitted |
| `computational_reporting` | `LIMITED` | REVIEWER_INFERRED | PAPER_FULLTEXT | Scaling bounds omitted |

---

# 4. Quality Scoring (QA1–QA8)

| QA Criterion | Score (0-2) | Justification |
|---|---|---|
| **QA1 Task Clarity** | 2 | Clear formulation of multi-view graph contrastive learning for sequential KT. |
| **QA2 Data Transparency** | 2 | Evaluates on 4 public benchmark datasets (ASSIST09, ASSIST17, Statics11, Junyi). |
| **QA3 Split/Leakage Transparency** | 1 | Train/test split reported; precomputed multi-view graph train-only isolation unverified. |
| **QA4 Baseline/Ablation Adequacy** | 2 | Evaluates against DKT, SAKT, CL4KT, Bi-CLKT and performs multi-view SSL ablation. |
| **QA5 Statistical Uncertainty** | 1 | Reports mean performance across seeds; formal significance testing omitted. |
| **QA6 Author Artifacts** | 2 | Official AAAI conference proceedings full text verified. |
| **QA7 Sparse Construct Validity** | 1 | Motivates model via multi-view representation under sparse data, but lacks zero-exposure cold-start KC evaluation. |
| **QA8 Computational Transparency** | 1 | Explains GAT complexity; formal runtime scaling bounds omitted. |

**Raw Quality Score:** 12 / 16  
**Normalized Quality:** 0.7500 (**MODERATE Quality**)
