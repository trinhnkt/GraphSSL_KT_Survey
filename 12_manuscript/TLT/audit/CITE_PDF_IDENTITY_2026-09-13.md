# Cite ↔ PDF identity check — 2026-09-13

Compared in-text cite keys and `references.bib` title/authors with the first two pages of each deposited PDF in `14_references/`.

## Summary

- Bib entries checked: 44
- In-text cite keys: 44
- Identity MATCH (title + authors on title page): 43 by text, **44/44 after visual check of KGNN-KT**
- Title OK, authors partial: 0
- Image-only / no extractable text: 1 (`KT076_KGNNKT_2025`) — title page inspected as image; it **is** KGNN-KT
- Wrong paper or title mismatch or missing PDF: 0
- Cite keys in tex missing from bib: none
- Bib keys not cited in tex: none

Machine-readable: `CITE_PDF_IDENTITY_2026-09-13.csv`.

## Needs attention

| Cite key | Status | Notes | PDF first-page excerpt |
|---|---|---|---|
| `KT076_KGNNKT_2025` | IMAGE_ONLY then VISUAL_MATCH | Scan has no extractable text. Page 1 shows *KGNN-KT: Enhancing Knowledge Tracing in Programming Education through LLM-Extracted Knowledge Graphs*; Di Zhang, Qiang Niu, Tianshi Wang, Yuntian Hou, Jinheng Wu, Chao Zhang, Angelos Stefanidis; ICIC 2025; DOI `10.1007/978-981-96-9986-5_12`; pp. 137–147. | Springer title page (image) |

## All cited works

| Cite key | Status | Title OK | Authors OK | Pages |
|---|---|---|---|---|
| `KT004_GKT_2019` | MATCH | YES | YES | 9 |
| `KT010_GIKT_2021` | MATCH | YES | YES | 17 |
| `KT011_BiCLKT_2022` | MATCH | YES | YES | 12 |
| `KT012_JKT_2021` | MATCH | YES | YES | 14 |
| `KT014_PDKTC_2018` | MATCH | YES | YES | 10 |
| `KT016_SKT_2020` | MATCH | YES | YES | 10 |
| `KT023_SGKT_2022` | MATCH | YES | YES | 12 |
| `KT026_PretrainQ_2020` | MATCH | YES | YES | 7 |
| `KT029_DGEKT_2024` | MATCH | YES | YES | 24 |
| `KT031_KSGAKT_2022` | MATCH | YES | YES | 34 |
| `KT033_DGMN_2023` | MATCH | YES | YES | 11 |
| `KT035_HHSKT_2023` | MATCH | YES | YES | 13 |
| `KT036_TSKT_2024` | MATCH | YES | YES | 13 |
| `KT037_CMKT_2022` | MATCH | YES | YES | 14 |
| `KT038_DyGKT_2024` | MATCH | YES | YES | 12 |
| `KT039_CL4KT_2022` | MATCH | YES | YES | 10 |
| `KT042_S2HHN_2023` | MATCH | YES | YES | 17 |
| `KT043_3VCLKT_2024` | MATCH | YES | YES | 10 |
| `KT044_SINKT_2024` | MATCH | YES | YES | 11 |
| `KT047_DCSSL_2023` | MATCH | YES | YES | 13 |
| `KT050_GraphCA_2023` | MATCH | YES | YES | 16 |
| `KT052_CapsuleGNN_2022` | MATCH | YES | YES | 18 |
| `KT053_GASKT_2021` | MATCH | YES | YES | 12 |
| `KT056_LSTGraph_2025` | MATCH | YES | YES | 18 |
| `KT060_STHKT_2025` | MATCH | YES | YES | 13 |
| `KT062_LGSKT_2025` | MATCH | YES | YES | 13 |
| `KT063_MAHKT_2025` | MATCH | YES | YES | 13 |
| `KT064_MGEnsemble_2025` | MATCH | YES | YES | 13 |
| `KT066_HyperKT_2025` | MATCH | YES | YES | 15 |
| `KT067_SKMGKT_2025` | MATCH | YES | YES | 28 |
| `KT068_HKT_2025` | MATCH | YES | YES | 18 |
| `KT069_AEGOTCDKT_2025` | MATCH | YES | YES | 25 |
| `KT070_Coda_2025` | MATCH | YES | YES | 12 |
| `KT076_KGNNKT_2025` | VISUAL_MATCH | YES | YES | 11 |
| `KT077_R2GCurL_2026` | MATCH | YES | YES | 32 |
| `KT065_CSGKT_2025` | MATCH | YES | YES | 22 |
| `KT079_STGSKT_2026` | MATCH | YES | YES | 16 |
| `Piech_DKT_2015` | MATCH | YES | YES | 9 |
| `Pandey_SAKT_2019` | MATCH | YES | YES | 6 |
| `Ghosh_AKT_2020` | MATCH | YES | YES | 11 |
| `Zhang_DKVMN_2017` | MATCH | YES | YES | 10 |
| `Abdelrahman_Survey_2023` | MATCH | YES | YES | 36 |
| `Liu_pyKT_2022` | MATCH | YES | YES | 14 |
| `Shen_KTSurvey_2024` | MATCH | YES | YES | 22 |

## Survey nicknames vs official PDF titles

These table labels are survey short names. The cited PDF is still the same paper as the bib title.

| Cite key | Survey label | Official title on the PDF |
|---|---|---|
| `KT026` | PEBG / Pre-train Q-Emb | Improving Knowledge Tracing via Pre-training Question Embeddings (PEBG appears in the paper) |
| `KT047` | DC-SSL | Fusing Hybrid Attentive Network with Self-Supervised Dual-Channel Heterogeneous Graph for Knowledge Tracing |
| `KT031` | KSG-AKT | Knowledge Structure Enhanced Graph Representation Learning Model for Attentive Knowledge Tracing |
| `KT065` | CS-GKT | Graph Knowledge Tracing in Cognitive Situation… (paper uses CSGKT) |
| `KT067` | SKM-GKT | Graph-Based Effective Knowledge Tracing via Subject Knowledge Mapping |
| `KT079` | STG-SKT | Spatio-Temporal Fusion in Graph Neural Network for Streaming Knowledge Tracing |

## Method

- Title: normalized string (punctuation/case ignored) must appear on page 1–2, or six longest content words must all appear.
- Authors: first-author last name plus at least half of the remaining last names must appear on page 1–2.
- Wrong-paper flags: SAM/ASAM (Coldenhoff) or trajectory-prediction text in a KT cite.
- Did not re-code methods or results; this is identity only.
