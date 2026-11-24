import json
import urllib.request
from pathlib import Path
from pypdf import PdfReader

root = Path(r"D:\TRINH\GraphSSL_KT_Survey")
out = []

dois = [
    "10.1609/aaai.v39i1.30500",
    "10.1145/3690624.3709500",
    "10.24963/ijcai.2025/450",
    "10.1145/3627673.3679900",
    "10.1016/j.neunet.2026.107500",
]
out.append("DOI RECHECK")
for d in dois:
    url = "https://api.crossref.org/works/" + d
    req = urllib.request.Request(url, headers={"User-Agent": "GraphSSL-KT-survey/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=40) as r:
            msg = json.load(r)["message"]
        title = (msg.get("title") or [""])[0]
        issued = msg.get("issued", {}).get("date-parts")
        container = (msg.get("container-title") or [""])[0]
        out.append(f"OK\t{d}\t{issued}\tpage={msg.get('page')}\t{container}\t{title}")
    except Exception as e:
        out.append(f"FAIL\t{d}\t{type(e).__name__}\t{e}")

pdfs = {
    "Piech": root / "14_references" / "Deep Knowledge Tracing.pdf",
    "SAKT": root / "14_references" / "A Self-Attentive Model for Knowledge Tracing.pdf",
    "pyKT": root / "14_references" / "pyKT - A Python Library to Benchmark Deep Learning based Knowledge Tracing Models.pdf",
    "DGMN": root / "14_references" / "Deep Graph Memory Networks for Forgetting-Robust Knowledge Tracing.pdf",
}
out.append("\nPDF HEADS")
for name, path in pdfs.items():
    reader = PdfReader(str(path))
    text = (reader.pages[0].extract_text() or "")[:1500].replace("\n", " ")
    last = (reader.pages[-1].extract_text() or "")[:400].replace("\n", " ")
    out.append(f"\n{name} pages={len(reader.pages)}")
    out.append(text)
    out.append("LAST " + last)

dest = root / "audit" / "_verify_2026_11_17.txt"
dest.write_text("\n".join(out), encoding="utf-8")
print("wrote", dest, "lines", len(out))
