# DyGKT / ASSIST17 REPRODUCTION MANIFEST

**Evidence class:** `REPRODUCED` (CASE A — artifacts present)  
**Date:** 2026-09-15  
**Does not change:** manuscript-reported ECE \(0/37\).

| Item | Value |
|---|---|
| Author repository URL | https://github.com/PengLinzhi/DyGKT |
| Exact commit | `88e364881397e3dcfd266c387e8bcde666ab06cc` |
| Local clone | `09_benchmark/path_a_ece/upstream_DyGKT/` |
| Dataset name/version | `assist17` (bundled `processed_data/assist17/`: `ml_assist17.csv`, `.npy` node/skill features) |
| Preprocessing | Author DataLoader defaults (no survey reprocessing) |
| Split | Author time-ordered link classification: `val_ratio=0.1`, `test_ratio=0.1` |
| Seed | 0 (`--num_runs 1` → `DyGKT_seed0`) |
| Checkpoint | `upstream_DyGKT/saved_models/DyGKT/assist17/DyGKT_seed0/DyGKT_seed0.pkl` |
| Hyperparameters | `--model_name DyGKT --num_neighbors 100`; epochs default 100, early-stop patience 10 |
| Prediction file | `09_benchmark/path_a_ece/results/dygkt_assist17_test_probs.npz` |
| Number of predictions \(n\) | 94156 (transductive **test** edges) |
| ECE implementation | `09_benchmark/path_a_ece/compute_ece.py` equal-width bins |
| \(M\) | 10 |
| Per-bin table | `supplementary/dygkt_assist17_ece_bins.csv` |
| ECE | 0.0361 |
| Brier | 0.1770 |
| Author-metric test AUC | 0.8025 (also AP 0.7178) |
| Environment | torch 2.11.0+cu128 (RUN_LOG) |
| Train command | `python train_link_classification.py --dataset_name assist17 --model_name DyGKT --num_neighbors 100 --num_runs 1 --gpu 0` |
| Eval + dump | same flags with `SURVEY_ECE_DUMP=1` |
| Run log | `09_benchmark/path_a_ece/results/RUN_LOG_DyGKT_assist17.md` |
| JSON summary | `09_benchmark/path_a_ece/results/dygkt_assist17_ece.json` |
| Protocol | `09_benchmark/path_a_ece/PROTOCOL_REPRODUCED_ECE_DyGKT_v0.1.md` |

## Transductive test edges

Author DyGKT evaluates link classification on chronological splits. Probabilities dumped for the **transductive test** pass only (`SURVEY_ECE_SPLIT=test`): edges among nodes already seen in the graph construction pathway of the author code, not a zero-exposure KC hold-out. \(n=94156\) is the count of those test edges with \((\hat p, y)\) pairs used for ECE/Brier.

## Scope limits (must stay in manuscript)

Single model (DyGKT), single dataset (ASSIST17), single seed (0). Not a benchmark league table. Does not establish corpus-wide calibration.
