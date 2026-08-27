# coding_codebook_v0.4_PILOT.md

## Coding Codebook — Pilot Version 0.4

**Survey:** Graph-Based and Self-Supervised Knowledge Tracing in Sparse-Concept Settings: A Systematic Survey and Research Agenda  
**Version:** v0.4 — PILOT, NOT FROZEN  
**Date:** 2026-08-10

Parent documents:
- `SCOPE_v1.0_LOCKED.md`
- `RQs_v1.0_LOCKED.md`
- `SLR_PROTOCOL_v1.0_LOCKED.md`

This version incorporates decisions from Wave A review (KT004, KT039, KT035, KT014), resolving candidates CB13–CB17. It remains a pilot version and is not frozen until the full pilot corpus is adjudicated.

---

# 0. Changelog (v0.3 → v0.4)

- **CB13 (Repeated runs vs Random Seeds):** Added `resampling_repeats` and `repeated_run_unit` to the `EXPERIMENT` level to separate repeated data-split/resampling runs from random initialization seeds (`n_seeds`).
- **CB14 (Graph-Based KT without GNN):** Explicitly stated that an explicit graph satisfies the Graph-Based KT gateway even when `gnn_encoder=NONE` if the graph serves as a central structural mechanism (e.g., regularization, lookup, loss constraint, as in KT014 PDKT-C).
- **CB15 (Evidence Source Type):** Added `evidence_source_type` (`PAPER_FULLTEXT`, `PUBLISHER_METADATA`, `AUTHOR_CODE`, `AUTHOR_SUPPLEMENT`, `SECONDARY`, `REPRODUCED`) to the field-level evidence table schema.
- **CB16 (Coding Completeness):** Added `coding_completeness` (`FULLTEXT_CODED`, `PARTIAL_SOURCE_ONLY`, `FULLTEXT_REQUIRED`, `METADATA_ONLY`) to track paper-level coding status.
- **CB17 (Evidence Scope Isolation):** Added explicit rule prohibiting the inference of paper-stated evaluation protocols or reported metrics solely from author code repository defaults.

---

# 1. Record hierarchy

Maintain three linked data levels:

```text
PAPER
  └── MODEL
        └── EXPERIMENT
```

- PAPER: bibliographic identity, eligibility, artifacts, paper-level quality, coding completeness.
- MODEL: graph construction, graph representation, GNN/encoder, temporal backbone, fusion, SSL.
- EXPERIMENT: dataset, preprocessing, split, resampling repeats, sparse/cold-start condition, metrics, statistics, calibration, compute.

A substantively distinct graph-construction/provenance mechanism may create a separate model entry even when the remaining GKT architecture is shared.

---

# 2. Field-level evidence table — REQUIRED

Create a separate long-form evidence table:

```text
evidence_id
entity_level
entity_id
field_name
coded_value
coding_basis
evidence_source_type
evidence_locator
evidence_note
source_url
coder_id
coder_type
coder_confidence
adjudication_status
```

## `entity_level`

- `PAPER`
- `MODEL`
- `EXPERIMENT`

## `coding_basis`

- `AUTHOR_STATED`
- `REVIEWER_INFERRED`
- `METADATA`
- `REPRODUCED`
- `MIXED`

## `evidence_source_type` — ADDED IN v0.4 (CB15)

- `PAPER_FULLTEXT`: Stated directly in peer-reviewed text or author manuscript.
- `PUBLISHER_METADATA`: Official publisher record / DOI metadata.
- `AUTHOR_CODE`: Official author-hosted code, configuration, or environment repository.
- `AUTHOR_SUPPLEMENT`: Appendix, online supplementary material hosted by authors.
- `SECONDARY`: Third-party review, library (e.g., pyKT), or benchmark paper.
- `REPRODUCED`: Empirical run performed directly by survey reviewers.

## Evidence Scope Isolation Rule — ADDED IN v0.4 (CB17)

Do **not** infer manuscript-reported evaluation protocol details (e.g., split percentages, sequence truncation, reported AUC/ACC) solely from author repository defaults or scripts unless confirmed in the paper text. Facts derived from repository code must set `evidence_source_type = AUTHOR_CODE` and remain strictly isolated from paper-stated claims (`PAPER_FULLTEXT`).

## `coder_type`

- `HUMAN`
- `AI_ASSISTED`
- `ADJUDICATED`

