# Per-reference live check — 2026-09-20

Source: `12_manuscript/TLT/references.bib` (47 entries; 47 cited keys in manuscript).
Method: Crossref works API + DOI HTTP resolve + local PDF path existence.
**Content check:** identity via title/author/DOI match to Crossref and presence of `file=` PDF; not full-text semantic review.
Raw JSON: `REFERENCE_LIVE_CHECK_2026-09-20.json` · CSV: `REFERENCE_PER_ENTRY_VERDICT_2026-09-20.csv`.

## Summary

| Status | Count |
|---|---:|
| OK (exact Crossref match) | 40 |
| OK_SOFTWARE | 1 |
| CHECK (difference to review) | 2 |
| NO_DOI | 3 |
| DOI_FAIL | 1 |
| PASS / PASS_WITH_NOTES / PASS_NO_DOI (verdict) | 45 |

## Checklist dimensions

| Dimension | How verified |
|---|---|
| Tên bài (title) | Normalized string similarity vs Crossref ≥ 0.88 |
| Tên tác giả (authors) | Family-name set vs Crossref |
| Năm xuất bản (year) | Bib year vs Crossref issued/print/online year |
| Nội dung bài (identity) | Title+author+DOI match + local PDF locator exists |
| Link DOI | `https://doi.org/<doi>` HTTP resolve + Crossref record |

## Entries needing review (CHECK / NO_DOI / DOI_FAIL)

### `KT033_DGMN_2023` — CHECK / PASS_WITH_NOTES (year/pages soft)

- Bib title: Deep Graph Memory Networks for Forgetting-Robust Knowledge Tracing
- Bib year / venue: 2023 / IEEE Trans. Knowl. Data Eng.
- Bib authors: Ghodai Abdelrahman and Qing Wang
- DOI: `10.1109/TKDE.2022.3206447` (HTTP 202)
- URL: https://doi.org/10.1109/TKDE.2022.3206447 (HTTP None)
- Local PDF: `14_references/Deep Graph Memory Networks for Forgetting-Robust Knowledge Tracing.pdf` exists=True
- Title similarity: 1.0
- Crossref title: Deep Graph Memory Networks for Forgetting-Robust Knowledge Tracing
- Crossref year / container: 2022 / IEEE Transactions on Knowledge and Data Engineering
- Crossref volume/issue/page: //1-13
- Crossref authors: Ghodai Abdelrahman; Qing Wang
- Issue: YEAR differ: bib=2023 Crossref=2022
- Issue: PAGES differ: bib=7844-7855 Crossref=1-13

### `KT077_R2GCurL_2026` — CHECK / FAIL_OR_REVIEW (title/author/DOI)

- Bib title: 
- Bib year / venue: 2026 / ACM Trans. Inf. Syst.
- Bib authors: Tianhao Peng and Yanjun Pu and Yongqi Zhang and Yuchen Li and Jian Ren and Jie Luo and Kui Zhang and Haitao Yuan and Shuaiqiang Wang and Dawei Yin and Wenjun Wu
- DOI: `10.1145/3818614` (HTTP 403)
- URL: https://doi.org/10.1145/3818614 (HTTP None)
- Local PDF: `14_references/R2GCurL - Reinforced Robust Knowledge Tracing via Dynamic Graph Curriculum Learning.pdf` exists=True
- Title similarity: 0.0
- Crossref title: R
                    <sup>2</sup>
                    GCurL: Reinforced Robust Knowledge Tracing via Dynamic Graph Curriculum Learning
- Crossref year / container: 2026 / ACM Transactions on Information Systems
- Crossref volume/issue/page: 44/6/1-32
- Crossref authors: Tianhao Peng; Yanjun Pu; Yongqi Zhang; Yuchen Li; Jian Ren; Jie Luo; Kui Zhang; Haitao Yuan; Shuaiqiang Wang; Dawei Yin; Wenjun Wu
- Issue: TITLE mismatch (sim=0.00)

### `Piech_DKT_2015` — NO_DOI / PASS_NO_DOI (URL OK; verify title/authors against proceedings)

