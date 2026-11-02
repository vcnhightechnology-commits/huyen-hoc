# V53 — áp dụng khảo sát bố cục và giao diện

Ngày 25/10/2026. Tiếp yêu cầu của người dùng sau khảo sát các website có lưu lượng đáng kể. Cập nhật trên V53 hiện tại, không tạo phiên bản chỉ để đổi số. Bản hoàn thành trước thay đổi giữ tại `archives/v53-before-navigation-refresh/`, gồm HTML, hai ZIP và manifest; đã kiểm hash HTML trong các gói.

## Những gì đã áp dụng

Tham khảo từ hồ sơ `design-research/2026-10-25/REPORT.md`: đưa tra cứu ra sớm như nguyên tắc quan sát ở Tra Cứu Tử Vi; nhóm công cụ có mô tả rõ như Astro.com; giữ một hệ minh họa nhất quán và nền thẻ nhẹ như định hướng rút ra từ Astrology.com. Không sao chép HTML, ảnh, logo, văn bản luận giải hoặc toàn bộ bảng màu của các trang tham khảo.

- Thu gọn header và phần giới thiệu. Nút “Bắt đầu tra cứu” có nền xanh đậm, đưa đến khu chọn công cụ.
- Năm thẻ hành động: “Lập lá số”, “Xem Bát tự”, “Tra bản mệnh”, “Xem hướng nhà”, “Gieo quẻ”. Mỗi thẻ có mô tả ngắn về kết quả và biểu tượng nét vẽ cùng hệ; trạng thái hiện tại được giữ bằng nền, chữ và `aria-current`.
- Trên desktop, năm thẻ nằm cùng hàng. Điện thoại có ba thẻ ở hàng đầu, hai thẻ ở hàng sau, đủ tên và mô tả, không giấu công cụ trong một hàng cuộn.
- Phần đầu trên điện thoại dùng tranh hẹp cao 140–150 px cạnh tiêu đề; chữ mô tả ở bên dưới, không đặt trên ảnh. Lược các nhãn giới thiệu lặp ở đầu biểu mẫu trên mobile, giữ tên công cụ đang dùng.
- Nội dung diễn giải chính 15–16 px, khoảng dòng khoảng 1,85; nhãn biểu mẫu 14 px và input 16 px trên mobile. Nút và thao tác đọc/lưu có vùng nhấn rõ. Các con số hoặc nhãn dày trong lá số vẫn dùng kích thước riêng, không tuyên bố mọi chữ đều là 15 px.
- Bảng màu riêng của dự án: xanh `#244638`, nền giấy `#F7F4EC`, thẻ `#FFFEFA`, xanh nhẹ `#E7EDDF`, chữ `#26372E`. Chữ phụ được làm đậm hơn; đồng trầm dùng cho nhãn nhỏ và họa tiết.
- Tranh đã tạo được giữ nguyên byte; phần tính, diễn giải, hồ sơ và gieo quẻ không đổi mã. Nguồn nghiên cứu và khảo sát website tiếp tục nằm ngoài sản phẩm.

Các quy tắc mới nằm trong `experience.css`, được script build ghép vào HTML độc lập. Không có font tải từ bên ngoài, thư viện mới hoặc máy chủ tính toán.

## Đo trước và sau

Đo trên Chromium với cùng chiều rộng, chiều cao viewport 1000 px và cùng trang Tử vi chưa nhập. Vị trí là cạnh trên biểu mẫu theo tọa độ tài liệu; đây là phép đo bố cục, không phải kết quả thử nghiệm thời gian hoàn thành tác vụ với người dùng.

| Chiều rộng | Trước | Sau | Biểu mẫu sớm hơn |
|---:|---:|---:|---:|
| 1440 px | 850 px | 665 px | 185 px |
| 1024 px | 784 px | 638 px | 146 px |
| 768 px | 667 px | 618 px | 49 px |
| 650 px | 856 px | 623 px | 233 px |
| 390 px | 739 px | 638 px | 101 px |
| 320 px | 807 px | 629 px | 178 px |

Giá trị chính xác của toàn bộ phép đo nằm trong `qa/experience/test-results.json`; nếu hàng làm tròn ở báo cáo khác dưới một pixel, dùng JSON gốc. Chưa khẳng định việc giảm chiều cao đầu trang đã cải thiện tỷ lệ chuyển đổi; cần quan sát sử dụng thật để đánh giá điều đó.

Kiểm tương phản chữ chính trên nền kết quả khoảng **7,87:1**, chữ nút chính khoảng **10,25:1**, đều trên 4,5:1 trong các cặp được đo. Đây không phải chứng nhận khả năng tiếp cận toàn website. Đã kiểm không chồng chữ/ảnh ở phần đầu mobile và không tràn ngang trang ở các viewport đã thử.

## Kiểm thử đã chạy

- `verify-experience.mjs`: **36/36**, gồm bảo toàn byte của engine/nội dung/app, vị trí trước-sau, năm lựa chọn, chuyển form, cỡ chữ, tương phản, lưu/TXT, biểu đồ, in, dialog và không lộ hồ sơ đối thủ vào DOM.
- `verify.mjs`: **50/50**, các luồng năm công cụ, ngày sai, ngày nhuận/giờ, chưa biết giờ, hồ sơ và xuất. Có hồi quy chạy V52 thật trên 336 lá số Tử vi, 288 cấu hình Bát tự và 402 tổ hợp nạp âm/cung phi.
- `verify-imagery.mjs`: **35/35**, đủ hình nhúng, hiển thị năm công cụ ở 320/390/768/1024/1440 px, nguồn modular và bản in. Điều kiện cũ “ảnh nằm dưới toàn bộ lời giới thiệu” được thay bằng kiểm không chồng headline/description, phù hợp bố cục mới; khung tranh ở 320 px rộng 92 px và cao 140 px.
- Tổng ba bộ trong phạm vi này: **121/121**. Không cộng các kết quả lịch sử 123 của phạm vi đầu vào giờ sinh vào tổng này.

Các tệp `engine.js`, `engine-runtime.js`, `content.js`, `yi-content.js`, `app.js`, `art.js` khớp SHA-256 với manifest trước sửa. Không cần tạo phép đối chiếu engine mới chỉ vì đổi CSS. Không lỗi JavaScript hoặc yêu cầu HTTP trong lượt thử bản HTML độc lập. Đã nhìn ảnh desktop/mobile của trang đầu và kết quả.

## Phát hành

HTML ở gốc workspace, `v53/Huyen_Hoc_Cac.html` và `v53/site/index.html` cùng nội dung. Hai gói V53 được tạo lại, gói web vẫn chỉ gồm HTML và hướng dẫn. Tài liệu này, ảnh chụp đối thủ, số liệu truy cập, mã tái lập và các báo cáo không vào `site/`. Chỉ mở xem cục bộ, không xuất bản lên mạng.
