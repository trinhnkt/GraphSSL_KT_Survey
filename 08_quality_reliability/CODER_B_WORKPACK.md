# Coder B work pack — 20 papers

You are the independent human coder. Do **not** open `inter_rater_coderA_locked_v1.0.csv`, manuscript tables, or the `why_included` column in `inter_rater_coding_sample_v1.0.csv` (that column leaks Coder A).

**Fill this file only:** `inter_rater_coding_sample_BLIND_EMPTY_v1.3.csv`

Do **not** open `inter_rater_coding_sample_BLIND_EMPTY_v1.2.csv` or `inter_rater_coding_sample_BLIND_v1.0.csv` (AI-filled). AI quote help: `CODER_B_AI_ASSIST_RULES_v1.0.md`.

**Locator pack (4–6 quotes/paper: SSL / graph / cold-start / ECE):** `CODER_B_LOCATOR_PACK_v1.1.md`. Decisions stay yours.

Also read: `CODER_B_INSTRUCTIONS.md`, `00_protocol/SCOPE_v1.0_LOCKED.md` §4–§6, `00_protocol/coding_codebook_v1.0_LOCKED.md` §6, §11, §16.

Time: about **20–30 minutes per paper** (6–10 hours total). One sitting or two evenings.

## Allowed values (copy exactly)

| Field | Tokens |
|---|---|
| `coderB_S_criterion` | `Y` / `N` |
| `coderB_ssl_family` | If Y: one of `MULTIVIEW_CONTRASTIVE`, `GRAPH_CONTRASTIVE`, `GRAPH_RECONSTRUCTION`, `SEQUENCE_CONTRASTIVE`. If N: `NONE` |
| `coderB_graph_provenance` | `MODEL_DEFINED_FIXED` / `EXTERNAL_FIXED` / `DYNAMIC_LEARNED` / `NA` |
| `coderB_gnn_encoder` | `NONE` / `GCN` / `GAT` / `GNN_GENERIC` / `HETEROGENEOUS_GNN` / `HYPERGRAPH_GNN` / `DYNAMIC_GNN` / `SPATIOTEMPORAL_GNN` / `OTHER` |
| cold-start + ECE | `YES` / `NO` |

`coderB_id`: your name or initials. Same value on every row.

`coderB_locator`: section or page, e.g. `Sec. 3.2; p. 4`.

`coderB_note`: one sentence from the PDF, not from memory of the survey.

## Decision rules (no paper answers)

**S = Y** only if there is a self-generated pretext / consistency / reconstruction target (SCOPE §5). The word “self-supervised” in the title is not enough.

**S = N** when the extra signal is only: inductive GNN, LLM-built graph, curriculum, RL, denoising, ordinary regularizer, dropout, or generic pretraining without a pretext target.

If S = N, family must be `NONE`. If S = Y, pick **one** exclusive family (the primary pretext).

**Provenance**

- `EXTERNAL_FIXED`: expert / curriculum / concept map / LLM-extracted graph supplied from outside the KT loss.
- `MODEL_DEFINED_FIXED`: graph prescribed by the architecture or a fixed formula, not an expert map and not a live learned graph.
- `DYNAMIC_LEARNED`: edges or topology evolve from interactions during training.
- `NA`: no explicit graph (sequence-only).

Graph-KT may have `gnn_encoder=NONE` if an explicit graph is still a central mechanism (regularizer, lookup, relational bias).

**Strict KC cold-start = YES** only if some KC has **zero** training-interaction exposure under the stated split. Interaction-drop, 80/20 learner split, or “sparse data” prose ≠ YES.

**Item cold-start**: new exercise/item, not a withheld KC.

**Learner cold-start**: new student or near-zero history protocol.

**ECE = YES** only if the manuscript reports Expected Calibration Error (or an explicit ECE table/formula). Brier or NLL alone is still `NO`.

## PDF map (`14_references/`)

| ID | Model | File |
|---|---|---|
| KT004 | GKT | `Graph-based Knowledge Tracing - Modeling Student Proficiency Using Graph Neural Network.pdf` |
| KT011 | Bi-CLKT | `Bi-CLKT - Bi-Graph Contrastive Learning Based Knowledge Tracing.pdf` |
| KT014 | PDKT-C | `Prerequisite-Driven Deep Knowledge Tracing.pdf` |
| KT026 | PEBG | `Improving Knowledge Tracing via Pre-training Question Embeddings.pdf` |
| KT031 | KSG-AKT | `Knowledge Structure Enhanced Graph Representation Learning Model for Attentive Knowledge Tracing.pdf` |
| KT035 | HHSKT | `HHSKT - A Learner-Question Interactions Based Heterogeneous Graph Neural Network Model for Knowledge Tracing.pdf` |
| KT037 | CMKT | `CMKT - Concept Map Driven Knowledge Tracing.pdf` |
| KT038 | DyGKT | `DyGKT - Dynamic Graph Learning for Knowledge Tracing.pdf` |
| KT039 | CL4KT | `Contrastive Learning for Knowledge Tracing.pdf` |
| KT042 | S2-HHN | `Self-Supervised Heterogeneous Hypergraph Network for Knowledge Tracing.pdf` |
| KT043 | 3V-CLKT | `Weighted Heterogeneous Graph-Based Three-View Contrastive Learning for Knowledge Tracing in Personalized e-Learning Systems.pdf` |
| KT044 | SINKT | `SINKT - A Structure-Aware Inductive Knowledge Tracing Model with Large Language Model.pdf` |
| KT047 | DC-SSL | `Fusing Hybrid Attentive Network with Self-Supervised Dual-Channel Heterogeneous Graph for Knowledge Tracing.pdf` |
| KT050 | GraphCA | `GraphCA - Learning From Graph Counterfactual Augmentation for Knowledge Tracing.pdf` |
| KT066 | HyperKT | `Dual-Channel Adaptive Scale Hypergraph Encoders With Cross-View Contrastive Learning for Knowledge Tracing.pdf` |
| KT068 | HKT | `HKT - Hierarchical Structure-Based Knowledge Tracing.pdf` |
| KT070 | Coda | `Denoising Programming Knowledge Tracing with a Code Graph-based Tuning Adaptor.pdf` |
| KT076 | KGNN-KT | `KGNN-KT - Enhancing Knowledge Tracing in Programming Education Through LLM-Extracted Knowledge Graphs.pdf` |
| KT077 | R2GCurL | `R2GCurL - Reinforced Robust Knowledge Tracing via Dynamic Graph Curriculum Learning.pdf` |
| KT079 | STG-SKT | `Spatio-Temporal Fusion in Graph Neural Network for Streaming Knowledge Tracing.pdf` |

Suggested order (method, then experiment): Method / model section first (S, family, provenance, encoder), then Experiments (three cold-starts + ECE). Search the PDF for: `contrastive`, `pretext`, `InfoNCE`, `reconstruct`, `cold-start`, `zero-shot`, `unseen concept`, `ECE`, `calibration`.

## After you finish

Send back only `inter_rater_coding_sample_BLIND_EMPTY_v1.3.csv`. Do not compute \(\kappa\). Do not look at Coder A.
