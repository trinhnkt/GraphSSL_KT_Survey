# Coder B subset — DaoMT (10 papers, no locator)

**Path locked:** independent human pass. Open PDFs yourself. Do not ask an assistant for quotes or tokens.

You are Coder B for this subset only. Code from each PDF and the locked codebook.

**Fill this file only:** `inter_rater_coding_sample_BLIND_EMPTY_v1.4_DaoMT.csv`

`coderB_id` is already `DaoMT`. Do not change it. Do not copy rows from any other CSV.

Do **not** open locator packs, Coder A, manuscript tables, `BLIND_EMPTY_v1.3*.csv`, or the 20-row `BLIND_EMPTY_v1.4.csv`.

Also read: `protocol/SCOPE_v1.0_LOCKED.md` §4–§6, `protocol/coding_codebook_v1.0_LOCKED.md` §6, §11, §16.

Time: about **20–40 minutes per paper** (4–7 hours).

## Allowed values (copy exactly)

| Field | Tokens |
|---|---|
| `coderB_S_criterion` | `Y` / `N` |
| `coderB_ssl_family` | If Y: one of `MULTIVIEW_CONTRASTIVE`, `GRAPH_CONTRASTIVE`, `GRAPH_RECONSTRUCTION`, `SEQUENCE_CONTRASTIVE`. If N: `NONE` |
| `coderB_graph_provenance` | `MODEL_DEFINED_FIXED` / `EXTERNAL_FIXED` / `DYNAMIC_LEARNED` / `NA` |
| `coderB_gnn_encoder` | `NONE` / `GCN` / `GAT` / `GNN_GENERIC` / `HETEROGENEOUS_GNN` / `HYPERGRAPH_GNN` / `DYNAMIC_GNN` / `SPATIOTEMPORAL_GNN` / `OTHER` |
| cold-start + ECE | `YES` / `NO` |

`coderB_locator`: section or page you opened.

`coderB_note`: one sentence from that PDF.

## Decision rules (no paper answers)

**S = Y** only if there is a self-generated pretext / consistency / reconstruction target (SCOPE §5). The word “self-supervised” in the title is not enough.

**S = N** when the extra signal is only: inductive GNN, LLM-built graph, curriculum, RL, denoising, ordinary regularizer, dropout, or generic pretraining without a pretext target.

If S = N, family must be `NONE`. If S = Y, pick **one** exclusive family (the primary pretext).

**Provenance**

- `EXTERNAL_FIXED`: expert / curriculum / concept map / LLM-extracted graph supplied from outside the KT loss.
- `MODEL_DEFINED_FIXED`: graph prescribed by the architecture or a fixed formula, not an expert map and not a live learned graph.
- `DYNAMIC_LEARNED`: edges or topology evolve from interactions during training.
- `NA`: no explicit graph (sequence-only).

Graph-KT may have `gnn_encoder=NONE` if an explicit graph is still a central mechanism.

**Strict KC cold-start = YES** only if some KC has **zero** training-interaction exposure under the stated split. Interaction-drop, 80/20 learner split, or “sparse data” prose ≠ YES.

**Item cold-start**: new exercise/item, not a withheld KC.

**Learner cold-start**: new student or near-zero history protocol.

**ECE = YES** only if the manuscript reports Expected Calibration Error (or an explicit ECE table/formula). Brier or NLL alone is still `NO`.

## PDF map (`pdfs/` in this pack) — these 10 only

| ID | Model | File |
|---|---|---|
| KT004 | GKT | `Graph-based Knowledge Tracing - Modeling Student Proficiency Using Graph Neural Network.pdf` |
| KT011 | Bi-CLKT | `Bi-CLKT - Bi-Graph Contrastive Learning Based Knowledge Tracing.pdf` |
| KT014 | PDKT-C | `Prerequisite-Driven Deep Knowledge Tracing.pdf` |
| KT026 | PEBG | `Improving Knowledge Tracing via Pre-training Question Embeddings.pdf` |
| KT039 | CL4KT | `Contrastive Learning for Knowledge Tracing.pdf` |
| KT044 | SINKT | `SINKT - A Structure-Aware Inductive Knowledge Tracing Model with Large Language Model.pdf` |
| KT047 | DC-SSL | `Fusing Hybrid Attentive Network with Self-Supervised Dual-Channel Heterogeneous Graph for Knowledge Tracing.pdf` |
| KT068 | HKT | `HKT - Hierarchical Structure-Based Knowledge Tracing.pdf` |
| KT070 | Coda | `Denoising Programming Knowledge Tracing with a Code Graph-based Tuning Adaptor.pdf` |
| KT076 | KGNN-KT | `KGNN-KT - Enhancing Knowledge Tracing in Programming Education Through LLM-Extracted Knowledge Graphs.pdf` |

If KT076 is image-only, page images are in `kt076_pages/` (no codes on those images).

Method section first (S, family, provenance, encoder), then Experiments (three cold-starts + ECE). Find the passages yourself.

## After you finish

Return only `inter_rater_coding_sample_BLIND_EMPTY_v1.4_DaoMT.csv`. Do not compute \(\kappa\).
