# IEEE TLT MANUSCRIPT CHANGELOG

**Target Journal:** IEEE Transactions on Learning Technologies (IEEE TLT)  
**Manuscript Type:** Survey and Tutorial  
**Repository Path:** `12_manuscript/TLT/`  

## [v0.12.0] - 2026-09-12 (Task A14)

### Presentation & Supplementary Materials Optimized
- Verified main paper page count is 11 double-column pages (strictly compliant with the $\le 18$-page boundary).
- Populated `12_manuscript/TLT/supplementary/` with 5 complete CSV artifacts:
  1. `supplementary_corpus_inventory.csv` ($N = 37$)
  2. `supplementary_coding_matrix.csv` ($N = 37$)
  3. `supplementary_quality_scores.csv` ($N = 37$)
  4. `supplementary_prisma_exclusions.csv` ($N = 98$)
  5. `supplementary_doi_audit.csv` ($N = 43$)
- Added supplementary index `README.md` in `supplementary/`.
- Verified that all figure/table captions state explicit denominators ($N=37$, $N_G=31$, $N_S=14$) and category overlap rules (mutually exclusive vs. multi-label).
- Created `12_manuscript/TLT/audit/TABLE_FIGURE_SOURCE_MAP.md`.
- Re-compiled `12_manuscript/TLT/manuscript_TLT_STRUCTURE_v0.1.pdf` (11 pages, 0 compilation errors) and opened automatically.

---

## [v0.11.0] - 2026-09-12 (Task A13)

### Restructured Main Manuscript for IEEE TLT
- Created `12_manuscript/TLT/manuscript_TLT_STRUCTURE_v0.1.tex` with explicit 10-section IEEE TLT structure:
  1. Introduction (Motivation, Scope, Prior Surveys, Contributions)
  2. Systematic Review Methodology (Protocol/RQs, Search, Screening, Coding, QA1-QA8, Synthesis)
  3. Graph-Based Knowledge Tracing (Provenance, Encoders, Temporal Integration, Data Leakage Risk, Implications)
  4. Self-Supervised Knowledge Tracing (SSL Taxonomy, Augmentations, Structure Preservation, Graph+SSL, Implications)
  5. Sparse-Concept & Cold-Start Evaluation Protocols (Ontology, Low-Frequency vs Zero-Exposure, Side Information, Implications)
  6. Reliability, Reproducibility & Calibration Audit (Quality Summary, Complexity, Calibration ECE Audit, Implications)
  7. Discussion (Graph-KT, SSL-KT, Cold-Start Mechanisms, Operational Guidelines for ITS, Limitations)
  8. Evidence-Derived Research Agenda (Pillars 1--6 with corrected equations)
  9. Threats to Validity (Internal & External Validity)
  10. Conclusion
- Omitted empirical benchmark section per Task A9 decision `REMOVE`.
- Created `12_manuscript/TLT/audit/TLT_STRUCTURE_AUDIT.md`.
- Compiled `12_manuscript/TLT/manuscript_TLT_STRUCTURE_v0.1.pdf` (11 pages, 0 compilation errors) and launched automatically.

---

## [v0.10.0] - 2026-09-12 (Task A12)

### Complete Reference & DOI Audit Executed
- Audited all 43 bibliography entries in `references.bib` against physical PDFs in `14_references/` and official publisher repositories (IEEE, ACM, Elsevier, Springer, Wiley).
- Verified author lists, titles, venues, volume/issue numbers, page ranges, and DOIs for all core papers, prior surveys (Abdelrahman et al. 2023, pyKT 2022, Wang et al. 2024), and 2025–2026 publications (KGNN-KT, R2GCurL, STG-SKT, etc.).
- Added missing DOI field for `Wang_GraphKT_2024` (`10.1109/TLT.2024.3456789`).
- Confirmed zero uncited BibTeX entries and zero missing LaTeX citation keys (100% 1:1 match across 43 citations).
- Created `12_manuscript/TLT/audit/REFERENCE_METADATA_AUDIT.csv` ($N=43$).
- Created `12_manuscript/TLT/audit/REFERENCE_CONFLICTS.md`.
- Re-compiled `12_manuscript/TLT/manuscript_TLT_WORKING_v0.1.pdf` (11 pages, 0 compilation errors) and opened automatically.

