from pathlib import Path

files = [
    Path(r"D:\TRINH\GraphSSL_KT_Survey\12_manuscript\TLT\main_tlt_anonymous.tex"),
    Path(r"D:\TRINH\GraphSSL_KT_Survey\12_manuscript\TLT\main_tlt_full.tex"),
    Path(r"D:\TRINH\GraphSSL_KT_Survey\12_manuscript\TLT\manuscript_TLT_FORMATTED_v1.3.tex"),
]

pairs = [
    (
        "manuscript-reporting audit $0/37$; one REPRODUCED overlay in Sec.~\\ref{sec:reliability}",
        "manuscript-reporting audit $0/37$",
    ),
    (
        "an ECE manuscript-reporting audit ($0/37$) plus one survey-computed overlay, and the go/not-enough-evidence checklist",
        "an ECE manuscript-reporting audit ($0/37$), and the go/not-enough-evidence checklist",
    ),
    (
        "Manuscript ECE $0/37$; one survey-computed overlay",
        "Manuscript ECE $0/37$",
    ),
    (
        " and one calibration plot (CL4KT). One survey-computed ECE overlay (DyGKT/ASSIST17; one model, one dataset, one seed) shows calibration can be measured from author artifacts; it does not establish corpus-wide calibration. Coded gaps remain",
        " and one calibration plot (CL4KT). Coded gaps remain",
    ),
    (
        "The DyGKT ECE overlay (Sec.~\\ref{sec:reliability}) and the venue-extension probe (Sec.~\\ref{sec:venue_ext}) were not specified in the survey protocol.",
        "The venue-extension probe (Sec.~\\ref{sec:venue_ext}) was not specified in the survey protocol.",
    ),
    (
        " The DyGKT/ASSIST17 survey-computed ECE overlay in Sec.~\\ref{sec:reliability} demonstrates a measurable calibration number on one author codebase (single model/dataset/seed); it does not establish calibration for the corpus as a whole, is not a tutoring decision rule, and does not flip this corpus verdict.",
        "",
    ),
    (
        " The DyGKT/ASSIST17 overlay in Sec.~\\ref{sec:reliability} is survey-computed (survey-computed) on a single model/dataset/seed and does not close that manuscript-reporting gap or establish corpus-wide calibration.",
        "",
    ),
    (
        " One survey-computed ECE overlay on DyGKT/ASSIST17 is reported in Sec.~\\ref{sec:reliability}; it is not a corpus re-ranking.",
        "",
    ),
    (
        " A single survey-computed equal-width ECE overlay on DyGKT/ASSIST17 (Sec.~\\ref{sec:reliability}) shows calibration can be measured from author artifacts on one model/dataset/seed; it does not establish corpus-wide calibration, and raw $P(r=1)$ remains",
        " Raw $P(r=1)$ remains",
    ),
]

block = (
    "As a single survey-computed overlay---not a manuscript-reported corpus fact---we ran the author DyGKT implementation \\cite{KT038_DyGKT_2024} on ASSIST17 (seed~$0$, author train/val/test ratios, transductive test edges, $n=94{,}156$) and obtained equal-width ECE~$=0.0361$ and Brier~$=0.1770$ (author-metric test AUC~$=0.8025$). That overlay is one model, one dataset, and one seed; it is not a benchmark ranking. It shows calibration \\emph{can} be measured when author artifacts are available; it does not change the $0/37$ manuscript-reporting claim, does not establish calibration for the corpus as a whole, and does not license corpus-wide tutoring actions from raw $P(r=1)$. Implications for tutoring decisions remain in Table~\\ref{tab:its_implications}; the supplementary package records the reproduction manifest, run log, and per-bin table.\n"
    "\n"
    "\\textbf{Why DyGKT, and which setting.} DyGKT was chosen on practical grounds: its authors release a repository with bundled processed ASSIST17 data and an evaluation script. No systematic selection among corpus models is documented and no other model was run, so the overlay is a convenience demonstration and not a sample of Graph-KT. The setting is \\emph{transductive}: probabilities are sigmoid outputs on time-ordered held-out test edges (author split 0.8/0.1/0.1) among nodes seen during training. ECE was not computed for the author's new-node (inductive) test pass (author-metric AUC $0.8035$), so the overlay carries no information about zero-exposure KC or item cold-start.\n"
)

for path in files:
    raw = path.read_bytes()
    nl = b"\r\n" if b"\r\n" in raw else b"\n"
    text = raw.decode("utf-8")
    work = text.replace("\r\n", "\n")
    if block not in work:
        raise SystemExit(f"BLOCK MISSING {path.name}")
    work = work.replace(block, "")
    for old, new in pairs:
        n = work.count(old)
        if n != 1:
            raise SystemExit(f"{path.name}: expected 1 of {old[:60]!r}, found {n}")
        work = work.replace(old, new, 1)
    path.write_bytes(work.replace("\n", nl.decode("ascii")).encode("utf-8"))
    print(path.name, "ok", "0.0361", work.count("0.0361"), "DyGKT", work.count("DyGKT"), "0/37", work.count("0/37"))
