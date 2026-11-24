import urllib.parse
import urllib.request

query = (
    '(Title:("knowledge tracing") OR Abstract:("knowledge tracing") OR Keyword:("knowledge tracing") '
    'OR Title:("student knowledge tracing") OR Abstract:("student knowledge tracing") OR Keyword:("student knowledge tracing")) '
    'AND (Title:(graph) OR Abstract:(graph) OR Keyword:(graph) '
    'OR Title:("graph neural network") OR Abstract:("graph neural network") OR Keyword:("graph neural network") '
    'OR Title:(GNN) OR Abstract:(GNN) OR Keyword:(GNN) '
    'OR Title:(GCN) OR Abstract:(GCN) OR Keyword:(GCN) '
    'OR Title:(GAT) OR Abstract:(GAT) OR Keyword:(GAT) '
    'OR Title:(hypergraph) OR Abstract:(hypergraph) OR Keyword:(hypergraph) '
    'OR Title:(heterogeneous) OR Abstract:(heterogeneous) OR Keyword:(heterogeneous) '
    'OR Title:("dynamic graph") OR Abstract:("dynamic graph") OR Keyword:("dynamic graph") '
    'OR Title:("temporal graph") OR Abstract:("temporal graph") OR Keyword:("temporal graph") '
    'OR Title:(prerequisite) OR Abstract:(prerequisite) OR Keyword:(prerequisite) '
    'OR Title:("concept map") OR Abstract:("concept map") OR Keyword:("concept map") '
    'OR Title:("skill graph") OR Abstract:("skill graph") OR Keyword:("skill graph") '
    'OR Title:("knowledge graph") OR Abstract:("knowledge graph") OR Keyword:("knowledge graph") '
    'OR Title:("concept graph") OR Abstract:("concept graph") OR Keyword:("concept graph") '
    'OR Title:("knowledge structure") OR Abstract:("knowledge structure") OR Keyword:("knowledge structure"))'
)
params = {
    "fillQuickSearch": "false",
    "target": "advanced",
    "expand": "dl",
    "field1": "AllField",
    "text1": query,
    "pageSize": "50",
    "startPage": "0",
}
url = "https://dl.acm.org/action/doSearch?" + urllib.parse.urlencode(params)
req = urllib.request.Request(url, headers={"User-Agent": "GraphSSL-KT-survey/1.0"})
with urllib.request.urlopen(req, timeout=60) as resp:
    body = resp.read()
    print("status", resp.status)
    print("final", resp.geturl())
    print("bytes", len(body))
open(r"D:\TRINH\GraphSSL_KT_Survey\audit\_srch001_page.html", "wb").write(body)
