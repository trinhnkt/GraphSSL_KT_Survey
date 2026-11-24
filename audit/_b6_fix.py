from pathlib import Path

root = Path(r"D:\TRINH\GraphSSL_KT_Survey\12_manuscript\TLT")
files = [
    root / "main_tlt_anonymous.tex",
    root / "main_tlt_full.tex",
    root / "manuscript_TLT_FORMATTED_v1.3.tex",
]
pairs = [
    ("survey-computed survey-computed", "survey-computed"),
    ("by locked pretext family", "by pretext family"),
    ("with locked sparse/cold-start fields", "with coded sparse/cold-start fields"),
    ("is a locked coding table", "is a coding table"),
    ("as the locked display values", "as the displayed values"),
    ("as a locked count", "as a corpus count"),
    ("is a locked coding of", "is a coding of"),
    ("four locked pretext families", "four pretext families"),
    ("37 PRIMARY\\_CORE papers", "37 primary-core papers"),
    ("GRAPH\\_BASED means", "graph-based means"),
    ("SELF\\_SUPERVISED means", "self-supervised means"),
    ("all-NO fields", "all-no fields"),
]
for path in files:
    raw = path.read_bytes()
    crlf = b"\r\n" in raw
    text = raw.decode("utf-8").replace("\r\n", "\n")
    n = 0
    for old, new in pairs:
        c = text.count(old)
        if c:
            text = text.replace(old, new)
            n += c
        else:
            print("MISSING", path.name, old)
    out = text.replace("\n", "\r\n") if crlf else text
    path.write_bytes(out.encode("utf-8"))
    print(path.name, n)
