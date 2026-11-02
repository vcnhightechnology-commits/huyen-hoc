# Quyển 3: ngoại ứng và điều kiện vật tượng

Đọc liên tục ảnh PDF103–144 của bản đã lưu. Đây là 42 bản ghi có giới hạn:41trang nội dung,27trang nội dung mới/14mở rộng và1trang kết đã đọc trước. Không nhận là phiên âm đủ mọi chữ hoặc áp hết sách.

- `MANUAL_READINGS.json`: ghi rõ phạm vi từng trang, SHA ảnh và PDF; không OCR/tải/render mới.
- `UNIT_MAP.json`: nối26đề mục số đã ghim với41trang nội dung; phần cuối chữ là143/in41,kết144/in42.
- `MATERIAL_PREMISES.json`:13đối chiếu có điều kiện từ109–110. Các mức là lời nhận định truyền thống,không phải trọng số khoa học/xác suất/kết quả đã kiểm nghiệm.
- `CONTEXT_PREMISES.json`: động/tĩnh của vật và người quan sát tách riêng;4chính sách vai trò,10tên ứng và10hàng hành động khác; không tính ngày dự báo.
- `external-reference.mjs`: chỉ tham chiếu nội bộ. Chọn trường hợp nguồn,quái và mô tả quan sát rõ ràng; không nhận diện vật từ tên/câu hỏi. Kết quả vật chất tách khỏi đồ thị biểu tượng cũ; không tự cộng điểm hoặc kết luận.
- `WORKED_EXAMPLES.json`:11.1→46 và50.6→32 đúng số học. Giả thuyết sơ bộ sai về50→32 đã bị engine bác bỏ trước khi phát hành; không nâng giai thoại thành kiểm chứng tiên đoán.
- `VARIANTS_AND_GAPS.json`:7vấn đề văn bản/ngữ cảnh còn giữ riêng. Không sửa nguồn Hán hoặc chính sách toàn cục từ một đoạn địa phương.

`node v53/scripts/verify-meihua-external.mjs`:11kiểm nguồn/runtime,104cặp quẻ/bối cảnh mới,12tổ hợp động/tĩnh vàhai ví dụ in. HTML đang dùng không đổi. CandidateThể–Dụng vẫn ở thư mục riêng,chưa nhận đã kiểm browser/PDF.

Quyển1,các mệnh đề phụ quyển2/3/4/5,bảng133–143từng trường,nhân chứng độc lập và độ đúng dự báo vẫn mở. Xem `../../MEIHUA_EXTERNAL_REPORT.md`.
