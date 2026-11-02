# Quyển 1 và tám nhóm quẻ in

Đã đọc liên tục42trang PDF13–54với ghi chép có giới hạn;45đề mục số ghim revision được nối vị trí. 23trang nội dung mới,19đọc mở rộng gồm54đã từng kiểm ranh. Trang54có mục Ngũ vị và lời kết,không phải trang trắng kết thuần túy.

- `MANUAL_READINGS.json`, `UNIT_MAP.json`: phạm vi từng trang/mục,không nhận đã phiên âm hết mệnh đề.
- `SOURCE_BASELINE.json`:214bản ghi ảnh cũ giữ nguyên,18trang mới render từPDFcũ;232trang nay đều có ảnh2000px. Không HTTP/OCR.
- `TABLE_FIELDS.json`:216vị trí đề mục vật tượng,27mỗi quái. Giữ214thân trường bản số với SHA riêng;chưa nhận tất cả giống bản in. Hai trường bị bỏ khỏi bản số có đoạn chép tay ngắn:Khảm–Động vật vàCấn–Tính tự. Tám đầu mục bản in謀望khác nhãn bản số謀旺.
- `PALACE_ROWS.json`:64tên quẻ trong tám hàng in,giữ riêng7vị trí khác bản số(gồm兌為澤/兌為金và未/末). IDVăn Vương và thượng/hạ quái là định danh biên tập đã kiểm engine;dãy mặt nạ nhị phân là suy luận triển khai khớp cả64,không phải ký hiệu in trong sách.
- `palace-reference.mjs`:tra nhóm/vị trí theo số quẻ hoặc6bit dưới lên,tái tạo chuỗi nhóm,tra chứng cứ đề mục. Không suy hành Thể Mai Hoa từ hành nhóm;không tự dựng Thế–Ứng/Nạp Giáp/Lục thân/Lục thần hoặc dự báo Lục Hào.
- `FIVE_VOLUME_NAVIGATION.json`:đủ vị trí năm quyển:212trang trong khoảng các quyển,gồm209nội dung/3trang kết. 123mục số ba quyển và93nhóm/đơn vị lồng quyển4/5không phải cùng đơn vị đếm hoặc số sách.
- `VARIANTS_AND_GAPS.json`:hai trường thiếu,tám nhãn đề mục và các tiền đề cách tiếng/màu còn cần phân biệt.

`node v53/scripts/verify-meihua-volume1.mjs`:10kiểm có64quẻ engine thật/64khóa bit vàphản ví dụ hành cung≠hành Thể. Không cộng lại384cấu trúc/467cách gieo cũ. HTML/site/webZIPgiữ byte;nghiên cứu ngoài site. B01và toàn kho chưa khai thác hết.
