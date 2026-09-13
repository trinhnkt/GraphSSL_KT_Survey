# IEEE TLT Manuscript Restructuring Audit
**Survey Protocol Version:** v1.0 LOCKED  
**Audit Target:** `12_manuscript/TLT/manuscript_TLT_STRUCTURE_v0.1.tex`  
**Date:** 2026-09-12  

---

## 1. Executive Summary

This audit verifies that the manuscript has been systematically restructured into `manuscript_TLT_STRUCTURE_v0.1.tex` to strictly match the requested section order and educational technology positioning for **IEEE Transactions on Learning Technologies (IEEE TLT)**.

---

## 2. Section Mapping & Structural Audit Matrix

| Section # | Section Title in `manuscript_TLT_STRUCTURE_v0.1.tex` | Checklist Requirements Covered | Audit Verification Status |
| :---: | :--- | :--- | :---: |
| **1** | **Introduction** | Learning-technology motivation (ITS/EDM/adaptive learning), Scope & gateway criteria ($\text{PRIMARY\_CORE} = \text{KT} \land (\text{GRAPH} \lor \text{SSL})$), Prior-survey positioning (Table 2), Main contributions. | **VERIFIED** |
| **2** | **Systematic Review Methodology and PRISMA Protocol** | Protocol & 6 RQs, 7-database search ($N=2,017$), PRISMA 2020 screening flow ($N=37$), Field-level coding scheme, QA1-QA8 framework, Evidence synthesis strategy. | **VERIFIED** |
| **3** | **Taxonomy and Synthesis of Graph-Based Knowledge Tracing** | Graph provenance (4 channels), GNN encoders (5 families, Table 1), Temporal integration & fusion, Methodological risk (Log-derived data leakage), Learning-technology implications. | **VERIFIED** |
| **4** | **Taxonomy and Synthesis of Self-Supervised Knowledge Tracing** | SSL objective taxonomy (4 families, Table 2), Augmentation strategies & perturbations, Structure preservation, Graph+SSL intersection ($N_{G \cap S}=8$), Learning-technology implications. | **VERIFIED** |
| **5** | **Sparse-Concept \& Cold-Start Evaluation Protocols** | Sparsity & cold-start ontology, Generic interaction sparsity vs zero-exposure KC cold-start (Table 3), External side information, Evaluation split vulnerabilities audit, Learning-technology implications. | **VERIFIED** |
| **6** | **Reliability, Reproducibility \& Calibration Audit** | QA assessment summary (HIGH 78.4%, MODERATE 21.6%), Computational complexity bounds, Probability calibration audit (0/37 ECE reported), Learning-technology implications. | **VERIFIED** |
| **7** | **Discussion** | Synthesis of Graph-KT contributions, Synthesis of SSL-KT contributions, Architectural mechanisms under cold-start, Learning-technology operational guidelines, Limitations. | **VERIFIED** |
| **8** | **Evidence-Derived Research Agenda** | Six mathematically formalized pillars: LLM-GNN fusion, Non-Euclidean hyperbolic manifolds, *pyKT-ColdStart* benchmark suite, Trustworthy calibrated KT, Continuous-time Neural ODEs, Causal counterfactual graph debiasing. | **VERIFIED** |
| **9** | **Threats to Validity** | Internal validity (search, selection bias, coding reliability), External validity (dataset generalizability, temporal scope, metric limits). | **VERIFIED** |
| **10** | **Conclusion** | Final synthesis of core findings and research agenda vision. (Draft state maintained for final A15 lock). | **VERIFIED** |

---

## 3. Compliance & Output Verification

- **Page Count**: 11 double-column IEEE pages (strictly within the $\le 18$-page boundary).
- **Compilation Status**: `manuscript_TLT_STRUCTURE_v0.1.pdf` compiled cleanly with 0 errors and 0 undefined references.
- **Reference Resolution**: All 43 in-text citations map 1:1 to verified publisher records in `references.bib`.

---
*End of TLT Structure Audit Report.*
