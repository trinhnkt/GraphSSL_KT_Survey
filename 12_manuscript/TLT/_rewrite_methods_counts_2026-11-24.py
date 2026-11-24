# -*- coding: utf-8 -*-
"""Sync Methods/counts language to frozen N=44 audits."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FILES = [
    "main_tlt_anonymous.tex",
    "main_tlt_full.tex",
    "manuscript_TLT_FORMATTED_v1.3.tex",
]

REPS = [
    # Comparison table
    (
        r"37 PDFs; search-log $N_{\mathrm{rec}}=2{,}017$; no screening ledger",
        r"44 PDFs after full-text update; search-log $N_{\mathrm{rec}}=2{,}017$; no historical screening ledger",
    ),
    # Venue probe
    (
        r"The candidates (Supplementary Table~S-Files) are not coded and do not change $N=37$, $N_G$, $N_S$, or any $\kappa$; adding them would require full-text screening and coding under the coding protocol. The 37-paper core is therefore a deposited set and not a saturated census, and $N_S$ in particular may be understated.",
        r"The candidates (Supplementary Table~S-Files) are not coded into the expanded core and do not change $N=44$, $N_G$, $N_S$, or any $\kappa$; adding them would require full-text screening and coding under the coding protocol. The 44-paper core (original deposited set plus the Sec.~\ref{sec:gateway_ext} update) is therefore not a saturated census, and $N_S$ in particular may be understated.",
    ),
    # PRISMA inclusion paragraph
    (
        r"The coded primary core is the \textbf{37 primary-core papers} with deposited PDFs and coding tables. The legacy seed list of 34 core records is not a second inclusion total. Those export files are the record-level evidence a recall fraction would require, so no recall fraction for the 34 records is reported. The five expansion identifiers removed at corpus verification are KT078 and KT080--KT083 (Supplementary Table~S-PRISMA-5). Each had been marked for full-text inclusion and was then dropped because the deposited Crossref check of 2026-09-15 records that the claimed DOI did not resolve or resolved to a different paper; no matching PDF is in the reference deposit. \texttt{KT\#\#\#} labels are inventory identifiers from the seed list and a later expansion batch, not a numbering of the 140 full-text records or of the 37 included papers.",
        r"Those stage counts end at 37 on the original identification path. The coded primary core used in this paper is the \textbf{44 primary-core papers} after the Sec.~\ref{sec:gateway_ext} full-text update, with deposited PDFs and coding tables. The legacy seed list of 34 core records is not a second inclusion total. Those export files are the record-level evidence a recall fraction would require, so no recall fraction for the 34 records is reported. The five expansion identifiers removed at corpus verification are KT078 and KT080--KT083 (Supplementary Table~S-PRISMA-5). Each had been marked for full-text inclusion and was then dropped because the deposited Crossref check of 2026-09-15 records that the claimed DOI did not resolve or resolved to a different paper; no matching PDF is in the reference deposit. \texttt{KT\#\#\#} labels are inventory identifiers from the seed list and a later expansion batch, not a numbering of the 140 full-text records or of the 44 included papers.",
    ),
    (
        r"A record-level screening ledger is not deposited. $N=37$ primary-core papers.}",
        r"A record-level screening ledger is not deposited. Original-path arithmetic ends at 37; coded core after Sec.~\ref{sec:gateway_ext} is $N=44$.}",
    ),
    # AI role
    (
        r"(i)~author verification of the inclusion identity of the 37 PDFs, (ii)~independent double-coding of a 20-paper sample by two human coders (Sec.~\ref{sec:icr}) with adjudication of five cells to the adjudicated reference, (iii)~PDF-level re-checks of three provenance records (Sec.~\ref{sec:deviations}), and (iv)~the deposited screening subset above.",
        r"(i)~author verification of the inclusion identity of the 44 PDFs, (ii)~independent double-coding of a 20-paper sample by two human coders (Sec.~\ref{sec:icr}) with adjudication of five cells to the adjudicated reference, (iii)~PDF-level re-checks of seven provenance records plus KT085 display lock (Sec.~\ref{sec:deviations}), (iv)~human adjudication of the deposited full-text disagreement REC\_0047, and (v)~the deposited screening subset above.",
    ),
    # QA7 methodology
    (
        r"QA7 scores how informative the evaluation design is for RQ4. It applies to all 37 primary-core papers because RQ4 asks how well each protocol supports sparse-concept inference, not because every author claimed to solve cold-start. The survey protocol permits QA7 to be coded not applicable when a paper makes no sparse or cold-start claim; this survey does not use that option, so the applicable maximum remains $16$.",
        r"QA7 scores how informative the evaluation design is for RQ4. It applies to all 44 primary-core papers because RQ4 asks how well each protocol supports sparse-concept inference, not because every author claimed to solve cold-start. The survey protocol permits QA7 to be coded not applicable when a paper makes no sparse or cold-start claim; this survey does not use that option, so the applicable maximum remains $16$.",
    ),
    (
        r"Two review variables are kept separate from QA7. They are a coarse overlay from sparse-protocol category, not a new abstract-level recode of all 37 papers. Claim values use code values in Supplementary Table~S-Tokens. KT035 (HHSKT) is the documented exception: its protocol category remains interaction sparsity only, but the paper reports an interaction-drop evaluation, so the overlay is not a generic 80/20 split. The 37-row file is Supplementary Table~S-Files.",
        r"Two review variables are kept separate from QA7. They are a coarse overlay from sparse-protocol category, not a new abstract-level recode of all 44 papers. Claim values use code values in Supplementary Table~S-Tokens. Interaction-drop evaluation is YES for HCMKT only; HHSKT is sparse-only under the locked decision table. The 44-row expanded file is Supplementary Table~S-Files.",
    ),
    (
        r"""35 & Standard interaction split \\
