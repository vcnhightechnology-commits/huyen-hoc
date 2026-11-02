# Phúc nguyên và Đại du niên trong bản ảnh Dương trạch thập thư

Ngày 28/10/2026. Phạm vi P08, nối tiếp `HOME_YANGZHAI_SHISHU_REPORT.md`. Đây là hồ sơ nội bộ; không thêm nguồn hoặc phòng kiểm định vào site.

## Phần đã đọc và nguồn byte

Đã xem 48 ảnh JPEG gốc trích trực tiếp từ luồng DCT của PDF, tại vị trí 34–81. Trong đó 34–80 là 47 vị trí đọc lần đầu; 81 là vị trí ranh đã đọc trước, lần này xem lại bản raw. `論福元第二` khép ở 57; `論大遊年第三` mở ở 58 và kết ở đầu 81, trước `穿宮九星`.

PDF vẫn là tệp 151.275.796 byte, 195 vị trí, SHA-256 `b6394102a995bb66df173452b37614b29d58e34ff85e08c43077006572ac48a5`. Nó được máy chủ Commons cung cấp và có thông tin dẫn về Thiên Nhất Các, cùng dấu xử lý Shuge/PDFPatcher; chưa có cơ sở gọi đây là byte tải trực tiếp từ cơ quan lưu trữ. Hồ sơ tải và bốn thân HTTP/TLS ở phạm vi trước được giữ nguyên. Phạm vi này có **0 HTTP mới, 0 container mới, 0 nhân chứng văn bản độc lập mới**.

48 tệp JPEG khớp từng byte với luồng DCT trong PDF; không dùng bộ mã hóa `page.images`. 12 crop PNG không nội suy đã được xem và kiểm bằng pixel với vùng nguồn. Vị trí 81 cũng có một bản raw trong phạm vi trước; không đếm thành trang hoặc nhân chứng mới.

Tổng hiện có 87 vị trí khác nhau đã được đọc đầu, gồm 40 vị trí trước và 47 mới. Bốn trong mười đề mục chính đã đủ khoảng đọc đầu. **108 vị trí còn chưa đọc; không có đề mục hoặc tác phẩm nào được nhận là đã áp dụng hết mọi mệnh đề.** 40 ảnh dẫn xuất pypdf trước đây vẫn được ghi đúng là dẫn xuất; việc xem 48 raw ở lần này không biến tất cả 40 ảnh trước thành raw đã xem lại.

## Dữ liệu đã chép riêng trước khi hỏi engine

`MANUAL_FUYUAN_TABLE.json` chứa 180 hàng năm Can Chi, 360 ô nam/nữ từ bốn vị trí 38–41, cùng 40 chú trung ký đọc trực tiếp. Các hàng được nhập từ ảnh trước khi tính công thức hoặc chạy engine. Script ghi dữ liệu chỉ gắn chỉ số và lưu JSON; không sinh giá trị cung bằng công thức.

Chữ có dạng 良/異 trong tên cung được giữ ở ô làm việc rồi chuẩn hóa cục bộ thành 艮/巽. Đây là bản đọc phục vụ đối chiếu, chưa phải bản chép ngoại giao mọi nét chữ. 兌 và các nhãn Can Chi được đọc theo dạng chữ chuẩn. Không thay chữ trong PDF.

Bảng và lời tóm tắt 41 cho điểm khởi nam **1/4/7**, nữ **5/2/8**, lần lượt trên/giữa/dưới. Nam nghịch, nữ thuận; gặp số giữa5 thì nam ký Khôn2, nữ ký Cấn8. Một ghi chú nháp trước đó đã đọc nhầm điểm tay 巳/兌 thành số cung6/8. `READING_CORRECTION_AUDIT.json` giữ lỗi và cách sửa bằng ảnh36/41. Ghi chú sai chưa được dùng trong engine hoặc web.

Tám khẩu quyết ở 58 được chép vào `MANUAL_YOUNIAN_SEQUENCES.json`. Chuyển bảy ký hiệu mỗi khẩu quyết sang các phương theo thứ tự đã khai báo tạo **64 tọa độ dẫn xuất**; không gọi chúng là 64 ô đồ hình đã nhập độc lập. Các đồ 60–65 cho phép nhận diện ngữ cảnh gốc cửa và thứ tự phương; chưa đối hết mọi chữ nhỏ trong 12 đồ này. Thiên Ất trong nguồn được đối tên với Thiên Y của runtime bằng alias có khai báo; 絕/絶 là chuẩn hóa chữ khi so với tham chiếu khác.

## Chức năng nội bộ và kết quả thực thi

`fuyuan-younian-reference.mjs` có hai API theo đúng tên hệ nguồn:

- `sourceFuyuan`: nhận nguyên, số thứ tự năm1–60 và nhóm đếm nam/nữ đã khai báo. Trả số cung trước trung ký, số sau trung ký và quái. Không nhận ngày sinh hoặc tự chọn ranh năm.
- `sourceYouNian`: nhận gốc đã biết và ngữ cảnh `birth-fuyuan` hoặc `declared-source-gate`. Ngữ cảnh chưa rõ trả `null`. Trả tên sao, hành sao/cung và quan hệ có chiều; không tự chọn gốc theo tọa/hướng nhà, hình học, độ cao hoặc dự đoán kết quả.

