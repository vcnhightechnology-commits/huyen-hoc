# Chuỗi Thực thần–Thiên Ấn trong Tam Mệnh Thông Hội

Ngày 29/10/2026. Nối phần C07 đang dở sau khi mất file phiên chat. Bản trên ổ đĩa đã tiến hơn PENDING_RESEARCH_STATE.json: có kỳ vọng đóng băng, mô-đun thử nghiệm, ảnh cắt và một batch runtime thật. Tiếp nhận phần này, không gọi lại engine hoặc tải lại nguồn chỉ để phục hồi ngữ cảnh.

## Văn nguồn và phần suy luận

Đoạn FOOD-00-C07 thuộc 論食神, tờ 005-85a. Ảnh p171 đã giữ được xem lại qua hai crop native giới hạn đúng kích thước; p170 là 84b, không phải 85a. Không có vị trí ảnh hoặc phản hồi HTTP mới.

Văn đọc: `假如甲見丙為食柱中有壬作甲木偏印尅制丙火不能生戊土不能制庚金使甲木受制退財豈不窘乎`. Sau `不能生戊土` văn không lặp chủ ngữ cho `不能制庚金`. Giữ nguyên văn, ghi rõ ba mô hình: chưa phân định; gán cả hai vị từ phủ định cho 丙; hoặc thử gán vị từ sau cho 戊 theo vị trí gần nhất. Mô hình thứ hai là suy luận biên tập tương thích quan hệ ngũ hành, chưa phải xác lập ý nghĩa nguyên bản. Mô hình thứ ba bộc lộ vấn đề: 戊→庚 là sinh, không phải khắc. Không sửa chủ ngữ vào văn nguồn hoặc lấy tọa độ này làm bằng chứng cơ chế thực tế.

Sáu cạnh đồ thị nguồn giữ riêng quan hệ tọa độ và tác động hữu hiệu. Vai trò với gốc 甲 được tách khỏi vai trò khi đổi gốc sang 丙/戊. Năm can được nêu trong văn không phải năm trụ sinh. Các lớp dẫn `又曰`, `元理賦云`, `一行云` được giữ; lời cứu giải và cân bằng chưa có bộ xác định độ mạnh, phạm vi hay thứ tự ưu tiên. Lời về tướng mạo, tính cách, tài lộc, sức khỏe và thọ mệnh vẫn là nội dung lịch sử trong hồ sơ, không trở thành kết luận cho người dùng.

## Chức năng và kiểm chứng

`inspectSourceFoodChain` nhận đúng tên hệ nguồn, cách gán chủ ngữ tường minh và ba tiền đề nghiên cứu kiểu true/false/null. Chỉ mô hình gán 丙 với đủ tiền đề đã khai báo mới trả danh sách hai cạnh bị văn mô tả là ức chế; kết quả luôn ghi đó là lời nguồn có điều kiện, chưa được engine xác minh. Thiếu tiền đề giữ chưa rõ. Hiệu lực chế hóa, cứu giải, độ mạnh và kết quả thực tế đều chưa tự suy ra. Không nhận ngày sinh hoặc bốn trụ như tiền đề đã được chứng minh.

Kỳ vọng trước triển khai giữ nguyên SHA cho ba tệp. Một batch đã lưu lúc 14:06 ngày 29/10/2026 thực thi 11 lời gọi Thập thần HHC, 11 truy vấn bảng Thập thần lunar-typescript 1.8.6 và 5 truy vấn hành. Đây là đối tọa độ, không phải 11 lá số hay xác minh ý nghĩa câu cổ. Khi nối công việc và kiểm mô-đun đã tích hợp, không thực thi lại batch này.

Bảy nhóm kiểm gồm 8 ca kỳ vọng, 81 khung ba giá trị, 979 bất biến, 9 khung không hỗ trợ và 5 đầu vào sai. Kiểm dữ liệu nguồn đối byte/SHA, hai crop RGB với ảnh gốc và kết quả runtime đã giữ. Hai crop thử có đáy vượt chiều cao ảnh được giữ để kiểm toán và không tính làm bằng chứng đã xem. Mô-đun được tiếp nhận nguyên byte; script kiểm thử chỉ đổi đường dẫn import và dữ liệu.

Ma trận hiện hành ở `research/bazi-food-chain/CURRENT_CONTEXT_COVERAGE.json`: 90 ngữ cảnh cha, 44 liên kết từng phần, 46 chưa liên kết, 0 áp trọn. Chỉ C07 được thêm liên kết. Ma trận 43/47 tại bazi-tongke-cases và toàn bộ các hàng còn lại giữ nguyên; đây không phải 44 quy tắc hoàn chỉnh.

## Tiếp tục

C07 còn thiếu định nghĩa vượng suy, hiệu lực chế hóa, cứu giải, mức ưu tiên và nhân chứng giải chủ ngữ. C05 là hướng tiếp theo: đối phạm vi năm/tháng và ngày/giờ trong ảnh cũ, không tự biến danh sách thành AND/OR hoặc số trụ. Tử vi, nhà ở và Dịch vẫn theo trạng thái mở trong ma trận toàn kho. Chưa coi đọc đầu hoặc hàm tra nguồn là áp hết tác phẩm.

Nguồn, mô-đun nghiên cứu, suy luận và QA được giữ ngoài site. HTML, thư mục site và ZIP web giữ nguyên byte. Bản nguồn trước sửa vẫn ở `archives/v53-before-bazi-food-chain`. Sau cập nhật trạng thái, gói nguồn và PACKAGE_MANIFEST được tạo lại; kết quả kiểm cuối lưu trong `qa/bazi-food-chain/RELEASE_RESULTS.json`.
