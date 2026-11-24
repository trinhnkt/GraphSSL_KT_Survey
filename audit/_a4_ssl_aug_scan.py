import re
from pathlib import Path
import fitz

root = Path(r"D:\TRINH\GraphSSL_KT_Survey\14_references")
files = {
    "KT011": "Bi-CLKT - Bi-Graph Contrastive Learning Based Knowledge Tracing.pdf",
    "KT026": "Improving Knowledge Tracing via Pre-training Question Embeddings.pdf",
    "KT042": "Self-Supervised Heterogeneous Hypergraph Network for Knowledge Tracing.pdf",
    "KT043": "Weighted Heterogeneous Graph-Based Three-View Contrastive Learning for Knowledge Tracing in Personalized e-Learning Systems.pdf",
    "KT047": "Fusing Hybrid Attentive Network with Self-Supervised Dual-Channel Heterogeneous Graph for Knowledge Tracing.pdf",
    "KT050": "GraphCA - Learning From Graph Counterfactual Augmentation for Knowledge Tracing.pdf",
    "KT066": "Dual-Channel Adaptive Scale Hypergraph Encoders With Cross-View Contrastive Learning for Knowledge Tracing.pdf",
    "KT068": "HKT - Hierarchical Structure-Based Knowledge Tracing.pdf",
}
pat = re.compile(
    r"augment|dropout|drop edge|edge drop|mask|perturb|counterfactual|reconstruct|pretext|InfoNCE|contrastive view|subgraph",
    re.I,
)
out = []
for key, name in files.items():
    path = root / name
    out.append(f"\n######## {key} exists={path.exists()} ########\n")
    if not path.exists():
        continue
    doc = fitz.open(path)
    # page-level so locators are real
    for i, page in enumerate(doc, start=1):
        text = re.sub(r"\s+", " ", page.get_text())
        hits = list(pat.finditer(text))
        if not hits:
            continue
        out.append(f"\n--- {key} p.{i} hits={len(hits)} ---\n")
        for match in hits[:4]:
            start = max(0, match.start() - 80)
            end = min(len(text), match.end() + 100)
            out.append(text[start:end] + "\n")
    doc.close()
Path(r"D:\TRINH\GraphSSL_KT_Survey\audit\_a4_ssl_aug_contexts.txt").write_text("".join(out), encoding="utf-8")
print("chars", len("".join(out)))
