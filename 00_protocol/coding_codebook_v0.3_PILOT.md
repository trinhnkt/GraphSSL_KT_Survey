# coding_codebook_v0.3_PILOT.md

## Coding Codebook — Pilot Version 0.3

**Survey:** Graph-Based and Self-Supervised Knowledge Tracing in Sparse-Concept Settings: A Systematic Survey and Research Agenda  
**Version:** v0.3 — PILOT, NOT FROZEN  
**Date:** 2026-08-09

Parent documents:
- `SCOPE_v1.0_LOCKED.md`
- `RQs_v1.0_LOCKED.md`
- `SLR_PROTOCOL_v1.0_LOCKED.md`

This version incorporates the KT004 adjudication. It must still be tested on the rest of Wave A and the full 15-paper pilot before becoming v1.0.

---

# 1. Record hierarchy

Maintain three linked data levels:

```text
PAPER
  └── MODEL
        └── EXPERIMENT
```

- PAPER: bibliographic identity, eligibility, artifacts, paper-level quality.
- MODEL: graph construction, graph representation, GNN/encoder, temporal backbone, fusion, SSL.
- EXPERIMENT: dataset, preprocessing, split, sparse/cold-start condition, metrics, statistics, calibration, compute.

A substantively distinct graph-construction/provenance mechanism may create a separate model entry even when the remaining GKT architecture is shared.

---

# 2. Field-level evidence table — REQUIRED

KT004 showed that one row-level `coding_basis/evidence_locator` is too coarse.

Create a separate long-form evidence table:

```text
evidence_id
entity_level
entity_id
field_name
coded_value
coding_basis
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

# 4. Corpus status

Use:

- `PRIMARY_CORE`
- `PRIMARY_ADJACENT_SPARSE`
- `PRIMARY_ADJACENT_METHOD`
- `BACKGROUND`
- `EXCLUDE_FULLTEXT`

Gateway:

```text
PRIMARY_CORE = KT AND (GRAPH_BASED OR SELF_SUPERVISED)
```

---

# 5. Graph source — UPDATED

`graph_source`:

- `NONE`
- `EXPERT_PREREQUISITE`
- `CURRICULUM_CONCEPT_MAP`
- `Q_MATRIX`
- `CO_OCCURRENCE`
- **`SEQUENTIAL_TRANSITION`**  ← added in v0.3
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

# 6. Graph provenance — UPDATED

`graph_provenance`:

- `EXTERNAL_FIXED`
- **`MODEL_DEFINED_FIXED`**  ← added in v0.3
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

# 9. Directionality — CLARIFIED

## `directed`

`Y/N/UNCLEAR/NA`

**Definition:** `directed` describes the **graph topology / adjacency relation**, not whether the implementation applies different incoming and outgoing message functions.

Examples:

- symmetric dense adjacency → `directed=N`;
- ordered transition i→j → `directed=Y`.

Use `message_passing_direction` to describe directional propagation rules.

---

# 10. Typed edges — CLARIFIED

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

# 11. Graph encoder

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

**Important:** an explicit graph may satisfy the Graph-Based KT gateway even when `gnn_encoder=NONE`, if the graph is used as a structural constraint, regularizer, lookup, or another central mechanism. This point remains to be stress-tested in KT014.

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

# 17. Reproducibility QA6 — CLARIFIED

QA6 scores author-supported reproducibility artifacts.

- `0`: no author artifact;
- `1`: partial author artifact;
- `2`: substantial author artifact supporting meaningful reproduction.

A third-party reimplementation **does not increase QA6**. It may be recorded separately as `third_party_implementation_available`.

---

# 18. Quality scoring

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

# 19. KT004 adjudicated examples

| Model | graph_source | graph_provenance | directed | typed_edges |
|---|---|---|---|---|
| GKT-Dense | OTHER | MODEL_DEFINED_FIXED | N | N |
| GKT-Transition | SEQUENTIAL_TRANSITION | PRECOMPUTED_UNCLEAR_SPLIT | Y | N |
| GKT-DKTGraph | LEARNED_FROM_INTERACTIONS | PRECOMPUTED_UNCLEAR_SPLIT | Y | N |
| GKT-PAM | LEARNED_FROM_INTERACTIONS | JOINTLY_LEARNED_TRAINING | Y | N |
| GKT-MHA | LEARNED_FROM_INTERACTIONS | JOINTLY_LEARNED_TRAINING | Y | N |
| GKT-VAE | LEARNED_FROM_INTERACTIONS | JOINTLY_LEARNED_TRAINING | Y | Y |

---

# 20. v0.3 status

**Do not freeze v0.3.**

The next stress tests are:

```text
KT039 → KT035 → KT014
```

Any new recurring issue becomes a candidate for v0.4 after Wave A review.
