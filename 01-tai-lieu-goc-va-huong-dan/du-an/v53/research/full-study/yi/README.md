# Kinh Dịch: hiệu khảo đủ 384 hào trên ảnh một bản khắc

Cập nhật tiếp 26/10/2026: đối thêm16vị trí và5đoạn chú in đen trong một ảnh sách khác, có niên đại/định danh ấn bản còn điều kiện. Xem [PROVENANCE.md](../../yi-second-witness/PROVENANCE.md) và [báo cáo](../../../YI_COMMENTARY_REFINEMENT_REPORT.md). Bốn lời đọc Việt được làm rõ; audit384hào/corpusHán của phạm vi ở dưới vẫn nguyên byte. Không cộng16vị trí thành lượt đọc384hào thứhai.

Ngày hoàn tất phạm vi: 26-10-2026. Tài liệu nghiên cứu nội bộ, không đưa lên web người xem.

## Phạm vi đã hoàn tất

Đã đọc trực tiếp, chép và đối chiếu **384/384 hào thông thường**, đủ **64/64 quẻ**, từ hai册 của cùng một bản *周易四卷／朱熹本義*. Đọc riêng **乾用九** và **坤用六** ngoài mẫu số 384. **OCR-only: 0**. Mỗi hàng có nguyên chuỗi Hán không dấu câu, nhãn hào, trang PDF và SHA-256 ảnh. Một lượt đọc bằng mắt của một người đọc, có rà chọn lọc; không phải hai người đọc độc lập toàn văn.

Hai PDF là **hai册 của một ấn bản**, không phải hai chứng nhân lịch sử độc lập. Đã hoàn tất lời 384 hào và hai lời Dụng; chưa chép toàn bộ chú giải/Thập Dực và không suy ra đã khai thác hết kiến thức Kinh Dịch hoặc kho sách. Không thay chữ corpus hoặc lời gợi mở trên web trong gói này.

## Nguồn và byte được giữ

