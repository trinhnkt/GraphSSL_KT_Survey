import re
from pathlib import Path
import fitz
path = Path(r"D:\TRINH\GraphSSL_KT_Survey\14_references\GraphCA - Learning From Graph Counterfactual Augmentation for Knowledge Tracing.pdf")
doc = fitz.open(path)
text = re.sub(r"\s+", " ", doc[5].get_text())
idx = text.lower().find("counterfactual replacement")
out = Path(r"D:\TRINH\GraphSSL_KT_Survey\audit\_a4_graphca_p6.txt")
out.write_text(text[idx:idx+2200] + "\n\n---- p7 ----\n" + re.sub(r"\s+", " ", doc[6].get_text())[:1200], encoding="utf-8")
print("wrote", idx)
