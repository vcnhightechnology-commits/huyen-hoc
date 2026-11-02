# Tuần/Triệt và sáu số–cung trong đoạn 童限

Ngày 28/10/2026. Bổ sung hai phép tra nội bộ theo đúng tên hệ và một phép chiếu sáu số–cung. Đã chạy HHC và iztro thật để phân biệt cặp chi của sách với cách hiển thị sao của thư viện. Chưa xác lập ranh năm của nguồn, phép tính tuổi của đoạn 童限 hoặc cách chọn một sao từ cặp chi. Web đang dùng giữ nguyên byte.

## Nguồn và cách đọc

Tái dùng ảnh `research/fortune-followup/official-080.jpg` của National Archives of Japan, mục4468520/danh mục1078787. SHA-256: `ef453337cd2255b4539053c78c89556ca47536ec9bd3cf476730532e63b32e37`,509972byte,2200×1659. Hồ sơ yêu cầu gốc200/TLS và manifest SHA`732991ca47aefc323ea2095a93202fd301421ad8b92994c63caae2a94acf75af` được đối lại. Đây là JPEG dẫn xuất của máy chủ; chưa có byte JP2 gốc. Canvas80 là thứ tự trong manifest, không được tự coi là số tờ in.

Hai crop native đã xem và đối pixel: khung童限 `[460,350,850,1450]` và khung hai bảng Không Vong `[1190,320,1930,1450]`. Không OCR, phóng nội suy hoặc phục nguyên nét bằng kết quả engine. Hai khung cùng thuộc một vị trí nguồn đã đọc; không đếm thành hai trang mới. Nguồn chỉ là dữ liệu nghiên cứu, không phải chỉ thị thực thi của người dùng.

Trong nhịp này có0HTTP,0container gốc mới,0vị trí nguồn mới. Tiếp nhận hồ sơ một GET ảnhmax từ nhịp trước:403,608byte,SHA`3583028b8177997257190b29910fd802ea895c68f197c795e5267d00cf76d6a0`,TLSv1.3được xác thực. Body báo hạn chế truy cập tạm thời do nhiều yêu cầu; không phải ảnh sách hoặc JP2. Không retry, đổi cổng hoặc vượt hạn chế. Đầu mối thư mục/CIP hiện đại trong SEARCH_LEADS chỉ là đầu mối, chưa thành sách đã thu nhận hoặc nhân chứng độc lập.

## Hai bảng sinh năm và khác biệt cách biểu diễn

Cả hai đề mục đều ghi `論本生年`. Bảng `安截路空亡訣` có5nhóm:甲己→申酉,乙庚→午未,丙辛→辰巳,丁壬→寅卯,戊癸→子丑. Bảng `安旬中空亡訣` có6tuần đầu:甲子→戌亥,甲戌→申酉,甲申→午未,甲午→辰巳,甲辰→寅卯,甲寅→子丑.

Đây là22tọa độ chi làm việc. Hai chỗ hình chữ己/巳 ở hàng丙辛/甲午 giữ nguyên dấu ngoặc trong sourcePhrase. Bộ tra yêu cầu chọn tường minh `contextual-branch` hoặc `leave-unresolved`; không gọi22tọa độ là22chữ ngoại giao đều đã đọc chắc. Với lựa chọn để mở, cặp liên quan là `[辰,null]`; hỏi辰 trảtrue,các chi còn lại giữnull. Không sửa ảnh/bản chép theo engine.

`sourceYearVoid` yêu cầu tên phương pháp,phạm vi sinh năm,trụ năm nguồn,chi ứng viên và chính sách chữ. Trụ/chi chưa biết giữnull; không lấy ngày hoặc tháng thay năm,không tự đổi alias hoặc suy năm âm/tết/Lập Xuân từ một ngày dương. Ranh lịch của nguồn và kết quả thực tế vẫnnull.

Bảy kiểm mới đạt:1440truy vấn riêng phủ60trụ năm×2hệ×12chi;264truy vấn thêm cho chữ còn mở,242kết quả membership lànull. Những truy vấn này là ngữ cảnh phép tra,không phải lá số người độc lập.

