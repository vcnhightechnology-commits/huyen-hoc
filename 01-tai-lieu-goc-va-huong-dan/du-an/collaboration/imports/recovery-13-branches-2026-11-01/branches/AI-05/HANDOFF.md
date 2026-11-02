# AI-05 — Mai Hoa Dịch Số — Lục thần, Thể–Dụng, ngoại ứng

**Nhánh được ghi nhận:** `codex/ai-05-mai-hoa`  
**PR được ghi nhận:** 6 (không xác minh trực tiếp tại thời điểm lập)  
**Mốc commit:** Không có SHA cuối được xác minh lại  
**Tình trạng phát hành:** nghiên cứu/kiểm thử; **không được suy là đã hợp nhất hoặc được engine chấp nhận**.

## 1. Nguồn và phạm vi

《梅花易數》, bản in/scan năm 1925 (12 trang được tham chiếu trong nghiên cứu); phân biệt các truyền bản trong lập quẻ và chiết tự.

## 2. Nội dung nghiên cứu đã khôi phục

- Phát hiện trường `season` có thể bị nhầm với **địa chi** nếu dữ liệu thiếu kiểu/phạm vi; bổ sung kiểm rõ mùa, tháng, ngày và quy ước ngũ hành.
- Tách **Lục thần theo thiên can ngày** với cách giải thích nét chữ/chiết tự; không suy một quy tắc từ tên giống nhau của hai học phái.
- Ma trận theo dõi **18 chủ đề, 85 mệnh đề**, mỗi mệnh đề cần nguồn/điều kiện/ngoại lệ/trạng thái. Đã kiểm các cặp mùa–hành (25) và chi–hành (60) theo định nghĩa dữ liệu được khai báo.
- Hội thoại ghi 11 tệp mới, 2 tệp cập nhật, 26 commit trên nhánh và PR #6 nháp; chưa nhập vào engine.

## 3. Kiểm thử được ghi nhận

Theo lịch sử: 18 chủ đề/85 mệnh đề; 12/12 nhóm kiểm, 25 mùa–ngũ hành và 60 chi–ngũ hành. Trừ phần có log/tệp gốc trong bộ lưu, các số liệu là kết quả báo cáo lịch sử, không được chạy lại toàn bộ trong phiên này.

## 4. Tệp và mã đã tạo/được nhắc đến

Ma trận `THEORY_MATRIX`, tài liệu nguồn, test script và báo cáo trong lịch sử; không có bản sao byte gốc hiện truy xuất được.

## 5. Điều chưa hoàn tất, giới hạn nguồn và hướng nối tiếp

Dị bản lập quẻ, điều kiện Thể/Dụng và Hậu thiên thời-phương, ngoại ứng, đoán chữ; không gắn suy luận khi chưa xác định bản và ngữ cảnh.

---
