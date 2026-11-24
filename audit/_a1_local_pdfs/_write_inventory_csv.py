import csv
import json
from pathlib import Path

inv = json.loads(
    Path(r"D:\TRINH\GraphSSL_KT_Survey\audit\_a1_local_pdfs\inventory.json").read_text(
        encoding="utf-8"
    )
)

ROLE = {
    "Deep Knowledge Tracing.pdf": "BASELINE",
    "A Self-Attentive Model for Knowledge Tracing.pdf": "BASELINE",
    "Context-Aware Attentive Knowledge Tracing.pdf": "BASELINE",
    "Dynamic Key-Value Memory Networks for Knowledge Tracing.pdf": "BASELINE",
    "Prerequisite-Driven Deep Knowledge Tracing.pdf": "PRIMARY_CORE",
    "Graph-based Knowledge Tracing - Modeling Student Proficiency Using Graph Neural Network.pdf": "PRIMARY_CORE",
    "Structure-Based Knowledge Tracing - An Influence Propagation View.pdf": "PRIMARY_CORE",
    "Improving Knowledge Tracing via Pre-training Question Embeddings.pdf": "PRIMARY_CORE",
    "GIKT - A Graph-Based Interaction Model for Knowledge Tracing.pdf": "PRIMARY_CORE",
    "JKT - A Joint Graph Convolutional Network Based Deep Knowledge Tracing.pdf": "PRIMARY_CORE",
    "GASKT - A Graph-Based Attentive Knowledge-Search Model for Knowledge Tracing.pdf": "PRIMARY_CORE",
    "Bi-CLKT - Bi-Graph Contrastive Learning Based Knowledge Tracing.pdf": "PRIMARY_CORE",
    "SGKT - Session Graph-Based Knowledge Tracing for Student Performance Prediction.pdf": "PRIMARY_CORE",
    "Knowledge Structure Enhanced Graph Representation Learning Model for Attentive Knowledge Tracing.pdf": "PRIMARY_CORE",
    "CMKT - Concept Map Driven Knowledge Tracing.pdf": "PRIMARY_CORE",
    "Contrastive Learning for Knowledge Tracing.pdf": "PRIMARY_CORE",
    "Modeling Knowledge Proficiency Using Multi-Hierarchical Capsule Graph Neural Network.pdf": "PRIMARY_CORE",
    "Deep Graph Memory Networks for Forgetting-Robust Knowledge Tracing.pdf": "PRIMARY_CORE",
    "HHSKT - A Learner-Question Interactions Based Heterogeneous Graph Neural Network Model for Knowledge Tracing.pdf": "PRIMARY_CORE",
    "Self-Supervised Heterogeneous Hypergraph Network for Knowledge Tracing.pdf": "PRIMARY_CORE",
    "Fusing Hybrid Attentive Network with Self-Supervised Dual-Channel Heterogeneous Graph for Knowledge Tracing.pdf": "PRIMARY_CORE_FILENAME_CASE",
    "GraphCA - Learning From Graph Counterfactual Augmentation for Knowledge Tracing.pdf": "PRIMARY_CORE",
    "DGEKT - A Dual Graph Ensemble Learning Method for Knowledge Tracing.pdf": "PRIMARY_CORE",
    "Heterogeneous Graph-Based Knowledge Tracing with Spatiotemporal Evolution.pdf": "PRIMARY_CORE",
    "DyGKT - Dynamic Graph Learning for Knowledge Tracing.pdf": "PRIMARY_CORE",
    "Weighted Heterogeneous Graph-Based Three-View Contrastive Learning for Knowledge Tracing in Personalized e-Learning Systems.pdf": "PRIMARY_CORE",
    "SINKT - A Structure-Aware Inductive Knowledge Tracing Model with Large Language Model.pdf": "PRIMARY_CORE",
    "Exploring Long- and Short-Term Knowledge State Graph Representations with Adaptive Fusion for Knowledge Tracing.pdf": "PRIMARY_CORE",
    "STHKT - Spatiotemporal Knowledge Tracing with Topological Hawkes Process.pdf": "PRIMARY_CORE",
    "LGS-KT - Integrating Logical and Grammatical Skills for Effective Programming Knowledge Tracing.pdf": "PRIMARY_CORE",
    "MAHKT - Knowledge Tracing with Multi-Association Heterogeneous Graph Embedding Based on Knowledge Transfer.pdf": "PRIMARY_CORE",
    "Multi-Granularity Ensemble Interaction Graph Modeling for Knowledge Tracing.pdf": "PRIMARY_CORE",
    "Graph Knowledge Tracing in Cognitive Situation - Validation of Classic Assertions in Cognitive Psychology.pdf": "PRIMARY_CORE",
    "Dual-Channel Adaptive Scale Hypergraph Encoders With Cross-View Contrastive Learning for Knowledge Tracing.pdf": "PRIMARY_CORE",
    "Graph-Based Effective Knowledge Tracing via Subject Knowledge Mapping.pdf": "PRIMARY_CORE",
    "HKT - Hierarchical Structure-Based Knowledge Tracing.pdf": "PRIMARY_CORE",
    "A Cross-Domain Knowledge Tracing Model Based on Graph Optimal Transport.pdf": "PRIMARY_CORE",
    "Denoising Programming Knowledge Tracing with a Code Graph-based Tuning Adaptor.pdf": "PRIMARY_CORE",
    "KGNN-KT - Enhancing Knowledge Tracing in Programming Education Through LLM-Extracted Knowledge Graphs.pdf": "PRIMARY_CORE_IMAGE_ONLY",
    "R2GCurL - Reinforced Robust Knowledge Tracing via Dynamic Graph Curriculum Learning.pdf": "PRIMARY_CORE",
    "Spatio-Temporal Fusion in Graph Neural Network for Streaming Knowledge Tracing.pdf": "PRIMARY_CORE",
    "Knowledge Tracing - A Survey.pdf": "PRIOR_SURVEY",
    "pyKT - A Python Library to Benchmark Deep Learning based Knowledge Tracing Models.pdf": "PRIOR_BENCHMARK",
    "A Survey of Knowledge Tracing - Models, Variants, and Applications.pdf": "PRIOR_SURVEY",
    "A Survey of Graph-Based Knowledge Tracing from Structural and Propagation Perspectives - Models, Applications, and Future Directions.pdf": "PRIOR_SURVEY",
    "Deep Learning Based Knowledge Tracing A Review, a Tool and Empirical Studies.pdf": "PRIOR_SURVEY",
    "Convolutional Neural Network for Trajectory Prediction.pdf": "NOT_A_KT_PAPER",
    "Model Generalization - A Sharpness Aware Optimization Perspective.pdf": "NOT_A_KT_PAPER",
}

