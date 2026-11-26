# VX wet-ink HOWTO (KT090–KT098)

## Mục tiêu
Đổi `AI_ONLY` → `HUMAN_VERIFIED` rồi mở `TLT_SUBMISSION_READY = YES`.

## Bước nhanh

1. **Đọc PDF** theo thứ tự trong  
   `HUMAN_VERIFY_SIGNOFF_KT090-098_v2_HUMAN.md`  
   (dùng quote ở `HUMAN_VERIFY_EVIDENCE_PACK_KT090-098_v1.md`).

2. **Điền signoff v2** — gõ tên + ngày + KEEP/CHANGE từng paper.  
   Không để `_FILL_`.

3. **Điền CSV fillable**  
   `audit/VENUE_PROBE_HUMAN_VERIFICATION_FILLABLE.csv`

   Ví dụ một dòng PASS:

   ```text
   KT092,GRKT,YES,YES,YES,NA,YES,YES,Nguyen Khanh Trinh,2026-11-26,HUMAN_VERIFIED,wet-ink; S=NO confirmed p.X
   ```

   - `ssl_code_verified`: dùng `NA` nếu S=NO (KT090–092); `YES` nếu S=YES.
   - `status` phải là `HUMAN_VERIFIED` cho cả 9 nếu muốn READY.

4. **Chạy apply script**

   ```powershell
   python D:\TRINH\GraphSSL_KT_Survey\audit\_apply_vx_human_verify_2026-11-26.py
   ```

   Script sẽ:
   - ghi `audit/VENUE_PROBE_HUMAN_VERIFICATION.csv`
   - nếu cả 9 = `HUMAN_VERIFIED`: sửa wording vNext + flip gate YES  
   - nếu còn placeholder: **không** đổi manuscript / READY

5. **Rebuild PDF**

   ```powershell
   cd D:\TRINH\GraphSSL_KT_Survey\12_manuscript\TLT
   pdflatex Graph_SSL_KT_TLT_REVISED_vNext_full.tex
   bibtex Graph_SSL_KT_TLT_REVISED_vNext_full
   pdflatex Graph_SSL_KT_TLT_REVISED_vNext_full.tex
   pdflatex Graph_SSL_KT_TLT_REVISED_vNext_full.tex
   # tương tự anonymous
   ```

6. Kiểm tra `audit/TLT_FINAL_PRE_SUBMISSION_GATE_vNext.md` → READY = YES.

## Không làm
- Không bịa tên verifier.
- Không đổi S của KT092 thành YES chỉ vì related-work có “contrastive”.
- Không nộp PDF title cũ.
