# Đối ảnh điều kiện cách cục Bát tự — V53

Hoàn thành phạm vi nghiên cứu ngày 26/10/2026. Giữ cùng V53. Snapshot trước phạm vi: `../archives/v53-before-pattern-extension/`. Đây là mốc nghiên cứu và phát triển công cụ đọc nguồn; HTML, site và ZIP web giữ nguyên byte so với bản đọc tàng can tháng đã kiểm.

## Kết quả và ảnh hưởng đến sản phẩm

Đọc có mục tiêu thêm **28 mệnh đề trong tám mục** của cùng quyển 5: Chính Tài, Thiên Tài, Ấn thụ, Đảo Thực, Thương Quan, Thực Thần, Dương Nhận và Kiến Lộc. Cộng mười mệnh đề của lượt trước, cả **mười đề mục trong ma trận đều có căn cứ ảnh cho một phần**, tổng 38 mệnh đề. **Không phải đã hiệu khảo hết mười chương hoặc toàn quyển.**

Điểm quan trọng là giữ điều kiện và phản ví dụ trước khi lập bộ nhận diện. Tài có điều kiện về thân/trợ lực, thứ tự và vị trí; Ấn thụ không chỉ riêng Chính Ấn; Thương Quan có nhánh dùng Tài hoặc Ấn phụ thuộc điều kiện chưa được định lượng. Thực Thần có yêu cầu đi kèm, không tự thành cấu trúc sinh Tài/chế Sát chỉ vì hai nhãn xuất hiện.

Trang tệp 138 nay đọc được từ container cũ: câu **không có Thực thì chỉ luận Thiên Ấn** có căn cứ ảnh. Phản hồi HTTP429 cũ vẫn giữ nguyên và không được gọi là một lần tải ảnh thành công. Chương Dương Nhận giới hạn năm dương can trong đoạn mở đầu, phân ba tên theo ngữ cảnh và có ví dụ hai trụ 甲申/丁卯 được xét khác với cách suy từ một cặp đơn lẻ. Kiến Lộc định nghĩa theo can ngày/chi tháng lâm quan, nêu trực tiếp hai cặp Giáp–Dần, Ất–Mão, rồi yêu cầu xét các trụ khác. Không có bảng mười cặp trực tiếp trong đoạn này.

Vì vậy không thêm nhãn cách cục, điểm vượng suy hoặc dụng thần chưa đủ quy tắc. Các diễn giải và vị trí hiện có trên web vẫn phù hợp với phần nguồn vừa đọc. Công cụ giải mã ngoại tuyến và bộ fixture mới giúp nối tiếp nghiên cứu mà không phụ thuộc việc tải ảnh từng trang. Nguồn, mã công cụ và QA nằm ngoài site; không thêm thư viện DjVu vào web người dùng.

## Nguồn và cách tái lập

