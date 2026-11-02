Nhà ở — hai dấu Kiến/Phá trong bảng720ô và ranh tháng, 29/10/2026

P08 bảng逐月吉凶日: đối riêng sự có/không của hai chữ建/破 trên đủ720tọađộ,60建/60破/600ôkhônghaichữnày; chưa chép hết các nhãn ghép khác, không coi600ô là trống hay tốt. Tra nguồn riêng buộc tháng khai báo, can chi hợp lệ và giữ kết luận tổng thểnull. Một batch quét2560đối tượng lịch để chọn720khung chi tháng/ngày, gọi720getZhiXing lunar-typescript1.8.6 thật, khớp720dấu đã chọn;24vídụ ranh cho kết quả khác khi tự thay tháng âm số. Sáu nhóm kiểm đạt,2880truy vấn gốc tháng không hỗ trợ bị từ chối; không chạy lại lịch.18cropnative khớpRGB,15dùnglàmchứng;2cropcắtcụtvà1glyphchưachốt bịloại.0HTTP/vịtrí/container/nhânchứng mới; không lập lịch chọn ngày hay kết luận cát hung; web nguyên byte, toàn kho mở.

Phạm vi văn bản

Tái dùng ảnh facsimile131–134 của P08DươngTrạchThậpThư, nguồn PDF có SHA-256b6394102a995bb66df173452b37614b29d58e34ff85e08c43077006572ac48a5. Hồ sơ gốc là PDF được Commons phục vụ, mô tả bản giữ tại Thiên Nhất Các và có dấu xử lý Shuge/PDFPatcher; chưa xác minh độc lập mô tả cấp item của cơ quan và không gọi byte này là bản scan nguyên thủy của cơ quan. Không có HTTP, vị trí ảnh, container gốc hoặc nhân chứng độc lập mới. Sáu panel mười cột ngày theo60can chi và12hàng tháng cho720tọađộ. Thứ tự ngày và hàng tháng được đọc trực tiếp; J/P/dot chỉ là ký hiệu nhập liệu biên tập. Không dùng công thức để điền ô nguồn.

Mỗi ô chỉ được đối sự hiện diện của hai chữ建/破:60chữ建,60chữ破,600ô không có hai chữ đã chọn. Những ô đó vẫn chứa nhãn khác; toàn bộ720ô đều chưa có tuyên bố chép hết mọi chuỗi nhãn. Không gọi dot là ô trống, không gọi không có Kiến/Phá là ngày tốt. Caption天皇帝星 rõ chữ帝, nhưng glyph nhỏ trong ô bảng chưa chốt là帝/寧/富. Đã rút nhận dạng sơ bộ từ phép so hình; không lấy OCR hoặc caption để điền token.

Chức năng và đối chiếu thực thi

source-day-markers.mjs là tham chiếu nội bộ cho tọa độ nguồn. Hàm nhận đúng hệ nguồn, tháng1–12 hoặcnull, can chi ngày hợp lệ hoặcnull và monthBasis='declared-source-month'. Không nhận ngầm tháng âm, dương lịch, tiết khí hay tháng nhuận. Thiếu tọa độ giữunknown; sai can chi bị từ chối. Kết quả chỉ có danh sách chữ đã chọn và neo ảnh; các nhãn còn lại, đầy đủ ô và khuyến nghị tổng thể không được suy ra.

MANUAL_BUILD_BREAK_MARKERS/NATIVE_CROPS được đóng băng trước engine. Một batch tạo2560đối tượng Lunar từ các ngày hiện đại để chọn đủ720khung chi tháng/can chi ngày. Chỉ720lời gọi getZhiXing được thực hiện; toàn bộ chỉ so dấu建/破, không so các nhãn còn lại với thư viện.2560đối tượng quét không phải2560lásố sinh hay2560ca độc lập đạt. Thư viện lunar-typescript1.8.6 được giữ SHA-256. Runtime không bị chạy lại trong các kiểm sau.

720khung có đủ khớp dấu đã chọn.24ví dụ lưu lại cho thấy dùng số tháng âm thay khung chi tháng đã khai báo có thể đổi nhãn. Điều này minh họa sự khác nhau giữa hai đầu vào, không chứng minh nguồn phải dùng tháng tiết khí hoặc thư viện sai. Chưa có adapter ngày hiện đại hay hiệu quả chọn ngày được xác minh.

Sáu nhóm kiểm đạt gồm hash/freeze,720tọađộ/dấu,lookup720ô,thực thi thư viện,24ví dụ khác gốc tháng và2880truy vấn monthBasis không hỗ trợ bị từ chối.0HHCchart/0iztrochart trong phạm vi này. API giờ sourceJieluActivityScope đã có ở phạm vi trước nên được tái dùng qua chỉ mục; không tạo hàm trùng hay chạy lại144ca giờ.

Bằng chứng và giới hạn

18crop native được xem/so RGBpixel:15làchứngđọc,2crop đoạn giờ còn cắt sau嫁 và1crop glyph bảng chưa chốt bị loại khỏi chứng nguyên câu/nhận dạng. Nguồn đầy đủ cho ngoại lệ 截路空亡 vẫn là hồ sơ trước; không nối phần bị thiếu bằng suy đoán. Lời nguồn nêu建破魁罡 ngay cả có吉星 là bối cảnh văn bản, không phải hậu quả đã chứng minh. Chưa đủ mọi nhãn/công việc/ưu tiên để đưa kết luận tổng thể cho người dùng.

Bản5348tệp/sourceZIP2863598154byte được giữ trongarchives/v53-before-home-day-markers trước tích hợp. HTML707411byte/engine/content/site/webZIP giữ nguyên byte. Kho vẫnactive-not-complete; không xuất bản mạng.
