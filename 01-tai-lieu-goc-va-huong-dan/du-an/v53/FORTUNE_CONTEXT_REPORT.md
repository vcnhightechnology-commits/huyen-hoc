# Đọc vận hạn cùng bối cảnh sao gốc — V53, 26/10/2026

Kết quả đại hạn/lưu niên/lưu nguyệt nay ghi rõ **các chính tinh thực sự nằm ở cung gốc đang được đọc**, nhãn trạng thái theo bảng hiện dùng, và Tứ Hóa của năm được chọn nếu sao mục tiêu nằm tại chính cung đó. Mở “Đọc gợi mở về các sao” để đọc thêm; mặc định thu gọn để ba chặng dễ lướt. TXT và in tự mở đủ rồi trả lại trạng thái.

Hai chính tinh đồng cung có thể nhận lời gợi mở phối hợp đã biên tập trước đây; không gom sao tam hợp thành đồng cung. Cung vô chính diệu có câu riêng và ghi đúng cung đối diện, không chuyển sao thành sao tọa thủ. Trước đại hạn đầu không dựng một cung khác thay thế. Việc đổi ngày/chọn tháng/mở hồ sơ tính lại toàn bộ phần bối cảnh.

Sao đang đọc là sao gốc trên lá số, không tự biến thành sao lưu niên/lưu nguyệt di chuyển. Nhãn Tứ Hóa trong phần mới thuộc **năm âm đang xem**, không phải một bảng Tứ Hóa mới cho mỗi chặng. Các dị bản Canh/Nhâm và cung/tuổi khởi hạn vẫn giữ trạng thái riêng; phần tính hạn không đổi.

## Nghiên cứu nguồn mới

