# V53 — đối chiếu ảnh Tử vi từ cơ quan lưu trữ và làm rõ quy ước vận hạn

Hoàn thành 26/10/2026, sau phạm vi bốn mục. Bản hoàn thành trước sửa được giữ tại `../archives/v53-four-items-completed/` với HTML, manifest và hai ZIP. Giữ V53, không xuất bản mạng.

## Kết quả trên web

Phần vận hạn nay ghi rõ **lựa chọn tháng nhuận thực sự đã dùng** và **quy ước ngày của giờ sinh 23h**. Hai thông tin đi cùng ngày xem, năm âm, múi giờ và tuổi mụ trong kết quả, TXT và bản in; mở hồ sơ cũ cũng nhận nhãn mặc định hiện có. Câu về đại hạn đổi thành “Đại hạn trên lá số này khởi tại cung Mệnh” để xác định phạm vi, tránh trình bày một cách khởi hạn như kết luận chung cho mọi truyền bản.

Không đổi số liệu lá số, công thức lịch/hạn hoặc bảng Tứ Hóa mặc định. Nguồn, ảnh sách, corpus và bảng khác biệt vẫn ngoài site. Thay đổi công khai chỉ là phần diễn giải quy ước giúp đọc và giữ kết quả đúng ngữ cảnh.

## Nguồn chính thức đã truy cập được

