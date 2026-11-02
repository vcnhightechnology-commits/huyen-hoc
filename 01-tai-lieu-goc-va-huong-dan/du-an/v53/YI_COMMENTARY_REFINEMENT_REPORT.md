# Kinh Dịch: đối ảnh mục tiêu và làm rõ bốn lời đọc

Hoàn tất phạm vi ngày26/10/2026, cùngV53. Nghiên cứu và báo cáo giữ ngoài site.

## Kết quả cho người xem

Chỉnh đúng bốn lời đọc theo vị trí, dùng chung trong phần hào đang động và phần đọc đủ sáu hào:

- **Bác, hào6:** thêm hình ảnh chiếc xe nâng đỡ/người đồng hành đã bị lược mất; vẫn giữ quả còn lại và mái che.
- **Đại Súc, hào3:** làm rõ rèn tập, phòng vệ và thận trọng khi tiến, tránh hiểu thành cứ có khí thế thì nên tiến.
- **Tổn, hào1:** làm rõ giúp kịp lúc nhưng phải xác nhận nhu cầu và cân mức đóng góp. Đây là ứng dụng hiện đại được biên tập, không áp quan hệ trên/dưới của cổ văn thành nghĩa vụ của người dùng.
- **Cấn, hào3:** thay câu mô tả rách cơ lưng theo nghĩa đen bằng hình ảnh cố dừng đến bế tắc, tự chế và điều chỉnh cách nghỉ. Không suy thành bệnh trạng hay sự kiện chắc chắn.

Tiêu đề,380lời đọc thường khác, hai lờiDụng, lựa chọn hào và phép gieo giữ nguyên. Chữ corpus Hán, lịch/an sao và các phép tính khác giữ nguyên byte. Giao diện chỉ có lời gợi mở và gợi ý thực hành; không thêm nguồn, dị văn, ghi chú hiệu khảo hoặc danh mục sách vào trang người xem.

## Nguồn và mức xác minh

