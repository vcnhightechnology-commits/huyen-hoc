# Đính chính vị trí cột Tư Mệnh và Câu Trần

Ngày 28/10/2026. Đây là **lỗi chép của quá trình nghiên cứu**, không phải dị bản sách hoặc lỗi engine. Bản web đang dùng chưa nhận bảng này nên không bị ảnh hưởng.

Báo cáo `HOME_FINAL_SPANS_REPORT.md` từng ghi 132 ô, trong đó 12 ô Tư Mệnh khác engine và 12 ô Câu Trần chưa chép. Rà lại toàn chiều từ đầu đề đến dữ liệu ở ảnh raw 135 cho thấy đã lấy cột **Câu Trần** gán vào **Tư Mệnh**; cột kế bên mang chữ **日** đã bị xem là cột Câu Trần bất thường. Các crop cũ vẫn giữ để kiểm toán; đọc rời phần cuối cột mà không giữ đầu đề đã không ngăn được lỗi này. Các ưu tiên nghiên cứu dị bản Tư Mệnh trong báo cáo trước và báo cáo đồ phân viện được thay thế bởi đính chính này.

Theo đúng cột có đầu đề trên ảnh, Tư Mệnh là `午申戌子寅辰午申戌子寅辰`, Câu Trần là `未酉亥丑卯巳未酉亥丑卯巳`. Cột 日 riêng in `申子辰巳酉丑寅午戌亥卯未`; không nhập dãy đó thành giờ của Câu Trần. Vai trò đầy đủ của cách nhóm ở cột 日 vẫn chưa giải quyết. Hàng đối chiếu dùng nhãn ngày tuần tự Tý–Hợi tại 134 và ghi rõ tiền đề này.

Giữ nguyên mười cột đầu, sửa 12 ô Tư Mệnh và thêm 12 ô Câu Trần, trước khi chạy engine. **Sáu kiểm mới đạt**; chạy **144 đối tượng Lunar thật**, truy vấn 144 nhãn thần giờ và 144 loại Hoàng/ Hắc đạo. Đủ **144/144 tọa độ nhãn và 144/144 loại khớp** sau alias tường minh. Alias 青龍/金匱/勾陳 là chữ phồn–giản; **土堂 vẫn là chữ in gốc**, phép so dùng alias biên tập 玉堂, không đổi chữ nguồn. Bảng hiện tại đủ đúng một nhãn tại mỗi cặp ngày–giờ được đối chiếu. Không còn 12 khác biệt tọa độ từng nêu.

Ngày dương mẫu giữ từ fixture trước nhưng được kiểm lại chi ngày và chi giờ trên từng đối tượng Lunar mới. Không gọi đây là 144 nhân chứng độc lập hoặc 144 ngày ứng nghiệm. Chỉ thử giờ nhánh ở 0,2,…,22 giờ của ngày mẫu trong tháng 10/2026; không giải quyết Tý muộn, múi giờ lịch sử, ranh ngày hoặc quy tắc tuyển trạch đầy đủ. Không so/đổi HHC hoặc iztro trong phạm vi này.

**Bốn crop native có đầu đề đã xem và khớp pixel**, gồm hai cột thật, cột 日 và khung ba cột; không resample. Crop nháp đầu tiên đặt tên Câu Trần nhưng thực tế là cột 日 được giữ với tiền tố INITIAL và audit. 0 HTTP, 0 vị trí PDF mới, 0 nhân chứng ấn bản mới. Các web trích Nghệ thuật điển 677–678 chỉ dùng định vị, chưa cung cấp nhân chứng bảng giờ có thể đối ảnh; không suy ra bản in không có bảng.

Hàm tra cứu riêng hiện dùng bảng sửa trong `research/home-hour-alignment/`; thư mục `home-yangzhai-final-spans/selection/` và các báo cáo/kiểm cũ giữ lịch sử, **không dùng bảng Tư Mệnh cũ làm dữ liệu hiện hành**. Ngoại lệ 截路空亡 chỉ ba loại việc vẫn giữ nguyên hàm và cách hiểu đã kiểm. Các phép kết luận chung vẫn trả trống; đủ bảng tọa độ không phải đủ thuật tuyển trạch.

HTML độc lập, site chỉ có index, ZIP web và engine giữ nguyên byte. Nguồn, bản sửa, audit và kiểm chứng nằm ngoài site. P08 vẫn 195 vị trí qua lượt đọc đầu, 0 mục áp dụng hết; các điều kiện đồ nhà, 720 ô tháng, ma trận năm/tuổi/thước, Bát tự, Tử vi và Dịch tiếp tục mở.
