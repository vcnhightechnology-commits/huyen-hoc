# Nhật–Nguyệt, động–biến và giới hạn tác động — 27/10/2026

Đã đọc lần đầu toàn khoảng các mục13,14,15,**“lại15”**,16,17 của B02, từ PDF56 tới69. Phần tính nội bộ mới giữ bảng60 ô định tính theo tháng, quan hệ xung/hợp, nhãn nhật xung có tiền đề và **giới hạn hào biến chỉ tác động lại chính vị trí ban đầu**. Không tự suy tổng vượng suy, chọn Dụng thần, gán ngày Gregorian hoặc đưa lời đoán mới lên web.

## Nguồn và sửa bản đồ đơn vị

Tái dùng PDF B02 đã ghim11.089.308 byte/394 trang, SHA-256 `caac111bc5c5b1c08fd27b3828e7cf6b5430503800f2427d8f2b28809022abaa`. **0 HTTP/PDF gốc mới**,19 render cục bộ mới và6 trang cũ đọc mở rộng, tổng25 bản ghi. Trong đó14 trang nội dung nằm trong khoảng sáu mục đọc lần đầu; chương19 có bảy trang quy tắc/ví dụ đọc có giới hạn, chưa nhận hoàn tất ranh kết chương. PDF70 là tờ kết quyển1;71 là đầu chương18, không tính đã đọc hết chương18. Không OCR hoặc tạo PDF mới.

Đối cả mục lục PDF13 và đề mục PDF59 phát hiện **mục 四時旺相 đánh số “第又十五”**. Bản đồ135 đơn vị trước đã bỏ mất mục phụ này, gán nhầm Tứ thời vào16, Nguyệt tướng vào17 và vì thế chưa có Nhật thần17. Lớp hiện hành sửa thành **136 đơn vị =130 số thường +6 mục phụ**; giữ mọi bản đồ/báo cáo135 cũ làm mốc lịch sử. Đây là sửa lỗi lập chỉ mục nội bộ, không phải thêm chương mới của sách hay lỗi của web đang dùng.

| Mục | Khoảng PDF đã đọc | Phần được biểu diễn nội bộ |
|---|---|---|
|13 Khắc xứ phùng sinh|56–57|Giữ điều kiện cứu qua trung gian và tính chất Kỵ/Nguyên khác nhau; không ghép thành kết luận chung.|
|14 Động tĩnh sinh khắc|57–58|Phân biệt mạnh/yếu của hào tĩnh và hoạt động của hào động; quan hệ hình học không tự là hiệu lực.|
|15 Động biến sinh khắc xung hợp|58–59|Giới hạn các lớp hào chính, hào biến và Nhật–Nguyệt.|
|Lại15 Tứ thời vượng tướng|59–60|12 hàng tháng/60 ô hành; giữ ba ghi chú dư khí.|
|16 Nguyệt tướng|60–66|Nguyệt kiến tác động, nguyệt phá, nhập không tạm thời, sinh/khắc/hợp; chưa có bộ xác định ranh tháng.|
|17 Nhật thần|66–69|Bốn nhãn nhật xung phụ thuộc mạnh/yếu và động/tĩnh; ngoại lệ nhật chiếm hào/nguyệt xung và các điều kiện đồng thời.|

136 đơn vị hiện có7 mục nền tảng đọc/áp một phần,12 mục đọc lần đầu toàn khoảng,1 mục khác đọc một phần (19), **116 thân mục vẫn ở mức đề mục**;0 mục nhận đã áp trọn mọi mệnh đề. Mục18 và phần còn lại của19/20 không tự được hoàn thành từ các ảnh liền kề hoặc bảng sáu cặp.

## Bảng tháng giữ đúng định tính nguồn

12 tháng từ Dần tới Sửu có12 vị trí chi vượng và16 vị trí chi “thứ/次”, tổng28 vị trí chi được nêu. “次” của chi cùng hành không bị nhầm với “相” của hành được sinh. Trong60 ô hành, **Mộc tháng Thìn, Hỏa tháng Mùi, Thủy tháng Sửu** giữ “dư khí”; các hành còn lại của tháng Tý giữ chữ “suy” thay vì tự chuẩn hóa tất cả sang “hưu tù”. Không quy đổi nhãn thành điểm số.

API nhận chi tháng nhập rõ. Tên “tháng1…12” trong dữ liệu chỉ là thứ tự in. Các đoạn vừa đọc chưa xác lập adapter lịch Gregorian/âm lịch/tiết khí, múi giờ hoặc ranh ngày; không dùng chúng để tự chuyển lịch. Bảng tháng cũng **không tự điền tổng mạnh/yếu trước nhật tác động**, vì sách xét thêm Nhật, động/biến, sinh/khắc và cứu trợ đồng thời.

## Ngăn các đường tác động không thuộc quy tắc đang đọc

Ví dụ **Khôn2 → Tấn35**, động4/6 ở PDF58–59:

