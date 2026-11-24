from pathlib import Path

files = [
    Path(r"D:\TRINH\GraphSSL_KT_Survey\12_manuscript\TLT\main_tlt_anonymous.tex"),
    Path(r"D:\TRINH\GraphSSL_KT_Survey\12_manuscript\TLT\main_tlt_full.tex"),
    Path(r"D:\TRINH\GraphSSL_KT_Survey\12_manuscript\TLT\manuscript_TLT_FORMATTED_v1.3.tex"),
]

old_intro = (
    "Table~\\ref{tab:survey_comparison} records those differences of scope.\n"
)
new_intro = (
    "Table~\\ref{tab:survey_comparison} records those differences of scope. "
    "Shukurlu \\cite{Shukurlu_LossKT_2025} reviews loss-augmented KT, including the contrastive losses of Bi-CLKT, SP-CLKT, CL4KT, and CoSKT (that survey's Sec.~4 and Table~1), and names GKT only in related work (its Sec.~2). "
    "That survey is not a graph-provenance coding and has no ECE section. "
    "The $0/37$ ECE count in this paper is the manuscript-reporting result inside the Graph/SSL primary corpus; calibration studies outside that corpus are not coded here.\n"
)

old_spec = (
    "\\begin{tabular}{@{}>{\\raggedright\\arraybackslash}p{2.15cm}\n"
    ">{\\raggedright\\arraybackslash}p{2.25cm}\n"
    ">{\\raggedright\\arraybackslash}p{2.35cm}\n"
    ">{\\raggedright\\arraybackslash}p{2.25cm}\n"
    ">{\\raggedright\\arraybackslash}p{2.35cm}\n"
    ">{\\raggedright\\arraybackslash}p{2.55cm}@{}}\n"
)
new_spec = (
    "\\begin{tabular}{@{}>{\\raggedright\\arraybackslash}p{1.85cm}\n"
    ">{\\raggedright\\arraybackslash}p{1.85cm}\n"
    ">{\\raggedright\\arraybackslash}p{1.9cm}\n"
    ">{\\raggedright\\arraybackslash}p{1.85cm}\n"
    ">{\\raggedright\\arraybackslash}p{1.9cm}\n"
    ">{\\raggedright\\arraybackslash}p{2.05cm}\n"
    ">{\\raggedright\\arraybackslash}p{2.15cm}@{}}\n"
)

rows = [
    (
        "\\textbf{Dimension} & \\cite{Abdelrahman_Survey_2023} & \\cite{Liu_pyKT_2022,Liu_DLKT_2025} & \\cite{Shen_KTSurvey_2024} & \\cite{Xu_GbKT_2026} & \\textbf{This survey} \\\\",
        "\\textbf{Dimension} & \\cite{Abdelrahman_Survey_2023} & \\cite{Liu_pyKT_2022,Liu_DLKT_2025} & \\cite{Shen_KTSurvey_2024} & \\cite{Xu_GbKT_2026} & \\cite{Shukurlu_LossKT_2025} & \\textbf{This survey} \\\\",
    ),
    (
        "Protocol & Narrative / semi-systematic & Empirical tool + review & Narrative TLT review & Graph-KT survey (JEDM) & 37 PDFs; search-log $N=2{,}017$; no screening ledger \\\\",
        "Protocol & Narrative / semi-systematic & Empirical tool + review & Narrative TLT review & Graph-KT survey (JEDM) & Loss review; five models (Sec.~4) & 37 PDFs; search-log $N=2{,}017$; no screening ledger \\\\",
    ),
    (
        "Graph-KT & High-level GNN overview & Sequence-first; GKT as one DLKT model & Graph-KT as one DL variant & Structure $\\times$ propagation & Provenance $\\times$ encoder ($N_G=36$) \\\\",
        "Graph-KT & High-level GNN overview & Sequence-first; GKT as one DLKT model & Graph-KT as one DL variant & Structure $\\times$ propagation & GKT named only (Sec.~2) & Provenance $\\times$ encoder ($N_G=36$) \\\\",
    ),
    (
        "SSL-KT & Minimal / none & Not an SSL-KT taxonomy & Not a dedicated SSL-KT taxonomy & Not an SSL-KT survey & S-criterion coding table; 4 families ($N_S=9$; 2 families $n=1$) \\\\",
        "SSL-KT & Minimal / none & Not an SSL-KT taxonomy & Not a dedicated SSL-KT taxonomy & Not an SSL-KT survey & Four contrastive losses (Table~1) & S-criterion coding table; 4 families ($N_S=9$; 2 families $n=1$) \\\\",
    ),
    (
        "Sparse / cold-start & Generic sparsity & Standard interaction splits & Learning-process variants & Dataset catalogue, not a zero-exposure ontology & Interaction sparsity vs item / learner / strict KC \\\\",
        "Sparse / cold-start & Generic sparsity & Standard interaction splits & Learning-process variants & Dataset catalogue, not a zero-exposure ontology & Data sparsity named (Sec.~1) & Interaction sparsity vs item / learner / strict KC \\\\",
    ),
    (
        "Provenance / split & Not audited & Benchmark splits for DLKT & Not audited & Not a leakage/provenance audit & Split/provenance coded; no leakage \\% \\\\",
        "Provenance / split & Not audited & Benchmark splits for DLKT & Not audited & Not a leakage/provenance audit & Not a provenance audit & Split/provenance coded; no leakage \\% \\\\",
    ),
    (
        "ECE / trust & Not evaluated & AUC / ACC emphasis & Not evaluated & Not an ECE audit & Manuscript ECE $0/37$ \\\\",
        "ECE / trust & Not evaluated & AUC / ACC emphasis & Not evaluated & Not an ECE audit & No ECE section & Manuscript ECE $0/37$ \\\\",
    ),
    (
        "Learning-technology use & Broad KT applications & Shared experimental protocol & Models, variants, applications & Graph structure for EDM & T1--T3 evidence-to-GO for ITS / adaptive / formative use \\\\",
        "Learning-technology use & Broad KT applications & Shared experimental protocol & Models, variants, applications & Graph structure for EDM & Deployment named (abstract) & T1--T3 evidence-to-GO for ITS / adaptive / formative use \\\\",
    ),
    (
        "Artifacts & Citation index & pyKT repository & EduData / EduKTM & Dataset guidance & QA6 author-artifact coding; supplementary labels \\\\",
        "Artifacts & Citation index & pyKT repository & EduData / EduKTM & Dataset guidance & Table~1 loss summary & QA6 author-artifact coding; supplementary labels \\\\",
    ),
]

for path in files:
    raw = path.read_bytes()
    nl = "\r\n" if b"\r\n" in raw else "\n"
    text = raw.decode("utf-8").replace("\r\n", "\n")
    if text.count(old_intro) != 1:
        raise SystemExit(f"{path.name}: intro {text.count(old_intro)}")
    text = text.replace(old_intro, new_intro, 1)
    if text.count(old_spec) != 1:
        raise SystemExit(f"{path.name}: spec {text.count(old_spec)}")
    text = text.replace(old_spec, new_spec, 1)
    for old, new in rows:
        n = text.count(old)
        if n != 1:
            raise SystemExit(f"{path.name}: row {n} {old[:60]!r}")
        text = text.replace(old, new, 1)
    if text.count("Shukurlu_LossKT_2025") != 2:
        raise SystemExit(f"{path.name}: cite count {text.count('Shukurlu_LossKT_2025')}")
    path.write_bytes(text.replace("\n", nl).encode("utf-8"))
    print(path.name, "ok", "0/37", text.count("0/37"))
