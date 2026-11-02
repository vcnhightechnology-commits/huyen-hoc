# AI-08 — Dương Trạch — 24 Sơn, Song Sơn và Phóng Thủy

**Nhánh được ghi nhận:** `codex/ai-08-duong-trach`  
**PR được ghi nhận:** 7 (không xác minh trực tiếp tại thời điểm lập)  
**Mốc commit:** Không kiểm được SHA HEAD hiện thời  
**Tình trạng phát hành:** nghiên cứu/kiểm thử; **không được suy là đã hợp nhất hoặc được engine chấp nhận**.

## 1. Nguồn và phạm vi

《陽宅十書》/Dương Trạch Thập Thư, chương `論放水第七`, scan PDF các trang 107, 109 và 110.

## 2. Nội dung nghiên cứu đã khôi phục

- So sánh bảng **24 Sơn** và các cặp **song sơn**; trong 12 cặp có 8 cặp được ghi nhận khác dòng bảng chính của nguồn đối chiếu — cần giữ đúng trường phái và phân loại.
- Bảng **phóng thủy** có dị biệt cụ thể ở hàng `未`; cần kiểm scan trang 110 trước khi xác nhận dữ liệu.
- Điều kiện bản văn `只放天干水為宜` (chỉ nên phóng nước Thiên Can) phải gắn với đúng phạm vi bảng, không áp dụng vô điều kiện.
- Có bộ `audit_crosswalk.py` kiểm bảng và 7/7 ca Python; 9 tệp nghiên cứu và PR #7 nháp theo lịch sử.

## 3. Kiểm thử được ghi nhận

Theo lịch sử: 7/7 Python unit tests đạt. Trừ phần có log/tệp gốc trong bộ lưu, các số liệu là kết quả báo cáo lịch sử, không được chạy lại toàn bộ trong phiên này.

## 4. Tệp và mã đã tạo/được nhắc đến

`audit_crosswalk.py`, dữ liệu crosswalk, tests, `README.md`, `SOURCE_REGISTER.md`, `THEORY_MATRIX.md`, `OPEN_QUESTIONS.md`, `RESEARCH_STATE.json` (chưa xuất nguyên byte).

## 5. Điều chưa hoàn tất, giới hạn nguồn và hướng nối tiếp

Đối ảnh trang 107 (âm dương), 109 (điều kiện), 110 (hàng 未); không gộp song sơn hoặc suy quy tắc duy nhất khi các truyền bản khác nhau.

---
