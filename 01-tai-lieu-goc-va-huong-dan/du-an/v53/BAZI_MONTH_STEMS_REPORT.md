# Đọc đủ tàng can của tháng trong Bát tự — V53

Hoàn thành phạm vi ngày 26/10/2026. Giữ cùng V53, không xuất bản. Snapshot trước phạm vi: `../archives/v53-before-month-stems/`.

## Kết quả cho người dùng

Trong **Bát tự → Nguyệt lệnh và đại vận**, thêm phần thu gọn **Xem đủ các can trong tháng…**. Mỗi can của chi tháng có một thẻ riêng: tên can, bản khí hay can tàng khác, quan hệ với Nhật chủ và vị trí can lộ tương ứng ở năm/tháng/giờ đã biết. Nhật chủ không được tính thêm thành một vị trí lộ; thiếu giờ thì không dựng can giờ. Ngày có trụ bất định tiếp tục chặn phần này.

Trước đây phần nguyệt lệnh nhấn mạnh bản khí và chỉ nêu tên các can đã lộ; quan hệ của các can tàng khác chưa nằm cạnh nhau trong chính phần tháng. Nay có thể đọc đủ mà không ghép lại từ bốn thẻ tàng can ở phần trên. Bản khí vẫn giữ đúng vai trò, không thay bằng một can phụ vì tên quan hệ phù hợp với một mục sách. Có mặt hoặc lộ can không được biến thành xác nhận cách cục, điểm vượng suy hoặc dụng thần.

TXT và bản in mở đủ phần tháng dù đang thu gọn, rồi phục hồi trạng thái. Hồ sơ vẫn chỉ lưu đầu vào và tính lại. PDF mẫu tám trang đã xem đủ; phần can tháng và bảng mười đại vận giữ thành nhóm khi vừa trang, không bỏ hai dòng cuối bảng sang một trang riêng. Màn hình 320–1440 px không tràn ngang.

Chỉ thay phần trình bày `bazi-cycles.js` và CSS `bazi-locations.css`. **Các hàm tính nguyệt lệnh, khởi vận, khoảng chưa rõ giờ và đại vận giữ nguyên đoạn mã**. `engine.js`, `app.js`, Thập thần, các nội dung và công cụ khác giữ nguyên byte.

## Căn cứ mới đọc trên ảnh