Tải thành công PDF [Commons NCL-00037 周易本義](https://commons.wikimedia.org/wiki/File:NCL-00037_%E5%91%A8%E6%98%93%E6%9C%AC%E7%BE%A9.pdf):95.666.503byte,325trang, SHA-256`83472d8eb932ad44de18a552e54304947a01f994abbda5b534440db01026fa31`. SHA-1khớp API công khai. Tải được cả biểu ghiNCL00037/rarecatx0205789 và danh mục liên hợp; năm phản hồiHTTPS200/TLS/headers/byte/hash được giữ tại `research/yi-second-witness/REQUESTS.json`. PDF doWikimedia cung cấp, không gọi là tải bytePDF trực tiếp từNCL.

Danh mụcNCL ghi `乾隆庚午(十五年, 1710)` nhưng trường trung lịch là乾隆15; liên hợp ghi1750 tại日期,Commons ghi1750. Chưa thấy đề ký năm in trong trang đã đọc. Giữ mâu thuẫn và mức định danh có điều kiện trong [PROVENANCE.md](research/yi-second-witness/PROVENANCE.md); không coi quy đổi1750 là kiểm chứng đề ký, không gán chú đỏ cho người viết chỉ bằng metadata. Đây là nhân chứng ảnh riêng thuộc cùng họ chú giảiChuHy, chưa chứng minh phả hệ độc lập. Nó cũng không giải quyết江南/江西 của bản1874.

PDFmetadata nêu2675×1937 nhưng JPEG thực trích để đọc là1713×1240.90raster được chọn để điều hướng và đọc mục tiêu cóhash; **không gọi là90trang đã hiệu khảo**.8crop phóng lớn được kiểm đúng pixel vớiảnhcha, chỉ là dẫn xuất. KhôngOCR; không vượt xác thực hoặc hạn chế truy cập của cơ quan.

Đọc trực tiếp16vị trí:9.3/9.6/14.4/16.4/23.6/26.3/29.4/34.4/35.5/41.1/47.4/50.4/52.3/52.5/59.1/61.4.15chuỗi trùng bản chép ảnh1874 sauNFC/bỏdấucâu,1khác ở26.3: giữ `日` của lời hào và ghi riêng chú `日當為曰`, so với `曰` trong biên chép1874. Cần tái xét chữ/nguyên tắc chép tại vị trí ấy trước mọi thay corpus.16vị trí này được chọn vì đã khác corpus điện tử;0chuỗi trùng app/Wikisource không phải tỷ lệ sai của toàn sách hoặc16lỗi đã được chứng minh.

Năm đoạn chú in đen được đọc có mục tiêu. Đáng chú ý,50.4 inlời `其形渥` nhưng chú nói `形渥者本作刑剭謂重刑也今從之`; bản văn và ý kiến người chú cùng tồn tại, không được ép thành một chữ thay thế duy nhất. Phân biệt lời sách, đề nghị trongchú và biên tập hiện đại ở `MANUAL_READINGS.json`, `COLLATION_AUDIT.json`, `CONSUMER_CHANGES.json`. Chú đỏ không chép/áp dụng. Không gọi16hào là một lượt hiệu khảo384hào thứhai hoặc khai thác hếtKinhDịch.

## Kiểm tra và phát hành

**30/30 kiểm tra phù hợp đạt:**15nguồn/runtime +15trìnhduyệt.4096lần dựng quẻ thật bằngHHC_ENGINE bao phủ64quẻ×64tập hào động; giữ đúng vị trí và chỉ hai lờiDụng đúng điều kiện. Kiểm nhúngHTML dùng nguyên sáumôđunYihiện hành; bốn vị trí cập nhật trùng giữa đọc hào chọn và đọc sáu hào;384tiêu đề còn duy nhất. Chỉ bốn bản ghi biên tập khácsnapshot, các môđun khác kiểm SHA bằngmanifest trước sửa.

Trình duyệt kiểm từng lời mới, lưu/mở hồ sơ bằng đầu vào và tính lại, TXTđủ sáuhào/kếtquảthu gọn được phục hồi, inhiện đúnglời/ẩnform,320/390/768/1440pxkhông tràn, đổi đầu vào xóa kếtquảcũ.0lỗiJS/0yêu cầuHTTP từHTML độc lập. Đã xem ảnh390/1440px; lượt này không tạoPDFmới vì không đổi bố cục in, chỉ kiểm chế độin và nội dung. Kết quả tại `qa/yi-second-witness/ENGINE_RESULTS.json`, `BROWSER_RESULTS.json`.

Hai lỗi trong cách chạy bài kiểm đã sửa: tiến trình conPython bịsandboxtừchối được thay bằng đọc bản nguồn cũ đã trích/kiểmSHA từZIP; nội dungtrongdetailsđangđóng được lấy bằngtextContentthay vìinnerText. Không phải lỗi định tuyến hay mất lời đọc của sản phẩm; lần chạy cuối30/30đạt.

Bản trước sửa giữ tại `../archives/v53-before-yi-second-witness/`, gồmHTML,manifestvàhaiZIP. HTMLđộc lập/gốc/sitevàhaiZIPđược đồngbộ cùngV53;sitechỉindex.html,góiwebchỉindex.html/HUONG_DAN.md. Không xuất bản. Tái kiểm:

```powershell
node v53/scripts/verify-yi-second-witness.mjs
node v53/scripts/verify-yi-second-witness-browser.mjs
python v53/scripts/verify-yi-second-witness-release.py --no-write
```

Phạm vi bốn hướng nghiên cứu vẫn **chưa hoàn tất**. Tiếp theo cần xác minh đề ký/định danh nhân chứng bổ sung, xử lý phần dị văn/chú giải còn lại theo tác động nghĩa, và nối tiếp các điều kiện cách cụcBátTự, dị bảnTứHóa/khởihạn, ranh năm/Phitinhnhàở đang mở. Không tải lại cùngPDF hoặc lặp384hào chỉ để tăng số.
