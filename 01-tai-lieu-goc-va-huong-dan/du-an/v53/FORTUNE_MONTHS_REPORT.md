# V53 — xem vận hạn theo từng tháng trong năm

Hoàn thành ngày 26/10/2026, tiếp nối phần đối chiếu ảnh Tử vi. Bản trước sửa giữ ở `../archives/v53-before-fortune-months/`, gồm HTML, manifest và hai ZIP. Cập nhật cùng V53, không xuất bản mạng.

## Chức năng người dùng

Sau khi lập lá số và chọn ngày xem vận hạn, mở **Các tháng trong năm…** ở cuối phần vận hạn. Bảng dùng **năm âm của ngày đang xem**, gồm 12 tháng thường và tháng nhuận nếu có, xếp theo thời gian. Mỗi dòng ghi khoảng ngày dương, cung lưu nguyệt và địa chi; dòng chứa ngày đang xem được đánh dấu.

Bấm một dòng để xem từ ngày đầu khoảng đó. Bảng vẫn mở và giữ tiêu điểm bàn phím ở dòng mới, ngày xem trong biểu mẫu/hồ sơ được cập nhật. Mở hồ sơ sẽ tính lại bảng theo ngày và quy ước đã lưu, không dùng một ảnh chụp kết quả cũ.

Ba chính sách tháng nhuận dùng đúng lựa chọn của lá số:

| Lựa chọn | Cách trình bày tháng nhuận |
|---|---|
| Giữ cùng số tháng âm | Một dòng, cùng chỉ số tháng với tháng thường mang số đó. |
| Dùng tháng kế tiếp | Một dòng, dùng chỉ số tháng kế theo lựa chọn. |
| Từ ngày 16 dùng tháng kế | Hai dòng: ngày 1–15 và ngày 16 đến hết tháng. Đây là hai khoảng đọc trong một tháng nhuận, không phải hai tháng mới. |

Ví dụ UTC+7/UTC+8, năm 2025 nhuận tháng 6 có 13 tháng lịch; chế độ từ ngày 16 có 14 khoảng đọc. Dòng 1–15 tương ứng 25/7–8/8/2025; dòng 16–29 tương ứng 9–22/8/2025. Bấm dòng thứ hai chọn đúng 9/8/2025 và chuyển cung lưu nguyệt, không đổi ngày sinh hoặc quy ước lá số.

TXT luôn giữ đủ danh sách tháng, kể cả khi bảng đang thu gọn; thao tác tải xong trả lại trạng thái thu gọn. Trình duyệt mở bảng khi in/PDF rồi khôi phục trạng thái cũ khi kết thúc. Các phần khác của kết quả không bị tự mở hàng loạt.

## Ranh giới dữ liệu

- Năm sinh: những khoảng kết thúc trước ngày sinh bị khóa. Khoảng có ngày sinh chỉ cho mở từ ngày sinh trở đi, nhãn ngày âm và khoảng ngày dương được điều chỉnh tương ứng.
- Tháng có ngày lịch nhạy: tạm khóa điều hướng cả khoảng và ghi rõ có một phần cần xác nhận lịch. Người dùng vẫn có thể chọn ngày trực tiếp ngoài khoảng nhạy; không gán nhãn mọi ngày trong tháng đều sai.
- Phạm vi: năm âm 1899 có thể xuất hiện từ ngày dương đầu năm 1900, nhưng bảng tháng chỉ hỗ trợ năm âm 1900–2100 và ngày dương trong 1900–2100. Trường hợp ấy có thông báo giới hạn. Tháng cuối năm âm 2100 vượt sang 2101 được ghi chưa hỗ trợ đủ khoảng, không tạo đường dẫn sang ngày ngoài miền hoặc tự cắt thành tháng 29 ngày.
- Bảng tháng là một cách duyệt kết quả của engine hiện có, chưa phải luận tổng hợp tất cả sao hoặc dự đoán sự kiện. Không thêm điểm tháng tốt/xấu.

## Nghiên cứu nguồn đi kèm

