# Bát tự: chọn riêng can giờ Tý muộn — V53

Phạm vi hoàn thành ngày 26/10/2026. Nghiên cứu và kiểm thử giữ ngoài `site/`; không xuất bản lên mạng. Bản trước được giữ tại `../archives/v53-before-late-zi-witness/`.

## Kết quả trên web

Ở **Bát tự → Tùy chọn ngày giờ**, khi nhập giờ **23:00–23:59**, đã biết giờ và chọn đổi ngày lúc **00:00**, người dùng có thêm **Can giờ Tý muộn**:

- **Theo ngày đang đọc:** giữ kết quả của các bản trước, cũng là mặc định khi mở hồ sơ cũ không có trường mới.
- **Theo ngày kế tiếp:** giữ ngày trụ và Nhật chủ hiện tại, tính riêng can giờ bằng can ngày kế. Ví dụ 09/08/2018 23:30 UTC+8: cùng ngày Quý Dậu, lựa chọn cũ là giờ Nhâm Tý, lựa chọn mới là Giáp Tý.

Nếu đã chọn đổi ngày từ 23:00, cả ngày và can giờ đã theo ngày kế; lựa chọn riêng được ẩn để tránh hiểu là tiến ngày hai lần. Ngoài giờ 23 hoặc chưa rõ giờ sinh, lựa chọn cũng được ẩn và không dựng trụ giờ. Kết quả ghi đúng cách tính đang dùng; TXT/in giữ thông tin đó. Thập thần và vị trí can lộ được tính lại theo can giờ thực, đại vận tiếp tục dùng ngày/tiết đã xác định.

Đây là hai quy ước được tách rõ, không có nhãn “chính xác hơn” hay tự đổi hồ sơ đã lưu. `lateZiHour` nhận `day` hoặc `next`, mặc định `day`; giá trị khác bị từ chối. Chỉ nhánh can giờ Bát tự và biểu mẫu/nhãn kết quả thay đổi. Các mô-đun Thập thần, đại vận, nội dung, Kinh Dịch, vận hạn và nhà ở giữ nguyên byte. Đoạn bộ tính lịch/an sao Tử vi trong `engine.js` giữ nguyên byte.

## Nhân chứng ảnh đã đọc

