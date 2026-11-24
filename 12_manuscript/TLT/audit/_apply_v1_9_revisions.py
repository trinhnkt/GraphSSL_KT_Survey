"""Apply the v1.9 reviewer-response revisions to the three TLT manuscript sources.
Each replacement asserts the expected number of occurrences per file and reports misses.
"""
import csv, os, sys, io

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES = ['main_tlt_anonymous.tex', 'main_tlt_full.tex', 'manuscript_TLT_FORMATTED_v1.3.tex']

rows = list(csv.DictReader(open(os.path.join(BASE, 'supplementary', 'graph_provenance_subbins_8way_v1.9.csv'), encoding='utf-8')))
D = {'MODEL_DEFINED_FIXED': 'MDF', 'EXTERNAL_FIXED': 'EXT', 'DYNAMIC_LEARNED': 'DYN'}
R = {'PRECOMPUTED_UNCLEAR_SPLIT': 'PRE', 'JOINTLY_LEARNED_TRAINING': 'JNT', 'EXTERNAL_FIXED': 'EXT', 'UNCLEAR': 'UNC'}
S = {'Q-matrix/expert-authored': 'Q', 'Log-derived': 'L', 'Architecture-defined': 'A', 'External': '--', 'Dynamic-learned': '--'}


def rec(r):
    v = r['record_8way']
    return 'MIX' if v.startswith('MIXED') else R[v]


def st(r):
    s = r['display_vs_record']
    return 'A' if s == 'AGREES' else ('D' if s.startswith('DIFFERS_DOC') else 'U')


cells = [f"{r['paper_id']} & {D[r['display_3token']]} & {rec(r)} & {S[r['subbin_v1_9']]} & {st(r)}" for r in rows]
assert len(cells) == 36
half = 18
body = '\n'.join(cells[i] + ' & ' + cells[i + half] + r' \\' for i in range(half))
APPENDIX = r"""\appendices
\section{Per-Paper Provenance Records}
\label{app:provenance}
Table~\ref{tab:prov_appendix} lists, for the 36 Graph-KT papers, the displayed three-token code (Disp.), the value in the per-paper eight-value \texttt{graph\_provenance} record (Rec.), the sub-bin of Sec.~\ref{sec:graph_provenance}, and whether the record maps to the displayed code under the collapse rule. The deposited records contain only five of the nine codebook tokens at paper level: \texttt{JOINTLY\_LEARNED\_TRAINING} ($n=13$), \texttt{PRECOMPUTED\_UNCLEAR\_SPLIT} ($n=13$), \texttt{EXTERNAL\_FIXED} ($n=8$), \texttt{UNCLEAR} ($n=1$, HHSKT, abstract-level coding), and one mixed record (GKT: Dense graph \texttt{MODEL\_DEFINED\_FIXED}, Transition graph \texttt{PRECOMPUTED\_UNCLEAR\_SPLIT}). No paper-level record is \texttt{TRAIN\_ONLY\_INFERRED}, \texttt{FULL\_DATA\_INFERRED}, \texttt{MIXED\_PROVENANCE}, or \texttt{PRETRAINED\_TWO\_STAGE}; in other words, no record states that a graph was built from the training split only. The machine-readable table is \path{supplementary/graph_provenance_subbins_8way_v1.9.csv}.

\begin{table*}[t]
\caption{Per-paper provenance records ($N_G=36$; KT004 counted once; CL4KT excluded as non-graph). Disp.: MDF $=$ \texttt{MODEL\_DEFINED\_FIXED}, EXT $=$ \texttt{EXTERNAL\_FIXED}, DYN $=$ \texttt{DYNAMIC\_LEARNED}. Rec.: JNT $=$ \texttt{JOINTLY\_LEARNED\_TRAINING}, PRE $=$ \texttt{PRECOMPUTED\_UNCLEAR\_SPLIT}, UNC $=$ \texttt{UNCLEAR}, MIX $=$ mixed. Sub: Q $=$ Q-matrix/expert-authored, L $=$ log-derived, A $=$ architecture-defined (only for display MDF). St: A $=$ record maps to Disp.; D $=$ differs, with a documented PDF-level adjudication or recode; U $=$ differs, with no PDF-level re-check on file. St counts: A 24, D 5, U 7.}
\label{tab:prov_appendix}
\centering
\scriptsize
\setlength{\tabcolsep}{3.5pt}
\begin{tabular}{@{}lllll@{\hspace{1.4em}}lllll@{}}
\toprule
ID & Disp. & Rec. & Sub & St & ID & Disp. & Rec. & Sub & St \\
\midrule
""" + body + r"""
\bottomrule
\end{tabular}
\end{table*}

"""

