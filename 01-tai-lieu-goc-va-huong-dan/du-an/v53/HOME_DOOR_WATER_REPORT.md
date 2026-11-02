# Huyền Không trang quái, mở cửa và phóng thủy — hồ sơ P08

Ngày 28/10/2026; nối tiếp `HOME_FUYUAN_YOUNIAN_REPORT.md`. Hồ sơ nội bộ, không phát hành nội dung nghiên cứu lên site.

Đã xem trực tiếp 18 ảnh DCT gốc tại vị trí PDF94–111, khép khoảng đọc đầu ba mục `論玄空裝卦訣第五`, `論開門修造門第六`, `論放水第七`. 95–110 là 16 vị trí mới; 94 và111 là hai ranh đọc mở rộng, không tính mới. 104 kết quyển hai; 105 mở quyển ba. Tổng P08 hiện có 103/195 vị trí đọc đầu, bảy trong mười khoảng mục đủ lượt đọc đầu; **92 vị trí chưa đọc và mọi bộ điều kiện phụ vẫn mở**. Không đồng nghĩa đã đọc ngoại giao mọi chữ hay áp hết các mục.

PDF151.275.796 byte/SHA-256 `b6394102a995bb66df173452b37614b29d58e34ff85e08c43077006572ac48a5` giữ nguyên. 18 JPEG khớp byte luồng DCT trong PDF; không mã hóa lại ảnh. 12 crop PNG đã xem khớp pixel, không nội suy. Một crop dự định vào cột 巽/巳 nhưng thực tế vào 丙/午 được giữ đúng tên cũ và ghi `CROP_TARGET_AUDIT.json`; có crop sửa đúng đích. Không sửa PDF. **0 HTTP, 0 container hoặc nhân chứng văn bản độc lập mới**. Nguồn Commons có dẫn về Thiên Nhất Các và dấu xử lý Shuge như hồ sơ trước, chưa phải byte tải trực tiếp được xác minh từ máy chủ cơ quan.

## Dữ liệu và phép tra cứu đã bổ sung

`MANUAL_WATER_TABLE.json` chép trực tiếp 24 hàng `二十四山放水定局` từ109–110: **46 mục phương trong dòng chính**, **8 dòng có chú bên/16 mục phương chú bên**. Đây là 62 lần xuất hiện dấu phương trong hai lớp chữ, không phải 62 quy tắc độc lập hoặc 62 hướng khác nhau. Các dấu được giữ ở cấp chữ in như 甲/乙/乾; chưa đổi sang độ la bàn hoặc cung bản vẽ.

Giữ nguyên các dòng khó đọc bằng crop native: 寅 có dòng chính 壬癸/廉貞 và chú 甲乙/六煞; 巽 và巳 có dòng chính 庚辛/六煞, chú 丙丁/巨門. Không sửa các dòng đó cho giống một bảng suy từ engine. Dòng chính và chú bên không tự trở thành thứ tự ưu tiên hoặc danh sách hợp nhất. Các chữ mô tả thiên tỉnh được giữ làm bản đọc chữ; chưa suy kích thước, độ sâu, kỹ thuật thoát nước hoặc cấu tạo xây dựng.

`MANUAL_SOURCE_POLARITY.json` chép hai nhóm12 dấu từ107. Câu nguồn dùng 坎/離/震/兌 cho bốn chính phương; ánh xạ có khai báo sang 子/午/卯/酉 của bảng24sơn. Không gọi nhóm âm–dương này là quy ước phổ quát cho mọi hệ phong thủy, giới tính hoặc lịch.

`source-water-reference.mjs` có hai phép tra cứu riêng:

- `sourceMountainPolarity` trả nhóm âm–dương của đúng đoạn nguồn, giữ nguyên dấu nguồn và alias.
- `sourceWaterTable` chỉ trả bảng khi đã khai báo **gốc山龍** và **nước đi**. Với gốc 福元/hướng cửa/chưa rõ hoặc nước đến/chưa rõ thì để kết quả bảng `null`. Có thể kiểm dấu phương nằm trong dòng chính hay chú bên; kết quả “không được liệt kê” không được đổi thành “xấu”. Tên sao, lời thiên tỉnh và các lớp chữ vẫn riêng.

