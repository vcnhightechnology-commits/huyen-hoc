# Lục Hào: tuần không, động tán, sinh–vượng–mộ–tuyệt và tháng phá

Ngày công việc: 27/10/2026. Trạng thái toàn kho: **active-not-complete**. Tài liệu nghiên cứu riêng; không nằm trong `site`.

## Kết quả có thể tái lập

Đọc lần đầu toàn khoảng chương 18–27, gồm bốn mục đánh lại số 26; khép ranh kết chương 19 bằng ảnh 79/80 và các trang 73–78 đã đọc ở phạm vi trước. Khoảng liên tục PDF 71–108 có 38 trang, trong đó lượt này có 33 bản ghi ảnh: 25 render mới, 8 trang đọc mở rộng; năm trang giữa chương 19 được kế thừa với hash rõ ràng. Đây là hoàn tất lượt đọc khoảng trang, chưa phải áp dụng hết mọi mệnh đề hoặc xác minh các chuyện ứng nghiệm.

Chỉ mục vẫn 136 đơn vị (130 số thường + 6 mục phụ). Số đơn vị mới hoàn tất lượt đọc khoảng: 14; tổng 26. Còn **103 thân mục chỉ ở mức đề mục**, 7 mục nền tảng mới khai thác một phần. Không mục nào được gán toàn đơn vị đã áp dụng hết. Tiêu đề thân chương 22 in **靜動**, còn chỉ mục chuẩn hóa trước đó là **暗動**; giữ hai lớp và crop đọc, không âm thầm sửa chữ bản ảnh.

Thêm bộ tham chiếu `research/liuyao-void-motion/void-motion-reference.mjs`, chạy riêng, kế thừa bốn bộ trước mà không sửa các bản đã hoàn tất:

- Sáu dòng tuần không in tại PDF 93 → tọa độ 60 ngày can chi hợp lệ. Sáu mươi dòng là phép suy ra minh thị từ chu kỳ, không giả là sách in đủ 60 dòng.
- Gắn **thuộc cặp không theo tọa độ** cho hào chính/hào biến. Trạng thái không còn tác dụng, chân không, ứng kỳ và sự kiện vẫn chưa quyết định. Không nhận ngày Gregorian hoặc tự chọn ranh giờ/ngày/tháng.
- Mười hai dòng tháng phá và 18 tọa độ sinh/vượng/mộ/tuyệt đọc rõ. Kim/Mộc/Thủy/Thổ đủ bốn vị trí; Hỏa mới có sinh Dần và mộ Tuất trong khoảng này, hai ô vượng/tuyệt để chưa biết, không điền bằng trí nhớ.
- Khung tác giả ở đây cho Thổ sinh Thân, vượng Tý, mộ Thìn, tuyệt Tỵ; đồng thời bàn điều kiện khiến Tỵ Hỏa sinh Thổ. Lời trích “Hỏa Thổ sinh Dần” và lập trường tác giả được tách riêng; không trộn bảng truyền bản.
- 36 mệnh đề giới hạn, 16 tiền đề boolean minh thị. Chỉ đối các liên hợp điều kiện đã ghi, dùng ba trạng thái có/không/chưa biết; không phát sinh thứ tự ưu tiên hay điểm cát hung chung.
- Chương 23 khiến kết luận động yếu gặp nhật xung phải hạ xuống **có thể tán, chưa quyết định**. Tác giả nói trường hợp này ít, còn hậu nhật trực/khắc/chuyển sinh; bộ NhậtNguyệt cũ được giữ lịch sử, bộ tổng hợp mới ghi rõ hạn chế sâu hơn.
- Bản in PDF 93 đọc **有氣不動亦為空**. Giữ nguyên cùng câu “旺不為空”, ghi chồng lấn điều kiện chưa được giải quyết; không thay chữ thành 無氣 để làm thuật toán có vẻ nhất quán.
- Sáu hàng Lục thần in ở PDF 71 kiểm lại đủ mười can, sáu vị trí; quy đổi 元武/玄武 và chiều đọc được ghi. Hồn quẻ gắn theo Du hồn thứ bảy/Quy hồn thứ tám, không suy sự kiện từ tên hồn.

## Kiểm chứng thực thi

