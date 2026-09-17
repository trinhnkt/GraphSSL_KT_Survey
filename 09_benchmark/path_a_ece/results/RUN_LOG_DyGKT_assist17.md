# RUN LOG — DyGKT / assist17 ECE (Path A)

## A. Smoke plumbing (NOT for manuscript)

| Field | Value |
|---|---|
| Date | 2026-09-14 |
| Config | `--num_epochs 2 --num_runs 1` |
| Test AUC | 0.7292 |
| ECE \(M=10\) | 0.0627 (SMOKE only) |
| Note | Plumbing only. **Do not cite.** |

## B. Official Path A (manuscript-grade) — DONE

| Field | Value |
|---|---|
| Date | 2026-09-14 |
| Status | **COMPLETE** |
| upstream commit SHA | `88e364881397e3dcfd266c387e8bcde666ab06cc` |
| torch / CUDA | torch 2.11.0+cu128 |
| Train wall time | 4400 s (~73 min); ran to epoch 65 then early-stop / final reload |
| Command train | `python train_link_classification.py --dataset_name assist17 --model_name DyGKT --num_neighbors 100 --num_runs 1 --gpu 0` |
| Command eval | same flags + `SURVEY_ECE_DUMP=1` |
| Test AUC | **0.8025** |
| Test AP | **0.7178** |
| New-node test AUC | 0.8035 |
| ECE \(M=10\) equal-width | **0.0361** |
| Brier | **0.1770** |
| n test edges | 94156 |
| Artifacts | `results/dygkt_assist17_test_probs.npz`, `results/dygkt_assist17_ece.json` |
| Deviations | none vs protocol v0.1 (seed 0, assist17, author code) |

Evidence class: `REPRODUCED`. Does **not** change locked corpus claim `0/37` manuscripts report ECE.