The main coding tables may retain row-level evidence notes for convenience, but the field-level evidence table is the audit source of truth for nontrivial decisions.

Do not store long copyrighted quotations. Store a page/section/table locator plus a short paraphrase.

---

# 3. Missing values

Use:

- `NR` = relevant information not reported;
- `NA` = not applicable;
- `UNCLEAR` = information exists but cannot be coded confidently;
- `TBD_VERIFY` = factual/metadata verification still required.

Do not leave applicable final fields blank.

---

# 4. Corpus status & Coding Completeness

## Corpus Tier

- `PRIMARY_CORE`
- `PRIMARY_ADJACENT_SPARSE`
- `PRIMARY_ADJACENT_METHOD`
- `BACKGROUND`
- `EXCLUDE_FULLTEXT`

Gateway:

```text
PRIMARY_CORE = KT AND (GRAPH_BASED OR SELF_SUPERVISED)
```

## `coding_completeness` — ADDED IN v0.4 (CB16)

Track paper-level inspection completeness:

- `FULLTEXT_CODED`: Peer-reviewed full text inspected; all applicable fields coded.
- `PARTIAL_SOURCE_ONLY`: Inspecting available text/code, but key sections missing or partially accessible.
- `FULLTEXT_REQUIRED`: Abstract/metadata inspected; full text required before final adjudication (e.g., KT035).
- `METADATA_ONLY`: Coded solely from bibliographic record or abstract.

---

# 5. Graph source

`graph_source`:

- `NONE`
- `EXPERT_PREREQUISITE`
- `CURRICULUM_CONCEPT_MAP`
- `Q_MATRIX`
- `CO_OCCURRENCE`
- `SEQUENTIAL_TRANSITION`
- `SIMILARITY`
- `LEARNED_FROM_INTERACTIONS`
- `SEMANTIC_TEXT`
- `LLM_ASSISTED`
- `HYBRID_MULTI_SOURCE`
- `OTHER`
- `UNCLEAR`

## `SEQUENTIAL_TRANSITION`

Use when edges/weights are derived from **ordered transitions** between concepts/items, such as the count or probability that node j immediately follows node i.

Do not collapse this to co-occurrence when order/direction is part of the construction.

---

# 6. Graph provenance

`graph_provenance`:

- `EXTERNAL_FIXED`
- `MODEL_DEFINED_FIXED`
- `TRAIN_ONLY_INFERRED`
- `JOINTLY_LEARNED_TRAINING`
- `FULL_DATA_INFERRED`
- `PRECOMPUTED_UNCLEAR_SPLIT`
- `MIXED_PROVENANCE`
- `NA`
- `UNCLEAR`

## `MODEL_DEFINED_FIXED`

Use when the graph is prescribed by the model architecture or mathematical definition and is:

- not supplied by an external expert/curriculum source;
- not inferred from interaction data;
- not jointly learned.

Example: a uniform dense graph fixed by the architecture.

---

# 7. Leakage coding

`graph_leakage_risk`:

- `LOW`
- `POTENTIAL`
- `HIGH`
- `NA`
- `UNCLEAR`

A data-derived precomputed graph whose train/test provenance is not reported should generally be coded `PRECOMPUTED_UNCLEAR_SPLIT` with `POTENTIAL` risk rather than assumed train-only.

Every `POTENTIAL` or `HIGH` value requires field-level evidence.

---

# 8. Graph representation

Multi-valued `graph_representation`:

- `KC_KC`
- `ITEM_ITEM`
- `ITEM_KC_BIPARTITE`
- `LEARNER_ITEM`
- `LEARNER_KC`
- `HETEROGENEOUS_MULTI_NODE`
- `HYPERGRAPH`
- `MULTI_RELATIONAL`
- `HIERARCHICAL`
- `DAG`
- `DYNAMIC_TEMPORAL`
- `SESSION_GRAPH`
- `OTHER`
- `NONE`
- `UNCLEAR`

---

# 9. Directionality

## `directed`

`Y/N/UNCLEAR/NA`

**Definition:** `directed` describes the **graph topology / adjacency relation**, not whether the implementation applies different incoming and outgoing message functions.

Examples:

- symmetric dense adjacency → `directed=N`;
- ordered transition i→j → `directed=Y`.

Use `message_passing_direction` to describe directional propagation rules.