rows = []
for item in inv["files"]:
    name = item["file"]
    if name not in ROLE:
        raise SystemExit("unmapped " + name)
    note = ""
    dois = item["dois_page1_2"]
    if any("nnnnnnn" in d for d in dois):
        note = "Page 1-2 prints a placeholder DOI; not copied into the bibliography."
    if any(d.endswith("123678") for d in dois):
        note = "Page 1-2 prints 10.1109/JAS.2023.123678. Not used to change the bibliography."
    if item["chars_page1"] == 0:
        note = "No extractable text layer. Identity is the filename only."
    if name.startswith("Fusing Hybrid"):
        note = "Filename case differs from the README line; same DC-SSL paper."
    rows.append(
        {
            "file": name,
            "pages": item["pages"],
            "text_layer": "NO" if item["chars_page1"] == 0 else "YES",
            "doi_printed_on_page_1_or_2": "; ".join(dois),
            "title_line_from_page_1": " ".join(item["title_lines"][:2]),
            "library_role": ROLE[name],
            "is_one_of_the_seven_A1_candidate_pdfs": "NO",
            "note": note,
        }
    )

out = Path(r"D:\TRINH\GraphSSL_KT_Survey\tables\A1_LOCAL_PDF_INVENTORY_2026-11-13.csv")
with out.open("w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    w.writeheader()
    w.writerows(rows)
print(len(rows), out.name)