Tái dùng [hồ sơ/manifest công khai của **国立公文書館**](https://www.digital.archives.go.jp/file/1078787), mã子060-0001, tác phẩm *新鋟希夷陳先生紫微斗数全書*. Lấy thêm3ảnh IIIF ở canvas90–92, HTTP200/TLS hợp lệ, giữ nguyên bodyJPEG2200×1659 vàSHA256 trong `research/fortune-context/REQUESTS.json`. Đây là3ảnh mới của **cùng một bản in đã dùng**, không tính là3tác phẩm hoặc một nhân chứng độc lập mới. Nguồn/ảnh/câu chữ không đưa vào site.

Đọc có mục tiêu4đơn vị:

1. Canvas90phải: bốn nhóm vị trí củaTửVi và sao đồng cung — Dần/Thân vớiThiênPhủ, Tỵ/Hợi vớiThấtSát, Thìn/Tuất vớiThiênTướng, Sửu/Mùi vớiPháQuân. Chỉ mã hóa mệnh đề vị trí; không nhận các lời tài/quan/birth-can phía sau là đã kiểm chứng.
2. Canvas90trái: hai câu mở đầu mụcTửVi nhập hạn. Đoạn có điều kiện sao/phối hợp và hạn, chưa đủ làm căn cứ dự báo sự kiện hoặc di chuyển sao gốc.
3. Canvas91trái: sáu nhóm địa chi củaThiênCơ, có các mệnh đề đồng cung vớiCựMôn/TháiÂm/ThiênLương. Giữ nguyên bối cảnh của danh sách, không tự đổi bảng trạng thái theo một câu.
4. Canvas92trái: mở đầuTháiDương và lời về các sao hội hợp. Đọc vai trò/từ khóa liên hệ; không sao chép mô tả ngoại hình, tuổi thọ hoặc giàu nghèo vào web.

`MANUAL_READINGS.json` có vị trí nửa trang, chuỗi làm việc, phạm vi đọc và điều kiện bị loại khỏi thuật toán. Không gọi3ảnh là đã hiệu khảo toàn bộ6trang hoặc cả4quyển. Một số chữ mô tả trạng thái khác bảng cũ: đoạnTửVi dùng旺地 ởDần/Thân, còn bảng trước ghi廟ởDần; danh sáchThiênCơ ởMão/Dậu dùng陷地, trong khi bảng phần mềm đang chọn là旺/旺 và bảng ảnh trước là旺/廟. Từ ngữ văn xuôi/bảng và điều kiện đi kèm được lưu riêng; không ép chúng thành một thang chung, không coi cùng một ấn bản là nhân chứng thứhai giải quyết dị bản.

Diễn giải công khai tái dùng14lời sao và22lời phối hợp đã biên tập; đây là lời chiêm nghiệm hiện đại, không phải bản dịch nguyên câu phú vừa đọc. Độ khớp vị trí không kiểm chứng các mệnh đề tiên đoán của cổ bản.

## Thực thi và kiểm thử

**149/149 kiểm tự động đạt:**11kiểm engine/nguồn mới,19kiểm trình duyệt mới,50hồi quy lõi,47hồi quy bốn mục và22hồi quy bảng tháng.

-Góiiztro2.6.2 thật giữ209/209tệp khớp tarball đã lưu vàintegrity. Không tải lại npm, không thay engine bằng mã giả.
-14điều kiện cung/sao của hai nhóm đoạn ảnh được đạt tới trong1.440lá số mẫu;1.770phép kiểm đồng vị trí khớp. Đây là14điều kiện địa chi/co-star, không phải14quy tắc tiên đoán được chứng minh.
-72horoscope iztro thật,24lá số×3ngày xem:216cung đại/năm/tháng và tập sao gốc khớp.41cung rỗng giữ riêng cung đối diện;70gắn kết TứHóa chỉ xuất hiện ở đúng vị trí sao mục tiêu. Các mẫu này là hạn người lớn; không mở rộng phép so sang童限 củaiztro.
-Giữ riêng NhâmPhủKhoa củaHHC; không ép theo TảKhoa mặc định củaiztro. Vận đầu chưa có và tham chiếu cung sai được xử lý rõ. Đọc bối cảnh không sửa bất kỳ lá số nào; vẫn đúng khi đảo thứ tự mảng cung.
-UIlưu/mở/đổi ngày/chọn tháng/TXT/in, thu gọn/phục hồi,320/390/768/1440px:0lỗiJavaScript,0HTTP củaHTMLđộc lập. PDF8trang giữ ba bối cảnh cùng toàn bảng tháng; các thẻ hạn giữ liền khi đủ chỗ. Đã xem cả8trang và ảnh điện thoại.

Mã mới `fortune-context.js`/`.css`; `fortune.js` chỉ gọi phần render và thêm nhãn phân lớp. Hàm tính`inspect` được đối chiếu nguyên byte với snapshot. `engine.js`, `app.js`, `content.js`, `tuvi-context.js`, `fortune-months.js`, Bát tự và mặt bằng giữ nguyên byte. Nguồn/QA ngoài site; đồng bộHTMLgốc/V53/site và haiZIP cùngV53 sau kiểmmanifest. Snapshot trước phạm vi: `archives/v53-before-fortune-context/`. Không xuất bản.

Tái kiểm: `node v53/scripts/verify-fortune-context.mjs`, `node v53/scripts/verify-fortune-context-browser.mjs`, `python v53/scripts/verify-fortune-context-release.py --no-write`. Dữ liệu thực thi ở `qa/fortune-context/`; giới hạn/nguồn/khác biệt được giữ trong `research/fortune-context/`.

## Byte phát hành

HTML661.904byte, SHA-256`99451380b729a68e5a0cf3dacf7b16134ced191bebe3d9aca85988f8a65a4635`; ba bản gốc/V53/site đồng nhất,908tệp trongmanifest. Góiweb chỉHTML/hướngdẫn. Gói nguồn giữ tài liệu/ảnh/QA; kiểm đồng nhất ở`qa/fortune-context/RELEASE_RESULTS.json`.