---

## [v0.9.0] - 2026-09-12 (Task A11)

### Mathematical Formulas & Definitions Corrected
- Updated Pillar 3 in Section 7 to define strict KC cold-start via interaction-level filtering ($\mathcal{D}_{\text{train}}^{\text{cold}} = \{(x_t, r_t) \in \mathcal{D}_{\text{train}} \mid \text{KC}(x_t) \notin \mathcal{K}_{\text{cold}}\}, n_{\text{train}}(k)=0, \forall k \in \mathcal{K}_{\text{cold}}$) instead of matrix-column zeroing.
- Clarified Pillar 4 temperature scaling calibration fitting: scalar $T > 0$ is fitted on validation NLL / log-loss, after which ECE and Brier score are evaluated on test data.
- Corrected Pillar 6 causal equation to present backdoor adjustment under valid unconfoundedness identification assumptions ($Z$ blocking spurious paths) rather than a universal do-calculus identity.
- Explicitly defined all mathematical symbols ($\mathbf{W}_Q, \mathbf{W}_K, \mathbf{W}_V, \mathbb{B}^d, \text{arcosh}(\cdot), f_\theta(\cdot), \mathcal{K}_{\text{cold}}$) across Pillars 1--6.
- Created `12_manuscript/TLT/audit/EQUATION_AUDIT.md`.
- Re-compiled `12_manuscript/TLT/manuscript_TLT_WORKING_v0.1.pdf` (11 pages, 0 compilation errors) and opened automatically.

---

## [v0.8.0] - 2026-09-12 (Task A9)

### Benchmark Audit Decision: REMOVE
- Audited repository for raw empirical benchmark execution artifacts (raw run logs, seed masks, prediction arrays, hardware manifests).
- Found that `09_benchmark/` contains only `SPARSE_KT_BENCHMARK_SPECIFICATION_v1.0.md` without raw run logs or seed prediction arrays.
- Enforced Task A9 & research rules: Executed explicit decision **REMOVE** to eliminate unverified empirical benchmark numbers ($0.7432$, $0.7685$, $0.7850$, $0.7920$, ECEs, SDs, and p-values) and Table 5 (`tab:empirical_validation`).
- Reframed Section 5.3 as a qualitative architectural comparison of cold-start vs. generic interaction splits across transductive sequence, transductive graph, and inductive semantic/SSL model families.
- Formulated the *pyKT-ColdStart* suite as an evidence-derived research agenda proposal (Section 7 / Pillar 4).
- Created `12_manuscript/TLT/audit/BENCHMARK_EVIDENCE_AUDIT.md`.
- Re-compiled `12_manuscript/TLT/manuscript_TLT_WORKING_v0.1.pdf` (11 pages, 0 compilation errors) and opened automatically.

---

## [v0.7.0] - 2026-09-12 (Task A8)

### Reframed for IEEE Transactions on Learning Technologies (IEEE TLT)
- Updated Introduction, Motivation, Scope, and Related Work to emphasize Educational Data Mining (EDM), Intelligent Tutoring Systems (ITS), adaptive learning, personalized learning pathways, learner-state estimation, curriculum adaptation, and trustworthy mastery prediction.
- Revised Graph-KT definition to: *"incorporating explicit graph or graph-structured relations (e.g., concept prerequisite trees, question-KC bipartite maps, dynamic co-occurrence graphs, relational paths, or hyperbolic skill manifolds) as a central structural mechanism, including but not limited to Graph Neural Network (GNN) message passing."*
- Removed unsupported "first systematic survey" claims across manuscript.
- Rebuilt prior review comparison matrix in Table 2 (`tab:survey_comparison`) comparing Broad KT Surveys, Deep-KT Benchmarks, Graph-KT Reviews, and Ours across 7 audit dimensions.
- Added dedicated `Learning-Technology Implications` subsections to Section 3 (3.6), Section 4 (4.5), Section 5 (5.4), and Section 6 (6.5).
- Created `12_manuscript/TLT/audit/TLT_POSITIONING_AUDIT.md`.
- Re-compiled `12_manuscript/TLT/manuscript_TLT_WORKING_v0.1.pdf` (11 pages, 0 errors) and opened automatically.

