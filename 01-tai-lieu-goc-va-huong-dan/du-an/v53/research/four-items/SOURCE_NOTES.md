# Nguồn và giới hạn của phạm vi bốn mục — 26/10/2026

Tài liệu nội bộ, không nằm trong `site/` hoặc gói web. SHA-256 xác nhận danh tính byte đã giữ, không phải chữ ký nhà xuất bản hoặc chứng minh học thuyết tiên đoán.

## Kinh Dịch

Tái dùng 64 HTML đã lưu ở V48, đối chiếu hash với `v49/data/yi_research.json`. Các revision được ghi riêng cho từng quẻ. V49 từng ghi nhận 377/384 hào cùng chữ và 7 khác dạng; lượt này không tự giải quyết bảy khác dạng ấy hoặc gọi bản chép số là ảnh cổ bản.

Đọc từng hào trong nhóm 3–18, 19–34, 35–50, 51–64; viết riêng 372 lời Việt và câu hỏi thực hành, ghép bằng số quẻ/vị trí hào. Giữ 12 lời Càn–Khôn và hai lời bổ sung Dụng Cửu/Dụng Lục đã hoàn thành trước. `YI_REVIEW.json` lưu hào nguồn, nhãn, revision, hash và lời biên tập theo từng vị trí. Bốn TSV là nguồn biên tập có thể sửa, không phải một hàm tạo sáu lời chung theo cấp vị trí.

Độ phủ 384/384 nghĩa là mỗi hào thường có lời gợi mở riêng, **không** nghĩa đã dịch sát toàn bộ hào từ, hiệu khảo toàn bộ ảnh ấn bản, thống nhất mọi cách hiểu hoặc chứng minh khả năng tiên đoán. Câu liên quan bệnh, sinh nở hoặc vai trò nam nữ cổ được chuyển thành gợi mở phù hợp hoàn cảnh, không dùng như chỉ định y khoa hay dự báo cá nhân.

## Bát tự