CROSSTAB = r"""\textbf{Sub-bins of the displayed \texttt{MODEL\_DEFINED\_FIXED} code.} That code mixes three construction logics, so we split its 19 papers by a deterministic rule on the locked \texttt{graph\_source} token and the per-paper eight-value record: \emph{Q-matrix/expert-authored} ($n=3$: GIKT, PEBG, GASKT; graph taken from the exercise--KC annotation only), \emph{log-derived} ($n=10$; any component derived from interaction logs, including GKT's transition graph, or an eight-value record of \texttt{PRECOMPUTED\_UNCLEAR\_SPLIT}), and \emph{architecture-defined} ($n=6$: HHSKT, TSKT, GraphCA, Capsule GNN, MG-Ensemble, CS-GKT; the remainder). The rule is applied to coding records; it was not re-read from the PDFs. Log-derived graphs are the ones for which a train-only construction statement matters (Sec.~\ref{sec:graph_kt}).

\textbf{The three-token display is not a mechanical collapse of the eight-value records.} Of the 36 records, 24 map to the displayed code under the collapse rule. Five differ with a documented PDF-level adjudication or recode (SKT, TSKT, SINKT, Capsule GNN, KGNN-KT). Seven differ with no PDF-level re-check on file: SGKT, HHSKT, GraphCA, LGS-KT, MG-Ensemble, CS-GKT, and AEGOT-CDKT (Appendix~\ref{app:provenance}). If those seven took the code implied by their records, the counts would be 16 model-defined, 8 external, 11 dynamic, and 1 unclassified (HHSKT, \texttt{UNCLEAR}) instead of 19/8/9. We keep 19/8/9 as the locked display values and report the alternative as a sensitivity bound; resolving the seven papers needs a PDF-level re-check that has not been done.

\begin{table}[t]
\caption{Graph-KT papers by provenance sub-bin and encoder group ($N=36$; 35 cells, 15 empty). Counts only: no outcome measure (AUC, ECE, leakage) is attached to any cell, and no association is inferred. Q $=$ Q-matrix/expert-authored; Log $=$ log-derived; Arch $=$ architecture-defined; Ext $=$ \texttt{EXTERNAL\_FIXED}; Dyn $=$ \texttt{DYNAMIC\_LEARNED}. File: \texttt{supplementary/graph\_provenance\_x\_encoder\_crosstab\_v1.9.csv}.}
\label{tab:prov_encoder}
\centering
\footnotesize
\setlength{\tabcolsep}{4pt}
\begin{tabular}{@{}lccccc|c@{}}
\toprule
\textbf{Encoder group} & \textbf{Q} & \textbf{Log} & \textbf{Arch} & \textbf{Ext} & \textbf{Dyn} & \textbf{Total} \\
\midrule
GCN / generic & 1 & 3 & 2 & 3 & 3 & 12 \\
Heterogeneous & 0 & 3 & 3 & 1 & 0 & 7 \\
GAT & 1 & 1 & 0 & 1 & 1 & 4 \\
Hypergraph & 0 & 2 & 0 & 0 & 0 & 2 \\
Dynamic GNN & 0 & 0 & 0 & 0 & 2 & 2 \\
None (no GNN) & 1 & 0 & 0 & 2 & 0 & 3 \\
Other & 0 & 1 & 1 & 1 & 3 & 6 \\
\midrule
\textbf{Total} & 3 & 10 & 6 & 8 & 9 & 36 \\
\bottomrule
\end{tabular}
\end{table}

Table~\ref{tab:prov_encoder} reports distribution only. With 36 papers over 35 cells, no cell exceeds three papers and 15 cells are empty, so the table cannot support a statement about which provenance--encoder pairings work better; it only shows what has been built. Both hypergraph papers use log-derived graphs, both dynamic-GNN papers are dynamically learned (largely by construction), and no paper without a GNN uses a log-derived graph.

"""

