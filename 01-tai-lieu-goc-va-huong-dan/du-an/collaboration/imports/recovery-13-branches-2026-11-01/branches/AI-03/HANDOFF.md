# AI-03 — Tử Vi — Đại hạn, Tiểu hạn và Tứ Hóa

**Nhánh được ghi nhận:** `codex/ai-03-tu-vi`  
**PR được ghi nhận:** 2 (không xác minh trực tiếp tại thời điểm lập)  
**Mốc commit:** 712aa2ae9160c917c6a8021fa84b51389e75f0b0 (theo lịch sử)  
**Tình trạng phát hành:** nghiên cứu/kiểm thử; **không được suy là đã hợp nhất hoặc được engine chấp nhận**.

## 1. Nguồn và phạm vi

《紫微斗數全書》 (Tử Vi Toàn Thư), Shidian và các bảng Tứ Hóa theo nhiều dòng truyền bản.

## 2. Nội dung nghiên cứu đã khôi phục

- Khảo cứu quy trình khởi Đại hạn, Tiểu hạn, cung khởi, tuổi hạn và khác biệt phương pháp giữa các bản. Điểm đối chiếu chính là **Tiểu hạn nam thuận/nữ nghịch** trong một bản so với quy tắc **bốn nhóm chi/cung khởi** ở Shidian; hai hệ chưa được coi là tương đương.
- Lập ma trận **10 thiên can × 4 hóa** (Hóa Lộc, Hóa Quyền, Hóa Khoa, Hóa Kỵ), lưu các bất đồng thay vì xóa dị bản để ép khớp. Có nghiên cứu và QA đối với những tình huống đầu vào chưa đủ tiền đề.
- Đã báo cáo 279 ca kiểm và 1.578 vị trí bất định; những con số này là kiểm dữ liệu/ràng buộc, không phải bằng chứng dự đoán tử vi chính xác.
- Lần nghiên cứu trước ghi nhận 33 tệp và 6 commit riêng, PR #2 ở dạng nháp.

## 3. Kiểm thử được ghi nhận

Theo cuộc nghiên cứu trước: 279 ca kiểm; 1.578 bất biến/điểm không xác định được giữ lại. Trừ phần có log/tệp gốc trong bộ lưu, các số liệu là kết quả báo cáo lịch sử, không được chạy lại toàn bộ trong phiên này.

## 4. Tệp và mã đã tạo/được nhắc đến

Đã ghi nhận mã kiểm và các tệp ma trận/đối chiếu trên nhánh trong hội thoại; hiện không có bản sao nguyên byte thuộc nhánh này để đóng gói.

## 5. Điều chưa hoàn tất, giới hạn nguồn và hướng nối tiếp

Cần đối ảnh nguồn Tứ Hóa Canh, xác minh quy tắc tháng nhuận an Mệnh–Thân, Thân chủ Hỏa–Linh, miếu/vượng/hãm và khởi Đại hạn; chưa kiểm lại CI hoặc trình duyệt.

---
