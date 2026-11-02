# Mở rộng các phép Mai Hoa có đầu vào rõ

Gieo quẻ → Mai Hoa có thêm **ngày giờ và số cộng**, **chữ/âm đã xác định**, **trượng–thước**, **thước–tấc**. Tám cách chọn gồm bốn cách trước; phần chữ có bốn phân kiểu1chữ,2–3chữ,4–10chữ và11–100chữ. Kết quả ghi dữ liệu thực dùng và việc cộng/không cộng giờ. Biểu mẫu chỉ hiện đầu vào cần cho cách đang chọn; giữ lưu/mở hồ sơ,TXT/in và giao diện320–1440px.

Quy tắc/giới hạn tại `research/meihua-methods/SPECIFICATION.md`. Tái dùng byte nguồn đã giữ; không thêm HTTP,sách hoặc ảnh đọc mới. Sáu ví dụ số học đã đọc trước nay đi qua chính phương thức mới: ba số cộng4/6/21,hai ví dụ nét7/8và7/10,một ví dụ sáu âm cổ. Không tự đếm nét họ tên hoặc suy thanh cổ từ tiếng Việt. Hai phép đo giữ sự khác nhau về giờ; phần bằng0 và quy đổi đơn vị lịch sử chưa tự định nghĩa.

12 kiểm nguồn/runtime và50 Chromium đạt. Sáu fixture từ ví dụ in được phân biệt với sáu fixture quy tắc tự dựng;467 trường hợp bốn cách cũ so nguyên kết quả với snapshot,90 độ dài11–100 và từng độ dài âm4–10 được kiểm. `compose` nguyên văn, mọi JS khác và CSS giữ byte. UI thử bảy biến thể mới, lưu/mở từng biến thể, đầu vào ẩn sai, giờ bị ẩn, thiếu giờ bắt buộc, số không hợp lệ, helper hiện tại, TXT/in, các cách cũ, sửa sáu hào dẫn xuất trong hồ sơ,khôngJS/HTTP. PDF bốn trang đã xem đủ; lần render cuối khớp từng PNG đã xem. Không lặp toàn bộ51.840 tổ hợp cũ hoặc50 kiểm công cụ khác khi các mô-đun tương ứng không đổi.

Snapshot `archives/v53-before-meihua-methods/` giữ HTML694.834byte/SHA9e49791…,hai ZIP và nguồn trước. Nguồn/app/CSS của các chức năng ngoài Mai Hoa giữ nguyên; HTML/site/gói chỉ được coi đồng bộ khi `qa/meihua-methods/RELEASE_RESULTS.json` xác nhận. Không tăng số phiên bản.

Các nhóm phép chữ/đo/số cộng hoàn thành trong giới hạn đầu vào nêu trên; chưa hoàn tất toàn sách. Tiếp hỗ của Thể/Dụng,điều kiện theo mùa/ngoại ứng và bản đồ đơn vị đầy đủ quyển4–5. Những tranh chấp nhãn quẻ/dị văn đã ghi vẫn mở; không dùng chúng làm ca kiểm “đúng” cho bộ tính.
