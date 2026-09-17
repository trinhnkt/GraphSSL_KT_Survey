# PROTOCOL — Reproduced ECE on DyGKT (KT038) v0.1

**Status:** DRAFT scaffold (not yet executed).  
**Evidence class:** `REPRODUCED`  
**Date opened:** 2026-09-14  
**Paper:** KT038 — DyGKT: Dynamic Graph Learning for Knowledge Tracing (KDD 2024)  
**Author code:** https://github.com/PengLinzhi/DyGKT (local: `upstream_DyGKT/`)

---

## 1. Goal

Produce one survey-computed Expected Calibration Error (ECE) on the author DyGKT implementation for ASSIST17, to support the TLT learning-evidence gate (~8.5 audit lift).

This run does **not**:

- change the locked corpus count that **0/37 manuscripts report ECE**;
- license tutoring GO on T3 for the whole corpus;
- create a cross-paper AUC/ECE league table.

---

## 2. Fixed configuration

| Item | Value |
|---|---|
| Model | `DyGKT` |
| Dataset | `assist17` (bundled under `processed_data/assist17/`) |
| Split | author code defaults: `val_ratio=0.1`, `test_ratio=0.1` (time-ordered link classification) |
| Neighbors | `--num_neighbors 100` (README example; flag name corrected) |
| Runs for Path A | **1** seed (`--num_runs 1`, seed 0) for the primary ECE row; optional +4 later |
| Epochs | default 100 with early stopping `patience=10` |
| Probabilities | sigmoid outputs on the **transductive test** edges |
| ECE | equal-width, \(M=10\), bins \(((m-1)/M, m/M]\) |
| Secondary | Brier score on the same \((\hat p, y)\) |

Smoke plumbing (not for manuscript numbers): `--num_epochs 2 --num_runs 1`.

---

## 3. Environment

- Python 3.9+ recommended  
- PyTorch (author cites 1.8.1; newer CUDA builds OK if API-compatible)  
- `numpy`, `pandas`, `tqdm`, `tabulate`, `scikit-learn`  
- GPU preferred (`--gpu 0`); CPU allowed for smoke only  

Upstream lives at `09_benchmark/path_a_ece/upstream_DyGKT/`. Re-clone if missing:

```text
git clone --depth 1 https://github.com/PengLinzhi/DyGKT.git upstream_DyGKT
```

Survey dump hook (already applied in this workspace):

- `evaluate_models_utils.py` writes NPZ when `SURVEY_ECE_DUMP=1` and `SURVEY_ECE_SPLIT` is set.
- `evaluate_link_classification.py` sets `SURVEY_ECE_SPLIT=test` only around the transductive test pass.

---

## 4. Execution steps

### 4.1 Train

```powershell
cd upstream_DyGKT
python train_link_classification.py --dataset_name assist17 --model_name DyGKT --num_neighbors 100 --num_runs 1 --gpu 0
```

Checkpoint path pattern:

```text
./saved_models/DyGKT/assist17/DyGKT_seed0/DyGKT_seed0.pkl
```

### 4.2 Evaluate + dump probabilities

```powershell
$env:SURVEY_ECE_DUMP = "1"
$env:SURVEY_ECE_OUT = (Resolve-Path ..\results).Path + "\dygkt_assist17_test_probs.npz"
python evaluate_link_classification.py --dataset_name assist17 --model_name DyGKT --num_neighbors 100 --num_runs 1 --gpu 0
```

Expect console: `[SURVEY_ECE_DUMP] wrote ... n=... split=test`.

### 4.3 Compute ECE

```powershell
cd ..
python compute_ece.py --probs-file results\dygkt_assist17_test_probs.npz --out-json results\dygkt_assist17_ece.json
```

### 4.4 Record run metadata

Fill `results/RUN_LOG_DyGKT_assist17.md` with:

- git commit SHA of `upstream_DyGKT`
- torch / CUDA versions
- wall time
- test AUC / AP from evaluate logs (author metrics)
- ECE / Brier from JSON
- any deviation from this protocol → also note in `00_protocol/protocol_deviations.md` if manuscript wording changes

---

## 5. Manuscript insertion rule (after numbers exist)

Add **one** supplementary table / short paragraph:

> Survey-computed equal-width ECE (\(M=10\)) on DyGKT / ASSIST17 (author code, seed 0, REPRODUCED) = \<value\>. Corpus manuscript-reported ECE remains \(0/37\).

T3 checklist stays **NO-GO** for corpus-wide \(P(r=1)\) action; the reproduced row only shows calibration **can** be measured.

---

## 6. Acceptance checklist

- [ ] Train completed; checkpoint present  
- [ ] NPZ dump for **test** split only  
- [ ] `dygkt_assist17_ece.json` written with `evidence_source_type=REPRODUCED`  
- [ ] RUN_LOG filled  
- [ ] Manuscript / supplementary updated without altering \(0/37\)  
- [ ] Changelog entry (e.g. v1.6.14)  

---

## 7. Non-goals

- Full 5-seed paper replication  
- Zero-exposure KC split (Path B)  
- Coda / SINKT until DyGKT ECE lands  
- Temperature scaling fit unless explicitly added as a second REPRODUCED experiment  
