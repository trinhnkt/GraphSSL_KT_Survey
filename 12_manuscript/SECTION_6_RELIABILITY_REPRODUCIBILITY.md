# Section 6: Reliability, Reproducibility & Calibration Audit (RQ5)

## 6.1 Quality Assessment (QA1–QA8) Synthesis

We systematic audited all 42 primary core studies across eight quality criteria (QA1–QA8):

- **QA1 Task Clarity (Mean: 1.95 / 2.00)**: Excellent problem formulation across all studies.
- **QA2 Data Transparency (Mean: 1.90 / 2.00)**: 92.9% of studies evaluate on public benchmark datasets (ASSISTments, EdNet, Statics, Junyi).
- **QA3 Split Control (Mean: 1.76 / 2.00)**: Most studies clearly describe 80/20 train/test splits, though graph precomputation leakage risk remains unaddressed in 28.6% of papers.
- **QA4 Baseline Adequacy (Mean: 1.90 / 2.00)**: Strong baseline comparisons against classic (DKT, DKVMN) and modern (AKT, CL4KT) models.
- **QA5 Statistical Rigor (Mean: 1.10 / 2.00)**: Significant gap: while 100% of studies report multi-run mean AUC across 5 seeds, **less than 15% perform formal significance testing (t-test / Wilcoxon)** or report confidence intervals.
- **QA6 Reproducibility Artifacts (Mean: 1.45 / 2.00)**: 16 out of 42 studies (38.1%) provide official open-source code repositories verified in pyKT benchmarks.
- **QA7 Sparse Construct Validity (Mean: 1.05 / 2.00)**: Major weakness: 95.2% fail to evaluate strict zero-exposure KC cold-start splits despite making data sparsity claims.
- **QA8 Computational Transparency (Mean: 1.38 / 2.00)**: Only 42.9% of studies report empirical training times, GPU memory consumption, or formal asymptotic time complexity bounds.

---

## 6.2 Data Split Resampling & Seed Repetition (CB13)

Under codebook rule `CB13`, we differentiate model seed repetition (`n_seeds`) from dataset split resampling (`resampling_repeats`):
- 40 out of 42 studies repeat model training over 5 random seeds using a *single fixed train/test split* (`resampling_repeats = 1`).
- Only 2 studies perform 5-fold cross-validation or multiple independent data split resamplongs (`resampling_repeats > 1`). This indicates that reported AUC standard deviations reflect model initialization variance rather than data partition variance.

---

## 6.3 Predictive Accuracy vs Model Calibration

While all 42 core studies report ROC-AUC and Accuracy metrics, **0 out of 42 primary core studies report Expected Calibration Error (ECE) or reliability diagrams**. In intelligent tutoring systems, overconfident or poorly calibrated probability outputs can lead to inappropriate exercise recommendations. Incorporating probability calibration metrics represents an urgent necessity for trustworthy AI in education.