**8 kiểm hoàn chỉnh đạt.** Công thức độc lập khớp 360 ô nguồn và 40 chú trung ký. Kiểm thứ tự phương khớp tám khẩu quyết; kiểm đầu vào ngăn thay gốc cửa bằng hướng nhà, dùng năm dương thay số thứ tự năm, hoặc ngầm nhận trường thiếu.

Lần chạy cuối tạo **180 đối tượng `LunarYear` thực của lunar-typescript1.8.6**, đọc 360 trường nguyên/Can Chi cho các số năm 1900–2079, rồi thực thi **360 lời gọi `HHC_ENGINE.directions`** trên hai nhóm giới. Các trường năm của thư viện chọn đủ 180 tọa độ nguồn; 360 số cung HHC khớp bảng. Tám nhãn trong mỗi kết quả cũng được đối với 64 tọa độ đã khai triển, thành 2.880 phép so nhãn lặp trong các ngữ cảnh năm. Đây không phải 2.880 quy tắc hoặc nhân chứng độc lập.

64 quan hệ sau alias cũng khớp tham chiếu Đại du niên của Hiệp Kỷ ở phạm vi trước. Đó là so hai hồ sơ tác phẩm; chưa chứng minh các truyền bản độc lập về lịch sử hoặc đã xác nhận mọi cách ứng dụng.

SHA-256 engine HHC giữ nguyên `39f08bd1887faca4d35f7ad415ebf596621010d530b489212774d5cbf99040e6`. SHA runtime lunar thực thi nằm trong `REFERENCE_RESULTS.json`.

`TEST_FAILURE_AUDIT.json` ghi một lỗi đường dẫn import Windows trong phép kiểm tham chiếu khác, sau khi sáu kiểm và 360 HHC/180 LunarYear đã chạy qua. Script lỗi được giữ; sửa bằng `pathToFileURL`, không đổi logic nguồn. Lần chạy lại có thêm 360 HHC và 180 LunarYear trùng ngữ cảnh: **tổng lịch sử là 720 HHC, 360 LunarYear/720 trường năm**, trong đó bộ fixture được lưu thuộc lần đạt cuối 360/180. Không cộng hai lượt thành bằng chứng độc lập hoặc 16 kiểm hoàn chỉnh.

## Các lớp nghĩa chưa được gộp

Nguồn 34–37 phân 福元 theo năm sinh với cung/tọa/hướng của nhà, và không dùng năm sinh cha thay cho mọi con, anh em. Các viện có tường/cửa ngăn và nghi môn cần giữ phạm vi riêng. 46–56 là các sơ đồ tình thế có cửa, đường và cao thấp; chưa thành bộ nối mặt bằng đo được.

58 và66 nêu sao tốt còn phải đắc địa, cao thấp và sinh khắc của cung. 74–80 phân rõ sao ở trên/cung ở dưới, và các sao cùng hành vẫn có lời ứng khác: ví dụ 武曲/破軍 cùng Kim, 巨門/祿存 cùng Thổ. Vì thế quan hệ sinh–khắc trừu tượng chỉ được trả như tọa độ có chiều, không dùng để rút ra bệnh, tuổi thọ, tử vong, tài sản hoặc kết quả gia đình. Phần vè 67–73 và các lời ứng 74–81 đã đọc đầu nhưng chưa trích hết mệnh đề hoặc xác minh hiệu quả.

Đầu bảng 40 in `萬曆五十二年以後為下元`. Giữ nguyên niên khoản bất thường này; chưa có xác minh lịch sử độc lập và không tự sửa tên niên hiệu. Phép so phần mềm theo trường năm không chứng minh phép đổi niên khoản này sang lịch Gregorian. Đoạn nguồn cũng chưa xác lập ranh Tết/Lập Xuân; không dùng kết quả để đóng bộ nối ngày sinh.

## Phát hành và phần nối tiếp

HTML gốc, bản độc lập V53, site sạch và ZIP web giữ nguyên byte. Bản snapshot trước phạm vi ở `archives/v53-before-home-yangzhai-fuyuan/`, gồm gói nguồn đã kiểm 4.074 tệp/2.340.565.337 byte và các hash. Module và dữ liệu nghiên cứu được tiếp nhận đúng byte; kiểm toàn gói cuối sẽ ghi ở `qa/home-yangzhai-fuyuan/RELEASE_RESULTS.json`.

Tiếp các mục chưa đủ khoảng đọc: ngoại hình13–33, Huyền Không trang quái94–100, mở/sửa cửa100–105, phóng thủy105–111, tuyển trạch124–168, phù trấn168–195. Tên 玄空 trong sách chưa đủ để gọi là thuật Phi tinh hiện đại. Với phần đã đọc, còn toàn bộ điều kiện phụ, phép chọn sao khởi/độ cao và cách nối nhà thực. Kho 40 mục vẫn mở; không báo đã khai thác hết.
