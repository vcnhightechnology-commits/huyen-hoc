# Nền tảng Lục Hào từ hai ấn bản ảnh — 27/10/2026

Đã khai thác phần cấu trúc có thể tái lập trong B02 **Tăng San Bốc Dịch** và B03 **Bốc Phệ Chính Tông**, tạo bộ tham chiếu chạy được trong tài liệu nội bộ. **Chưa đưa công cụ Lục Hào hoặc lời đoán mới ra web; chưa khai thác hết hai sách hoặc toàn kho.** Bản dùng vẫn là HTML 707.411 byte, SHA-256 `549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857`.

## Nguồn và mức xác minh

| Hồ sơ | Byte / trang PDF | SHA-256 | Giới hạn |
|---|---:|---|---|
| B02, NLC416-12jh005345-45344 | 11.089.308 / 394 | `caac111bc5c5b1c08fd27b3828e7cf6b5430503800f2427d8f2b28809022abaa` | Metadata Commons: sáu quyển văn bản/ba sách đóng. Tựa PDF3 đề năm Ất Sửu Dân Quốc, tháng bảy (1925); chưa xác minh độc lập năm in bằng trang xuất bản. PDF394 là logo/tờ kết. |
| B03, NLC892-GBZX0301013045-259368 | 50.191.031 / 60 | `5dcd7b5005b1e86f441a9350eefb7c0e9e628c47ab926b2a7d1bdd6691a4773d` | Chỉ sách đóng thứ nhất của tác phẩm mười bốn quyển. PDF2 đề 光緒甲辰新鐫 (1904), 王洪緒輯, 河潞武子齡校對, 文成堂存板. Không gộp thành bản 1889 khác hoặc lấy năm tựa 1709 làm năm in. |

Tám yêu cầu HTTPS được thực thi: sáu thân phản hồi HTTP200 giữ nguyên, gồm hai PDF, hai API Commons, API Wikisource và danh mục Nhật; hai truy cập danh mục NLC thất bại trước khi kết nối TLS, không có thân phản hồi. Các phản hồi thành công có TLS được xác thực; kích thước/SHA1 PDF khớp API, revision mô tả tệp lần lượt `808899674` và `754088939`. SHA-256 chỉ xác nhận byte đã lưu, không phải chữ ký cơ quan lưu trữ hoặc bằng chứng phả hệ văn bản độc lập.

Wikisource có lời tựa B03 revision `2395728`, nhưng liên kết **卷01 không có trang**. Nhãn “toàn văn theo quyển” kế thừa chưa được xác minh. Danh mục chính thức Nhật `子059-0008`, hồ sơ `1079274`, ghi 李文輝, 清乾隆/学耕堂, sáu冊/sáu巻; mới giữ metadata và sáu liên kết sách, chưa tải/đọc ảnh nhân chứng đó. Mã ngày `500000` không được đổi thành một năm in. Web open gặp403 nhưng yêu cầu HTTPS công khai thông thường trả200; giữ riêng hai quan sát, không vượt kiểm soát truy cập. Cả hai danh mục NLC vẫn ghi thất bại.

`research/liuyao-foundations/SOURCE_AUDIT.json` và `REQUESTS.json` giữ URL, thời điểm, byte, hash và lỗi. Không tải lại chỉ để tăng số nguồn.

## Phần đã đọc và biên dịch

Có **28 bản ghi đọc ảnh có giới hạn**, gồm21 trang B02 và7 trang B03. Các bản ghi ghi rõ vùng/chủ đề đã đọc, không nhận là chép trọn trang. **84 ảnh nhỏ/11 contact sheet chỉ phục vụ định vị**, không tính thành84 trang đã đọc hoặc hai sách đã đọc hết. Ảnh lớn đã render nhưng không có bản ghi đọc vẫn chưa được tính. Không dùng OCR.

| Quy tắc | Căn cứ trực tiếp | Phạm vi bộ tính |
|---|---|---|
| Tám cung/64 thành viên | B02 PDF24–26; B03 PDF20–21 | Nhận diện cung, hành cung và thứ tự tám giai đoạn; tên chuẩn hóa/ID số là lớp biên tập. |
| 48 vị trí Nạp Giáp | B03 PDF21, bổ chứng B02 PDF45–46 | Mỗi nửa quẻ đọc từ dưới lên; đối thêm bảng Mai Hoa đã lưu riêng. |
| 25 quan hệ Lục thân | B02 PDF46–47 | Lấy **hành cung quẻ ban đầu** làm gốc; không lấy Nhật chủ Bát tự. |
| Tám vị trí Thế/Ứng | B02 PDF47, đồ hình PDF26–27; B03 PDF21–22 | Thế `[6,1,2,3,4,5,4,3]`, Ứng `[3,4,5,6,1,2,1,6]`; không tự an lại Thế/Ứng cho cột hào biến. |
| Hào động và chú hào biến | B02 PDF44–45,47 | Chỉ hào6/9 có chú biến; Lục thân biến giữ cung gốc. |
| Sáu thần | B03 PDF22 | Nhận can ngày nhập rõ; hai hàng xoay in trực tiếp, bốn vòng còn lại suy từ thứ tự/điểm đầu. Thiếu can ngày để trống. |

