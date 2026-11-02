# Hoàn thành bốn mục V53 — 26/10/2026

Theo yêu cầu “làm tiếp cho tới khi xong 4 mục”, bản V53 hiện tại đã tích hợp đủ bốn phạm vi dưới đây. Không mở V54, không xuất bản. Nguồn, corpus và đối chiếu giữ trong tài liệu nội bộ, ngoài `site/` và gói web. Bản trước giữ tại `../archives/v53-before-four-items/`.

| Mục | Kết quả người dùng nhận được | Kiểm chứng chính |
|---|---|---|
| Kinh Dịch | Đủ 384 hào thường có lời gợi mở riêng; chọn hào động nào đọc đúng hào đó. Hai lời bổ sung Càn–Khôn chỉ xuất hiện khi đủ sáu hào động. | 372 lời mới được biên tập từng hào từ bản số đã lưu; 64 hash nguồn giữ nguyên; 4.096 tổ hợp chọn vị trí đúng. |
| Bát tự | Đọc Thập thần của can lộ và tàng can từng chi, nhận diện bản khí và giải thích các quan hệ hiện diện. Chưa biết giờ thì không dựng trụ giờ; trụ còn bất định thì tạm dừng đọc quan hệ. | Đọc ảnh trang 54/trang in 三六 của bản Uyên Hải có thư mục xác định; 12 tập hợp tàng can; 100 cặp can khớp bảng thư viện chạy thật. |
| Nhà ở | Thêm “Đọc hướng từ số đo” trong Hướng theo tuổi: chọn đối tượng, góc, bất định, Bắc thật/Bắc từ và độ từ thiên. Giữ hai hướng nếu phép đo chạm ranh. Bảy mục bố trí phòng vẫn hoạt động. | Đọc đủ tám đồ hình NDL; 64/64 nhãn hướng khớp engine; kiểm biên, vòng 0/360, hiệu chỉnh Bắc từ và lưu/khôi phục số đo. |
| Tử vi | Nút “Xem vận hạn theo ngày” ngay đầu kết quả; chọn ngày để đọc đại hạn, lưu niên, lưu nguyệt, Tiểu hạn riêng, Tứ Hóa năm và 12 chặng đại hạn. Ngày xem lưu cùng hồ sơ, xuất TXT và in. | 178 lần gọi horoscope của iztro 2.6.2 thật trong hai bộ so, có ghi rõ điều chỉnh chính sách tháng nhuận, đồng hạn và khác biệt Nhâm Hóa Khoa. |

## Cách mở các phần mới

Mở `../Huyen_Hoc_Cac.html` hoặc `Huyen_Hoc_Cac.html` trong thư mục này. Tại Tử vi, lập lá số rồi bấm **Xem vận hạn theo ngày**; ngày xem để trống cho đến khi người dùng chọn. Bát tự hiển thị phần Thập thần & tàng can sau kết quả chính. Hướng nhà → Hướng theo tuổi có phần đọc số đo; Bố trí các phòng giữ ở `#home`. Gieo quẻ/nhập hào như trước, phần lời riêng xuất hiện theo hào động.

## Kiểm thử

| Lệnh | Số kiểm đạt | Phạm vi |
|---|---:|---|
| `node scripts/verify-four-engine.mjs` | 14/14 | 384 hào, 4.096 tập hào động, byte engine, 209 tệp iztro, 100 cặp can, 12 bảng tàng can, 64 hướng, đo góc, 72 horoscope, ranh năm âm và lịch nhạy. |
| `node scripts/verify-fortune-policies.mjs` | 7/7 | 106 horoscope bổ sung, ba quy ước tháng nhuận, ranh ngày 15/16, Tiểu hạn đủ 12 chi/hai giới tính, khác biệt Tứ Hóa, ngày Tý muộn. |
| `node scripts/verify-four-browser.mjs` | 47/47 | Luồng người dùng bốn mục, nút vận hạn, lưu/mở/TXT/in, xóa kết quả cũ khi sửa, 320/390/768/1440 px, không HTTP/nguồn riêng trong DOM. |
| `node scripts/verify.mjs` | 50/50 | Hồi quy năm công cụ, so bộ tính V52 thật, lưu/xóa hồ sơ, xuất, lịch và bố cục. |
| `node scripts/verify-home-guide.mjs` | 40/40 | Bảy phòng, ghi vị trí/quan sát, TXT/in, điều hướng và điện thoại. |
| `node scripts/verify-experience.mjs` | 36/36 | Năm thẻ công cụ, tranh/chữ/tương phản, bố cục, riêng tư, in và không phụ thuộc mạng. |

