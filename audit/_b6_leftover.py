import re
from pathlib import Path

root = Path(r"D:\TRINH\GraphSSL_KT_Survey\12_manuscript\TLT")
files = [
    root / "main_tlt_anonymous.tex",
    root / "main_tlt_full.tex",
    root / "manuscript_TLT_FORMATTED_v1.3.tex",
    root / "figures" / "fig_ssl_framework.tex",
    root / "figures" / "fig_taxonomy_2d.tex",
    root / "figures" / "fig_graph_construction_pipeline.tex",
    root / "figures" / "fig_meta_analysis_charts.tex",
    root / "figures" / "fig_prisma_flow.tex",
]
pat = re.compile(r"locked|Sec\.~?14|Sec\.~?22\.1|\.csv|\\_[A-Z]|PRIMARY\\_CORE|Mechanism notes", re.I)
for f in files:
    t = f.read_text(encoding="utf-8")
    print("==", f.name)
    for i, line in enumerate(t.splitlines(), 1):
        if pat.search(line):
            print(f"{i}: {line.strip()[:240]}")
