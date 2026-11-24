"""Extract keyword passages from the 20 IRR PDFs. No codes assigned."""
from __future__ import annotations

import json
import re
from pathlib import Path

import fitz

ROOT = Path(r"D:\TRINH\GraphSSL_KT_Survey")
REF = ROOT / "14_references"
OUT = ROOT / "08_quality_reliability" / "_locator_raw.json"

PAPERS = {
    "KT004": "Graph-based Knowledge Tracing - Modeling Student Proficiency Using Graph Neural Network.pdf",
    "KT011": "Bi-CLKT - Bi-Graph Contrastive Learning Based Knowledge Tracing.pdf",
    "KT014": "Prerequisite-Driven Deep Knowledge Tracing.pdf",
    "KT026": "Improving Knowledge Tracing via Pre-training Question Embeddings.pdf",
    "KT031": "Knowledge Structure Enhanced Graph Representation Learning Model for Attentive Knowledge Tracing.pdf",
    "KT035": "HHSKT - A Learner-Question Interactions Based Heterogeneous Graph Neural Network Model for Knowledge Tracing.pdf",
    "KT037": "CMKT - Concept Map Driven Knowledge Tracing.pdf",
    "KT038": "DyGKT - Dynamic Graph Learning for Knowledge Tracing.pdf",
    "KT039": "Contrastive Learning for Knowledge Tracing.pdf",
    "KT042": "Self-Supervised Heterogeneous Hypergraph Network for Knowledge Tracing.pdf",
    "KT043": "Weighted Heterogeneous Graph-Based Three-View Contrastive Learning for Knowledge Tracing in Personalized e-Learning Systems.pdf",
    "KT044": "SINKT - A Structure-Aware Inductive Knowledge Tracing Model with Large Language Model.pdf",
    "KT047": "Fusing Hybrid Attentive Network with Self-Supervised Dual-Channel Heterogeneous Graph for Knowledge Tracing.pdf",
    "KT050": "GraphCA - Learning From Graph Counterfactual Augmentation for Knowledge Tracing.pdf",
    "KT066": "Dual-Channel Adaptive Scale Hypergraph Encoders With Cross-View Contrastive Learning for Knowledge Tracing.pdf",
    "KT068": "HKT - Hierarchical Structure-Based Knowledge Tracing.pdf",
    "KT070": "Denoising Programming Knowledge Tracing with a Code Graph-based Tuning Adaptor.pdf",
    "KT076": "KGNN-KT - Enhancing Knowledge Tracing in Programming Education Through LLM-Extracted Knowledge Graphs.pdf",
    "KT077": "R2GCurL - Reinforced Robust Knowledge Tracing via Dynamic Graph Curriculum Learning.pdf",
    "KT079": "Spatio-Temporal Fusion in Graph Neural Network for Streaming Knowledge Tracing.pdf",
}

# Keep patterns broad; human assigns codes.
PATTERNS = {
    "ssl_pretext": r"self[- ]supervis|contrastive|info\s*nce|pretext|reconstruct|masked |autoencod|consistency loss|pre-train|pretrain",
    "graph_encoder": r"\bGCN\b|\bGAT\b|\bGNN\b|graph convolution|graph attention|hypergraph|message passing|heterogeneous graph|dynamic graph|adjacency",
    "graph_source": r"prerequisite|concept map|expert|Q-matrix|co-occurrence|construct(?:ed|ion) the graph|knowledge graph|LLM|large language",
    "cold_start": r"cold[- ]start|zero[- ]shot|unseen concept|unseen skill|unseen question|new concept|new skill|new question|new item|new student|zero exposure|hold[- ]out",
    "ece_cal": r"\bECE\b|expected calibration|calibration error|Brier|reliability diagram|calibrat",
}

WINDOW = 420


def normalize(text: str) -> str:
    text = text.replace("\x00", " ")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def snippets(page_text: str, pattern: str, limit: int = 3) -> list[str]:
    hits = []
    for m in re.finditer(pattern, page_text, flags=re.I):
        start = max(0, m.start() - WINDOW // 2)
        end = min(len(page_text), m.end() + WINDOW // 2)
        chunk = normalize(page_text[start:end]).replace("\n", " ")
        chunk = re.sub(r"\s+", " ", chunk)
        if len(chunk) < 40:
            continue
        if chunk not in hits:
            hits.append(chunk)
        if len(hits) >= limit:
            break
    return hits


def main() -> None:
    report = {}
    for pid, name in PAPERS.items():
        path = REF / name
        rec = {
            "file": name,
            "exists": path.exists(),
            "pages": 0,
            "chars": 0,
            "extractable": False,
            "hits": {k: [] for k in PATTERNS},
        }
        if not path.exists():
            report[pid] = rec
            continue
        doc = fitz.open(path)
        rec["pages"] = doc.page_count
        full = []
        for i, page in enumerate(doc, start=1):
            text = page.get_text("text") or ""
            rec["chars"] += len(text)
            full.append(text)
            for key, pat in PATTERNS.items():
                for snip in snippets(text, pat, limit=2):
                    rec["hits"][key].append({"page": i, "text": snip})
        rec["extractable"] = rec["chars"] > 400
        # cap hits per bucket
        for key in rec["hits"]:
            rec["hits"][key] = rec["hits"][key][:6]
        doc.close()
        report[pid] = rec

    OUT.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"wrote {OUT}")
    for pid, rec in report.items():
        n = sum(len(v) for v in rec["hits"].values())
        print(f"{pid} pages={rec['pages']} chars={rec['chars']} extractable={rec['extractable']} hits={n}")


if __name__ == "__main__":
    main()
