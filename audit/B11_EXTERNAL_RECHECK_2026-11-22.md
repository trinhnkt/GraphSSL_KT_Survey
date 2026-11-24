# B11 external recheck — 2026-11-22

The 2026-11-13 file `audit/B11_REFERENCE_AUDIT.md` left five rows at `NEEDS_EXTERNAL_VERIFICATION`. This pass opened publisher or proceedings records for those rows. `12_manuscript/TLT/references.bib` was not edited. Counts are unchanged.

| Key | Bibliography pages | Result | Source opened |
| --- | --- | --- | --- |
| Piech_DKT_2015 | 505–513 | **PASS_PAGES** | NeurIPS abstract page confirms the title and the seven authors and does not print pages. The ACM proceedings record `10.5555/2969239.2969296` states pages 505–513. The author-lab page states the same range. The deposited PDF has 9 pages, which is the length of 505–513, and does not print those numbers. |
| Pandey_SAKT_2019 | 384–389 | **PASS_PAGES** | The ERIC full text of the EDM 2019 paper prints “pp. 384–389”. The University of Minnesota publication record states pages 384–389. The deposited PDF has 6 pages, which is the length of that range. |
| Liu_pyKT_2022 | 18542–18555 | **PASS_PAGES** | Crossref `10.52202/068431-1347`, publisher Neural Information Processing Systems Foundation, pages 18542–18555, the same six authors, 2022. The official NeurIPS PDF does not print the book page numbers. The deposited PDF has 14 pages, which is the length of that range. The proceedings DOI was not added to the bibliography; the existing NeurIPS URL stays the open copy. |
| KT033_DGMN_2023 | vol. 35, no. 8, pp. 7844–7855, 2023 | **NEEDS_EXTERNAL_VERIFICATION** | Crossref for `10.1109/TKDE.2022.3206447` was read again on 2026-11-22. It still records issued 2022, pages 1–13, and no volume. IEEE Xplore returned 403. The deposited PDF is marked “JOURNAL SUBMISSION” and is not the issue PDF. The final-issue line in the bibliography was not replaced. |
| Cursor_AI_2026 | no pages; URL `https://cursor.com` | **NEEDS_EXTERNAL_VERIFICATION** | The site was not opened in this pass. The bibliography entry was not changed. |

Three page ranges now match an external record. Two rows stay unverified. This recheck does not change `READY_FOR_SUBMISSION`. That flag stays NO because A1 and A3 still fail.
