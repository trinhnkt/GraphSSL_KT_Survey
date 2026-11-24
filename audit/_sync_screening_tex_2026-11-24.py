# -*- coding: utf-8 -*-
from pathlib import Path

REPLACEMENTS = [
(
"""This paper reports identification, screening, eligibility, and inclusion in a PRISMA-style flow (Fig.~\\ref{fig:prisma_flow}) under the survey protocol. Identification $N_{\\mathrm{rec}}=2{,}017$ is the search-log sum; a record-level screening ledger is not deposited. We report a locator-assisted coding-sample $\\kappa$ and a separate independent-blind 20-paper $\\kappa$ (Sec.~\\ref{sec:icr}); we do not claim a completed screening or full-text reliability package.""",
"""This paper reports identification, screening, eligibility, and inclusion in a PRISMA-style flow (Fig.~\\ref{fig:prisma_flow}) under the survey protocol. Identification $N_{\\mathrm{rec}}=2{,}017$ is the search-log sum; a record-level screening ledger is not deposited. Screening agreement is available for the deposited independently double-screened subset, but not for the complete historical screening stages (Sec.~\\ref{sec:icr}). A locator-assisted coding-sample $\\kappa$ and a separate independent-blind 20-paper $\\kappa$ are reported for coded study attributes and are not pooled with screening agreement."""
),
(
"""Those stage counts are report arithmetic. The repository does not contain a 750-row title/abstract ledger, a deduplication ledger, or 98 row-level EC1--EC7 exclusion records. Title/abstract and full-text pair files named in the protocol are not present. The coded primary core is the \\textbf{37 primary-core papers} with deposited PDFs and coding tables.""",
"""Those stage counts are report arithmetic. The repository does not contain a 750-row title/abstract ledger, a deduplication ledger, or 98 row-level EC1--EC7 exclusion records. Deposited independently double-screened subset pair files are present for 11 title/abstract rows and 1 full-text row; they do not reconstruct the historical stages. The coded primary core is the \\textbf{37 primary-core papers} with deposited PDFs and coding tables."""
),
(
"""Screening and primary coding were carried out by an AI research assistant (a tool-using LLM agent) under the coding protocol; this is a methodological fact and not language polishing. The deposited title/abstract and full-text screening files (43 and 48 rows, seed-stage records rather than the 750-record ledger) list the assistant as both screener and reviewer, and no human second-screener file exists. Of the 45 coding-record files (pilot versions included), 41 name the assistant as coder. Documented human steps are limited to (i)~author verification of the inclusion identity of the 37 PDFs, (ii)~independent double-coding of a 20-paper sample by two human coders (Sec.~\\ref{sec:icr}) with adjudication of five cells to the adjudicated reference, and (iii)~PDF-level re-checks of three provenance records (Sec.~\\ref{sec:deviations}). Per-paper human verification of the remaining primary-coding fields is not documented. Consequently the primary coding is not an independent human judgment, the reported $\\kappa$ values measure agreement between human coders and an AI-generated, partly adjudicated reference, and an error shared by the assistant and a human coder would not be detected. The stage-level inclusion and exclusion decisions behind 750/140/103 cannot be audited at record level.""",
"""Screening and primary coding were carried out by an AI research assistant (a tool-using LLM agent) under the coding protocol; this is a methodological fact and not language polishing. The deposited title/abstract and full-text screening files (43 and 48 rows, seed-stage records rather than the 750-record ledger) list the assistant as both screener and reviewer. A human second screener later labeled a deposited independently double-screened subset (11 title/abstract rows and 1 full-text row) with primary decisions hidden; those pair files do not restore the historical 750-record ledger. Of the 45 coding-record files (pilot versions included), 41 name the assistant as coder. Documented human steps are limited to (i)~author verification of the inclusion identity of the 37 PDFs, (ii)~independent double-coding of a 20-paper sample by two human coders (Sec.~\\ref{sec:icr}) with adjudication of five cells to the adjudicated reference, (iii)~PDF-level re-checks of three provenance records (Sec.~\\ref{sec:deviations}), and (iv)~the deposited screening subset above. Per-paper human verification of the remaining primary-coding fields is not documented. Consequently the primary coding is not an independent human judgment, the reported coding $\\kappa$ values measure agreement between human coders and an AI-generated, partly adjudicated reference, and an error shared by the assistant and a human coder would not be detected. The stage-level inclusion and exclusion decisions behind 750/140/103 cannot be audited at record level."""
),
(
"""The survey protocol targets (i)~a 25\\% second-screener sample of deduplicated title/abstract records plus all uncertain records, (ii)~second review of all exclude at full text / uncertain full-text decisions and at least 25\\% of full-text eligibility decisions, and (iii)~double-coding of $\\max(20, 25\\%)$ primary-core papers (20 papers at $N=37$). Title/abstract and full-text pair files named in the protocol are not present. Inclusion identity of the 37 primary-core PDFs was verified by the authors. QA1--QA8 were assigned by the primary coder (an AI research assistant; Sec.~\\ref{sec:ai_role}). The 20-paper coding sample (all nine S-criterion papers, all five H1 S=N papers, plus six Graph-only coverage rows) was double-coded on eight fields.""",
"""The survey protocol targets (i)~a 25\\% second-screener sample of deduplicated title/abstract records plus all uncertain records, (ii)~second review of all exclude at full text / uncertain full-text decisions and at least 25\\% of full-text eligibility decisions, and (iii)~double-coding of $\\max(20, 25\\%)$ primary-core papers (20 papers at $N=37$).

\\textbf{Selection/screening reliability.} Screening agreement is available for the deposited independently double-screened subset, but not for the complete historical screening stages. On 11 of 42 deposited titled title/abstract rows ($11/42=26.2\\%$ of that deposited subset; not $11/750$), a human second screener independently labeled records with the primary decision hidden. Pre-adjudication raw agreement was $10/11$; Cohen's $\\kappa$ is undefined because the primary labels on this subset have no category variation. One full-text pair is deposited (REC\\_0047): primary \\texttt{EXCLUDE\\_FULLTEXT} versus second \\texttt{PRIMARY\\_ADJACENT\\_METHOD} (raw agreement $0/1$; $\\kappa$ undefined at $n=1$). Human adjudication of that disagreement, and legal full-text verification of the GKT-CD PDF, remain open. Pair tables are in the supplementary reliability package. These coefficients characterize the deposited independently double-screened subset and are not estimates of reliability for the full historical 750-record title/abstract stage or the 103 reported full-text exclusions.

\\textbf{Coding reliability.} Inclusion identity of the 37 primary-core PDFs was verified by the authors. QA1--QA8 were assigned by the primary coder (an AI research assistant; Sec.~\\ref{sec:ai_role}). The 20-paper coding sample (all nine S-criterion papers, all five H1 S=N papers, plus six Graph-only coverage rows) was double-coded on eight fields."""
),
(
"""    \\item \\textbf{Screening evidence.} The protocol requires a second-screener sample and record-level ledgers. They are not deposited, there is no second screener, and the 1{,}267/750/610/140/103 stage counts are report arithmetic (Sec.~\\ref{sec:ai_role}).""",
"""    \\item \\textbf{Screening evidence.} The protocol requires a second-screener sample and record-level ledgers for the reported stages. The historical 750-row ledger is still not deposited, so the 1{,}267/750/610/140/103 stage counts remain report arithmetic. A deposited independently double-screened subset (11 title/abstract pairs and 1 full-text pair) is now available and is reported separately (Sec.~\\ref{sec:icr})."""
),
(
"""    \\item \\textbf{Reliability recomputation.} Cohen's $\\kappa$ is undefined for three invariant all-no fields; they are excluded from the macro-average. The locator-assisted and independent passes are reported separately and are not pooled; no screening reliability exists.""",
"""    \\item \\textbf{Reliability recomputation.} Cohen's $\\kappa$ is undefined for three invariant all-no coding fields; they are excluded from the coding macro-average. The locator-assisted and independent coding passes are reported separately and are not pooled with each other or with the deposited screening-subset agreement."""
),
(
"""Future Graph/SSL-KT papers---and updates of this survey---should release split statements, graph-construction scripts or rules, calibration tables, and (for systematic reviews) pair-level inter-coder files. Screening and full-text second-screener pair files remain the open reliability task for the present protocol.""",
"""Future Graph/SSL-KT papers---and updates of this survey---should release split statements, graph-construction scripts or rules, calibration tables, and (for systematic reviews) pair-level inter-coder files. Deposited screening-subset pairs are now available; recovering reliability for the full historical 750/103 stages remains open because those ledgers are not deposited."""
),
(
"""\\textbf{Selection and coding reliability.} Identification $N_{\\mathrm{rec}}=2{,}017$ is from the search log; stage counts 750/140/103 are from the search-expansion report and are not backed by a deposited record-level ledger. QA1--QA8 were assigned by the primary coder (an AI research assistant; Sec.~\\ref{sec:ai_role}). Screening and full-text second-screener pair files are not in the repository. The 37 primary-core PDFs were identity-checked by the authors. The 20-paper coding sample reports field-wise Cohen's $\\kappa$ in Sec.~\\ref{sec:icr}: after excluding three invariant all-no fields for which $\\kappa$ is undefined ($p_e=1$), the locator-assisted mean over five defined $\\kappa$ values is $0.97$ ($158/160$ cells) and an independent pass by \\texttt{DaoMT} (no locator) yields mean $0.96$ over the same five defined fields ($157/160$). Those coefficients are not pooled. We release the coding schema, pair table, recomputed-$\\kappa$ sheet, QA scores, and sparse/cold-start fields as supplementary artifacts.""",
"""\\textbf{Selection reliability.} The historical screening stages are not backed by a complete record-level ledger, so selection reliability cannot be reconstructed for all reported title/abstract and full-text decisions. For this revision, we therefore report raw agreement and Cohen's $\\kappa$ only for the deposited records that received two independent screening decisions, with disagreements adjudicated separately. These coefficients characterize the available double-screened subset and should not be interpreted as reliability estimates for the full historical 750-record screening stage or the 103 reported full-text exclusions. They are also distinct from the 20-paper coding reliability analysis, which measures agreement on coded study attributes rather than inclusion/exclusion decisions.

\\textbf{Coding reliability.} QA1--QA8 were assigned by the primary coder (an AI research assistant; Sec.~\\ref{sec:ai_role}). The 37 primary-core PDFs were identity-checked by the authors. The 20-paper coding sample reports field-wise Cohen's $\\kappa$ in Sec.~\\ref{sec:icr}: after excluding three invariant all-no fields for which $\\kappa$ is undefined ($p_e=1$), the locator-assisted mean over five defined $\\kappa$ values is $0.97$ ($158/160$ cells) and an independent pass by \\texttt{DaoMT} (no locator) yields mean $0.96$ over the same five defined fields ($157/160$). Those coding coefficients are not pooled with each other or with screening agreement. We release the coding schema, screening-subset and coding pair tables, recomputed-$\\kappa$ sheet, QA scores, and sparse/cold-start fields as supplementary artifacts."""
),
]

targets = [
    Path(r"D:\TRINH\GraphSSL_KT_Survey\12_manuscript\TLT\main_tlt_full.tex"),
    Path(r"D:\TRINH\GraphSSL_KT_Survey\12_manuscript\TLT\manuscript_TLT_FORMATTED_v1.3.tex"),
]

for path in targets:
    text = path.read_text(encoding="utf-8")
    # Preserve newline style
    nl = "\r\n" if "\r\n" in text else "\n"
    working = text.replace("\r\n", "\n")
    for old, new in REPLACEMENTS:
        if old not in working:
            raise SystemExit(f"OLD not found in {path.name}: {old[:80]!r}")
        working = working.replace(old, new)
    # Verify absolute phrases removed
    for banned in [
        "no human second-screener file exists",
        "no screening reliability exists",
        "Title/abstract and full-text pair files named in the protocol are not present",
    ]:
        if banned in working:
            raise SystemExit(f"Banned phrase remains in {path.name}: {banned}")
    path.write_text(working.replace("\n", nl), encoding="utf-8")
    print("updated", path.name)
print("ok")