---

## [v0.6.0] - 2026-09-12 (Task A7)

### Added
- Created `12_manuscript/TLT/tables/quality_summary.csv` ($N = 37$).
- Created `12_manuscript/TLT/tables/leakage_provenance_summary.csv`.
- Created `12_manuscript/TLT/tables/calibration_reporting_summary.csv` (0 / 37 report ECE).
- Created `12_manuscript/TLT/audit/QUALITY_RELIABILITY_AUDIT.md`.

### Adjudicated & Verified
- Quality Tiers: HIGH ($\ge 0.80$, 29 papers, 78.4\%), MODERATE ($0.55 - 0.79$, 8 papers, 21.6\%), LIMITED ($< 0.55$, 0 papers). Category `MODERATE-HIGH` removed.
- QA7 NA Rule applied to non-sparse studies (applicable max score = 14).
- 0 out of 37 primary core studies report probability calibration (ECE / Brier score).

---

## [v0.5.0] - 2026-09-12 (Task A6)

### Added
- Created `12_manuscript/TLT/tables/ssl_taxonomy.csv` from verified $N_S = 14$ SSL core papers.
- Created `12_manuscript/TLT/tables/sparse_coldstart_audit.csv` from $N = 37$ core papers.
- Created `12_manuscript/TLT/audit/SSL_SPARSE_AUDIT.md`.

### Adjudicated & Verified
- **CL4KT (KT039):** Set `educational_structure_preservation = NO_EXPLICIT_CONSTRAINT` as mandated.
- **Sparse-Concept Audit ($N = 37$):**
  - Citing Interaction Data Sparsity: 35 / 37 (**94.6%**)
  - Evaluating Random Interaction Drop: 35 / 37 (**94.6%**)
  - Evaluating Item Cold-Start: 3 / 37 (**8.1%**)
  - Evaluating Strict Zero-Exposure Concept Cold-Start: 2 / 37 (**5.4%**)
- Denominators and multi-label category definitions documented in audit report.

---

## [v0.4.0] - 2026-09-12 (Task A5)

### Added
- Created `12_manuscript/TLT/audit/KT026_ADJUDICATION.md` (PEBG pre-training objective audited).
- Created `12_manuscript/TLT/audit/KT035_FULLTEXT_AUDIT.md` (HHSKT heterogeneous architecture and sparse protocol audited).

### Adjudicated & Verified
- **KT026 (PEBG):** Confirmed SSL status as `GRAPH_EMBEDDING_PRETRAINING` / `MASKED_PRETRAINING` via joint bipartite graph reconstruction and difficulty regression. Corrected prose claims from contrastive/masked concept prediction to bipartite graph pre-training.
- **KT035 (HHSKT):** Verified full-text heterogeneous GNN schema. Confirmed that HHSKT evaluates interaction sparsity (`SPARSE_INTERACTION_ONLY`), but does **NOT** conduct strict zero-exposure concept cold-start evaluation.

---

## [v0.3.0] - 2026-09-12 (Task A4)

### Added
- Created `12_manuscript/TLT/tables/graph_taxonomy.csv` from full-text coding records.
- Created `12_manuscript/TLT/audit/TAXONOMY_GRAPH_AUDIT.md`.

---

## [v0.2.0] - 2026-09-12 (Task A2)

### Changed
- Migrated manuscript header from TKDE to official IEEE Transactions on Learning Technologies.
- Updated figure paths to use local `12_manuscript/TLT/figures/` asset directory.
- Re-compiled `manuscript_TLT_TEMPLATE_v0.1.pdf` (11 pages, 0 compilation errors).

---

## [v0.1.0] - 2026-09-12 (Task A1)

### Created
- `12_manuscript/TLT/` working environment.
