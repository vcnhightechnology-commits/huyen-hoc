# Phạm vi nhà ở: nhân chứng Trung Quốc, 24 sơn và Đại Du Niên

Ngày thực hiện: 2026-10-26. Tài liệu nội bộ; không đưa bản sách, báo cáo hoặc bảng kiểm engine vào site người dùng.

Đã hoàn tất một phạm vi có thể tích hợp: bảng 24 sơn, tám cung × ba sơn, đối hướng 180°, mô hình ranh góc/sai số và bộ 105 ca kỳ vọng. Đồng thời chạy engine thật đối chiếu 64 nhãn cung × hướng theo một nhân chứng chữ Trung Quốc. Chưa hoàn tất khảo cứu toàn bộ phong thủy nhà ở.

## Nguồn và byte

- **欽定協紀辨方書 卷二**, thuộc **四庫全書**. [Hồ sơ công khai Commons / CADAL06056503](https://commons.wikimedia.org/wiki/File:CADAL06056503_%E6%AC%BD%E5%AE%9A%E5%8D%94%E7%B4%80%E8%BE%A8%E6%96%B9%E6%9B%B8%C2%B7%E5%8D%B7%E4%BA%8C.djvu). Hồ sơ ghi 允祿、梅瑴成、何國宗 và CADAL/Đại học Chiết Giang; đây là thông tin nhà cung cấp, chưa đối chiếu hồ sơ lưu giữ gốc CADAL. Trang ảnh 2 xác nhận tên sách và tên tập 四庫全書. Không gọi đây là bản đầu tiên hoặc bản tác giả.
- Lưu cả container `CADAL06056503.djvu`, **3.433.014 byte**, SHA-256 **`bfd3b76c55d62324919ab161c8c2ba2ecb129b3b2c59a3ab0428807e8f8278db`**. SHA-1 `96c3d1b9cdf5889ca88938b161b5f330b37c12b6` trùng thông tin API Commons. Container 110 trang; **không tuyên bố đã đọc cả 110 trang**.
- Lưu bản chữ [Wikisource ghim revision 787335](https://zh.wikisource.org/w/index.php?oldid=787335&title=%E6%AC%BD%E5%AE%9A%E5%8D%94%E7%B4%80%E8%BE%A8%E6%96%B9%E6%9B%B8_%28%E5%9B%9B%E5%BA%AB%E5%85%A8%E6%9B%B8%E6%9C%AC%29%2F%E5%8D%B702). Bản chữ mang nhãn Tứ Khố; bản chữ và ảnh là hai hiện vật số riêng. Đã đối ảnh đoạn 二十四方位; đoạn 大遊年變卦 mới đọc bản chữ.
- `MANIFEST.json` lưu URL, thời gian UTC, HTTP, TLS, header, số byte, SHA-256 cho từng response. 15 response HTTP200 đều xác thực TLS; 8 response HTTP400 được giữ nguyên và đánh dấu không dùng. Lỗi 400 do kích thước thumbnail957px không nằm trong kích thước tiêu chuẩn; sau đó dùng ảnh500px được trang công khai cung cấp và kích thước960px được máy chủ chấp nhận. Không vượt chặn truy cập.
- `READINGS.json` ghi từng ảnh đã xem trực tiếp. Trang5: đồ hình24phương. Trang6–7: giải thích và đủ tám cung × ba sơn. Trang2–4 xác định sách/mục lục; trang8 trống. Ảnh500/960px là bản render của Commons, không đồng nhất với byte container DjVu.

## Điều sách cho biết

Đoạn 二十四方位 định danh24phương gồm bốn quẻ góc, tám can và mười hai chi. Văn bản nêu Tý–Ngọ và Nhâm–Bính là các cặp sơn–hướng đối nhau. Tám nhóm hoàn chỉnh:

| Cung | Nhóm ba sơn | Hướng theo đồ hình |
|---|---|---|
| 坎 Khảm | 壬 子 癸 | Bắc |
| 艮 Cấn | 丑 艮 寅 | Đông Bắc |
| 震 Chấn | 甲 卯 乙 | Đông |
| 巽 Tốn | 辰 巽 巳 | Đông Nam |
| 離 Ly | 丙 午 丁 | Nam |
| 坤 Khôn | 未 坤 申 | Tây Nam |
| 兌 Đoài | 庚 酉 辛 | Tây |
| 乾 Càn | 戌 乾 亥 | Tây Bắc |

Đồ hình in Nam trên, Đông trái, Bắc dưới, Tây phải. Đã đọc trực tiếp vòng24nhãn và đối lại danh sách ba sơn mỗi cung. Chữ 巳/己 gần hình trong ảnh/bản chữ; trường hợp sơn 辰巽巳 được chuẩn hóa thành chi 巳 dựa đồng thời vòng đồ hình và danh mục mười hai chi, được ghi lại trong `READINGS.json`.

Sách phân biệt 正針, 中針 và 縫針. Quy tắc giao lần này chỉ dùng vòng24phương chính; không tự tráo sang một vòng kim khác. Sách cũng lưu ý các cách quy ngũ hành khác nhau; vì vậy bảng24sơn **không kèm một bảng ngũ hành phổ quát hoặc lời phán cát hung**.

## Suy luận hình học và quy ước số hóa

`RULE_24_MOUNTAINS.json` tách rõ dữ kiện trên khỏi các lựa chọn lập trình dưới đây:

1. Trên bản đồ số Bắc lên trên, chọn tâm **子 Tý = 0°**, tăng góc theo kim đồng hồ. Đây là cách mã hóa hiện đại trên mốc Bắc do người dùng khai báo. Đoạn sách đã đọc không nói “0° Bắc thật”.
2. Chia đều360°/24 = **15°/sơn**, nửa bề rộng7,5°. Chuỗi tâm: 子0, 癸15, 丑30, 艮45, 寅60, 甲75, 卯90, 乙105, 辰120, 巽135, 巳150, 丙165, 午180, 丁195, 未210, 坤225, 申240, 庚255, 酉270, 辛285, 戌300, 乾315, 亥330, 壬345.
3. Với `a = normalize360(angle)`, chỉ số danh nghĩa `floor((a + 7.5) / 15) % 24`. Ranh dưới đóng, ranh trên mở. Ví dụ7,5° danh nghĩa là Quý. Đây là quy tắc xử lý hòa của phần mềm.
4. Đối hướng: `normalize360(a + 180)`, hoặc chỉ số `(i+12)%24`. Dữ kiện sách kiểm chứng các ví dụ Tý↔Ngọ, Nhâm↔Bính; việc mở rộng thành toàn vòng180° là hình học của vòng đều đã khai báo.
5. Khi **sai số=0**, chỉ trả sơn danh nghĩa theo ranh nửa mở; tại7,5° chỉ Quý. Khi **sai số>0**, miền sai số dùng khoảng **đóng** và giữ mọi sơn chạm miền góc. Với tâm0° và sai số8°, ứng viên Nhâm/Tý/Quý. Nhánh sai số>0 có thể kiểm mỗi tâm bằng khoảng cách tròn `distance(a,center) <= 7.5 + error` với dung sai số học thích hợp. Đây là quyết định thống nhất với mô-đun sản phẩm ngày2026-10-26; thay đề xuất ban đầu giữ hai sơn ngay cả khi sai số0 đúng ranh. Cả hai cách xử lý ranh đều là quy ước số hóa, không phải quy tắc được sách chỉ định.
6. Mốc Bắc thật/Bắc từ phải giữ riêng. Nếu người dùng khai báo đo Bắc từ và muốn đổi sang Bắc thật, chỉ đổi khi có độ từ thiên tường minh, dương về Đông: `true = normalize360(magnetic + declination)`. Không mặc định độ từ thiên bằng0; công thức đổi mốc này không được gán là lời sách.

`CASES_24_MOUNTAINS.json` có105ca:24tâm,24ranh,48ca sát hai phía ranh và9ca sai số/Bắc/360. Đây là dữ liệu kỳ vọng để tích hợp, **chưa phải kết quả đã chạy engine24sơn của sản phẩm**. Chưa sửa engine/UI.

## Đối chiếu Đại Du Niên với engine thật

Đọc bản chữ Đại Du Niên trong cùng卷2. Đoạn này phân biệt Đại Du Niên của nhà ở với Tiểu Du Niên; không dùng lẫn hai bảng. Dùng biến đổi các hào của quẻ gốc để tạo quan hệ giữa hai cung. Mã hóa hào dưới/giữa/trên bằng trọng số1/2/4 là phép mã hóa số hiện đại; đoạn sách không dùng phép XOR.

| Những hào đổi | XOR | Nhãn Đại Du Niên |
|---|---:|---|
| Không đổi | 0 | 伏位 Phục Vị |
| Dưới | 1 | 禍害 Họa Hại |
| Giữa | 2 | 絶命 Tuyệt Mệnh |
| Dưới và giữa | 3 | 天醫 Thiên Y |
| Trên | 4 | 生氣 Sinh Khí |
| Dưới và trên | 5 | 六煞 Lục Sát |
| Giữa và trên | 6 | 五鬼 Ngũ Quỷ |
| Cả ba | 7 | 延年 Diên Niên |

Đã thực thi **`window.HHC_ENGINE.directions` thật** bằng NodeVM, engine SHA-256 `462fb78b222f4d17b761f785b42700b4241d0f0e82723d0ff09a0e2aca551dee`. **64/64** quan hệ tám cung × tám hướng khớp. Chi tiết đầu vào, nhãn kỳ vọng và nhãn thực nằm trong `DAYOUNIAN_ENGINE_CHECK.json`; tái chạy bằng `node v53/scripts/full-home-verify-engine.mjs`.

Giới hạn: đoạn Đại Du Niên này **chưa đối ảnh**. Việc engine dùng năm nào để truy cập một hàng cung chỉ là cách gọi hàm; đối chiếu này điều kiện hóa trên cung đã biết và **không xác nhận công thức năm sinh→cung phi**. Trùng nhãn cũng không chứng minh hiệu lực dự đoán và không tự đặt được phòng, bếp hoặc giường.

## Bổ sung công thức năm sinh — 26/10/2026

Sau phạm vi24sơn đã có thêm ảnh **八宅明鏡卷上**, hồ sơ NLC892-GBZX0301012368-287543. Tên chứa trong catalogue rộng hơn tên tác phẩm hiện trên bìa; không đồng nhất chúng. PDF58trang,27.056.088byte, SHA-256`347281dba5998391b59138cbf45224e0df30f41d9eda2767f9d54f5ccb3f8315`. Ảnh trang11/17/23 cho các hạt giống tam nguyên, nam nghịch/nữ thuận, nam5ký2/nữ5ký8; trang24 có mốc康熙二十三年上元甲子. Quy đổi mốc1684 và suy diễn chu kỳ180năm được ghi tách khỏi chữ in.

`node v53/scripts/full-home-kua-verify.mjs` chạy engine thật1900–2100, hai giới, **402/402** sốcung khớp quy tắc suy ra từ nguồn; có45trường hợp vào số5 (22nam/23nữ).18giá trị của9năm mẫu trong sách cũng khớp. Mã/tài liệu/byte/SHA ở `kua/KUA_RULE.json`, `kua/KUA_READINGS.json`, `kua/KUA_ENGINE_CHECK.json`, `kua/MANIFEST.json`. Primary đã xem lại trực tiếp ảnh11và23 để kiểm đoạn quy tắc, không coi58trang đã đọc hết.

## Phần còn lại chưa xác minh

- Công thức sốnăm→cung phi/namnữ/số5 đã có phạm vi chứng cứ mới nêu trên. **Ranh Tết/Lập Xuân vẫn chưa được giải quyết** bằng những đoạn đã đọc. Công cụ hiện giữ năm âm người dùng đã chọn hoặc năm âm từ bộ hỗ trợ; không tự chuyển sang Lập Xuân.
- Phi tinh9cung: hạt giống vận/năm/tháng, thứ tự bay thuận/nghịch, âm dương của sơn–hướng, quy tắc chọn khi kiêm hướng. Chưa có quy tắc Phi tinh hoàn chỉnh đủ chứng cứ trong phạm vi này, nên không giao thuật toán suy đoán.
- Quy tắc chọn tọa/hướng thực tế của căn hộ/nhà nhiều cửa, hướng miệng bếp/đầu giường và chia cung trên nhà méo/lõm. Hình học24sơn không tự trả lời những câu này.
- Chưa đọc toàn bộ sách, chưa xác nhận mọi quy tắc của Bát Trạch/Dương Trạch, chưa đánh giá hiệu lực tiên đoán. Các kết luận vị trí phòng hiện hành cần tiếp tục tách khỏi tiện nghi vật lý, thông gió, chiếu sáng và lối thoát.

## Tệp và lệnh tái kiểm

- `MANIFEST.json`: các response đã lưu + SHA/TLS/HTTP.
- `CADAL_IDENTITY.json`: định danh file, kích thước, số trang, SHA-1 và metadata của Commons.
- `READINGS.json`: các trang/đoạn đã trực tiếp đọc và giới hạn.
- `RULE_24_MOUNTAINS.json`: bảng triển khai và giới hạn nguồn.
- `CASES_24_MOUNTAINS.json`:105ca kỳ vọng.
- `VERIFICATION.json`: kiểm lại23body đã lưu, SHA-1 container khớp catalogue, dữ liệu đối hướng.
- `DAYOUNIAN_ENGINE_CHECK.json`:64kết quả chạy engine thật.
- `node v53/scripts/full-home-finalize.mjs`: kiểm hash byte và tái tạo dữ liệu tham chiếu/ca thử.
- `node v53/scripts/full-home-verify-engine.mjs`: chạy lại64quan hệ có điều kiện cung với engine hiện có.

Các script chỉ ghi vào thư mục nghiên cứu nhà ở được giao. Không chỉnh web, app, engine, package hoặc trạng thái chung.
