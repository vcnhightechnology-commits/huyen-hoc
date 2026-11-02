# AI-06 — Chu Dịch — Kinh văn, Thập Dực và khảo dị

**Nhánh được ghi nhận:** `codex/ai-06-chu-dich`  
**PR được ghi nhận:** PR nháp có ghi nhận, chưa xác định số (không xác minh trực tiếp tại thời điểm lập)  
**Mốc commit:** Không kiểm được SHA HEAD hiện thời  
**Tình trạng phát hành:** nghiên cứu/kiểm thử; **không được suy là đã hợp nhất hoặc được engine chấp nhận**.

## 1. Nguồn và phạm vi

《周易》/《易經》, Thập Dực, Tự Quái, Tạp Quái, Thuyết Quái và các phiên bản văn bản cổ số hóa.

## 2. Nội dung nghiên cứu đã khôi phục

- Thiết lập không gian **64 quẻ × 6 hào = 384 vị trí**, phân biệt thứ tự quẻ/hào với nguồn ghi chép và các lời chú.
- Ghi **61 dị văn** và **16 vị trí đối chiếu hai nguồn**. Có 15/16 trùng chữ; trường hợp **Đại Súc quẻ 26, hào 3** có bất đồng `曰/日`, cần tách câu chính văn khỏi bình chú, không xem số hóa là nguyên bản tối hậu.
- Mở rộng Thập Dực: **10 thiên/7 nhóm**, Tự Quái có 63 quan hệ quẻ kề nhau nhưng chỉ 61 lời nối được xác định; xem riêng ranh 30→31 và mẫu thiếu `以`. Tạp Quái có các khác biệt trong cùng nguồn/trang, không coi nhầm thành hai ấn bản.
- Hồ sơ đã báo cáo `ALL_61_VARIANTS.json`, `CASE_LEDGER.json`, `THEORY_MATRIX.md`, `SOURCE_REGISTER.md`, `OPEN_QUESTIONS.md`, `audit_yi06.py`.

## 3. Kiểm thử được ghi nhận

Theo lịch sử: 384 vị trí hào, 61 dị văn, 16 liên kết đối chiếu; 15/16 khớp chữ. Trừ phần có log/tệp gốc trong bộ lưu, các số liệu là kết quả báo cáo lịch sử, không được chạy lại toàn bộ trong phiên này.

## 4. Tệp và mã đã tạo/được nhắc đến

Tên tệp nghiên cứu và validator được ghi nhận trong hội thoại; chưa truy xuất được nguyên mã/JSON của nhánh AI-06.

## 5. Điều chưa hoàn tất, giới hạn nguồn và hướng nối tiếp

Cần đối lại chữ với ảnh in/đồ hình và nguồn độc lập, chạy validator trên checkout đầy đủ và đánh dấu phân biệt chính kinh/truyện/chú.

---