`node v53/scripts/verify-liuyao-void-motion.mjs`: **16/16 kiểm đạt**. Đã thực thi `lunar-typescript 1.8.6` thật, kiểm hash hai tệp runtime trước khi dùng: 60 ngày liên tiếp ở 12:00, 60 can chi khác nhau, 720 đối chiếu chi và sáu tuần. Thời điểm trưa chỉ tránh lẫn tranh luận giờ Tý trong phép đối chiếu, không chứng minh ranh ngày của sách.

Engine HHC thật chạy **140 lần**: 12 lần cho sáu hình in và 128 lần cho 64 cấu trúc quẻ/biến. Nối 64 cấu trúc với 60 ngày tham chiếu cho 3.840 ngữ cảnh, 46.080 cờ thuộc cặp không của hào chính/biến, 7.680 cờ đúng. Có 72 đối chứng độc lập theo chi × động/tĩnh × ba tiền đề mạnh/yếu/chưa biết. Digest ma trận: `5c18d2063a7b0ea72e7d07cfa6bb7e875b1fbf370208bc8450de8bd49a957192`.

Các hình đã khóa: Hoán 59→Khảm 29; Tốn 57→Khảm 29; Tốn 57→Càn 1; Gia nhân 37→Ký tế 63 chỉ hào 6 động; Đại súc 26 tĩnh; Minh di 36→Tiểu quá 62 hào 1/4 động, Thế Sửu Thổ 4 hóa Ngọ Hỏa. Kết quả chuyện cổ không được tính là độ chính xác dự báo.

## Nhân chứng ảnh độc lập về đối tượng lưu trữ

Tra [mục 増刪卜易１ của Quốc lập Công văn thư quán Nhật Bản](https://www.digital.archives.go.jp/item/4756813), theo liên kết công khai tới [IIIF manifest](https://www.digital.archives.go.jp/api/iiif/4756813/manifest.json). Giữ 11 body HTTP 200/TLS xác thực: item, viewer, manifest 51 canvas, ba thumbnail chỉ định vị, năm JPEG chụp trang đôi. Một yêu cầu canvas 33 timeout, không giữ body, không tải lặp. Web tool báo 403 cho item; yêu cầu HTTPS công khai thông thường trả 200 được ghi riêng, không tắt TLS hay dùng thông tin đăng nhập.

`INDEPENDENT_WITNESS.json` khóa URL/byte/SHA từng body và giới hạn đọc. Các ảnh là byte phản hồi máy chủ không sửa; JPEG thực nhận 3.000×2.073, không đồng nhất với metadata canvas 6.150×4.250, không tuyên bố là master độ phân giải cao nhất. Đây là ảnh sách in do cơ quan lưu trữ cung cấp; niên đại xuất bản trực tiếp, quan hệ phả hệ với bản B02 và độ độc lập văn bản chưa xác lập bằng các trang này.

Canvas 37 đọc được danh sách năm điều Nguyên thần hữu lực/sáu điều bất lực; canvas 38 có năm/bảy điều Kỵ thần và ví dụ Đại quá→Đỉnh. Không thấy chuyện Đoài→Giải có ngày đang tranh luận trong đúng khoảng mệnh đề Nguyên thần tương ứng đã xem. Giới hạn này **không chứng minh chuyện vắng trong toàn sách**, cũng chưa giải quyết mâu thuẫn B02 PDF 52: ngày in Tân Mão → tuần Giáp Thân/Ngọ Mùi không, còn văn giải nói Dần Mão không. Tân Hợi phù hợp Dần Mão chỉ là giả thuyết, không sửa nguồn.

## Bản dùng và phần tiếp tục

HTML độc lập/root/site vẫn **707.411 byte**, SHA-256 `549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857`; ZIP web 344.047 byte giữ nguyên. Không đưa nghiên cứu riêng lên trang người dùng, không xuất bản mạng. Snapshot trước phạm vi giữ nguồn ZIP **944.353.384 byte** tại `archives/v53-before-liuyao-void-motion/`.

Tiếp: đối chiếu các chương tương ứng B03; hoàn chỉnh tiền đề mạnh/yếu trước can thiệp Nhật–Nguyệt, các điều chân không/không theo xa gần, phản–phục và tầng quẻ/tầng hào; tìm nhân chứng trực tiếp cho chữ/ngày chưa thống nhất. Đọc thân mục sau 28 và các nhánh Mai Hoa/Bát Tự/Tử Vi/nhà ở còn mở. Chưa có bộ luận đoán Lục Hào công khai hoặc tuyên bố khai thác hết sách/toàn kho.
