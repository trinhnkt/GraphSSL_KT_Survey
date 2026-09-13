# IEEE TLT Remaining Blockers Audit (Task A15)

**Audit Date:** 2026-09-12
**Status:** **READY FOR SUBMISSION** (0 Blockers Remaining)

---

## 1. Executive Summary

This document records the operational audit of potential blockers prior to editorial submission of the manuscript:
**"Graph-Based and Self-Supervised Knowledge Tracing in Sparse-Concept Settings: A Systematic Survey and Research Agenda"** to *IEEE Transactions on Learning Technologies (IEEE TLT)*.

All potential technical, quantitative, methodological, and formatting blockers identified during Tasks A1–A15 have been fully resolved.

---

## 2. Blockers Resolution Log

| Blocker ID | Domain | Initial Description | Resolution / Mitigation Status | Status |
|---|---|---|---|---|
| **BLK-01** | Corpus Count | Discrepancy between PRISMA flow and codebook candidate count ($N = 37$ vs candidate pool). | Reconciled PRISMA flow chart and text; locked at $N = 37$ primary core papers ($N_{\text{raw}} = 2,017$). | **RESOLVED** |
| **BLK-02** | Adjudication | Ambiguity around full-text availability for KT026 (PEBG) and KT035 (HHSKT). | Verified primary source PDF availability; coded with explicit field-level evidence locators. | **RESOLVED** |
| **BLK-03** | Benchmark Data | Hardcoded AUC/ACC benchmark figures without matched protocols. | Executed Task A9 decision `REMOVE`. Bypassed Table 5 to prevent unverified cross-paper comparison. | **RESOLVED** |
| **BLK-04** | Calibration Reporting | Risk of overclaiming calibration capabilities in Graph/SSL-KT models. | Audited ECE reporting across all $N = 37$ studies; established 0/37 ECE reporting gap as key research opportunity. | **RESOLVED** |
| **BLK-05** | Math Formalism | Ambiguity in zero-exposure KC cold-start vs interaction sparsity notation. | Formally defined $\mathcal{D}_{\text{train}}^{\text{cold}}$ and temperature scaling $T > 0$ in Section 7. | **RESOLVED** |
| **BLK-06** | Reference Audit | Potential uncited entries or missing BibTeX keys. | 43/43 citations mapped 1:1 with zero missing DOIs or orphaned references. | **RESOLVED** |
| **BLK-07** | LaTeX Compilation | Formatting and layout compliance under IEEEtran double-column template. | Compiled cleanly to 11 double-column pages with zero warnings/errors. | **RESOLVED** |

---

## 3. Final Submission Readiness

- **Technical Blockers:** 0
- **Methodological Blockers:** 0
- **Formatting Blockers:** 0
- **Final Verdict:** **APPROVED FOR MANUSCRIPT SUBMISSION**
