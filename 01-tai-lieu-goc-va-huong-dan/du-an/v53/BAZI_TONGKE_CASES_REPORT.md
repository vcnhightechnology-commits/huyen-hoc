# Bát tự — ba ví dụ in trong 食神同窠

Ngày 29/10/2026. Hồ sơ nghiên cứu nội bộ; bản web người dùng giữ nguyên byte.

Đồng khoa FOOD-05-C03: đọc trọn ba chuỗi bốn trụ trên hai ảnh đã giữ191–192, ba crop native khớp RGB. Chốt bản chép và kỳ vọng trước một batch thật:36 cặp vai trò có hướng,23 cặp can phân biệt,36 lần gọi HHC god/36 tra bảng lunar-typescript1.8.6, ba lượt inspect với đầu vào bốn trụ in sẵn. Ba cặp tương thích suy ra theo thứ tự năm/tháng/ngày/giờ là năm→tháng, năm→giờ, ngày→giờ; đây là phân tích biên tập, sách không chú trực tiếp vai trò cho từng cặp. Tự lấy ngày làm gốc làm đổi hai cặp; ba cặp đảo chiều không khớp. Sáu kiểm tái dùng kết quả đã lưu, không chạy lại engine. Không xác lập ngày sinh lịch sử, giàu nghèo, hỗ hoán/sinh vượng/lộc quý hay quy tắc trọn. Tái dùng API十三位 có sẵn, không tạo bộ phân loại trùng;43/47/0 liên kết phần vẫn giữ, C03 thêm hồ sơ đối ca ngoài số áp dụng.0HTTP/vị trí/container/nhân chứng mới, web nguyên byte.

## Chữ nguồn và phần diễn giải

Container CADAL06066041.djvu đã giữ:10.721.582 byte, SHA-256 `013ce4861680a2bf08b811050c45a45bb2d3ce9d164f7e2341d7070bd5cb2c1a`. Hai PNG191–192 là ảnh giải mã đã có. Ba crop cuối đã xem và khớp từng pixel RGB; ba crop thử thiếu đầu/cuối còn ở tmp, không đưa vào gói chứng cứ. Không tải lại, không thêm vị trí hoặc nhân chứng độc lập. Bản số Kanripo và ảnh cùng họ WYG không được tính thành hai truyền bản độc lập.

| Nhãn trên sách | Bốn trụ in | Cặp tương thích khi dùng thứ tự bốn trụ thông thường | Nếu lấy can ngày làm gốc đến cùng trụ đích |
|---|---|---|---|
| 韓魏公 | 戊申 庚申 庚辰 庚辰 | năm戊申 → tháng庚申 | 庚→庚: Tỷ Kiên; 辰/申 khác chi |
| 宋秦檜 | 庚午 己丑 乙卯 壬午 | năm庚午 → giờ壬午 | 乙→壬: Chính Ấn; 卯/午 khác chi |
| 明王崇古少保 | 乙亥 辛巳 戊申 庚申 | ngày戊申 → giờ庚申 | 戊→庚: Thực Thần, cùng申 |

Nguồn in các chuỗi trụ, không chú riêng ba mũi tên này. Thứ tự năm/tháng/ngày/giờ và việc chọn cặp là diễn giải biên tập. Các cặp tương thích đều cùng chi và có quan hệ Thực Thần trong hệ đang dùng; đối với phép đếm十三位 đã giữ, đây là tiến12 trong vòng60. Không suy ra mọi trường hợp bắt buộc lấy năm hoặc ngày. Giữ câu `月不如日日不如時` như lời xếp thứ tự của sách; không gán điểm hoặc chấm hơn kém ba nhân vật.

Đọc trọn đoạn C03 lần này; bản ảnh dùng祿, bản số dùng禄. Lưu hai dạng và không sửa corpus. Cụm `若互換生旺帶祿貴者大貴` vẫn chưa có phép đánh giá đủ tiền đề trong hồ sơ này. Tên nhân vật là nhãn nguồn; không xác minh ngày sinh lịch sử hay thành tựu, tuổi thọ, giàu nghèo.

## Thực thi và kiểm chứng

Bản chép, kỳ vọng ba cặp và ba khung thay gốc ngày, ảnh/crop cùng script đã băm trước lần chạy thật. Một batch thực thi36 lời gọi trực tiếp `HHC_BAZI_RELATIONS.god`,36 tra bảng `LunarUtil.SHI_SHEN`1.8.6,3 lời gọi `inspect`. Có23 cặp can phân biệt trong36 cặp vai trò. Các lời gọi nội bộ của inspect không được cộng vào36 lời gọi trực tiếp. Không phải36 lá số; không tạo đối tượng lịch, không chạy iztro, không dựng ngày hiện đại thay ngày sinh nhân vật.

Đủ36 cặp vai trò khác nhau trong ba ví dụ có đúng3 cặp tương thích. Hai lần thay gốc ngày mất tọa độ đã chọn; trường hợp thứ ba giữ nguyên. Đảo ba cặp cho quan hệ Thiên Ấn và không khớp phép tiến12 có hướng. Ba inspect thật giữ cách trình bày Thập thần theo can ngày của sản phẩm; không dùng tên cách cổ để đổi định nghĩa này.

Sáu nhóm kiểm đạt. Lệnh kiểm tái dùng ACTUAL_RUNTIME và chỉ gọi lại hàm tọa độ thuần đã có; không chạy lại engine hoặc bảng lunar. Không thêm API tương tự, không biến ví dụ thành bộ luận giàu nghèo. Ma trận90 cha vẫn43 có liên kết phần/47 chưa có/0 áp trọn; C03 có hồ sơ đọc và đối ca mới, không được tính là thêm quy tắc đã áp.

```powershell
node v53/research/bazi-tongke-cases/test-evidence.mjs --no-write
python v53/scripts/verify-bazi-tongke-cases-sources.py --no-write
python v53/scripts/verify-bazi-tongke-cases-release.py --no-write
```

Giữ release5389 tệp ở `archives/v53-before-bazi-tongke-cases/` trước cập nhật tài liệu. Nguồn/crop/runtime/QA ngoài site; HTML707.411byte, engine, bazi-relations, content và ZIP web giữ nguyên. Kiến Lộc UI còn chờ browserQA. Toàn kho vẫn mở; xem NEXT_STEPS.md và EXHAUSTIVE_WORK_STATE.json.
