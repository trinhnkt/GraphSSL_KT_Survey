from pathlib import Path
from pypdf import PdfReader

root = Path(r"D:\TRINH\GraphSSL_KT_Survey\14_references")
prov = {
    "KT023": "SGKT - Session Graph-Based Knowledge Tracing for Student Performance Prediction.pdf",
    "KT035": "HHSKT - A Learner-Question Interactions Based Heterogeneous Graph Neural Network Model for Knowledge Tracing.pdf",
    "KT050": "GraphCA - Learning From Graph Counterfactual Augmentation for Knowledge Tracing.pdf",
    "KT062": "LGS-KT - Integrating Logical and Grammatical Skills for Effective Programming Knowledge Tracing.pdf",
    "KT064": "Multi-Granularity Ensemble Interaction Graph Modeling for Knowledge Tracing.pdf",
    "KT065": "Graph Knowledge Tracing in Cognitive Situation - Validation of Classic Assertions in Cognitive Psychology.pdf",
    "KT069": "A Cross-Domain Knowledge Tracing Model Based on Graph Optimal Transport.pdf",
}
keys = ("session graph", "construct", "adjacency", "predefined", "learned", "heterogeneous graph", "optimal transport", "concept graph", "knowledge graph", "built")
lines = ["PROVENANCE"]
for pid, name in prov.items():
    path = root / name
    lines.append(f"\n## {pid} exists={path.exists()} file={name}")
    if not path.exists():
        continue
    reader = PdfReader(str(path))
    lines.append(f"pdf_pages={len(reader.pages)}")
    hits = 0
    for i, page in enumerate(reader.pages, 1):
        text = page.extract_text() or ""
        low = text.lower()
        for key in keys:
            j = low.find(key)
            if j >= 0:
                snippet = text[max(0, j - 90):j + 160].replace("\n", " ")
                lines.append(f"p{i} [{key}] {snippet}")
                hits += 1
                break
        if hits >= 6:
            break
    if hits == 0:
        lines.append("NO_TEXT_HIT")

ssl = {
    "KT011": ("Bi-CLKT - Bi-Graph Contrastive Learning Based Knowledge Tracing.pdf", ("contrastive", "subgraph", "dropout")),
    "KT026": ("Improving Knowledge Tracing via Pre-training Question Embeddings.pdf", ("reconstruct", "bipartite", "question-skill")),
    "KT042": ("Self-Supervised Heterogeneous Hypergraph Network for Knowledge Tracing.pdf", ("contrastive", "hyperedge", "mask")),
    "KT043": ("Weighted Heterogeneous Graph-Based Three-View Contrastive Learning for Knowledge Tracing in Personalized e-Learning Systems.pdf", ("contrastive", "three", "view")),
    "KT047": ("Fusing hybrid attentive network with self-supervised dual-channel heterogeneous graph for knowledge tracing.pdf", ("contrastive", "dual-channel", "mask")),
    "KT050": ("GraphCA - Learning From Graph Counterfactual Augmentation for Knowledge Tracing.pdf", ("infonce", "counterfactual", "perturb")),
    "KT066": ("Dual-Channel Adaptive Scale Hypergraph Encoders With Cross-View Contrastive Learning for Knowledge Tracing.pdf", ("infonce", "line-graph", "hypergraph")),
    "KT068": ("HKT - Hierarchical Structure-Based Knowledge Tracing.pdf", ("reconstruct", "hierarchical", "contrastive")),
}
lines.append("\nSSL")
for pid, (name, words) in ssl.items():
    path = root / name
    lines.append(f"\n## {pid} exists={path.exists()}")
    if not path.exists():
        continue
    reader = PdfReader(str(path))
    blob = "\n".join((p.extract_text() or "") for p in reader.pages).lower()
    for word in words:
        lines.append(f"{word}\t{blob.count(word.lower())}")

Path(r"D:\TRINH\GraphSSL_KT_Survey\audit\_prov_ssl_scan.txt").write_text("\n".join(lines), encoding="utf-8")
print("done", len(lines))
