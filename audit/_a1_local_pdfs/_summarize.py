import json
from pathlib import Path

p = Path(r"D:\TRINH\GraphSSL_KT_Survey\audit\_a1_local_pdfs\inventory.json")
data = json.loads(p.read_text(encoding="utf-8"))
lines = []
for row in data["files"]:
    title = " | ".join(row["title_lines"][:3])[:160]
    dois = ", ".join(row["dois_page1_2"][:3]) or "-"
    lines.append(
        f"{row['pages']:3} p1chars={row['chars_page1']:5} refpage={row['ref_start_page_1indexed']} doi={dois}"
    )
    lines.append(f"  FILE {row['file']}")
    lines.append(f"  HEAD {title}")
    if row["candidate_hits"]:
        lines.append(f"  HITS {row['candidate_hits']}")
Path(r"D:\TRINH\GraphSSL_KT_Survey\audit\_a1_local_pdfs\summary.txt").write_text(
    "\n".join(lines), encoding="utf-8"
)
print("wrote", len(data["files"]))
