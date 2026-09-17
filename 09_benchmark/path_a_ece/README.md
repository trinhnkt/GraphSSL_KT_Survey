# Path A — Reproduced ECE (DyGKT / KT038)

**Status:** scaffold ready; train + ECE numbers **not yet run**.  
**Target lift:** ~8.0 → ~8.5 (one REPRODUCED calibration overlay).

## Layout

| Path | Role |
|---|---|
| `PROTOCOL_REPRODUCED_ECE_DyGKT_v0.1.md` | Locked run recipe |
| `compute_ece.py` | Equal-width ECE (\(M=10\)) + Brier from dumped probs |
| `upstream_DyGKT/` | Author repo clone (`PengLinzhi/DyGKT`) + survey dump hook |
| `results/` | NPZ + JSON outputs (gitignored contents) |

## Quick start (after GPU env ready)

```powershell
cd D:\TRINH\GraphSSL_KT_Survey\09_benchmark\path_a_ece\upstream_DyGKT

# Smoke (plumbing only — not manuscript-grade)
python train_link_classification.py --dataset_name assist17 --model_name DyGKT --num_neighbors 100 --num_runs 1 --num_epochs 2 --gpu 0

# Official Path A (early-stopping; prefer GPU)
python train_link_classification.py --dataset_name assist17 --model_name DyGKT --num_neighbors 100 --num_runs 1 --gpu 0

$env:SURVEY_ECE_DUMP = "1"
$env:SURVEY_ECE_OUT = "..\results\dygkt_assist17_test_probs.npz"
python evaluate_link_classification.py --dataset_name assist17 --model_name DyGKT --num_neighbors 100 --num_runs 1 --gpu 0

cd ..
python compute_ece.py --probs-file results\dygkt_assist17_test_probs.npz
```

Note: upstream README typo `--num_neighbor` → correct flag is `--num_neighbors`.

## Manuscript rule

- Report as **survey-computed / REPRODUCED** ECE on DyGKT–assist17.
- Keep locked claim: **0/37 manuscripts report ECE**.
- Do not mix into pyKT-ColdStart or cross-paper AUC tables.
