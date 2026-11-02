# Nhà ở: phân biệt Đại/Tiểu Du Niên và các bảng theo tên nguồn

Ngày 27/10/2026. Tài liệu nội bộ; không đưa nguồn hoặc phòng kiểm định vào site người dùng. Đây là mở rộng căn cứ và bộ tham chiếu riêng; HTML/engine đang dùng không đổi. Toàn kho và bốn hướng vẫn chưa hoàn tất.

## Nguồn ảnh và phạm vi đã đọc

Container **欽定協紀辨方書卷二**, CADAL06056503 đã giữ từ trước: **3.433.014 byte**, SHA-256 `bfd3b76c55d62324919ab161c8c2ba2ecb129b3b2c59a3ab0428807e8f8278db`, 110 vị trí ảnh. Không tải lại hoặc tính là sách mới. Metadata/bìa Tứ Khố không chứng minh bản đầu hay tác giả đích thực của mọi lời được dẫn.

Đã giải mã và trực tiếp xem **103 ảnh mới** (1,9–110):95 trang nội dung,5 trang trống,3 ngoại văn/bìa/kết. Cộng với7 ảnh2–8 đã đọc và giữ báo cáo trước, đủ110 vị trí có lượt đọc đầu. 49–50 là ảnh nằm ngang trong container, mỗi ảnh vẫn chỉ một vị trí. `VOLUME_UNIT_MAP.json` định vị12 mục; các khoảng giao trang không được cộng thành số trang độc lập. **Đọc đủ vị trí ảnh không có nghĩa đã trích hết mọi mệnh đề, ô bảng hoặc áp hết quyển.**

Decoder DjVu.js0.5.4 giữ nguyên byte, SHA `10a831d62cc7ced39c30c7350a11410402d082a0f0a5b073a88d3d7ca662add3`. Node chỉ cung cấp bộ chứa ImageData và cờ hiện diện document cho nhánh giải mã đồng bộ; không trình duyệt/worker/OCR/network. Một trang hiệu chuẩn Bát tự223 cho mảng RGBA trùng từng pixel với PNG đã giải mã trong trình duyệt; không tính thêm trang nguồn. Giải mã lại58/101 khớp mảng pixel;103 PNG có SHA byte, kích thước và SHA RGBA riêng. Việc trình duyệt thử khởi chạy bị EPERM được giải quyết bằng nhánh decoder cục bộ, không nâng quyền.

## Quy tắc đã làm thành tham chiếu riêng

- `you-nian-reference.mjs` bắt buộc chọn tên hệ Đại hoặc Tiểu Du Niên và quẻ gốc/đích rõ ràng. Thiếu một quẻ giữnull. Bảy phép đổi hào có28 cặp không thứ tự/56 cặp có hướng, cộng8 tự cung cho64 quan hệ mỗi hệ.
- Ở ảnh91–106, năm phép đổi cho tên khác nhau giữa hai hệ: đổi dưới,hai hào dưới,hai hào trên,trên+dưới,cả ba. Tổng40 cặp khác tên;16 cặp không tự cung trùng literal. Tám tự cung giữ hai tên **輔弼/伏位**, chỉ cùng vai trò bản cung; không cộng thành24 literal trùng tên. Trọng số hào1/2/4 vàXOR là mã hóa hiện đại.
- Ảnh63/65/71/73/75/77/79/81 cho đủ64 ô viết tắt sao Tiểu Du Niên; chép trực tiếp và đối riêng với phép biến hào. Ảnh57–59 phân biệt 地理家從龍上起 và 選擇家從向上起: tập sao được nguồn gọi吉 khác nhau. Bộ riêng chỉ trả đánh giá theo bối cảnh được chọn tường minh, mặc địnhnull. Lớp đồ hình so sánh còn có cách đánh giá riêng; không hợp nhất thành điểm tốt/xấu phổ quát.
- `named-table-reference.mjs` giữ **hai bảng24sơn** Chính ngũ hành/洪範五行 từ ảnh10/18.48 gán hành được kiểm độc lập theo bản ghi nguồn. Ví dụ壬 là水 ở Chính nhưng火 ở Hồng phạm,辛 là金 ở Chính nhưng水 ở Hồng phạm. Không lấy một bảng thay mọi bảng.
- Cùng bộ riêng giữ12 dòng 月生氣/死氣 của **bản chữ WYG Trạch Kinh**, bắt buộc số tháng nguồn1–12 và tên nhân chứng. Không đổi từ ngày hiện đại, không mặc định ranh tháng/nhuận và không coi sinh khí tháng là sao Bát Trạch. HFL có已/巳 ở dòng cuối chưa đối ảnh, chưa được tự sửa hoặc hỗ trợ như bảng đã giải quyết.

