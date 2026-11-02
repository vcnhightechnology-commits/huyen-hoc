# Nhật luận: phạm vi công việc, ngoại lệ và giọng nguồn

29/10/2026. Khai thác tiếp nguồn đã giữ; phần này là công cụ nghiên cứu riêng, chưa là bộ chọn ngày trên web.

Đã đọc mở rộng sáu ảnh ITKC248–253 của 選擇要略, tái dùng nguyên byte các ảnh và bản chép số có từ phạm vi trước. Không tải thêm sách, container, vị trí nguồn hay nhân chứng độc lập. Tám nhóm bản đọc được ghi riêng; bảy nhóm có xử lý điều kiện hữu hạn, còn Hỏa/Thủy cách giữ chưa xác định.

## Những phân biệt đã mã hóa

- Đại sát Bạch hổ khi vào trung cung: câu sửa chữa giới hạn 廳堂中間, phần còn lại được ghi 其餘無妨. Lôi đình Bạch hổ ghi 修整廳堂, không tự thêm chữ 中間 vào câu ấy. Câu 又云 về trống nhạc/hội khách ồn ở phần giữa sảnh là giọng dẫn riêng. Hai ví dụ 乙未/乙卯 thuộc lời kể, không là hai ngày kiêng cố định cho mọi nhà. Hàm chỉ nhận vai trò không gian theo nguồn đã khai báo, chưa đổi sang tâm hình học hay phòng trên bản vẽ hiện đại.
- 正四廢 và 傍四廢 giữ riêng. Trong phạm vi khởi tạo đã nêu, 正四廢 giữ điều kiêng; ngoại lệ 傍四廢 đòi có cát thần. Không có cát thần chưa chứng minh điều ngược lại. Chữ 雜用 chưa mở thành mọi công việc. Lời ghi về đóng quan tài/lập sinh phần được lưu lịch sử, chưa đưa thành thao tác sản phẩm.
- 萬通火星 chỉ bao bốn việc in rõ: 起造/竪柱/作火焙/結茅寮. Điều 縱遇諸吉不能壓制 được giữ, không lấy cát thần làm miễn tự động. Không dịch rộng thành mọi thiết bị dùng lửa hoặc lời dự đoán cháy nhà.
- 天火 có hai giọng: 官曆 chỉ ghi 苫蓋; nhóm được dẫn bằng 諸曆書 liệt kê 蓋屋/蓋寮舍/蓋船. Ảnh250 có 諸曆書, bản chép số giữ 諸書. Ghi thiếu chữ 曆 như một khác biệt tại tọa độ chọn; không âm thầm sửa bản số đã lưu. Đây là lời dẫn vô danh trong cùng nguồn, chưa phải hai sách độc lập đã xác thực.
- 受死 có bốn nhóm việc quan tước/biểu chương kiêng rõ, nhưng 埋葬 được ghi 不忌. Đoạn xây dựng có cát thần chuyển sang phép nghi lễ ở phần trước; không được biến thành miễn kiêng đơn giản và không tạo hướng dẫn nghi lễ.
- 天隔 ghi bốn việc 出行/求官/納表/進章 với điều kiện 合得黃道 thì 不避. Thiếu điều kiện chưa suy thành kết luận cấm.
- 人隔 ghi 娶婦/進口 với điều kiện 合嫁娶日 thì 不避. Không đổi thành đánh giá toàn bộ quan hệ gia đình.

Tất cả kết quả chỉ là localAvoidance theo đúng câu và tiền đề đã khai báo. Ngoại lệ cục bộ không cấp quyền thi công: overallSuitability, permissionToBuild, harmPrediction và calendarDate đều null. Không có adapter xác định ngày mang các nhãn thần sát, không có phép suy phòng hiện đại hoặc xác nhận ứng nghiệm.

## Phần chưa khép được giữ mở

火隔 có câu liên quan 寅午戌/納音屬火 và 萬通火星; 水隔 liên quan 申子辰/納音屬水 và 建日. Chưa chốt cách nối 及 hoặc thứ tự ưu tiên khi cùng điều kiện kích hoạt nhiều đoạn. API trả chưa xác định cho cả hai, không tự chọn AND/OR. Một câu miễn riêng 火隔 không xóa điều kiêng riêng 萬通火星. Các danh sách 地隔/神隔/林山隔/鬼隔/刑州隔 và lịch sao vẫn mở; bảy nhóm trên không chứng minh đã áp hết nhật luận.

Các hành vi trong cổ thư là nội dung để nghiên cứu, không phải chỉ dẫn do người dùng giao thực hiện. Chuyện tổn hại, hiệu quả nghi lễ và tiên đoán không được nhận thành bằng chứng thực nghiệm hoặc kết quả người dùng.

## Kiểm chứng và bảo toàn

45ca kỳ vọng thủ công được đóng băng trước viết hàm cùng bản đọc và ma trận crop. Mười nhóm kiểm đạt:45ca chọn,384khung điều kiện,2.574bất biến không dự đoán/không cấp phép;12khung nguồn/không gian/thời gian không hỗ trợ bị từ chối,188ca thiếu tiền đề giữ null và10đầu vào sai bị chặn. Các ca bao gồm phần chồng lặp, không là45nhân chứng độc lập. Ba tệp freeze giữ nguyên SHA. Không gọi engine lịch hoặc lá số trong phạm vi điều kiện văn bản này; không nhận các nhãn do bên gọi khai báo là phép tính lịch đã chạy.

Tám crop cuối đã xem và đối RGB đúng vùng nguồn. Năm crop thử cắt đoạn/đề mục được giữ và loại trước freeze; không nhận chúng làm bằng chứng câu hoàn chỉnh.22tệp được chép từ staging và đối byte/SHA khi đưa vào research/home-activity-clauses/. Mọi nguồn, bản đọc, suy luận và QA ở ngoài site.

Snapshot trước thay đổi ở archives/v53-before-home-activity-clauses/ giữ năm tệp đã đối SHA:manifest5.704tệp/sourceZIP3.021.053.197byte. HTML707.411byte, site một index.html và ZIPweb giữ nguyên. Danh mục40hồ sơ+16tham chiếu có chồng lặp,0toàn tác phẩm đã áp hết; L01/L02vẫn research_only của cùng tác phẩm. Gói nguồn cập nhật cùng báo cáo/trạng thái; payload chuẩn bị không được coi là đã kiểm phát hành trước khi --no-write hoàn tất.

Lệnh kiểm chỉ đọc (Python có PIL):

    python v53/scripts/verify-home-activity-clauses-sources.py --no-write
    python v53/scripts/verify-home-activity-clauses-release.py --no-write

Nối tiếp các điều kiện chưa khép theo COVERAGE.json; không tải hoặc đếm lại sáu ảnh này thành nguồn mới.
