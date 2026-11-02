# Quy trình phối hợp nghiên cứu

1. Đọc AGENTS.md ở gốc kho, rồi vào `du-an/` đọc chính sách lưu trữ, trạng thái nghiên cứu, NEXT_STEPS và ma trận độ phủ. Các con trỏ M01 cũ được giữ; yêu cầu mới đang ưu tiên AI-01.
2. Chọn README của một trong 13 mục. Đọc hồ sơ phục hồi và thư mục submission được dẫn; ghi rõ phạm vi đang nhận trong `WORK_LOG.md` của mục đó trên nhánh riêng.
3. Mở nhánh `codex/ai-xx-ten-viec` từ nhánh chung hiện hành. Xác nhận base commit; tránh sửa chồng engine hoặc trạng thái chung với AI khác. Đề xuất thay đổi trạng thái chung qua Merge Request.
4. Lấy đúng nguồn theo manifest, kiểm SHA-256 trước đọc. Phân biệt nguồn gốc, bản chép, ảnh dẫn xuất, quy ước, suy luận và chưa xác minh. Lưu tọa độ trang/tờ, URL và phần ảnh đã thực sự đọc. Không đếm URL hoặc bản chép web thành truyền bản độc lập.
5. Mỗi luận điểm ghi đầy đủ điều kiện, ngoại lệ, chủ thể và vị trí trụ. Không lấp chỗ thiếu bằng kiến thức hiện đại hoặc điểm số tùy ý. Quy tắc chưa đủ điều kiện giữ trong nghiên cứu, không đưa thành kết luận tự động.
6. Nếu thay mã, thực thi engine thật và kiểm phù hợp. Tái dùng payload đã giữ khi có thể; không tự gọi số kiểm lịch sử là kiểm hiện tại. Không đưa corpus, QA hay bảng so engine lên giao diện người dùng.
7. Cập nhật WORK_LOG, nguồn, câu hỏi mở, kết quả kiểm và bước tiếp. Merge Request ghi rõ tệp sửa, căn cứ, giới hạn, dữ liệu cần tải thêm. Không tự merge hoặc tạo nhiều bản ZIP phát hành.

Hồ sơ phục hồi có 3/33 tài sản byte gốc; 25 bản trích chưa xác minh byte và 5 tài sản chưa lấy được. AI-10 mới có 13/24 tệp kiểm theo hồ sơ. Không thực thi mã trích để chứng minh các số cũ. Những giới hạn này phải tiếp tục đi theo kết quả nghiên cứu.

Lưu ý AI-01: ghi chú đối ảnh mới nhất đã cập nhật cách đọc can tháng ở scan NLC 06857 p.50; một số hồ sơ cũ vẫn ghi chưa phân xử. Ưu tiên báo cáo facsimile hiện hành, giữ lịch sử trước đó và chưa coi dị văn là một luật engine.
