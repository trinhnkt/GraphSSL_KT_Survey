# -*- coding: utf-8 -*-
import json
import urllib.request

UA = "GraphSSL-KT-Survey-A1/2026-11-22 (mailto:survey-audit@localhost)"


def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/vnd.github+json"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read().decode("utf-8"))


def main():
    repo = get("https://api.github.com/repos/lucky7-code/CoSKT")
    print("repo", repo.get("full_name"), repo.get("description"), repo.get("html_url"))
    contents = get("https://api.github.com/repos/lucky7-code/CoSKT/contents/")
    for item in contents:
        print(item.get("type"), item.get("name"), item.get("size"), item.get("download_url"))


if __name__ == "__main__":
    main()
