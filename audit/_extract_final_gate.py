import json
from pathlib import Path

p = Path(r"C:\Users\EDM\.cursor\projects\d-TRINH-GraphSSL-KT-Survey\agent-transcripts\a8430371-650c-4212-b7b0-cac29720baca\a8430371-650c-4212-b7b0-cac29720baca.jsonl")
out = Path(r"D:\TRINH\GraphSSL_KT_Survey\audit\_final_gate_spec.txt")
found = False
with p.open(encoding="utf-8") as f:
    for line in f:
        if "FINAL GLOBAL GATE" not in line or "user_query" not in line:
            continue
        obj = json.loads(line)
        text = obj["message"]["content"][0]["text"]
        i = text.find("# FINAL GLOBAL GATE")
        if i < 0:
            continue
        chunk = text[i:i + 6000]
        out.write_text(chunk, encoding="utf-8")
        print(chunk)
        found = True
        break
if not found:
    raise SystemExit("not found")
