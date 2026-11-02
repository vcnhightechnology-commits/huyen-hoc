# V53 — xác định năm âm từ ngày sinh dương lịch

Ngày: 25/10/2026. Phạm vi tiếp nối trên V53, không mở phiên bản mới. Bản V53 đầu tiên được giữ nguyên trong `archives/v53-first-consumer/` dưới dạng HTML và hai gói ZIP; mã và kiểm thử của lần phát hành đó nằm trong gói nguồn đã lưu.

## Vấn đề và thay đổi

Trước đây Bản mệnh và Hướng nhà chỉ nhận một năm âm lịch. Người dùng có thể nhập nhầm năm dương khi sinh trước Tết dù có lời nhắc. Hai mục nay cho chọn “Năm âm lịch” hoặc “Ngày dương lịch”. Cách thứ hai yêu cầu đủ ngày, tháng, năm, chuyển lịch rồi dùng **năm âm** để tra nạp âm và cung phi.

Thông tin năm thực sự dùng được hiển thị ngay dưới biểu mẫu và trong kết quả, TXT, bản in. Ví dụ 28/01/2025 dương lịch thuộc 29/12/2024 âm lịch tại UTC+7: dùng Giáp Thìn 2024, không dùng Ất Tỵ 2025. Ngày 29/01/2025 mới dùng năm 2025.

Lịch mặc định là Việt Nam UTC+7. Người dùng có thể chọn lịch theo độ lệch UTC khác; đây là độ lệch của lịch âm áp dụng, **không phải** phép chuyển một thời điểm sinh giữa các địa phương hoặc tra IANA tự động. Không bịa giờ sinh để đổi năm, không áp Lập Xuân hoặc đổi ngày Tý của Bát tự vào công cụ này. Cùng ngày 29/01/1968, engine dùng năm 1968 tại UTC+7 nhưng năm 1967 tại UTC+8, nên tùy chọn lịch được lưu và khôi phục đầy đủ.

Hồ sơ ngày dương lưu ngày gốc, lịch áp dụng và cách nhập. `compute()` xác định lại năm trên mỗi lần chạy và mở hồ sơ, kể cả khi trường `year` trong hồ sơ đã cũ hoặc bị đổi. Hồ sơ cũ chỉ có năm vẫn mở theo cách nhập năm âm trực tiếp. Đổi ngày, cách nhập hoặc lịch làm hết hiệu lực kết quả cũ. Các giá trị của phần biểu mẫu đang ẩn được giữ trong phiên, không tự ghi vào kho lưu.

## Nguồn, byte và trường hợp chưa giải quyết

Tái dùng kho gốc đã tải và kiểm chứng ở V46; không tải lại nguồn chỉ để có thêm bản sao. Đọc lại đủ **200 TXT**, đối chiếu SHA-256 và số byte với `v46/evidence/download_manifest.json`: 200/200 khớp. Các URL, byte, SHA-256, dòng minh chứng và kết quả thử mới nằm trong `qa/year-helper/source-audit.json`, tách khỏi web phát hành.