- Bib title: Deep Knowledge Tracing
- Bib year / venue: 2015 / Adv. Neural Inf. Process. Syst. (NeurIPS)
- Bib authors: Chris Piech and Jonathan Bassen and Jonathan Huang and Surya Ganguli and Mehran Sahami and Leonidas Guibas and Jascha Sohl-Dickstein
- DOI: `NONE` (HTTP None)
- URL: https://proceedings.neurips.cc/paper/2015/hash/bac9162b47c56fc8a4d2a519803d51b3-Abstract.html (HTTP 200)
- Local PDF: `14_references/Deep Knowledge Tracing.pdf` exists=True
- Title similarity: None
- Issue: No DOI — official URL reachable (proceedings/OA)

### `Pandey_SAKT_2019` — NO_DOI / PASS_NO_DOI (URL OK; verify title/authors against proceedings)

- Bib title: A Self-Attentive Model for Knowledge Tracing
- Bib year / venue: 2019 / Proc. 12th Int. Conf. Educ. Data Mining (EDM)
- Bib authors: Shalini Pandey and George Karypis
- DOI: `NONE` (HTTP None)
- URL: https://educationaldatamining.org/edm2019/proceedings/ (HTTP 200)
- Local PDF: `14_references/A Self-Attentive Model for Knowledge Tracing.pdf` exists=True
- Title similarity: None
- Issue: No DOI — official URL reachable (proceedings/OA)

### `Liu_pyKT_2022` — NO_DOI / PASS_NO_DOI (URL OK; verify title/authors against proceedings)

- Bib title: {pyKT}: A {Python} Library to Benchmark Deep Learning based Knowledge Tracing Models
- Bib year / venue: 2022 / Adv. Neural Inf. Process. Syst. (NeurIPS) Datasets Benchmarks Track
- Bib authors: Zitao Liu and Qiongqiong Liu and Jiahao Chen and Shuyan Huang and Jiliang Tang and Weiqi Luo
- DOI: `NONE` (HTTP None)
- URL: https://proceedings.neurips.cc/paper_files/paper/2022/hash/75ca2b23d9794f02a92449af65a57556-Abstract-Datasets_and_Benchmarks.html (HTTP 200)
- Local PDF: `14_references/pyKT - A Python Library to Benchmark Deep Learning based Knowledge Tracing Models.pdf` exists=True
- Title similarity: None
- Issue: No DOI — official URL reachable (proceedings/OA)

### `Xu_GbKT_2026` — DOI_FAIL / FAIL DOI/Crossref

- Bib title: A Survey of Graph-Based Knowledge Tracing from Structural and Propagation Perspectives: Models, Applications, and Future Directions
- Bib year / venue: 2026 / J. Educ. Data Min.
- Bib authors: 
- DOI: `10.5281/zenodo.21443288` (HTTP 200)
- URL: https://jedm.educationaldatamining.org/index.php/JEDM/article/view/1089 (HTTP None)
- Local PDF: `14_references/A Survey of Graph-Based Knowledge Tracing from Structural and Propagation Perspectives - Models, Applications, and Future Directions.pdf` exists=True
- Title similarity: None
- Issue: Crossref fetch failed: HTTP Error 404: Not Found

## Full per-entry verdict (cited only)

