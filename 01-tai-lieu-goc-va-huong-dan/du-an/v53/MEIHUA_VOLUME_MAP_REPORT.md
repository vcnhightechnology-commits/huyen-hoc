# Mai Hoa: bản đồ hai quyển chữ và giới hạn áp dụng

Ngày 26/10/2026. Đây là hồ sơ nội bộ, không có trong site hoặc ZIP web. Nối tiếp `MEIHUA_WITNESS_REPORT.md`; không thay bản ghi hay kết quả kiểm của phạm vi trước.

Đã đọc ảnh của 47 trang còn thiếu trong bản đồ quyển bốn và năm: PDF150–178,209–219,221–227. Bốn trang207,208,220,228 được xem lại để nối bảng và ranh chương. Tái dùng toàn bộ ảnh/PDF đã giữ; không tải HTTP, không OCR, không tạo ảnh render mới. Mỗi bản ghi mới giữ SHA-256 của ảnh nguồn trong `research/meihua-volume-map/MANUAL_READINGS.json`.

Kết hợp với hồ sơ trước, bản đồ nay đi liên tục qua **84 trang PDF145–228**, gồm82 trang nội dung và hai trang kết188/228. Đây là độ phủ vị trí và một số mệnh đề có mục tiêu, **chưa phải bản chép đủ từng câu, đọc hết năm quyển hoặc áp dụng hết sách**. 34 nhóm cũ được giữ, thêm59 nhóm/đơn vị lồng, tổng93. Chương bao `新訂指明心法`, tiểu mục `歌曰` và nhóm nhiều đề nhỏ được ghi đúng cấp; không đếm chúng thành93 thuật toán hay93 sách.

## Những khác biệt làm thay đổi cách phát triển

- Quyển bốn chủ yếu bàn hình chữ, chữ ký, nét dài/ngắn/đậm/nhạt, thứ tự viết, câu hỏi và ngoại cảnh. `五言作用歌` nói rõ cùng một chữ, nhiều người viết có nét khác nhau(PDF215). Văn bản gõ thông thường không cung cấp những quan sát này. Không có căn cứ tự nhận diện đầy đủ từ Unicode hoặc tổng nét.
- `八卦斷` có thêm mệnh đề勾陳(PDF161), nhưng không vì vậy tạo “quái thứ chín”. Engine đang dùng vẫn tám quái; đã thực thi tám trường hợp hợp lệ và một trường hợp9 bị từ chối.
- `六神筆法` là hệ hình nét(PDF172), có螣蛇/無正位. Nó khác vòng sáu thần theo can ngày(PDF179–180). Không lấp chỗ vô chính vị bằng một thuộc tính suy từ vòng can ngày.
- Dụng thần là nét cuối trong `四言獨步`(PDF213) thuộc phép chữ. Không ghép nó thành Dụng quái động của Mai Hoa hay dụng thần Bát tự. `反體`(PDF172) còn cho cách đọc ngược chữ có vẻ tốt; không thể làm bộ chấm cát hung bằng vài từ tích cực.
- Các đoạn問壽/六甲/疾病 và thơ tính tuổi từ nét(PDF169–171,214,218–219) giữ tư cách tuyên bố lịch sử. Không dùng chúng làm dự báo tuổi thọ, xác định thai/giới tính hoặc chẩn đoán. Các ví dụ hồi thuật không chứng minh độ chính xác dự báo.
- Mục勢(PDF164) còn không chắc giữa視勢/觀勢; giữ hai cách đọc, không coi đã hiệu khảo xong. `筆法筌蹄` ghi lại cách đọc hiện tại, giữ ảnh làm căn cứ thay vì dựa vào nhãn mục lục cũ.

## Những phần đã trích có giới hạn

`BOUNDED_EXTRACTS.json` giữ bốn ví von nước theo mùa tạiPDF160: xuân đục, hạ cạn, thu trong, đông đóng. Đây là ví von bút pháp, tách khỏi bảng旺相休囚20ô tạiPDF204 và dữ liệu thời tiết. Sáu nhãn hình thần ởPDF172 có tư cách riêng. Ba trang155–157 có23 nhãn ví dụ chữ:5+12+6; chưa biến thành23 ca dự đoán đúng hoặc23 fixture tổng nét.

Bảng `後天時方` bắt đầuPDF207 và kết ở212, không kết ở208. Đã lập chỉ mục **60 khóa can chi** cùng ranh trang4/12/12/12/12/8 hàng. Mười hai cột cho720 vị trí nhãn, nhưng **chưa chép và đối chiếu đủ720 ô**. `HOUR_TABLE_INDEX.json` ghi rõ số ô nhãn đã chép là0; không nội suy chúng theo một chu kỳ giả định. Dạng in己/巳, nhãn ngắn/nhiều chữ và ý nghĩa đầu vào của lời dẫn vẫn cần đối chứng. Không đưa bảng này ra web như bộ chọn giờ tốt.

## Kiểm chứng và tình trạng bản dùng

`node scripts/verify-meihua-volume-map.mjs`: **9/9 kiểm đạt**, gồm byte nguồn/47 ảnh, tập trang và ranh in,93 nhóm/đơn vị,60 khóa bảng và sáu ranh chuyển trang, sự tách biệt các hệ kiến thức, thực thi engine với chín kiểm quái và byte bản dùng. Kết quả tại `qa/meihua-volume-map/SOURCE_RESULTS.json`. Những kiểm này không phải kiểm nghiệm dự báo đời người.

HTML đang dùng vẫn703.410byte, SHA-256 `3800162854742c915d60f0051c65cadb0eb9a1c803f9f937bf1b6a593c96d268`; các mô-đun JS/CSS, site và ZIP web giữ nguyên. Gói nguồn/hồ sơ nội bộ được đồng bộ riêng. Gói nguồn831.546.206byte trước phạm vi này và manifest được giữ ở `../archives/v53-before-meihua-volume-map/`.

Bản Thể–Dụng mở rộng vẫn nằm riêng ở `research/meihua-layers/PENDING.json`:14 kiểm phép tính đã đạt,0 kiểm trình duyệt/PDF được thực thi, chưa phát hành. Vướng mắc bộ duyệt tự động hết hạn mức đã có hồ sơ; phạm vi hiện tại không thử vượt cơ chế duyệt và không nhận kiểm chưa chạy là đạt.

## Phần tiếp tục

Không còn trang trống trong **bản đồ vị trí quyển4/5**, nhưng vẫn còn mệnh đề, nét khó, điều kiện và dị bản chưa giải quyết. Cần hoàn thiện hàng nhãn của bảng giờ với ngữ nghĩa đầu vào và nhân chứng khác, không suy ô chưa đọc. Những nhận định phụ thuộc hình nét chỉ có thể áp dụng khi có đầu vào quan sát thích hợp và phương pháp rõ.

Ưu tiên tiếp theo là đọc đủ quy tắc điều kiện của quyển1–3: Thể/Dụng/hỗ/biến,18 nhóm câu hỏi, vượng suy/mùa và ba yếu tố/mười ứng; nối từng đơn vị ảnh với bản số đang có. Không lặp lại23 chuyện chữ hoặc93 nhãn chỉ để tăng số kiểm. Bộ Nạp Giáp nội bộ trước đây chưa đủ cung/Thế/Ứng/Lục thân/Phục thần, không phải chức năng Lục Hào hoàn chỉnh. Toàn kho vẫn `active-not-complete`.
