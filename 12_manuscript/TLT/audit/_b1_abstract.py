from pathlib import Path

old = (
    " As a survey-computed overlay---not a change to the $0/37$ manuscript-reporting claim---"
    "we also report equal-width ECE on author DyGKT/ASSIST17 (one model, one dataset, one seed)."
)
files = [
    Path(r"D:\TRINH\GraphSSL_KT_Survey\12_manuscript\TLT\main_tlt_anonymous.tex"),
    Path(r"D:\TRINH\GraphSSL_KT_Survey\12_manuscript\TLT\main_tlt_full.tex"),
    Path(r"D:\TRINH\GraphSSL_KT_Survey\12_manuscript\TLT\manuscript_TLT_FORMATTED_v1.3.tex"),
]
for path in files:
    raw = path.read_bytes()
    nl = "\r\n" if b"\r\n" in raw else "\n"
    text = raw.decode("utf-8").replace("\r\n", "\n")
    n = text.count(old)
    if n != 1:
        idx = text.find("DyGKT/ASSIST17")
        print(path.name, "count", n, "idx", idx)
        if idx >= 0:
            print(repr(text[idx - 120:idx + 80]))
        raise SystemExit(1)
    text = text.replace(old, "")
    path.write_bytes(text.replace("\n", nl).encode("utf-8"))
    print(path.name, "ok", text.count("0.0361"), text.count("DyGKT/ASSIST17"), text.count("KT038"), text.count("0/37"))