Tổng **194/194** phép kiểm trong sáu bộ. Số tổ hợp/so sánh bên trong từng phép kiểm được ghi riêng, không cộng thành số ca giao diện. Một phép hồi quy cũ đếm toàn bộ `.reading-card` đã được giới hạn vào nhóm đọc Nhật chủ gốc sau khi giao diện có thêm thẻ Thập thần; kết quả Nhật chủ không bị thay đổi. Bộ kiểm 12 hào trước đây là mốc lịch sử; bộ bốn mục thay phần kỳ vọng “62 quẻ dùng lời chung” bằng kiểm 64 quẻ có lời riêng.

Các kết quả JSON và ảnh ở `qa/four-items/`, hồi quy ở `qa/`. Đã nhìn ảnh máy tính/điện thoại và kiểm in phần vận hạn có ngày chọn, ẩn biểu mẫu. Engine lịch/phép an sao trong `engine.js` giữ nguyên byte so với bản trước bốn mục. Phần mới nằm trong các mô-đun nội dung, quan hệ, thời gian và đo hướng.

## Giới hạn cần hiểu đúng

384 lời là gợi mở biên tập theo từng hào, không phải bản dịch sát chữ hoặc hiệu khảo ảnh trọn bộ. Bát tự chưa chấm vượng suy/chọn dụng thần. 64 nhãn NDL xác minh bảng hướng của một bản Nhật chuyển biên, chưa chứng minh quy ước năm sinh hoặc tác dụng khi đặt phòng. Vận hạn là luồng đọc chủ đề cung theo thời gian, chưa phải luận tổng hợp tất cả sao hoặc dự đoán sự kiện.

iztro dùng cách chia tháng nhuận từ ngày 16; HHC giữ cả ba lựa chọn và ghi hiệu chỉnh khi so khác chính sách. Trước đại hạn đầu, chương trình ghi chưa có đại hạn thay vì lấy đồng hạn của iztro. Năm Nhâm giữ Thiên Phủ Hóa Khoa theo bảng Toàn Thư đang dùng, khác Tả Phù của iztro. Các khác biệt này là dữ kiện trong báo cáo, không được gọi là khớp thô toàn bộ.

Nguồn Uyên Hải mới có bản scan, metadata thư viện, byte HTTPS/SHA và ảnh trang đã đọc; Tam Mệnh Thông Hội ghim commit, phân biệt tàng can cố định với bảng phân ngày tư lệnh. Chi tiết và mức chứng cứ ở `research/four-items/SOURCE_NOTES.md`, `BAZI_SOURCE_AUDIT.json`, `FORTUNE_RULE_NOTES.json` và `COVERAGE_UPDATE.json`. Chưa áp dụng hết kho sách, chưa xác thực mọi truyền bản hoặc năng lực tiên đoán.

## Gói phát hành

`scripts/build.mjs` tạo HTML độc lập, `scripts/package.py` đồng bộ HTML gốc/HTML V53/site và hai ZIP. `site/` chỉ có `index.html`; gói web chỉ có `index.html` và `HUONG_DAN.md`. Bản scan, chứng cứ, báo cáo và kiểm thử chỉ nằm trong gói nguồn. Hash cuối nằm tại `PACKAGE_MANIFEST.json`. Không tự gửi dữ liệu người dùng, không xuất bản mạng; các bản V46–V52 và snapshot trước thay đổi được giữ lại.