Đã lấy được byte HTTPS từ [hồ sơ 国立公文書館, mã 1078787](https://www.digital.archives.go.jp/file/1078787), [viewer quyển đóng thứ nhất](https://www.digital.archives.go.jp/img/4468520) và [IIIF manifest](https://www.digital.archives.go.jp/api/iiif/4468520/manifest.json). Đợt trước V52 bị 403; lần này công cụ đọc web vẫn trả 403 nhưng truy cập HTTPS thông thường trả 200. Không giải thử thách, đổi cookie để vượt chặn hoặc truy cập ảnh bị giới hạn.

Metadata cơ quan xác nhận tên 新鋟希夷陳先生紫微斗数全書, mã 子０６０－０００１, cựu tàng 紅葉山文庫, người tuyển 陳搏（宋）, bổ đính 潘希尹（明）, mô tả 刊本:明:::, hai sách đóng/bảy quyển, trạng thái 公開. Đây là xác nhận độc lập các trường thư mục; không tự chứng minh tác giả lịch sử, năm in chính xác hoặc mọi mô tả Nam Dương đường/Bảo Hòa đường của bên cung cấp khác.

Manifest có 129 canvas cho sách đóng thứ nhất. Chỉ lấy bảy ảnh thứ tự **74–80**, tất cả có `restricted:false` trong dữ liệu viewer. Lưu đúng byte JPEG do IIIF trả ở chiều rộng 2200 px, toàn khung, kèm URL/headers/TLS/SHA. Đây là ảnh dẫn xuất do máy chủ tạo từ JP2, **không gọi là đã tải JP2 nguyên bản**, không sửa hoặc phục chế chữ. Số 74–80 là thứ tự manifest, không phải số tờ in hoặc trang PDF.

`research/fortune-followup/REQUESTS.json` giữ 13 thân phản hồi: 12 HTTP 200 và một chuyển hướng 302 có thân rỗng. Không có PDF toàn sách được tải trong phạm vi này. Link tải Thư Cách được khảo sát để tìm nguồn; bộ so cuối sử dụng ảnh chính thức của cơ quan.

## Sáu đoạn đã đọc và kết quả đối chiếu

| Đoạn | Định vị ảnh | Kết quả |
|---|---|---|
| Văn Xương/Văn Khúc | 75, khung phải | Đọc được cột giải thích khởi Tuất nghịch theo giờ và khởi Thìn thuận theo giờ. Vùng đen ở cột thơ bên cạnh không được đoán phục hồi. |
| Tả Phù/Hữu Bật | 75, cuối khung phải và đầu khung trái | Khởi Thìn thuận/tháng Giêng; khởi Tuất nghịch. Chỉ xác nhận tháng thường, chưa suy rộng cách xử lý tháng nhuận. |
| Tứ Hóa | 76 khung trái, tiếp 77 khung phải | 40 mục sao có 38 mục đồng với bảng hiện dùng; hai khác biệt can Canh được giữ riêng. Nhâm Thiên Phủ Hóa Khoa có căn cứ ảnh rõ. |
| Đẩu Quân | 79, khung phải và tiếp khung trái | Từ cung Thái Tuế nghịch tới tháng sinh, rồi thuận tới giờ sinh để an mốc tháng Giêng. Cách đếm các tháng sau và chính sách tháng nhuận vẫn là quy ước triển khai riêng. |
| Đại hạn | 80, khung phải | Ảnh thực có lời khởi từ cung kề: dương nam/âm nữ hướng Phụ Mẫu, âm nam/dương nữ hướng Huynh Đệ. Chưa được xem là chứng cứ cho cách khởi tại Mệnh của engine hiện tại. |
| Tiểu hạn | 80, khung trái | Xác nhận bốn cung khởi theo nhóm chi và nam thuận/nữ nghịch, không phụ thuộc âm dương can năm. Cách đánh tuổi vẫn cần phân biệt với chính lời văn. |

Điểm Tứ Hóa cần giữ rõ: câu ảnh can Canh là **庚日武同相為首**: Thái Dương Lộc, Vũ Khúc Quyền, Thiên Đồng Khoa, Thiên Tướng Kỵ. Bản chép số/bảng hiện dùng là Thái Dương Lộc, Vũ Khúc Quyền, Thái Âm Khoa, Thiên Đồng Kỵ. Câu Nhâm **壬梁紫府武宿是** củng cố Thiên Phủ Hóa Khoa đang dùng, khác Tả Phù của iztro. Không lấy một đoạn này để kết luận toàn bộ các bảng trong chính ấn bản đều nhất quán hoặc một truyền bản đúng duy nhất.

Bản ghi đầy đủ ở `research/fortune-followup/WITNESS_AUDIT.json`. Chuỗi Hán là bản đọc làm việc có chuẩn hóa một số dạng chữ, không phải ấn bản hiệu khảo ngoại giao từng nét; hai câu then chốt Canh/Nhâm giữ riêng. Bảy ảnh tải được không đồng nghĩa đã đọc/hiệu khảo hết bảy trang hoặc 129 canvas.

## Kiểm chứng thực thi và sản phẩm

Ba bộ vừa chạy **67/67 đạt**:

- `verify-fortune-witness.mjs`: **8/8**. Kiểm byte nguồn/metadata/canvas; 144 lá số HHC thật trên 12 tháng thường và 12 giờ chi, 576 trường Văn Xương/Văn Khúc/Tả Phù/Hữu Bật đúng công thức từ đoạn ảnh; mốc tháng Giêng khớp HHC và **72 lần horoscope iztro 2.6.2 thật**; giữ đúng 38/40 và hai khác biệt Canh; engine giữ nguyên byte.
- `verify-fortune-conventions-browser.mjs`: **12/12**. Cả ba lựa chọn tháng nhuận, Tý muộn, lưu/mở, hồ sơ thiếu trường quy ước cũ, TXT/in, 320/390/1440 px và không lộ nguồn/HTTP/lỗi JavaScript.
- `verify-four-browser.mjs`: **47/47** hồi quy tích hợp bốn mục. Không thay số liệu 194/194 của phạm vi trước thành tổng số lượt mới; 47 phép kiểm này là chạy lại một bộ đã có.

Kết quả JSON/ảnh ở `qa/fortune-followup/` và `qa/four-items/`. Đã nhìn ảnh metadata ở 390 px, các dòng quy ước tự xuống dòng và đọc rõ. Các kiểm hiện tại không chứng minh năng lực tiên đoán, toàn bộ tháng nhuận theo ảnh hoặc giải quyết dứt điểm quy tắc khởi đại hạn.

Build/package cập nhật HTML gốc, HTML V53, site và hai ZIP. `site/` chỉ có `index.html`; gói web chỉ HTML và hướng dẫn. Chứng cứ/báo cáo chỉ thuộc gói nguồn. Hash cuối trong `PACKAGE_MANIFEST.json`.

## Phần còn mở

Đối chiếu bảng Tứ Hóa dạng đồ trong cùng ấn bản, các đoạn có thể không đồng nhất ở can Canh, tuổi/cung khởi đại hạn và cách áp lưu niên. Không tải lại bảy ảnh hay cùng metadata chỉ để tăng số nguồn. Các vấn đề lịch 1906/2057, giờ địa phương lịch sử và nguyên bản Bát trạch vẫn độc lập, chưa được giải quyết bởi nguồn này.
