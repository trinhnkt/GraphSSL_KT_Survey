# B11 — Reference verification

**Date:** 2026-11-13. **Source checked:** Crossref REST API (`https://api.crossref.org/works/{doi}`) for every DOI in `12_manuscript/TLT/references.bib`, plus the JEDM landing page and the deposited PDF for the Xu survey, which has no DOI.
**Not done:** no locked file edited; N, N_G, N_S, and the 0/37 and 1/37 counts unchanged. DyGKT was not removed. P0 was not cited.

Table: `tables/B11_REFERENCE_VERIFICATION.csv` (47 printed entries; the IEEEtran control entry is not a reference and is omitted). Raw Crossref extracts: `audit/_b11_crossref/`.

## Result

| Status | Count | Meaning |
|---|---:|---|
| PASS | 34 | DOI resolves, and title, year, authors, volume/issue, and pages match. The venue is the abbreviated form of the Crossref container title. |
| PASS_WITH_NOTE | 7 | DOI resolves. A date or page form differs, and the bibliography was left as recorded. See below. |
| PASS_PUBLISHER_PAGE | 1 | Xu et al., no Crossref DOI. Confirmed from the publisher page and the PDF header. |
| NEEDS_EXTERNAL_VERIFICATION | 5 | No DOI, or Crossref has only an early-access record. |

## Priority items named in the review

| Printed no. | Item | Result |
|---|---|---|
| [8] | Liu et al., IEEE TKDE 2025 | PASS. DOI `10.1109/TKDE.2025.3552759`. Vol. 37, no. 8, pp. 4512–4536, 2025. |
| [9] | Xu et al., JEDM | PASS_PUBLISHER_PAGE. No DOI. Landing page confirms title, four authors, and publication on 2026-07-19. The PDF header reads *Journal of Educational Data Mining*, Volume 18, No. 2, 2026. The file has 47 pages, which matches pp. 41–87. |
| [32]–[43] | KT056 through KT076, the 2025 block | PASS, except [39] KT067 and [41] KT069, which are PASS_WITH_NOTE on the issue year (below). |
| [43] | KGNN-KT | PASS. DOI `10.1007/978-981-96-9986-5_12`. ICIC 2025, pp. 137–147. |
| [44] | R²GCurL | DOI `10.1145/3818614` resolves to this paper in *ACM Transactions on Information Systems*, vol. 44, no. 6, pp. 1–32, 2026. Authors match. The title command in the bibliography was broken (a tab had removed the backslash in `\textsuperscript`), so the printed list showed `exttwosuperior`. Corrected in `references.bib` and in the three `.bbl` files. |
| [45] | STSKT / streaming KT, DASFAA 2026 | PASS. DOI `10.1007/978-981-92-0375-8_9` resolves to this chapter, Lecture Notes in Computer Science, pp. 136–153, 2026. The `978-981-92` prefix is the registered Springer chapter DOI, not an unmatched string. |

## Left unchanged, with the reason

- **KT016 [15].** Crossref spells the fourth author `Hunag`. The bibliography keeps `Huang`.
- **KT029 [18].** Bibliography uses ACM article numbers `78:1--78:24`. Crossref records pages 1–24 of the same article (vol. 42, no. 3).
- **KT031 [19], KT052 [30], KT067 [39], KT069 [41].** Crossref `issued` date is a year earlier than the bibliography year. Volume, issue, and pages match where Crossref has them. The bibliography year was not replaced by the online date.
- **KT033 [20], DGMN.** Crossref returns early access only (2022, pp. 1–13, no volume). The bibliography cites the final issue, *IEEE TKDE*, vol. 35, no. 8, pp. 7844–7855, 2023. That final pagination was not overwritten from the early-access record. Status: `NEEDS_EXTERNAL_VERIFICATION` if a fresh publisher page is required before submission.

## No DOI, not re-fetched in this pass

Piech et al. 2015 [1], Pandey and Karypis 2019 [2], Liu et al. pyKT 2022 [7], and the Cursor software entry [47]. Each already has a URL in the bibliography. Their pages were not opened in this pass, so they stay `NEEDS_EXTERNAL_VERIFICATION`.

## Bibliography edit

One edit: the R²GCurL title markup, in `12_manuscript/TLT/references.bib` and the three compiled `.bbl` files (`main_tlt_anonymous.bbl`, `main_tlt_full.bbl`, `manuscript_TLT_FORMATTED_v1.3.bbl`). No other reference field was changed.

Stop. B11 is not a submission clearance for the five unverified rows.
