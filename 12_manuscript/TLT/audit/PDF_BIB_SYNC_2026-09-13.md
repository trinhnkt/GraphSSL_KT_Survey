# Sync `references.bib` to deposited PDFs — 2026-09-13

Filename inventory (cite key ↔ PDF): `PDF_BIB_INVENTORY_2026-09-13.csv`.

Compared title pages in `14_references/` with `12_manuscript/TLT/references.bib`. Applied PDF/title-page names where the file is the correct paper.

## Applied to bib (PDF is the printed name)

| Key | Was | Now (from PDF) |
|---|---|---|
| `KT012_JKT_2021` | Yilun Tang, Tao Zhao, Yilong Chen, Zhiyong Guan | **Yifu Tang, Taige Zhao, Yunliang Chen, Ziyu Guan** (same as Crossref) |
| `KT036_TSKT_2024` | Hua Yang | **Huali Yang** |
| `KT011_BiCLKT_2022` | Qiuyu Lei; Ajmal Saeed Mian | **Qi Lei; Ajmal Mian** |
| `KT014_PDKTC_2018` | Vincent Wenchen Zheng | **Vincent W. Zheng** |
| `KT004_GKT_2019` | … Graph Neural **Networks** | … Graph Neural **Network** (ACM title page) |
| `Ghosh_AKT_2020` | Andrew Lan | **Andrew S. Lan** |

Earlier PDF-confirmed rows kept: GASKT authors, MAHKT authors, SINKT title, PEBG DOI `/219`, HHSKT DOI `2022.119334`, Piech *Leonidas Guibas*.

## Deposit conflicts — bib **not** changed to match the file

| File | Problem | Bib kept |
|---|---|---|
| ~~`Model Generalization - A Sharpness Aware Optimization Perspective.pdf`~~ | **Resolved 2026-09-13 later pass:** that 11-page file *is* DGMN. Renamed to `Deep Graph Memory Networks for Forgetting-Robust Knowledge Tracing.pdf`. The 4-page Coldenhoff/Li/Zhu SAM report is a separate uncited file. | Abdelrahman & Wang, DGMN, `10.1109/TKDE.2022.3206447` |
| `KGNN-KT - Enhancing Knowledge Tracing in Programming Education Through LLM-Extracted Knowledge Graphs.pdf` | Image-only / no extractable title-page text | Crossref/Springer: Di Zhang et al., `10.1007/978-981-96-9986-5_12` |

DGMN deposit is now complete (title-page check: Abdelrahman & Wang).

## Remainder

Last-name checks on the other deposited papers matched the bib. Some ACM files are HTML-to-PDF landing pages (GKT, CL4KT, AKT) but the printed author lines still match.
