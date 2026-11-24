# -*- coding: utf-8 -*-
"""Apply C1--C3 wording to the three live TLT tex files. CRLF preserved."""
from pathlib import Path

ROOT = Path(r"D:\TRINH\GraphSSL_KT_Survey\12_manuscript\TLT")
FILES = [
    ROOT / "main_tlt_anonymous.tex",
    ROOT / "main_tlt_full.tex",
    ROOT / "manuscript_TLT_FORMATTED_v1.3.tex",
]

NOTATION_OLD = r"""$\mathcal{X}_{1:T}$ & Sequential interaction history of a student up to time $T$ \\
$x_t, r_t$ & Exercise/concept attempted at time $t$ and binary response $r_t \in \{0,1\}$ \\
$\mathcal{E}, \mathcal{K}$ & Repository sets of exercises and Knowledge Components (KCs) \\
$\mathbf{A} \in \mathbb{R}^{|\mathcal{K}| \times |\mathcal{K}|}$ & Concept graph adjacency matrix (co-occurrence / prerequisite) \\
$h_k^t \in \mathbb{R}^d$ & Dynamic hidden knowledge state representation of concept $k$ \\
$\mathbf{Z}^{(v)}$ & Node/view representation embedding matrix from GNN view $v$ \\
$\tau$ & Temperature hyperparameter in InfoNCE contrastive loss \\
$\text{ECE}$ & Expected Calibration Error (equal-width bins; manuscript-reporting audit $0/37$) \\"""

NOTATION_NEW = r"""$N_{\mathrm{rec}}$ & Number of raw records in the search log \\
$N$ & Number of primary-core papers \\
$n$ & Count of a stated sample, or the number of predictions in an ECE sum \\
$\mathcal{X}_{1:T}$ & Sequential interaction history of a student up to time $T$ \\
$x_t, r_t$ & Exercise/concept attempted at time $t$ and binary response $r_t \in \{0,1\}$ \\
$\mathcal{E}, \mathcal{K}$ & Repository sets of exercises and Knowledge Components (KCs) \\
$\mathbf{A} \in \mathbb{R}^{|\mathcal{K}| \times |\mathcal{K}|}$ & Concept graph adjacency matrix (co-occurrence / prerequisite) \\
$\tau$ & Temperature hyperparameter in InfoNCE contrastive loss \\
$\text{ECE}$ & Expected calibration error over equal-width bins of predicted confidence \\"""

FIG_OLD = r"""\begin{figure*}[t]
\centering
\subfloat[Graph provenance: model-defined fixed graph $n=19$, external fixed graph $n=8$, dynamically learned graph $n=9$ ($N_G=36$; mutually exclusive).]{%
\includegraphics[width=0.48\textwidth,height=1.85in,keepaspectratio]{figures/fig_graph_construction_pipeline.pdf}%
\label{fig:graph_pipeline}}
\hfill
\subfloat[Encoder counts ($N_G=36$; mutually exclusive): GCN/generic $12$, heterogeneous GNN $7$, Other $6$, \texttt{GAT} $4$, hypergraph $2$, dynamic $2$, none $3$ (PDKT-C, CMKT, PEBG).]{%
\includegraphics[width=0.48\textwidth,height=1.85in,keepaspectratio]{figures/fig_meta_analysis_charts.pdf}%
\label{fig:meta_charts}}
\caption{Graph-taxonomy counts: provenance (left) and encoder family (right).}
\label{fig:graph_counts}
\end{figure*}

"""

OVERLAY_OLD = r"""\begin{tabular}{@{}rll@{}}
\toprule
$n$ & Evaluation regime & Sparsity claim \\
\midrule
35 & Generic split & No explicit focus \\
1 & Drop (HHSKT) & Generic data sparsity \\
1 & Item cold-start & Item cold-start \\
0 & Zero-exposure KC & Strict KC cold-start \\
\bottomrule
\end{tabular}"""

OVERLAY_NEW = r"""\begin{tabular}{@{}rl@{}}
\toprule
$n$ & Evaluation reported \\
\midrule
35 & Standard interaction split \\
1 & Interaction-drop (HHSKT) \\
1 & Item cold-start (SINKT) \\
0 & Strict KC cold-start \\
\bottomrule
\end{tabular}"""

QA_INSERT_AFTER = (
    "That list is a reporting-adequacy partition for this review, "
    "not a ranking of scientific contribution."
)

