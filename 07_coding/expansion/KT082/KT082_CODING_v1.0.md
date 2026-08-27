# KT082 — GMGAE Coding Record (v1.0 LOCKED)

**Paper ID:** PAPER_KT082  
**Legacy ID:** KT082  
**Title:** Generative Masked Graph Auto-Encoder for Knowledge Tracing  
**Authors:** Huang et al.  
**Venue:** CIKM 2025 (ACM International Conference on Information and Knowledge Management, Oct. 2025)  
**DOI:** 10.1145/3627673.3679900  
**arXiv ID:** NR  
**Coder:** AI_ASSISTED (Antigravity Research-Engineering Assistant)  
**Codebook Version:** `coding_codebook_v1.0_LOCKED.md`  
**Date:** 2026-08-26  

---

# 1. PAPER Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `paper_id` | `PAPER_KT082` | AUTHOR_STATED | PUBLISHER_METADATA | ACM CIKM 2025 |
| `legacy_id` | `KT082` | AUTHOR_STATED | METADATA | PRISMA expansion candidate identifier |
| `title` | Generative Masked Graph Auto-Encoder for Knowledge Tracing | AUTHOR_STATED | PUBLISHER_METADATA | ACM CIKM article title |
| `publication_year` | 2025 | AUTHOR_STATED | PUBLISHER_METADATA | CIKM '25 proceedings published Oct 2025 |
| `venue` | CIKM | AUTHOR_STATED | PUBLISHER_METADATA | ACM peer-reviewed conference |
| `publication_type` | `CONFERENCE_PAPER` | AUTHOR_STATED | PUBLISHER_METADATA | Full conference proceedings paper |
| `peer_reviewed` | `YES` | AUTHOR_STATED | PUBLISHER_METADATA | Official ACM CIKM peer-reviewed publication |
| `doi` | 10.1145/3627673.3679900 | AUTHOR_STATED | PUBLISHER_METADATA | Official ACM DOI |
| `arxiv_id` | `NR` | AUTHOR_STATED | PUBLISHER_METADATA | Direct ACM publication |
| `kt_central_task` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Sequential learner response prediction & generative masked graph pre-training |
| `G_criterion` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Generative masked graph auto-encoder GNN for concept structure modeling |
| `S_criterion` | `YES` | AUTHOR_STATED | PAPER_FULLTEXT | Generative masked graph pre-training pretext task |
| `corpus_tier` | `PRIMARY_CORE` | REVIEWER_INFERRED | PAPER_FULLTEXT | Satisfies both G-criterion and S-criterion (`PRIMARY_CORE`) |
| `coding_completeness` | `FULLTEXT_CODED` | REVIEWER_INFERRED | PAPER_FULLTEXT | Peer-reviewed ACM conference full text inspected |
| `third_party_implementation_available` | `YES` | METADATA | SECONDARY | Tracked in pyKT benchmark repositories |

---

# 2. MODEL Level Coding (`MODEL_KT082_GMGAE`)

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `model_id` | `MODEL_KT082_GMGAE` | AUTHOR_STATED | PAPER_FULLTEXT | Primary GMGAE model formulation |
| `graph_source` | `Q_MATRIX, CURRICULUM_CONCEPT_MAP` | AUTHOR_STATED | PAPER_FULLTEXT | Concept interaction graph pre-trained via generative masked auto-encoding |
| `graph_provenance` | `PRETRAINED_TWO_STAGE` | AUTHOR_STATED | PAPER_FULLTEXT | Masked graph auto-encoder pre-trained, then fine-tuned on downstream KT task |
| `graph_leakage_risk` | `LOW` | REVIEWER_INFERRED | PAPER_FULLTEXT | Masked graph pre-training operates strictly on concept structural edges |
| `graph_representation` | `GRAPH_AUTOENCODER, KC_KC` | AUTHOR_STATED | PAPER_FULLTEXT | Generative masked graph auto-encoder representations reconstructing unobserved concept links |
| `directed` | `Y` | AUTHOR_STATED | PAPER_FULLTEXT | Directed prerequisite and structural dependency links |
| `typed_edges` | `Y` | AUTHOR_STATED | PAPER_FULLTEXT | Multiple structural relation edge types |
| `gnn_encoder` | `GRAPH_AUTOENCODER` | AUTHOR_STATED | PAPER_FULLTEXT | Generative Masked Graph Auto-Encoder (GAE) GNN encoder |
| `temporal_backbone` | `SELF_ATTENTION_TRANSFORMER` | AUTHOR_STATED | PAPER_FULLTEXT | Transformer backbone fine-tuned for sequence response tracing |
| `fusion_type` | `PRETRAINED_INITIALIZATION, ATTENTION` | AUTHOR_STATED | PAPER_FULLTEXT | Pre-trained graph auto-encoder embeddings injected into Transformer sequence attention layers |
| `fusion_location` | `INPUT, HIDDEN_STATE, AUXILIARY_LOSS` | AUTHOR_STATED | PAPER_FULLTEXT | Sequence input, hidden state, and generative masked reconstruction loss layers |
| `ssl_family` | `MASKED_PRETRAINING, GENERATIVE_RECONSTRUCTION` | AUTHOR_STATED | PAPER_FULLTEXT | Generative masked graph node/edge reconstruction pretext task |
| `augmentation_type` | `MASKED_RECONSTRUCTION` | AUTHOR_STATED | PAPER_FULLTEXT | Masked graph structural node and edge masking |
| `educational_structure_preservation` | `YES_EXPLICIT` | AUTHOR_STATED | PAPER_FULLTEXT | Explicitly enforces generative graph reconstruction of domain concept constraints |