1. [Commons — 第一册](https://commons.wikimedia.org/wiki/File:NCPSSD-71014695_%E5%91%A8%E6%98%93%E5%9B%9B%E5%8D%B7_%E7%AC%AC%E4%B8%80%E5%86%8C.pdf): 97 trang, 28.895.802 byte; SHA-256 `a35643bec19d116a0ce1323a4afcb6ac7d8cb247618adb0edc2531696ab64bb5`.
2. [Commons — 第二册](https://commons.wikimedia.org/wiki/File:NCPSSD-71014696_%E5%91%A8%E6%98%93%E5%9B%9B%E5%8D%B7_%E7%AC%AC%E4%BA%8C%E5%86%8C.pdf): 112 trang, 35.731.493 byte; SHA-256 `9a810330902aa4230fd0e55db746e63f123aaeb7ae78899488cb62879ee26b2d`.

PDF tải từ Wikimedia; metadata Commons ghi nguồn NCPSSD, barcode 71014695/71014696, bookid GJ1152645/GJ1152646,（宋）朱熹注, 1874, 經104/2540. Danh mục trực tiếp NCPSSD không truy cập được trong lần này: không tuyên bố byte tải trực tiếp từ cơ quan. Metadata/wikitext/template dẫn nguồn/provenance có URL, byte, SHA riêng. Commons ghi scan public domain.

**Xung đột thư mục còn mở:** Commons ghi 江南書局刻本, nhưng đề ký ảnh册1 PDF p4 đọc **同治十三年甲戌／江西書局開雕**. Giữ cả hai lớp bằng chứng. Năm 1874 phù hợp với đề ký; tên nhà khắc cần xác minh thư mục độc lập.

209 JPEG là byte ảnh gốc nhúng trong 209 trang PDF; mỗi trang một ảnh, không có lớp văn bản trích xuất được. Contact sheet chỉ để điều hướng. 64 mốc quẻ có thể là một trang trong quẻ, không mặc định là trang đầu. 册2 p46/p47 chụp trùng nội dung 艮, không đếm hai lần.

## Cách đọc và kết quả đối chiếu

Đọc cột từ phải sang trái, từ trên xuống; chỉ chép lời hào cỡ chữ lớn, loại nhãn, lời Tượng và chú. Chữ in biểu diễn bằng Unicode, không tái tạo kiểu khắc/dấu câu. Mỗi checkpoint hoàn tất sáu hào của từng quẻ; 12 checkpoint giữ đủ 384 chuỗi.

So với corpus V49 và nguyên chuỗi Wikisource lưu ở V49 bằng NFC, bỏ dấu câu/khoảng trắng, **không gộp dị thể**: **327/384** trùng app, **325/384** trùng Wikisource; **57** hàng khác app, **59** hàng khác Wikisource, **61** hàng khác ít nhất một bên, **55** hàng khác cả hai. Số khác chuỗi không đồng nghĩa số lỗi đã chứng minh. App/Wikisource cũng không được tính là hai truyền bản độc lập.

Rà ảnh phóng lớn sửa một lỗi chép nháp: 艮九三 là **厲熏心**, không phải 厲薰心. Lịch sử sửa/lượt rà chọn lọc trong `manual-review-notes.json`. `PARENT_SPOT_REVIEW.json` ghi lượt rà độc lập riêng năm chuỗi, không phải đọc lại cả 384.

## Khác văn từ đáng chú ý

| Vị trí | Chữ trên ảnh | Chuỗi V49 | Trang PDF |
|---|---|---|---|
| 9.3 | 輿說輻 | 車說輹 | 册1 p53 |
| 9.6 | 尚德載 | 尚得載 | 册1 p54 |
| 14.4 | 匪其彭 | 匪其尫 | 册1 p64 |
| 16.4 | 朋盍簪 | 朋盍戠 | 册1 p68 |
| 23.6 | 君子得輿 | 君子德車 | 册1 p82 |
| 26.3 | 利艱貞曰閑輿衞 | 利艱貞吉日閑輿衛 | 册1 p88 |
| 29.4 | 樽酒…納約 | 尊酒…内約／內約 | 册1 p94 |
| 34.4 | 大輿之輹 | 大轝之腹 | 册2 p10 |
| 35.5 | 失得勿恤 | 矢得勿恤 | 册2 p12 |
| 41.1 | 已事遄往 | 祀事遄往 | 册2 p23 |
| 47.4 | 來徐徐…金車 | 來荼荼…金轝 | 册2 p36 |
| 50.4 | 其形渥 | 其刑渥 | 册2 p42 |
| 52.3 | 列其夤厲熏心 | 裂其夤厲閽心 | 册2 p46 |
| 52.5 | 言有序 | 言有孚 | 册2 p48 |
| 59.1 | 用拯馬壯吉（hết lời hào） | còn 悔亡 sau 吉 | 册2 p61 |
| 61.4 | 月幾望 | 月既望 | 册2 p65 |

Ngoài khác văn từ còn có 恒/恆, 无/無, 羣/群, 甕/瓮, 衞/衛, 朶/朵. 渙九二 in **机**, chú **机音几**: không thay máy móc 机 thành 機. Bảy vị trí V49 ban đầu đã được chứng kiến trên ảnh **của bản này**; không suy ra mọi truyền bản thống nhất. Báo cáo ban đầu giữ ở `README_INITIAL_SEVEN.md` và `facsimile-audit.json` như snapshot cũ.

用九 in **見羣龍无首吉**, 册1 p25; 用六 in **利永貞**, 册1 p36. Ghi riêng ngoài mẫu số 384.

## Tệp hiện hành và tái kiểm tra

- `yao-384-collation-queue.json`: đủ 384 hàng, chữ/nhãn/trạng thái/trang/SHA và đối sánh.
- `yao-384-transcription.csv`: bản tra cứu 384 hàng; `variant-review.csv`: 61 hàng khác ít nhất một chuỗi điện tử.
- `full-384-progress.json`, `checkpoint-01.json`…`checkpoint-12.json`: biên chép theo lô.
- `supplementary-readings.json`: 用九/用六; `facsimile-384-audit.json`: audit hiện hành, SHA PDF/ảnh/checkpoint, thống kê và giới hạn.
- `manual-review-notes.json`, `extracted-pages.json`: cách đọc/sửa nháp và 209 hash ảnh gốc.
- `manual-hexagram-anchors.json`, `hexagram-64-page-matrix.csv`: 64 mốc bằng ảnh.
- `README_INITIAL_SEVEN.md`, `facsimile-audit.json`, `yao-384-collation-queue.initial-seven.json`: snapshot bảy hào ban đầu, không phải số hiện hành.

Tái kiểm tra ngoại tuyến từ gốc dự án, không tải lại:

```powershell
node v53/scripts/full-yi-progress.mjs
node v53/scripts/full-yi-final-audit.mjs
```

PASS: đủ 384 vị trí duy nhất/sáu hào mỗi quẻ/64 quẻ; hai lời bổ sung riêng; 12 hash checkpoint; 209 hash ảnh; hai hash PDF. Kiểm tra máy xác minh liên kết và byte, không thay thế phán quyết dị bản.

Nghiên cứu tiếp theo: chọn thêm ấn bản định danh để xét trước các hàng khác văn từ; đọc chú giải theo câu hỏi cụ thể và ghi rõ là diễn giải. Việc đọc hết lời hào không biến lời cát/hung thành sự kiện thực nghiệm hoặc dự báo chắc chắn về đời người.