AI_ROLE = r"""\subsection{Role of the AI Research Assistant}
\label{sec:ai_role}
Screening and primary coding were carried out by an AI research assistant (a tool-using LLM agent) under the locked codebook; this is a methodological fact and not language polishing. The deposited title/abstract and full-text screening files (43 and 48 rows, seed-stage records rather than the 750-record ledger) list the assistant as both screener and reviewer, and no human second-screener file exists. Of the 45 per-paper coding records, 41 name the assistant as coder. Documented human steps are limited to (i)~author verification of the inclusion identity of the 37 PDFs, (ii)~independent double-coding of a 20-paper sample by two human coders (Sec.~\ref{sec:icr}) with adjudication of five cells to the locked gold, and (iii)~PDF-level re-checks of three provenance records (Sec.~\ref{sec:deviations}). Per-paper human verification of the remaining primary-coding fields is not documented. Consequently the primary coding is not an independent human judgment, the reported $\kappa$ values measure agreement between human coders and an AI-generated, partly adjudicated reference, and an error shared by the assistant and a human coder would not be detected. The stage-level inclusion and exclusion decisions behind 750/140/103 cannot be audited at record level.

"""

VENUE = r"""\subsection{Venue-Extension Probe}
\label{sec:venue_ext}
After the locked search, we probed six education-technology venues (EDM, AIED, LAK, L@S, JEDM, IJAIED) with one search-engine query per venue on 2026-11-11 (first five results reviewed; not a database export; log in \path{03_search/search_log_venue_extension_v1.9.csv}). Two venue-confirmed Graph-KT candidates were found: an EDM~2022 poster (AGKT) and an L@S~2024 paper on expert-defined graphs. The AIED, LAK, and IJAIED queries returned none, and the only JEDM hit is the graph-KT survey already cited as a prior review. The same queries surfaced eight further Graph-KT or SSL-KT papers in other venues (KDD~2024, IJCAI~2025, ACM TKDD~2023, IEEE Access~2025, Neurocomputing~2026, and others); seven of the ten candidates are described in their abstracts as combining a graph with contrastive or self-supervised learning. None of the ten appears in any deposited screening record, and eight are published in outlets covered by databases we searched (ACM DL, IEEE Xplore, ScienceDirect), so their absence reflects either a recall gap or an unrecorded screening decision; the missing ledger cannot distinguish the two. The candidates (\path{03_search/venue_extension_candidates_v1.9.csv}) are not coded and do not change $N=37$, $N_G$, $N_S$, or any $\kappa$; adding them would require full-text screening and coding under the locked codebook. The 37-paper core is therefore a locked deposit and not a saturated census, and $N_S$ in particular may be understated.

"""

DEVIATIONS = r"""
\subsection{Deviations from the Locked Protocol}
\label{sec:deviations}
The locked protocol files were not edited. The following departures are recorded in \path{00_protocol/protocol_deviations.md} (DEV-20261106-01 to -03 and DEV-20261111-01).
\begin{itemize}
    \item \textbf{Screening evidence.} The protocol requires a second-screener sample and record-level ledgers. They are not deposited, there is no second screener, and the 1{,}267/750/610/140/103 stage counts are report arithmetic (Sec.~\ref{sec:ai_role}).
    \item \textbf{Provenance display and recodes.} The eight-value \texttt{graph\_provenance} field is reported as three display tokens; 24 of 36 records map to the displayed code, five differ with a documented PDF-level adjudication, and seven differ without one (Sec.~\ref{sec:graph_provenance}, Appendix~\ref{app:provenance}). TSKT was recoded from \texttt{EXTERNAL\_FIXED} to \texttt{MODEL\_DEFINED\_FIXED} after a PDF check; the earlier Capsule GNN coding-file value \texttt{EXTERNAL\_FIXED} is superseded; SKT stays in the model-defined bin although its PDF is mixed.
    \item \textbf{S-criterion narrowing.} Re-auditing the SSL criterion reduced $N_S$ from 14 to 9. SINKT, Coda, KGNN-KT, R$^2$GCurL, and STSKT were removed from SSL coding and remain in the corpus as Graph-KT; $N=37$ is unchanged. The exclusive \texttt{ssl\_family} values are the four locked tokens; an earlier ``seven families'' count used display aliases.
    \item \textbf{Reliability recomputation.} Cohen's $\kappa$ is undefined for three invariant all-NO fields; they are excluded from the macro-average. The locator-assisted and independent passes are reported separately and are not pooled; no screening reliability exists.
    \item \textbf{Sparse/cold-start file.} The deposited \texttt{sparse\_coldstart\_audit.csv} carried a \texttt{sparse\_interaction\_drop\_eval} column that was YES for all 37 rows, contradicting the body and the H2 overlay (HHSKT only). Version v1.9 sets it to YES for HHSKT only, drops the constant generic-sparsity column, and keeps the deposited file unchanged. The new NO values reflect the H2 overlay and were not re-read from the PDFs.
    \item \textbf{Post hoc additions outside the protocol.} The DyGKT ECE overlay (Sec.~\ref{sec:reliability}) and the venue-extension probe (Sec.~\ref{sec:venue_ext}) were not specified in the locked protocol.
\end{itemize}
"""