Các mặt nạ bit `[0,1,3,7,15,31,23,16]` là cách biểu diễn do nhà phát triển suy ra rồi kiểm với64 tên quẻ và engine thật; không coi chúng là lịch sử hào động của một lần gieo. Tên quẻ được chuẩn hóa theo định danh, không tuyên bố mọi dị thể chữ của hai ấn bản đã hiệu khảo.

### Ví dụ chống an sai Lục thân quẻ biến

B02 PDF44–45 có **Trạch Thiên Quải43 → Thiên Phong Cấu44**, động hào1 và6, mã số từ dưới lên `[9,7,7,7,7,6]`. Quải thuộc **Khôn Thổ**, Thế5/Ứng2. Hào biến1 Sửu Thổ và6 Tuất Thổ đều giữ **Huynh đệ**. Dù quẻ Cấu tự thuộc Càn Kim, dùng Kim làm gốc ở đây sẽ cho **Phụ mẫu**, trái lời giải trực tiếp. Bộ tính giữ chẩn đoán cung riêng của quẻ biến, đồng thời chỉ cho phép cung gốc làm căn cứ Lục thân.

Hai ví dụ gieo ở PDF23–24 là **nhận dạng cực tính quẻ ban đầu**: đổi ký hiệu tròn/chữ thập thành nét để đọc hình. Chúng không phải cặp quẻ chính–biến. Đã tách mã63 `[7,8,9,6,9,8]` và64 `[8,9,8,7,6,7]` khỏi kết quả biến suy bằng thuật toán (lần lượt51 và12). Không dùng kết quả suy để nhận đã thấy hình biến trong sách. Ví dụ thứ tư là Càn tĩnh, đủ sáu nhãn Lục thân ở PDF46.

## Kiểm chứng thực thi

**16/16 kiểm nguồn/cấu trúc đạt** (`qa/liuyao-foundations/ENGINE_RESULTS.json`):

- Chạy **8.260 lời gọi `HHC_ENGINE.hexNumber` thật**, gồm64 định danh,4 ví dụ và hai lời gọi cho mỗi **4.096 cặp quẻ chính–biến**; không mô phỏng đầu ra engine.
- Kiểm **12.288 chú hào động** trong quét đầy đủ, chỉ hiện chú ở hào đổi; mọi Lục thân lấy hành cung chính. Có3.584 cặp khác cung và9.864 chú sẽ khác nếu sai lầm lấy hành cung quẻ biến. Đây là phản ví dụ thuật toán, không phải số lỗi của sách hoặc web đang dùng.
- Đối64 thành viên với danh mục ảnh Mai Hoa trước;48 Nạp Giáp với bảng ảnh đã lưu và một phép vòng chi độc lập;25 Lục thân với chu trình sinh/khắc độc lập; tám mốc Thế/Ứng và bốn ví dụ nguồn được kiểm riêng.
- Kiểm10 can ngày, hai hàng sáu thần in trực tiếp, đầu vào thiếu can, sai kiểu/mảng thưa/chuỗi số và yêu cầu lịch/dự báo chưa hỗ trợ. Kết quả trả về cách ly, không làm đổi bảng gốc.
- HTML và toàn bộ JS/CSS gốc giữ byte; tham chiếu nghiên cứu không được đưa vào site. Không cần chạy lại UI/PDF khi không đổi sản phẩm.

Digest của4.096 cấu trúc đầy đủ: `5c127081137371396489bee77ccb6b61c5b94946ef64a9c2a78ee2c706169060`. Các kiểm xác nhận tính đúng của phép dựng cấu trúc trong phạm vi đã định nghĩa; **không xác minh khả năng dự báo**.

## Trạng thái tiếp theo và đóng gói

B02/B03 chuyển từ `not_established` sang **`research_only`** với chuỗi ảnh → quy tắc → bộ tính → kiểm chứng. Không nâng lên tính năng công khai hoặc “toàn tác phẩm đã áp dụng”. Ma trận vẫn40 hồ sơ, **0 tác phẩm đã áp hết**, bốn hướng và toàn kho giữ `active-not-complete`.

Tiếp bản đồ đầy đủ chương/quyển, Phi–Phục/Phục thần và ví dụ, điều kiện Nhật–Nguyệt/旬空/vượng suy, chọn Dụng/Nguyên/Kỵ thần và mọi ngoại lệ theo từng bản. Cần đọc đủ tiền đề trước khi ghép thành diễn giải cho người dùng; các khẳng định lịch sử về y tế, tuổi thọ/tử vong và hiệu nghiệm không được tự biến thành kết luận sản phẩm. Yêu cầu/kiêng kỵ trong sách chỉ là nội dung nguồn.

Snapshot trước phần này: `../archives/v53-before-liuyao-foundations/`, giữ gói nguồn cũ846.213.328 byte. `package.py --research-only` cập nhật manifest/gói nguồn; HTML độc lập, site một tệp và ZIPweb344.047 byte giữ nguyên. `qa/liuyao-foundations/RELEASE_RESULTS.json` kiểm lại mọi byte manifest/ZIP, trạng thái và các tệp lịch sử. Không công bố lên mạng, gửi đi hoặc đổi số phiên bản.

Tệp chính: `research/liuyao-foundations/RULES.json`, `SOURCE_FIXTURES.json`, `MANUAL_READINGS.json`, `liuyao-reference.mjs`, `FUNCTIONAL_BACKLOG.json`. Tái lập bằng `record-liuyao-foundations.py`, `verify-liuyao-foundations.mjs` và `verify-liuyao-foundations-release.py`; không cần gọi mạng lại.
