# -*- coding: utf-8 -*-
"""Look for the 16 search exports dated 2026-08-26 anywhere under the repo."""
import os
import zipfile

ROOT = r"D:\TRINH\GraphSSL_KT_Survey"
NAMES = [
    "acm_qg_20260826.csv",
    "acm_qs_20260826.csv",
    "ieee_qg_20260826.csv",
    "ieee_qs_20260826.csv",
    "sciencedirect_qg_20260826.csv",
    "sciencedirect_qs_20260826.csv",
    "springer_qg_20260826.csv",
    "springer_qs_20260826.csv",
    "scopus_qg_20260826.csv",
    "scopus_qs_20260826.csv",
    "wos_qg_20260826.csv",
    "wos_qs_20260826.csv",
    "arxiv_qg_20260826.csv",
    "arxiv_qs_20260826.csv",
    "scopus_qp_20260826.csv",
    "scopus_qr_20260826.csv",
]
wanted = {name.lower(): name for name in NAMES}
found = {name: [] for name in NAMES}
date_hits = []
archives = []
n_files = 0
n_dirs = 0

for dirpath, dirnames, filenames in os.walk(ROOT):
    n_dirs += 1
    for filename in filenames:
        n_files += 1
        low = filename.lower()
        path = os.path.join(dirpath, filename)
        if low in wanted:
            found[wanted[low]].append(path)
        if "20260826" in low or "2026-08-26" in low or "2026_08_26" in low:
            date_hits.append(path)
        if low.endswith((".zip", ".7z", ".rar", ".tar", ".gz")):
            archives.append(path)

print("dirs", n_dirs)
print("files", n_files)
print("--- exact names ---")
for name in NAMES:
    print(name, found[name] or "ABSENT")
print("--- date in filename ---")
for path in date_hits:
    print(path)
print("--- archives ---")
for path in archives:
    print(path)
    if path.lower().endswith(".zip"):
        try:
            with zipfile.ZipFile(path) as zf:
                for info in zf.infolist():
                    low = info.filename.lower()
                    if "20260826" in low or "2026-08-26" in low or os.path.basename(low) in wanted:
                        print("  INSIDE", info.filename)
        except Exception as exc:
            print("  unreadable", exc)
