"""B6: replace internal jargon in the three live manuscripts and figure sources.

Does not edit _backup_before_v1.9. Does not change numeric claims.
"""
from pathlib import Path

ROOT = Path(r"D:\TRINH\GraphSSL_KT_Survey\12_manuscript\TLT")
FILES = [
    ROOT / "main_tlt_anonymous.tex",
    ROOT / "main_tlt_full.tex",
    ROOT / "manuscript_TLT_FORMATTED_v1.3.tex",
    ROOT / "figures" / "fig_ssl_framework.tex",
    ROOT / "figures" / "fig_taxonomy_2d.tex",
    ROOT / "figures" / "fig_graph_construction_pipeline.tex",
    ROOT / "figures" / "fig_meta_analysis_charts.tex",
    ROOT / "figures" / "fig_prisma_flow.tex",
]

PHRASES = [
    ("The locked protocol (Sec.~22.1)", "The survey protocol (Supplementary Table~S-Tokens)"),
    ("the locked protocol (Sec.~22.1)", "the survey protocol (Supplementary Table~S-Tokens)"),
    ("locked codebook Sec.~14 tokens", "pretext-family names (Supplementary Table~S-Tokens)"),
    ("locked codebook Sec.~14", "the coding protocol (Supplementary Table~S-Tokens)"),
    ("Locked codebook Sec.\\ 14 tokens only", "Four pretext families"),
    ("Mechanism notes are not families", "Family names are the four headings at left"),
    ("databases locked in the protocol", "databases named in the survey protocol"),
    ("Deviations from the Locked Protocol", "Deviations from the Survey Protocol"),
    ("under the locked survey protocol", "under the survey protocol"),
    ("under the locked protocol", "under the survey protocol"),
    ("Locked graph-taxonomy counts", "Graph-taxonomy counts"),
    ("locked codebook values", "code values in Supplementary Table~S-Tokens"),
    ("locked codebook families", "four pretext families"),
    ("locked codebook", "coding protocol"),
    ("locked ontology tokens", "code values in Supplementary Table~S-Tokens"),
    ("locked search-log sum", "search-log sum"),
    ("locked search log", "search log"),
    ("the locked search", "the recorded search"),
    ("After the locked search", "After the recorded search"),
    ("locked gold", "adjudicated reference"),
    ("locked S-criterion", "S-criterion"),
    ("locked coding tables", "coding tables"),
    ("locked manuscript-reporting count", "manuscript-reporting count"),
    ("no locked leakage", "no leakage"),
    ("locked leakage", "leakage"),
    ("no locked classroom", "no classroom"),
    ("from the locked coding", "from the coded records"),
    ("from locked coding", "from the coded records"),
    ("of the locked coding", "of the coded records"),
    ("locked \\texttt{graph\\_source}", "recorded graph source"),
    ("the locked \\texttt{graph\\_source} token", "the recorded graph-source value"),
    ("37 locked primary-core", "37 primary-core"),
    ("A locked 37-PDF", "A 37-PDF"),
    ("\\textbf{Locked 37-PDF corpus and coding protocol}", "\\textbf{37-PDF corpus and coding protocol}"),
    ("Locked 37 PDFs", "37 PDFs"),
    ("4 locked \\texttt{ssl\\_family} tokens", "4 pretext families"),
    ("4 locked families", "4 pretext families"),
    ("exclusive locked token", "exclusive family code (Supplementary Table~S-Tokens)"),
    ("four locked tokens", "four family codes (Supplementary Table~S-Tokens)"),
    ("Identification (locked search log)", "Identification (search log)"),
    ("locked survey protocol", "survey protocol"),
    ("locked protocol", "survey protocol"),
    ("locked fields", "coded fields"),
    ("locked primary-core", "primary-core"),
    ("SSL-KT~codebook~families", "SSL-KT pretext families"),
]

