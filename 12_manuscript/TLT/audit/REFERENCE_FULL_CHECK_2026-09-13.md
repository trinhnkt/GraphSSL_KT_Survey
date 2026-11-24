# Full bibliography live check — 2026-09-13

Source: `12_manuscript/TLT/references.bib` (44 cited works).
Method: Crossref works API for every DOI; official proceedings pages for the three no-DOI items. Raw JSON: `REFERENCE_LIVE_CHECK_2026-09-13.json`.

**All 44 records exist.** None is a fabricated paper.

## DOI coverage

| Class | Count | Keys |
|---|---|---|
| Official DOI (resolves) | 41 | All except the three rows below |
| No publisher DOI (proceedings URL used) | 3 | `Piech_DKT_2015`, `Pandey_SAKT_2019`, `Liu_pyKT_2022` |

NeurIPS 2015 / EDM 2019 / NeurIPS 2022 Datasets & Benchmarks do not assign Crossref DOIs. Official locators:

- Piech: https://proceedings.neurips.cc/paper/2015/hash/bac9162b47c56fc8a4d2a519803d51b3-Abstract.html
- Pandey: https://educationaldatamining.org/edm2019/proceedings/ (short paper 87)
- pyKT: https://proceedings.neurips.cc/paper_files/paper/2022/hash/75ca2b23d9794f02a92449af65a57556-Abstract-Datasets_and_Benchmarks.html

## Errors found and applied to the bib

| Key | Problem | Official record | Action |
|---|---|---|---|
| `KT026_PretrainQ_2020` | DOI `10.24963/ijcai.2020/216` is a **different** IJCAI 2020 paper (Rozenshtein & Sarne) | PEBG is paper 219: https://doi.org/10.24963/ijcai.2020/219 — Liu, Yang, Chen, Shen, Zhang, Yu; pp. 1577–1583 | DOI/URL → `/219` |
| `KT035_HHSKT_2023` | `10.1016/j.eswa.2023.119334` **404** | https://doi.org/10.1016/j.eswa.2022.119334 — Ni, Wei, Zhao, He, Zheng; ESWA 215:119334 (print Apr 2023) | DOI year 2023 → 2022 |
| `KT044_SINKT_2024` | Title shortened | ACM/Crossref: *SINKT: A Structure-Aware Inductive Knowledge Tracing Model with Large Language Model* | Title aligned; authors already correct |
| `KT053_GASKT_2021` | Authors **wrong** (Lixin Wang, Di Wu); pages 269–281 | Springer: Mengdan Wang, Chao Peng, Rui Yang, Chenchao Wang, Yao Chen, Xiaohua Yu; pp. 268–279; DOI unchanged | Authors + pages |
| `KT063_MAHKT_2025` | Three authors missing; vol. 309 | Crossref vol. **310**; authors add Shengze Hu, Jing Geng, Qiang Zhu | Authors + volume |

## Not errors (checked, left unchanged)

| Key | Flag | Why kept |
|---|---|---|
| `KT016_SKT_2020` | Crossref lists “Zhenya **Hunag**” | IEEE/author spelling is **Huang**; Crossref typo |
| `KT077_R2GCurL_2026` | Title HTML `<sup>2</sup>` vs LaTeX `R^{2}` | Same paper; authors match |
| `KT033_DGMN_2023` | Crossref issued 2022, pages 1–13 | Early-access deposit; bib keeps IEEE issue pagination vol. 35 no. 8 pp. 7844–7855 |
| Piech / Pandey | Title-search hit the wrong paper | Expected: no DOI. Official proceedings confirm authors and titles |

## Author/title match on the other 39

After the five fixes above, the remaining DOI entries match Crossref on family-name lists and titles (case/punctuation ignored). `Zhang_DKVMN_2017` DOI `10.1145/3038912.3052580` is the WWW 2017 record.

## What this check did not do

- Did not re-read every PDF first page (that is a separate `14_references/` deposit check).
- Did not treat old `VERIFIED_PUBLISHER` CSV labels as evidence.