Nguồn trực tiếp gồm [HKO 1916](https://www.hko.gov.hk/en/gts/time/calendar/text/files/T1916e.txt), [1968](https://www.hko.gov.hk/en/gts/time/calendar/text/files/T1968e.txt), [2024](https://www.hko.gov.hk/en/gts/time/calendar/text/files/T2024e.txt) và [2025](https://www.hko.gov.hk/en/gts/time/calendar/text/files/T2025e.txt); các byte đang dùng là bản lưu trước đó, không mô tả là lần tải mới.

Đối chiếu toàn bộ **73.048 dòng** trong `v46/data/hko_calendar_days.json` tại UTC+8: **73.047 năm khớp**, một ngày được từ chối suy năm tự động. SHA-256 của tệp đã trích: `a53becb30c9be9977ea6672aab83aa8e1a24ffb0f3db89b2dffd0f5ed1922805`. Năm âm trong JSON là dữ liệu **suy ra từ ngữ cảnh năm và chuyển tháng** trong TXT, không phải một cột năm âm ghi nguyên văn ở mỗi dòng gốc. Nguồn thiếu 30/12/2069 dương lịch vẫn được giữ thiếu; không nội suy để làm đủ mẫu.

Ngày **03/02/1916 tại UTC+8**: bảng công bố bắt đầu tháng Giêng năm 1916, trong khi bộ lịch đang dùng trả cuối năm 1915. Với cách nhập ngày dương, web yêu cầu người dùng đối chiếu và nhập năm âm đã xác nhận, không âm thầm chọn một năm. Đây là bảo vệ trước một sai khác đã biết, không phải giải thích mới cho sai khác lịch sử. Cách nhập năm âm trực tiếp vẫn hoạt động. Không gán kết quả HKO UTC+8 thành chứng cứ cho lịch Việt Nam UTC+7 hoặc mọi độ lệch khác.

Ngày 01/01/1900 dương lịch đổi ra năm âm 1899 nằm ngoài phạm vi tra cứu hiện tại: từ chối với thông báo cụ thể, không ép thành 1900. Đối chiếu trên không xác nhận toàn bộ ngày/tháng đều trùng nhau; nhiều khác biệt đã biết ở V46 không làm đổi năm và không thuộc phạm vi sửa này.

## Sửa lỗi lưu sau khi nhập bằng bàn phím

Kiểm thử phát hiện một lỗi ở luồng biểu mẫu cũ: bấm Enter có thể tạo kết quả khi ô nhập còn đang có tiêu điểm; khi bấm Lưu, sự kiện `change` đến muộn do ô mất tiêu điểm có thể xóa chính kết quả vừa tính dù dữ liệu không đổi. Sửa bằng cách ghi dấu trạng thái biểu mẫu tại lúc tính, chỉ xóa kết quả khi dữ liệu hoặc trạng thái gieo quẻ thực sự thay đổi. Mã lưu hồ sơ không phụ thuộc việc gửi biểu mẫu phải đến từ nhấp chuột.

Đã kiểm tra trực tiếp Enter → Lưu, gửi biểu mẫu khi ô đang có tiêu điểm → Lưu, và việc thay dữ liệu thật vẫn xóa kết quả cũ. Đây là sửa chức năng chung, không chỉ sửa cho biểu mẫu năm mới.

## Kiểm chứng và giới hạn

- `scripts/verify-year-helper.mjs`: **38/38** kiểm tra đạt; gồm byte gốc, toàn kho năm UTC+8, trước/trong Tết, đổi lịch 1968, ngoại lệ 1916, năm 1899, ngày sai, lưu/mở, cố ý sửa năm đã lưu, TXT, in và thao tác Enter.
- `scripts/verify.mjs`: chạy lại **50/50** hồi quy, giữ so với V52 thật trên 336 lá số Tử vi, 288 cấu hình Bát tự và 402 tổ hợp năm/giới tính.
- `scripts/final-check.mjs`: chạy lại **11/11**; 605 tệp bản V46–V52 vẫn nguyên byte. Tổng **99/99** kiểm tra ở ba bộ.
- Cả hai biểu mẫu mới và kết quả vừa màn hình 320/390/768/1440 px. Đã nhìn ảnh di động mới. Không lỗi JavaScript, không yêu cầu HTTP hoặc nguồn nghiên cứu xuất hiện trong giao diện thử.

Đây là tăng độ đúng của đầu vào năm âm và độ bền của luồng lưu, không xác nhận tính tiên đoán. Chưa sửa khác biệt lịch ngày 1916, chưa thay bộ lịch bằng lịch công bố và chưa mở rộng tra cứu trước năm âm 1900.

Bản HTML độc lập, `site/index.html`, HTML thuận tiện ở gốc workspace và hai gói hiện tại được build/đóng gói lại. Gói web vẫn chỉ gồm HTML và hướng dẫn, không gồm báo cáo, kho HKO hay các JSON đối chiếu.
