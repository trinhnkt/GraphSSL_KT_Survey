import fitz
from pathlib import Path

root = Path(r"D:\TRINH\GraphSSL_KT_Survey\14_references")
queries = {
    "A Cross-Domain Knowledge Tracing Model Based on Graph Optimal Transport.pdf": ["dynamic heterogeneous graph contrastive"],
    "A Survey of Knowledge Tracing - Models, Variants, and Applications.pdf": ["diagnostic transformer"],
    "Deep Learning Based Knowledge Tracing A Review, a Tool and Empirical Studies.pdf": ["diagnostic transformer"],
    "Denoising Programming Knowledge Tracing with a Code Graph-based Tuning Adaptor.pdf": ["diagnostic transformer"],
    "HKT - Hierarchical Structure-Based Knowledge Tracing.pdf": ["diagnostic transformer"],
    "Multi-Granularity Ensemble Interaction Graph Modeling for Knowledge Tracing.pdf": ["diagnostic transformer"],
    "A Survey of Graph-Based Knowledge Tracing from Structural and Propagation Perspectives - Models, Applications, and Future Directions.pdf": [
        "deckt",
        "dual-encoder",
        "dtransformer",
        "diagnostic transformer",
        "self-paced",
        "coskt",
        "hcmkt",
        "bipartite",
        "dynamic heterogeneous graph contrastive",
        "10.3390/e27070685",
    ],
}
out = []
for name, needles in queries.items():
    doc = fitz.open(root / name)
    out.append("=" * 20 + " " + name)
    for i, page in enumerate(doc):
        text = page.get_text("text") or ""
        low = text.lower()
        for needle in needles:
            pos = low.find(needle.lower())
            if pos < 0:
                continue
            start = max(0, pos - 180)
            end = min(len(text), pos + len(needle) + 220)
            snippet = " ".join(text[start:end].split())
            out.append(f"p.{i+1} [{needle}] {snippet}")
    doc.close()
Path(r"D:\TRINH\GraphSSL_KT_Survey\audit\_a1_local_pdfs\hit_context.txt").write_text(
    "\n".join(out), encoding="utf-8"
)
print("lines", len(out))