QA_BLOCK = r"""

\begin{table}[t]
\caption{QA1--QA8 item scores on the 37 primary-core papers. Each item is scored $0$, $1$, or $2$. The counts are the item distribution. HIGH and MODERATE thresholds are unchanged.}
\label{tab:qa_distribution}
\centering
\footnotesize
\setlength{\tabcolsep}{6pt}
\begin{tabular}{@{}lccc@{}}
\toprule
\textbf{Item} & \textbf{0} & \textbf{1} & \textbf{2} \\
\midrule
QA1 Task clarity & 0 & 0 & 37 \\
QA2 Data and preprocessing & 0 & 0 & 37 \\
QA3 Split, provenance, leakage & 0 & 6 & 31 \\
QA4 Baselines and ablations & 0 & 0 & 37 \\
QA5 Statistical uncertainty & 0 & 37 & 0 \\
QA6 Author artifacts & 0 & 26 & 11 \\
QA7 Sparse and cold-start construct & 35 & 0 & 2 \\
QA8 Computational reporting & 0 & 5 & 32 \\
\bottomrule
\end{tabular}
\end{table}

QA1, QA2, and QA4 are $2$ on every paper, and QA5 is $1$ on every paper, so those four items do not separate the corpus. QA7 is $2$ only for HHSKT and SINKT. No cutoff was moved, and the LIMITED tier stays empty."""

PAIRS = [
    (NOTATION_OLD, NOTATION_NEW, 1),
    ("(search-log $N = 2,017$)", "(search-log $N_{\\mathrm{rec}} = 2{,}017$)", 2),
    ("search-log $N=2{,}017$", "search-log $N_{\\mathrm{rec}}=2{,}017$", 1),
    ("total of $N=2{,}017$", "total of $N_{\\mathrm{rec}}=2{,}017$", 1),
    ("Identification $N=2{,}017$", "Identification $N_{\\mathrm{rec}}=2{,}017$", 4),
    (
        "sum to $N = 2,017$ identified records",
        "sum to $N_{\\mathrm{rec}} = 2{,}017$ identified records",
        1,
    ),
    ("$N_{\\text{raw}}=2{,}017$", "$N_{\\mathrm{rec}}=2{,}017$", 1),
    (r"\frac{|B_m|}{N}", r"\frac{|B_m|}{n}", 1),
    (
        "and $N$ in this display is the number of predictions, not the number of papers.",
        "and $n$ is the number of predictions in that sum.",
        1,
    ),
    ("(Fig.~\\ref{fig:graph_pipeline})", "(Table~\\ref{tab:prov_encoder})", 1),
    (FIG_OLD, "", 1),
    (
        "Coded GNN encoder values on the 36 Graph-KT papers are shown in Fig.~\\ref{fig:meta_charts}.",
        "Coded GNN encoder values on the 36 Graph-KT papers are the column totals of Table~\\ref{tab:prov_encoder}. The bar chart of those totals is supplementary and is not printed next to the provenance counts.",
        1,
    ),
    (OVERLAY_OLD, OVERLAY_NEW, 1),
    (
        "QA7 is applicable on every row of that overlay.",
        "QA7 is applicable on every row of that overlay. Generic data sparsity is YES on all 37 rows of the deposited sparse file, so that field does not separate papers and is not used as a synthesis variable.",
        1,
    ),
    (QA_INSERT_AFTER, QA_INSERT_AFTER + QA_BLOCK, 1),
]


def load(path: Path) -> str:
    raw = path.read_bytes()
    text = raw.decode("utf-8")
    if "\r\n" not in text:
        raise SystemExit(f"{path.name}: expected CRLF")
    return text.replace("\r\n", "\n")


def save(path: Path, text: str) -> None:
    path.write_bytes(text.replace("\n", "\r\n").encode("utf-8"))


def apply_one(path: Path) -> None:
    text = load(path)
    for old, new, expected in PAIRS:
        found = text.count(old)
        if found != expected:
            raise SystemExit(f"{path.name}: expected {expected}, found {found} for: {old[:90]!r}")
        text = text.replace(old, new)
    leftovers = []
    for token in ["fig:graph_pipeline", "fig:meta_charts", "fig:graph_counts", "$N = 2,017$", "$N=2{,}017$", r"N_{\text{raw}}", "h_k^t", r"\mathbf{Z}^{(v)}"]:
        if token in text:
            leftovers.append(token)
    if leftovers:
        raise SystemExit(f"{path.name}: leftovers {leftovers}")
    save(path, text)
    print("updated", path.name)


def main() -> None:
    for path in FILES:
        apply_one(path)


if __name__ == "__main__":
    main()
