import time
import urllib.parse
import urllib.request
from pathlib import Path

q = (
    '((ti:"knowledge tracing" OR ti:"student knowledge tracing") OR '
    '(abs:"knowledge tracing" AND (abs:graph OR abs:GNN OR abs:GCN OR abs:GAT))) '
    "AND submittedDate:[201501010000 TO 202607312359]"
)
out = Path(r"D:\TRINH\GraphSSL_KT_Survey\03_search\exports\arxiv_qg_20261114.xml")
chunks = []
start = 0
page = 200
total = None
while True:
    url = (
        "http://export.arxiv.org/api/query?search_query="
        + urllib.parse.quote(q)
        + f"&start={start}&max_results={page}"
    )
    req = urllib.request.Request(url, headers={"User-Agent": "GraphSSL-KT-survey/1.0"})
    text = urllib.request.urlopen(req, timeout=90).read().decode("utf-8", "replace")
    if total is None:
        i = text.find("totalResults>")
        j = text.find("<", i + 13)
        total = int(text[i + 13 : j])
        print("total", total)
    chunks.append(text)
    got = text.count("<entry>")
    print("start", start, "got", got)
    start += got
    if got == 0 or start >= total:
        break
    time.sleep(3)

out.write_text("\n".join(chunks), encoding="utf-8")
print("wrote", out, "entries", sum(c.count("<entry>") for c in chunks))
