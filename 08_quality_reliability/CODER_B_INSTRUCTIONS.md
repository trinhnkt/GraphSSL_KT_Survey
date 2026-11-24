# Coder B — locator-assisted double-code (20 papers)

**Superseded for independent-blind B.** This file allows a locator pack. For a new human B with no locator, use `CODER_B_INDEPENDENT_INSTRUCTIONS_v1.4.md` and `inter_rater_coding_sample_BLIND_EMPTY_v1.4.csv`.

Read this before opening any coder-A file.

## Rule

You code from the **PDF** in `14_references/` and the locked codebook (`00_protocol/coding_codebook_v1.0_LOCKED.md`, `SCOPE_v1.0_LOCKED.md` §5). Do **not** look at `inter_rater_coderA_locked_v1.0.csv` or the manuscript tables until adjudication.

Fill only `08_quality_reliability/inter_rater_coding_sample_BLIND_EMPTY_v1.3.csv`.

Do **not** open `inter_rater_coding_sample_BLIND_EMPTY_v1.2.csv` or `inter_rater_coding_sample_BLIND_v1.0.csv` (AI-filled, not human B).

AI may fetch PDF quotes (`CODER_B_AI_ASSIST_RULES_v1.0.md`). You still assign every code.

Do **not** use `inter_rater_coding_sample_v1.0.csv` while coding: its `why_included` column leaks Coder A. Work pack (PDF map, tokens, rules): `CODER_B_WORKPACK.md`. Locator quotes (no codes): `CODER_B_LOCATOR_PACK_v1.1.md`.

## Sample

20 primary-core papers, coverage-stratified (not simple random). See the `stratum` column. All 9 S=Y papers and all 5 H1 S=N papers are included so the S-criterion can be checked.

## Fields

| Column | Allowed values |
|---|---|
| `coderB_S_criterion` | `Y` or `N`. Y only if a self-generated pretext/consistency target exists (SCOPE §5). Inductive, LLM graph, curriculum, RL, or denoising alone is **N**. |
| `coderB_ssl_family` | Locked exclusive token if Y: `MULTIVIEW_CONTRASTIVE` / `GRAPH_CONTRASTIVE` / `GRAPH_RECONSTRUCTION` / `SEQUENCE_CONTRASTIVE`. If N: `NONE`. |
| `coderB_graph_provenance` | `MODEL_DEFINED_FIXED` / `EXTERNAL_FIXED` / `DYNAMIC_LEARNED` / `NA` (sequence-only). |
| `coderB_gnn_encoder` | Codebook encoder or `NONE`. |
| `coderB_strict_kc_cold_start` | `YES` only for a zero-exposure KC hold-out. Interaction-drop ≠ YES. |
| `coderB_item_cold_start` | `YES` / `NO` |
| `coderB_learner_cold_start` | `YES` / `NO` |
| `coderB_ece_reported` | `YES` only if the manuscript reports Expected Calibration Error. |

Add `coderB_locator` (page/section) and `coderB_note` (one sentence).

## After you finish

Return the CSV. A third person (or the team after lock) compares to coder A and computes \(\kappa\). Do not compute \(\kappa\) yourself on a sheet that already contains coder A.
