# Cửa nội bộ trên mặt bằng chữ nhật

Ngày 26/10/2026. Đây là phần mở rộng hình học của `../measured-plan/SPECIFICATION.md`, không phải quy tắc cổ về hướng cửa hoặc một phương pháp Phi tinh. Không tải nguồn ngoài mới trong phạm vi này.

## Mô hình và đầu vào

Khung nhà, trục X/Y, đơn vị mét và các chữ nhật phòng giữ nguyên. Đường ranh giữa phòng được mô hình hóa bằng đoạn không có bề dày. Công cụ chỉ nhận cửa khi **hai phòng dùng chung một đoạn cạnh** trên sơ đồ; chưa mô hình hóa bề dày tường, khoảng cách hai mép tường, vách cong hoặc cửa nằm giữa hai vùng không chạm nhau. Kích thước phòng là dữ liệu người dùng đã ghi, không phải kết quả đo tự động.

`internalDoors` là mảng tùy chọn, mặc định rỗng, tối đa60 phần tử. Mỗi phần tử gồm `a,b` là hai chỉ số phòng nguyên khác nhau trong danh sách hiện tại; `offset`≥0, `length`≥0,01m và tên tối đa60 ký tự. Giao diện dùng mã hàng ổn định, rồi đổi sang chỉ số tại lúc tính. Xóa một phòng làm bỏ trống lựa chọn liên quan; không tự chuyển cửa sang phòng khác mang chỉ số cũ.

## Tìm đoạn cạnh chung

Hai chữ nhật không được giao diện tích dương. Một cặp cạnh đứng trùng X và giao khoảng Y dài dương tạo tường đứng; cặp cạnh ngang trùng Y và giao khoảng X dài dương tạo tường ngang. Chỉ chạm góc, tách rời hoặc chồng diện tích thì không có tường chung. Sai số so số thực `1e-8m` giữ quy ước cũ, chỉ dành cho tính toán, không phải độ chính xác đo nhà thực.

Đoạn đứng có gốc ở đầu trên của **phần chung**, đoạn ngang có gốc ở đầu trái. Nếu phòngA là `(0,0,5,8)` và B là `(5,2,5,4)`, đoạn chung từ `(5,2)` đến `(5,6)`. Offset1m/rộng1m cho hai đầu cửa `(5,3)`–`(5,4)`, không phải tính từ góc trên của A. Đảo thứ tự chọn hai phòng giữ tọa độ vật lý.

Cửa phải nằm trọn đoạn chung. Cửa có thể dùng hết đoạn hoặc chạm đầu/cuối. Nếu phòng thứ ba chạm/phủ một đoạn cửa dài dương thì từ chối vì liên kết hai phòng không còn đơn nghĩa. Chỉ chạm một đầu điểm không bị xem là phủ đoạn. Kiểm tra này chỉ dùng các chữ nhật đã nhập; không suy ra tường thực.

Hai hàng cửa trên cùng đường ranh có giao chiều dài dương được báo trùng, kể cả chọn hai phòng theo thứ tự đảo. Chạm một đầu không tạo chiều dài trùng. Cảnh báo không làm đổi diện tích phòng phủ. Dữ liệu cửa không tham gia phép tính diện tích, phương vị phòng, 24sơn hoặc hướng cửa viền ngoài.

## Hiển thị và xuất

Ký hiệu `N1…N60` màu tím, tên và hai phòng kết nối. Không có pháp tuyến ra ngoài riêng cho cửa nội bộ; không tạo góc hướng, chiều mở cánh hoặc kết luận lưu thông/cát hung từ đoạn thẳng. Danh sách chỉ thể hiện cửa đã nhập, không chứng minh các phòng còn lại thiếu lối đi.

SVG theo hệ tọa độ cũ, nét trắng lót và tím trên tường, ký hiệu N có viền chữ để nhìn rõ. Tải SVG giữ tên cửa cùng chú giải; TXT giữ tên cặp phòng, đầu đoạn, offset, rộng và hai tọa độ. Bản in mở mục mặt bằng có kết quả, giấu form và khôi phục trạng thái sau in theo luồng đã có.

Mọi thay đổi số đo/thêm/xóa hàng xóa kết quả cũ; sự kiện `change` trễ với cùng chữ ký dữ liệu giữ kết quả vừa tính. Không tự lưu browser storage hoặc truyền mạng; tải lại xóa dữ liệu phiên. Nhãn người dùng được escape ở HTML/SVG và dùng textContent ở gợi ý nhập.

## Nguồn, suy luận và điều chưa xác minh

Đoạn chung, giao khoảng, tọa độ và xử lý mã phòng là **quy ước hình học triển khai**, có ví dụ tính tay và đối chiếu kết quả phiên bản trước; không gán cho sách cổ. Nguồn 24sơn đã kiểm trước (Hiệp Kỷ quyển2/CADAL06056503) được tái dùng để giữ hướng viền ngoài, không xác nhận cách đặt cửa giữa phòng. `REUSED_SOURCES.json` giữ byte/hash từng nguồn và mô-đun liên quan; các bản nguồn không tải lại.

Nhà méo/lõm/nhiều tầng, tường có bề dày, cung phi theo ranh năm và Phi tinh còn mở. Không gọi hoàn thành cửa nội bộ là hoàn tất nhà ở hay toàn kho sách. Không chạy lại engine tử vi/Bát tự đối chiếu thư viện vì không đổi các phép tính ấy; bộ hồi quy lõi vẫn chạy để kiểm việc ghép HTML.
