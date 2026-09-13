# Benchmark Evidence Audit & Decision Report
**Survey Protocol Version:** v1.0 LOCKED  
**Audit Target:** `09_benchmark/`, `10_analysis/`, and `12_manuscript/TLT/manuscript_TLT_WORKING_v0.1.tex`  
**Date:** 2026-09-12  

---

## 1. Executive Summary

This audit evaluates the evidence completeness of the empirical benchmark reported in Table 5 (`tab:empirical_validation`) of the working draft. Per protocol rules and Task A9 instructions, all quantitative empirical claims in the systematic review must be grounded in primary source verification or fully reproducible raw execution logs.

---

## 2. Artifact Checklist Audit

| Required Artifact | Availability | Location / Status | Evidence Assessment |
| :--- | :---: | :--- | :--- |
| **Benchmark Specification** | **PRESENT** | `09_benchmark/SPARSE_KT_BENCHMARK_SPECIFICATION_v1.0.md` | Proposed specification document only |
| **Dataset / Version Manifest** | **MISSING** | None | No raw dataset or version hash archived |
| **Preprocessing Pipeline** | **MISSING** | None | No transformation scripts for cold-start splits |
| **Exact Train/Val/Test Splits**| **MISSING** | None | No split index masks or KC split lists |
| **Cold-KC ID Lists** | **MISSING** | None | No explicit list of 22 held-out KCs |
| **Model Commit / PyTorch Code**| **MISSING** | None | No runnable baseline model code in repo |
| **Hyperparameter Configs** | **MISSING** | None | No YAML/JSON configs for LR, batch size, etc. |
| **Random Seeds & Iteration Logs**| **MISSING** | None | No multi-seed stdout/stderr execution logs |
| **Prediction Tensors / Arrays** | **MISSING** | None | No ground truth or prediction logits files |
| **Per-Seed Metric Logs** | **MISSING** | None | Only single mean values printed in text report |
| **ECE Confidence Bin Outputs** | **MISSING** | None | No calibration curve arrays or bin counts |
| **Statistical Test Outputs** | **MISSING** | None | No raw p-value computation output files |
| **GPU / Hardware Manifest** | **MISSING** | None | No VRAM consumption or hardware run logs |

---

## 3. Explicit Decision

### **DECISION: REMOVE**

**Rationale:**  
The repository contains the benchmark specification (`09_benchmark/SPARSE_KT_BENCHMARK_SPECIFICATION_v1.0.md`), but lacks raw execution logs, per-seed prediction arrays, data split manifests, and PyTorch reference implementations. Pursuant to Task A9 rules and protocol rules 1 & 4 (*Do not fabricate statistics; do not reconstruct experiments from numbers already printed in the draft*), exact empirical benchmark numbers ($0.7432$, $0.7685$, $0.7850$, $0.7920$, ECE values, standard deviations, and Wilcoxon $p$-values) must be **REMOVED** from the working draft.

---

## 4. Remediation Actions Executed on Working Manuscript

1. **Table Removal**: Removed Table 5 (`tab:empirical_validation`) containing unverified empirical benchmark numbers from `manuscript_TLT_WORKING_v0.1.tex`.
2. **Text Claim Removal**: Removed all hardcoded AUC ($0.7432, 0.7685, 0.7850, 0.7920, 0.5120, 0.7185$), ECE, $\pm$ SD, and $p < 0.01$ claims from Section 5.
3. **Methodological Reframing**: Reframed the cold-start discussion around the methodological finding from our primary core literature synthesis ($N=37$): 94.6% of studies evaluate exclusively on generic interaction data sparsity, whereas strict zero-exposure concept cold-start evaluation requires external knowledge graph priors or LLM-derived semantic representations.
4. **Research Agenda Integration**: Kept the benchmark framework as a key future research agenda proposal (*pyKT-ColdStart* benchmark suite in Section 7 / Agenda Pillar 4).

---
*End of Benchmark Evidence Audit Report.*
