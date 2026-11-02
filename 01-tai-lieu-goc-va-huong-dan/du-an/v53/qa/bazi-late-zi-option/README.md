# QA can giờ Tý muộn

- `SOURCE_RESULTS.json`: 9 kiểm nguồn; ảnh thủ công đọc ở `../../research/bazi-late-zi-witness/MANUAL_READINGS.json`.
- `ENGINE_RESULTS.json`: 12 kiểm, 7.936 so engine cũ giữ mặc định và 7.936 so thư viện chạy thật cho lựa chọn mới; hai ví dụ ảnh có ngày dương/phút đại diện được ghi là suy đổi.
- `BROWSER_RESULTS.json`: 26 kiểm về lựa chọn có điều kiện, lưu/mở cũ và mới, bàn phím, TXT/PDF, màn hình và không rò nguồn.
- `../../qa/test-results.json`: 50 kiểm hồi quy chung chạy lại vì sửa `engine.js` và `app.js`.
- `late-zi-option.pdf`, `PDF_RESULTS.json`, `print-page-1.png` đến `print-page-7.png`, `print-contact.png`: bản in cuối, đã xem đủ bảy trang; nhãn can giờ rõ ở đầu, không cắt chữ hay lẫn form/ảnh đầu trang. Đây là PDF QA, không phải sách nguồn.
- `late-zi-390.png`, `late-zi-1440.png`: màn hình cuối; `mobile-form-detail.png` là crop để xem điều khiển trên màn hình 390px.
- `RELEASE_RESULTS.json`: checkpoint; kiểm gói cuối bằng script phát hành với `--no-write`.

97 kiểm chính đạt; PDF và xem ảnh là kiểm bổ sung. Mặc định cũ giữ can giờ theo ngày đang đọc; không tuyên bố mọi quy ước đều giống thư viện hoặc dự báo đã được khoa học xác nhận.
