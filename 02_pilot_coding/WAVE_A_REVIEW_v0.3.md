# WAVE_A_REVIEW_v0.3

## Order completed

KT004 → KT039 → KT035 → KT014

## KT004

Status: **ADJUDICATED FOR PILOT**.

Accepted:
- `MODEL_DEFINED_FIXED`
- `SEQUENTIAL_TRANSITION`
- required field-level evidence table
- topology-based definition of `directed`
- relation-category definition of `typed_edges`
- QA6 excludes third-party implementations
- six model entries retained

## KT039 — CL4KT

Status: **PRIMARY CODED** from official ACM metadata and authors' implementation repository.

Core coding:
- `kt_central_task=Y`
- `G_criterion=N`
- `S_criterion=Y`
- `PRIMARY_CORE`
- `ssl_family=SEQUENCE_CONTRASTIVE`
- `temporal_backbone=SELF_ATTENTION_TRANSFORMER`
- augmentations: mask, crop, reorder/permute, replace
- `educational_structure_preservation=NO_EXPLICIT_CONSTRAINT`
- author code/config/environment artifacts are available
- sparse-KC focus was not established from the inspected sources

New candidate issue:
- distinguish `AUTHOR_CODE` evidence from manuscript-stated evidence.

## KT035 — HHSKT

Status: **PARTIAL — FULL TEXT REQUIRED**.

Authoritative abstract supports:
- KT centrality;
- heterogeneous graph construction;
- graph neural network framing;
- short-term/windowing attention;
- three real-world benchmark datasets;
- average AUC improvement up to 3%.

The accessible authoritative source does **not** support final coding of:
- graph source/provenance;
- node/edge types;
- exact temporal backbone;
- fusion details;
- dataset names;
- split;
- statistical testing;
- calibration;
- computational details.

These remain `UNCLEAR/NR`; do not fill them from secondary assumptions.

## KT014 — PDKT-C

Status: **PRIMARY CODED** from the author-hosted full paper.

Core coding:
- `G_criterion=Y`, `S_criterion=N`, `PRIMARY_CORE`
- expert-labeled prerequisite graph
- `graph_provenance=EXTERNAL_FIXED`
- `graph_representation=KC_KC`
- directed prerequisite relation
- `gnn_encoder=NONE`
- `temporal_backbone=RNN_LSTM_GRU`
- `fusion_type=REGULARIZATION_ONLY`
- `sparsity_construct=GENERIC_DATA_SPARSITY`
- five datasets
- main comparison 70/10/20
- repeated random split/selection 10 times
- AUC, ACC, MAE, RMSE
- hardware reported

Important correction:
An explicit graph can be central to Graph-Based KT without a GNN. The legacy survey's “graph module / unspecified GNN” coding for KT014 should therefore be reconsidered.

## v0.4 candidates after Wave A

- CB13: add `resampling_repeats` separate from `n_seeds`.
- CB14: explicitly state Graph-Based KT does not require a GNN encoder.
- CB15: add `AUTHOR_CODE` / evidence source type.
- CB16: add coding-completeness flag for abstract-only/full-text status.
- CB17: separate evidence source scope: paper vs author code vs metadata vs reproduced.

## Gate

Do **not** freeze the codebook yet.  
Next action should be:
1. resolve Wave-A CB13–CB17;
2. create `coding_codebook_v0.4_PILOT`;
3. if desired, perform second coding/adjudication for KT039 and KT014;
4. obtain HHSKT full text before final pilot adjudication.
