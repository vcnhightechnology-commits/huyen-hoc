# Thực thần và mười mục phụ: khoảng đọc, điều kiện và giới hạn

Ngày 28/10/2026. Nghiên cứu nội bộ, không thêm nội dung nguồn vào site.

## Phạm vi đã xử lý

Đọc lần đầu toàn bộ khoảng bản chép số từ **論食神** tới trước **論陽刃**: 6.755 codepoint có đánh dấu trang sau khi giải mã CRLF thành LF (bản giữ nguyên byte có7.050codepoint); chia liên tục thành **90 nhóm ngữ cảnh/5.307 codepoint sạch**, chỉ bỏ PB, dấu đoạn và khoảng trắng. Mỗi chữ còn lại được gán đúng một lần. Đây là các đoạn biên tập có thể chứa nhiều mệnh đề, không phải 90 quy tắc nguyên tử đã áp dụng.

Mười một đơn vị gồm 論食神, 飛天禄馬, 倒衝禄, 天衝食禄, 福星貴人, 食神同窠, 食神帶合, 専食合禄, 紅鸞天印, 墨池涌泉, 専印合禄. Đã xem **31 vị trí container 168–198**: 168 là ranh cuối mục trước; phần hiện có của mục này là 30 vị trí 169–198. Có 27 vị trí đọc lần đầu (168 và 172–197), 4 vị trí đọc mở rộng (169–171/198). Hai mươi bảy PNG là dẫn xuất native mới từ container cũ, không phải tải 27 trang nguồn mới.

## Nguồn và khoảng đứt

Giữ nguyên CADAL06066041.djvu, **10.721.582 byte/226 ảnh**, SHA-256 `013ce4861680a2bf08b811050c45a45bb2d3ce9d164f7e2341d7070bd5cb2c1a`. Đối lại manifest HTTP200/TLS đã lưu. Bản chép KR3g0042_005.txt có SHA-256 `1ebdd92feaa57496b702f962ad6fafd4f19c17e98c38a94b40f626ef321dd997`. Ảnh và bản chép thuộc cùng dòng WYG, không tính là hai nhân chứng độc lập. Nhịp này **0 HTTP,0 container gốc,0 nhân chứng độc lập mới**.

Ảnh188 kết tờ làm việc93b; ảnh189 có số in **九十六**, mở giữa bài thơ của mục 倒衝. Bản chép còn94a/94b/95a/95b giữa hai mốc này, gồm đuôi 飛天 và đầu 倒衝. Chưa xác lập bốn tờ ấy thiếu ở mọi nơi trong container hay bị chuyển chỗ; chưa bù ảnh và không suy một độ lệch số học cố định. Các đoạn chỉ có bản số được đánh dấu rõ trong CONTEXTS/CONTINUITY_AUDIT. Không tuyên bố đã đọc đủ toàn bộ nhân chứng ảnh hoặc đối từng chữ của cả khoảng.

## Chức năng riêng đã kiểm

Module `research/bazi-food-source/special-food-reference.mjs` tách hai hệ tọa độ theo nguồn:

- **専食:** can ngày 戊/giờ 庚申; phép dò chữ 甲丙/卯寅 của câu193 giới hạn năm/tháng. Hai ngày 戊午/戊寅 được giữ như tọa độ “khó làm cách”, không tự thành kết luận loại. Tính đủ đầu vào của phép dò chỉ xét hai vị trí thực sự được dò, độc lập với việc chưa biết ngày/giờ.
- **専印:** can ngày 癸/giờ 庚申; giữ riêng tọa độ can 戊己丙 và chi 巳午寅 theo câu197, không thay hàng loạt 己/巳. Đây là dò chữ lộ có phạm vi khai báo, không xác nhận sự khắc/xung/hư hợp đã có hiệu lực.

Ví dụ ảnh194–195 in **甲戌庚午戊辰庚申**, có Giáp năm nhưng lời bình nêu Canh tháng chế. Bộ kiểm giữ hình dạng phản ví dụ và nhận tiền đề chế hiệu lực chỉ khi được khai báo; một chữ Giáp không tự đủ để kết luận hỏng cách. Văn xuôi **愛財星印綬**, thơ **要無官印**, văn **喜秋冬生** và bình **不專秋冬生** giữ song song; chưa đặt thứ tự ưu tiên hoặc cổng mùa tự động.

