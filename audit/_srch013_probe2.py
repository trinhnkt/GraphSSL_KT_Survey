import re
import urllib.parse
import urllib.request

params = [
    ("advanced", ""),
    ("terms-0-operator", "AND"),
    ("terms-0-term", '"knowledge tracing" OR "student knowledge tracing"'),
    ("terms-0-field", "title"),
    ("terms-1-operator", "OR"),
    ("terms-1-term", '"knowledge tracing" AND (graph OR GNN OR GCN OR GAT)'),
    ("terms-1-field", "abstract"),
    ("date-filter_by", "date_range"),
    ("date-from_date", "2015-01-01"),
    ("date-to_date", "2026-07-31"),
    ("date-date_type", "submitted_date"),
    ("abstracts", "show"),
    ("size", "50"),
]
url = "https://arxiv.org/search/advanced?" + urllib.parse.urlencode(params)
open(r"D:\TRINH\GraphSSL_KT_Survey\audit\_srch013_url.txt", "w", encoding="utf-8").write(url)
req = urllib.request.Request(url, headers={"User-Agent": "GraphSSL-KT-survey/1.0"})
html = urllib.request.urlopen(req, timeout=60).read().decode("utf-8", "replace")
open(r"D:\TRINH\GraphSSL_KT_Survey\audit\_srch013_page.html", "w", encoding="utf-8").write(html)
h1 = re.search(r"<h1[^>]*>[\s\S]*?</h1>", html)
print(re.sub(r"\s+", " ", h1.group(0)) if h1 else "no h1")
print(url)
