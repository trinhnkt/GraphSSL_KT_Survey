from pathlib import Path
p = Path(r"D:\TRINH\GraphSSL_KT_Survey\03_search\exports\sciencedirect_qg_20261114.bib")
text = p.read_text(encoding="utf-8", errors="replace")
n = text.count("@article") + text.count("@inproceedings") + text.count("@incollection")
print("entries", n, "chars", len(text))
needles = [
    "10.3390/e27070685",
    "dual-encoder contrastive",
    "10.1145/3543507.3583255",
    "diagnostic transformer",
    "10.1109/tlt.2024.3386750",
    "coskt",
    "self-paced contrastive",
    "novel contrastive view",
    "hcmkt",
    "978-981-96-0821-8",
    "bipartite graphs for interpretable",
    "dynamic heterogeneous graph contrastive",
    "10.1016/j.asoc.2024.112194",
    "10.1016/j.eswa.2025.128840",
    "10.1016/j.neucom.2024.128366",
]
low = text.lower()
for s in needles:
    print(("Y" if s.lower() in low else "N"), s)
