# IEEE TLT reference-format alignment — 2026-09-20

TLT Author Resources require citations/references to be fully compliant with the
[IEEE Reference Guide](https://journals.ieeeauthorcenter.ieee.org/wp-content/uploads/IEEE-Reference-Guide.pdf).
Style engine: `IEEEtran.bst` 1.14 + `\bibliographystyle{IEEEtran}`.

## Changes applied to `12_manuscript/TLT/references.bib`

1. **Title acronyms braced** so IEEEtran sentence-case does not print `Gikt` / `Cmkt` / etc.  
   Examples: `{GIKT}`, `{Bi-CLKT}`, `{DGEKT}`, `{DyGKT}`, `{CMKT}`, `{SINKT}`, `{R²GCurL}`, …
2. **Conference names abbreviated** per IEEE Reference Guide (`Proc.`, `Int.`, `Conf.`, omit “of the” / “on”).  
   Examples: `Proc. IEEE Int. Conf. Data Mining (ICDM)`, `Adv. Neural Inf. Process. Syst. (NeurIPS)`.
3. **Journal abbreviations** kept IEEE-style (`IEEE Trans. Learn. Technol.`, `Inf. Process. Manag.`, …).
4. **Article-number paper (KT069)** uses `note = {{Art. no.} 10}` (IEEEtran.bst 1.14 has no `articlenumber` field).
5. **Online locator** remains `url = {https://doi.org/...}` → IEEE `[Online]. Available:` (doi field retained for audit).
6. **AI disclosure cite**: Acknowledgment now cites `Cursor_AI_2026` (IEEE AI-generated-text policy).

## Rebuild

- `manuscript_TLT_FORMATTED_v1.3.pdf` — 14 pages  
- `main_tlt_anonymous.pdf` + title-named full/anonymous PDFs refreshed

## Not changed (already compliant / intentional)

- Author list truncation: BSTCTL forced et al. after 6 names  
- Metadata content previously live-checked 2026-09-15 (Crossref)
