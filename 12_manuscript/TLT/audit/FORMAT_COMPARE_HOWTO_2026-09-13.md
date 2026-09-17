# Format compare — 2026-09-13 (package A)

## What was available

| Artifact | Location | TLT-specific? |
|---|---|---|
| Word Selector download | `15. Check list/Transactions-template-and-instructions-on-how-to-create-your-article-formatted (4).docx` | No. Title: *Preparation of Articles for IEEE TRANSACTIONS and JOURNALS (2022)*. No *Learning Technologies* text. |
| LaTeX Selector family | `15. Check list/IEEE-Transactions-LaTeX2e-templates-and-instructions/` | No. Generic IEEEtran V1.8b (`bare_jrnl_new_sample4.tex`, `New_IEEEtran_how-to.pdf`). |
| `TLT-instructions-only.pdf` | Named on [TLT Author Resources](https://ieee-edusociety.org/publication/tlt/tlt-author-resources) | **Not in this repo.** Not inside the Word `.docx`. Not inside the generic LaTeX folder. IEEE Template Selector does not publish a stable permalink. |

Automated download from `https://template-selector.ieee.org/` was not completed in this pass (site is a click-through wizard; prior automation was blocked). The in-repo LaTeX folder is the same ZIP family the Selector returns for Transactions journals, including TLT (IEEEtran journal, not `compsoc`).

## What was compared

Manuscript: `manuscript_TLT_FORMATTED_v1.3.pdf` (13 pages, IEEEtran V1.8b `[lettersize,journal]`).

Instruction set used: `15. Check list/IEEE-Transactions-LaTeX2e-templates-and-instructions/New_IEEEtran_how-to.pdf` plus `bare_jrnl_new_sample4.tex`.

| Element | How-to / sample | Manuscript | Verdict |
|---|---|---|---|
| Class | `[journal]{IEEEtran}` V1.8b; sample uses `lettersize` | Same class file V1.8b | Match |
| Society | TLT is Education Society, not `compsoc` | No `compsoc` | Correct |
| Title / abstract / keywords | Title case; abstract after `\maketitle`; `IEEEkeywords` alphabetical | Keywords A–Z as of v1.5.6 | Match |
| Drop cap | `\IEEEPARstart` | Yes | Match |
| Copyright line | Not required at submission | Omitted | Match |
| Figures | `[!t]` | Three column figures `[!t]` | Match; page 5 is float-heavy |
| Bibliography | IEEEtran | `IEEEtran.bst` | Match |
| Biographies | Photo optional | `IEEEbiographynophoto` | Allowed |
| AI text | Disclose + cite the system | Cursor `\cite{Cursor_AI_2026}` | Match |

This record replaces the claim that a side-by-side with `TLT-instructions-only.pdf` is still an open author step **unless** that PDF later appears in a TLT-branded ZIP. Until then, the official instruction set in hand is `New_IEEEtran_how-to.pdf`.

## Portal

Submit on the IEEE TLT Author Portal (IEEE account). Do not use ScholarOne as the new-submission site.
