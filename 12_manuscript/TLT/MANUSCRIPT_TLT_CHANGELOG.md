# IEEE TLT Manuscript Changelog

All notable changes to the IEEE Transactions on Learning Technologies (IEEE TLT) manuscript preparation package are documented in this file.

---

## [v1.0.0] - 2026-09-12 (Task A15 Final Release)

### Added
- Created complete manuscript LaTeX candidate: `manuscript_TLT_FINAL_CANDIDATE.tex` and compiled PDF `manuscript_TLT_FINAL_CANDIDATE.pdf` (11 double-column pages).
- Created supplementary artifacts package in `supplementary/`:
  - `table_prisma_flow.csv`
  - `table_graph_kt_taxonomy.csv`
  - `table_ssl_kt_taxonomy.csv`
  - `table_quality_reliability.csv`
  - `table_supplementary_extended.csv`
  - `README.md`
- Created audit compliance artifacts in `audit/`:
  - `MANUSCRIPT_TLT_FINAL_COMPLIANCE.md`
  - `MANUSCRIPT_TLT_REMAINING_BLOCKERS.md`

### Changed
- Standardized section structure into 10 explicit IEEE TLT sections matching target journal requirements.
- Standardized mathematical formalism including explicit interaction-level cold-start sets $\mathcal{D}_{\text{train}}^{\text{cold}}$, temperature scaling $T > 0$, and backdoor adjustment causal graph.
- Repositioned core narrative to highlight implications for Intelligent Tutoring Systems (ITS), Educational Data Mining (EDM), and adaptive learning platforms.

### Removed
- Removed unverified hardcoded benchmark AUC/ACC comparison table (Task A9 decision `REMOVE`) to ensure 100% methodological traceability without data fabrication.

---

## [v0.1.0] - 2026-09-12 (Initial Migration)
- Migrated content from `04_manuscript/` into IEEE TLT structure (`12_manuscript/TLT/`).