COLDSTART = r"""\textbf{Learner cold-start} is a new learner or a minimal-history condition at prediction time (a learner with few or no prior interactions); it is not equivalent to sparse KCs, and holding out whole learners with their full histories is not by itself a learner cold-start evaluation. Table~\ref{tab:coldstart_decision} operationalizes the four constructs; the locked fields were coded under the SCOPE definitions and this table restates them without re-coding.

\begin{table}[t]
\caption{Decision table for the sparsity and cold-start constructs. ``Not sufficient'' lists a common claim that does not by itself earn a YES. Counts are from the locked coding ($N=37$).}
\label{tab:coldstart_decision}
\centering
\footnotesize
\setlength{\tabcolsep}{2.5pt}
\begin{tabular}{@{}>{\raggedright\arraybackslash}p{0.19\columnwidth}>{\raggedright\arraybackslash}p{0.30\columnwidth}>{\raggedright\arraybackslash}p{0.25\columnwidth}c@{}}
\toprule
\textbf{Construct} & \textbf{YES iff} & \textbf{Not sufficient} & \textbf{n} \\
\midrule
Interaction-drop evaluation & Interactions are deliberately removed from training or history and results are reported by drop level & A random 80/20 split & 1 \\
Item cold-start & Test items are withheld from training & Random interaction split & 1 \\
Learner cold-start & Test learners have no or truncated history and are scored separately & Learner-level split with full histories & 0 \\
Strict KC cold-start & At least one KC has zero training interactions & An external graph alone & 0 \\
\bottomrule
\end{tabular}
\end{table}

"""

ECE_SCAN = r"""
\textbf{Keyword scan beyond ECE.} To test whether ECE-only coding hides other calibration evidence, we scanned the PDF text layers of 36 of the 37 primary-core papers for ECE, Brier, reliability-diagram or calibration-plot, and negative-log-likelihood or log-loss strings (KGNN-KT has no extractable text layer and was not scanned; its coding record is ECE $=$ NO). ECE appears in $0/36$ and Brier in $0/36$. One paper, CL4KT, shows a calibration plot (``calibration binned by predictions'' on ASSIST09) without a summary statistic. Negative-log-likelihood strings occur only as training objectives, so no evaluation-time NLL is reported; other ``calibrat-'' strings refer to calibrated Q-matrices. The scan is string-based and can miss a metric described without these terms (output in \path{supplementary/calibration_keyword_scan_v1.9.csv}). The audit is therefore stated as ECE reporting $0/37$, not as the absence of any calibration evidence.
"""

DYGKT = r"""

\textbf{Why DyGKT, and which setting.} DyGKT was chosen on practical grounds: its authors release a repository with bundled processed ASSIST17 data and an evaluation script. No systematic selection among corpus models is documented and no other model was run, so the overlay is a convenience demonstration and not a sample of Graph-KT. The setting is \emph{transductive}: probabilities are sigmoid outputs on time-ordered held-out test edges (author split 0.8/0.1/0.1) among nodes seen during training. ECE was not computed for the author's new-node (inductive) test pass (author-metric AUC $0.8035$), so the overlay carries no information about zero-exposure KC or item cold-start."""

