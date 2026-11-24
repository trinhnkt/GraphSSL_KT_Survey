import re
import time
import urllib.parse
import urllib.request
from pathlib import Path

base = Path(r"D:\TRINH\GraphSSL_KT_Survey\audit\_srch013_url.txt").read_text(encoding="utf-8").strip()
ids = []
for start in range(0, 300, 50):
    url = base + "&start=" + str(start)
    req = urllib.request.Request(url, headers={"User-Agent": "GraphSSL-KT-survey/1.0"})
    html = urllib.request.urlopen(req, timeout=60).read().decode("utf-8", "replace")
    found = re.findall(r"https://arxiv.org/abs/(\d{4}\.\d{4,5})", html)
    # keep order, drop dupes on the page
    page_ids = []
    for i in found:
        if i not in page_ids:
            page_ids.append(i)
    print("start", start, "ids", len(page_ids), "h1", re.search(r"Showing.{0,40}results", html).group(0) if re.search(r"Showing.{0,40}results", html) else "none")
    ids.extend(page_ids)
    time.sleep(1)

uniq = []
for i in ids:
    if i not in uniq:
        uniq.append(i)
print("unique", len(uniq))
Path(r"D:\TRINH\GraphSSL_KT_Survey\audit\_srch013_ids.txt").write_text("\n".join(uniq), encoding="utf-8")