| Key | Verdict | Title sim | DOI HTTP | PDF | Notes |
|---|---|---:|---:|:---:|---|
| `Abdelrahman_Survey_2023` | PASS | 1.0 | 403 | Y | — |
| `Cursor_AI_2026` | PASS (software cite; not a research paper) | — | — | — | — |
| `Ghosh_AKT_2020` | PASS | 1.0 | 403 | Y | — |
| `KT004_GKT_2019` | PASS | 1.0 | 403 | Y | — |
| `KT010_GIKT_2021` | PASS | 1.0 | 200 | Y | — |
| `KT011_BiCLKT_2022` | PASS | 1.0 | 200 | Y | — |
| `KT012_JKT_2021` | PASS | 1.0 | 200 | Y | — |
| `KT014_PDKTC_2018` | PASS | 1.0 | 202 | Y | — |
| `KT016_SKT_2020` | PASS | 1.0 | 202 | Y | — |
| `KT023_SGKT_2022` | PASS | 1.0 | 200 | Y | — |
| `KT026_PretrainQ_2020` | PASS | 1.0 | 200 | Y | — |
| `KT029_DGEKT_2024` | PASS | 1.0 | 403 | Y | — |
| `KT031_KSGAKT_2022` | PASS | 1.0 | 403 | Y | — |
| `KT033_DGMN_2023` | PASS_WITH_NOTES (year/pages soft) | 1.0 | 202 | Y | YEAR differ: bib=2023 Crossref=2022; PAGES differ: bib=7844-7855 Crossref=1-13 |
| `KT035_HHSKT_2023` | PASS | 1.0 | 200 | Y | — |
| `KT036_TSKT_2024` | PASS | 1.0 | 200 | Y | — |
| `KT037_CMKT_2022` | PASS | 1.0 | 202 | Y | — |
| `KT038_DyGKT_2024` | PASS | 1.0 | 403 | Y | — |
| `KT039_CL4KT_2022` | PASS | 1.0 | 403 | Y | — |
| `KT042_S2HHN_2023` | PASS | 1.0 | 200 | Y | — |
| `KT043_3VCLKT_2024` | PASS | 1.0 | 202 | Y | — |
| `KT044_SINKT_2024` | PASS | 1.0 | 403 | Y | — |
| `KT047_DCSSL_2023` | PASS | 1.0 | 200 | Y | — |
| `KT050_GraphCA_2023` | PASS | 1.0 | 202 | Y | — |
| `KT052_CapsuleGNN_2022` | PASS | 1.0 | 200 | Y | — |
| `KT053_GASKT_2021` | PASS | 1.0 | 200 | Y | — |
| `KT056_LSTGraph_2025` | PASS | 1.0 | 200 | Y | — |
| `KT060_STHKT_2025` | PASS | 1.0 | 200 | Y | — |
| `KT062_LGSKT_2025` | PASS | 1.0 | 200 | Y | — |
| `KT063_MAHKT_2025` | PASS | 1.0 | 200 | Y | — |
| `KT064_MGEnsemble_2025` | PASS | 1.0 | 200 | Y | — |
| `KT065_CSGKT_2025` | PASS | 1.0 | 200 | Y | — |
| `KT066_HyperKT_2025` | PASS | 1.0 | 202 | Y | — |
| `KT067_SKMGKT_2025` | PASS | 1.0 | 200 | Y | — |
| `KT068_HKT_2025` | PASS | 1.0 | 200 | Y | — |
| `KT069_AEGOTCDKT_2025` | PASS | 1.0 | 200 | Y | — |
| `KT070_Coda_2025` | PASS | 1.0 | 403 | Y | — |
| `KT076_KGNNKT_2025` | PASS | 1.0 | 200 | Y | — |
| `KT077_R2GCurL_2026` | FAIL_OR_REVIEW (title/author/DOI) | 0.0 | 403 | Y | TITLE mismatch (sim=0.00) |
| `KT079_STGSKT_2026` | PASS | 1.0 | 200 | Y | — |
| `Liu_DLKT_2025` | PASS | 1.0 | 202 | Y | — |
| `Liu_pyKT_2022` | PASS_NO_DOI (URL OK; verify title/authors against proceedings) | — | — | Y | No DOI — official URL reachable (proceedings/OA) |
| `Pandey_SAKT_2019` | PASS_NO_DOI (URL OK; verify title/authors against proceedings) | — | — | Y | No DOI — official URL reachable (proceedings/OA) |
| `Piech_DKT_2015` | PASS_NO_DOI (URL OK; verify title/authors against proceedings) | — | — | Y | No DOI — official URL reachable (proceedings/OA) |
| `Shen_KTSurvey_2024` | PASS | 1.0 | 202 | Y | — |
| `Xu_GbKT_2026` | FAIL DOI/Crossref | — | 200 | Y | Crossref fetch failed: HTTP Error 404: Not Found |
| `Zhang_DKVMN_2017` | PASS | 1.0 | 403 | Y | — |