TOKENS = [
    ("graph\\_source=NONE", "graph source = none"),
    ("gnn\\_encoder=NONE", "GNN encoder = none"),
    ("MODEL\\_DEFINED\\_FIXED", "model-defined fixed graph"),
    ("JOINTLY\\_LEARNED\\_TRAINING", "jointly learned during training"),
    ("PRECOMPUTED\\_UNCLEAR\\_SPLIT", "precomputed graph, split unclear"),
    ("TRAIN\\_ONLY\\_INFERRED", "train-only graph, inferred"),
    ("FULL\\_DATA\\_INFERRED", "full-data graph, inferred"),
    ("PRETRAINED\\_TWO\\_STAGE", "pretrained graph, two-stage"),
    ("EXTERNAL\\_FIXED", "external fixed graph"),
    ("DYNAMIC\\_LEARNED", "dynamically learned graph"),
    ("MIXED\\_PROVENANCE", "mixed provenance"),
    ("SPARSE\\_INTERACTION\\_ONLY", "interaction sparsity only"),
    ("STRICT\\_KC\\_COLD\\_START", "strict KC cold-start"),
    ("ITEM\\_COLD\\_START", "item cold-start"),
    ("EXCLUDE\\_FULLTEXT", "exclude at full text"),
    ("GRAPH\\_RECONSTRUCTION", "graph reconstruction"),
    ("MULTIVIEW\\_CONTRASTIVE", "multi-view contrast"),
    ("GRAPH\\_OPTIMAL\\_TRANS", "optimal transport on graphs"),
    ("COOCCURRENCE\\_SIMILARITY", "co-occurrence similarity"),
    ("SEQUENTIAL\\_TRANSITION", "sequential transition"),
    ("DYNAMIC\\_COOCCURRENCE", "dynamic co-occurrence"),
    ("HETEROGENEOUS\\_GNN", "heterogeneous GNN"),
    ("SPATIOTEMPORAL\\_GNN", "spatiotemporal GNN"),
    ("HYPERGRAPH\\_GNN", "hypergraph GNN"),
    ("CAPSULE\\_GNN", "capsule GNN"),
    ("DYNAMIC\\_GNN", "dynamic GNN"),
    ("GRAPH\\_MEMORY", "graph memory"),
    ("GNN\\_GENERIC", "generic GNN"),
    ("PRIMARY\\_CORE", "primary-core"),
    ("graph\\_leakage\\_risk", "graph-leakage risk"),
    ("sparse\\_protocol\\_category", "sparse-protocol category"),
    ("sparse\\_interaction\\_drop\\_eval", "interaction-drop evaluation"),
    ("strict\\_kc\\_cold\\_start", "strict KC cold-start"),
    ("learner\\_cold\\_start", "learner cold-start"),
    ("item\\_cold\\_start", "item cold-start"),
    ("graph\\_provenance", "graph provenance"),
    ("graph\\_source", "graph source"),
    ("gnn\\_encoder", "GNN encoder"),
    ("ssl\\_family", "pretext family"),
    ("ece\\_reported", "ECE reported"),
    ("REPRODUCED", "survey-computed"),
    ("UNCERTAIN", "uncertain"),
    ("UNCLEAR", "unclear"),
    ("NONE", "none"),
    ("OTHER", "other"),
    ("NA", "not applicable"),
    ("NO", "no"),
]

PATHS = [
    (r"\path{00_protocol/protocol_deviations.md}", "the protocol-deviation record"),
    (r"\path{03_search/search_log_venue_extension_v1.9.csv}", "Supplementary Table~S-Files"),
    (r"\path{03_search/venue_extension_candidates_v1.9.csv}", "Supplementary Table~S-Files"),
    (r"\path{supplementary/calibration_keyword_scan_v1.9.csv}", "Supplementary Table~S-Files"),
    (r"\path{supplementary/graph_provenance_subbins_8way_v1.9.csv}", "Supplementary Table~S-Files"),
    (r"\path{supplementary/graph_provenance_x_encoder_crosstab_v1.9.csv}", "Supplementary Table~S-Files"),
    (r"\path{supplementary/supplementary_quality_scores_v2_QA7_sensitivity.csv}", "Supplementary Table~S-Files"),
    (r"\path{tables/sparse_coldstart_audit_v1.9.csv}", "Supplementary Table~S-Files"),
    (r"\texttt{tables/H2\_qa7\_two\_variables.csv}", "Supplementary Table~S-Files"),
    (r"\texttt{tables/sparse\_coldstart\_audit\_v1.9.csv}", "Supplementary Table~S-Files"),
    (r"\texttt{sparse\_coldstart\_audit.csv}", "Supplementary Table~S-Files"),
]


def apply_one(text: str) -> tuple[str, int]:
    n = 0
    for old, new in PATHS + PHRASES:
        c = text.count(old)
        if c:
            text = text.replace(old, new)
            n += c
    for token, readable in TOKENS:
        old = r"\texttt{" + token + "}"
        c = text.count(old)
        if c:
            text = text.replace(old, readable)
            n += c
        # figure files sometimes use the token without wrapping every time
        if token.startswith("GRAPH") or "ssl" in token or token.startswith("graph"):
            c2 = text.count(token)
            if c2:
                text = text.replace(token, readable)
                n += c2
    return text, n


def main() -> None:
    for path in FILES:
        raw = path.read_bytes()
        crlf = b"\r\n" in raw
        text = raw.decode("utf-8")
        if crlf:
            text = text.replace("\r\n", "\n")
        new, n = apply_one(text)
        out = new.replace("\n", "\r\n") if crlf else new
        path.write_bytes(out.encode("utf-8"))
        print(f"{path.name}: {n} replacements")


if __name__ == "__main__":
    main()
