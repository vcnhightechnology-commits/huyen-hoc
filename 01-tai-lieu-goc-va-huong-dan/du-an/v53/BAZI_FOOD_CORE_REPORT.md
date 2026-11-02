# Thực thần: lượng, khí lực và nhãn quan hệ

Ngày28/10/2026. Nối từ `BAZI_FOOD_SOURCE_REPORT.md`, không thêm một tác phẩm hoặc nhân chứng nguồn.

## Phạm vi

Chọn **12 mệnh đề/135 codepoint** từ **8 ngữ cảnh** trong corpus90 nhóm vừa đọc. Giữ offset và nội dung chính xác ở `research/bazi-food-core/SELECTED_PREDICATES.json`. Tám ngữ cảnh được chọn vẫn còn mệnh đề phụ chưa mã hóa;82 nhóm khác chưa được chọn trong module này. Không cộng phần chọn nhỏ này thành một lần đọc sách mới hoặc tuyên bố hết điều kiện Thực thần.

## Quy tắc riêng

Module `core-reference.mjs` có **11 phép kiểm tiền đề nguồn**, gồm thân/Thực đều vượng và vô xung phá; mẹ/con cùng suy tuyệt; Thực nhiều/ít với Ấn vận; thân suy/Kiêu vượng; Tài quá nhiều; nhãn Thương Quan trong ngữ cảnh Thực trùng; Thực bị khắc/cùng không vong; chuỗi Thực chế Sát/sinh Tài; hai đường ngày dương/âm với ám hợp Quan/Ấn và yêu cầu không hiển/thuần.

Chỉ âm dương nhật can và quan hệ can lộ được tính từ đầu vào can–chi đã định danh. **21 tiền đề khí lực, nhiều/ít, thuần, xung phá và hợp/chế hiệu lực nhận khai báo nghiên cứu**, không tự xác nhận cho người thật. Việc yêu cầu sự tương tác hiệu lực là điều kiện triển khai thận trọng để tránh suy từ hai chữ có mặt; các mảnh nguồn không cung cấp đủ thuật toán ấy. Ba giá trị true/false/null giữ thiếu dữ liệu khác kết quả sai. Không tự xem “không nhiều” là “ít”, “không mạnh” là “yếu”, hay một can Thực là đã “thuần”.

Nguồn luận **食神多者宜行印運/食少者不宜** theo hai tiền đề khác. Bộ kiểm giữ hai nhánh và cấm khai báo đồng thời nhiều/ít trong cùng khung lượng, nhưng không tự suy ngưỡng số lượng. Câu **重見變為傷官** được giữ như nhãn luận cách có tiền đề riêng; mọi quan hệ 食神 của can vẫn giữ nguyên.

Kết quả một phép kiểm tiền đề true chỉ nói các khai báo của phép kiểm ấy khớp. Nó không xác nhận thành toàn cách, vượng suy, thứ tự ưu tiên giữa văn/thơ/bình hoặc kết quả cuộc đời. Các trường này vẫn null; không phát hành module lên site.

## Kiểm thực thi

**8 kiểm đạt**, gồm78 tổ hợp ba giá trị. Chạy **2 HHC Bát tự thật+2 lần inspect quan hệ** cho hai ví dụ nguồn đã dựng lịch ở phạm vi trước, lần này để kiểm phép chiếu mới. Ví dụ 戊日 có hai Thực lộ ở tháng/giờ; ví dụ 専印癸日 không có Thực lộ. Cả hai vẫn để nhiều/ít và nhãn trùng cách ở trạng thái chưa xác định nếu không có tiền đề riêng. Đây là hai ví dụ cũ chạy lại cho logic mới, không phải hai chứng cứ nguồn độc lập mới.

Đối thêm **10 nhánh quan hệ Thực** của module mới bằng10 truy vấn hàm Thập thần HHC thật và10 truy vấn bảng lunar-typescript1.8.6 thật. Cộng8 truy vấn bảng quan hệ từ hai chart trên là **18 truy vấn bảng**, không phải18 lá số lịch. Cặp can–chi tổng hợp trong phép thử10 nhánh chỉ dùng kiểm tọa độ, không khẳng định là bộ ngày–giờ lịch khả dĩ. Không chạy thêm lịch/search lunar hoặc lặp6 bài kiểm của phạm vi trước chỉ để tăng số.

Module và8 tệp tiếp nhận giữ đúng byte; hai script kiểm chỉ đổi đường dẫn nhập/xuất/snapshot. Kiểm nguồn kế thừa byte/TLS/crop/RGBA từ phạm vi trước bằng cách đọc, không giải mã hoặc tải lại ảnh cũ. Bốn tờ94a–95b vẫn chưa có ảnh liên tục; không dùng phần predicate nhỏ này để đóng khoảng thiếu.

## Gói và công việc còn lại

Bảo toàn mốc3.927tệp/ZIP nguồn2.107.724.336byte tại `archives/v53-before-bazi-food-core`. HTML707.411byte/site sạch/ZIPweb nguyên byte; ứng viên giao diện vẫn riêng khi browser QA chưa khả dụng. `verify-bazi-food-core-release.py --no-write` kiểm toàn bộ manifest/ZIP sau đóng gói, kết quả đọc cuối mới xác nhận gói hoàn chỉnh.

Tiếp tục các mệnh đề phụ của90 nhóm, lượng/thuần/khí lực theo phương pháp có tên, hiệu lực ám hợp, dị tự và các lớp dẫn. Các mục Bát tự khác cùng Tử vi/nhà ở/Dịch vẫn mở; danh mục40 tác phẩm/mục nguồn,0 tác phẩm áp dụng hết. Không công bố đã khai thác hết kho.
