# Coder B — independent double-code (no locator)

Read this before opening any other file in `08_quality_reliability/`.

## Rule

You code from the **PDF** in `14_references/` and the locked codebook (`00_protocol/coding_codebook_v1.0_LOCKED.md`, `00_protocol/SCOPE_v1.0_LOCKED.md` §4–§6).

Fill only `08_quality_reliability/inter_rater_coding_sample_BLIND_EMPTY_v1.4.csv`.

Do **not** use a locator pack, quote list, or AI to fetch passages or suggest tokens.

Do **not** open Coder A, manuscript tables, `BLIND_EMPTY_v1.3*.csv`, `BLIND_v1.0.csv`, or `CODER_B_LOCATOR_PACK_*.md`.

If you have already seen those files, stop. You are not eligible for this pass.

## Sample

20 primary-core papers (same IDs as the locked coding sample). Coverage-stratified, not simple random.

## Fields

| Column | Allowed values |
|---|---|
| `coderB_S_criterion` | `Y` or `N`. Y only if a self-generated pretext/consistency target exists (SCOPE §5). Inductive, LLM graph, curriculum, RL, or denoising alone is **N**. |
| `coderB_ssl_family` | If Y, one exclusive token: `MULTIVIEW_CONTRASTIVE` / `GRAPH_CONTRASTIVE` / `GRAPH_RECONSTRUCTION` / `SEQUENCE_CONTRASTIVE`. If N: `NONE`. |
| `coderB_graph_provenance` | `MODEL_DEFINED_FIXED` / `EXTERNAL_FIXED` / `DYNAMIC_LEARNED` / `NA` (sequence-only). |
| `coderB_gnn_encoder` | Codebook encoder or `NONE`. |
| `coderB_strict_kc_cold_start` | `YES` only for a zero-exposure KC hold-out. Interaction-drop ≠ YES. |
| `coderB_item_cold_start` | `YES` / `NO` |
| `coderB_learner_cold_start` | `YES` / `NO` |
| `coderB_ece_reported` | `YES` only if the manuscript reports Expected Calibration Error. |

Write `coderB_locator` (page/section you used) and `coderB_note` (one sentence from that PDF).

`coderB_id` = your name or initials, same on every row. Do not use `NguyenKT`.

## After you finish

Return only the v1.4 CSV. Do not compute \(\kappa\). Do not look at Coder A.
