# -*- coding: utf-8 -*-
from pathlib import Path

ROOT = Path(r"D:\TRINH\GraphSSL_KT_Survey")
TEX = [
    ROOT / "12_manuscript" / "TLT" / "main_tlt_anonymous.tex",
    ROOT / "12_manuscript" / "TLT" / "main_tlt_full.tex",
    ROOT / "12_manuscript" / "TLT" / "manuscript_TLT_FORMATTED_v1.3.tex",
]

SUB = r"""
\subsection{Full-Text Gateway Check after the Search}
\label{sec:gateway_ext}
On 22 November 2026 we read six in-window papers that sit outside the 37-paper coding tables. The gateway is unchanged: the paper studies knowledge tracing, and it uses an explicit graph or a self-supervised objective. DECKT \cite{DECKT_2025}, KT-Deeper \cite{Han_KTDeeper_2024}, and HCMKT \cite{HCMKT_2026} meet both tests. CoSKT \cite{CoSKT_2024}, DTransformer \cite{DTransformer_2023}, and SP-CLKT \cite{SPCLKT_2024} meet the self-supervised test and do not use an explicit graph. None of the six reports ECE or a zero-exposure KC split. They are not rows in the provenance, encoder, quality, or SSL-augmentation tables, and this reading does not show that they were among the $N_{\mathrm{rec}}=2{,}017$ search records, so the PRISMA arithmetic and those tables stay at 37. One further chapter, contrastive learning on a bipartite graph (DOI 10.1007/978-981-96-0821-8\_14), had no PDF and was not read.

"""

REPLACEMENTS = [
    (
        "yielding $N_G = 36$, $N_S = 9$, and $N_{G \\cap S} = 8$. Screening",
        "yielding $N_G = 36$, $N_S = 9$, and $N_{G \\cap S} = 8$. Six further in-window papers, read on 22 November 2026, meet the same gateway and are not rows in those tables; none reports ECE or a zero-exposure KC split (Sec.~\\ref{sec:gateway_ext}). Screening",
    ),
    (
        "\\subsection{Role of the AI Research Assistant}",
        SUB + "\\subsection{Role of the AI Research Assistant}",
    ),
    (
        "None of the 37 studies isolate a zero-exposure KC split. Item cold-start is YES for SINKT only ($1/37$).",
        "None of the 37 studies isolate a zero-exposure KC split. Item cold-start is YES for SINKT only ($1/37$). The six papers in Sec.~\\ref{sec:gateway_ext} likewise report no zero-exposure KC split.",
    ),
    (
        "None of the 37 manuscripts report ECE ($0/37$); a keyword scan of 36 PDFs finds no Brier score and one calibration plot (CL4KT).",
        "None of the 37 manuscripts report ECE ($0/37$); a keyword scan of 36 PDFs finds no Brier score and one calibration plot (CL4KT). The six papers in Sec.~\\ref{sec:gateway_ext} likewise report no ECE.",
    ),
    (
        "None of the 37 studies isolates a strict zero-exposure KC hold-out.",
        "None of the 37 studies isolates a strict zero-exposure KC hold-out. The six papers in Sec.~\\ref{sec:gateway_ext} likewise report no such split.",
    ),
    (
        "None of the 37 studies isolate a zero-exposure KC split; item cold-start is YES for SINKT only.",
        "None of the 37 studies isolate a zero-exposure KC split; item cold-start is YES for SINKT only. The six papers in Sec.~\\ref{sec:gateway_ext} likewise report no zero-exposure KC split.",
    ),
    (
        "only CL4KT is sequence-only SSL.",
        "only CL4KT is sequence-only SSL. Three papers read after this coding are also sequence-only SSL (Sec.~\\ref{sec:gateway_ext}).",
    ),
]


def newline_of(text):
    return "\r\n" if "\r\n" in text else "\n"


def apply_tex(path):
    text = path.read_text(encoding="utf-8")
    nl = newline_of(text)
    for old, new in REPLACEMENTS:
        old_n = old.replace("\n", nl)
        new_n = new.replace("\n", nl)
        count = text.count(old_n)
        if count != 1:
            raise SystemExit(f"{path.name}: expected 1 of {old[:60]!r}, found {count}")
        text = text.replace(old_n, new_n, 1)
    path.write_text(text, encoding="utf-8", newline="")


def main():
    for path in TEX:
        apply_tex(path)
        print("updated", path.name)


if __name__ == "__main__":
    main()
