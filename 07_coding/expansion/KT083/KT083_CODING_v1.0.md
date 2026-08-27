# KT083 — DV-HGCL Coding Record (v1.0 LOCKED)

**Paper ID:** PAPER_KT083  
**Legacy ID:** KT083  
**Title:** Dual-View Heterogeneous Graph Contrastive Learning for Knowledge Tracing  
**Authors:** Zheng et al.  
**Venue:** Neural Networks, Vol. 182, Article 107500, Jan. 2026  
**DOI:** 10.1016/j.neunet.2026.107500  
**arXiv ID:** NR  
**Coder:** AI_ASSISTED (Antigravity Research-Engineering Assistant)  
**Codebook Version:** `coding_codebook_v1.0_LOCKED.md`  
**Date:** 2026-08-26  

---

# 1. PAPER Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `paper_id` | `PAPER_KT083` | AUTHOR_STATED | PUBLISHER_METADATA | Neural Networks 2026 |
| `legacy_id` | `KT083` | AUTHOR_STATED | METADATA | PRISMA expansion candidate identifier |
| `title` | Dual-View Heterogeneous Graph Contrastive Learning for Knowledge Tracing | AUTHOR_STATED | PUBLISHER_METADATA | Article title |
| `publication_year` | 2026 | AUTHOR_STATED | PUBLISHER_METADATA | Published Jan 2026 |
| `venue` | Neural Networks | AUTHOR_STATED | PUBLISHER_METADATA | Elsevier peer-reviewed journal |
| `publication_type` | `JOURNAL_ARTICLE` | AUTHOR_STATED | PUBLISHER_METADATA | Full journal article |
| `peer_reviewed` | `YES` | AUTHOR_STATED | PUBLISHER_METADATA | Official journal publication |
| `doi` | 10.1016/j.neunet.2026.107500 | AUTHOR_STATED | PUBLISHER_METADATA | Official DOI |
| `arxiv_id` | `NR` | AUTHOR_STATED | PUBLISHER_METADATA | Direct journal article |
| `kt_central_task` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Sequential learner response prediction & dual-view heterogeneous contrastive state tracing |
| `G_criterion` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Dual-view heterogeneous graph neural network over question and concept graphs |
| `S_criterion` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Dual-view heterogeneous graph contrastive learning pretext task |
| `corpus_tier` | `PRIMARY_CORE` | REVIEWER_INFERRED | PAPER_FULLTEXT | Satisfies both G-criterion and S-criterion (`PRIMARY_CORE`) |
| `coding_completeness` | `FULLTEXT_CODED` | REVIEWER_INFERRED | PAPER_FULLTEXT | Peer-reviewed journal full text inspected |
| `third_party_implementation_available` | `YES` | METADATA | SECONDARY | Tracked in pyKT benchmark repositories |

---

# 2. MODEL Level Coding (`MODEL_KT083_DV_HGCL`)

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `model_id` | `MODEL_KT083_DV_HGCL` | AUTHOR_STATED | PAPER_FULLTEXT | Primary DV-HGCL model formulation |
| `graph_source` | `Q_MATRIX, CURRICULUM_CONCEPT_MAP, SIMILARITY` | AUTHOR_STATED | PAPER_FULLTEXT | Dual-view heterogeneous graph constructed from question-level and concept-level structural views |
| `graph_provenance` | `PRECOMPUTED_UNCLEAR_SPLIT` | REVIEWER_INFERRED | PAPER_FULLTEXT | Heterogeneous graph adjacencies precomputed prior to contrastive learning |
| `graph_leakage_risk` | `LOW` | REVIEWER_INFERRED | PAPER_FULLTEXT | Question-concept heterogeneous structure constructed independently of student test splits |
| `graph_representation` | `HETEROGENEOUS_MULTI_NODE, DUAL_GRAPH` | AUTHOR_STATED | PAPER_FULLTEXT | Dual-view heterogeneous graph representations linking fine-grained questions and coarse-grained concepts |
| `directed` | `Y` | AUTHOR_STATED | PAPER_FULLTEXT | Directed prerequisite and bi-bipartite exercise-KC mapping links |
| `typed_edges` | `Y` | AUTHOR_STATED | PAPER_FULLTEXT | Multiple heterogeneous relation edge categories |
| `gnn_encoder` | `HETEROGENEOUS_GNN` | AUTHOR_STATED | PAPER_FULLTEXT | Dual-view Heterogeneous Graph Neural Network encoder |
| `temporal_backbone` | `RNN_LSTM_GRU` | AUTHOR_STATED | PAPER_FULLTEXT | GRU sequence backbone for temporal state tracking |
| `fusion_type` | `ATTENTION, CONCAT` | AUTHOR_STATED | PAPER_FULLTEXT | Attentive dual-view fusion injecting heterogeneous graph representations into GRU states |
| `fusion_location` | `INPUT, HIDDEN_STATE, AUXILIARY_LOSS` | AUTHOR_STATED | PAPER_FULLTEXT | Sequence input, hidden state, and dual-view contrastive loss layers |
| `ssl_family` | `GRAPH_CONTRASTIVE, MULTIVIEW_CONTRASTIVE` | AUTHOR_STATED | PAPER_FULLTEXT | Cross-view heterogeneous contrastive loss between question and concept graph views |
| `augmentation_type` | `NODE_MASK, SUBGRAPH_SAMPLE` | AUTHOR_STATED | PAPER_FULLTEXT | Heterogeneous graph structural perturbations |
| `educational_structure_preservation` | `YES_EXPLICIT` | AUTHOR_STATED | PAPER_FULLTEXT | Explicitly preserves question-concept bipartite associations and domain hierarchy |

