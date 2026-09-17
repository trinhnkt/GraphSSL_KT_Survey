# ScholarOne upload list (2026-09-13)

**Superseded for submission.** TLT now requires the IEEE Author Portal. Use `AUTHOR_PORTAL_UPLOAD_LIST_2026-09-13.md` (13-page PDF). Keep this file only as the earlier checklist.

Do **not** attach `12_manuscript/TLT/audit/` (old \(N_S=14\) / 7-family maps, H6 gate, PDF recheck).

## Manuscript (required)

| File | Path |
|---|---|
| Main PDF — full (14 pages) | `12_manuscript/TLT/Graph-Based and Self-Supervised Knowledge Tracing in Sparse-Concept Settings - A Critical Survey.pdf` |
| Main PDF — anonymous (14 pages) | `12_manuscript/TLT/Graph-Based and Self-Supervised Knowledge Tracing in Sparse-Concept Settings - A Critical Survey - Anonymous.pdf` |
| LaTeX source | `12_manuscript/TLT/manuscript_TLT_FORMATTED_v1.3.tex` |
| Bibliography | `12_manuscript/TLT/references.bib` |
| Class file (needed to compile) | `12_manuscript/TLT/IEEEtran.cls` |

## Figures (upload with source or embed; already in the PDF)

| File |
|---|
| `12_manuscript/TLT/figures/fig_prisma_flow.pdf` |
| `12_manuscript/TLT/figures/fig_taxonomy_2d.pdf` |
| `12_manuscript/TLT/figures/fig_graph_construction_pipeline.pdf` |
| `12_manuscript/TLT/figures/fig_meta_analysis_charts.pdf` |
| `12_manuscript/TLT/figures/fig_ssl_framework.pdf` |

Optional source: the matching `.tex` in the same folder.

## Supplementary CSV (current)

Upload these, not `audit/*.csv`:

| File | Use |
|---|---|
| `supplementary/supplementary_corpus_inventory.csv` | 37-paper inventory |
| `supplementary/supplementary_ssl_taxonomy_Ns9.csv` | **9 SSL rows only** (do not upload the old 14-row `supplementary_coding_matrix.csv`) |
| `supplementary/supplementary_quality_scores.csv` | QA1–QA8 |
| `supplementary/supplementary_prisma_exclusions.csv` | Full-text exclusions |
| `supplementary/supplementary_doi_audit.csv` | DOI audit |
| `tables/H2_qa7_two_variables.csv` | QA7 overlay 37 rows |
| `tables/ssl_taxonomy.csv` | Same 9 SSL rows as the manuscript table |
| `tables/graph_taxonomy.csv` | 36 Graph-KT rows |
| `tables/sparse_coldstart_audit.csv` | Sparse/cold-start |

## Cover letter (if ScholarOne asks)

`12_manuscript/TLT/COVER_LETTER.tex` (and its PDF if you compile it). Do not write “first survey.”

## Do not upload

- Entire `audit/` folder
- `H1_FIVE_PAPER_PDF_RECHECK_2026-09-13.md`
- `supplementary_coding_matrix.csv` (still has 5 non-SSL rows with retired family aliases)
- `14_references/` PDFs of cited papers (not a TLT supplement unless the journal asks)
- `_pdf_extract_tmp/`
