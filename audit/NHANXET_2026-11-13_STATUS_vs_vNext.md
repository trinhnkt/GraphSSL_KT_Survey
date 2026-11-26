# Đối chiếu nhận xét Hậu (13/11/2026) ↔ vNext N=53 (26/11/2026)

**Nguồn:** `15. Check list/2026.11.13/NhanXet_Survey_GraphSSLKT_Trinh_2026Nov13.pdf`  
**Bản lúc nhận xét:** N=37, ~14 trang, ~46 refs  
**Bản hiện tại:** `Graph_SSL_KT_TLT_REVISED_vNext` — N=53, 16 trang, bib ≥65

| Mã | Yêu cầu (tóm tắt) | Trạng thái vNext | Ghi chú |
|---|---|---|---|
| **A1** | Corpus thiếu DECKT (+ SSL khác) | **DONE (mở rộng)** | DECKT + DTransformer + SP-CLKT + CoSKT + HCMKT + … + venue probe → **N=53**. Con số 0/37 đã thay bằng 0/53. |
| **A2** | Calibration không chỉ ECE | **DONE** | ECE 0/53, Brier 0/53, RMSE 15/53; T3 thu hẹp; không gọi RMSE = calibration. |
| **A3** | Second screener / protocol | **PARTIAL / DEVIATION** | Có subset 11+1 đôi; κ screening không định nghĩa; **ghi protocol deviation**. Không khôi phục ledger 750. |
| **A4** | Tổng hợp trả lời RQ1–RQ3 | **MOSTLY DONE** | Taxonomy provenance×encoder + SSL paradigm/view; không còn chỉ đếm N_S=9. |
| **B1** | DyGKT ECE overlay | **DONE** | Overlay gỡ khỏi main text. |
| **B2** | Tách SSL model vs view + structure-preserving aug | **DONE in spirit** | `SSL_TAXONOMY_FINAL`: paradigm vs view; NS=22. Aug structure-preserve: không phải mọi hàng có field riêng — chấp nhận được nếu Threats/Methods nêu giới hạn. |
| **B3** | Câu CL4KT / aug gắn bài | **DONE** | Audit B3. |
| **B4** | Công thức (6)(7) | **DONE** | Audit B4. |
| **B5** | Search tái lập | **PARTIAL** | Cutoff 31/07 + supplementary 23/11 rõ; export gốc 16 file vẫn thiếu → đã nói thẳng. |
| **B6** | Bớt jargon/path/token trong thân bài | **IMPROVED** | Methods đã nén; còn một số inventory ID (KT###) — chấp nhận cho traceability. |
| **B7** | Bớt disclaimer lặp | **IMPROVED** | Threats gom 1 section. |
| **B8** | Định vị survey trước + calibration ngoài corpus | **DONE-ish** | Bảng so sánh Shen/Zanellati/Xu/Shukurlu; ECE scoped trong corpus. |
| **B9** | Agenda Group B bớt chung chung | **DONE-ish** | Group A coded gaps trước Group B. |
| **B10** | Quan hệ P0 | **DONE (Option B)** | Không cite P0; nộp song song. |
| **B11** | Verify refs 2025–2026 | **MOSTLY DONE** | 53/53 primary trong bib; VX authors từ PDF; vẫn nên spot-check DOI portal. |
| **C1** | Fig 2–3 trùng | Kiểm tra nhẹ khi rảnh | Không blocking. |
| **C2** | Ký hiệu N đa nghĩa | **IMPROVED** | Bảng notation; vẫn cần đọc kỹ. |
| **C3** | QA gần invariant | **DONE wording** | “reporting completeness”; thresholds review-defined. |

## Việc còn lại (không phải toàn bộ checklist cũ)

1. **Wet-ink KT090–KT098** (blocker gate hiện tại) — `06_coding/VX_WETINK_HOWTO.md`
2. A3: chấp nhận deviation đã viết; **không** cố bịa κ historical.
3. Optional: seed recall x/34 nếu muốn đáp đúng chữ A1 điểm 5 của nhận xét (chưa bắt buộc cho READY nếu đã mở rộng corpus + nói ledger thiếu).

## Kết luận
Hầu hết mức **A/B** của nhận xét 13/11 đã được xử lý qua đợt mở rộng N=53 + vNext.  
**Không nộp** cho đến khi wet-ink VX xong và gate = YES.
