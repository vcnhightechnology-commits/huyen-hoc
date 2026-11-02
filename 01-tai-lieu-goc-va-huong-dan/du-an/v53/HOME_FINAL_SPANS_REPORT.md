# P08 — khép lượt đọc đầu Dương Trạch Thập Thư; bảng giờ theo bản sách

Ngày: 2026-10-28. Phạm vi nội bộ, tiếp V53.

Đã đọc thêm **92 vị trí PDF chưa đọc**, khép ba khoảng mục **ngoại hình, tuyển trạch, phù trấn**. Cộng các phạm vi đã giữ: **195/195 vị trí có lượt đọc đầu, 10/10 khoảng mục chính**. Đây là độ phủ đọc cấu trúc/ngữ cảnh; **chưa hiệu khảo mọi chữ, chưa áp dụng mọi quy tắc, chưa hoàn tất kho sách**.

## Nguồn và ranh đếm

Tái dùng PDF kho Commons dẫn về Thiên Nhất Các, 151.275.796 byte, 195 vị trí; SHA-256 `b6394102a995bb66df173452b37614b29d58e34ff85e08c43077006572ac48a5`. PDF có dấu xử lý Shuge/PDFPatcher/iText; không đổi thành tuyên bố byte nguyên máy chủ cơ quan. Không HTTP, container hay nhân chứng độc lập mới.

Ba bộ ảnh mới giữ **95 bản ghi raw DCT / 94 vị trí phân biệt**: ngoại hình13–34 (22), tuyển trạch124–168 (45), phù trấn168–195 (28). Vị trí168 chung hai bộ;34/124 đã đọc trước. Chỉ **13–33 và125–195 =92** được tính mới. Vị trí168 của bộ phù trấn đã xem qua file raw cùng byte của bộ tuyển trạch; không tính thêm lượt đọc độc lập. Có95 ghi chú theo bản ghi/94 vị trí, không phải95 nhân chứng hay quy tắc nguyên tử.

40 vị trí đọc đầu cũ dùng ảnh pypdf mã hóa lại đúng kích thước, có audit giữ riêng;155 vị trí mới qua các phạm vi sau được đọc từ DCT nguyên xuất. Không hồi tố thành toàn40 ảnh raw cũ đều đã xem. **8 crop PNG không đổi kích thước** đã xem/khớp pixel trong phạm vi này. 120 ô hình ngoại cảnh là kiểm kê panel, có panel chứa nhiều hình nhỏ, chưa phải120 quy tắc đo lường đã áp dụng.

## Chức năng đã lập và đối chiếu thật

Chép trực tiếp **11 cột /132 ô giờ** ở134–135 trước khi chạy engine. Cột `勾陳` còn12 ô chưa hiệu khảo đủ; không điền bằng công thức phổ biến. Bản in ghi `土堂`, giữ nguyên; `玉堂` chỉ alias biên tập khi so, `金匱`→`金匮` và `青龍`→`青龙` là alias chữ tường minh.

Chạy `lunar-typescript@1.8.6` thật: **144 đối tượng lịch =12 dò chi ngày +132 tọa độ giờ**, **132 truy vấn thần giờ**. Dùng12 ngày liên tiếp01–12/10/2026, giờ00–22; xác nhận chi ngày chính xác và chi giờ cho từng ca. Không kiểm giờ23, múi giờ/instant hay ranh năm cổ. **120 ô khớp sau alias** (12 ô trong số này dùng alias土堂→玉堂); **12 ô cột司命 khác engine**: nguồnghi未酉亥丑卯巳lặp, engine trả勾陈tại các tọa độ ấy. Giữ khác biệt, chưa kết luận lỗi in hay dị bản; không sửa source/engine/web để ép khớp. Không gọi engine hiện đại là nhân chứng cổ độc lập.

Module riêng `selection/source-hour-reference.mjs` có ba API:

- Tra tọa độ theo **nhãn nguồn + chi ngày**, giữ司命bất đồng và勾陳null.
- Truy vấn các nhãn đã chép tại **chi ngày + chi giờ**; luôn khai báo độ phủ chưa đầy, ô không thấy không tự thành giờ xấu.
- Giới hạn ngữ nghĩa **截路空亡** theo trạng thái do bên gọi khai báo và loại việc; không tự suy Can Chi/ngày/tiết khí.

**8 kiểm đạt**: cấu trúc132ô; chữ/alias/bất đồng;132đối chiếu thật;144ngữcảnhgiờtra;15tổhợptrạngthái/loạiviệc;đầuvàonghiêm;khôngđổibảngquađầura;byteHTML/enginegiữnguyên. 0HHC/iztromới vì không đối chiếu trường của chúng; không chạy kiểm không liên quan chỉ để tăng số.

## Hiệu chỉnh cách đọc và giới hạn áp dụng

Crop134cho thấy ba mệnh đề liên tiếp: Hoàng đạo/quý nhân/lộc mã; Hắc đạo/không vong; rồi **截路空亡止忌出行嫁娶移徙餘皆不忌**. Ghi chú đầu lỡ đọc thành ngoại lệ cấm mọi việc đã sửa, giữ trong `READING_CORRECTION_AUDIT.json`. Quy tắc này chỉ nêu đi xa/cưới hỏi/chuyển chỗ; chưa đủ để gán ưu tiên giữa mọi lớp hoặc lập bộ chọn giờ tổng hợp. Ghi chú sai chỉ ở staging, không vào engine/web phát hành.

Tuyển trạch còn bảng720ô12tháng×60ngày, ma trận năm/lộc mã/quý nhân, tuổi hành niên, tháng theo tiết khí, Thái Âm/Thái Dương và nhiều gốc thần khác nhau. Lượt đọc không thay việc chép từng ô hay xác lập tuổi/ranh lịch. `SOURCE_DISPOSITIONS.json` ghi từng mục và khoảng trống.

Phù trấn có hình phù, nguyên liệu, chôn/đốt/tế tự, lời gán bệnh/tử vong/tài sản và lời biên soạn có giọng khác nhau. Phân loại **tư liệu nghi lễ/lịch sử**, không triển khai thành chẩn đoán, hướng dẫn thi công hay lời hứa trừ tai; không coi mọi nét phù đã phiên. Lời kết194–195 là tranh luận về宅法/mệnh/vận/tu đức, không chứng cứ hiệu nghiệm. Các mô tả hình ngoại cảnh cũng chưa tự thành bộ đo mặt bằng hiện đại.

HTMLgốc/V53/site707.411byte và ZIPweb344.047byte giữ nguyên. Site chỉ `index.html`; toàn bộ ảnh, ghi chú, module tra nguồn, audit và đối chiếu ngoài site. Bản trước giữ tại `archives/v53-before-home-yangzhai-final-spans/`, ZIPnguồn2.456.417.440byte. Xác minh cuối dùng `v53/scripts/verify-home-final-spans-release.py --no-write` sau khi đóng gói; chỉ kết quả đạt cuối xác nhận gói.

Tiếp tục các điều kiện hoàn chỉnh trong10mục, ưu tiên12đồ phân viện/cao-thấp46–56/82–93 và giao môn/đổi hào94–100; không tải lại dữ liệu cũ hay tuyên bố cả kho đã khai thác hết. Những nhánhBátTự/TửVi/Dịchcòn mở giữ trong trạng thái chung.
