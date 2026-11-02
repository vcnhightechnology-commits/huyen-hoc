# Mai Hoa: điều kiện Thể–Dụng và mười tám chủ đề

Ngày26/10/2026. Nối tiếp `MEIHUA_VOLUME_MAP_REPORT.md`, trong cùng V53. Hồ sơ và chương trình tham chiếu chỉ dùng nội bộ; không nạp vào HTML/site hay ZIP web.

## Phạm vi nguồn thực sự đã làm

Đã đọc ảnh liên tục PDF55–102 trong tệp gốc `research/meihua/NLC416-12jh005426-44577.pdf`, SHA-256 `af608094ab11ae209eae91a9365565e7c9cff604aac3da5e753e04d1cc4598c0`. Có48 bản ghi trang:44 trang nội dung55–98, hai quảng cáo99–100, logo101 và bìa下冊102. Trong44 trang nội dung,38 có bản ghi mới, sáu trang56/58/59/61/95/96 được đọc mở rộng. Trang54 xem lại để xác nhận cuối quyển một. Quyển hai kết ởPDF98/trang in44, không kéo nội dung sang bìa102.

Render thêm28 trang thiếu từ PDF đã giữ bằng Poppler, cỡ2000px; tổng214 PNG. Không HTTP, OCR hay tải sách mới. Tệp PDF và186 bản ghi ảnh cũ giữ nguyên; bản chỉ mục trước render lưu tại `../archives/v53-before-meihua-conditions/`. PNG là bản dẫn xuất, không tự nhận byte ảnh nhúng gốc.48 trang được đọc có cấp độ giới hạn, không đồng nhất214 ảnh với214 trang đã hiệu khảo.

`UNIT_MAP.json` nối52 mục văn bản số quyển hai với dải trang in. Bao quát vị trí chương không có nghĩa hoàn thành bản chép từng dòng, mọi điều kiện phụ hoặc toàn tác phẩm. Năm quyển, lịch sử tác giả và nhân chứng độc lập vẫn còn mở.

## Bộ quy tắc tham chiếu đã thực thi

`research/meihua-conditions/conditions-reference.mjs` nhận kết quả thật của engine Mai Hoa đang phát hành và một chủ đề được chọn rõ. Nó kiểm tra tính nhất quán của sáu hào, quái trên/dưới, hào động, hỗ và Dụng biến trước khi đọc. Nó không tự nhận câu hỏi thành chủ đề hoặc lấy dữ liệu sinh của Bát tự làm mùa/ngoại ứng.

`DOMAIN_RULES.json` giữ18 nhóm câu hỏi,17 cặp vai trò Thể–Dụng và85 mệnh đề quan hệ trực tiếp. Chẳng hạn cùng Thể khắc Dụng: mục ăn uống nói có trở ngại, mưu sự nói thành nhưng chậm, đi xa nói có thể đi, người đi xa nói về chậm. Mục sinh sản đặt Thể là mẹ, Dụng là sinh; hai chiều tương sinh có đối tượng hưởng lợi khác nhau. Đây là ngữ nghĩa tuyên bố của bản sách, không phải85 dự báo đã được thực nghiệm xác nhận. Những lời về thai/giới tính, thuốc nóng/lạnh, bệnh/tử vong, ma quỷ, kiện tụng, tiền bạc và phần mộ không được xuất thành quyết định cho người dùng.

Thiên thời(PDF63–65) ghi rõ **không chia Thể–Dụng**; chương trình trả về không áp dụng quan hệ này, không rơi về kết luận của mục nhân sự. Đoạn tĩnh chiêm(PDF93) nói không nghe thấy/gặp thấy gì thì không luận ngoại quái. Không có dữ liệu quan sát thì đầu ra giữ rỗng; khi dùng ngoại ứng tham chiếu phải nhập rõ mô tả đã quan sát và quái do người quan sát chọn.

Đồ thị nội bộ giữ Thể gốc làm mốc, Dụng, hỗ phía Thể, hỗ phía Dụng và Dụng biến. Các cạnh sinh/khắc giữa các nút được ghi riêng. ĐoạnPDF89 cho điều kiện “khắc quái đang sinh Thể” hoặc “khắc quái đang khắc Thể”; chương trình chỉ đánh dấu điều kiện cần xét. **Không tự triệt tiêu cạnh, cộng điểm, xếp trọng số hoặc chốt cát hung**. Các lớp có vị trí/ngữ cảnh khác nhau, không mặc định là các sự kiện đồng thời.