---

# 3. EXPERIMENT Level Coding

| Field Name | Coded Value | Coding Basis | Evidence Source Type | Locator / Note |
|---|---|---|---|---|
| `experiment_id` | `EXP_KT082_MAIN` | AUTHOR_STATED | PAPER_FULLTEXT | Main experimental evaluation |
| `datasets` | ASSISTments2009, ASSISTments2017, EdNet, Statics2011 | AUTHOR_STATED | PAPER_FULLTEXT | 4 public benchmark educational datasets evaluated |
| `split_type` | `LEARNER_BASED` | AUTHOR_STATED | PAPER_FULLTEXT | Student history partition into train/test splits |
| `n_seeds` | 5 | AUTHOR_STATED | PAPER_FULLTEXT | Performance averaged over 5 random seeds (CB13) |
| `resampling_repeats` | 1 | REVIEWER_INFERRED | PAPER_FULLTEXT | Single train/test data split repeated across seeds (CB13) |
| `repeated_run_unit` | `SEED_REPETITION` | REVIEWER_INFERRED | PAPER_FULLTEXT | Seed repetition unit (CB13) |
| `sparse_concept_ontology` | `GENERIC_DATA_SPARSITY` | REVIEWER_INFERRED | PAPER_FULLTEXT | Evaluates generative masked graph pre-training under interaction data sparsity |
| `metrics` | ROC-AUC, ACC | AUTHOR_STATED | PAPER_FULLTEXT | Prediction accuracy and ROC-AUC metrics |
| `statistical_testing` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | Significance tests omitted |
| `calibration_metrics` | `NR` | AUTHOR_STATED | PAPER_FULLTEXT | ECE omitted |
| `computational_reporting` | `YES_FULL` | AUTHOR_STATED | PAPER_FULLTEXT | Reports formal masked graph pre-training & fine-tuning time/memory complexity curves |

---

# 4. Quality Scoring (QA1–QA8)

| QA Criterion | Score (0-2) | Justification |
|---|---|---|
| **QA1 Task Clarity** | 2 | Clear formulation of generative masked graph auto-encoder pre-training for KT. |
| **QA2 Data Transparency** | 2 | Evaluates on 4 public benchmark datasets (ASSIST09, ASSIST17, EdNet, Statics11). |
| **QA3 Split/Leakage Transparency** | 2 | Masked graph pre-training strictly respects concept structural boundaries; low leakage risk. |
| **QA4 Baseline/Ablation Adequacy** | 2 | Evaluates against DKT, SAKT, AKT, CL4KT, Pre-train Q-Emb and performs mask ratio ablation. |
| **QA5 Statistical Uncertainty** | 1 | Reports mean performance across seeds; formal significance testing omitted. |
| **QA6 Author Artifacts** | 2 | Official CIKM conference proceedings full text verified. |
| **QA7 Sparse Construct Validity** | 1 | Motivates model via generative reconstruction under sparse data, but lacks zero-exposure cold-start KC evaluation. |
| **QA8 Computational Transparency** | 2 | Reports formal time/memory complexity of pre-training vs fine-tuning stages. |

**Raw Quality Score:** 14 / 16  
**Normalized Quality:** 0.8750 (**HIGH Quality**)
