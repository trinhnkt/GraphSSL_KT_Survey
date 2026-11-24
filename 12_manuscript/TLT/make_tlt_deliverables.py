"""Copy full manuscript and build anonymous TLT tex."""
from pathlib import Path
import re

src = Path(r"D:\TRINH\GraphSSL_KT_Survey\12_manuscript\TLT\manuscript_TLT_FORMATTED_v1.3.tex")
text = src.read_text(encoding="utf-8")

full = Path(r"D:\TRINH\GraphSSL_KT_Survey\12_manuscript\TLT\main_tlt_full.tex")
full.write_text(text, encoding="utf-8")

old_author = r"""\author{Khanh-Trinh~Nguyen,
        Tuan~Dao~Minh,
        Duong~Nguyen~Tien,
        Chi~Thanh~Nguyen,
        and~Van-Hau~Nguyen$^{*}$%
\thanks{K.-T. Nguyen (ORCID: 0009-0004-3739-0484),
T.~Dao Minh (ORCID: 0009-0009-1641-6813),
D.~Nguyen Tien (ORCID: 0009-0007-1104-7129),
and V.-H. Nguyen (ORCID: 0000-0002-3256-5626)
are with the Faculty of Information Technology,
Hung Yen University of Technology and Engineering, Hung Yen 160000, Vietnam
(e-mail: trinhnk@utehy.edu.vn; tuanymc@utehy.edu.vn;
duongnt@utehy.edu.vn; haunv@utehy.edu.vn).}%
\thanks{C.~T. Nguyen (ORCID: 0000-0003-4335-7002)
is with the Academy of Military Science and Technology, Ha Noi 100000, Vietnam
(e-mail: thanhnc@ioit.ai.vn).}%
\thanks{$^{*}$Corresponding author: Van-Hau Nguyen.}%
}"""

new_author = r"""\author{Anonymous Authors
\thanks{Manuscript submitted to IEEE Transactions on Learning Technologies.
Author names, affiliations, emails, and ORCIDs are omitted for this anonymous copy.}
}"""

if old_author not in text:
    raise SystemExit("author block not found")

anon = text.replace(old_author, new_author)
anon = anon.replace(
    r"{Nguyen \MakeLowercase{\textit{et al.}}: Graph/SSL Knowledge Tracing in Sparse-Concept Settings}",
    r"{Anonymous: Graph/SSL Knowledge Tracing in Sparse-Concept Settings}",
)
anon = re.sub(
    r"\\begin\{IEEEbiographynophoto\}.*?\\end\{IEEEbiographynophoto\}\s*",
    "",
    anon,
    flags=re.S,
)

out = Path(r"D:\TRINH\GraphSSL_KT_Survey\12_manuscript\TLT\main_tlt_anonymous.tex")
out.write_text(anon, encoding="utf-8")
print("anon has Khanh-Trinh:", "Khanh-Trinh" in anon)
print("anon has ORCID:", "ORCID" in anon)
print("anon has UTEHY email:", "utehy.edu.vn" in anon)
print("anon has IEEEbiography:", "IEEEbiography" in anon)
print("wrote", full.name, out.name)