Văn109 nêu `以山龍為主`, đồng thời nói trường hợp `脫龍就局` xét 福元/門向. Bộ nối tự động giữa các khung đó chưa xác lập; vì vậy API ngăn dùng một dấu hướng cửa thay cho sơn của bảng. API không nhận số độ, năm, mặt bằng hoặc tự phán gốc.

## Kiểm chứng

**8 kiểm đạt**, gồm kiểm đầy đủ24 hàng/62 mục dấu phương trong hai lớp, phân bố12/12, 72 ngữ cảnh sơn–chiều nước và72 ngữ cảnh gốc thay thế. Kiểm các dòng crop khó, sao chính/chú riêng, trường thiếu và lỗi đầu vào; trả dữ liệu sao chép để người gọi không làm biến đổi bảng trong bộ nhớ. Không có lần kiểm thất bại của logic trong phạm vi này; lỗi crop đích được ghi riêng, không che đi.

Nguồn95 trực tiếp nêu bốn cặp phòng 乾坤, 震巽, 坎離, 艮兌 là 延年. Đã thực thi **8 lời gọi `HHC_ENGINE.directions` thật**, chiếu bốn cặp theo hai chiều khai báo; tám nhãn đều khớp Diên Niên. Đây là bốn cặp in trong nguồn, không gọi thành tám ca nguồn độc lập. Các số năm truy cập engine kế thừa từ bộ trước, chỉ để vào cung tương ứng; không tái xác nhận ngày sinh, ranh năm hoặc mặt bằng. EngineSHA-256 giữ nguyên `39f08bd1887faca4d35f7ad415ebf596621010d530b489212774d5cbf99040e6`. **0 lượt lịch mới**; không đem nhãn sao phóng thủy so với cung hiện đại tự giả định.

## Phần đã đọc nhưng chưa đóng chức năng

94–100 nói 初爻/氣口/交門/換象 và các giọng chú khác nhau. Đầu đoạn chia 乾坎艮震 với 巽離坤兌 theo khung riêng. Bốn cặp 延年 chỉ là tọa độ được nêu rõ; chưa khép toàn phép đổi hào, sao gốc, người/phòng và năm tháng hội cục. Tên `玄空` chưa đủ chứng minh đây là Phi tinh hiện đại.

100–104 chứa nhiều lớp tránh ngày, tháng, mùa, năm; các bảng chiếm vị trí cửa, thước mặt trước/sau/trên/dưới và bảng ngày lớn/nhỏ không cùng một phép. Thước có nhiều loại và giọng phê bình truyền bản. Chưa chép đủ các ô, định đơn vị, chọn mặt thước hoặc quy đổi cm; không tự tạo khuyến nghị kích thước cửa.

105–111 phân nước đến/đi, trong/ngoài, trung đường/thiên tỉnh, âm/dương sơn. Tên sao trong các phần ứng nghiệm, bảng phóng thủy và cung không được hợp thành một điểm số. Lời bệnh, tử vong, tội trạng, gia đình và tài sản chỉ được lưu theo bối cảnh lịch sử; chưa xác minh hiệu quả thực tế và không dùng để kết luận người dùng.

Ba mục được đọc đầu không có nghĩa toàn bộ từng câu/đồ/bảng đã áp dụng hết. Nguồn còn ngoại hình13–33, tuyển trạch125–167 và phù trấn168–195 chưa đọc; ranh124 đã đọc trước. Các truyền bản/các phần khác của kho40 mục vẫn đang mở.

## Gói và tính liên tục

Trước tiếp nhận đã giữ snapshot `archives/v53-before-home-yangzhai-door-water/` của bản4.161 tệp, ZIP nguồn2.414.727.056 byte, hash đối đúng. Dữ liệu/module nguồn được tiếp nhận đúng byte, phép kiểm chỉ thay đường dẫn khi đưa vào thư mục nghiên cứu. Báo cáo đóng gói cuối nằm ở `qa/home-yangzhai-door-water/RELEASE_RESULTS.json` sau khi xác minh đọc lại.

HTML707.411 byte, bản độc lập, site sạch và ZIP web giữ nguyên; nghiên cứu/QA nằm ngoài site. Chưa có bộ nối hình học, Bắc từ/Bắc thật, kỹ thuật nước, thước cửa hoặc thuật ngày được xác lập trong phạm vi này.