WORKED = r"""
\textbf{Worked example (SINKT, KT044).} A learning engineer asks whether SINKT can onboard a newly authored module. \emph{Step~1 (T1).} Read the coded fields: \texttt{strict\_kc\_cold\_start}$=$NO and \texttt{item\_cold\_start}$=$YES (one quarter of questions held out). The held-out unit is a question, so the evidence covers a new item whose KCs appear in training. \emph{Step~2.} The new module introduces KCs absent from training, so no coded protocol matches it: not enough evidence to GO. \emph{Step~3 (T2).} \texttt{graph\_provenance}$=$\texttt{EXTERNAL\_FIXED} (LLM/semantic graph from a documented source), so the graph can be inspected as an artifact, but its pedagogical validity is not coded: conditional, not GO. \emph{Step~4 (T3).} \texttt{ece\_reported}$=$NO, so the calibration of $P(r=1)$ is unverified: not enough evidence to GO for remediation triggers; closing it needs ECE or Brier on the decision split (Recommendation~3). The checklist output for SINKT is T1 not enough evidence to GO, T2 conditional on graph inspection, T3 not enough evidence to GO. It is a reading of coded fields, not a test of SINKT.
"""

ACK_OLD = r"""The authors used the Cursor AI coding assistant~\cite{Cursor_AI_2026} for language polishing, \LaTeX\ formatting, consistency checking, and implementation of author-approved manuscript and artifact revisions. All inclusion decisions, coding judgments, evidence interpretations, statistical decisions, and scientific conclusions were made and verified by the authors. AI-assisted changes were reviewed against the source literature and locked review protocol, and the authors take full responsibility for the final content."""
ACK_NEW = r"""An AI research assistant (Cursor~\cite{Cursor_AI_2026}; coding files also record an earlier agent session as ``Antigravity'') screened candidate records and produced the primary paper-, model-, and experiment-level coding records under the locked protocol (Sec.~\ref{sec:ai_role}). It also assisted with drafting, \LaTeX\ formatting, consistency checking, and implementation of author-approved revisions. The authors defined the protocol, verified the inclusion identity of the 37 PDFs, supervised two human coders on a 20-paper sample, adjudicated disagreements, and take responsibility for the final content. Per-paper human verification of every primary-coding field is not documented; the reliability results should be read with that limitation."""

# (old, new, expected_count)
R = []
add = R.append

# --- abstract
add(("Inclusion decisions were not second-screened; inter-coder reliability is reported only for a 20-paper coding sample.",
     "Screening and primary coding were produced by an AI research assistant and not second-screened by a human; inter-coder reliability is reported only for a 20-paper human-coded sample.", 1))
add(("plus an operational GO/NO-GO checklist for those three tutoring decisions", "plus an operational go/not-enough-evidence checklist for those three tutoring decisions", 1))
add(("The agenda puts corpus-derived priorities (zero-exposure benchmarks, calibration reporting, train-only graphs) before open technical directions.\n\\end{abstract}",
     "A post hoc venue probe found ten candidate Graph/SSL-KT papers outside the locked core, so the core is not a saturated census. The agenda puts corpus-derived priorities (zero-exposure benchmarks, calibration reporting, train-only graphs) before open technical directions.\n\\end{abstract}", 1))
# --- intro
add(("and the GO/NO-GO checklist in Sec.~\\ref{sec:go_nogo}.", "and the go/not-enough-evidence checklist in Sec.~\\ref{sec:go_nogo}.", 1))
add(("T1--T3 GO/NO-GO for ITS / adaptive / formative use", "T1--T3 evidence-to-GO for ITS / adaptive / formative use", 1))
add(("The coding separates generic interaction sparsity from item, learner, and strict KC cold-start. None of the 37 studies isolate a zero-exposure KC split.",
     "The coding separates item, learner, and strict KC cold-start (one-sentence learner definition and decision table, Table~\\ref{tab:coldstart_decision}) from baseline interaction sparsity, which is not itself a finding. None of the 37 studies isolate a zero-exposure KC split.", 1))
add(("\\textbf{Calibration and deployment-readiness audit}: None of the 37 manuscripts report ECE ($0/37$).",
     "\\textbf{ECE reporting audit}: None of the 37 manuscripts report ECE ($0/37$); a keyword scan of 36 PDFs finds no Brier score and one calibration plot (CL4KT).", 1))
