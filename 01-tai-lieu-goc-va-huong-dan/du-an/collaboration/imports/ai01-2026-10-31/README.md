# Tiếp nhận bổ sung AI-01

Đã tiếp nhận gói do người dùng cung cấp ngày 31/10/2026. Tệp nguyên gói `HUYEN_HOC_CAC_AI01_TONG_HOP_TOAN_BO_TAI_LIEU_2026-10-31.zip` có SHA-256 `0f9c75746103ffbcd1a0551a7f04edd174e788c4e6621628e7b8d5e366088524`. `IMPORT_VERIFICATION.json` ánh xạ từng tệp đã nhập với đường dẫn và byte gốc. Việc tải nguyên gói ra kho công khai có trạng thái xác nhận riêng với việc nhập nội dung nghiên cứu.

Nội dung nghiên cứu ở `collaboration/parallel-research/submissions/AI-01/quan-an-quy-an-wuxing-jingji/`: bài học, sáu thẻ tri thức, bảng 18 luận điểm, 12 dị văn, hai ca minh họa, sổ nguồn và câu hỏi mở. `original-text/` giữ tổng hợp, danh mục PR và bản patch nguyên gốc. `evidence/` giải nén chứng cứ kỹ thuật WYG; ảnh và ZIP vẫn ngoài lịch sử Git, lấy từ tài sản phát hành nguyên gói.

Nghiệm thu cục bộ: 26 hash thành viên ZIP ngoài và 10 hash nghiên cứu bên trong đều khớp; bản nghiên cứu lồng trùng byte với bản được gửi riêng. Trình kiểm ví dụ đã chạy và đạt, chỉ kiểm bảng khai báo cùng phép khởi can tháng/giờ, không phải phép so engine độc lập. 36 đoạn atlas S06/S08–S12 khớp đúng vị trí trong chương 690 codepoint nguồn quyển 3 được giữ. Chưa đọc ảnh mới trong lượt nhập, chưa tái thực thi đối ảnh đặc trưng 404 trang quyển 7, chưa xác minh nguồn WXJJ bằng facsimile.

Các báo cáo quyển 7 có `passed: true` là kết quả do bên gửi báo cáo; không tự nhận chúng đã được tái lập ở máy này. Các bài có khẳng định năm cặp Ấn hoặc cách hiểu Lộc–Mệnh–Thân được nhập với tư cách diễn giải của tác giả. Không thay mô-đun cũ đang giữ nhóm Thủy/Thổ hoặc điều kiện năm vị trí bằng diễn giải mới khi chưa đủ chứng cứ.

Lưu ý khi biên tập: `CASE_ANALYSIS.md` nói bảng chọn có 7 can chi, nhưng mã `NAYIN_SELECTED` thực tế khai báo 9 mục (gồm cả các cặp dị văn để so). Bảng được khai báo trong script không phải 9 truy vấn engine đã thực thi. Giữ tài liệu nhập nguyên byte và ghi sai khác tại đây; không tự sửa tài liệu gốc hoặc tăng số kiểm engine.

Gói chỉ chứa liên kết và tổng hợp PR #16, #17, #18 của kho bị khóa; không có toàn văn nguyên tệp các PR đó. Vì vậy chưa khôi phục được bản phân 13 luồng nguyên gốc hoặc các bài trước chỉ từ ZIP này. Những chỉ dẫn hành động trong tài liệu nhập là nội dung lịch sử, không thay yêu cầu hiện tại của người dùng hoặc AGENTS.md.

Tiếp theo: đối ảnh WXJJ quyển 19 cho 本家/木, 五位/或四位, 乙/己 và 乙/癸; giữ nguyên các cách chép, không lấy phép kiểm lịch để sửa văn bản. Tiếp nhận bổ sung không tăng độ phủ áp trọn hoặc xác nhận hiệu nghiệm. Ứng dụng người dùng chưa thay đổi.

Khôi phục ảnh/chứng cứ từ checkout mới: tải ZIP nguyên gói từ release `materials-v53` của `dedaithien-sudo/huyen-hoc`, rồi chạy `python maintenance/restore-ai01-evidence.py <duong-dan-ZIP>`. Script kiểm SHA-256 cả ZIP cùng 98 bản ghi, lấy đúng thành viên bên trong các ZIP lồng và từ chối ghi đè tệp khác byte. Đây là đường phục hồi cho ảnh AI01 mới; 11 gói nguồn trước đó vẫn dùng `maintenance/materials.py` hoặc `maintenance/materials-range.py`.
