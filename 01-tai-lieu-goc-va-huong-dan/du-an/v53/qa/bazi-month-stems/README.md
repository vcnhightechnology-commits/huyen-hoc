# QA phần can tháng

7 kiểm nguồn +13 nguồn/engine +21 UI +50 hồi quy trong `../test-results.json` =91 kiểm chính. Kiểm văn bản PDF và xem ảnh không cộng vào số đó.

`ENGINE_RESULTS.json` giữ16fixture nguồn,4trường hợp Chính Quan ngoài bản khí, mẫu so2928lá số và số vị trí thực. Fixture là lá số thử hiện đại khớp hai trường nguồn, không xác nhận ngày sinh lịch sử. `SOURCE_RESULTS.json` giữ chênh kích thước ảnh1 và HTTP429; cả hai không được dùng để nâng mức chứng cứ.

`month-stems.pdf`, `PDF_RESULTS.json`, `print-page-1.png` đến `print-page-8.png`, `print-contact.png`: bản in cuối đã xem đủ tám trang. Nhóm tháng không bị tách tiêu đề khỏi thẻ, bảng mười vận giữ đủ cùng trang trong mẫu; không cắt chữ hoặc đưa form/nguồn lên bản đọc. `month-stems-390.png` và `month-stems-1440.png` là phần chi tiết trên màn hình.

`RELEASE_RESULTS.json` là checkpoint đóng gói; lệnh phát hành `--no-write` kiểm lại gói cuối. Tài liệu chính `../../BAZI_MONTH_STEMS_REPORT.md`.