---

# 3. EXPERIMENT Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `experiment_id` | `EXP_KT083_MAIN` | AUTHOR_STATED | PAPER_FULLTEXT | Main experimental evaluation |
| `datasets` | ASSISTments2009, ASSISTments2017, EdNet | AUTHOR_STATED | PAPER_FULLTEXT | 3 public benchmark educational datasets evaluated |
| `split_type` | `LEARNER_BASED` | AUTHOR_STATED | PAPER_FULLTEXT | Student history partition into train/test splits |
| `n_seeds` | 5 | AUTHOR_STATED | PAPER_FULLTEXT | Performance averaged over 5 random seeds (CB13) |
| `resampling_repeats` | 1 | REVIEWER_INFERRED | PAPER_FULLTEXT | Single train/test data split repeated across seeds (CB13) |
| `repeated_run_unit` | `SEED_REPETITION` | REVIEWER_INFERRED | PAPER_FULLTEXT | Seed repetition unit (CB13) |
| `sparse_concept_ontology` | `GENERIC_DATA_SPARSITY` | REVIEWER_INFERRED | PAPER_FULLTEXT | Evaluates dual-view contrastive learning under sparse question interaction data |
| `metrics` | ROC-AUC, ACC | AUTHOR_STATED | PAPER_FULLTEXT | Prediction accuracy and ROC-AUC metrics |
| `statistical_testing` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | Significance tests omitted |
| `calibration_metrics` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | ECE omitted |
| `computational_reporting` | `YES_FULL` | AUTHOR_STATED | PAPER_FULLTEXT | Reports formal heterogeneous GNN time/memory complexity curves |

---

# 4. Quality Scoring (QA1–QA8)

| QA Criterion | Score (0-2) | Justification |
|---|---|---|
| **QA1 Task Clarity** | 2 | Clear formulation of dual-view heterogeneous graph contrastive learning for KT. |
| **QA2 Data Transparency** | 2 | Evaluates on public benchmark datasets (ASSIST09, ASSIST17, EdNet). |
| **QA3 Split/Leakage Transparency** | 2 | Dual-view heterogeneous graph constructed independently of test split; low leakage risk. |
| **QA4 Baseline/Ablation Adequacy** | 2 | Evaluates against DKT, SAKT, GKT, Bi-CLKT, DC-SSL and performs view ablation. |
| **QA5 Statistical Uncertainty** | 1 | Reports mean performance across seeds; formal significance testing omitted. |
| **QA6 Author Artifacts** | 2 | Official Neural Networks journal full text verified. |
| **QA7 Sparse Construct Validity** | 1 | Motivates model via dual-view heterogeneous representation under sparse data, but lacks zero-exposure cold-start KC evaluation. |
| **QA8 Computational Transparency** | 2 | Reports formal time/memory complexity of dual-view GNN operations. |

**Raw Quality Score:** 14 / 16  
**Normalized Quality:** 0.8750 (**HIGH Quality**)
