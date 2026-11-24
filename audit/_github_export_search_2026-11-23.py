# -*- coding: utf-8 -*-
"""List paths containing 20260826 or an exports folder in the user's GitHub repos."""
import json
import subprocess

repos = [
    "GraphSSL_KT_Survey",
    "When-Overall-AUC-Hides-Miscalibration",
    "Luu-Sparse-Concept-and-Calibration",
    "Workshop1",
    "MCP_EDU",
    "pub2",
]
out = []
for repo in repos:
    raw = subprocess.check_output(
        ["gh", "api", f"repos/trinhnkt/{repo}/git/trees/HEAD?recursive=1"],
        text=True,
        encoding="utf-8",
    )
    data = json.loads(raw)
    paths = [item.get("path", "") for item in data.get("tree", [])]
    hits = [
        p for p in paths
        if "20260826" in p or "/exports/" in p or p.startswith("exports/")
    ]
    out.append({"repo": repo, "files": len(paths), "truncated": data.get("truncated"), "hits": hits})
path = r"D:\TRINH\GraphSSL_KT_Survey\audit\_github_export_search_2026-11-23.json"
with open(path, "w", encoding="utf-8", newline="\n") as fh:
    json.dump(out, fh, ensure_ascii=False, indent=2)
print(json.dumps(out, ensure_ascii=False, indent=2))
