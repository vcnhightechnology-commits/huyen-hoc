# AI-09 — Trạch Nhật — Khâm Định Hiệp Kỷ Biện Phương Thư

**Nhánh được ghi nhận:** `codex/ai-09-trach-nhat`  
**PR được ghi nhận:** 8 (không xác minh trực tiếp tại thời điểm lập)  
**Mốc commit:** 9afb4c2cdd2 (mốc lịch sử rút gọn)  
**Tình trạng phát hành:** nghiên cứu/kiểm thử; **không được suy là đã hợp nhất hoặc được engine chấp nhận**.

## 1. Nguồn và phạm vi

《欽定協紀辨方書》 quyển 11, 35, 36; bản/scan CADAL 06056527; NDL/CiNii và ứng viên sách in 1911 上海錦章書局/SSID-13464303.

## 2. Nội dung nghiên cứu đã khôi phục

- Giữ cấu trúc **dẫn nguồn → lời phê bình → giới hạn áp dụng** tại các quyển 11/35/36, có 8 cặp dẫn/phê không nên rút gọn thành một quy tắc tốt/xấu.
- Khảo các ngày **Dương Công Kỵ**, **Thần tại**, Tứ Bất Tường, Tuần Sơn Nhị Thập Tứ Thần Sát; báo cáo đối chiếu có chênh **35/31** mục Thần tại theo cách cắt nguồn.
- Bảo lưu dị tự `夘` so với `卯` trong các biểu thức như `丁夘/己夘/辛夘/乙夘` thay vì tự chuẩn hóa để đạt test.
- Tạo tập quét 4.096 cấu hình và 53.248 phép kiểm; báo cáo chỉ **2 cấu hình** khớp đủ 13 mốc đang xét. Đó là kiểm khớp dữ liệu, không chứng minh đúng phong tục/trạch nhật ứng dụng.
- Theo lịch sử có 18 tệp nghiên cứu, PR #8 nháp.

## 3. Kiểm thử được ghi nhận

Theo lịch sử: kiểm 4.096 cấu hình × 13 mốc = 53.248 đối chiếu. Trừ phần có log/tệp gốc trong bộ lưu, các số liệu là kết quả báo cáo lịch sử, không được chạy lại toàn bộ trong phiên này.

## 4. Tệp và mã đã tạo/được nhắc đến

Bảng dẫn chứng/dị bản, hồ sơ Thần tại, scripts đánh giá, nguồn/register; không có tệp gốc AI-09 xuất được trong lần này.

## 5. Điều chưa hoàn tất, giới hạn nguồn và hướng nối tiếp

Đối ảnh CADAL và NDL/CiNii, xác định truyền bản, giới hạn theo Dụng sự; chưa nhập engine.

---
