# Hiệu khảo ảnh Kinh Dịch: 7 vị trí V49 và bản đồ 64 quẻ

Ngày thực hiện: 26-10-2026. Đây là tài liệu nghiên cứu nội bộ, không dùng làm trang web cho người xem.

## Phạm vi đã thực hiện

- Tải nguyên byte hai PDF của *周易四卷* trên Wikimedia Commons, do Commons ghi nguồn National Center for Philosophy and Social Sciences Documentation (NCPSSD), barcode 71014695/71014696. Tổng 209 trang PDF gồm bìa, lời tựa, thượng/hạ kinh và các phần khác.
- Trích đúng byte ảnh JPEG nhúng trong cả 209 trang; mỗi trang có đúng một ảnh. PDF không có lớp văn bản trích xuất được. Không dùng OCR để coi là đã đọc sách.
- Xác định trực tiếp trên ảnh một trang mốc cho đủ **64/64 quẻ**. Ma trận này là chỉ đường tới ảnh, không phải chứng nhận đã hiệu khảo sáu hào của từng quẻ. Có một cặp ảnh chụp trùng nội dung tại quyển 2 PDF p46/p47, vì vậy không áp dụng công thức cộng số trang.
- Chép và đối chiếu đầy đủ **7/384 hào thông thường**, đúng bảy vị trí V49 đã phân loại khác dạng chữ. **377/384 hào còn lại chưa được hiệu khảo trên ảnh trong phạm vi này.** 用九 của 乾 và 用六 của 坤 không nằm trong mẫu số 384 và cũng chưa hiệu khảo.

## Định danh và byte đã giữ

