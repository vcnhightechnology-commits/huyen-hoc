# Mai Hoa: định danh bản in và các bảng quyển bốn–năm

Ngày 26/10/2026. Đây là phạm vi nghiên cứu nội bộ tiếp nối V53, chưa phải khai thác hết sách hoặc hoàn thành Lục Hào.

## Kết quả ảnh hưởng độ tin cậy

Trang PDF231 ghi trực tiếp **中華民國十四年十一月出版** và dòng phát hành cùng tháng, tương ứng **tháng11/1925**. Văn Minh thư cục là đơn vị in/phát hành; nhan đề ghi **全二冊**, trong khi nội dung chia **năm quyển**. Hai khái niệm này không được đếm thành hai hoặc năm tác phẩm độc lập. Đây là niên đại của nhân chứng đang giữ, chưa chứng minh bản in đầu tiên hoặc tác giả lịch sử Thiệu Ung. Lần tra danh mục NLC thất bại TLS vẫn được giữ nguyên.

Đầu quyển bốn ở PDF145, trang in1; PDF188 là trang kết quyển bốn, trang in44. Đầu quyển năm ở **PDF189**, trang in1; PDF228 là trang kết, trang in40. Vì vậy ước tính cũ bắt đầu quyển năm ở188 bị sửa; PDF200 là trang in12 và PDF220 là trang in32. Giá trị cũ vẫn lưu trong `research/meihua-reading/ADDITIONAL_SCAN_NOTES.json`, cùng chứng cứ sửa. PDF229–230 là quảng cáo;231 là trang xuất bản, không phải ba chương thuật số mới.

PDF gốc vẫn5.621.631byte, SHA-256 `af608094ab11ae209eae91a9365565e7c9cff604aac3da5e753e04d1cc4598c0`. Lượt này không tải HTTP mới. Thêm87PNG từ PDF cũ, tổng186derivative; không gọi87ảnh là87trang đã đọc.

## Phần thực sự đọc và trích

`research/meihua-witness/MANUAL_READINGS.json` có **41bản ghi trang có mục tiêu**:35trang nội dung(32mới,3mở rộng),3trang kết,2quảng cáo và1trang xuất bản. Mục lục9–12được dùng lại để điều hướng. Mỗi bản ghi giữ hash ảnh; không OCR, không nhận là đã chép đủ từng chữ của trang.

`UNIT_MAP.json` lập34nhóm đơn vị có giới hạn. Nhiều mục sao trong văn tự được giữ thành một nhóm; không tăng số chương đã hoàn thành bằng cách đếm từng tiêu đề con. Các trang150–178,209–219,221–227vẫn cần lập bản đồ/đọc đầy đủ;123đề mục bản số trước đây không thay cho phần này.

- **Nạp Giáp:** PDF206–207có48tổ hợp can–chi–hành của tám quái, phân ba hào dưới/ba hào trên và chỉ dẫn đọc từ dưới lên. `NAJIA_TABLE.json` giữ đủ bảng; `najia-reference.mjs` biên dịch thành sáu vị trí cho từng quẻ trong nghiên cứu. Càn/Khôn có can khác giữa hai nửa nên không dùng một can cho cả sáu hào. Chưa xác lập cung, Thế–Ứng, Lục thân, Phục thần hoặc toàn bộ điều kiện luận Lục Hào từ bảng này.
- **Sáu thần theo can ngày:** PDF179ghi sáu cách khởi; PDF180chỉ in hai hàng ví dụ Giáp–Ất/Bính–Đinh. Bốn phép xoay còn lại là suy diễn triển khai được ghi riêng. Quy tắc dùng can **ngày**, khác hình chữ của mục `六神形式` quyển năm; không tự đổi thành can giờ hoặc can năm sinh.
- **Nạp âm:** PDF205đọc đủ30cặp/60Giáp Tý. Hai tên `路傍土`/`路旁土` và `井泉水`/`泉中水` được giữ như dị danh; không tự sửa byte nguồn hoặc đổi nhãn đang dùng khi hành không khác.
- **Mùa:** PDF204in20ô thuộc bốn hàng Vượng/Tướng/Hưu/Tù; bảng này không in hàng Tử. Chưa tự bổ sung hàng thứ năm, ranh mùa hoặc dùng bảng làm điểm vượng suy tổng hợp.

Các mục tướng chữ yêu cầu hình dạng nét, độ dài, độ nghiêng, chỗ nối, ngữ cảnh người viết và điều đang hỏi. Mục Chủ thần còn phân biệt can năm của bản thân với nạp âm ngày cho việc gần; chữ Dụng thần ở đây cũng không tự đồng nghĩa với dụng thần Bát tự. Truyện đoán chữ, dự báo bệnh/chết/tài sản và đánh giá đạo đức được phân loại trong lịch sử văn bản; chưa có cơ sở để biến thành kết luận cá nhân tự động.

## Kiểm chứng đã chạy

`node v53/scripts/verify-meihua-witness.mjs`: **13/13kiểm đạt**. Bộ kiểm xác nhận PDF/sáu phản hồi cũ/186ảnh khớp hash;48ô Nạp Giáp hợp lệ về cặp âm dương và hành của chi; bốn ca Càn/Khôn/Thái/Bĩ giữ chiều từ dưới lên. Bộ tính hiện hành chạy đủ64quẻ để kiểm384vị trí nghiên cứu. Bộ `destiny` thật chạy60năm trong chu kỳ, **60/60hành nạp âm khớp**, giữ hai cặp dị danh. Hai hàng sáu thần in sẵn khớp;20ô mùa giữ đúng phạm vi đã trích.

Các lượt này kiểm định chép bảng, chiều hào, phép ghép và tương thích dữ liệu; không chứng minh lời dự báo truyền thống. Không có kiểm trình duyệt hoặc PDF mới trong phạm vi nghiên cứu này.

## Bản người dùng và công việc dở

HTML đang dùng giữ **703410byte**, SHA-256 `3800162854742c915d60f0051c65cadb0eb9a1c803f9f937bf1b6a593c96d268`. Mọi JS/CSS gốc, HTML độc lập, root và site giữ byte bản đã hoàn thành; gói web giữ nguyên. Nguồn nghiên cứu, candidate và QA chỉ nằm trong gói nguồn nội bộ.

Candidate giải thích bốn lớp Thể–Dụng nằm ở `research/meihua-layers/candidate/`.14kiểm phép tính đạt, gồm384cấu trúc/1536quan hệ; các hàm nhập/lập quẻ cũ nguyên văn. Lệnh chạy trình duyệt chưa được thực hiện vì bộ duyệt phê chuẩn tự động không hoàn tất do hạn mức sử dụng. Không đổi cách khởi chạy để vượt bước duyệt này; không ghi kiểmUI/PDF là đạt. Mốc chi tiết ở `research/meihua-layers/PENDING.json`. Chỉ tích hợp sau khi kiểm giao diện, lưu/mở, TXT, in và xem ảnh PDF xong.

Tiếp tục đọc phần thân sách còn mở, đối chiếu nhân chứng khác cho Nạp Giáp/Lục Hào và hoàn thiện điều kiện của từng truyền bản. Không nhận là toàn kho hoặc cả bốn hướng đã hoàn tất.