Ví dụ nhà họ Điền quẻ Tỉnh48→Thăng46(PDF96): Thể Tốn Mộc được Khảm Thủy sinh, hỗ Đoài Kim khắc Mộc, hỗ Ly Hỏa lại khắc Kim. Chương trình giữ đủ các quan hệ và điều kiện; không biến câu chuyện29 năm của sách thành thời hạn hỏng nhà. Biến Khôn Thổ khắc nguồn sinh Khảm Thủy cũng được ghi là khả năng quan hệ trong mô hình, tách khỏi mệnh đề câu chuyện đã in.

`SEASON_PREMISES.json` giữ đúng hai trạng thái được nêu ở từng nhóm mùa: vượng và nhóm bị khắc, tổng10 ô; không tự điền thành bảng đủ vượng/tướng/hưu/tù/tử. Có12 mốc chi tháng/ngày ởPDF84–85. Đầu vào mùa, chi tháng và chi ngày được tách riêng. Nếu tháng Ngọ cho Hỏa vượng, ngày Tý cho Hỏa suy thì lưu cả hai, không giả đặt ưu tiên tháng/ngày. Ranh tiết khí/tháng âm lịch, cách đổi từ ngày dương và trọng số chưa được các đoạn này xác định.

## Năm khác biệt giữ nguyên để đối chứng

| Vị trí | Điều quan sát | Cách xử lý |
|---|---|---|
| PDF57 | Ảnh in乾為戌亥; bản số坤為戌亥 | Giữ cả hai, không sửa byte bản chép hoặc coi đây là xác minh ranh lịch. |
| PDF69 | Giao dịch: ảnh đặt Dụng là交易之應, Thể khắc Dụng交易成遲; bản số dùng財/有財 | Bảng tham chiếu theo nhân chứng in này, gắn phạm vi rõ. |
| PDF74 | Ảnh主貧退, bản số主運退 ở mộ phần | Giữ khác biệt và tính chất tuyên bố lịch sử. |
| PDF83 | Giữa trưa Ly, ảnh và bản số cùng nói坤兌為體則吉 | Chữ兌 mâu thuẫn chiều Hỏa khắc Kim. Không tự sửa thành艮. |
| PDF73 | Ví dụ Bĩ hào hai ghi hỗ Tốn/Ly | Engine thật cho hỗ gốcTiệm53=Tốn/Cấn; hỗ của quẻ biếnTụng6 làGia Nhân37=Tốn/Ly. Ghi khác ngữ cảnh, không đổi quy tắc chung. |

Sáu trường hợp Bĩ12 được chạy thật, quẻ biến lần lượt25/6/33/20/35/45. Các chuyện bệnh kèm chúng không phải sáu ca kiểm nghiệm lâm sàng. Đoạn sách dùng cách đọc có điều kiện và có chỗ đổi ngữ cảnh hỗ; vẫn cần nhân chứng khác trước khi áp một chính sách mới cho toàn engine.

## Kết quả kiểm và bản phát hành

`node scripts/verify-meihua-conditions.mjs`: **14/14 kiểm đạt**, kết quả `qa/meihua-conditions/ENGINE_RESULTS.json`. Có384 cấu trúc quẻ thật đưa qua bộ đọc mới,1.920 nút/4.710 cạnh,85 lựa chọn mệnh đề theo chủ đề,25 cặp ngũ hành kiểm độc lập,10 ô mùa/12 mốc chi, sáu ca Bĩ và các phản ví dụ về vai trò/thiên thời/ngoại ứng. Số kiểm phản ánh tính đúng của phép biểu diễn, không chứng minh năng lực dự báo.

HTML đang dùng703.410byte/SHA-256 `3800162854742c915d60f0051c65cadb0eb9a1c803f9f937bf1b6a593c96d268`; JS/CSS/root/site/ZIP web giữ nguyên. Nghiên cứu được gói vào ZIP nguồn và manifest riêng. Gói nguồn831.586.307byte trước phạm vi này được giữ tại `../archives/v53-before-meihua-conditions/`.

Candidate Thể–Dụng giao diện vẫn ở `research/meihua-layers/PENDING.json`,14 kiểm phép tính cũ,0 kiểm browser/PDF, chưa phát hành. Phạm vi hiện tại không thử vượt bộ duyệt đang vướng hạn mức. Bộ quy tắc18 chủ đề ở đây cũng chưa phải giao diện mới hoặc kết luận tổng hợp hoàn chỉnh.

## Phần còn phải làm

Tiếp đọc và nối đủ mệnh đề phụ của quyển một/ba, rồi đối chiếu các lựa chọn khác nhau về hỗ, điều kiện mùa và ngoại ứng; không lặp52 đề mục hoặc384 cấu trúc để tăng số.18 chủ đề vẫn còn bảng người/vật, vị trí, thời điểm, ngoại lệ và chữ khó chưa được trích đủ. Bảng giờ720 vị trí quyển năm, cùng các truyền bản và chức năng khác trong kho, vẫn mở. Toàn kho giữ `active-not-complete`.