Đã lấy thêm sáu ảnh IIIF công khai từ [bộ lưu trữ chính thức](https://www.digital.archives.go.jp/api/iiif/4468520/manifest.json), ở thứ tự 81/83/85/87/88/89; giữ byte JPEG 2200 px, HTTP/TLS/SHA và định vị canvas. Đây là ảnh dẫn xuất toàn khung do cơ quan tạo, không gọi là JP2 nguyên bản. Năm ảnh dùng định vị, chỉ một vùng ảnh 88 được phân loại trong lượt này.

Vùng phải ảnh 88 là đồ bố trí/phối hợp **Lộc–Quyền–Khoa–Kỵ**, bốn chữ lớn ở bốn ô và các ô điều kiện nhỏ bên dưới. Nó **không phải bảng mười can → bốn sao**. Không chép thêm 40 mục an sao từ đồ này, không dùng nhan đề để nói đã xác nhận hai dị bản can Canh, không áp điểm mạnh/yếu từ các ô nhỏ lên người dùng.

Kết quả trước về can Canh và lời khởi đại hạn từ cung kề vẫn được giữ riêng. Không đổi bảng Tứ Hóa, cục, cung khởi đại hạn hoặc an sao mặc định chỉ từ đồ vừa xem. `research/fortune-table/DIAGRAM_AUDIT.json` ghi mức đọc, hash và điều chưa xác minh; sáu ảnh không được tính thành sáu đoạn đã hiệu khảo.

Nền của bảng tháng là mốc Đẩu Quân đã đọc từ ảnh 79 ở lượt trước; đếm các tháng tiếp theo và ba cách tháng nhuận tiếp tục là quy ước triển khai đã khai báo. Không gán cách chia ngày 16 cho cổ bản. Engine lịch/an sao trong `engine.js` giữ nguyên byte; mô-đun mới `fortune-months.js` chỉ tổ chức lịch tháng và gọi lại phần vận hạn hiện có.

## Kiểm thử vừa chạy

| Bộ kiểm | Đạt | Bằng chứng |
|---|---:|---|
| `verify-fortune-months.mjs` | 13/13 | 232 khoảng tháng của 2000/2023/2025/2026/2033/2050, đủ ba chính sách; ngày đầu/cuối, số ngày và thứ tự khớp lunar-typescript thật ở UTC+8. 464 lần horoscope iztro 2.6.2 thật kiểm cung ở cả hai đầu khoảng. Kiểm riêng ranh tháng nhuận UTC+7/UTC+8, trước sinh, năm âm/Gregory, lịch nhạy, 1899 và 2100. |
| `verify-fortune-months-browser.mjs` | 22/22 | Điều hướng, tiêu điểm, đánh dấu, lưu/mở, TXT khi thu gọn, in PDF thật, các giới hạn và 320/390/768/1440 px; không HTTP/lỗi JavaScript/nguồn riêng trên UI. |
| `verify-fortune-months-print.py` | 2/2 | Đọc PDF thật 5 trang: đủ tháng 1–12, hai khoảng tháng 6 nhuận, ngày chọn và quy ước. Đã nhìn trang 5 chứa toàn bảng. |
| `verify-four-browser.mjs` | 47/47 | Hồi quy tích hợp bốn mục đã hoàn thành. |
| `verify.mjs` | 50/50 | Hồi quy năm công cụ, so engine V52 thật, lưu/xóa hồ sơ, TXT và bố cục. |
| `verify-home-guide.mjs` | 40/40 | Bảy khu vực nhà, điều hướng, TXT/in và điện thoại; kiểm ảnh hưởng của xử lý in mới. |

Tổng **174/174** phép kiểm trong sáu bộ vừa chạy. Các bộ hồi quy là chạy lại, không được gọi là 174 ý nghĩa nghiên cứu mới. Các ngày và chỉ số trong hai bộ so được lưu tại `qa/fortune-months/`; PDF/ảnh chỉ là chứng cứ QA, ngoài site.

464 lần so không phải 464 lần khớp thô mọi quy ước: iztro dùng split16; chênh cùng tháng/tháng kế được ghi rõ trước khi so. Split16 khớp trực tiếp. lunar-typescript cũng là phụ thuộc trong chuỗi iztro; hai phép so không phải hai nhân chứng lịch độc lập hoàn toàn. Độ khớp runtime không chứng minh năng lực tiên đoán.

## Phát hành và phần còn lại

Đã cập nhật HTML gốc, HTML V53, `site/index.html`, hướng dẫn, manifest và hai ZIP. Gói web chỉ HTML/hướng dẫn; nguồn/ảnh sách/báo cáo/PDF kiểm thử chỉ trong gói nguồn. Kiểm gói xác nhận ba HTML bằng byte và snapshot trước sửa được giữ nguyên.

Cần tiếp tục tìm nhân chứng khác hoặc đoạn văn liên quan để phân định can Canh và tuổi/cung khởi đại hạn; không quay lại ảnh 88 với giả định đó là bảng mười can. Không tự đổi quy ước hiện dùng khi chưa có phạm vi rõ và kiểm thử phù hợp.