---

# 10. Typed edges

## `typed_edges`

`Y/N/UNCLEAR/NA`

Use `Y` only when the model distinguishes **multiple edge/relation categories** as part of the graph representation or message-passing rule.

Do not set `typed_edges=Y` merely because:

- edges are directed;
- incoming and outgoing functions differ;
- attention has multiple heads.

Examples:

- one prerequisite relation type → usually `typed_edges=N`;
- VAE/NRI model with K latent edge types → `typed_edges=Y`;
- multi-relational graph with prerequisite/similarity/co-occurrence relations → `typed_edges=Y`.

Record the original edge names in `edge_types_original`.

---

# 11. Graph encoder — CLARIFIED IN v0.4 (CB14)

`gnn_encoder`:

- `NONE`
- `GCN`
- `GAT`
- `GRAPH_SAGE`
- `RGCN_RELATIONAL`
- `HETEROGENEOUS_GNN`
- `HGT`
- `HGNN_HYPERGRAPH`
- `TEMPORAL_DYNAMIC_GNN`
- `GRAPH_MEMORY`
- `GRAPH_ATTENTION_HYBRID`
- `OTHER`
- `UNCLEAR`

**Graph-KT Gateway without GNN Rule (CB14):** An explicit graph satisfies the Graph-Based KT gateway even when `gnn_encoder=NONE` if the graph serves as a central structural mechanism (e.g., loss regularization constraint, structural embedding lookup, or relational matrix bias). Confirmed in KT014 (PDKT-C), where expert prerequisite graphs constrain GRU representations without a message-passing GNN encoder.

---

# 12. Temporal KT backbone

- `BKT_HMM`
- `RNN_LSTM_GRU`
- `MEMORY_NETWORK`
- `SELF_ATTENTION_TRANSFORMER`
- `TEMPORAL_CONVOLUTION`
- `TEMPORAL_GRAPH_NATIVE`
- `STATE_SPACE`
- `OTHER`
- `UNCLEAR`

If an LLM provides semantic features but does not track learner state over time, put it in `semantic_auxiliary_encoder`, not `temporal_backbone`.

---

# 13. Fusion

`fusion_type`:

- `NONE`
- `CONCAT`
- `ADD`
- `GATE`
- `ATTENTION`
- `CROSS_ATTENTION`
- `MESSAGE_PASSING_IN_PREDICTION_LOOP`
- `GRAPH_INITIALIZATION`
- `REGULARIZATION_ONLY`
- `JOINT_LATENT_STATE`
- `LATE_FUSION`
- `TEACHER_STUDENT`
- `OTHER`
- `UNCLEAR`

`fusion_location`:

- `INPUT`
- `HIDDEN_STATE`
- `PREDICTION`
- `AUXILIARY_LOSS`
- `MULTI_STAGE`
- `OTHER`
- `UNCLEAR`
- `NA`

---

# 14. SSL family

- `NONE`
- `SEQUENCE_CONTRASTIVE`
- `GRAPH_CONTRASTIVE`
- `MULTIVIEW_CONTRASTIVE`
- `MASKED_INTERACTION`
- `MASKED_CONCEPT`
- `MASKED_GRAPH_MODELING`
- `GRAPH_RECONSTRUCTION`
- `RELATION_EDGE_PREDICTION`
- `GENERATIVE_PRETEXT`
- `TEACHER_STUDENT_SELF_DISTILLATION`
- `MULTITASK_HYBRID`
- `OTHER`
- `UNCLEAR`

Generic pretraining is not automatically SSL.

A VAE/KL term used solely for latent graph inference is not automatically a self-supervised KT pretext objective.

---

# 15. Augmentation and structure preservation

`augmentation_type` may be multi-valued:

- `INTERACTION_MASK`
- `INTERACTION_CROP`
- `INTERACTION_REORDER`
- `INTERACTION_REPLACE`
- `NODE_MASK`
- `NODE_DROP`
- `EDGE_DROP`
- `EDGE_ADD`
- `EDGE_REWEIGHT`
- `SUBGRAPH_SAMPLE`
- `RELATION_PERTURB`
- `DIFFICULTY_AWARE_MASK`
- `FREQUENCY_AWARE_MASK`
- `SEMANTIC_PERTURB`
- `NO_EXPLICIT_AUGMENTATION`
- `OTHER`
- `NA`
- `UNCLEAR`

