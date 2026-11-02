# V53 — thêm hình minh họa cho bản người dùng

Ngày: 25/10/2026. Yêu cầu: thêm hình ảnh để trang bớt đơn điệu nhưng vẫn cuốn hút. Cập nhật cùng V53; bản hoàn thành ngay trước thay đổi được giữ tại `archives/v53-before-imagery/` gồm HTML, gói web, gói nguồn và manifest.

Đã tạo ba tranh bằng **ImageGen tích hợp**: sơn thủy xanh ngọc cho phần đầu trang; trăng sao cho trạng thái chưa nhập của Tử vi, Bát tự và Gieo quẻ; sen trong bình men ngọc cho Bản mệnh và Hướng nhà. Tông nền giấy, xanh trầm và vàng nhạt đồng bộ với giao diện. Không dùng chữ giả, trang sách hoặc biểu đồ thiên văn làm dữ liệu minh chứng. Tranh chỉ có vai trò trang trí.

Ảnh nằm ngoài các kết quả tính, lá số và phần diễn giải. Màn hình nhỏ đặt tranh sơn thủy dưới lời giới thiệu, tránh đè lên chữ. Ảnh trang trí có `alt` rỗng và vùng `aria-hidden`; có kích thước sẵn để hạn chế dịch chuyển bố cục. Không thêm chuyển động hoặc ảnh nền dưới văn bản. Giao diện in ẩn tranh trang trí.

Ba PNG gốc được giữ trong `assets/originals/`. `scripts/prepare-art.py` chỉ giảm kích thước theo tỷ lệ và mã hóa WebP, không cắt, tô màu hay chỉnh nội dung. Ảnh dùng trên web tổng cộng 204.062 byte (hero 139.220; trăng sao 25.714; sen 39.128). Prompt đầy đủ ở `assets/GENERATION_PROMPTS.json`; kích thước và SHA-256 gốc/WebP ở `assets/ASSET_MANIFEST.json`.

`art.js` dùng các tệp cục bộ khi phát triển. Script build nhúng hero và registry hình vào HTML bằng data URL. Mỗi ảnh chỉ được lưu một lần trong HTML rồi tái dùng theo công cụ, không tải qua mạng. `site/index.html` và HTML ở gốc workspace vẫn là bản độc lập. Gói web chỉ có HTML và hướng dẫn, không kèm prompt, ảnh PNG gốc, báo cáo hoặc nguồn nghiên cứu.

`scripts/verify-imagery.mjs`: **35/35** kiểm tra đạt. Đã kiểm byte ảnh, giải mã ảnh nhúng, chọn tranh theo năm công cụ, bố cục 320/390/768/1024/1440 px, ảnh trên điện thoại không đè chữ, trang nguồn cục bộ, kết quả Tử vi và bản in. Không lỗi JavaScript hoặc yêu cầu HTTP trong lượt kiểm tra bản độc lập. Đã nhìn ảnh chụp máy tính và điện thoại. Các hàm tính và nội dung luận giải giữ nguyên so với bản lưu trước bổ sung ảnh; hồ sơ 99 kiểm tra nền trước đó vẫn được giữ, không tuyên bố là 99 phép kiểm mới cho thay đổi hình ảnh.

Không xuất bản lên mạng. Nguồn, suy luận nghiên cứu và bảng đối chiếu tiếp tục nằm ngoài web sử dụng.