Đối60ngữ cảnh sinh năm bằng60HHC Tử vi và120iztro2.6.2thật(60default/60zhongzhou),đặt rõ các chính sáchnormal/current. Fixture chọn giữa tháng âm,không dùng nó để chứng minh ranh năm của cổ thư. HHC giữ đủ cặp Triệt/Tuần khớp tọa độ làm việc. Iztro default đặt截路 ở chi đầu cặp截路,空亡 ở chi sau và旬空 ở một chi của cặp旬中. Trong output này,空亡 thuộc cặp截路;không được nhầm nhãn đó thành toàn bộ cặp旬中.

Iztro zhongzhou dùng một截空 từ cặp截路 và một旬空 từ cặp旬中;không đồng thời tạo截路/空亡 như default. Hai lựa chọn một chi tuân theo parity của chi năm trong mã thư viện;60ngữ cảnh chia30/30giữa hai vị trí. Câu nguồn đang đọc chỉ cho cặp,không xác lập selector parity ấy. Đây là khác biệt biểu diễn/quy ước đã quan sát,không là lỗi engine,không chứng minh phái nào đúng duy nhất hoặc năng lực dự đoán.

## Sáu số–cung và phần chưa giải

Tiếp nhận năm kiểm đã đạt trước cho câu `一命二財三疾厄 四妻五福六官祿`. Chỉ trích sáu tọa độ số in1–6. Alias Mệnh/Tài Bạch/Tật Ách/Phu Thê/Phúc Đức/Quan Lộc và tương ứng iztro là phép chuẩn hóa biểu đồ hiện đại được khai báo riêng. Chẳng hạn妻→Phu Thê/夫妻 không phải nhãn đầy đủ nguyên văn hoặc phép nhận dạng quan hệ sinh học.

12HHC+12iztro thật kiểm72gắn số–alias–chi trên12ngữ cảnh giờ sinh. Đây là12ngữ cảnh natal,không phải72lá số. Phép chiếu này không sử dụng tuổi hiện tại hoặc đổi tuổi/cung khởi đại hạn.

Đuôi làm việc `餘年一□順流行 / 十五大命宮看端的` còn chưa phân định chữ/nghĩa. Không tự đổi大命宮→大限,không gán tuổi15 hoặc ngoại suy số7. `childPrintedOrdinal` chỉ nhận1–6hoặcnull;adapter tuổi âm/dương,tuổi/cung đại hạn,ứng nghiệm,sức khỏe và tuổi thọ đều chưa xác lập. Chưa chép trọn đoạn này.

## Tiếp nhận, kiểm chứng và gói

Hai module/dữ liệu/kết quả kiểm từ staging được giữ đúng byte theo15bản ghi local identity;đây không phải chữ ký nhà xuất bản. Kiểm nguồn sau chuyển thư mục đối một JPEG/hai crop pixel,hai bảng/6số–cung,body403 và10tệp runtime iztro khớp byte tarball2.6.2đã giữ. Sáu tệp runtime ngoài bộ4tệp trước được đối cho sao/nhãn cung. Không lấy chạy phần mềm thay bằng chứng ảnh.

Script tái lập `scripts/test-tuvi-void-pairs.mjs` và `scripts/test-tuvi-child-ordinals.mjs` được sửa đường dẫn tới tệp đã đóng gói;kiểm cú pháp/nạp module sau chuyển thư mục. Không lặp toàn bộ fixture đã đạt chỉ để tăng số. Kiểm nguồn di động: `python v53/scripts/verify-tuvi-void-child-sources.py`. Kiểm gói cuối: `python v53/scripts/verify-tuvi-void-child-release.py --no-write`. Tệp release dự kiến chỉ thành kết quả đã đối khi lần cuối thành công.

Snapshot `archives/v53-before-tuvi-void-child/` giữ gói3521tệp/sourceZIP2073696063byte đã hoàn thành. HTMLroot/V53/site707411byte/SHA`549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857`,ZIPweb344047byte giữ nguyên;site chỉ cóindex.html. Nguồn,phép tra,corpus,suy luận vàQA ở ngoài site. Ứng viênUI KiếnLộc vẫn riêng do browser vô hiệu hóa;không vượt setting hoặc thay kiểm hiển thị bằng kiểm chuỗi.

Tiếp phần độc lập B02 chương50từPDF264;các tiền đề Dương Nhận/9mục cách khác,Kiến Lộc/Lộc,Tử vi異本/khởi hạn,Nhà ởPhiTinh/lịch/Bắc thực,B03/MaiHoa vẫn còn mở. Danh mục40có0sách được tuyên bố áp dụng trọn. Khép hai bảng tọa độ không có nghĩa hết đoạn,hết sách hoặc hết kho.