`educational_structure_preservation`:

- `YES_EXPLICIT`
- `PARTIAL`
- `NO_EXPLICIT_CONSTRAINT`
- `NO_AUGMENTATION`
- `NA`
- `UNCLEAR`

---

# 16. Sparse/cold-start ontology

- `NO_EXPLICIT_FOCUS`
- `LOW_FREQUENCY_KC`
- `LONG_TAIL_KC`
- `STRICT_KC_COLD_START`
- `LOW_DEGREE_GRAPH_NODE`
- `ITEM_COLD_START`
- `LEARNER_COLD_START`
- `SHORT_HISTORY`
- `GENERIC_DATA_SPARSITY`
- `SPARSE_ATTENTION_ARCHITECTURE`
- `MULTIPLE`
- `UNCLEAR`

Strict KC cold-start means zero **training-interaction exposure**. Record graph/semantic/LLM information available to the held-out KC separately.

A preprocessing filter that removes low-frequency KCs is not, by itself, a sparse-KC evaluation.

---

# 17. Experiment Repeated Runs & Random Seeds — ADDED IN v0.4 (CB13)

In the `EXPERIMENT` level schema:

- `n_seeds`: Integer number of distinct random seed values reported or evaluated (e.g., 5 seeds).
- `resampling_repeats`: Integer count of repeated split / resampling runs (e.g., 10 runs of random 70/10/20 re-splits as in KT014 PDKT-C).
- `repeated_run_unit`: Unit of repeated execution:
  - `SPLIT_RESAMPLING`: Repeated random data partitioning.
  - `SEED_REPETITION`: Repeated runs over identical data splits with different model seeds.
  - `CROSS_VALIDATION_FOLD`: K-fold cross-validation iterations.
  - `RUN_AVERAGE`: Reported average over multiple runs without specified split detail.
  - `NA`: Single run.
  - `UNCLEAR`: Multiple runs reported without clear repeat mechanism.

Do **not** overload `n_seeds` when a paper executes repeated data resampling.

---

# 18. Reproducibility QA6

QA6 scores author-supported reproducibility artifacts.

- `0`: no author artifact;
- `1`: partial author artifact;
- `2`: substantial author artifact supporting meaningful reproduction.

A third-party reimplementation **does not increase QA6**. It may be recorded separately as `third_party_implementation_available`.

---

# 19. Quality scoring

Applicable criteria 0/1/2:

- QA1 task clarity
- QA2 data/preprocessing transparency
- QA3 split/provenance/leakage transparency
- QA4 baseline/ablation adequacy
- QA5 statistical uncertainty
- QA6 author artifacts
- QA7 sparse/cold-start construct validity
- QA8 computational transparency

Report:

```text
raw_quality_score
applicable_quality_max
normalized_quality = raw_quality_score / applicable_quality_max
```

Tiers:

- HIGH ≥ 0.80
- MODERATE 0.55–0.79
- LIMITED < 0.55

---

# 20. Adjudicated Examples Summary

| Paper ID | Model | graph_source | graph_provenance | gnn_encoder | evidence_source_type | coding_completeness |
|---|---|---|---|---|---|---|
| KT004 | GKT-Dense | OTHER | MODEL_DEFINED_FIXED | GCN | PAPER_FULLTEXT | FULLTEXT_CODED |
| KT004 | GKT-Transition | SEQUENTIAL_TRANSITION | PRECOMPUTED_UNCLEAR_SPLIT | GCN | PAPER_FULLTEXT | FULLTEXT_CODED |
| KT039 | CL4KT | NONE | NA | NONE | AUTHOR_CODE | FULLTEXT_CODED |
| KT035 | HHSKT | HETEROGENEOUS_MULTI_NODE | UNCLEAR | HETEROGENEOUS_GNN | PUBLISHER_METADATA | FULLTEXT_REQUIRED |
| KT014 | PDKT-C | EXPERT_PREREQUISITE | EXTERNAL_FIXED | NONE | PAPER_FULLTEXT | FULLTEXT_CODED |

---

# 21. v0.4 status

**Do not freeze v0.4.**

This version is active for Pilot Wave B, beginning with **KT011**.

Any new recurring issue identified during Wave B will be recorded for v0.5 before the full 15-paper pilot synthesis.
