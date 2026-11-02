# Chứng cứ phạm vi vị trí Thập thần

- `BEFORE_EXPORT.json` và `before-default-closed.txt`: tái hiện TXT thiếu câu diễn giải trên snapshot cũ.
- `ENGINE_RESULTS.json`: 16 kiểm nguồn/runtime/mô-đun; dữ liệu so thật ở `../../research/bazi-relation-locations/RUNTIME_COMPARISON.json`.
- `BROWSER_RESULTS.json`: 21 kiểm giao diện, lưu/mở, xuất/in và kích thước màn hình.
- `bazi-locations-390.png`, `bazi-locations-1440.png`: ảnh màn hình cuối.
- `bazi-relation-locations.pdf`, `PDF_RESULTS.json`, `final-print-page-1.png` đến `final-print-page-7.png`, `final-print-contact.png`: **bản in cuối**, đã xem đủ bảy trang, không cắt chữ hoặc mất vị trí; tiêu đề nguyệt lệnh đi cùng nội dung.
- `print-page-*.png` và `print-contact.png`: bản render thử cũ đã bị thay thế trong quá trình QA; chế độ media màn hình trong harness ban đầu. Giữ dấu vết, không dùng làm bằng chứng bản in cuối.
- `RELEASE_RESULTS.json`: checkpoint đóng gói; lệnh `verify-bazi-relation-locations-release.py --no-write` đọc lại gói cuối mà không thay đổi manifest.

37 kiểm chính đạt; kiểm văn bản PDF và xem ảnh là chứng cứ bổ sung. Sai khác 23 giờ được giữ riêng, không tính thành ca khớp. Xem `../../BAZI_RELATION_LOCATIONS_REPORT.md` để biết giới hạn.