Nguồn: [三命通會·卷五, CADAL06066041 trên Commons](https://commons.wikimedia.org/wiki/File:CADAL06066041_%E4%B8%89%E5%91%BD%E9%80%9A%E6%9C%83%C2%B7%E5%8D%B7%E4%BA%94.djvu). Commons quy nguồn CADAL/Đại học Chiết Giang; ảnh trang 2 xác nhận **欽定四庫全書 / 三命通會卷五**. Chưa xác minh độc lập danh mục gốc CADAL, niên đại in hoặc phả hệ văn bản. Không gọi một container khác là truyền bản độc lập chỉ vì khác tệp.

Container DjVu **10.721.582 byte**, SHA-256 `013ce4861680a2bf08b811050c45a45bb2d3ce9d164f7e2341d7070bd5cb2c1a`, SHA-1 `dd6be166b360a58bd142235803fc5a19fd8f267b` khớp API, API ghi 226 trang. Giữ nguyên 38 thân phản hồi/byte/hash/TLS: 37 HTTP 200 và một HTTP 429 khi hỏi ảnh trang 138. Phản hồi 429 không được thử vòng lại hoặc tính là ảnh đã có; tiếp tục làm với phần độc lập đã tải được.

Đã lưu 17 JPEG render của Commons, không đồng nhất chúng với byte trang gốc của DjVu. Trang 1 API báo 960×1363 nhưng phản hồi thực là 500×710; giữ chênh, không dùng trang ấy làm bằng chứng nội dung. 16 ảnh còn lại thực rộng 960 px, chiều cao khớp API. Giữ riêng toàn bộ container và các bản render có URL/hash; không dùng OCR.

Đọc có mục tiêu **ba mục**, 11 ảnh ngữ cảnh và đối **10 mệnh đề ngắn** với bản chép số Kanripo WYG đã ghim commit. Không gọi 11 ảnh là 11 trang đã chép/hiệu khảo đầy đủ hoặc đã đọc hết 226 trang.

| Mục | Ảnh / mã trang WYG | Điều đã đối và giới hạn |
|---|---|---|
| 論正官 | 11–16 / 005-5a–7b | Năm mệnh đề về nguyệt lệnh, chi tàng/can thấu, ngoại lệ khi có Ấn dù thân yếu, cách xét ngoài nguyệt chi và điều kiện Quan/Thực. Đối riêng danh sách 16 cặp can ngày–chi tháng trên ảnh 12. Không áp các lời phán quan chức, bệnh/tai hoặc đời sống. |
| 論偏官 | 46–48 / 005-22b–23b | Ba mệnh đề: định danh quan hệ, có chế/không chế trong ngữ cảnh chương, chế quá mức không tự động tốt. Không đổi tên cố định Thất Sát trên app hoặc dựng bộ chấm lực. |
| 論倒食 | 136–137 / 005-67b–68a | Hai mệnh đề ngắn về tên gọi và điều kiện chế/hợp; đọc các ví dụ chung quanh. Câu cụ thể “không có Thực chỉ luận Thiên Ấn” ở 68b **vẫn chỉ đối bản số**, vì ảnh 138 chưa có. Không nối hai cột không liên tiếp thành một lời trích. |

Những chữ 看/㸔 được ghi rõ là chuẩn hóa dạng chữ khi so, không âm thầm coi mọi dạng khác là lỗi. Chữ can 己 và chi 巳 trong danh sách được đọc theo ảnh/vai trò in, tách khỏi dạng của bản chép số cũ. Hồ sơ: `research/bazi-pattern-witness/MANUAL_READINGS.json`, `REQUESTS.json`, `commons-imageinfo.json`, các ảnh `p*.jpg`; bản số đối chiếu giữ SHA-256 `1ebdd92feaa57496b702f962ad6fafd4f19c17e98c38a94b40f626ef321dd997`.

## Phát hiện liên quan trực tiếp đến cách đọc tháng

Ảnh 12 nêu 16 trường hợp theo đủ mười can ngày. Đối bảng tàng can và quan hệ bằng **lunar-typescript 1.8.6 chạy thật** cùng HHC: cả 16 có đúng can Chính Quan trong chi tháng; **bốn trường hợp nằm ngoài bản khí**:

| Can ngày | Chi tháng | Can Chính Quan | Bản khí thực trong bảng đang dùng |
|---|---|---|---|
| Ất | Tỵ | Canh | Bính |
| Tân | Dần | Bính | Giáp |
| Nhâm | Ngọ | Kỷ | Đinh |
| Quý | Tỵ | Mậu | Bính |

Do đó không thể coi “tên quan hệ của bản khí = toàn bộ cách cục của tháng”. Đây là phản ví dụ cho một lối rút gọn, **không có nghĩa bốn trường hợp đã đủ mọi điều kiện lập Chính Quan cách**. Những tháng/ngày trong sách là dữ kiện hai trường, chưa phải lá số đầy đủ. Tệp kiểm có 16 lá số tính được làm fixture cho từng cấu trúc; đó là đầu vào hiện đại tìm để kiểm phần mềm, không là ngày sinh của người được sách nói đến.

## Kiểm thử

**91/91 kiểm chính đạt**: 7 kiểm nguồn, 13 nguồn/engine, 21 trình duyệt và 50 hồi quy. PDF và xem ảnh là chứng cứ bổ sung.

- Thực thi bản lunar-typescript 1.8.6 đã kiểm byte runtime. So 2.928 lá số năm nhuận 2020: 366 ngày × bốn giờ × hai lựa chọn can giờ Tý muộn, UTC+8. Đối trụ tháng/ngày trước rồi đối đủ can tàng tháng, thứ tự bản khí, quan hệ với Nhật chủ và vị trí lộ theo can thực của lá số HHC. Phủ đủ 12 chi tháng và mười quan hệ.
- Mọi trường `inspect()` cũ (kể cả khởi vận và mười chặng) khớp mô-đun trước phạm vi. Không dùng phép so tháng để tuyên bố mọi trụ giờ giữa các quy ước giống thư viện; sai khác mặc định giờ Tý muộn vẫn được tách rõ ở báo cáo trước.
- Quét lại một ngày chưa rõ giờ qua 1.440 phút vì phần hiển thị mới tiêu thụ dữ liệu này; khoảng vận và rào bất định giữ nguyên. Không dựng giờ khi thiếu, không đếm Nhật chủ thành lộ can.
- Cả 16 ví dụ nguồn có fixture thật, bốn phản ví dụ bản khí được giữ riêng; thẻ Chính Quan phụ được hiển thị đúng. Không có nhãn cách cục tự xác nhận.
- Kiểm thu gọn/mở, TXT/in phục hồi, lưu/mở hồ sơ, trụ bất định và sửa đầu vào xóa kết quả. Không lỗi JavaScript, không HTTP trong bản độc lập, không rò corpus/nguồn. Hồi quy chung 50 kiểm bao gồm năm công cụ, lưu/xuất và dữ liệu tương đương các mốc trước.
- PDF mẫu tám trang có đủ bản khí và hai can khác, vị trí, lời đọc và bảng vận; đã render và xem đủ, không cắt chữ. Giữ đủ một nhóm tháng và toàn bảng vận trên một trang khi vừa, form/ảnh đầu trang được ẩn.

Kết quả chi tiết: `qa/bazi-month-stems/ENGINE_RESULTS.json`, `SOURCE_RESULTS.json`, `BROWSER_RESULTS.json`, `PDF_RESULTS.json`; script cùng tên `verify-bazi-month-stems*`, `verify-bazi-pattern-source.py`, hồi quy `verify.mjs`.

## Phát hành và phần còn mở

HTML gốc/`v53`/`site`, ZIP web và ZIP nguồn đồng bộ theo manifest và kiểm bằng `verify-bazi-month-stems-release.py`. `site/` chỉ có `index.html`; nguồn sách và QA giữ ngoài site. Không đổi số phiên bản hoặc sửa snapshot cũ.

Ma trận mười mục chỉ có thêm dấu vết đối ảnh có mục tiêu cho Chính Quan, Thiên Quan và một phần Đảo Thực; chưa hiệu khảo hết ba mục, chưa đủ mười mục. Không thêm bộ nhận diện cách cục, thuật toán vượng suy hoặc dụng thần toàn cục. Các hướng Tử vi, nhà ở và Kinh Dịch vẫn mở theo WORK_STATE; phạm vi tháng này đã xong, không lặp 16 cặp/2.928 lá số để tăng lượt kiểm.
