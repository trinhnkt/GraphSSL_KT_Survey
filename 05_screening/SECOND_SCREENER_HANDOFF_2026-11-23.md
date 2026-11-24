# Phiếu giao cho người sàng lọc thứ hai

Ngày lập: 2026-11-23. Phiếu này để trống phần quyết định. Trợ lý không điền hộ và không tính kappa.

## Ai được điền

Một người không có tên trên bài. Bốn tác giả không điền phiếu này: Nguyễn Khánh Trình, Đào Minh Tuấn, Nguyễn Tiến Dương, Nguyễn Chí Thanh. Người điền không xem các file sàng lọc cũ và không xem mục gateway trong bản thảo.

## Việc làm được ngay

Đọc bảy PDF trong `14_references`, đúng tên file ở cột `pdf_filename` của `inter_rater_fulltext_SEVEN_BLIND_EMPTY_2026-11-23.csv`. Với mỗi bài, điền một nhãn vào cột `decision`:

- `PRIMARY_CORE` khi bài là tiếng Anh, là bài tạp chí hoặc hội nghị có phản biện, knowledge tracing là nhiệm vụ chính, đủ chi tiết phương pháp, đọc được toàn văn, và có ít nhất một trong hai: đồ thị tường minh được mô hình dùng, hoặc mục tiêu tự giám sát lấy nhãn từ chính dữ liệu.
- `PRIMARY_ADJACENT_SPARSE` khi knowledge tracing là chính, độ thưa hoặc cold-start là trọng tâm, nhưng không có đồ thị và không có tự giám sát.
- `PRIMARY_ADJACENT_METHOD` khi bài hữu ích cho hiệu chỉnh, rò rỉ, hoặc tái lập, nhưng không phải bài Graph/SSL chính.
- `BACKGROUND` khi bài là nền, không phải mô hình cần mã hóa.
- `EXCLUDE_FULLTEXT` khi loại. Khi đó điền một mã vào `exclusion_code`: `EC1_NO_KT`, `EC2_CD_ONLY`, `EC3_RECOMMENDATION_ONLY`, `EC4_GENERIC_GRAPH_SSL`, `EC5_LLM_TUTOR_ONLY`, `EC6_SPARSE_ATTENTION_ONLY`, `EC7_WRONG_PUBLICATION_TYPE`, `EC8_DUPLICATE_SUPERSEDED`, `EC9_INSUFFICIENT_METHOD`, `EC10_NON_ENGLISH`, `EC11_PERFORMANCE_PREDICTION_NOT_KT`, `EC12_OUTSIDE_DATE_WINDOW`. `EC13_OTHER` chỉ khi không mã nào khác đúng, và cột `note` phải ghi lý do.

Đồ thị không đòi hỏi GNN. Điểm tương đồng hoặc attention chưa phải đồ thị. Pretraining thông thường chưa phải tự giám sát.

Điền tên người sàng lọc vào `screener_name`. Lưu file đã điền thành một bản mới, không ghi đè file trống.

## Việc phiếu này không thay

Protocol còn yêu cầu 25% bản ghi sau khử trùng ở tiêu đề và tóm tắt, cộng mọi bản ghi `UNCERTAIN`, và ở toàn văn thì mọi quyết định loại cộng ít nhất 25% mọi quyết định. Các danh sách 750, 610 và 103 bản ghi không có trong kho. Bảy dòng trong phiếu này không phải mẫu đó, và chưa đủ để báo cáo kappa sàng lọc.
