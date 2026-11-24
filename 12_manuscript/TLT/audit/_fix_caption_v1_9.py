import io, os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
pairs = [
    (" File: \\texttt{supplementary/graph\\_provenance\\_x\\_encoder\\_crosstab\\_v1.9.csv}.}", "}"),
    ("Table~\\ref{tab:prov_encoder} reports distribution only.",
     "Table~\\ref{tab:prov_encoder} reports distribution only (file: \\path{supplementary/graph_provenance_x_encoder_crosstab_v1.9.csv})."),
]
for f in ['main_tlt_anonymous.tex', 'main_tlt_full.tex', 'manuscript_TLT_FORMATTED_v1.3.tex']:
    p = os.path.join(BASE, f)
    t = io.open(p, encoding='utf-8', newline='').read()
    for a, b in pairs:
        assert t.count(a) == 1, (f, a)
        t = t.replace(a, b)
    io.open(p, 'w', encoding='utf-8', newline='').write(t)
print('ok')
