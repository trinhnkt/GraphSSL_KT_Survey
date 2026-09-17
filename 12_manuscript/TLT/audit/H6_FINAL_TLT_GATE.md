# H6 — Final TLT gate

**Date:** 2026-09-13 (updated after residual-review fixes)  
**Source:** `manuscript_TLT_FORMATTED_v1.3.tex`  
**PDF:** `12_manuscript/TLT/manuscript_TLT_FORMATTED_v1.3.pdf`  
**Decisions:** `audit/CURSOR_FINAL_FIX_DECISIONS.md`

## Locked counts (identity)

| Quantity | Value | Source evidence |
|---|---:|---|
| \(N_{\mathrm{CORE}}\) | 37 | `corpus_counts.csv` `N_PRIMARY_CORE` |
| \(N_G\) | 36 | `graph_taxonomy.csv` unique papers with `graph_source != NONE` |
| \(N_S\) | 9 | `ssl_taxonomy.csv` after H1 |
| \(N_{G\cap S}\) | 8 | SSL IDs except KT039 |
| Identity | \(36+9-8=37\) | H1 decision note |
| Exclusive locked SSL families | 4 | `MULTIVIEW_CONTRASTIVE` 5; `GRAPH_CONTRASTIVE` 2; `GRAPH_RECONSTRUCTION` 1; `SEQUENCE_CONTRASTIVE` 1 |
| Strict KC cold-start YES | 0/37 | PDF-strict recode; see `LOCKED_COUNTS_v1.6.md` |
| Item cold-start YES | 1/37 | KT044 question hold-out only |
| Learner cold-start YES | 0/37 | sparse audit |
| QA HIGH / MODERATE / LIMITED | 11 / 26 / 0 | H2; mean 0.76; max = 16 |
| Provenance | 18 / 9 / 9 | model-defined / external / dynamic |
| Encoder display | GCN/generic 12; Heterogeneous 7; Other 6; GAT 4; NONE 3 | v1.6 (HKT GNN_GENERIC; Coda DYNAMIC) |

## Gate table

| Check | Status | Source evidence | Manuscript location | Remaining risk |
|---|---|---|---|---|
| \(N_{\mathrm{CORE}}=37\) | PASS | `corpus_counts.csv` | Abstract; §I.C; Conclusion | None |
| \(N_G=36\), \(N_S=9\), \(N_{G\cap S}=8\) | PASS | H1 CSV + `ssl_taxonomy.csv` (9 rows) | Abstract; Table II; Figs. 2/5; Table IV; §IV; Conclusion | Author should confirm the five SSL removals |
| SSL families = 4 locked tokens | PASS | `audit/SSL_FAMILY_LOCKED_ALIGNMENT.md` | Table IV; Fig. 5; §IV | Mechanism notes must not be read as extra family codes |
| Strict KC / item / learner cold-start | PASS | `sparse_coldstart_audit.csv` | Table V; §V; agenda | None |
| QA7 applicable 37/37 | PASS | RQ4 evidence lens; protocol §22.1 NA option **not used** | §II.D unnumbered overlay; §VI | Do not say “all papers claim sparsity” |
| QA tiers HIGH 11 / MODERATE 26 / LIMITED 0 | PASS | H2; scores unchanged | §II.D; §VI | HIGH list is a reporting-adequacy partition, not a ranking of contribution |
| Table II prior surveys | PASS | Liu TKDE 2025 DOI; Xu JEDM 2026 URL; no `\resizebox` | §I.C; Table II; bib | Xu has no recorded DOI |
| Table III GKT / PEBG | PASS | H4; PEBG PDF / `gnn_encoder=NONE` | Table III; Fig. 4 | Dense/Transition stay in supplementary CSV |
| Eq. 8 not `K/cold` | PASS | PDF text: `KC(xt) ∈ K \ Kcold` | Agenda pillar 3 | Visual check still recommended |
| Treatment ≠ history / adjacency | PASS | Treatment \(W\); history \(\mathcal{X}_{1:T}\); adjacency \(\mathbf{A}\) | Table I; Eq. 11 | None |
| Five index terms | PASS | IEEE keywords block | Title page | None |
| AI disclosure | PASS | Acknowledgment expanded | Acknowledgment | Authors must confirm the wording |
| No “first survey” | PASS | Explicit non-claim | §I.C | None |
| No unmatched “consistently improves” | PASS | Source grep | — | None |
| No leakage % | PASS | Protocol: no locked rate | §III.D; Table VI | None |
| No AUC league table | PASS | Explicit non-claim | §V; Conclusion | None |
| Compile / citations | PASS | Rebuild after this update | PDF | Unused `lettersize` option; underfull boxes |
| Figures 2/5 rebuilt | PASS | Figure tex + pdflatex | Figs. 2, 5 | Older audit maps may still quote \(N_S=14\) or 7 families; do not ship those |

## Language rules

Checked in source: no first-survey claim; no collapse-prevention result; no random-guess statistic; no locked leakage percentage; no cross-paper AUC ranking.

## Final status

**READY_FOR_SUBMISSION** (technical gate: counts, wording, compile).

This is not an automatic submit. Authors should still sign off the H1 SSL corpus (\(N_S=9\)) and the AI-disclosure sentence before ScholarOne upload.

Do not attach this gate file as supplementary unless it matches the compiled PDF.

Do not submit automatically.
