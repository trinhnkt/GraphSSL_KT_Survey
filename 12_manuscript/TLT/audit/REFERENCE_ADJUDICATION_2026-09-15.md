# Reference metadata adjudication — 2026-09-15

Scope: all **47 cited** keys in `12_manuscript/TLT/references.bib` against live Crossref (DOI rows) + official proceedings/JEDM pages (NO_DOI rows).

Live scan: `REFERENCE_LIVE_CHECK_2026-09-15.json` / `REFERENCE_FULL_CHECK_2026-09-15.md`.

## Verdict

| Outcome | Count | Notes |
|---|---:|---|
| Crossref OK (title/authors/year/venue/DOI) | 39 | No action |
| KEEP as known Crossref vs print mismatch | 2 | ACM article-number style; IEEE print pagination |
| FIXED this pass | 3 | See below |
| NO_DOI verified OK via official source | 4 | Piech, Pandey, Liu_pyKT, Cursor |
| DOI added (was NO_DOI) | 1 | Xu_GbKT Zenodo DOI |

**No wrong paper identity** (title/authors swapped) was found among cited keys.

## Fixes applied to `references.bib` (2026-09-15)

| Key | Field | Was | Now | Evidence |
|---|---|---|---|---|
| `KT079_STGSKT_2026` | pages | `150--162` | `136--153` | Crossref / Springer chapter DOI `10.1007/978-981-92-0375-8_9` |
| `KT029_DGEKT_2024` | pages | `78:1--78:25` | `78:1--78:24` | PolyU hub: article 78, pp. 1–24; Xu JEDM cites `78:1–78:24` |
| `Xu_GbKT_2026` | doi | *(missing)* | `10.5281/zenodo.21443288` | JEDM citation meta `DC.Identifier.DOI` |
| `Liu_pyKT_2022` | pages | *(empty)* | `18542--18555` | NeurIPS / Xu JEDM citation of pyKT |

## CHECK rows adjudicated (keep)

### `KT029_DGEKT_2024` — KEEP ACM article-number style

- Title, authors, year 2024, TOIS 42(3), DOI `10.1145/3638350`: **OK**
- Crossref reports `page=1-24` (within-article); ACM style is `78:1--78:24` (article number 78)
- After fix, pages align with 24-page article length

### `KT033_DGMN_2023` — KEEP IEEE **print** citation

- Title, authors, DOI `10.1109/TKDE.2022.3206447`: **OK**
- Bib: TKDE **35**(8): **7844--7855**, year **2023** (IEEE CSDL / researchr / Xu JEDM all agree)
- Crossref still stores early-access stub (year 2022, page 1–13, empty volume) — **do not overwrite print metadata with Crossref stub**

## NO_DOI rows verified

| Key | Title / authors / year / venue / pages | Source |
|---|---|---|
| `Piech_DKT_2015` | Deep Knowledge Tracing; Piech et al.; 2015; NeurIPS 28; 505–513 | NeurIPS proceedings / Stanford geometry page |
| `Pandey_SAKT_2019` | A Self-Attentive Model for Knowledge Tracing; Pandey & Karypis; 2019; EDM; 384–389 | EDM 2019 / UMN Experts / ERIC |
| `Liu_pyKT_2022` | pyKT…; Liu et al.; 2022; NeurIPS Datasets & Benchmarks; **18542–18555** | NeurIPS abstract page; pages filled this pass |
| `Xu_GbKT_2026` | Survey…; Xu, Kujala, Metsämuuronen, Laakso; 2026; JEDM 18(2):41–87 | JEDM meta: volume 18, issue 2, pages 41–87; DOI Zenodo added |
| `Cursor_AI_2026` | Software @misc (Anysphere / cursor.com) | Intentional non-DOI cite |

## Prior fixes already in bib (2026-09-13)

Documented in `REFERENCE_FULL_CHECK_2026-09-13.md` / `H5_REFERENCE_NOTATION_AUDIT.md` (e.g. KT026 DOI `/219`, KT035, KT053, KT063, KT044 title). Not re-opened.

## Rebuild note

Bibliography-only changes; regenerate TLT PDF when packaging for Author Portal so the reference list shows corrected KT079 / DGEKT pages and Xu DOI.

**Done 2026-09-15:** rebuilt `manuscript_TLT_FORMATTED_v1.3.pdf` + `main_tlt_anonymous.pdf` (v1.6.17).
