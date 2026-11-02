# Rà soát kiến thức trong kho sách và nguồn đối chứng

**Trạng thái hiện tại ngày 26/10:** xem [LIBRARY_APPLICATION_STATUS.md](LIBRARY_APPLICATION_STATUS.md) và [ma trận mới](research/library-current/COVERAGE.md). Nội dung dưới đây là mốc kiểm kê 25/10, trước khi hoàn thành384 lời theo hào, Thập thần/tàng can và luồng vận hạn; không dùng số liệu cũ để mô tả web hiện tại.

Ngày 25/10/2026. **Chưa áp dụng hết kho sách.** Đây là kiểm kê có dấu vết tệp và thực thi, không đánh giá bằng số lượng liên kết hoặc số phiên bản. Không sửa chức năng web trong phạm vi này; nguồn và ma trận giữ ngoài `site/`.

> Cập nhật sau lượt kiểm kê này: Càn–Khôn đã có 12 hào đọc riêng và 2 lời bổ sung. Xem `YI_LINE_READING_REPORT.md`; các số liệu bên dưới giữ như mốc kiểm kê trước cải tiến đó.

## Kho hiện có thực chất gồm gì?

Đã trích và rà **40 hồ sơ `BOOKS`** từ HTML V45 được giữ nguyên, **16 hồ sơ nguồn của mô-đun** và các khối quy tắc/chính văn nhúng. Hai bộ danh mục có chồng lặp, không phải 56 cuốn sách. 40 hồ sơ chỉ có 38 URL sau khi chuẩn hóa đường dẫn ngôn ngữ: F02/X04 trùng một URL CText; F03/M05 cùng trỏ cổng Khoa học kỹ thuật chung, không định danh một bản sách.

Các nhãn cũ “Toàn văn”, “Bản scan” mô tả đường dẫn tham khảo, không chứng minh đã tải, đọc hết, hiệu khảo hay áp dụng toàn bộ. Trong lần rà này, 2 hồ sơ chính có chuỗi dấu vết dùng một phần rõ ràng (Chu Dịch và Tử Vi Toàn Thư); 6 hồ sơ có quy tắc/lời dẫn kế thừa cần củng cố xuất xứ; 2 hồ sơ được thu/kiểm bổ sung nhưng chưa dùng vào web; 30 hồ sơ chưa tìm được bằng chứng áp dụng cụ thể. Đây là phân loại chứng cứ của **hồ sơ danh mục**, không phải tỷ lệ kiến thức hoặc số sách “đã học xong”. Không mục nào được đánh dấu đã áp toàn tác phẩm.

Ma trận đủ từng mục ở [research/library-audit/COVERAGE.md](research/library-audit/COVERAGE.md); dữ liệu và tệp chứng cứ ở `COVERAGE.json`. Giữ lời ghi `verified` cũ như ghi nhận lịch sử, không nâng thành chứng thực mới.

## Chỗ thiếu tác động trực tiếp đến sản phẩm

| Nhóm | Đang dùng ở V53 | Có trong kho nhưng chưa dùng đủ |
| --- | --- | --- |
| Kinh Dịch | 64 tên/quẻ, cấu trúc sáu hào, quẻ biến; lời gợi mở biên tập. | Kho nhúng có 64 quái từ, 384 hào từ và 54 thuật ngữ. V49 đã đối chiếu 384 vị trí với 64 trang nguồn: 377 trùng chữ, 7 khác dạng. V53 hiện không dùng chính văn từng hào, mà dùng sáu lời gợi mở theo vị trí. Chưa kiểm toàn bộ nghĩa dịch. |
| Bát tự | Tứ trụ, Nhật chủ, hành chính; Thập thần của can có tính trong dữ liệu. | UI chưa đọc Thập thần/tàng can đầy đủ. Cách cục, dụng thần, nguyệt lệnh và đại vận chưa có chuỗi hiệu khảo đủ để đưa vào kết luận. Các tùy chọn giờ Mặt Trời ở bản nghiên cứu cũ cũng chưa vào luồng người dùng hiện tại. |
| Tử vi | Mệnh–Thân/Cục, 12 cung, sao và cờ; diễn giải 14 chính tinh, đọc cung đối diện. | Thuộc tính tuổi khởi đại hạn còn có trong cung nhưng chưa có luồng đọc vận hạn. Nhiều lớp nghiên cứu Phi Hóa/lưu kỳ và nội dung phối hợp sao chưa nằm trong bản đọc hiện tại. Chưa hiệu khảo toàn bộ phú hoặc bảng độ sáng theo từng ấn bản. |
| Phong thủy | Cung phi/tám hướng; gợi ý 7 khu vực, rà soát điều kiện thực tế. | Chưa áp toàn Trạch Kinh/Bát Trạch Minh Kính, chưa tính Phi tinh, không có mặt bằng đo đạc để đặt phòng. Phần nhà ở là biên tập có giới hạn, không phải bản dịch trọn sách. |
| Các nhánh khác | Chưa có công cụ riêng. | Mai Hoa, Lục Hào/Nạp Giáp, trạch nhật, Kỳ Môn, Lục Nhâm, Thái Ất; nhiều mục chỉ mới là liên kết. Không nhập chung vào cách gieo/đọc quẻ Chu Dịch. |

