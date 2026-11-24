import time
import urllib.request
from pathlib import Path

ids = Path(r"D:\TRINH\GraphSSL_KT_Survey\audit\_srch014_ids.txt").read_text(encoding="utf-8").split()
out = Path(r"D:\TRINH\GraphSSL_KT_Survey\03_search\exports\arxiv_qs_20261114.xml")
chunks = []
for start in range(0, len(ids), 50):
    batch = ids[start : start + 50]
    url = (
        "http://export.arxiv.org/api/query?id_list="
        + ",".join(batch)
        + f"&start=0&max_results={len(batch)}"
    )
    req = urllib.request.Request(url, headers={"User-Agent": "GraphSSL-KT-survey/1.0"})
    text = urllib.request.urlopen(req, timeout=90).read().decode("utf-8", "replace")
    print("batch", start, "entries", text.count("<entry>"))
    chunks.append(text)
    time.sleep(3)
out.write_text("\n".join(chunks), encoding="utf-8")
print("wrote", sum(c.count("<entry>") for c in chunks))