Nguồn ảnh mới: [thư mục sách của Thư viện Quốc gia Đài Loan](https://taiwanebook.ncl.edu.tw/zh-tw/book/NTL-9900014379), mã NTL-9900014379. Theo thư mục: 秦慎安校勘, 文明, 1926; 207 trang; bản lưu/ảnh do 國立臺灣圖書館 cung cấp. PDF lấy từ [bản scan trên Commons](https://commons.wikimedia.org/wiki/File:NTL-9900014379_淵海子平子平真詮_v.1.pdf), giữ đúng byte nhận bằng HTTPS.

Đọc trực tiếp PDF trang 54, trang in 三六, quyển một, mục 又地支藏遁歌: đủ 12 tập hợp tàng can. Bài ca có thứ tự câu khác cách sắp bản khí lên trước ở giao diện; ghi riêng hai thứ tự trong `BAZI_SOURCE_AUDIT.json`. Không lấy thứ tự câu thành tỷ lệ vượng suy. Đối chiếu thêm bảng chạy thật của lunar-typescript; 12 tập hợp và thứ tự bản khí được chọn đều khớp. Trang 40 và 55 chỉ là ảnh dò tìm, không tính thành ba đoạn sách đã xác minh. PDF trích chữ không ra nội dung Hán hữu dụng tại đây; không nói đã OCR toàn sách.

Nguồn bản chép số: [Kanripo KR3g0042](https://github.com/kanripo/KR3g0042/tree/7db72e5553de6ee4c45ed3980c6c67f8a6e451bf), 三命通會, WYG theo định danh của kho, ghim commit `7db72e5553de6ee4c45ed3980c6c67f8a6e451bf`. Giữ Readme, quyển đề yếu và đủ 12 quyển. Chỉ dùng các đoạn đã đọc: quyển năm 1a–4b về Nhật chủ/sinh khắc/âm dương và 5a về Chính Quan. Đây là bản số được ghim, chưa hiệu khảo toàn bộ với ảnh Văn Uyên Các.

Quyển hai 33a–36a, 論人元司事, có bảng phân ngày tư lệnh và các cách kể khác; ví dụ Tý có Nhâm–Quý. **Không gộp bảng phân ngày vào bảng tàng can cố định** hoặc tự cho trọng số. Quan hệ Thập thần được kiểm trên 100 cặp can có thứ tự bằng thư viện chạy thật, còn lời diễn giải tiếng Việt là biên tập, không chép các phán đoán phú quý/tai họa từ sách. Chưa xây dựng phép chọn dụng thần hoặc kết luận vượng suy.

## Nhà ở và hướng đo

Tái dùng ảnh [NDL 八宅明鏡図解](https://ndlsearch.ndl.go.jp/books/R100000039-I760737), 松浦琴鶴, 東京 : 靖康堂, 1881 theo thư mục. Lượt trước đọc Càn/Khôn/Đoài/Cấn (32 nhãn), lượt này đọc thêm Ly/Tốn/Chấn/Khảm từ ảnh 10/13/14: đủ tám đồ hình/64 nhãn. Đồ in Nam ở trên, Đông bên trái; chuyển tên hướng trước khi so với engine. Khôn được định danh bằng chữ 坤; số 五黄 in trên đồ không được đồng nhất với cung phi số 2 của chương trình.

Đây là bản Nhật chuyển biên, không phải nguyên bản Trung Quốc. Kết quả 64/64 chỉ kiểm nhãn tám hướng theo tám quái, không xác minh phép năm sinh→cung phi, ngày đổi năm Tết/Lập Xuân, 24 sơn, vị trí phòng hoặc tác dụng phong thủy. Ảnh 03 và 23 từng trả HTTP 400 vẫn giữ trạng thái lỗi, không tính là ảnh sách tải được.

Công cụ mới đọc số đo theo tám miền 45°; 0° là Bắc thật. Với Bắc từ, bắt buộc nhập độ từ thiên, Đông dương: góc thật = góc từ + từ thiên, chuẩn hóa về [0,360). Không tự lấy từ thiên bằng 0 hoặc tự tra theo vị trí thiếu dữ liệu. Góc chính xác nằm ở biên được quy ước sang miền theo chiều kim đồng hồ; khoảng bất định đóng chạm biên giữ đủ hai ứng viên. Đây là quy ước xử lý đo, không phải phát hiện từ cổ bản. Người dùng chọn rõ đang đo cửa, giường, bếp theo quy ước họ đã chọn, hoặc đối tượng khác; không tự đặt phòng theo một nhãn hướng tốt.

## Tử vi theo ngày

Tái dùng Toàn Thư bản số và iztro 2.6.2 đã lưu, không tải lại để tăng số nguồn. `FORTUNE_RULE_NOTES.json` phân biệt đoạn bản số đã đọc, công thức chỉ số, quy ước áp dụng và phần chưa hiệu khảo ảnh. Gói iztro thực thi có đủ 209 tệp khớp byte tarball cũ.

Lượt một có 72 lần gọi horoscope thật trên ngày thường, trước/sau Tết, trước đại hạn đầu và tháng nhuận. Lượt hai thêm 106 lần: 72 ca ba chính sách tháng nhuận, 24 ca Tiểu hạn đủ 12 chi/hai giới tính, 10 năm kiểm Tứ Hóa. Các chỉ số ngoài được đổi theo địa chi thực, không so nhầm thứ tự mảng cung của hai chương trình.

iztro dùng tháng nhuận đổi sau ngày 15 cho lưu nguyệt; HHC giữ lựa chọn cùng tháng/tháng kế/từ ngày 16. Khi khác chính sách, chênh lệch tháng được ghi trên từng ca trước khi so; 24 ca split16 trong lượt hai khớp trực tiếp, không hiệu chỉnh. Không gọi toàn bộ 178 lần là khớp thô tuyệt đối. Trước đại hạn đầu, iztro có thể trả đồng hạn; HHC ghi chưa vào đại hạn, không dùng đồng hạn làm đại hạn.

Tứ Hóa năm Nhâm: Toàn Thư bản số đang giữ ghi Thiên Phủ Hóa Khoa, iztro dùng Tả Phù. Giữ khác biệt này, không sửa nguồn để ép khớp. Đưa bảng theo can sinh sang can năm xem là quy ước triển khai được công bố trong tài liệu này; chưa có hiệu khảo ảnh riêng chứng minh toàn bộ cách áp lưu niên. Khởi đại hạn theo cung Mệnh/cục là quy ước hiện có, đã so runtime; một đoạn ngắn “An đại hạn” trong bản số chưa đủ tự giải quyết cách khởi tuổi/cung của mọi truyền bản.

Web trình bày cung gốc mà lớp đại hạn/năm/tháng đi qua và gợi mở theo chủ đề của cung. Chưa tổng hợp toàn bộ hệ sao vận hạn thành dự báo sự kiện, không dời sao gốc, không tính điểm năm tốt/xấu. Giữ múi giờ, năm âm, tuổi mụ, lựa chọn ngày Tý muộn và tháng nhuận của lá số. Ngày lịch nằm trong khoảng nhạy bị yêu cầu xác nhận thay vì trả kết quả chắc chắn.

## Nguồn đã tải và phần còn lại

`sources/MANIFEST.json` giữ URL, URL cuối, status, TLS, headers, byte, SHA-256 và thời gian UTC của từng thân phản hồi. `SOURCE_INTEGRITY.json` là kết quả kiểm lại. `BAZI_SOURCE_AUDIT.json` ghi hash PDF và ảnh trang đã đọc. `HOME_64_READINGS.json` ghi hash ảnh NDL. Nguồn, bộ so và ghi chép ở ngoài thư mục phát hành.

Hoàn thành bốn phạm vi không có nghĩa áp dụng hết kho sách. Còn: hiệu khảo Kinh Dịch bằng ảnh; kiểm ảnh các đoạn Tứ Hóa/Đẩu Quân/đại hạn; nguyên bản Trung Quốc và quy ước năm/cung phi; giờ địa phương lịch sử; các khoảng lịch 1906/2057. Chỉ mở lại khi có nguồn tốt hơn hoặc một lỗi cụ thể cần xử lý.
