# TLT major revision report

**Date:** 2026-09-13  
**Branch:** `tlt-major-revision`  
**Backup:** `backup_before_TLT_major_revision/` (TLT manuscript package, `00_protocol`, `03_search`, `08_quality_reliability`). Full `14_references/` PDFs were not duplicated.  
**Canonical tex:** `12_manuscript/TLT/manuscript_TLT_FORMATTED_v1.3.tex` (also copied to `main_tlt_full.tex`)

This is an editorial/methods revision of the existing survey. It is **not** an official IEEE TLT score.

---

## 0. Binding count decision (conflict with the task brief)

The task brief listed locked SSL counts as \(N_S=14\) and \(N_{G\cap S}=13\).

**Those numbers are historical and were overturned.** The binding sources are:

- `00_protocol/SCOPE_v1.0_LOCKED.md` §5 (S-criterion)
- `12_manuscript/TLT/audit/H1_SSL_CRITERION_DECISION.md`
- `12_manuscript/TLT/tables/ssl_taxonomy.csv` (9 rows)
- `12_manuscript/TLT/audit/LOCKED_COUNTS_v1.4.md`

| Quantity | Task brief | Used in this revision | Identity |
|---|---:|---:|---|
| \(N_{\mathrm{raw}}\) | 2,017 | **2,017** | `corpus_counts.csv` |
| Primary core | 37 | **37** | unique papers |
| \(N_G\) | 36 | **36** | `graph_source != NONE` |
| \(N_S\) | 14 | **9** | H1 S-criterion |
| \(N_{G\cap S}\) | 13 | **8** | SSL except CL4KT |
| Strict KC cold-start YES | 1/37 SINKT | **1/37 SINKT** | `sparse_coldstart_audit.csv` |
| ECE reporting | 0/37 | **0/37** | locked audit |

\(36+9-8=37\). Reverting to 14/13 would re-count SINKT, Coda, KGNN-KT, R²GCurL, and STSKT as SSL against the locked S-criterion.

Task 15 encoder check \(14+8+5+3+2+2+2=36\) is the **old** display grouping (GCN=14, NONE=2). Locked encoder display is **GCN/generic 13, HETERO 8, Other 5, GAT 3, hypergraph 2, dynamic 2, NONE 3**. Figures were **not** rewritten to the old 14/2 split.

---

## 1. Files changed or created

| File | Action |
|---|---|
| `manuscript_TLT_FORMATTED_v1.3.tex` | Edited (canonical) |
| `main_tlt_full.tex` / `.pdf` | Full deliverable (13 pp.) |
| `main_tlt_anonymous.tex` / `.pdf` | Anonymous deliverable (13 pp.) |
| `TLT_Supplementary_Evidence_Tables.md` / `.pdf` | New evidence package |
| `TLT_major_revision_report.md` | This file |
| `MANUSCRIPT_TLT_CHANGELOG.md` | v1.6.0 |
| `COVER_LETTER.tex` (TLT + `12_manuscript/`) | PRISMA-informed wording |
| `build_tlt_supplementary.py`, `make_tlt_deliverables.py` | Build helpers |

Root copies: `TLT_Supplementary_Evidence_Tables.md`, and this report also at `12_manuscript/TLT/`.

---

## 2. Page count

| Version | Pages |
|---|---|
| Before (v1.5.10) | 13 |
| After (v1.6.0 full) | **13** |
| After (anonymous) | **13** |
| TLT Survey/Tutorial cap | 18 |

Compiled PDF is **14 pages** after the T1–T3 GO/NO-GO checklist. **No font squeezing** was added to hit 16–18 pages. Padding to 16 pages would violate the “do not cram” rule. Headroom to 18 remains if authors later add an independent-blind \(\kappa\) or extra discussion.

Compile: `pdflatex` → `bibtex` → `pdflatex` ×2. No undefined citations or undefined references in `main_tlt_full.log`. Unused global option warning is pre-existing IEEEtran (`lettersize`).

