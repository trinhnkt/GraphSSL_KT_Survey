# Format compare (2026-11-24)

## Available local reference

Compared manuscript elements to:

`15. Check list/IEEE-Transactions-LaTeX2e-templates-and-instructions/New_IEEEtran_how-to.pdf`

(Cover letter already states this comparison.)

| Element | IEEEtran how-to expectation | Manuscript status |
|---|---|---|
| Class | IEEEtran journal | `\documentclass[lettersize,journal]{IEEEtran}` |
| Title / authors / thanks | Present | Anonymous: Anonymous Authors + TLT thanks; Full: 5 authors + ORCID footnotes |
| Abstract | Single abstract block | Yes |
| Index Terms / keywords | Present | `\begin{IEEEkeywords}` |
| Two-column body | Yes | Yes |
| Bibliography | IEEEtran.bst | `references.bib` + IEEEtran |
| Bios | After refs on full copy | Present on full/formatted |
| Invented received dates | Avoid | Not invented |

## TLT-instructions-only.pdf

Named on [TLT Author Resources](https://ieee-edusociety.org/publication/tlt/tlt-author-resources) inside the **TLT Word / LaTeX ZIP** from the IEEE Template Selector.

- Not present in this repo.
- Direct zip URL attempt from EduSociety returned 404.
- **Author action:** download TLT package via Template Selector → open `TLT-instructions-only.pdf` → 5-minute visual side-by-side with `main_tlt_anonymous.pdf` (margins, abstract label, keyword label, figure caption style).

Until that file is obtained, format readiness rests on IEEEtran how-to + compiled 18-page Transactions look (acceptable interim; TLT still urges the TLT-specific PDF).
