from pathlib import Path
text = Path(r"D:\TRINH\GraphSSL_KT_Survey\03_search\exports\arxiv_qs_20261114.xml").read_text(encoding="utf-8")
low = text.lower()
i = low.find("coskt")
print("idx", i)
print(text[max(0, i - 240): i + 240])