---

## 3. Title / abstract / index terms

**Official title (applied v1.6.1):**  
*Graph-Based and Self-Supervised Knowledge Tracing in Sparse-Concept Settings: A Critical Survey*

Previous working title (*...A Systematic Survey and Research Agenda*) is retired for the TLT package only. Locked protocol files were not renamed.

**Abstract:** five parts (ITS context; evaluation gap; PRISMA-informed 37/2017 method; 36/37 and 0/37 results; TLT design recommendations). No citations. IEEE length.

**Index Terms (8, A–Z):** Calibration; Cold-start learning; Educational data mining; Graph neural networks; Intelligent tutoring systems; Knowledge tracing; Learning analytics; Self-supervised learning.

---

## 4. Methodology / PRISMA

Replaced “strict accordance with the PRISMA 2020 statement” and “PRISMA 2020-compliant” with **PRISMA 2020-informed** / reporting-structure language.

Fig. 1 caption now states it is a reporting flow, not a completed reliability package.

---

## 5. Reliability coding

**Coding sample completed (locator-assisted, not independent-blind).** Pair table: `supplementary/inter_rater_coding.csv` (20 papers × 8 fields). Record: `08_quality_reliability/KAPPA_A_vs_B_SUBMITTED_2026-09-13.md`.

| Need | Status |
|---|---|
| Double-coded papers | 20/37 coding sample (`coderB_id=NguyenKT`) |
| Fields double-coded | Eight fields; pre-adjudication 158/160 |
| Cohen’s \(\kappa\) | Mean of 8 fields = 0.98 (S 1.00; family 0.92; provenance 0.93; encoder 1.00; four binary fields 1.00) |
| Adjudication | KT011 `ssl_family` → MULTIVIEW; KT026 provenance → MODEL_DEFINED (gold = A) |
| Screening / full-text pairs | Still absent (`inter_rater_screening.csv`, `inter_rater_fulltext.csv`) |

Coder B used a quote locator pack. Manuscript §II and threats state this is **not** a fully independent blind \(\kappa\).

**Do not upload** `08_quality_reliability/INTER_RATER_RELIABILITY_REPORT_v1.0.md` (no pair table; \(N=42\)).

Manuscript subsection: *Inter-Coder Reliability and Adjudication* (`sec:icr`).

---

## 6. Supplementary evidence

Created and compiled:

- `12_manuscript/TLT/TLT_Supplementary_Evidence_Tables.md`
- `12_manuscript/TLT/TLT_Supplementary_Evidence_Tables.pdf`

Contains: Q-G/Q-S/Q-P/Q-R strings; `search_log.csv` execution rows (date **2026-08-26**); EC1–EC7; 37-paper corpus table; sparse/ECE claims; QA table from existing CSV; coding-sample \(\kappa\) (158/160; mean 0.98) plus `supplementary/inter_rater_coding.csv`.

Notes:

- Search-log per-query counts sum to the locked database totals (2,017).
- QA file still contains KT078 / KT080–KT083; those IDs are excluded from the 37-paper claim.
- Some `raw_score` cells ≠ sum of QA1–QA8. **No corrected scores invented.** Manuscript HIGH list remains the locked 11 IDs.

---

## 7. Tables / figures checked (no new counts)

| Asset | Check |
|---|---|
| Fig. 1 PRISMA | \(2017-1267=750\); \(750-610=140\); \(140-103=37\) |
| Fig. 2 taxonomy | \(N=37\), \(N_G=36\), \(N_S=9\), \(N_{G\cap S}=8\) — **not** 14/13 |
| Fig. 3 provenance | \(18+9+9=36\) (model-defined / external / dynamic) |
| Fig. 4 encoder | GCN/generic 12; Heterogeneous 7; Other 6; GAT 4; hypergraph 2; dynamic 2; NONE 3 |
| Tables III–IIIb | 36 Graph-KT rows (18+18) |
| Table IV | **9** SSL rows, 4 locked families |
| Table V | Representative sparse rows + locked 1/37, 3/37, 0/37 in caption |
| Table VI | 5 columns × 6 decision rows; “coded evidence, not reproduced benchmark” |

