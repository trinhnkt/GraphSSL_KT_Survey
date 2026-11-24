import re
import time
import urllib.request
from pathlib import Path

base = Path(r"D:\TRINH\GraphSSL_KT_Survey\audit\_srch014_url.txt").read_text(encoding="utf-8").strip()
ids = []
for start in range(0, 250, 50):
    url = base + "&start=" + str(start)
    req = urllib.request.Request(url, headers={"User-Agent": "GraphSSL-KT-survey/1.0"})
    html = urllib.request.urlopen(req, timeout=60).read().decode("utf-8", "replace")
    h1 = re.search(r"Showing.{0,40}results", html)
    found = []
    for i in re.findall(r"https://arxiv.org/abs/(\d{4}\.\d{4,5})", html):
        if i not in found:
            found.append(i)
    print("start", start, "ids", len(found), "h1", h1.group(0) if h1 else "none")
    if not found:
        break
    ids.extend(found)
    time.sleep(1)

uniq = []
for i in ids:
    if i not in uniq:
        uniq.append(i)
print("unique", len(uniq))
Path(r"D:\TRINH\GraphSSL_KT_Survey\audit\_srch014_ids.txt").write_text("\n".join(uniq), encoding="utf-8")
