# Reference check — 2026-09-13

Target: `12_manuscript/TLT/references.bib` vs manuscript cites, Crossref/publisher records, and `14_references/` PDFs.

Do **not** treat `audit/REFERENCE_CONFLICTS.md` (2026-09-12; 43 entries) or `REFERENCE_METADATA_AUDIT.csv` “VERIFIED_PUBLISHER” rows as current truth.

## Cite ↔ bib ↔ PDF

| Check | Result |
|---|---|
| In-text cite keys | 44 |
| BibTeX entries | 44 |
| Cite missing from bib | 0 |
| Uncited bib entries | 0 |
| Primary-core papers cited | 37/37 |
| PDFs in `14_references/` | 44/44 cited works have a matching title-named file |

`KT033_DGMN_2023` is deposited as `Deep Graph Memory Networks for Forgetting-Robust Knowledge Tracing.pdf` (was misnamed as the SAM title). `Zhang_DKVMN_2017` is deposited.

Uncited PDFs are kept on disk and are **not** listed in the bibliography or the cite-key inventory.

Inventory: `audit/PDF_BIB_INVENTORY_2026-09-13.csv`.

## Status after bib update (same day)

C1–C4 were written into `references.bib` and the two audit CSVs on 2026-09-13. Cite keys unchanged. Model nicknames in the manuscript (DC-SSL, Coda) unchanged.

## Conflicts (publisher record; now applied to bib)

### C1 — KT047 / DC-SSL (title, authors, volume)

- Bib: Zhengyang Wu, Yuqi Liu; title *Dual-Channel Self-Supervised Learning for Heterogeneous Graph Knowledge Tracing*; ESWA **231**, 120212; DOI `10.1016/j.eswa.2023.120212`.
- Crossref for that DOI: **Tangjie Wu, Qiang Ling**; *Fusing hybrid attentive network with self-supervised dual-channel heterogeneous graph for knowledge tracing*; ESWA **225**, article 120212.
- Deposited PDF title matches Wu & Ling, not the bib title.
- Old CSV marked this VERIFIED_PUBLISHER — that label is wrong.

### C2 — KT070 / Coda (author list)

- DOI `10.1145/3690624.3709172` and title/pages (354–365, KDD 2025) match Crossref.
- Official authors: Weibo Gao, Qi Liu, Rui Li, **Yuze Zhao, Hao Wang, Linan Yue, Fangzhou Yao, Zheng Zhang**.
- Bib authors after Rui Li are wrong: Hao Zhao, Zhenya Wang, Xing Yue, Jianhui Yao, Mi Zhang.

### C3 — KT076 / KGNN-KT (pages, missing DOI)

- Official Springer CCIS: DOI `10.1007/978-981-96-9986-5_12`, pages **137–147** (ICIC 2025).
- Bib: pages `1--12`, no DOI.

### C4 — Piech_DKT_2015 (author)

- Official NeurIPS 2015 list includes **Mehran Sahami**.
- Bib has **Amit Sahai** instead. No Crossref DOI (NeurIPS 2015); pages 505–513 are consistent with secondary records.

## Spot-checked OK (this pass)

- `KT050_GraphCA_2023` DOI `10.1109/JAS.2023.123678` is a real IEEE/CAA JAS record (vol. 10, no. 11, pp. 2108–2123).
- `Zhang_DKVMN_2017` DOI `10.1145/3038912.3052580` is the WWW 2017 record; PDF not deposited.
- `Shen_KTSurvey_2024` DOI `10.1109/TLT.2024.3383325` unchanged.
- `KT077_R2GCurL_2026` DOI `10.1145/3818614` resolves on Crossref (ACM TOIS).

## Not a submission blocker by itself

IEEE TLT will still compile. C1–C4 are bibliography accuracy issues a reviewer can catch. Fix bib to publisher records before upload if time allows; do not invent a second DC-SSL paper.
