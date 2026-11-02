# B03: quyển 8–10 và điều kiện tượng gia trạch

Ngày 27/10/2026. Hồ sơ nghiên cứu nội bộ, ngoài site người dùng.

## Nguồn và phạm vi đọc

Sách đóng thứ tư, cùng bộ sáu sách 卜筮正宗: **57.017.134 byte / 67 trang**; SHA-256 `5f8bb92f28120fa4c2c4d629ae8bad9f785dc02324f15f285085c99ab7ffadaf`. PDF và Commons API revision **754088947** đã tải trong staging trước, hai body HTTP 200/TLS được giữ byte. SHA-1 `81df815ecbbfac0526e6b630c73533bafc08155c` và size khớp API; SHA-256 là định danh byte tại máy, không chữ ký nhà xuất bản. **Một PDF/hai body mới vào gói phát hành; không HTTP mới trong nhịp đọc này**. Bản ghi 1904 trong siêu dữ liệu chưa thành kiểm chứng ấn ký mới; cùng bộ không tính nhân chứng độc lập.

Đã xem cả 67 trang theo phạm vi ghi nhận: 65 trang nội dung và hai bìa. Có 17 trang kế thừa pending, thêm 48 trang nội dung và hai bìa được render/xem; hai crop QA 360dpi tại 40–41 không cộng thành trang nguồn. Không OCR hoặc chép ngoại giao đầy đủ. Ranh trực tiếp: quyển 8 mở ở 2, kết ở 21; quyển 9 mở 22, kết 44; quyển 10 mở 45, kết 66.

11 mục chính: 種作2–6, 蠶桑6–9, 六畜9–13, 求名13–17, 仕宦17–21; 求財22–28, 家宅28–44; 墳墓45–54, 求師54–57, 學館57–62, 詞訟62–66. Bốn khoảng đầu kế thừa; bảy khoảng mới/khép phần trước. Mục lồng 新增家宅搜精分別六爻斷法38–44 thuộc Gia trạch, không phải bảy trang độc nhất hoặc mục chính thứ 12. **0 mục đánh dấu áp dụng hết**.

## Chức năng riêng và đối ảnh

`home-symbol-reference.mjs` giữ tọa độ tượng quẻ của đoạn Gia trạch. Trang 28 nêu hào 2 là nhà, hào 5 là nhân khẩu, trong/ngoài; không lấy số thứ tự hào làm tầng nhà. Thế/Ứng giữ của bản quẻ, không đổi thành hai vai này.

Trang 41 nêu `四爻兄弟方言戶` và giải thích thiếu Huynh đệ thì không được lập tức luận cửa. Đại môn còn xét hào 4 hợp hào 2; câu nguồn nói rõ động hoặc tĩnh đều được xét. Tham chiếu dùng bảng lục hợp đã đối trước, **không gán mọi hào 4 là cửa** và không thêm tiền đề động chưa có trong câu này. Trang 40, trong đoạn hào 3, có `兄弟卯爻床榻論`: Huynh đệ Mão được luận giường, không tự gọi cửa. Crop QA đã xem trực tiếp cho cả hai điều kiện.

Đầu vào chỉ nhận sáu giá trị 6/7/8/9 từ dưới lên và ngữ cảnh đoạn nguồn xác nhận. Kết quả trả chi/thân của hào gốc, tiền đề từng tượng và quan hệ cấu trúc. Hào biến giữ riêng theo cung gốc; Huynh đệ biến không thay Huynh đệ gốc để thỏa điều kiện cửa. Không đủ tiền đề chỉ nghĩa chưa đủ cho tượng này, **không chứng minh nhà thực không có cửa**. Không có góc la bàn, tọa độ phòng, số tầng, vị trí cửa/giường thật, khuyến nghị dời đồ hoặc cát hung thực tế. Chưa đưa tham chiếu vào web người dùng.

17 mệnh đề có giới hạn trong `OPERATIONAL_CLAUSES.json` phân mục nông nghiệp/tằm/vật nuôi, thi cử/chức vị, cầu tài, gia trạch, mộ, thầy/học quán và kiện tụng. Vai trò phụ thuộc vật và người được hỏi. Các lời bệnh/tai họa/tử tôn/khấn lễ/sinh lợi là dữ liệu văn bản lịch sử; không phải chỉ dẫn người dùng, kiểm chứng kết cục hoặc tư vấn hiện đại. Danh tính người thêm từng đoạn 新增 và phả hệ chưa hiệu khảo xong.

## Kiểm chứng thực thi

Đạt **9 kiểm**. HHC thật thực thi **64 lời gọi chỉ số quẻ**, nối đúng danh tính 64 quẻ. Bộ riêng chạy **4096 ngữ cảnh** (64 bản quẻ × 64 mặt nạ động), giữ **12288 chú hào động**. Đối chiếu riêng bằng dãy Nạp Giáp literal, chu kỳ ngũ hành và sáu cặp lục hợp, không lấy chính hàm đang thử làm oracle.

Trong tập hữu hạn này: 1024 ngữ cảnh có Huynh đệ hào 4; 128 đồng thời hợp hào 2; 64 có ngoại lệ giường hào 3. Có 256 ngữ cảnh hợp 4–2 nhưng thiếu Huynh đệ gốc, và 280 có Huynh đệ biến ở hào 4 nhưng thiếu Huynh đệ gốc: cả hai không qua tiền đề đại môn. Điều kiện tượng giữ bất biến khi chỉ đổi động/tĩnh; chú hào biến vẫn được giữ. Đây là số trường hợp cấu trúc, không tỷ lệ đoán đúng hoặc phát hiện đồ vật. Digest `b1c03df37eee4d47140e7ca24b143444a8bf85ed562035fa949caae678283fc8`.

Năm ca dương/âm do bộ kiểm chọn theo tiền đề nguồn được ghi rõ **ca dựng**, không giả là quẻ gieo in trong sách. Đầu vào sai/thiếu ngữ cảnh, extra la bàn/phòng/vượng suy, mảng thưa hoặc giá trị sai đều bị từ chối. HTML và 11 tham chiếu trước giữ byte.

## Phát hành và phần mở

HTML 707411 byte/SHA `549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857`; root/site/ZIP web giữ nguyên. Snapshot trước ở `archives/v53-before-liuyao-b03-book4/`: source ZIP 1391617952 byte / 2441 tệp manifest. Nghiên cứu nằm trong gói nguồn, ngoài site; kiểm toàn byte manifest/ZIP được ghi ở `qa/liuyao-b03-book4/RELEASE_RESULTS.json`.

Chưa xử lý mọi mệnh đề của sách 1–4, 384 chú hào/tiền tự, vượng suy, chân không, tự chọn Dụng hoặc ứng kỳ đầy đủ. Sách đóng 5–6 chưa tải tại mốc này; sách 5 được định danh từ liên kết điều hướng trong API sách 4, chưa được tính đã đọc. B02 còn 103 thân mục mức đề mục/136 đơn vị, 26 khoảng đọc lần đầu; ngày–tuần không PDF52 còn mâu thuẫn. Kho 40 tài liệu và bốn mục lớn vẫn active, chưa khai thác hết.
