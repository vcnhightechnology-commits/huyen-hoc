# Mai Hoa trong Gieo quẻ — checkpoint26/10/2026

Thêm lựa chọn **Mai Hoa** cạnh đồng xu/nhập sáu hào. Có bốn cách lấy số, một hào động, quẻ chủ/biến/hỗ, Thể/Dụng/ngũ hành và lời gợi mở. Hồ sơ lưu dữ liệu đầu vào cùng phiên bản quy ước, mở lại tính lại sáu hào; dữ liệu dẫn xuất cũ không được dùng làm căn cứ. Quy ước không hỗ trợ có thông báo, không âm thầm thay thế. TXT/in giữ đầu vào, vai trò và đủ sáu hào. Không tự điền ngày giờ khi mở biểu mẫu.

Nút điền hiện tại dùng lịch Việt Nam UTC+7, có mốc đổi ngày và tháng nhuận hiện rõ; ngày nằm trong vùng lịch cần xác nhận bị chặn. Cách sự vật/phương vị cần người dùng chọn biểu tượng và hướng quan sát. Giao diện dùng hình quái SVG, đã chỉnh checkbox tháng nhuận và thử320/390/768/1440px.

Nguồn riêng trong `research/meihua/PROVENANCE.md`, `MANUAL_READINGS.json`, `RULES.json` và hai chỉ mục. PDF5.621.631byte/232trang khớp CommonsAPI; ba quyển chép giữ revision. 25 trang có sổ đọc mục tiêu (24 trang nội dung và tờ cuối232), thêm bìa/tựa/mục lục2–12 để phân định cấu trúc; chưa tuyên bố đã đọc hết năm quyển hoặc xác minh năm in1925. Sáu ví dụ chỉ đối chiếu số học; không nhận các chuyện kể làm bằng chứng khả năng dự báo.

Kiểm chính:20 nguồn/runtime +38 Chromium +50 hồi quy =108 kiểm đạt. Engine chạy384 cấu trúc,51.840 tổ hợp thành phần ngày giờ,768 tổ hợp phương vị và1.728 tổ hợp hai đợt âm thanh. Quét tổ hợp không xác nhận mọi ngày âm tồn tại hoặc hiệu lực dự báo. Chromium kiểm bốn cách, lỗi nhập, lưu/mở cũ/mới, dữ liệu dẫn xuất bị sửa, phiên bản lạ, TXT/in, nút hiện tại tại23h/00h/Tết/tháng nhuận, màn hình nhỏ và khôngJS/HTTP. PDF bốn trang được render/xem toàn bộ; nguồn, log và báo cáo ngoài site.

Các bộ tính/nội dung cũ ngoài app.js giữ nguyên byte so snapshot `archives/v53-before-meihua/`; thay đổi app chỉ tích hợp phương thức mới và khôi phục hồ sơ an toàn. Kiểm50 lõi chạy engine thực, gồm so V52. HTML/site/gói được kiểm riêng bằng `scripts/verify-meihua-release.py` sau đóng gói; kết quả tại `qa/meihua/RELEASE_RESULTS.json` là mốc xác nhận phát hành.

Phần còn mở: đọc và phân loại toàn bộ từng đơn vị năm quyển, thống nhất mapping mục lục ảnh với bản chép3quyển, phép chữ/nét/âm lịch sử, phép đo, điều kiện mùa/ngoại ứng và các dị bản. Toàn kho/bốn hướng giữ **active-not-complete**. Checkpoint này không phải hoàn tất sách.
