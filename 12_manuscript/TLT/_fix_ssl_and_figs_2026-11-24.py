# -*- coding: utf-8 -*-
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TEX_FILES = [
    "main_tlt_anonymous.tex",
    "main_tlt_full.tex",
    "manuscript_TLT_FORMATTED_v1.3.tex",
]

REPS = [
    (
        "The S-criterion codes 9 papers into four exclusive codebook families (Fig.~\\ref{fig:ssl_framework}; Table~\\ref{tab:ssl_taxonomy}). This is a coding table, not a saturated SSL-KT taxonomy: two families (graph reconstruction, sequence contrast) have one paper each. Hypergraph, line-graph, and hierarchical wording in the table are mechanism notes, not extra family codes:",
        "On the pre-expansion SSL set, exclusive codebook families coded 9 papers into four families (Fig.~\\ref{fig:ssl_framework}; Table~\\ref{tab:ssl_taxonomy}). After the Sec.~\\ref{sec:gateway_ext} update, $N_S=16$ (fifteen contrastive or consistency objectives and one generative reconstruction under the freeze note); the four-family list below remains the pre-expansion exclusive coding and is not a complete partition of the 16. Hypergraph, line-graph, and hierarchical wording in the table are mechanism notes, not extra family codes:",
    ),
    (
        "The augmentation column of Table~\\ref{tab:ssl_taxonomy} gives the page-checked wording for the other eight SSL papers.",
        "The augmentation column of Table~\\ref{tab:ssl_taxonomy} gives the page-checked wording for the other printed SSL rows; expansion SSL rows are in the supplementary 16-row file.",
    ),
    (
        "Eight primary core papers ($N_{G \\cap S} = 8$) combine an explicit graph mechanism with a self-supervised objective (all SSL-KT papers except sequence-only CL4KT). Table~\\ref{tab:ssl_taxonomy} lists all 9 SSL-KT studies.",
        "Twelve primary-core papers ($N_{G \\cap S} = 12$) combine an explicit graph mechanism with a self-supervised objective. Sequence-only SSL papers are CL4KT, DTransformer, CoSKT, and SP-CLKT. Table~\\ref{tab:ssl_taxonomy} prints representative SSL-KT rows from the $N_S=16$ set.",
    ),
]

for name in TEX_FILES:
    p = ROOT / name
    t = p.read_text(encoding="utf-8")
    n = 0
    for a, b in REPS:
        if a in t:
            t = t.replace(a, b)
            n += 1
    p.write_text(t, encoding="utf-8")
    print(name, "ssl fixes", n)

