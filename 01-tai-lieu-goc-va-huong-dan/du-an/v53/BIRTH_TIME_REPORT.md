# V53 — không tự điền giờ sinh chưa được cung cấp

Ngày 25/10/2026. Phạm vi này sửa độ đúng của đầu vào và hồ sơ, tiếp nối V53. Không mở phiên bản mới. Bản hoàn thành ngay trước sửa được giữ trong `archives/v53-before-explicit-birth-time/`, gồm HTML, ZIP web, ZIP nguồn và manifest; hash HTML bên trong hai ZIP đã được đối chiếu.

## Lỗi được xác nhận

Biểu mẫu Tử vi/Bát tự trước sửa tự điền **08:00**. Ngoài ra facade Bát tự nhận đầu vào thiếu giờ mà chưa bật “Chưa rõ giờ sinh” vẫn tự dùng **12:00** và trả cả trụ giờ. Hai hành vi có thể khiến kết quả được đọc như lá số dựa trên giờ sinh thực, dù người dùng chưa cung cấp giờ.

Trạng thái trước sửa được thực thi và lưu tại `qa/birth-time/before.json`, cùng SHA-256 HTML `dcc31530811166e09d5c3f313c17e46f34f78191346c2ea3ad87d6f631027ad4`. Đây là kiểm tra đầu vào phần mềm; không thêm một quy tắc an sao hoặc giả thuyết truyền bản.

## Thay đổi

- Biểu mẫu mới để trống cả giờ và phút, có HH/MM làm gợi ý. Tử vi yêu cầu nhập đủ giờ/phút; Bát tự cho lựa chọn rõ “Chưa rõ giờ sinh” để chỉ xem ba trụ.
- Engine từ chối thiếu giờ/phút trong chế độ biết giờ, cả khi được gọi qua mở hồ sơ và không đi qua `readInput()`. Không dùng số 0 làm phép kiểm có/không: **00:00 nhập thật vẫn hợp lệ**.
- Trường hợp Bát tự chưa biết giờ vẫn có thể dùng thời điểm neo nội bộ để xét các trụ và khoảng chuyển trụ; không tạo trụ giờ. Thời điểm neo không được giữ như giờ sinh trong hồ sơ người dùng, TXT hoặc tiêu đề kết quả.
- Khi mở hồ sơ cũ có `noTime: true` và giờ neo 12:00 đã lưu, bỏ giờ/phút khỏi biểu mẫu. Nếu người dùng bỏ lựa chọn chưa rõ giờ, họ phải nhập giờ thực; không vô tình biến thời điểm neo thành giờ sinh đã xác nhận.
- Hồ sơ có giờ thực được giữ nguyên, kể cả 00:00. Không tự sửa các hồ sơ cũ chỉ dựa vào việc chúng có 08:00, vì không có chứng cứ phân biệt giờ do người dùng nhập và giờ mặc định trong các bản trước.
- Giá trị `noTime` được kiểm kiểu boolean; chuỗi ký tự như `"false"` không được dùng như quyền chuyển sang chế độ chưa biết giờ.

## Thực thi và đối chiếu

`scripts/verify-birth-time.mjs` đạt **24/24** kiểm tra. Gồm 9 ca thiếu/sai giờ cho mỗi engine, 00:00, thiếu phút, gửi bằng Enter, biết/chưa biết giờ, lưu/mở hồ sơ, hồ sơ chưa biết giờ cũ có thời điểm neo, TXT, từ chối hồ sơ biết giờ bị thiếu giờ, và chặn xuất kết quả đã hết hiệu lực.

Chạy **iztro@2.6.2 thật** đang có trong kho V46: kiểm lại đủ **209 tệp cài đặt** khớp từng byte tarball npm đã lưu. SHA-512 tarball khớp metadata gốc đã lưu. Tarball SHA-256 `d44e96631c0506424c3aef25a7bba8e43e01729102d6a703720cbe224aec5403`. Không tải lại gói và không gọi phiên bản này là phiên bản mới nhất.

Đối chiếu 24 giờ dân sự × hai giới tính trên ngày 16/08/2000 UTC+8: **48 lần tạo lá số, 816/816 trường khớp** (Mệnh, Thân, cục, 14 chính tinh). Có 00:00 và 23:59. Quy ước ghi rõ `dayDivide: current`, năm normal, tháng nhuận giữ cùng tháng; không ép các quy ước khác thành kết quả giống nhau. Raw JSON từ engine thật, cấu hình và sai khác được giữ tại `qa/birth-time/iztro-hour-regression.json`.

Đây là hồi quy có mục tiêu sau sửa đầu vào; một ngày không đại diện toàn bộ lịch hoặc xác nhận khả năng tiên đoán. Các bảng đối chiếu và thông tin nguồn vẫn nằm ngoài web người dùng.

Chạy lại các bộ cần thiết sau thay đổi:

- `verify.mjs`: **50/50**; gồm 336 lá số so V52, 288 cấu hình Bát tự và 402 tổ hợp năm/cung phi.
- `verify-year-helper.mjs`: **38/38**, giữ nguyên đổi năm âm, ngoại lệ lịch, hồ sơ và thao tác Enter/Lưu.
- `final-check.mjs`: **11/11**, bản in và bố cục; 605 tệp bản V46–V52 giữ nguyên byte.
- Bộ mới **24/24**. Tổng bốn bộ vừa chạy: **123/123**.

Không lỗi JavaScript hoặc yêu cầu HTTP trong lượt thử bản HTML độc lập. Đã nhìn ảnh kết quả 00:00 trên điện thoại. Ảnh trang trí/CSS không thay đổi; bộ 35 kiểm tra ảnh cũ được giữ như hồ sơ lịch sử, không tính vào 123 phép kiểm vừa chạy.

## Phát hành

Build lại HTML độc lập, HTML thuận tiện ở gốc workspace và `site/index.html`; đóng lại hai gói V53. Gói web vẫn chỉ gồm HTML và hướng dẫn. Báo cáo, raw JSON, tarball tham chiếu và chứng cứ kiểm thử không đưa vào `site/`. Không tự xuất bản hoặc gửi dữ liệu cho người khác.