add(("states a three-decision GO/NO-GO checklist for learning engineers", "states a three-decision go/not-enough-evidence checklist for learning engineers", 1))
# --- methodology inserts
add(("\\subsection{PRISMA 2020 Screening \\& Eligibility Flow}", VENUE + "\\subsection{PRISMA 2020 Screening \\& Eligibility Flow}", 1))
add(("\\subsection{Evidence Coding Scheme}", AI_ROLE + "\\subsection{Evidence Coding Scheme}", 1))
add(("QA1--QA8 were assigned by the primary coder.", "QA1--QA8 were assigned by the primary coder (an AI research assistant; Sec.~\\ref{sec:ai_role}).", 2))
add(("count distributions of coded fields (not a pooled-effect meta-analysis).", "count distributions of coded fields (not a pooled-effect meta-analysis).\n" + DEVIATIONS, 1))
# --- graph provenance
add(("the adjacency is a pedagogical object rather than a log statistic.",
     "the adjacency originates outside the interaction logs, which is a precondition for, but not evidence of, pedagogical validity.", 1))
add(("These tokens support different tutoring uses; none of them licenses T1", CROSSTAB + "These tokens support different tutoring uses; none of them licenses T1", 1))
add(("provenance does not change the T1 NO-GO in Sec.~\\ref{sec:go_nogo}.", "provenance does not change the T1 verdict (not enough evidence to GO) in Sec.~\\ref{sec:go_nogo}.", 1))
# --- sparse / cold-start
add(("All 37 studies report generic interaction sparsity; none isolate a strict zero-exposure KC hold-out.", "None of the 37 studies isolates a strict zero-exposure KC hold-out.", 1))
add(("\\subsection{Methodological Audit of Evaluation Split Vulnerabilities}", COLDSTART + "\\subsection{Methodological Audit of Evaluation Split Vulnerabilities}", 1))
add(("All 37 rows have generic data sparsity. Strict KC cold-start YES", "Interaction-drop evaluation YES: $1/37$ (HHSKT). Strict KC cold-start YES", 1))
add(("The full 37-row file is \\texttt{tables/sparse\\_coldstart\\_audit.csv}.", "The full 37-row file is \\texttt{tables/sparse\\_coldstart\\_audit\\_v1.9.csv}.", 1))
add(("Generic data sparsity is YES for all 37 papers. Strict KC cold-start is YES for $0/37$ papers.", "Interaction-drop evaluation is YES for HHSKT only ($1/37$). Strict KC cold-start is YES for $0/37$ papers.", 1))
add(("all 37 rows are in \\path{tables/sparse_coldstart_audit.csv}. This survey does not report a reproduced cold-start AUC.",
     "all 37 rows are in \\path{tables/sparse_coldstart_audit_v1.9.csv}. The deposited v1 file carried a constant-YES drop column that contradicted this table; v1.9 corrects it (Sec.~\\ref{sec:deviations}). This survey does not report a reproduced cold-start AUC.", 1))
# --- reliability / ECE
add(("\\section{Reliability, Reproducibility \\& Calibration Audit (RQ5)}", "\\section{Reliability, Reproducibility \\& ECE Reporting Audit (RQ5)}", 1))
add(("\\subsection{Probability Calibration Audit (Expected Calibration Error)}", "\\subsection{ECE Reporting Audit}", 1))
add(("where $B_m$ is the set of predictions in $((m-1)/M, m/M]$.\n", "where $B_m$ is the set of predictions in $((m-1)/M, m/M]$.\n" + ECE_SCAN, 1))
add(("the supplementary package records the reproduction manifest, run log, and per-bin table.", "the supplementary package records the reproduction manifest, run log, and per-bin table." + DYGKT, 1))
# --- GO / not enough evidence
add(("\\subsection{Three Tutoring Decisions: a GO/NO-GO Checklist}", "\\subsection{Three Tutoring Decisions: a Go/Not-Enough-Evidence Checklist}", 1))
add(("Apply the three decisions in order (new content, then graph interpretation, then probability actions).",
     "Apply the three decisions in order (new content, then graph interpretation, then probability actions). A verdict of ``not enough evidence to GO'' says that the corpus lacks the evidence the action requires; it does not say the action is unsafe or that the models fail.", 1))
