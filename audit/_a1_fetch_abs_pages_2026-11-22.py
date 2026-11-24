# -*- coding: utf-8 -*-
import re
import urllib.request
from pathlib import Path

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
OUT = Path(r"D:\TRINH\GraphSSL_KT_Survey\audit\_a1_2026-11-22")
URLS = {
    "hcmkt.html": "https://www.sciencedirect.com/science/article/abs/pii/S0957417425024571",
    "han.html": "https://www.sciencedirect.com/science/article/abs/pii/S1568494624009682",
    "coskt.html": "https://ieeexplore.ieee.org/document/10495188/",
}


def main():
    for name, url in URLS.items():
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "text/html"})
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                raw = resp.read()
                final = resp.geturl()
                code = resp.status
        except Exception as exc:
            print(name, "ERR", exc)
            continue
        path = OUT / name
        path.write_bytes(raw)
        text = raw.decode("utf-8", "replace")
        print(name, code, final, "bytes", len(raw))
        for token in ("Abstract", "abstract", "graph", "contrastive", "self-supervised"):
            print(" ", token, text.lower().count(token.lower()))


if __name__ == "__main__":
    main()