Tìm được **新命理探原** của **袁樹珊**, [danh mục NCL-000002203](https://taiwanebook.ncl.edu.tw/zh-tw/book/NCL-000002203), ghi Hồng Kông, Nhuận Đức, năm 1915, 487 trang. PDF được tải từ **Wikimedia Commons**, được kho này quy nguồn ảnh về NCL; không mô tả là một lần tải PDF trực tiếp từ cơ quan.

PDF thực có **486 trang**, **58.287.949 byte**, SHA-256 `3dfee4ef4636d48c2d2e749f90408a825e0eacee99b8c73b9748a03deb73dcfd`; SHA-1 `2543dd33a32be978bd09e96557cdc3a57c0309a4` khớp API Commons. Bốn thân phản hồi HTTPS (API, trang mô tả cố định revision, danh mục cơ quan, PDF) đều lưu byte/hash/TLS. Chênh 487/486 được giữ, chưa suy ra trang bị thiếu hoặc toàn cuốn đã đủ.

Đã xem bìa, trang tên, lời tựa và colophon: tên/soạn giả/Nhuận Đức Hồng Kông khớp danh mục, lời tựa có **Dân quốc 4/Ất Mão**, phù hợp lời tựa 1915. Colophon chưa đọc được năm in; **không gọi bản vật lý này là bản in đầu 1915 đã xác minh**. JPEG/JP2 trang thực là 1017×1470 hoặc 1471 px, khác kích thước preview 762×1104 trên Commons. Lớp JP2 lặp lại trong PDF được định danh riêng, không tính là trang sách thứ hai.

Ba đơn vị đọc nội dung trên tám trang:

| Trang PDF / trang in | Đoạn thực đã đọc | Giá trị cho phạm vi này |
|---|---|---|
| 78–79 / 36–37 | 推時法, đủ năm nhóm can ngày khởi giờ | Đối quy tắc khởi giờ thông thường; không coi bảng bên cạnh đã đối hết mọi ô. |
| 86–88 / 44–46 | 推夜子時大運交脫法, chỉ dẫn giữ can chi ngày hiện tại nhưng giờ tính theo ngày kế; hai ví dụ Tý muộn/Tý sớm | Tý muộn có ngày Tân Dậu, giờ Canh Tý; sáng kế là ngày Nhâm Tuất, cùng giờ Canh Tý. Không nhập tuổi/mốc đại vận từ các trang này vào app. |
| 308–310 / 266–268 | 論時刻及夜子時與子時正不同; chú trực tiếp dùng can Nhâm để khởi Canh Tý khi ngày trụ vẫn Tân Dậu | Bằng chứng trực tiếp cho lựa chọn mới; vượt mức suy từ hai đoạn chung của WYG trước đây. |

Số trang điều hướng/ảnh đã lấy là 59, **không phải 59 trang hiệu khảo hoặc đọc hết 486 trang**. Tệp JP2 gốc trích từ PDF được giữ; hai PNG để xem có pixel khớp. Không dùng OCR. Đây là cách giải thích của một tác giả trong nhân chứng đã định danh, có dẫn tác phẩm cũ; không suy thành tất cả truyền bản Minh/Thanh đều dùng cùng ngoại lệ hoặc một phả hệ văn bản độc lập đã được chứng minh. WYG vẫn chưa được đối ảnh chỉ vì đã đọc sách này.

Ghi chép chính xác, ảnh và dữ liệu: `research/bazi-late-zi-witness/MANUAL_READINGS.json`, `REQUESTS.json`, `EXTRACTED_PAGES.json`, `evidence/`. Phần nghiên cứu trước ở `research/bazi-late-zi/REPORT.md` là mốc trước cải tiến; sai khác mặc định ở đó tiếp tục được giữ, lựa chọn mới cho phép đối chiếu cùng quy ước.

## Kiểm chứng đã hoàn thành

**97/97 kiểm trong bốn bộ đạt**: 9 nguồn, 12 engine, 26 giao diện và 50 hồi quy lõi. Kiểm văn bản PDF và xem ảnh là chứng cứ bổ sung, không cộng vào 97.

- Chạy thật lunar-typescript **1.8.6**, kiểm lại định danh byte runtime đã lưu. Lựa chọn mới khớp đủ bốn trụ ở **7.936 phép so mới**, bao gồm đủ 60 phút giờ Tý muộn trên 62 ngày và hai quy tắc ngày; cùng mẫu đã công khai ở nghiên cứu trước vì chính nhánh tính giờ đó vừa thay đổi.
- So với engine trong snapshot hiện hành: **7.936 lá số mặc định cũ giữ mọi trường tính toán**, ngoại trừ trường đầu vào mới có giá trị mặc định. 3.720 ca thực chịu ảnh hưởng giữ nguyên Nhật chủ và vị trí can giờ/nhãn Thập thần khớp API thật. Không giấu các khác biệt của mặc định để gọi mọi cách tính đều giống thư viện.
- Hai bộ trụ in trên ảnh sách khớp engine mới. Ngày dương 04/02/1914 và 05/02/1914 là **đổi từ ngày âm bằng thư viện**, không phải ngày dương in trên sách hoặc một ngày sinh lịch sử đã được xác nhận. Phút 30 là điểm đại diện bên trong khoảng giờ in, không phải phút sách ghi.
- Kiểm tùy chọn không tác động ngoài giờ 23 hoặc khi ngày đổi từ 23; kiểm thêm tính nhất quán ở UTC+7/UTC+8/UTC+5:30, không gọi là đối chứng lịch độc lập ở ba múi giờ. Ngày chưa rõ giờ không sinh trụ giờ, khoảng khởi/chuyển vận và rào trụ bất định giữ nguyên. Đổi can giờ riêng không đổi hướng, mốc khởi và mười đại vận trong ca đối chiếu.
- Hồ sơ cũ không có trường mới mở lại đúng kết quả cũ; hồ sơ mới khôi phục lựa chọn và tính lại từ đầu vào. Chọn quy tắc khác xóa ngay kết quả cũ; không để tải nhầm. TXT có đủ cách tính, tên ngày/giờ, vị trí và lời đọc thu gọn. Điều khiển có tên truy cập và dùng được bằng bàn phím.
- Không tràn ngang ở 320/390/768/1440 px, không có lỗi JavaScript hoặc yêu cầu HTTP trong HTML độc lập. Hồi quy 50 kiểm bao gồm đủ năm công cụ, lưu/mở/xuất và các miền ngày đang hỗ trợ.
- PDF kết quả **bảy trang** đã render và xem đủ: cách tính can giờ xuất hiện ở đầu, các quan hệ giữ đủ vị trí, form/ảnh đầu trang/nút thao tác được ẩn, không cắt chữ; tiêu đề nguyệt lệnh đi cùng nội dung. Nguồn sách và nhãn nghiên cứu không vào kết quả.

Script hiện hành: `scripts/verify-bazi-late-zi-witness.py`, `verify-bazi-late-zi-option.mjs`, `verify-bazi-late-zi-option-browser.mjs`, `verify-bazi-late-zi-print.py`; hồi quy `scripts/verify.mjs`. Kết quả ở `qa/bazi-late-zi-option/` và `qa/test-results.json`. Các script kiểm hash của mốc cũ áp dụng cho gói lịch sử tương ứng, không dùng chúng để phủ nhận một thay đổi engine có chủ đích ở phạm vi này.

## Trạng thái phát hành và việc tiếp theo

Build V53 được nhúng thành HTML độc lập, đồng bộ bản gốc/`v53`/`site`/hai ZIP, kiểm toàn bộ hash manifest và nội dung ZIP bằng `verify-bazi-late-zi-option-release.py`. `site/` chỉ có `index.html`; ZIP web chỉ có HTML và hướng dẫn. Nguồn và báo cáo nằm trong gói nguồn riêng. Snapshot trước phạm vi giữ cả hai gói đã hoàn thành.

Phạm vi **lựa chọn can giờ Tý muộn đã hoàn thành**, chưa hoàn thành toàn bộ bốn hướng nghiên cứu. Tiếp tục ma trận điều kiện cách cục Bát tự có ảnh/phản ví dụ; không lặp lại 62 ngày chỉ để tăng lượt kiểm. Niên đại in cụ thể và chênh số trang của nhân chứng này còn cần thư mục/đề ký tốt hơn, không dùng chúng để trì hoãn lựa chọn có căn cứ đã được tách rõ. Các dị bản Tử vi, ranh năm/Phi tinh nhà ở và hiệu khảo Kinh Dịch còn giữ trạng thái riêng.
