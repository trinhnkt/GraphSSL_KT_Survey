"""Align references.bib with IEEE Reference Guide (required by IEEE TLT)."""
from __future__ import annotations

import re
from pathlib import Path

BIB = Path(__file__).resolve().parents[1] / "references.bib"


def main() -> None:
    text = BIB.read_text(encoding="utf-8")

    title_repls = [
        (r"title\s*=\s*\{GIKT:", "title     = {{GIKT}:"),
        (r"title\s*=\s*\{Bi-CLKT:", "title     = {{Bi-CLKT}:"),
        (r"title\s*=\s*\{JKT:", "title     = {{JKT}:"),
        (r"title\s*=\s*\{SGKT:", "title     = {{SGKT}:"),
        (r"title\s*=\s*\{DGEKT:", "title     = {{DGEKT}:"),
        (r"title\s*=\s*\{HHSKT:", "title     = {{HHSKT}:"),
        (r"title\s*=\s*\{CMKT:", "title     = {{CMKT}:"),
        (r"title\s*=\s*\{DyGKT:", "title     = {{DyGKT}:"),
        (r"title\s*=\s*\{GraphCA:", "title     = {{GraphCA}:"),
        (r"title\s*=\s*\{GASKT:", "title     = {{GASKT}:"),
        (r"title\s*=\s*\{STHKT:", "title     = {{STHKT}:"),
        (r"title\s*=\s*\{LGS-KT:", "title     = {{LGS-KT}:"),
        (r"title\s*=\s*\{MAHKT:", "title     = {{MAHKT}:"),
        (r"title\s*=\s*\{HKT:", "title     = {{HKT}:"),
        (r"title\s*=\s*\{KGNN-KT:", "title     = {{KGNN-KT}:"),
        (
            r"title\s*=\s*\{R\{\\texttwosuperior\}GCurL:",
            r"title     = {{R{\texttwosuperior}GCurL}:",
        ),
    ]
    for pat, repl in title_repls:
        text, n = re.subn(pat, repl, text, count=1)
        print(f"title {pat[:28]}... -> {n}")

    booktitle_map = {
        "Proceedings of the IEEE/WIC/ACM International Conference on Web Intelligence (WI)":
            "Proc. IEEE/WIC/ACM Int. Conf. Web Intell. (WI)",
        "Proceedings of the European Conference on Machine Learning and Principles and Practice of Knowledge Discovery in Databases (ECML-PKDD)":
            "Proc. Eur. Conf. Mach. Learn. Knowl. Discovery Databases (ECML-PKDD)",
        "Proceedings of the IEEE International Conference on Data Mining (ICDM)":
            "Proc. IEEE Int. Conf. Data Mining (ICDM)",
        "Proceedings of the International Joint Conference on Artificial Intelligence (IJCAI)":
            "Proc. Int. Joint Conf. Artif. Intell. (IJCAI)",
        "Proceedings of the ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD)":
            "Proc. ACM SIGKDD Conf. Knowl. Discovery Data Mining (KDD)",
        "Proceedings of the ACM Web Conference (WWW)":
            "Proc. ACM Web Conf. (WWW)",
        "Proceedings of the ACM International Conference on Information and Knowledge Management (CIKM)":
            "Proc. ACM Int. Conf. Inf. Knowl. Manage. (CIKM)",
        "Proceedings of the International Conference on Knowledge Science, Engineering and Management (KSEM)":
            "Proc. Int. Conf. Knowl. Sci. Eng. Manage. (KSEM)",
        "Proceedings of the 31st ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD)":
            "Proc. 31st ACM SIGKDD Conf. Knowl. Discovery Data Mining (KDD)",
        "Proceedings of the 21st International Conference on Intelligent Computing (ICIC)":
            "Proc. 21st Int. Conf. Intell. Comput. (ICIC)",
        "Proceedings of the International Conference on Database Systems for Advanced Applications (DASFAA)":
            "Proc. Int. Conf. Database Syst. Adv. Appl. (DASFAA)",
        "Advances in Neural Information Processing Systems (NeurIPS)":
            "Adv. Neural Inf. Process. Syst. (NeurIPS)",
        "Proceedings of the 12th International Conference on Educational Data Mining (EDM)":
            "Proc. 12th Int. Conf. Educ. Data Mining (EDM)",
        "Proceedings of the 26th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (KDD)":
            "Proc. 26th ACM SIGKDD Int. Conf. Knowl. Discovery Data Mining (KDD)",
        "Proceedings of the 26th International Conference on World Wide Web (WWW)":
            "Proc. 26th Int. Conf. World Wide Web (WWW)",
        "Advances in Neural Information Processing Systems (NeurIPS) Datasets and Benchmarks Track":
            "Adv. Neural Inf. Process. Syst. (NeurIPS) Datasets Benchmarks Track",
    }
    for old, new in booktitle_map.items():
        if old not in text:
            print("MISSING booktitle:", old[:70])
        else:
            text = text.replace(old, new)
            print("OK booktitle:", new)

    text = text.replace("Inf. Process. Manage.", "Inf. Process. Manag.")

    text = text.replace(
        "  volume    = {42},\n  number    = {3},\n  pages     = {78:1--78:24},\n  year      = {2024},\n  doi       = {10.1145/3638350},",
        "  volume    = {42},\n  number    = {3},\n  articlenumber = {78},\n  year      = {2024},\n  doi       = {10.1145/3638350},",
    )
    text = text.replace(
        "  volume    = {28},\n  number    = {1},\n  pages     = {10},\n  year      = {2025},\n  doi       = {10.1007/s11280-024-01311-1},",
        "  volume    = {28},\n  number    = {1},\n  articlenumber = {10},\n  year      = {2025},\n  doi       = {10.1007/s11280-024-01311-1},",
    )

    # Elsevier-style article IDs -> Art. no.
    for art in [
        "108274",
        "117681",
        "119334",
        "122249",
        "120212",
        "104074",
        "125248",
        "107164",
        "112958",
        "112834",
        "113281",
        "104206",
    ]:
        old = f"pages     = {{{art}}}"
        new = f"articlenumber = {{{art}}}"
        if old in text:
            text = text.replace(old, new, 1)
            print("artno", art)
        else:
            print("FAIL artno", art)

    old_hdr = (
        "% Graph-Based and Self-Supervised Knowledge Tracing Bibliography\n"
        "% TLT / IEEE Reference Guide alignment (IEEEtran.bst 1.14)\n"
        "% - Journal titles abbreviated per IEEE style\n"
        "% - doi field kept for audit; url=https://doi.org/... so IEEEtran prints the locator\n"
        "% - IEEEtranBSTCTL: list up to 6 authors, then first author et al.\n"
        "% - file= points at 14_references/ (IEEEtran ignores this field)"
    )
    new_hdr = (
        "% Graph-Based and Self-Supervised Knowledge Tracing Bibliography\n"
        "% IEEE TLT requires IEEE Reference Guide compliance (IEEEtran.bst 1.14)\n"
        "% - Journal titles abbreviated per IEEE style\n"
        "% - Conference names abbreviated (Proc./Int./Conf./...)\n"
        "% - Model acronyms braced in titles so IEEEtran sentence-case keeps casing\n"
        "% - Article-ID periodicals use articlenumber (Art. no.) when applicable\n"
        "% - doi kept for audit; url=https://doi.org/... prints IEEE [Online] locator\n"
        "% - IEEEtranBSTCTL: list up to 6 authors, then first author et al.\n"
        "% - file= points at 14_references/ (IEEEtran ignores this field)"
    )
    if old_hdr in text:
        text = text.replace(old_hdr, new_hdr)
    else:
        print("WARN: header block not matched")

    BIB.write_text(text, encoding="utf-8")
    print("WROTE", BIB)
    for probe in [
        "title     = {GIKT:",
        "title     = {{GIKT}:",
        "Proceedings of the",
        "Proc. IEEE Int. Conf. Data Mining",
        "pages     = {108274}",
        "articlenumber = {108274}",
        "articlenumber = {78}",
    ]:
        print(f"  contains {probe!r}: {probe in text}")


if __name__ == "__main__":
    main()
