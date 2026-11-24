# D — Kappa package check (2026-09-13)

**Decision: NOT_COMPLETED.** No Cohen's \(\kappa\) is reported in the manuscript.

Do not treat `08_quality_reliability/INTER_RATER_RELIABILITY_REPORT_v1.0.md` as a completed reliability package. Do not upload that file.

## Protocol target (`SLR_PROTOCOL_v1.0_LOCKED.md`)

| Step | Requirement |
|---|---|
| §20.1 Title/abstract | 25% random sample of deduplicated records + all `UNCERTAIN` |
| §20.2 Full-text | All `EXCLUDE_FULLTEXT` / `UNCERTAIN` second-checked; \(\ge 25\%\) of full-text decisions double-screened |
| §21 Coding | Independent double-code \(\max(20, 25\%\times N_{\mathrm{CORE}})\). For \(N=37\): **20 papers**, stratified |
| Report | Sample size, raw agreement, \(\kappa\), disagreement categories, consensus process |
| Files named in §25 | `inter_rater_screening.csv`, `inter_rater_fulltext.csv`, `inter_rater_coding.csv` |

## What is in the repository

| Artifact | What it is | Enough for \(\kappa\)? |
|---|---|---|
| `08_quality_reliability/QUALITY_ASSESSMENT_AUDIT_v1.0.csv` | Single-pass QA1–QA8 (no `coder_id`, no coder B) | No |
| `08_quality_reliability/inter_rater_template.csv` | Header only | No |
| `08_quality_reliability/disagreement_log_template.csv` | Header only | No |
| Pilot `*_ADJUDICATION_*.md` | Codebook debug; KT004 is an **AI second-pass**, not human–human IRR (`08_quality_reliability/README.md`) | No |
| `INTER_RATER_RELIABILITY_REPORT_v1.0.md` | Claims \(\kappa=0.882/0.895/\ldots\), \(188/750\), \(42/140\), 12 of 42 papers | **No pair-level table.** Uses \(N_{\mathrm{CORE}}=42\), not the locked 37. No coder IDs. |

Those printed \(\kappa\) values are **not** copied into the manuscript.

## Missing (blocks D)

1. Named second human screener/coder and independent decisions.
2. The three protocol CSVs with paired labels.
3. The 20-paper double-code sample list (stratified Graph / SSL / both / sparse).
4. A \(\kappa\) computed from those pairs.

Completing D requires that human double-coding work. It cannot be filled from the existing single-coder QA sheet or from the v1.0 IRR narrative.

## Manuscript

Threats §IX.A states the protocol targets and that the \(\kappa\) package was **not** completed. The unsupported “second coder on a 20% sample” clause is removed (no 20% pair file exists).
