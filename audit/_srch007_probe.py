import re
import urllib.parse
import urllib.request

q = '("knowledge tracing" OR "student knowledge tracing") AND (graph OR "graph neural network" OR GNN OR GCN OR GAT OR hypergraph)'
params = {
    "query": q,
    "date-facet-mode": "between",
    "facet-start-year": "2015",
    "facet-end-year": "2026",
}
url = "https://link.springer.com/search?" + urllib.parse.urlencode(params)
req = urllib.request.Request(
    url,
    headers={"User-Agent": "Mozilla/5.0 (compatible; GraphSSL-KT-survey/1.0)"},
)
try:
    html = urllib.request.urlopen(req, timeout=45).read().decode("utf-8", "replace")
except Exception as e:
    open(r"D:\TRINH\GraphSSL_KT_Survey\audit\_srch007_url.txt", "w", encoding="utf-8").write(url + "\nERROR " + str(e))
    raise
open(r"D:\TRINH\GraphSSL_KT_Survey\audit\_srch007_url.txt", "w", encoding="utf-8").write(url)
open(r"D:\TRINH\GraphSSL_KT_Survey\audit\_srch007_page.html", "w", encoding="utf-8").write(html[:200000])
print("len", len(html))
for pat in [r"[0-9,]+\s+results", r"result-count[^<]{0,40}", r"Showing[^<]{0,80}"]:
    m = re.search(pat, html, re.I)
    print(pat, "=>", (m.group(0)[:120] if m else "NONE"))
print(url)