1. [Commons - 第一册](https://commons.wikimedia.org/wiki/File:NCPSSD-71014695_%E5%91%A8%E6%98%93%E5%9B%9B%E5%8D%B7_%E7%AC%AC%E4%B8%80%E5%86%8C.pdf): 97 trang, **28.895.802 byte**, SHA-256 `a35643bec19d116a0ce1323a4afcb6ac7d8cb247618adb0edc2531696ab64bb5`.
2. [Commons - 第二册](https://commons.wikimedia.org/wiki/File:NCPSSD-71014696_%E5%91%A8%E6%98%93%E5%9B%9B%E5%8D%B7_%E7%AC%AC%E4%BA%8C%E5%86%8C.pdf): 112 trang, **35.731.493 byte**, SHA-256 `9a810330902aa4230fd0e55db746e63f123aaeb7ae78899488cb62879ee26b2d`.

Đầu kinh ở quyển 1 PDF p22 ghi **朱熹本義**. Commons mô tả tác giả **（宋）朱熹注**, niên đại **1874**, số tra cứu **經104/2540**, bookid GJ1152645/GJ1152646. Nguồn này là ảnh một truyền bản có định danh; không phải chứng minh văn bản do Chu Hy trực tiếp viết hoặc ảnh bản in Tống.

**Xung đột metadata được phát hiện:** Commons ghi **江南書局刻本**, nhưng đề ký trong ảnh quyển 1 PDF p4 đọc rõ **同治十三年甲戌／江西書局開雕**. Ảnh nguyên và `evidence/imprint-crop.png` giữ nguyên để xét lại. Không âm thầm sửa một lớp theo lớp kia. Năm 同治十三年 và 甲戌 phù hợp với 1874; tên cơ sở khắc vẫn được ghi là xung đột thư mục.

Commons dẫn đường tới danh mục chính thức NCPSSD bằng barcode. Trình đọc web không truy cập được danh mục đó trong lần nghiên cứu này. PDF được tải từ máy chủ Wikimedia, **không tuyên bố byte đã tải trực tiếp từ NCPSSD**. Raw JSON API mô tả, wikitext và template liên kết tới cơ quan được giữ cùng URL, thời gian, độ dài và SHA-256. Commons ghi các scan là public domain.

## Bảy hào đã đọc thực tế

Chép chữ Hán không tái tạo dấu câu hiện đại; bỏ nhãn hào và phần chú để đối chiếu. Cột trang dùng số trang PDF **bắt đầu từ 1**, có tính bìa/lời tựa. Mỗi mục trong `facsimile-audit.json` có đường dẫn ảnh và SHA-256 ảnh riêng.

| Quẻ, hào | Quyển / PDF | Chữ đọc trên ảnh | Kết quả đối với V49 |
|---|---|---|---|
| 29 坎, 六四 | 1 / p94 | 樽酒簋貳用缶納約自牖終无咎 | **納**, ngoài cặp 内/內 trước đó; còn có 樽 thay 尊. Khớp phương án dị văn được chú ở Wikisource, không khớp nguyên chuỗi nền của cả hai bên. |
| 38 睽, 上九 | 2 / p18 | 睽孤見豕負塗載鬼一車先張之弧後說之弧匪寇婚媾往遇雨則吉 | In **塗**, cùng chữ với Wikisource tại vị trí này. |
| 51 震, 上六 | 2 / p45 | 震索索視矍矍征凶震不于其躬于其鄰无咎婚媾有言 | In **无**, cùng chuỗi Hán của app. |
| 53 漸, 初六 | 2 / p49 | 鴻漸于干小子厲有言无咎 | In **无**, cùng chuỗi Hán của app. |
| 53 漸, 六四 | 2 / p50 | 鴻漸于木或得其桷无咎 | In **无**, cùng chuỗi Hán của app. |
| 55 豐, 上六 | 2 / p54 | 豐其屋蔀其家窺其戶闃其无人三歲不覿凶 | In **覿**, cùng chuỗi Hán của Wikisource; vẫn in 无 ở 无人. |
| 59 渙, 九二 | 2 / p61 | 渙奔其机悔亡 | In **机**, cùng chuỗi Hán của app. Chú âm kề cạnh ghi **机音几**. |

Đếm đối sánh NFC sau bỏ dấu câu/khoảng trắng, **không gộp dị thể**: 4 chuỗi trùng app, 2 chuỗi trùng Wikisource, 1 chuỗi không trùng chuỗi nền của bên nào. Đây không phải thang điểm chất lượng toàn bộ app: chỉ là bảy vị trí đã chọn vì khác dạng ở V49.

## Ý nghĩa có thể áp dụng

- Không đổi hàng loạt 无 thành 無 hoặc 机 thành 機 chỉ vì một trang điện tử hiện đại dùng dạng đó. Scan thế kỷ XIX đã dùng 无 và 机 ở các vị trí vừa đọc.
- V49 “7 khác dạng” đúng trong phạm vi so sánh hai chuỗi V49; không được mở rộng thành “bảy lỗi đã sửa” hoặc “mọi ấn bản thống nhất”. Với 坎六四, thêm witness ảnh tạo ra quan hệ dị văn phức tạp hơn cặp 内/內.
- Không sửa corpus hay chức năng web trong gói nghiên cứu này. Khi quyết định một bản văn hiển thị, cần ghi chính sách chọn truyền bản, lưu các chứng tích còn lại riêng và giữ chú giải nội bộ. Người dùng web vẫn chỉ nhận kết quả và diễn giải.

## Tệp để nối tiếp và kiểm tra

- `manual-readings.json`: biên chép trực tiếp 7 hào, vị trí nửa trang, nhận xét chữ in, giới hạn đọc.
- `manual-hexagram-anchors.json`: 64 trang mốc đã nhận diện bằng mắt và đoạn nhận diện. Không suy ra tất cả trang mở đầu.
- `facsimile-audit.json`: gắn chữ V49, URL/revision/SHA nguồn V49, SHA ảnh scan, kết quả đối sánh riêng từng witness, metadata và thống kê giới hạn.
- `hexagram-64-page-matrix.csv`: ma trận 64 quẻ tới ảnh/trang mốc.
- `yao-384-collation-queue.json`: **384** vị trí có trạng thái rõ: 7 đã đọc/đối chiếu, 377 chưa; không suy ra hoàn thành từ việc có PDF.
- `extracted-pages.json`: SHA-256 của **209** ảnh JPEG trích byte; contact sheet chỉ là ảnh dẫn đường đã co nhỏ.
- `*.provenance.json` và `description-provenance.json`: URL tải, byte, SHA-256, metadata byte gốc và thời điểm lấy.

Tái lập từ thư mục gốc dự án (Node có sẵn; Python cần pypdf/Pillow):

```powershell
node v53/scripts/full-yi-fetch.mjs 'File:NCPSSD-71014695 周易四卷 第一册.pdf' 'File:NCPSSD-71014696 周易四卷 第二册.pdf'
node v53/scripts/full-yi-metadata.mjs
python v53/scripts/full-yi-extract.py
node v53/scripts/full-yi-audit.mjs
```

`full-yi-fetch.mjs` tải lại bản máy chủ đang phục vụ vào cùng tên; khi nghiên cứu một lần khác, lưu snapshot thư mục này trước để tránh thay thế chứng tích của lần này. Tái lập **chỉ kiểm tra chứng tích đã lưu**, không tải mạng lại: chạy riêng `node v53/scripts/full-yi-audit.mjs`.

## Kiểm tra đã chạy

`node v53/scripts/full-yi-audit.mjs` thành công: xác minh byte/SHA của 2 PDF, 2 metadata imageinfo và 3 JSON wikitext/template; 209 SHA ảnh; 64 ID quẻ duy nhất có ảnh/trang thật; 384 vị trí; đúng 7 hào mục tiêu độc lập xuất phát từ nhóm `explicit-glyph-variant` của V49. Bộ kiểm tra này kiểm tra tính toàn vẹn và liên kết chứng tích; không tự thay thế việc đọc cổ tự bằng mắt.

Phần chưa hoàn tất là hiệu khảo từng chữ của 377 hào còn lại, 用九/用六 và đối chiếu thêm truyền bản độc lập. Không gọi đây là đã khai thác hết kiến thức toàn bộ Kinh Dịch hoặc hết kho sách.