Tái dùng [三命通會·卷五 — CADAL06066041 trên Commons](https://commons.wikimedia.org/wiki/File:CADAL06066041_%E4%B8%89%E5%91%BD%E9%80%9A%E6%9C%83%C2%B7%E5%8D%B7%E4%BA%94.djvu): **10.721.582 byte**, SHA-256 `013ce4861680a2bf08b811050c45a45bb2d3ce9d164f7e2341d7070bd5cb2c1a`. Commons quy nguồn CADAL/Đại học Chiết Giang; ảnh tiêu đề xác nhận tên quyển. Chưa xác minh danh mục cơ quan gốc, năm in hoặc phả hệ độc lập. Tệp này và bản chép Kanripo WYG không tự thành hai dòng truyền bản độc lập.

Hai thân phản hồi HTTPS mới chỉ dành cho **công cụ**: [trang tải chính thức DjVu.js](https://djvu.js.org/downloads) và bundle được trang ấy dẫn. Trang ghi thư viện 0.5.4; bundle **556.634 byte**, SHA-256 `10a831d62cc7ced39c30c7350a11410402d082a0f0a5b073a88d3d7ca662add3`. Cả hai HTTP200/TLS hợp lệ, giữ URL/byte/hash tại `research/bazi-pattern-extension/tooling/REQUESTS.json`. Đây không phải sách hay nhân chứng văn bản mới. Không tải lại container, không gọi lại API trang138 hoặc chuyển địa chỉ để thử vượt giới hạn.

`render-pattern-djvu-local.mjs` chạy DjVu.Document/getPage/getImageData thực bằng bundle đã ghim hash, rồi lưu PNG qua Canvas. Số trang giải mã thực: **226**. Đã lưu và xem **31 PNG**: 29 trang ngữ cảnh mới, hai trang 2/12 hiệu chuẩn với phần đã biết. Ảnh gốc giải mã rộng 2.289–3.105 px; từng chiều cao, byte và SHA tại `LOCAL_RENDERS.json`. Các PNG là **ảnh phái sinh cục bộ**, không phải thân HTTP ảnh gốc mới hoặc một bản scan khác. Không OCR hay trích text-layer. Quá trình giải mã không phát sinh HTTP; script cũng chặn các route HTTP(S).

Giải mã lại độc lập bốn trang **2,138,198,218**, từ cùng byte đầu vào/decoder, thu được đúng SHA PNG đã lưu; kết quả thực ở `qa/bazi-pattern-extension/DECODER_RESULTS.json`. Đây là kiểm tái lập công cụ trong môi trường hiện tại, không phải xác nhận bằng bộ giải mã độc lập thứ hai.

Số trang tệp và số tờ in được ghi riêng. Ví dụ 138→68b, **198→100b**, **218→110b**, 225→114a; không dùng một công thức đổi số cho toàn quyển. Chỉ các vị trí có anchor đã đọc được xác nhận, chưa chẩn đoán nguyên nhân khoảng lệch hoặc độ đủ của toàn container.

| Mục | Trang tệp giải mã / tờ đối chiếu | Mệnh đề mới |
|---|---|---:|
| Chính Tài | 83–85 / 41a–42a | 4 |
| Thiên Tài | 99–100 / 49a–49b | 3 |
| Ấn thụ | 114–115 / 56b–57a | 4 |
| Đảo Thực | 138 / 68b | 1 |
| Thương Quan | 154–156 / 76b–77b | 5 |
| Thực Thần | 169–171 / 84a–85a | 3 |
| Dương Nhận | 198–204 / 100b–103b | 3 |
| Kiến Lộc | 218–225 / 110b–114a | 5 |

`MANUAL_READINGS.json` giữ từng đoạn chép bằng mắt, ngữ cảnh, anchor và giới hạn. So từng chuỗi liên tiếp tại đúng mã tờ của Kanripo WYG đã lưu, SHA-256 `1ebdd92feaa57496b702f962ad6fafd4f19c17e98c38a94b40f626ef321dd997`; bỏ khoảng trắng/ký hiệu xuống dòng. Các dạng 看/㸔, 專/専, 點/㸃, 健/徤, 護/䕶 được ghi riêng từng chỗ. Hai ví dụ Tài trên ảnh đọc can 己 trong khi bản số có 巳; giữ cả hai, không thay hàng loạt. Phép khớp bản chép không thay cho việc đọc ảnh hay xác minh truyền phái.

## Engine thật, phản ví dụ và kiểm thử

**20/20 kiểm tự động đạt**, kết quả `qa/bazi-pattern-extension/RESULTS.json`. Kiểm byte/SHA đầu vào, hai phản hồi công cụ, 31 PNG/chiều thật, 28 đoạn đúng tờ và liên tiếp, các anchor, lịch sử HTTP429 và byte sản phẩm. Không chạy lại UI/PDF khi HTML và mã sản phẩm không đổi; kết quả trình duyệt của bản tàng can tháng vẫn giữ lịch sử riêng.

Thực thi **lunar-typescript1.8.6** sau khi kiểm lại audit byte runtime, không giả lập. **367 lá số**: 366 ngày năm2020 lúc08:30 UTC+8 và một ca05:30. Bốn trụ HHC khớp thư viện trong toàn mẫu. Tám cặp can ghi trực tiếp ở các mục Tài/Thương/Thực khớp quan hệ thư viện và có fixture thực với đúng vị trí can; hai cặp ngày/tháng Kiến Lộc có fixture riêng. Phép so này xác minh cấu trúc tính toán trong mẫu, không xác minh lời phán số mệnh, mọi giờ/múi giờ hoặc một phương pháp vượng suy.

- 09/08/2020 08:30 UTC+8: can tháng Giáp là Tỷ Kiên của ngày Giáp, nhưng tháng Thân không phải cặp Giáp–Dần trong định nghĩa. Không biến mọi Tỷ Kiên thành Kiến Lộc.
- 03/01/2020 08:30 UTC+8: có Thiên Ấn nhưng không có Thực Thần trong toàn bộ can lộ/tàng đã biết theo bảng đang dùng. Giữ tên Thiên Ấn, không tự gán tổ hợp đoạt Thực.
- 02/01/2020 08:30 UTC+8: hai nhãn cùng có mặt. Đây là ca kiểm đối chứng, chưa đánh giá lực/chế/hợp hoặc thành cách.
- 11/02/2020 05:30 UTC+8: ngày 甲申, giờ 丁卯 khớp **hai trụ** của ví dụ trang204. HHC vẫn giữ Ất tàng trong Mão là Kiếp Tài, dù đoạn nguồn có cách xét Nhận riêng. Đây là một ngày hiện đại tái dựng hai trường; không xác nhận ngày sinh lịch sử hoặc toàn cách cục. Bản nháp test từng gõ nhầm ngày8; đã sửa lấy ngày11 từ fixture tìm được và kiểm thư viện, không có lỗi engine sản phẩm.

Hai mươi kiểm là các nhóm xác nhận nêu trên; không gọi 367 lá số là 367 kiểm độc lập hoặc khớp engine là bằng chứng tiên đoán. Bốn PNG tái lập được ghi riêng, không cộng lại thành số kiểm tính năng mới.

## Phát hành và phần còn mở

Giữ nguyên root HTML, `v53/Huyen_Hoc_Cac.html`, `site/index.html` **667.112 byte**, SHA-256 `bfc9e9975fd96fda944f5f952b58c33967d228956f1f065623e0008b152e3e37`. ZIP web và README người dùng nguyên byte. Cập nhật tài liệu, ma trận, công cụ, QA, manifest và ZIP nguồn; toàn bộ snapshot trước phạm vi giữ riêng. `verify-pattern-extension-release.py` kiểm gói sau đóng và chế độ `--no-write` xác nhận lần cuối. Không xuất bản.

Tiếp theo cần đọc trọn các điều kiện quanh từng cấu trúc, lập bảng quy tắc theo đúng một truyền bản với ví dụ thuận/nghịch, và định nghĩa được phép xét thân/mùa/chế/hợp trước khi lập thuật toán cách cục hay dụng thần. Chương có tiêu đề không đồng nghĩa đã trích hết kiến thức. Bốn hướng nghiên cứu vẫn **active-not-complete**; ma trận nguồn hiện có chưa bao trùm toàn kho sách.