Đã chạy engine V53 thật để kiểm cấu trúc dữ liệu: mẫu Tử vi trả 12 cung/52 sao; Bát tự có nhãn Thập thần cho bốn can; API Kinh Dịch chỉ trả tên/chủ đề/lời gợi mở, không có hào từ. Đây là một lượt kiểm điểm tiêu thụ dữ liệu, không phải lượt so iztro mới. Hash bốn tệp thực thi và đầu vào/kết quả giữ ở `RUNTIME_PROBE.json`. Mã UI được rà cùng, nên không coi dữ liệu tính ngầm là nội dung người dùng đã nhận.

## Nguồn bổ sung được chọn và kiểm

Vì kho chưa được khai thác hết, không mở rộng hàng loạt bằng cách thêm tên sách. Đã ưu tiên nhân chứng có thể định danh để đối chiếu các khoảng trống cụ thể.

### 1. Sách Bát trạch từ Thư viện Quốc hội Nhật Bản

[八宅明鏡図解 — NDL](https://ndlsearch.ndl.go.jp/books/R100000039-I760737): hồ sơ cơ quan lưu trữ ghi 松浦琴鶴, 靖康堂, Tokyo, 1881; mã thư mục 000000423595, DOI 10.11501/760737, có phụ lục *三元九星吉方図解*. Đây là bản Nhật, không gán thành bản gốc Trung Quốc của *Bát Trạch Minh Kính*.

Tải nguyên HTML thư mục, IIIF manifest và **21/23 ảnh** từ các URL manifest công khai. Ảnh 03 và 23 trả HTTP 400 với lỗi tham số chữ ký do dịch vụ chuyển tiếp; giữ nguyên thân lỗi, không tính là JPEG hợp lệ và không can thiệp tham số truy cập. Các tệp còn lại mở được JPEG 3331×2882. Chưa có bản ảnh đủ 23 canvas.

Đã mở xem ảnh mục tiêu 11–12 ở độ phân giải gốc và đọc bốn đồ hình Càn, Khôn, Đoài, Cấn, mỗi hình tám nhãn hướng chính. Đồ hình in **Nam trên, Đông trái**, khác sơ đồ Bắc trên của web; việc ánh xạ hướng được ghi tường minh trước khi so. **32/32 nhãn khớp engine thật**. Không tính chữ trong các nhánh 24 sơn thành mẫu đã đọc.

Có một khác biệt hệ số cần giữ: hình Khôn được in với “五黄” trong hệ Cửu tinh của sách; không lấy số 5 ấy đồng nhất với số cung phi 2 của engine. Phép so ghép theo tên quái **坤**, không dùng con số để giả tạo đồng nhất giữa hai hệ. Kết quả chỉ củng cố 32 nhãn hướng đã đọc, chưa kiểm công thức cung phi theo năm/giới tính, mọi đồ hình hoặc tác dụng phong thủy.

Chứng cứ: `NDL_CHART_READINGS.json` là lớp chép tay từ ảnh; `NDL_ENGINE_COMPARISON.json` là kết quả thực thi; byte/SHA trong `new-sources/MANIFEST.json`. Trang đầu, hai trang mục tiêu và các ảnh còn lại giữ riêng ngoài web.

### 2. Hai nhân chứng Trạch Kinh có phiên bản cố định

Tải từ kho do Kanripo quản lý, gồm Readme và ba tệp của mỗi nhân chứng tại commit cố định:

- [KR3g0019, WYG](https://github.com/kanripo/KR3g0019/tree/306f7650b38ab309e648b7a64ecd3b3d8cd5884a), commit `306f7650b38ab309e648b7a64ecd3b3d8cd5884a`.
- [KR5a0294, HFL](https://github.com/kanripo/KR5a0294/tree/c4a5508d8d672dd4e62713f577f90ed64a17c3c5), commit `c4a5508d8d672dd4e62713f577f90ed64a17c3c5`.

Đây là nguồn chép có mã trang và nhãn cơ sở do người quản lý công bố, không thay thế ảnh ấn bản. Đã xác nhận ba chỗ khác nhau ở đầu quyển thượng: 隂/陰, 而/無 và 藥/樂. Giữ nguyên hai chuỗi, chưa gọi bên nào là lỗi chép khi chưa ghép ảnh. Nhãn HFL ở đầu tệp và Readme còn cần đối chiếu với trường SOURCE ghi 三家本 1988; không gọi xuất xứ Hàm Phân Lâu là đã xác minh độc lập. Chi tiết `TEXT_WITNESS_CHECK.json`.

### 3. Kiểm chất lượng các đường dẫn sách cũ

Đã tải trang [Uyên Hải Tử Bình](https://zh.wikisource.org/wiki/淵海子平) hiện hành. Trang có cảnh báo **chưa nhập đủ** và **nguồn tác phẩm chưa rõ/cần xác minh**. Không dùng các nhãn “đã đọc” kế thừa để coi đây là bản sách đầy đủ hoặc tự nâng làm căn cứ duy nhất cho luận cách cục/dụng thần. Byte HTML, thời điểm và SHA được giữ.

Đã kiểm metadata [Tam Mệnh Thông Hội quyển một — CADAL/Internet Archive](https://archive.org/details/06066037.cn): có thông tin cơ sở quét/đóng góp Zhejiang University Library, 12 quyển tách 12 tập. Lần này **chỉ lưu metadata**, chưa tải PDF/ảnh sách, chưa coi 455 ảnh theo mô tả metadata là 455 trang đã sở hữu hoặc đã đọc. Mục này có giá trị làm hướng tìm ảnh nạp âm, chưa chứng minh toàn bộ sách đã dùng.

## Kiểm chứng, phát hành và hướng làm tiếp

**20/20 kiểm tra kiểm kê/xuất xứ đạt**, thêm **32 phép so nhãn hướng** khớp. Tái kiểm hash 64 HTML Chu Dịch V48 và 17 ảnh Tử vi V52 đã có, không tải lặp. Nguồn mới giữ **36 phản hồi HTTP 200**, tổng 56.762.545 byte, và 2 thân lỗi HTTP 400 riêng. Hai text witness được ghim commit; TLS/URL/thời điểm/byte/SHA được lưu. SHA xác nhận toàn vẹn bản tải, không xác nhận một học thuyết tiên đoán.

Tái lập từ `v53`: `node scripts/probe-library-coverage.mjs`, `python scripts/check-library-witnesses.py`, `python scripts/audit-library.py`, `python scripts/verify-library-audit.py`. Bước mạng riêng `node scripts/fetch-library-sources.mjs` tái dùng bản ghi cũ và kiểm hash, không tải lại hàng loạt. Cần đọc giới hạn từng JSON thay vì cộng mọi số đếm thành “sách đã kiểm hết”.

HTML người dùng giữ nguyên SHA-256 `71fa87cc7b8cf00bb74c5820d042936b65be06af4a1d42af2b3ea632f5790553`; bản web và nội dung công cụ không đổi. Gói nguồn V53 được cập nhật bằng chế độ chỉ đóng gói nghiên cứu; snapshot trước lần kiểm kê ở `../archives/v53-before-library-audit/`. Không tạo V54, không đưa corpus/nguồn lên trang người dùng.

Thứ tự ưu tiên tiếp theo:

1. Kinh Dịch: ghép từng hào với nguồn và rà nghĩa diễn giải trước khi đưa vào kết quả; tránh sáu lời chung theo vị trí bị hiểu là hào từ riêng.
2. Bát tự: xác minh ảnh sách cho Thập thần/tàng can, trình bày dữ liệu đã tính; tách phép đếm hành với vượng suy, dụng thần và cách cục.
3. Phong thủy: mở rộng đồ hình đã ghép ảnh, xác định quy ước cung phi/năm sinh và hướng của từng đối tượng; tìm bản Trung Quốc xác định của Bát Trạch/Dương Trạch Tam Yếu. Không dùng nguồn Nhật để xóa khác biệt truyền bản.
4. Tử vi: thiết kế luồng vận hạn người dùng từ dữ liệu đã kiểm, tiếp tục ảnh Tứ Hóa/phụ tinh; không khôi phục màn hình thử engine làm sản phẩm.

Các mục thư mục rộng, trạch nhật và Tam thức chỉ mở khi có phạm vi chức năng rõ. Chưa cần đi tìm sách đại trà vì còn nhiều dữ liệu đã có chưa được khai thác đúng mức.
