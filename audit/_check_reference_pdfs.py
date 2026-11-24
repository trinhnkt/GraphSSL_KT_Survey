import re
from pathlib import Path

bib_path = Path(r"D:\TRINH\GraphSSL_KT_Survey\12_manuscript\TLT\references.bib")
ref_dir = Path(r"D:\TRINH\GraphSSL_KT_Survey\14_references")
text = bib_path.read_text(encoding="utf-8")

entries = []
for match in re.finditer(r"@(\w+)\{([^,]+),", text):
    kind, key = match.group(1), match.group(2)
    if kind == "IEEEtranBSTCTL":
        continue
    start = match.end()
    # next entry or end
    nxt = re.search(r"\n@", text[start:])
    body = text[start:start + nxt.start()] if nxt else text[start:]
    title_m = re.search(r"title\s*=\s*\{(.+?)\}", body, re.S)
    file_m = re.search(r"file\s*=\s*\{([^}]+)\}", body)
    title = re.sub(r"\s+", " ", title_m.group(1)).strip() if title_m else ""
    file_rel = file_m.group(1).strip() if file_m else ""
    entries.append((key, kind, title, file_rel))

files = {p.name: p.stat().st_size for p in ref_dir.iterdir() if p.is_file() and p.suffix.lower() == ".pdf"}
pointed = set()
missing = []
no_file_field = []
empty = []
for key, kind, title, file_rel in entries:
    if not file_rel:
        no_file_field.append((key, kind, title))
        continue
    name = Path(file_rel).name
    pointed.add(name)
    path = ref_dir / name
    if not path.exists():
        missing.append((key, name))
    elif path.stat().st_size == 0:
        empty.append((key, name))

extra = sorted(set(files) - pointed)
print(f"BIB_ENTRIES {len(entries)}")
print(f"PDF_FILES {len(files)}")
print(f"POINTED {len(pointed)}")
print("--- MISSING ---")
for row in missing:
    print(f"{row[0]}\t{row[1]}")
print("--- NO_FILE_FIELD ---")
for key, kind, title in no_file_field:
    print(f"{key}\t{kind}\t{title[:120]}")
print("--- EMPTY ---")
for row in empty:
    print(f"{row[0]}\t{row[1]}")
print("--- EXTRA_PDF ---")
for name in extra:
    print(f"{name}\t{files[name]}")
