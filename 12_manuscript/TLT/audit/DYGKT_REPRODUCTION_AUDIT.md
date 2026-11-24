# DyGKT reproduction audit — 2026-09-15

## Decision: **CASE A — keep REPRODUCED**

| Checklist item | Status | Locator |
|---|---|---|
| Author repo URL | PASS | https://github.com/PengLinzhi/DyGKT |
| Commit hash | PASS | `88e364881397e3dcfd266c387e8bcde666ab06cc` |
| Dataset / split / seed | PASS | assist17; val/test 0.1; seed 0 |
| Checkpoint present | PASS | `saved_models/DyGKT/assist17/DyGKT_seed0/` |
| Prediction NPZ | PASS | `results/dygkt_assist17_test_probs.npz` |
| ECE JSON + bins | PASS | `dygkt_assist17_ece.json`; exported `supplementary/dygkt_assist17_ece_bins.csv` |
| Brier / AUC | PASS | 0.1770 / 0.8025 (RUN_LOG) |
| Run log / commands | PASS | `RUN_LOG_DyGKT_assist17.md` |
| Transductive test edges explained | PASS | Manifest § Transductive test edges |
| Not treated as corpus benchmark | PASS | Manuscript wording constraint |

## Numbers retained in main text

ECE 0.0361; Brier 0.1770; AUC 0.8025; \(n=94156\); \(M=10\); seed 0 — all match JSON/RUN_LOG.

## Non-claims

- Does not change \(0/37\) manuscript ECE reporting.
- Does not flip T3 GO/NO-GO for the corpus.
- Single model / dataset / seed only.
