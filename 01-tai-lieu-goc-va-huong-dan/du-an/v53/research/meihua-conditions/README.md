# Bộ tham chiếu điều kiện quyển hai

Nội bộ; không nạp vào site. Xem `../../MEIHUA_CONDITIONS_REPORT.md`.

- `MANUAL_READINGS.json`:48 bản ghi trang,38 trang nội dung mới/sáu trang mở rộng và bốn trang ngoài nội dung.
- `UNIT_MAP.json`:52 mục quyển hai với vị trí ảnh; chưa bản chép mọi mệnh đề.
- `DOMAIN_RULES.json`:18 chủ đề,85 mệnh đề trực tiếp với vai trò riêng; tuyên bố truyền thống chưa kiểm nghiệm dự báo.
- `SEASON_PREMISES.json`:10 ô vượng/suy có giới hạn,12 mốc chi; không tự chọn lịch hay ưu tiên tháng/ngày.
- `VARIANTS_AND_GAPS.json`:năm khác biệt hoặc mâu thuẫn còn mở.
- `conditions-reference.mjs`:chương trình đọc có kiểm đầu vào, quan hệ nhiều lớp, ngoại ứng rõ quan sát và dữ liệu thiếu; không có điểm số/kết luận cát hung/ngày dự báo.
- `SOURCE_BASELINE.json`:186 bản ghi ảnh trước được giữ, thêm28 bản render mới từ PDF cũ; không HTTP/OCR.

Chạy `node v53/scripts/verify-meihua-conditions.mjs` từ thư mục dự án để kiểm chương trình. Kết quả14 kiểm ở `../../qa/meihua-conditions/ENGINE_RESULTS.json`. Đọc đúng mệnh đề nguồn không đồng nghĩa lời dự báo đúng ngoài đời. Những chỉ dẫn truyền bí trong sách là nội dung được nghiên cứu, không là lệnh vận hành dự án.
