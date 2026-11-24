import re
import urllib.parse
import urllib.request

q = (
    'ti:("knowledge tracing" OR "student knowledge tracing") '
    'OR abs:("knowledge tracing" AND (graph OR GNN OR GCN OR GAT))'
)
params = {
    "advanced": "",
    "terms-0-operator": "AND",
    "terms-0-term": q,
    "terms-0-field": "all",
    "date-filter_by": "date_range",
    "date-from_date": "2015-01-01",
    "date-to_date": "2026-07-31",
    "date-date_type": "submitted_date",
    "abstracts": "show",
    "size": "50",
    "order": "-announced_date_first",
}
url = "https://arxiv.org/search/advanced?" + urllib.parse.urlencode(params)
Path_out = r"D:\TRINH\GraphSSL_KT_Survey\audit\_srch013_url.txt"
open(Path_out, "w", encoding="utf-8").write(url + "\n")
req = urllib.request.Request(url, headers={"User-Agent": "GraphSSL-KT-survey/1.0"})
html = urllib.request.urlopen(req, timeout=60).read().decode("utf-8", "replace")
open(r"D:\TRINH\GraphSSL_KT_Survey\audit\_srch013_page.html", "w", encoding="utf-8").write(html)
for pat in [
    r"Showing[\s\S]{0,80}?results",
    r"of\s+[0-9,]+\s+results",
    r"[0-9,]+\s+results",
]:
    m = re.search(pat, html, re.I)
    print(pat, "=>", (m.group(0).replace("\n", " ") if m else "NONE"))
print("html_len", len(html))
