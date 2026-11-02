# B03: quyển bốn và tiền đề Tam hợp/Tam hình

Ngày 27/10/2026. Đây là nghiên cứu nội bộ; không đưa nguồn hoặc phòng kiểm định vào site.

## Phạm vi đọc và bằng chứng

Tái sử dụng byte PDF sách đóng thứ hai đã tải ở phạm vi trước: 41.224.832 byte, 49 trang, SHA-256 `c1e1027331d43769733c6011b4fe99e90928e9fde013fce563c8e9bad81c04bf`. Không có HTTP hoặc PDF gốc mới. Hồ sơ API revision754088942/TLS/raw ở `research/liuyao-b03-volume3/` được giữ nguyên.

Đã xem lần đầu toàn khoảng quyển bốn, PDF30–48, và bìa49: 20 bản ghi, 17 ảnh mới (16 nội dung và một bìa), ba ảnh30–32 mở rộng phần đọc trước. PDF30 in `卜筮正宗卷之四`, `黃金策總斷千金賦直解`; PDF48 có `卜筮正宗卷之四終`. Sách đóng2 hiện đủ49trang đã xem theo phạm vi ghi nhận, gồm phần quyển ba ở hồ sơ trước. Không có OCR, bản chép ngoại giao toàn trang hoặc tuyên bố mọi câu đều được áp dụng.

`MANUAL_READINGS.json` giữ chủ đề và SHA ảnh từng trang. `OPERATIONAL_CLAUSES.json` ghi30mệnh đề có giới hạn, tách hỏi gì, đối tượng, vượng suy, thời hạn, động/tĩnh và cứu hộ. Nguồn nói về thành tín, thần minh hoặc y bệnh là dữ liệu lịch sử; không phải chỉ thị từ người dùng hay bằng chứng kiểm nghiệm khả năng dự đoán.

## Chức năng riêng mới

`triad-reference.mjs` nhận sáu giá trị6/7/8/9 từ dưới lên. Theo đoạn PDF39, bốn nhóm Tam hợp và hai nhóm Tam hình ba thành viên được kiểm tra: đủ mỗi chi trong riêng sáu hào bản quẻ, sau đó có ít nhất hai hào động trong cùng một bộ ba. Cách hiểu “ít nhất hai” là chuẩn hóa thao tác có ghi rõ, không giả làm một câu nguyên văn bổ sung.

Mỗi chi được gắn với đúng vị trí hào; hai bản sao của cùng một chi không thay thế chi còn thiếu. Kết quả chỉ là tiền đề cấu trúc. Chưa bổ sung chi biến, nhật/nguyệt, 子卯 hoặc tự hình; chưa kết luận hợp hóa, hiệu lực, cát hung hoặc ứng kỳ. Những trường đó giữ `null`. Hào tĩnh không bị gán giả chi biến. Đối số lịch/vượng suy không hỗ trợ bị từ chối rõ ràng.

## Kiểm chứng

Đạt9kiểm: 64 lời gọi HHC thật cho64số quẻ; đối chiếu Nạp Giáp bằng các dãy độc lập; 4096ngữ cảnh quẻ/động riêng so bằng cách chọn20bộ ba vị trí, khác với thuật toán tích Descartes của chức năng. Đây không phải4096lời gọi HHC mới hoặc tỷ lệ ứng nghiệm.

Trong24576nhóm/ngữ cảnh, có2048nhóm đủ thành viên, 1120nhóm qua tiền đề động, 2816bộ ba chứng kiến. 22dạng bản quẻ có chi lặp; kiểm tra đã loại trường hợp dùng lặp chi để bù thành viên thiếu. Digest `4e7a98afc24472077d21fa5f46770705293f61245b6f12b4b77f851dcccb3191`.

Điểm giới hạn quan trọng: cả hai Tam hình ba thành viên có0nhóm đủ trong riêng sáu chi bản quẻ trên danh mục64quẻ. Đây là suy ra hữu hạn từ cấu trúc Nạp Giáp đã kiểm, không phải khẳng định sách phủ nhận Tam hình. Muốn xét các trường hợp của sách phải đọc và xác minh cách ghép chi biến/nhật nguyệt trước; không tự thêm chúng để tạo kết quả.

HTML vẫn707411byte/SHA`549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857`; site và ZIPweb giữ nguyên. Tám tham chiếu cũ và bản phát hành trước được bảo tồn ở `archives/v53-before-liuyao-b03-volume4/`. Gói nguồn được đồng bộ riêng, kiểm manifest/ZIP và byte trước đó.

## Phần còn mở

Mọi mệnh đề quyển ba/bốn chưa được biên dịch đầy đủ; chưa có mô hình tổng vượng suy, chân không, tự chọn Dụng thần hoặc thời điểm/dự báo hoàn chỉnh. Sách đóng3–6 chưa tải. B02 còn136đơn vị đăng ký/103thân mục mức đề mục/26khoảng đọc lần đầu; mâu thuẫn ngày–tuần không PDF52 chưa giải quyết. Toàn kho40tài liệu và cả bốn mục lớn chưa hoàn tất.
