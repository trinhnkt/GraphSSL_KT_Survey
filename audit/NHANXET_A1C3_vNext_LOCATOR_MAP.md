# A1–C3 → vNext locator map

**Review:** `15. Check list/2026.11.13/NhanXet_Survey_GraphSSLKT_Trinh_2026Nov13.pdf` (Hậu, 13/11/2026)  
**MS:** `12_manuscript/TLT/Graph_SSL_KT_TLT_REVISED_vNext_full.tex` (line nos. 2026-11-26)

| Mã | Trạng thái | Chỗ trong vNext (section · dòng) | Câu / nội dung khớp |
|---|---|---|---|
| **A1** Corpus thiếu DECKT (+SSL) | **DONE** | Abstract L49; Sec. gateway_ext `\label{sec:gateway_ext}` L196–198; Sec. venue_ext L183–185; Fig.1 L187–192; cite block L206 | “integrates seven gateway-eligible papers… DECKT… DTransformer… SP-CLKT…” → N=53; Branch B bổ sung venue-probe |
| **A2** Calibration ≠ chỉ ECE | **DONE** | Abstract L49; Contrib L143; Sec. ECE audit L487–493; T3 L545–546; Conc. L612 | “None… ECE… or Brier…; 15 report RMSE… not calibration”; “audit is ECE reporting 0/53, not the absence of any calibration-related figure” |
| **A3** Second screener / protocol | **ACCEPTED_DEVIATION** | Sec. ICR L237–240; Deviations L246–250; Threats L595; AI role L202 | “11 title/abstract… 1 full-text”; “treated as a protocol deviation”; **không** đạt đủ 25% historical 750 như đề xuất gốc |
| **A4** Tổng hợp RQ1–RQ3 | **MOSTLY DONE** | RQ list L159–161; Sec. Graph L261–331; Sec. SSL L336–385; Discussion L498+ | Provenance×encoder; fusion subsection L297; leakage L330–331; SSL paradigm×view L346–347; CL4KT aug page-checked L356 |
| **B1** DyGKT ECE overlay | **DONE** | (đã gỡ) — không còn `0.0361` / REPRODUCED trong tex | Threats L601: audit survey ≠ reproduced benchmark |
| **B2** SSL paradigm vs view | **DONE** | Sec. SSL L346–347; Fig. ssl_framework L341; Abstract L49 | “contrastive (n=20) and reconstruction (n=2)… View-source… multi-view… bipartite” |
| **B2b** aug structure-preserve field | **PARTIAL** | L358–385; Table ssl_taxonomy | “none… states that a prerequisite edge is kept or removed” — quan sát có; field riêng 3-value không khóa trong main |
| **B3** CL4KT câu sai / aug gắn bài | **DONE** | L355–356; Table L378+ | “CL4KT… positive pair… question mask… hard-negative view (Sec. 3.5)” |
| **B4** Công thức cold-start ⊆ | **DONE** | Agenda A1 L569–574 | `\subseteq`; “removes every interaction whose exercise contains at least one cold KC” |
| **B4b** Công thức (7) chiều | **DONE/N/A** | Không còn eq (7) LLM–GNN weight trong draft | Audit B4: NOT_IN_CURRENT_DRAFT |
| **B5** Search tái lập | **PARTIAL** | Search L167–181; Identification L187–188; gateway L198 | Scopus Q-S string L178–179; “export files… not deposited”; KT078/080–083 + S-PRISMA-5 L188 |
| **B5b** Recall x/34 seed | **OPEN** | — | Không có câu “x/34 seed records were retrieved” |
| **B6** Bớt jargon/path | **IMPROVED** | Scope L147–149; Methods nén | Vẫn còn `KT###`, `PROVENANCE_COUNTS_LOCKED` (L251), một số `\texttt{...csv}` (L347, L493) |
| **B7** Disclaimer lặp | **IMPROVED** | Scope of Claims L147–149; Threats L591–601 | Gom giới hạn vào Scope + Threats; vẫn nhắc “not league table” vài chỗ hợp lệ |
| **B8** Định vị survey + Shukurlu | **DONE** | Sec. I-C L108–110; Table survey_comparison L124–132 | Shukurlu cited; Zanellati/Xu/Shen columns |
| **B8b** Calibration ngoài corpus | **PARTIAL** | L109 “calibration studies outside that corpus are not coded here” | Chưa cite Yan et al. arXiv:2606.14123 (cố ý/Option B liên quan P0) |
| **B9** Group B rút gọn | **DONE** | Agenda Group B L585–586 | Một đoạn 4 hướng; không còn eq (8)(9) dài |
| **B10** Quan hệ P0 | **DONE (Option B)** | Không cite P0 trong tex | `audit/B10_P0_SURVEY_RELATION.md` |
| **B11** Verify refs | **MOSTLY DONE** | Bib traceability L205–206; `references_vNext.bib` | 53/53 primary keys; spot-check DOI portal vẫn nên làm trước upload |
| **C1** Fig trùng | **OPTIONAL** | Fig taxonomy L266; Fig SSL L341; Fig meta nếu còn | Kiểm tra nhanh khi rảnh — không blocking |
| **C2** Ký hiệu N | **DONE** | Notation table L72–74 | $N_{\mathrm{rec}}$, $N$, $n$ tách; ECE dòng không còn REPRODUCED |
| **C3** QA / sparsity invariant | **DONE** | QA protocol L217–235; L458–481 | “Generic data sparsity… not used”; reporting-completeness; LIMITED = KT091 |

## Việc còn lại gắn nhận xét này
1. Wet-ink KT090–KT098 (gate hiện tại; ngoài A1–C3 gốc).
2. Optional: seed recall x/34 (**B5b**).
3. Optional: bớt thêm token `LOCKED` / path csv (**B6**).
4. Optional: C1 figure dedupe.
