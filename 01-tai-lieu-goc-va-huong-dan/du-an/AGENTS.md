# Huyền Học Các: lưu trữ và tiếp tục công việc

- Đọc `STORAGE_POLICY.md` trước mọi thao tác đóng gói, sao lưu hoặc dọn dữ liệu. Đây là chính sách mới do người dùng yêu cầu29/10/2026, thay yêu cầu cũ giữ mọi bản snapshot.
- Mỗi loại giữ một bản phát hành mới nhất đã tổng hợp dữ liệu cần thiết. Không tạo lại `archives/v53-before-*` hoặc chép full ZIP sau từng phạm vi nhỏ.
- Nguồn gốc và chứng cứ riêng được giữ theo SHA-256 tại chỉ mục tổng hợp. Không xóa nguồn duy nhất hoặc lịch sử chat Codex.
- Không đưa ZIP, backup và binary nguồn lớn vào Git checkpoint. Tôn trọng `.gitignore`; kiểm rằng không có tiến trình Git đang ghi full ZIP khi dọn object database.
- Trong khi `recovery/storage-consolidation/MAINTENANCE.json` có `status: active`, tiếp tục công việc hợp nhất/dọn đang dở; không chạy nghiên cứu/đóng gói nặng song song.
- Script/báo cáo cũ là lịch sử. Các kiểm dựa trên snapshot đã hợp nhất không còn là kiểm phát hành hiện hành; dùng `maintenance/` và báo cáo tổng hợp mới nhất.
