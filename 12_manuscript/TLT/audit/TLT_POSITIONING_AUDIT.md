# IEEE Transactions on Learning Technologies (IEEE TLT) Positioning Audit
**Survey Protocol Version:** v1.0 LOCKED  
**Audit Target:** `12_manuscript/TLT/manuscript_TLT_WORKING_v0.1.tex`  
**Date:** 2026-09-12  

---

## 1. Executive Summary

This audit documents the systematic reframing of the manuscript for publication in **IEEE Transactions on Learning Technologies (IEEE TLT)**. While maintaining full mathematical and architectural rigor regarding Graph Neural Networks (GNNs) and Self-Supervised Learning (SSL), the manuscript is reframed to emphasize core educational technology, educational data mining (EDM), and intelligent tutoring systems (ITS) challenges.

---

## 2. Reframed Scope & Educational Technology Concepts

The manuscript explicitly positions Graph-SSL Knowledge Tracing across seven core learning technology dimensions:
1. **Intelligent Tutoring Systems (ITS)**: Dynamic mastery estimation to support automated step-based tutoring and scaffolding.
2. **Adaptive Learning**: Real-time recommendation of exercises based on latent concept mastery boundaries.
3. **Personalized Learning Pathways**: Customizing learning trajectories for high-variance student cohorts.
4. **Learner-State Estimation**: Representing student proficiency as continuous vector embeddings over prerequisite skill topologies.
5. **Curriculum Adaptation**: Managing course onboarding when new concepts/items are added to learning platforms.
6. **Educational Data Mining (EDM)**: Discovering structural co-occurrence and prerequisite relationships from student interaction logs.
7. **Trustworthy Mastery Prediction**: Ensuring calibrated, non-leaky, and reproducible model outputs before deployment in high-stakes assessment settings.

---

## 3. Revised Graph-KT Definition

Per survey protocol guidelines and protocol rule 10, the definition of Graph-Based Knowledge Tracing (Graph-KT) is revised to accommodate explicit structural graphs beyond GNN message passing:

> **Revised Graph-KT Definition**: Knowledge Tracing models that incorporate explicit graphs or graph-structured relations (e.g., concept prerequisite trees, question-KC bipartite structures, dynamic interaction graphs, relational paths, or hyperbolic skill manifolds) as a **central structural mechanism**, including but not limited to Graph Neural Network (GNN) message passing.

---

## 4. Unsupported Claims Audit & Removal

All unsupported "first systematic survey" assertions have been systematically audited and rephrased across the manuscript:

| Section | Original Phrasing | Revised IEEE TLT Phrasing | Rationale |
| :--- | :--- | :--- | :--- |
| **1.3 (Intro)** | "...our work provides the first systematic survey dedicated specifically to..." | "...our work provides a dedicated, PRISMA 2020-compliant systematic survey focusing specifically on..." | Avoids absolute primacy claims while highlighting PRISMA rigor. |
| **7 (Conclusion)** | "This systematic survey has provided the first PRISMA 2020--compliant synthesis..." | "This systematic survey provides a comprehensive PRISMA 2020--compliant synthesis..." | Focuses on methodological compliance and scope rather than unverified priority. |

---

## 5. Prior-Survey Positioning Matrix

The prior literature comparison has been rebuilt to explicitly compare four primary categories of review and benchmark works across seven rigorous audit dimensions:

| Audit Dimension | Broad KT Surveys<br>*(Abdelrahman et al., 2023)* | Deep-KT Benchmark Suites<br>*(Liu et al. pyKT, 2022/2025)* | Dedicated Graph-KT Reviews<br>*(Wang et al., 2024)* | **This Systematic Survey**<br>*(Ours, 2026)* |
| :--- | :--- | :--- | :--- | :--- |
| **1. Systematic Protocol** | Narrative / Semi-systematic | Empirical benchmark code | Qualitative literature review | **Full PRISMA 2020 (7 databases, $N=2,017$)** |
| **2. Graph Coverage** | High-level GNN overview | Standard sequence baselines | GNN-focused taxonomy | **4-family Graph Provenance & 5-family GNN Encoder** |
| **3. SSL Pretext Coverage** | Minimal / None | Excluded | Minimal | **4-family SSL Pretext Taxonomy ($N_S=14$)** |
| **4. Sparse/Cold-Start Ontology** | Generic data sparsity | Standard interaction splits | Interaction sparsity focus | **Interaction Sparsity vs. Zero-Exposure Cold-Start** |
| **5. Graph Provenance Leakage** | Not audited | Not audited | Not audited | **Full Data-Leakage & Time-Split Audit** |
| **6. Calibration (ECE)** | Not evaluated | AUC / ACC only | Not evaluated | **Probability Calibration Audit (0/37 ECE reported)** |
| **7. Open Science & Reproducibility**| Citation indexing | Code repository | Paper taxonomy | **Field-Level Evidence & Full Open Science Audit** |

---

## 6. Learning-Technology Implication Sections Audit

Dedicated subsections titled `Learning-Technology Implications` have been introduced at the end of each core synthesis section (Sections 3--6) in `manuscript_TLT_WORKING_v0.1.tex`:

1. **Section 3.6 (`Learning-Technology Implications for Graph-KT`)**:  
   - Discusses how explicit concept prerequisite maps enhance pedagogical interpretability in ITS.
   - Highlights the critical operational risk of log-derived co-occurrence graphs causing data leakage and overestimating student readiness.

2. **Section 4.5 (`Learning-Technology Implications for SSL-KT`)**:  
   - Explains how self-supervised contrastive pre-training regularizes sparse interaction vectors in personalized learning platforms.
   - Emphasizes maintaining learning state stability when student interaction histories are short or fragmented.

3. **Section 5.4 (`Learning-Technology Implications for Sparse & Cold-Start KT`)**:  
   - Addresses real-world curriculum onboarding and content expansion.
   - Contrasts interaction sparsity with strict zero-exposure concept cold-start, proving that models evaluated under standard splits collapse when encountering brand-new curriculum modules.

4. **Section 6.5 (`Learning-Technology Implications for Trustworthy & Calibrated KT`)**:  
   - Establishes probability calibration (ECE / Brier score) as a prerequisite for trustworthy AI in education.
   - Warns that uncalibrated model probabilities lead to miscalibrated scaffolding, overconfident remediation, and degraded learner trust.

---
*End of TLT Positioning Audit.*
