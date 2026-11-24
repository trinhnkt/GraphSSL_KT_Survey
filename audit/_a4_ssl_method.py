import re
from pathlib import Path
import fitz

root = Path(r"D:\TRINH\GraphSSL_KT_Survey\14_references")
jobs = [
    ("KT011", "Bi-CLKT - Bi-Graph Contrastive Learning Based Knowledge Tracing.pdf", [6, 7], r"augment|corrupt|eliminat|PageRank|centrality|edge"),
    ("KT026", "Improving Knowledge Tracing via Pre-training Question Embeddings.pdf", [1, 2, 3, 4], r"reconstruct|pre-train|pretrain|bipartite|question-skill|relation"),
    ("KT042", "Self-Supervised Heterogeneous Hypergraph Network for Knowledge Tracing.pdf", [8, 9], r"dropout|hyperedge|augment|node"),
    ("KT043", "Weighted Heterogeneous Graph-Based Three-View Contrastive Learning for Knowledge Tracing in Personalized e-Learning Systems.pdf", [3, 4, 5, 6], r"view|mask|contrast|perturb|meta-path"),
    ("KT047", "Fusing Hybrid Attentive Network with Self-Supervised Dual-Channel Heterogeneous Graph for Knowledge Tracing.pdf", [4, 5, 6], r"channel|view|mask|contrast|InfoNCE"),
    ("KT050", "GraphCA - Learning From Graph Counterfactual Augmentation for Knowledge Tracing.pdf", [5, 6], r"counterfactual|perturb|edge|augment|subgraph"),
    ("KT066", "Dual-Channel Adaptive Scale Hypergraph Encoders With Cross-View Contrastive Learning for Knowledge Tracing.pdf", [7, 8, 10, 11], r"line graph|augment|hypergraph|mask|view"),
    ("KT068", "HKT - Hierarchical Structure-Based Knowledge Tracing.pdf", [5, 7, 8], r"reconstruct|contrast|hierarch|perturb|drop"),
]
out = []
for key, name, pages, pattern in jobs:
    doc = fitz.open(root / name)
    pat = re.compile(pattern, re.I)
    out.append(f"\n######## {key} ########\n")
    for p in pages:
        text = re.sub(r"\s+", " ", doc[p - 1].get_text())
        hits = list(pat.finditer(text))
        out.append(f"\n--- p.{p} hits={len(hits)} ---\n")
        for match in hits[:5]:
            start = max(0, match.start() - 120)
            end = min(len(text), match.end() + 160)
            out.append(text[start:end] + "\n")
    doc.close()
Path(r"D:\TRINH\GraphSSL_KT_Survey\audit\_a4_ssl_method.txt").write_text("".join(out), encoding="utf-8")
print("chars", sum(len(x) for x in out))
