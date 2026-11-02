# Kiểm tra ranh tháng trên kho HKO 1901–2100

Hoàn thành 26/10/2026, nối tiếp bảng tháng vận hạn V53. Đây là kiểm chứng bổ sung cho một chức năng đã có, không mở phiên bản mới hoặc thay bộ lịch chỉ để làm khớp số liệu. Web, HTML phát hành và ZIP người dùng giữ nguyên byte; cập nhật tài liệu, manifest và gói nguồn.

## Phạm vi và nguồn

Tái sử dụng **200 thân phản hồi TXT gốc HKO** trong `v46/evidence/hko/`, đã tải bằng HTTPS và lưu từ trước. Kiểm lại toàn bộ độ dài và SHA-256 so với manifest gốc, trạng thái HTTP200/TLS tại thời điểm tải và liên kết từng TXT từ index đã lưu. Không tải lại cùng nguồn. SHA là định danh byte bản lưu, không phải chữ ký số HKO.

Bộ kiểm mới phân tích độc lập trực tiếp từng dòng tiếng Anh: ngày dương, thứ trong tuần, ngày âm hoặc nhãn bắt đầu tháng. Tháng nhuận được suy từ hai nhãn tháng liên tiếp trùng số; năm âm suy từ chuỗi chuyển tháng. Không dùng kết quả HHC để điền năm âm/nhuận vào tham chiếu, cũng không nói TXT có cột năm âm/nhuận tường minh.

Đọc được **73.048 dòng ngày dương**, khôi phục đầy đủ các mốc tháng đã dùng trong V46. Nguồn năm 2069 thiếu dòng **30/12/2069**; giữ đúng khoảng trống này, không thêm dòng do engine tính. Mốc tháng hai phía vẫn có, nên việc so ngày đầu/cuối tháng không đòi điền ngày bị thiếu.

Tham chiếu là lịch **UTC+8**. Không gán chứng cứ HKO cho UTC+7. Nhóm kiểm riêng UTC+7 bên dưới chỉ là sự nhất quán giữa hai luồng dùng cùng engine.

## Kết quả ranh tháng

Chạy bảng tháng thật cho 200 năm, ghép theo năm âm/số tháng/cờ nhuận. So **2.472 khoảng đầy đủ**, lấy ngày đầu từ mốc HKO và ngày cuối bằng ngày trước mốc kế tiếp đã công bố. Không đưa tháng đầu bị cụt của năm âm1900 hoặc tháng cuối chưa có mốc sau trong kho vào tổng này.

| Kết quả | Số khoảng |
|---|---:|
| Khớp cả ngày đầu và cuối | 2.464 |
| Có khác biệt ranh ngày | 8 |
| Khác biệt vẫn có nút điều hướng khả dụng | **0** |
| Không tìm thấy dòng tương ứng trong bảng | **0** |

Tám khoảng khác biệt thuộc các ranh đã biết, không phải tám lỗi mới được bỏ ngỏ trên web:

| Năm âm/tháng | Khoảng HKO UTC+8 | Khoảng do bảng hiện tại tạo |
|---|---|---|
| 1914/9 | 19/10–16/11/1914 | 19/10–17/11/1914 |
| 1914/10 | 17/11–16/12/1914 | 18/11–16/12/1914 |
| 1915/12 | 5/1–2/2/1916 | 5/1–3/2/1916 |
| 1916/1 | 3/2–3/3/1916 | 4/2–3/3/1916 |
| 1920/9 | 12/10–9/11/1920 | 12/10–10/11/1920 |
| 1920/10 | 10/11–9/12/1920 | 11/11–9/12/1920 |
| 2097/6 | 9/7–6/8/2097 | 9/7–7/8/2097 |
| 2097/7 | 7/8–5/9/2097 | 8/8–5/9/2097 |

Cả tám dòng đều đã có trạng thái không khả dụng và lời yêu cầu xác nhận lịch. Không coi dòng bị khóa là đã sửa lịch; không đổi kết quả engine theo HKO một cách cục bộ. Các khác biệt từng ngày, tham số lịch1906/2057 hoặc năng lực tiên đoán không được giải quyết bởi phép so ranh tháng này. Tháng có cùng hai ranh cũng không chứng minh mọi ngày/chính sách lịch bên trong đều đã xác thực độc lập.

## Tính nhất quán của hai luồng

Đã chạy `solarToLunar` thật cho từng ngày dương 1901–2100, gom tháng theo kết quả trả về rồi so lại bảng tháng. Mỗi múi giờ UTC+7 và UTC+8 có **2.472 nhóm tháng đầy đủ** trong miền kiểm; cả hai đều không lệch ranh, không thiếu dòng. Điều này kiểm rằng bảng tháng không tạo ranh khác lịch hằng ngày của chính ứng dụng. Vì hai phía cùng dùng bộ lịch HHC, đây **không** phải hai nguồn lịch độc lập hoặc bằng chứng tuyệt đối cho ngày sóc.

Kiểm ranh dùng chế độ cùng tháng; ba chính sách vận hạn, tháng nhuận chia ngày16, trước sinh, lịch nhạy và cuối2100 đã có kiểm riêng trong `FORTUNE_MONTHS_REPORT.md`. Lượt này không chạy lại 464 horoscope iztro hoặc toàn bộ trình duyệt khi không đổi mã sản phẩm.

## Tái lập, chứng cứ và phát hành

- `node scripts/audit-month-boundaries.mjs`: chạy bảng tháng thật và ghi `research/month-boundaries/before.json`. Tên tệp giữ từ bước khảo sát ban đầu; không có thay đổi lịch để tạo một kết quả “sau sửa” giả định.
- `node scripts/audit-month-roundtrip.mjs`: kiểm với luồng lịch theo ngày, ghi `roundtrip.json`.
- `node scripts/verify-month-boundaries.mjs`: **7/7 kiểm đạt**; kiểm lại byte200TXT, phân tích độc lập, 2.472 khoảng, phân loại2.464/8 và không cho phép điều hướng tám dòng khác biệt. `VERIFICATION.json` có URL/hash từng TXT và trích đúng dòng quanh các ranh khác biệt/khoảng trống2069.
- `python scripts/verify-month-boundary-release.py`: xác minh kết quả audit, nguồn và byte sản phẩm giữ nguyên.

Nguồn/QA/tài liệu ở ngoài site. Bản manifest và ZIP nguồn trước lượt kiểm giữ tại `../archives/v53-before-month-boundary-audit/`; tệp ghi nhớ bảo toàn cũng giữ hash của ba HTML và ZIP web để chứng minh chúng không bị thay đổi. Manifest/gói nguồn V53 cập nhật sau phạm vi này, không xuất bản mạng.

Phần cần nghiên cứu tiếp vẫn là nhân chứng và tham số cho các ngày lịch nhạy; không lặp toàn bộ200TXT chỉ để tăng số liệu nếu bộ lịch hoặc parser chưa đổi.