1 & Interaction-drop (HHSKT) \\
1 & Item cold-start (SINKT) \\
0 & Strict KC cold-start \\""",
        r"""40 & Standard interaction split \\
1 & Interaction-drop (HCMKT) \\
1 & Item cold-start (SINKT) \\
2 & Learner cold-start (SGKT, CoSKT) \\
0 & Strict KC cold-start \\""",
    ),
    (
        r"QA7 is applicable on every row of that overlay. Generic data sparsity is YES on all 37 rows of the deposited sparse file, so that field does not separate papers and is not used as a synthesis variable.",
        r"QA7 is applicable on every row of that overlay. Generic data sparsity does not separate papers under the locked decision table and is not used as a synthesis variable.",
    ),
    # ICR
    (
        r"(iii)~double-coding of $\max(20, 25\%)$ primary-core papers (20 papers at $N=37$).",
        r"(iii)~double-coding of $\max(20, 25\%)$ primary-core papers (20 papers; the sample was fixed before the Sec.~\ref{sec:gateway_ext} update to $N=44$).",
    ),
    (
        r"One full-text pair is deposited (REC\_0047): primary \texttt{EXCLUDE\_FULLTEXT} versus second \texttt{PRIMARY\_ADJACENT\_METHOD} (raw agreement $0/1$; $\kappa$ undefined at $n=1$). Human adjudication of that disagreement, and legal full-text verification of the GKT-CD PDF, remain open. Pair tables are in the supplementary reliability package.",
        r"One full-text pair is deposited (REC\_0047): primary \texttt{EXCLUDE\_FULLTEXT} versus second \texttt{PRIMARY\_ADJACENT\_METHOD} (raw agreement $0/1$; $\kappa$ undefined at $n=1$). Human adjudication by Nguyen Van Hau set the final decision to \texttt{PRIMARY\_ADJACENT\_METHOD} (COMPLETED); the paper is not in the primary core. Pair tables are in the supplementary reliability package.",
    ),
    (
        r"Inclusion identity of the 37 primary-core PDFs was verified by the authors.",
        r"Inclusion identity of the 44 primary-core PDFs was verified by the authors.",
    ),
    # Deviations
    (
        r"The eight-value graph provenance field is reported as three display tokens; 24 of 36 records map to the displayed code, five differ with a documented PDF-level adjudication, and seven differ without one (Sec.~\ref{sec:graph_provenance}, Appendix~\ref{app:provenance}). TSKT was recoded from external fixed graph to model-defined fixed graph after a PDF check; the earlier Capsule GNN coding-file value external fixed graph is superseded; SKT stays in the model-defined bin although its PDF is mixed.",
        r"The eight-value graph provenance field is reported as three display tokens on the expanded Graph-KT set ($N_G=40$): model-defined fixed $24$, external fixed $7$, dynamically learned $9$, unclear $0$ (Sec.~\ref{sec:graph_provenance}, Appendix~\ref{app:provenance}; \texttt{PROVENANCE\_COUNTS\_LOCKED}). Seven PDF-level provenance re-reads plus the KT085 display lock are deposited. TSKT was earlier recoded from external fixed graph to model-defined fixed graph after a PDF check; SKT stays in the model-defined bin although its PDF is mixed.",
    ),
    (
        r"Re-auditing the SSL criterion reduced $N_S$ from 14 to 9. SINKT, Coda, KGNN-KT, R$^2$GCurL, and STSKT were removed from SSL coding and remain in the corpus as Graph-KT; $N=37$ is unchanged. The exclusive pretext family values are the four family codes (Supplementary Table~S-Tokens); an earlier ``seven families'' count used display aliases.",
        r"Re-auditing the SSL criterion reduced $N_S$ from 14 to 9 on the pre-expansion core. SINKT, Coda, KGNN-KT, R$^2$GCurL, and STSKT were removed from SSL coding and remain Graph-KT. After the Sec.~\ref{sec:gateway_ext} update, $N_S=16$ and $N_{G\cap S}=12$. The exclusive pretext-family table on the pre-expansion SSL set used four family codes (Supplementary Table~S-Tokens); an earlier ``seven families'' count used display aliases.",
    ),
    (
        r"The deposited Supplementary Table~S-Files carried a interaction-drop evaluation column that was YES for all 37 rows, contradicting the body and the H2 overlay (HHSKT only). Version v1.9 sets it to YES for HHSKT only, drops the constant generic-sparsity column, and keeps the deposited file unchanged. The new NO values reflect the H2 overlay and were not re-read from the PDFs.",
        r"An earlier deposited sparse file carried an interaction-drop column that was YES for all rows. The locked expanded coding sets interaction-drop YES for HCMKT only, item cold-start YES for SINKT only, learner cold-start YES for SGKT and CoSKT, and strict KC cold-start YES for $0/44$ (Sec.~\ref{sec:sparse_coldstart}). HHSKT is NO on all four constructs under the decision table.",
    ),
    # Provenance body
    (
        r"Paper-level coding of the 36 Graph-KT studies uses a three-token display collapse of the codebook graph provenance field (Table~\ref{tab:prov_encoder}). Counts are unique papers, not GKT Dense/Transition variants. Display model-defined fixed graph includes architecture-defined, Q-matrix, and log-derived \emph{fixed} graphs; it does not mean the graph was independent of interaction logs.",
        r"Paper-level coding of the 40 Graph-KT studies uses a three-token display collapse of the codebook graph provenance field (Table~\ref{tab:prov_encoder}). Counts are unique papers, not GKT Dense/Transition variants. Display model-defined fixed graph includes architecture-defined, Q-matrix, and log-derived \emph{fixed} graphs; it does not mean the graph was independent of interaction logs.",
    ),
    (
        r"\item \textbf{model-defined fixed graph ($n=19/36$, 52.8\%)}:",
        r"\item \textbf{model-defined fixed graph ($n=24/40$, 60.0\%)}:",
    ),
    (
        r"\item \textbf{external fixed graph ($n=8/36$, 22.2\%)}:",
        r"\item \textbf{external fixed graph ($n=7/40$, 17.5\%)}:",
    ),
    (
        r"\item \textbf{dynamically learned graph ($n=9/36$, 25.0\%)}:",
        r"\item \textbf{dynamically learned graph ($n=9/40$, 22.5\%)}:",
    ),
    (
        r"\textbf{Sub-bins of the displayed model-defined fixed graph code.} That code mixes three construction logics, so we split its 19 papers by a deterministic rule on the recorded graph source token and the per-paper eight-value record: \emph{Q-matrix/expert-authored} ($n=3$: GIKT, PEBG, GASKT; graph taken from the exercise--KC annotation only), \emph{log-derived} ($n=10$; any component derived from interaction logs, including GKT's transition graph, or an eight-value record of precomputed graph, split unclear), and \emph{architecture-defined} ($n=6$: HHSKT, TSKT, GraphCA, Capsule GNN, MG-Ensemble, CS-GKT; the remainder). The rule is applied to coding records; it was not re-read from the PDFs. Log-derived graphs are the ones for which a train-only construction statement matters (Sec.~\ref{sec:graph_kt}).",
        r"\textbf{Sub-bins of the displayed model-defined fixed graph code.} That code mixes three construction logics. On the pre-expansion model-defined records a deterministic rule on the recorded graph source token yielded \emph{Q-matrix/expert-authored} ($n=3$: GIKT, PEBG, GASKT), \emph{log-derived} ($n=10$), and \emph{architecture-defined} ($n=6$: HHSKT, TSKT, GraphCA, Capsule GNN, MG-Ensemble, CS-GKT). That sub-bin split was not re-derived for the expansion papers that enter the locked $24/40$ model-defined count. Log-derived graphs are the ones for which a train-only construction statement matters (Sec.~\ref{sec:graph_kt}).",
    ),
    # SSL opening
    (
        r"Nine of the 37 primary-core papers satisfy the S-criterion (a self-generated pretext or consistency target). Five other Graph-KT papers (SINKT, Coda, KGNN-KT, R$^2$GCurL, STSKT) satisfy the G-criterion but not the S-criterion: they use inductive, denoising, LLM-graph, curriculum/RL, or streaming-graph mechanisms without a self-generated pretext or consistency target. Fig.~\ref{fig:ssl_framework} illustrates pretext-family axes used in this survey.",
        r"Sixteen of the 44 primary-core papers satisfy the S-criterion (a self-generated pretext or consistency target); twelve of those also satisfy the G-criterion ($N_{G\cap S}=12$). Five Graph-KT papers (SINKT, Coda, KGNN-KT, R$^2$GCurL, STSKT) satisfy the G-criterion but not the S-criterion: they use inductive, denoising, LLM-graph, curriculum/RL, or streaming-graph mechanisms without a self-generated pretext or consistency target. Fig.~\ref{fig:ssl_framework} illustrates pretext-family axes used in this survey.",
    ),
    (
        r"The 9 SSL-KT manuscripts \emph{report} that pretext objectives regularize representations under interaction sparsity.",
        r"The 16 SSL-KT manuscripts \emph{report} that pretext objectives regularize representations under interaction sparsity.",
    ),
    # Cold-start constructs
    (
        r"SINKT \cite{KT044_SINKT_2024} evaluates a one-quarter \emph{question} hold-out and is coded YES for item cold-start, not for zero-exposure KC. HHSKT \cite{KT035_HHSKT_2023} evaluates interaction-drop sparsity and is coded no for strict KC cold-start.",
        r"SINKT \cite{KT044_SINKT_2024} evaluates a one-quarter \emph{question} hold-out and is coded YES for item cold-start, not for zero-exposure KC. HCMKT \cite{HCMKT_2026} evaluates interaction-drop sparsity and is coded no for strict KC cold-start. HHSKT is NO on all four constructs under the locked decision table.",
    ),
    (
        r"Learner cold-start & Test learners have no or truncated history and are scored separately & Learner-level split with full histories & 0 \\",
        r"Learner cold-start & Test learners have no or truncated history and are scored separately & Learner-level split with full histories & 2 \\",
    ),
    (
        r"It is coded no for a zero-exposure KC split. HHSKT \cite{KT035_HHSKT_2023} is coded no for strict KC cold-start (interaction-drop sparsity only) and is not treated here as an inductive cold-start evaluation.",
        r"It is coded no for a zero-exposure KC split. HCMKT \cite{HCMKT_2026} is the interaction-drop paper and is not treated here as an inductive cold-start evaluation. HHSKT is sparse-only under the locked decision table.",
    ),
    (
        r"\textbf{KT035} & HHSKT \cite{KT035_HHSKT_2023} & Sparse only & \textbf{NO} & NO & NO & Interaction-drop; not strict KC \\",
        (
            r"\textbf{KT035} & HHSKT \cite{KT035_HHSKT_2023} & Sparse only & \textbf{NO} & NO & NO & Sparse only; drop claim superseded \\"
            + "\n"
            + r"\textbf{KT086} & HCMKT \cite{HCMKT_2026} & Interaction-drop & \textbf{NO} & NO & NO & Drop rates 20/40/60\% \\"
            + "\n"
            + r"\textbf{KT023} & SGKT \cite{KT023_SGKT_2022} & Learner CS & \textbf{NO} & NO & YES & Truncated history groups \\"
            + "\n"
            + r"\textbf{KT087} & CoSKT \cite{CoSKT_2024} & Learner CS & \textbf{NO} & NO & YES & Sequences shorter than 50 \\"
        ),
    ),
    # Sensitivity + compute
    (
        r"\textbf{Sensitivity to QA7 applicability.} The survey protocol allows QA7 to be coded not applicable when a paper makes no sparse or cold-start claim. Of the 37 papers, only HHSKT and SINKT make such a claim (Table~\ref{tab:sparse_taxonomy}). Recomputing with QA7 not applicable for the other 35 papers (applicable maximum $14$; $16$ for HHSKT and SINKT) gives 31 HIGH, 6 MODERATE, and 0 LIMITED (corpus mean $0.86$). A single applicability decision therefore moves 20 papers into the HIGH tier, and neither version separates papers that evaluate a cold-start construct from papers that do not. The tiers are consequently a coarse reporting-completeness partition and are not evidence about sparse-concept adequacy; that evidence is in the dedicated sparse/cold-start fields (Table~\ref{tab:sparse_taxonomy}). The per-paper recomputation is in Supplementary Table~S-Files.",
        r"\textbf{Sensitivity to QA7 applicability.} The survey protocol allows QA7 to be coded not applicable when a paper makes no sparse or cold-start claim. A legacy recomputation on the pre-expansion 37-paper score file (QA7 not applicable except for two claim rows) moved many papers into the HIGH tier and is not the primary $N=44$ score reported above. Under the expanded coding, cold-start evaluation YES rows are HCMKT, SINKT, SGKT, and CoSKT (Table~\ref{tab:sparse_taxonomy}). The tiers remain a coarse reporting-completeness partition and are not evidence about sparse-concept adequacy; that evidence is in the dedicated sparse/cold-start fields.",
    ),
    (
        r"We did not extract wall-clock time, GPU memory, or paper-specific complexity formulas from the 37 manuscripts.",
        r"We did not extract wall-clock time, GPU memory, or paper-specific complexity formulas from the 44 manuscripts.",
    ),
    (
        r"Those two RMSE reports are not added to the twelve-of-37 count. CoSKT discusses cold start as short sequences and few students. That discussion is not a zero-exposure KC split.",
        r"HCMKT and DTransformer are already included in the $14/44$ RMSE count. CoSKT's short-sequence evaluation is learner cold-start YES and is not a zero-exposure KC split.",
    ),
    # Discussion leftovers
    (
        r"they are \emph{not} coded results of the 37-paper audit.",
        r"they are \emph{not} coded results of the 44-paper audit.",
    ),
    (
        r"None is a coded property of the 37 papers except",
        r"None is a coded property of the 44 papers except",
    ),
    (
        r"The 37 primary-core PDFs were identity-checked by the authors.",
        r"The 44 primary-core PDFs were identity-checked by the authors.",
    ),
    (
        r"verified the inclusion identity of the 37 PDFs,",
        r"verified the inclusion identity of the 44 PDFs,",
    ),
    # Contribution bullet that may still say N_S=9 on full/fmt if earlier partial
    (
        r"SSL-KT is a coding table among $N_S=9$ papers and four codebook pretext families, two of which have one paper each.",
        r"SSL-KT is coded by pretext paradigm and view source among $N_S=16$ papers ($N_{G\cap S}=12$), with sequence-only SSL retained as an explicit cell.",
    ),
    # Appendix provenance caption leftovers if any St wording
    (
        r"St counts: A 24, D 5, U 7.",
        r"Locked display counts on $N_G=40$: model-defined 24, external 7, dynamically learned 9.",
    ),
]

for name in FILES:
    p = ROOT / name
    t = p.read_text(encoding="utf-8")
    n = 0
    missing = []
    for a, b in REPS:
        c = t.count(a)
        if c:
            t = t.replace(a, b)
            n += c
        else:
            missing.append(a[:72].replace("\n", " "))
    p.write_text(t, encoding="utf-8")
    print(f"=== {name}: replaced {n}/{len(REPS)} ===")
    # residual probes
    for needle in ["N_G=36", "0/37", "1/37", "19/36", "8/36", "9/36", "37-PDF", "Interaction-drop (HHSKT)", "Learner cold-start YES: $0"]:
        if needle in t:
            print("  residual:", needle)
    if n < len(REPS):
        print(f"  missing {len(REPS)-n} patterns (ok if already updated on this file)")
