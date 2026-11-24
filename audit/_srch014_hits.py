from pathlib import Path

text = Path(r"D:\TRINH\GraphSSL_KT_Survey\03_search\exports\arxiv_qs_20261114.xml").read_text(encoding="utf-8")
print("entries", text.count("<entry>"))
needles = [
    "10.3390/e27070685",
    "dual-encoder contrastive",
    "deckt",
    "10.1145/3543507.3583255",
    "diagnostic transformer",
    "dtransformer",
    "10.1109/tlt.2024.3386750",
    "coskt",
    "self-paced contrastive",
    "10.1016/j.neucom.2024.128366",
    "novel contrastive view",
    "hcmkt",
    "10.1016/j.eswa.2025.128840",
    "978-981-96-0821-8",
    "bipartite graphs for interpretable",
    "dynamic heterogeneous graph contrastive",
    "10.1016/j.asoc.2024.112194",
]
low = text.lower()
for s in needles:
    print(("Y" if s.lower() in low else "N"), s)
