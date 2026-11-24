import urllib.parse
import urllib.request

q = (
    '((ti:"knowledge tracing" OR ti:"student knowledge tracing") OR '
    '(abs:"knowledge tracing" AND (abs:graph OR abs:GNN OR abs:GCN OR abs:GAT))) '
    'AND submittedDate:[201501010000 TO 202607312359]'
)
url = (
    "http://export.arxiv.org/api/query?search_query="
    + urllib.parse.quote(q)
    + "&start=0&max_results=1"
)
req = urllib.request.Request(url, headers={"User-Agent": "GraphSSL-KT-survey/1.0"})
t = urllib.request.urlopen(req, timeout=60).read().decode("utf-8", "replace")
i = t.find("totalResults")
print(t[i:i+80])
print("QUERY", q)