Những dữ kiện xác định được không bị trộn với lời dự báo. Mức lực, hợp/chế hiệu lực, ưu tiên nguyệt lệnh, thành toàn cách và kết quả đời sống đều chưa xác lập. Module giữ chúng ở null và không tham gia web người dùng.

## Các mục và dị tự còn phải khai thác

Phúc tinh nói rõ **以年論/若以日遁則非**: hai hàng 甲→丙寅/丙子,乙→丁亥/丁丑 được ghi đúng phạm vi; không dựng tám hàng còn lại rồi gọi là in trực tiếp. 同窠 có 十三位 và ví dụ 甲子→丙子; phép suy vòng60 và vai trò mọi trụ chưa mặc định. 帶合 giữ sáu bộ can; ảnh192 đọc làm việc **己人見辛**, bản số giữ **巳人見辛**, chỉ ghi khác biệt tại chỗ. 紅鸞 có bốn hàng và mục tiêu 日時; 墨池 có một ví dụ bốn trụ/sáu cặp phụ, phép AND/OR của hai mục tiêu đầu chưa được chọn.

Chương chính phân nhiều/ít Thực và điều kiện Ấn vận. Câu **食神重見變為傷官** là lời luận cách của nguồn, không đổi nhãn Thập thần cố định cho từng can chỉ vì có hai Thực. Ngoại lệ 不畏倒食 cần tiếp tục đối từng 己/巳 và điều kiện hóa khí; chuỗi ca quyết còn nhiều mệnh đề phụ. 飛天 nêu bốn ngày, bình sau chỉ hai ngày là 傷官; 倒衝 có hai/sáu ngày ở các lớp khác nhau. Không hợp nhất các lớp này thành một chuẩn không tên.

Lời về tính cách, hình thể, sức khỏe, thọ, con cái, địa vị/tài sản và các tiểu sử được lưu như mệnh đề lịch sử chưa kiểm chứng; không biến thành kết quả đã xác thực cho người dùng.

## Kiểm chứng và bảo toàn

**6 kiểm đạt.** Một lần chỉnh nhãn `sourceContainerPage` (container là DjVu) và sửa cờ đủ dữ liệu theo đúng phạm vi năm/tháng dẫn tới chạy lại 6 kiểm; giữ kết quả trước, không cộng thành12. Các bài kiểm đọc probe đã hoàn thành, không chạy lại engine để tăng số.

Probe thực thi **57 chart tìm kiếm hữu hạn lunar-typescript1.8.6**, sau đó **2 lunar forward+2 HHC Bát tự**. Hai bộ trụ in khớp với các ngày hiện đại khả dĩ 1934-06-26/16h và1957-05-01/16h, UTC+8, mốc ngày00h. Đây không phải khẳng định ngày sinh của nhân vật trong sách, niên đại lịch sử hoặc kết quả vận mệnh. Engine giữ SHA-256 `39f08bd1887faca4d35f7ad415ebf596621010d530b489212774d5cbf99040e6`.

Đã đối SHA31 ảnh, RGBA27 dẫn xuất native,8crop đã xem/khớp pixel,2 lần giải mã lại buffer189/195. Trong8crop có một crop đầu lấy nhầm đoạn Đồng窠; giữ và ghi nhận, sau đó tạo/xem crop đúng 帶合. Không tính crop nhầm là chứng cứ chữ 己. Có58 tệp tiếp nhận đồng nhất byte; module chức năng giữ nguyên byte từ staging. Hồ sơ nhập, script kiểm nguồn và kiểm gói được giữ trong nguồn phát triển.

Bảo toàn gói trước **3.856 tệp/ZIP nguồn2.100.342.805 byte** trong `archives/v53-before-bazi-food-source`. HTML độc lập707.411byte, site sạch và ZIPweb giữ nguyên; browser QA hiện không khả dụng, ứng viên Kiến Lộc tiếp tục riêng. Sau chuẩn bị manifest/ZIP, bước `verify-bazi-food-release.py --no-write` phải kiểm toàn bộ tệp trên đĩa và trong ZIP; kết quả đọc cuối là thẩm quyền xác nhận gói. Toàn kho vẫn active,40 mục danh mục/0 tác phẩm áp dụng hết.
