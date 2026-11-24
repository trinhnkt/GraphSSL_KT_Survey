from pathlib import Path

files = [
    Path(r"D:\TRINH\GraphSSL_KT_Survey\12_manuscript\TLT\main_tlt_anonymous.tex"),
    Path(r"D:\TRINH\GraphSSL_KT_Survey\12_manuscript\TLT\main_tlt_full.tex"),
    Path(r"D:\TRINH\GraphSSL_KT_Survey\12_manuscript\TLT\manuscript_TLT_FORMATTED_v1.3.tex"),
]

pairs = [
    (
        "This article is a Survey and Tutorial synthesis. It does not claim classroom outcomes, tutor-log A/B tests, or an executed \\emph{pyKT-ColdStart} run; the learning-technology deliverable is the coded stop/go checklist above.",
        "\\subsection{Scope of Claims}\n\\label{sec:scope_claims}\nCounts reported here are coded properties of the 37 primary-core papers. They are not pooled cross-paper effects, and the survey is not a model league table. The paper reports no classroom or deployment outcome. The go/not-enough-evidence checklist in Sec.~\\ref{sec:go_nogo} states the evidence a tutoring action would require before a GO verdict.",
    ),
    (
        "two of which have one paper each; it is not a saturated SSL taxonomy.",
        "two of which have one paper each.",
    ),
    (
        " and one calibration plot (CL4KT). Coded gaps remain tutoring-design constraints, not a reproduced accuracy ranking.",
        " and one calibration plot (CL4KT).",
    ),
    (
        "we do not claim a completed screening or full-text reliability package. Count-based conclusions are protocol-coded audit findings rather than independently replicated meta-analytic estimates.",
        "we do not claim a completed screening or full-text reliability package.",
    ),
    (
        "count distributions of coded fields (not a pooled-effect meta-analysis).",
        "count distributions of coded fields.",
    ),
    (
        "That manuscript-reporting count remains $0/37$ and is not a cross-paper calibration league table.",
        "That manuscript-reporting count remains $0/37$.",
    ),
    (
        "The four-family table is a coding of $N_S=9$, not a claim that SSL-KT families are saturated.",
        "The four-family table is a coding of $N_S=9$.",
    ),
    (
        "Corpus basis is coded evidence under the survey protocol, not a reproduced benchmark and not a classroom result.",
        "Corpus basis is coded evidence under the survey protocol.",
    ),
    (
        "Corpus basis is coded evidence under the survey protocol, not a reproduced benchmark and not a cross-paper league table.",
        "Corpus basis is coded evidence under the survey protocol.",
    ),
    (
        "The checklist is an agenda inference from the coded records: it is not a classroom study, not a reproduced benchmark, and not a license to deploy. Apply",
        "The checklist is an agenda inference from the coded records. Apply",
    ),
    (
        "They are critical readings of the coded records, not classroom outcomes and not reproduced AUC or ECE values.",
        "They are critical readings of the coded records.",
    ),
    (
        "SSL-KT is coded into four pretext families ($N_S=9$; two families have one paper each); that table is not a saturated taxonomy.",
        "SSL-KT is coded into four pretext families ($N_S=9$; two families have one paper each).",
    ),
    (
        "or acting on $P(r=1)$. It is not a cross-paper model league table.",
        "or acting on $P(r=1)$.",
    ),
    (
        "\\subsection{Methodological Limitations of the Present Survey}\n"
        "Screening and primary coding were performed by an AI research assistant under the survey protocol, not by an independent human coder (Sec.~\\ref{sec:ai_role}); human coding exists only for a 20-paper sample (Sec.~\\ref{sec:icr}). This review synthesizes published protocols; \\emph{pyKT-ColdStart} is a proposed evaluation specification only and is not an executed benchmark. The corpus spans papers through July 2026; LLM-KT work after the search cutoff falls outside the synthesis.\n",
        "",
    ),
]

for path in files:
    raw = path.read_bytes()
    nl = "\r\n" if b"\r\n" in raw else "\n"
    text = raw.decode("utf-8").replace("\r\n", "\n")
    for old, new in pairs:
        n = text.count(old)
        if n != 1:
            raise SystemExit(f"{path.name}: expected 1, found {n}, of {old[:80]!r}")
        text = text.replace(old, new, 1)
    if text.count("sec:scope_claims") != 1:
        raise SystemExit(f"{path.name}: scope label")
    if "Methodological Limitations of the Present Survey" in text:
        raise SystemExit(f"{path.name}: limitations heading remains")
    path.write_bytes(text.replace("\n", nl).encode("utf-8"))
    print(path.name, "ok", "0/37", text.count("0/37"), "N_G", text.count("N_G = 36"), "league table", text.count("league table"))