# --- figure sources ---
tax = ROOT / "figures" / "fig_taxonomy_2d.tex"
t = tax.read_text(encoding="utf-8")
t = t.replace(r"$N=37$", r"$N=44$")
t = t.replace(r"Graph provenance  $N_G=36$", r"Graph provenance  $N_G=40$")
t = t.replace(r"GNN encoder  $N_G=36$", r"GNN encoder (pre-exp.)")
t = t.replace(r"Self-supervised KT  $N_S=9$", r"Self-supervised KT  $N_S=16$")
t = t.replace(
    r"""{\fontsize{13}{15}\selectfont\bfseries 19}\\[-1pt]
  {\small Model-defined fixed}\\[-1pt]
  {\scriptsize\color{muted}model-defined fixed graph  52.8\%}}""",
    r"""{\fontsize{13}{15}\selectfont\bfseries 24}\\[-1pt]
  {\small Model-defined fixed}\\[-1pt]
  {\scriptsize\color{muted}model-defined fixed graph  60.0\%}}""",
)
t = t.replace(
    r"""{\fontsize{13}{15}\selectfont\bfseries 8}\\[-1pt]
  {\small External fixed}\\[-1pt]
  {\scriptsize\color{muted}external fixed graph  22.2\%}}""",
    r"""{\fontsize{13}{15}\selectfont\bfseries 7}\\[-1pt]
  {\small External fixed}\\[-1pt]
  {\scriptsize\color{muted}external fixed graph  17.5\%}}""",
)
t = t.replace(
    r"""{\fontsize{13}{15}\selectfont\bfseries 9}\\[-1pt]
  {\small Dynamically learned}\\[-1pt]
  {\scriptsize\color{muted}dynamically learned graph  25.0\%}}""",
    r"""{\fontsize{13}{15}\selectfont\bfseries 9}\\[-1pt]
  {\small Dynamically learned}\\[-1pt]
  {\scriptsize\color{muted}dynamically learned graph  22.5\%}}""",
)
t = t.replace(
    r"""{\bfseries 9}\\[-2pt]{\scriptsize SSL papers}};
\node[schip, right=0.21cm of s1] (s2) {{\bfseries 8}\\[-2pt]{\scriptsize Graph $\cap$ SSL}};
\node[scard, minimum height=1.05cm, below=0.20cm of s1, xshift=1.265cm] (s3) {%
  {\small Sequence-only SSL: CL4KT}\\[-1pt]
  {\scriptsize\color{muted}graph source = none}};
\node[scard, minimum height=2.15cm, below=0.20cm of s3] (s4) {%
  {\scriptsize\bfseries 4 pretext families}\\[2pt]
  {\scriptsize Multiview $n=5$; graph contrast $n=2$}\\[1pt]
  {\scriptsize Reconstruction $n=1$; sequence $n=1$}\\[1pt]
  {\scriptsize\color{muted}PEBG is graph reconstruction}};""",
    r"""{\bfseries 16}\\[-2pt]{\scriptsize SSL papers}};
\node[schip, right=0.21cm of s1] (s2) {{\bfseries 12}\\[-2pt]{\scriptsize Graph $\cap$ SSL}};
\node[scard, minimum height=1.05cm, below=0.20cm of s1, xshift=1.265cm] (s3) {%
  {\small Sequence-only SSL: 4 papers}\\[-1pt]
  {\scriptsize\color{muted}CL4KT, DTransformer, CoSKT, SP-CLKT}};
\node[scard, minimum height=2.15cm, below=0.20cm of s3] (s4) {%
  {\scriptsize\bfseries Expanded SSL note}\\[2pt]
  {\scriptsize 15 contrastive / consistency; 1 reconstruction}\\[1pt]
  {\scriptsize Pre-expansion exclusive families remain in body}\\[1pt]
  {\scriptsize\color{muted}Encoder chips not re-derived for expansion}};""",
)
t = t.replace(
    r"One row per paper. Provenance and encoder percentages use $N_G=36$. SSL counts use $N_S=9$. No hyperbolic encoder; SSL categories follow the four four pretext families.",
    r"One row per paper. Locked provenance $24/7/9$ on $N_G=40$. SSL $N_S=16$, $N_{G\cap S}=12$. Encoder chips are pre-expansion tallies.",
)
tax.write_text(t, encoding="utf-8")
print("updated", tax.name)

prisma = ROOT / "figures" / "fig_prisma_flow.tex"
p = prisma.read_text(encoding="utf-8")
p = p.replace(
    r"""\node[stage, fill=green!15, draw=green!60!black, below=1.0cm of fulltext] (final) {\textbf{Primary core}\\\textbf{37 primary-core PDFs}\\(34-record seed list; recall not computed)};

\node[note, below=0.55cm of final] (note) {Stage counts 750 / 140 / 103 are search-expansion report arithmetic.\\A record-level screening ledger is not deposited. Identification $N_{\mathrm{rec}}=2{,}017$ is the search-log sum.};""",
    r"""\node[stage, fill=green!15, draw=green!60!black, below=1.0cm of fulltext] (final) {\textbf{Original-path inclusion arithmetic}\\\textbf{$140-103=37$}\\(coded core after full-text update: $N=44$)};

\node[note, below=0.55cm of final] (note) {Stage counts 750 / 140 / 103 are search-expansion report arithmetic.\\A record-level screening ledger is not deposited. Identification $N_{\mathrm{rec}}=2{,}017$ is the search-log sum.\\Coded synthesis corpus after Sec.~gateway update: $N=44$ ($N_G=40$, $N_S=16$).};""",
)
prisma.write_text(p, encoding="utf-8")
print("updated", prisma.name)

pipe = ROOT / "figures" / "fig_graph_construction_pipeline.tex"
if pipe.exists():
    g = pipe.read_text(encoding="utf-8")
    g2 = g.replace(r"$N_G=36$", r"$N_G=40$").replace(
        r"$N_G=36$ papers; CL4KT excluded",
        r"$N_G=40$ papers; sequence-only SSL excluded",
    )
    pipe.write_text(g2, encoding="utf-8")
    print("updated", pipe.name, "changes", g != g2)

meta = ROOT / "figures" / "fig_meta_analysis_charts.tex"
if meta.exists():
    m = meta.read_text(encoding="utf-8")
    m2 = m.replace(r"$N_G=36$", r"$N_G=40$")
    meta.write_text(m2, encoding="utf-8")
    print("updated", meta.name, "changes", m != m2)
