from pathlib import Path

old = "QA1, QA2, and QA4 are $2$ on every paper"
new = "Table~\\ref{tab:qa_distribution} counts each score. QA1, QA2, and QA4 are $2$ on every paper"
root = Path(r"D:\TRINH\GraphSSL_KT_Survey\12_manuscript\TLT")
for name in ["main_tlt_anonymous.tex", "main_tlt_full.tex", "manuscript_TLT_FORMATTED_v1.3.tex"]:
    path = root / name
    text = path.read_bytes().decode("utf-8")
    found = text.count(old)
    if found != 1:
        raise SystemExit(f"{name} {found}")
    text = text.replace(old, new)
    if "\r\n" not in text:
        raise SystemExit("crlf lost")
    path.write_bytes(text.encode("utf-8"))
    print("ok", name)
