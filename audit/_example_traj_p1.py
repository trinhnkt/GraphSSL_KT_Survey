# -*- coding: utf-8 -*-
from pathlib import Path
from pypdf import PdfReader

pdf = Path(r"D:\TRINH\GraphSSL_KT_Survey\14_references") / "Convolutional Neural Network for Trajectory Prediction.pdf"
reader = PdfReader(str(pdf))
text = reader.pages[0].extract_text() or ""
text = "".join(ch for ch in text if not (0xD800 <= ord(ch) <= 0xDFFF))
out = Path(r"D:\TRINH\GraphSSL_KT_Survey\audit\_example_traj_p1.txt")
out.write_text(text, encoding="utf-8", newline="\n")
print("pages", len(reader.pages), "chars", len(text))
