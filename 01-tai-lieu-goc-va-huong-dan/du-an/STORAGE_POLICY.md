# Chính sách lưu trữ Huyền Học Các

Yêu cầu người dùng ngày 29/10/2026 thay chính sách giữ mọi bản cũ: mỗi loại chỉ giữ một bản mới nhất, tổng hợp đầy đủ dữ liệu riêng cần giữ từ bản cũ.

- Giữ một HTML phát hành mới nhất, một ZIP web mới nhất, một ZIP nguồn tổng hợp mới nhất. HTML dùng trong site/build là bản làm việc cần thiết, không tạo bản sao theo mốc.
- Nguồn gốc, byte/SHA-256 và bằng chứng duy nhất phải giữ trước khi dọn. Các nội dung lịch sử còn riêng được gom theo mã băm và bảng ánh xạ xuất xứ; không nhân toàn bộ ZIP qua từng lần cập nhật.
- Không tạo thêm `archives/v53-before-*` chứa ZIP toàn bộ. Không chạy các script tiếp nhận/kiểm lịch sử yêu cầu giữ snapshot cũ nếu chưa chuyển sang tra chỉ mục tổng hợp.
- Khi đóng một phạm vi có ích, cập nhật nguyên tử ZIP mới nhất. Chỉ xóa dữ liệu cũ sau khi nội dung cần giữ đã có trong tập tổng hợp và được kiểm chứng.
- ZIP, thư mục lưu trữ, dữ liệu tạm và nguồn nhị phân lớn ở ngoài checkpoint Git theo `.gitignore`. Git giữ mã nguồn/văn bản nhỏ; không đưa ZIP nguồn trở lại object database.
- Lịch sử chat Codex và bản chat đã khôi phục được giữ; thao tác dọn này không xóa SQLite hoặc các phiên chat trong `.codex`.
- Đang có khóa `recovery/storage-consolidation/MAINTENANCE.json`: ưu tiên hoàn tất hợp nhất/dọn, không chạy nghiên cứu/đóng gói nặng song song. Xem trạng thái khóa trước lượt tự động tiếp theo.

Các script/báo cáo phát hành cũ là chứng cứ lịch sử. Sau hợp nhất, đường dẫn snapshot cũ được xử lý qua chỉ mục phục hồi tổng hợp; không được dựng thêm bản full ZIP để làm các script cũ vượt kiểm.