**13 kiểm đạt**:9 kiểm Du Niên/byte và4 kiểm bảng theo tên. Thực thi **8 lời gọi `HHC_ENGINE.directions` thật** với các đầu vào truy cập8 hàng cung đã biết, đối64 nhãn với quy tắc mới đọc trên ảnh;64/64 khớp. Đây là kiểm quan hệ có điều kiện trên cung, không xác nhận năm→cung phi, ranh Tết/Lập Xuân, tọa/hướng thực tế hay vị trí phòng.128 quan hệ riêng,128 bối cảnh chính sách và48 gán hành là phép kiểm nội bộ, không phải thêm lời gọi engine. Không cần lặp các bộ hình học/cung phi trước khi chúng không đổi.

Bản nháp chép hai cặp ở ảnh102 bị kiểm trùng/mask phát hiện; xem lại trực tiếp cả hình101 và chữ102 cho **離坤/震艮**, thay bản nháp離艮/震坤. Đây là lỗi bản nháp nghiên cứu được sửa trước phát hành, không sửa sách hoặc sản phẩm. Nhật ký giữ trong `SOURCE_AUDIT.json`.

## Trạch Kinh: đã đọc gì và còn thiếu gì

Sáu tệp đã giữ gồm WYG(KR3g0019,commit306f7650b38ab309e648b7a64ecd3b3d8cd5884a) vàHFL(KR5a0294,commitc4a5508d8d672dd4e62713f577f90ed64a17c3c5), mỗi nhóm3 tệp. Đã đọc toàn bộ chữ giữ được;14 nhóm là **nhóm biên tập để phân loại**, không phải14 chương nguồn. Thêm10 cặp ngữ cảnh có mốc tờ:9 chỗ khác nghĩa/chữ và1 vấn đề chung về kiểm kê; ba đối chiếu mở đầu trước vẫn nguyên byte. Giữ literal và chỉ bỏ khoảng trắng/¶/dấu xuống dòng lời chú khi neo chuỗi; không gộp chữ dị thể.

Hai bản đều nói十干+十二支+乾艮坤巽=24 trong khi phép cộng là26. Không mượn tám can của sách khác để sửa. Câu ngày kiêng cũng khác; thiếu đồ hình, nghĩa âm/dương theo di chuyển/bảng đối ứng, ranh tháng/nhuận vàHFL/header1988 còn mở. Tên黃帝 vàlời quy tác giả trong sách là dữ liệu khảo cứu, không bằng chứng lịch sử tác quyền.

Ba response lỗi giữ nguyên:2HTTP403 từCommons và1HTTP503 từkhoWaseda, đềuTLS được xác thực. Các file `.403.txt`/`.503.txt` là thân lỗi với byte/SHA, **không là PDF/DjVu tải thành công**. Hai request403 ở nhịp staging trước, chỉ1 requestWaseda mới trong lượt nối tiếp; tổng3 thân lỗi mới đưa vào gói. Không thử lại URL bị lỗi, đổi danh tính hoặc vượt chặn.0container nguồn mới.

## Phần phải tiếp tục

Trích đủ các bảng 中針/縫針, quy tắc ứng dụng riêng, mọi ô墓龍變運/年月尅山家 và ví dụ có mùa Đông chí/五子/納音; đối từng384 nét hào của bảng八宮; điều kiện坐山/立向/龍 và nguồn dẫn. Quyển này có cả lời bình phản bác các lý giải cổ; không chuyển ví dụ y học/địa lý tượng trưng thành lời khuyên sức khỏe hay mô hình vật lý. Chưa có thuật toán Phi tinh9cung hoàn chỉnh từ các đoạn này.

Snapshot trước: `archives/v53-before-home-you-nian/`,2915 tệp/sourceZIP2018013895 byte. HTML root/V53/site707411 byte/SHA549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857 vàZIPweb344047 byte giữ nguyên; site chỉindex.html. Gói nguồn/manifest cập nhật để giữ bằng chứng và mã mới. Không công bố mạng, không tăng số phiên bản. Kết quả kiểm cuối ở `qa/home-you-nian/RELEASE_RESULTS.json`.

Lệnh kiểm: `node v53/scripts/test-home-you-nian.mjs`; `node v53/scripts/test-home-named-tables.mjs`; `node v53/scripts/redecode-home-you-nian.mjs`; `python v53/scripts/verify-home-you-nian-sources.py`. Không chạy lại script ghi đè dữ liệu lịch sử ở full-study/home.