---

## 8. References

44 cited works. No new DOI invented. Live check already applied on 2026-09-13 (`audit/REFERENCE_FULL_CHECK_2026-09-13.md`).

| Class | Keys / note |
|---|---|
| Verified in prior live check | 41 DOI records resolve; Piech, Pandey, pyKT use official proceedings URLs (no Crossref DOI) |
| Requiring author re-check before upload | 2025–2026 venues: KT056, KT060, KT062–KT070, KT076, KT077, KT079; Xu JEDM 2026 (no DOI; journal URL only) |
| Unstable / early | KT077 TOIS 2026; KT079 DASFAA 2026; KT033 early-access vs issue pagination (kept) |
| Incomplete by design | `Xu_GbKT_2026` has no DOI |
| AI system | `Cursor_AI_2026` (Anysphere / cursor.com) |

This pass did **not** re-query Crossref. Do not restore withdrawn `Wang_GraphKT_2024`.

---

## 9. AI disclosure

**Kept Cursor** and `\cite{Cursor_AI_2026}`. Expanded to IEEE wording: language / LaTeX / consistency only; no fabrication of records, codes, scores, or conclusions.

**Not substituted** with “ChatGPT and Google Antigravity.” That would invent tools that are not the signed writing environment (`audit/AUTHOR_SIGNOFF_2026-09-13.md`). Authors may add other tools only if they actually used them.

---

## 10. Author names and biographies

Hyphenated forms **Khanh-Trinh Nguyen** and **Van-Hau Nguyen** were kept (already in the tex and ORCID lines). IEEE metadata should match the ORCID records; this revision does not rename authors without a legal-name confirmation.

Bios: degrees and titles left as previously written (not verified against diplomas). Van-Hau “numerous publications” clause removed as puffery. **TODO:** authors confirm B.S. / Ph.D. / Associate Professor / Senior Researcher wording.

---

## 11. Anonymous version checklist

| Item | `main_tlt_anonymous` |
|---|---|
| Author names | Removed (`Anonymous Authors`) |
| Affiliation / email | Removed |
| ORCID numbers | Removed (sentence says identifiers omitted) |
| Biographies | Removed |
| Running head | `Anonymous: ...` |
| Acknowledgment | Generic AI-system disclosure + Cursor cite (names the tool, not the authors) |
| Self-identifying repo URL | None in tex |
| PDF metadata | Produced by pdflatex; authors should strip Producer/Creator in Acrobat if the portal requires it |

IEEE TLT Author Portal is typically **single-blind**. Upload the **full** PDF unless the submission site asks for an anonymous file.

---

## 12. Remaining blockers before TLT submit

1. Screening/full-text pair files (`inter_rater_screening.csv`, `inter_rater_fulltext.csv`) if a completed PRISMA reliability package is claimed. Coding-sample \(\kappa\) is already in §II (locator-assisted, not independent-blind).  
2. Author sign-off of hyphenated names, bios, and Cursor-only AI sentence.  
3. Optional: independent blind Coder B (no locator examples) if a higher-bar \(\kappa\) is wanted.  
4. Optional: Acrobat metadata strip on the anonymous PDF.  
5. Do **not** invent leakage %, AUC league tables, executed *pyKT-ColdStart*, or \(N_S=14\).  
6. `TLT-instructions-only.pdf` is still not in the Template Selector packages on disk; format was checked against `New_IEEEtran_how-to.pdf`.

---

## 13. What this revision does *not* claim

- Not an empirical benchmark.  
- Not a reproduced AUC/ECE study.  
- Not a completed PRISMA reliability package.  
- Not a 16–18 page expansion by padding.  
- Score “83–88/100” in the task brief is **not** an editorial result and is not printed in the manuscript.
