# TLT template comparison — 2026-09-13

Compared:
- Manuscript: `manuscript_TLT_FORMATTED_v1.3.tex` / 12-page PDF
- In-repo IEEE Transactions sample: `15. Check list/IEEE-Transactions-LaTeX2e-templates-and-instructions/bare_jrnl_new_sample4.tex` + `IEEEtran.cls` V1.8b
- Official TLT Author Resources (IEEE Education Society)

Not compared: `TLT-instructions-only.pdf` (IEEE Template Selector only; not in this repo).

## Class and layout

| Element | TLT / IEEE journal sample | This manuscript | Verdict |
|---|---|---|---|
| Class | `[lettersize,journal]{IEEEtran}` V1.8b | Same class, same `IEEEtran.cls` V1.8b | Match |
| Society option | TLT is Education Society, **not** `compsoc` | No `compsoc` | Correct |
| Body type | 10 pt journal two-column letter | Same (log: 10 point, letter) | Match |
| Page cap (Survey and Tutorial, from 1 Jan 2025) | 18 double-column pages | 12 | Under cap |
| `\IEEEpubid` + received dates | Sample has placeholders | Omitted (do not invent) | Correct for first submit |
| `\markboth` | Sample invents Vol/No/Date | Journal name + running author title; no fake volume | Correct for first submit |
| Abstract + `IEEEkeywords` | After `\maketitle` | Same | Match |
| `\IEEEPARstart` | Yes | Yes | Match |
| Bibliography | `IEEEtran.bst` | `IEEEtran.bst` + `references.bib` | Match |
| Biographies | Photo optional (`IEEEbiography` / `nophoto`) | All `IEEEbiographynophoto` | Allowed |
| ORCID | Required for all authors | All five in `\thanks` | Match |
| AI text | Disclose in acknowledgments; cite the system | `\section*{Acknowledgment}` names Cursor and cites `Cursor_AI_2026` (v1.5.6) | Match (named system) |

## Packages vs sample

Sample uses: `amsmath`, `amsfonts`, `array`, `subfig`, `textcomp`, `url`, `graphicx`, `cite` (+ optional `algorithm`, `stfloats`).

Manuscript adds: `booktabs`, `multirow`, `xcolor`, `hyperref`, `balance`, `fontenc`/`inputenc`. Extra packages are common; production may strip `hyperref`. `\usepackage{balance}` is unused (no `\balance`).

Log warning: unused global option `[lettersize]` — the official sample uses the same option.

## Residual (author must do)

1. Download TLT package from IEEE Template Selector and compare the PDF **side-by-side** with `TLT-instructions-only.pdf` (headers, copyright line, biography spacing).
2. Optional: name the AI system in the acknowledgment if IEEE policy is applied strictly.
3. Photos can wait until acceptance.

This comparison is **not** a substitute for the official TLT-instructions-only visual check.
