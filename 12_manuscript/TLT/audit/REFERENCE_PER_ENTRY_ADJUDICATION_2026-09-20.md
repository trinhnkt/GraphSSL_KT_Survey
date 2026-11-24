# Per-reference adjudication — 2026-09-20

Live Crossref + DOI HTTP + local PDF identity check of
`12_manuscript/TLT/references.bib` (47 entries; all manuscript cites covered).

**Method**
- Title / authors / year / volume / pages vs Crossref works API
- DOI resolve via `https://doi.org/…`
- Content identity: local `file=` PDF exists + title tokens / metadata / first-page text
- Not a full-text semantic review of scientific claims

**Artifacts**
- `REFERENCE_LIVE_CHECK_2026-09-20.json`
- `REFERENCE_PER_ENTRY_VERDICT_2026-09-20.csv`
- `REFERENCE_FULL_CHECK_2026-09-20.md` (machine draft)
- This file = human adjudication after machine flags

---

## Executive verdict

| Bucket | Count | Meaning |
|---|---:|---|
| PASS | 44 | Title + authors + year + DOI/URL + PDF identity OK |
| PASS_WITH_NOTES | 2 | Same paper; Crossref incomplete or no Crossref DOI |
| FAIL metadata | 0 | After adjudication / one bib fix |
| Fixed this pass | 1 | `Xu_GbKT_2026` — removed invalid Zenodo DOI |

**Overall: bibliography identity is sound for TLT submission** after the Xu DOI fix.

---

## Machine run summary (before adjudication)

| Status | Count |
|---|---:|
| OK | 40 |
| OK_SOFTWARE (`Cursor_AI_2026`) | 1 |
| CHECK | 2 (`KT033`, `KT077`) |
| NO_DOI | 3 (`Piech`, `Pandey`, `Liu_pyKT`) |
| DOI_FAIL | 1 (`Xu_GbKT` — invalid Zenodo DOI) |

---

## Adjudicated exceptions

### 1. `KT033_DGMN_2023` — PASS_WITH_NOTES (KEEP bib)

| Field | Bib | Crossref | Decision |
|---|---|---|---|
| Title | Deep Graph Memory Networks… | Match | PASS |
| Authors | Abdelrahman; Wang | Match | PASS |
| Year | **2023** | 2022 (incomplete record) | **KEEP 2023** |
| Volume/issue/pages | 35(8):7844–7855 | blank / 1–13 | **KEEP bib** |
| DOI | `10.1109/TKDE.2022.3206447` | Resolves | PASS |
| PDF | Present; title tokens on page | | PASS |

Evidence: IEEE print citation is widely used as 2023, TKDE 35(8):7844–7855 (also cited that way in Xu JEDM 2026). Crossref record for this DOI is incomplete (no volume/issue).

### 2. `KT077_R2GCurL_2026` — PASS (false machine TITLE flag)

| Field | Result |
|---|---|
| DOI `10.1145/3818614` | Crossref OK; ACM TOIS 44(6):1–32, 2026 |
| Authors | Peng et al. match Crossref |
| Title | Crossref has HTML `R<sup>2</sup>GCurL`; bib uses `{R{\texttwosuperior}GCurL}` — same paper |
| PDF page 1 | “R2GCurL: Reinforced Robust Knowledge Tracing…” + Tianhao Peng | PASS |

Machine `sim=0.00` was a **parser artifact** (nested braces / HTML), not a wrong paper.

### 3. `Xu_GbKT_2026` — PASS after fix

| Field | Before | After |
|---|---|---|
| DOI | `10.5281/zenodo.21443288` (**404** / not in Crossref) | **Removed** |
| URL | JEDM article 1089 | Kept |
| Title / authors / year | Match JEDM landing page (Published July 19, 2026) | PASS |
| Pages | 41–87, vol. 18 no. 2 | PASS |
| PDF | Present; title in metadata + text | PASS |

### 4. NO_DOI proceedings — PASS_NO_DOI

| Key | Official URL | PDF identity |
|---|---|---|
| `Piech_DKT_2015` | NeurIPS proceedings URL reachable | PDF title “Deep Knowledge Tracing” |
| `Pandey_SAKT_2019` | EDM 2019 proceedings URL reachable | PDF text contains “self-attentive” |
| `Liu_pyKT_2022` | NeurIPS 2022 DB track URL reachable | PDF text contains “pykt” |

No DOI is normal for these venues; not a metadata error.

### 5. `Cursor_AI_2026` — PASS (software cite)

IEEE AI disclosure cite; not a research paper. URL in howpublished.

### 6. `KT076_KGNNKT_2025` — PASS

DOI/Crossref OK. Local PDF is image-heavy (no extractable body text) but **metadata title = KGNN-KT…LLM-Extracted Knowledge Graphs** — identity OK.

---

## Dimension checklist (all cited entries)

| Dimension | Result |
|---|---|
| Tên bài (title) | PASS (47/47 after KT077/Xu adjudication) |
| Tên tác giả (authors) | PASS |
| Năm xuất bản (year) | PASS; KT033 KEEP print 2023 vs Crossref online 2022 note |
| Nội dung / đúng bài (PDF identity) | PASS; all `file=` PDFs present (0 missing) |
| Link DOI | PASS after removing Xu false Zenodo DOI; 3 intentional NO_DOI |

---

## Action taken

1. Removed invalid `doi = {10.5281/zenodo.21443288}` from `Xu_GbKT_2026`.
2. Added note: no Crossref DOI; publisher landing page used.
3. No other silent bib overwrites.

Rebuild bibliography/PDF after this fix before portal upload.