- Hào biến6 Tỵ Hỏa có thể hồi đầu khắc hào chính6 Dậu Kim; không tự khắc hào biến4 Dậu Kim.
- Hào chính4 Sửu Thổ có cạnh sinh hào chính6 Dậu Kim, nhưng không được áp cạnh ấy lên hào biến4 Dậu Kim.
- Tháng Tý Thủy có thể khắc hào biến6 Tỵ Hỏa; ngày Mão có thể xung hào biến4 Dậu Kim. Hào trong quẻ không được tính ngược lại là làm tổn thương Nhật–Nguyệt.

Bộ tham chiếu dựng nút riêng cho từng hào chính/hào biến và hai bối cảnh ngày/tháng. Cạnh giữ riêng **được phép theo lớp** và **hiệu lực chưa xác định**. Giới hạn này thuộc những đoạn B02 đang đọc, không được gọi là quy tắc phổ quát cho mọi truyền bản. Các hào Phục/Phi được sách nhắc nhưng chưa tích hợp thành nút trong đồ thị mới; bộ Phục thần trước vẫn giữ riêng.

Nhật xung không mặc nhiên là phá: tĩnh mạnh → ám động; tĩnh yếu → nhật phá; động mạnh → tăng động; động yếu → tán. Thiếu tiền đề mạnh/yếu cho kết quả chưa phân định. “Hào chiếm ngày bị tháng xung” giữ cả hai quan hệ thô cùng ghi chú “phá mà không phá”; không xóa chứng cứ nguyệt xung hoặc tự nhận đã định tổng vượng suy. Phần nói xung không, xung hợp và khác biệt “tán” được lưu thành điều kiện nghiên cứu; chưa cấp tuần không/mộ/tuyệt tự động.

Sáu cặp Lục xung được đọc từ bảng PDF80, sáu cặp Lục hợp từ73; bốn nhóm Tam hợp từ77 chỉ trả **định danh đủ ba chi**, không nhận cứ có ba chi là đã hóa hành/thành cục hoặc có kết quả tốt. Chương19 tự nói có cát/hung, cần khí của Dụng, động/tĩnh, không/phá/mộ và bối cảnh; những tiền đề đầy đủ còn mở.

## Kiểm thực thi

**14/14 kiểm đạt**,140 lời gọi `HHC_ENGINE.hexNumber` thật. Sáu ví dụ cấu trúc: Khôn tĩnh; Đoài58→Quy Muội54; Khôn2→Tấn35; Cấn52→Di27; Độn33→Cấu44; Quải43→Lý10. Các chuyện y tế/tài lộc nguồn chỉ dùng để định vị cấu trúc, không xác minh kết quả dự báo.

Quét64 cấu trúc với đủ sáu hào động và chi tháng/ngày nhập rõ tạo **11.648 cặp nút có hướng**:3.840 cặp được phép theo lớp,7.808 bị khóa. Mọi cạnh vẫn giữ hiệu lực chưa xác định.144 cặp chi kiểm với đối chiếu số học độc lập;60 ô tháng,28 vị trí chi, ba dư khí và bốn định danh Tam hợp được kiểm riêng. Digest64 đồ thị: `b76ce9e44f0e8d5d01ef72fe63d1af30c8c3fe38b3b1c2b421da81a3abbfcdd6`.

Các fixture nháp nhầm tên/vị trí được sửa qua ảnh, tên quẻ in, Nạp Giáp và engine, không sửa nguồn gốc hoặc engine để khớp. Trong mã nháp, nhãn chi từng ghi đè ID nút của cạnh; kiểm ví dụ Khôn–Tấn phát hiện và đã sửa bằng các trường ID/chi riêng trước khi đóng gói. Đây là lỗi bộ tham chiếu đang phát triển, chưa từng nằm trong web phát hành.

HTML707.411 byte/SHA `549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857`, toàn JS/CSS, ba tham chiếu Lục Hào trước và ZIPweb344.047 byte giữ nguyên. Không chạy lại kiểm UI/PDF hoặc4.096 cặp nền tảng khi không đổi. Snapshot `../archives/v53-before-liuyao-day-month/` giữ gói nguồn942.482.353 byte. Manifest/gói nguồn được cập nhật bằng `--research-only`; kiểm toàn byte ở `qa/liuyao-day-month/RELEASE_RESULTS.json`.

Tiếp mục18–27, ranh cuối19, đầy đủ Lục xung/ám động/tán/không/mộ/tuyệt và quy ước ranh lịch; đối B03/nhân chứng khác cho phần đang có bất đồng. Vấn đề ngày Tân Mão/tuần không ở PDF52 của mốc trước vẫn mở; tài liệu vừa đọc không tự giải quyết nó. B02/B03 vẫn `research_only`,0 toàn tác phẩm đã áp hết; toàn kho `active-not-complete`. Nghiên cứu/corpus nằm ngoài site.
