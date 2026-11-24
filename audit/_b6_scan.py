import re
from pathlib import Path

p = Path(r"D:\TRINH\GraphSSL_KT_Survey\12_manuscript\TLT\main_tlt_anonymous.tex")
t = p.read_text(encoding="utf-8")
print("texttt", len(re.findall(r"\\texttt\{", t)))
toks = sorted(set(re.findall(r"\\texttt\{([^}]+)\}", t)))
for x in toks:
    print(f"T {t.count(x):3d} {x}")
print("---PATH---")
for m in sorted(set(re.findall(r"\\path\{([^}]+)\}", t))):
    print(f"P {t.count(m):3d} {m}")
print("---LOCKED LINES---")
for i, line in enumerate(t.splitlines(), 1):
    if re.search(r"locked|Sec\.~?14|Sec\.~?22\.1|\.csv", line, re.I):
        print(f"{i}: {line.strip()[:220]}")