add(("Verdict: \\textbf{NO-GO} for new-KC onboarding from a learner-level 80/20 AUC.", "Verdict: \\textbf{not enough evidence to GO} for new-KC onboarding: the coded protocols do not test it, and an untested case is not a failed one.", 1))
add(("Verdict: \\textbf{conditional GO} only when the source is a documented external map. \\textbf{NO-GO} for calling a co-occurrence or transition graph a pedagogical prerequisite unless a train-only construction statement is reported.",
     "Verdict: \\textbf{conditional GO} only when the source is a documented external map; for a co-occurrence or transition graph, \\textbf{not enough evidence to GO} as a pedagogical prerequisite unless a train-only construction statement is reported.", 1))
add(("Verdict: \\textbf{NO-GO}. Required evidence before GO: ECE or Brier", "Verdict: \\textbf{not enough evidence to GO}. Required evidence before GO: ECE or Brier", 1))
add(("\nThese three verdicts are why Table~\\ref{tab:its_implications}", WORKED + "\nThese three verdicts are why Table~\\ref{tab:its_implications}", 1))
add(("would change a T1--T3 verdict from NO-GO to GO.", "would change a T1--T3 verdict from not-enough-evidence to GO.", 1))
add(("Generic data sparsity is YES for all 37 papers and is not evidence of any cold-start construct.", "Baseline interaction sparsity is not evidence of any cold-start construct.", 1))
add(("Screening and coding were performed by the research team rather than by an independent external coder (Sec.~\\ref{sec:icr}).",
     "Screening and primary coding were performed by an AI research assistant under the locked protocol, not by an independent human coder (Sec.~\\ref{sec:ai_role}); human coding exists only for a 20-paper sample (Sec.~\\ref{sec:icr}).", 1))
# --- threats
add(("so relevant work outside those indexes may be absent.", "so relevant work outside those indexes may be absent. A post hoc venue probe (Sec.~\\ref{sec:venue_ext}) found ten Graph/SSL-KT candidates absent from the deposited records.", 1))
add(("Generic data sparsity, item cold-start, learner cold-start, and strict KC cold-start are separate locked fields.", "Interaction-drop evaluation, item cold-start, learner cold-start, and strict KC cold-start are separate locked fields.", 1))
add(("the GO/NO-GO checklist.", "the go/not-enough-evidence checklist.", 1))
# --- conclusion
add(("\\textbf{Contribution 4 --- Calibration audit.} None of the 37 manuscripts report ECE ($0/37$).", "\\textbf{Contribution 4 --- ECE reporting audit.} None of the 37 manuscripts report ECE ($0/37$); a keyword scan finds no Brier score and one calibration plot (CL4KT).", 1))
add(("\\textbf{Contribution 3 --- Validity audit.} Generic interaction sparsity is separated from item, learner, and strict KC cold-start.", "\\textbf{Contribution 3 --- Validity audit.} Item, learner, and strict KC cold-start are separated from baseline interaction sparsity.", 1))
add(("A three-decision GO/NO-GO checklist (new KC, skill-map graph, $P(r=1)$ action)", "A three-decision go/not-enough-evidence checklist (new KC, skill-map graph, $P(r=1)$ action)", 1))
add(("The intended use is to give a learning engineer a coded stop/go before", "The intended use is to give a learning engineer a coded go/not-enough-evidence reading before", 1))
add(("\\section*{Acknowledgment}\n" + ACK_OLD, APPENDIX + "\\section*{Acknowledgment}\n" + ACK_NEW, 1))

problems = 0
for fn in FILES:
    path = os.path.join(BASE, fn)
    t = io.open(path, encoding='utf-8', newline='').read().replace('\r\n', '\n')
    for old, new, n in R:
        c = t.count(old)
        if c != n:
            print(f'[{fn}] MISMATCH count={c} expected={n}: {old[:90]!r}')
            problems += 1
            continue
        t = t.replace(old, new)
    out = path
    if problems == 0:
        io.open(out, 'w', encoding='utf-8', newline='').write(t.replace('\n', '\r\n'))
    print(fn, 'written')
print('problems', problems)
