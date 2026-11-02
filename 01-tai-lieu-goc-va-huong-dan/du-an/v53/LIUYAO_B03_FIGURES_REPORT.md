# B03: vị trí 64 hình quẻ và điều kiện tra Phục thần

27/10/2026. Tài liệu nghiên cứu ngoài `site`; toàn kho **active-not-complete**.

## Đọc ảnh và ma trận độ phủ

Đã xem hết khoảng văn bản quyển hai của sách vật lý B03 đang có: PDF 34–59, 26 trang chứa 64 hình quẻ và lời bàn; PDF 60 là bìa/kết có dấu lưu trữ, không phải niên đại xuất bản. Lượt này thêm 22 render (21 nội dung + 1 bìa), đọc mở rộng 5 trang 34–38 đã giữ, tổng 27 bản ghi ảnh và hai crop PDF 59. Giữ nguyên PDF gốc/SHA từ phạm vi trước; không HTTP hoặc PDF gốc mới.

`FIGURE_LOCATOR.json` định vị 64 hình theo tám cung/thứ tự tám giai đoạn, bằng vị trí thực đọc trên ảnh. Cung Khảm đủ Khảm 29–Tiết 60–Truân 3–Ký tế 63–Cách 49–Phong 55–Minh di 36–Sư 7; Tỷ 8 thuộc cung Khôn. Một lượt render QA 360dpi bổ sung và crop PDF 49 đọc đầu đề **火雷筮嗑**, giữ chữ 筮 riêng với tên chuẩn hóa 噬嗑/số 21; quan hệ dị bản vẫn chờ đối nguồn khác. Không coi tên chuẩn hóa là bản chép ngoại giao. Tổng crop QA giữ: ba; 22 render trang nội dung/bìa và một render QA bổ sung được phân biệt.

Đã khép **lượt đọc khoảng quyển hai**, chưa đối ngoại giao đủ 384 chú hào hoặc biên dịch mọi mệnh đề. Tiền tự/nhập môn còn đọc có giới hạn, nên chưa gọi cả sách vật lý đã đọc hết; sách hiện có chỉ là quyển vật lý đầu của tác phẩm 14 quyển văn bản. B02 vẫn 136 đơn vị/103 thân mục đề mục/26 khoảng đọc lần đầu, không giảm số mở của B02 vì đọc nguồn song song.

## Quy tắc đã thêm

Cuối PDF 59 giải thích khi nào tìm Phục thần: khi trên hào chính và những hào thực sự biến chưa có loại Lục thân cần xét mới tra gốc cung theo ví dụ. Nếu loại đó đã hiện trên chính/biến, không mặc định mở thêm phép chọn Phục thần.

Bộ riêng `availability-reference.mjs` yêu cầu **loại Lục thân cần tìm đã được chỉ rõ**. Hàm trả các tọa độ hiện/biến, cờ có cần tìm ở tầng hình quẻ, danh sách gốc cung nếu chưa thấy, và dữ liệu gốc cung chẩn đoán tách riêng. Nhiều hào cùng loại không tự chọn một hào. Không quyết hiệu lực Dụng thần, vượng suy, ứng kỳ, tác dụng Nhật–Nguyệt hoặc phép quái thân. Không tuyên bố khung B02 có mọi ưu tiên giống B03.

Ví dụ in trực tiếp: Độn 33 tĩnh thiếu Tài nên có thể tra Tài Dần Mộc 2 ẩn dưới Ngọ Hỏa. Nhưng Độn động hào 1 thành Đồng nhân 13, hào 1 Thìn Thổ Phụ mẫu biến ra **Mão Mộc Thê tài**. Văn bản chọn Tài Mão hiện trong biến, không nhìn Tài Dần ẩn. Bộ mới tái lập đúng ví dụ, tránh đưa Phục thần lên làm lựa chọn mặc định dù biến hào đã có đối tượng cần tìm.

## Đối chiếu mới và kiểm thực thi

Thêm 13 vị trí Phục thần in ở bảy cung ngoài Càn: Cách, Lý, Tiệm, Thăng, Gia nhân, Di, Đỉnh, Mông, Tụng, Phục, Hàm, Tiểu quá, Quy muội. Từng ca khóa loại Lục thân, vị trí, chi ẩn, chi che và quan hệ sinh/khắc/tiết; quan hệ này không tự là kết luận sử dụng được. Sáu ca cung Càn của phạm vi trước giữ nguyên, không cộng lại như ca mới.

`node v53/scripts/verify-liuyao-b03-figures.mjs`: **9/9 kiểm đạt**, **79 lần gọi số quẻ HHC thật** (64 hình + 13 vị trí + hai quẻ của ví dụ động biến). Có đối chứng Độn tĩnh/Độn→Đồng nhân, đã hiện Lục thân ở hào chính, nhiều hào cùng loại, không dựng biến hào từ hào tĩnh, và từ chối ngữ cảnh lịch/quái thân chưa hỗ trợ. Không chạy lại ma trận lịch 60 ngày hoặc 4.096 cặp cũ để tăng số kiểm.

Digest bản đồ vị trí 64 hình: `dad9db9b9d05ae47a91d0fadb0aa11fac06bfd09f7f79db945a654a3d951e193`. Đây là kiểm tọa độ và điều kiện tìm ở tầng hình quẻ, không phải kiểm ứng nghiệm dự đoán.

HTML/root/site giữ nguyên 707.411 byte/SHA-256 `549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857`; ZIP web 344.047 byte. Snapshot trước phạm vi giữ ZIP nguồn **984.235.159 byte**, manifest 2.208 tệp. Bộ hiện tại, báo cáo, ảnh, hash và QA nằm trong gói nguồn riêng; không xuất bản mạng.

Tiếp: đối kỹ 384 chú hào/các mệnh đề hiệu lực còn lại, dị bản đầu đề số 21 đã đọc 筮, toàn nhập môn/tiền tự nếu cần xác lập phương pháp; tìm đúng các sách vật lý tiếp theo để đọc quy tắc hoàn chỉnh. Giữ mở khác biệt quái thân, vượng suy/chân không/phản phục/tầng quẻ so tầng hào, mâu thuẫn ngày B02 PDF 52 và các nhánh khác của kho. Không tuyên bố B03, bốn hướng, hay toàn kho đã hoàn tất.

Đầu mối lượt sau: [Commons, NLC892-GBZX0301013045-259365, 第2冊](https://commons.wikimedia.org/wiki/File:NLC892-GBZX0301013045-259365_%E5%8D%9C%E7%AD%AE%E6%AD%A3%E5%AE%97_%E5%8D%81%E5%9B%9B%E5%8D%B7_%E7%AC%AC2%E5%86%8A.pdf). Mới tìm được trang nguồn qua tra cứu, **chưa tải PDF/giữ body API/chốt hash hoặc đọc nội dung**. Phải lấy revision/imageinfo và byte thật, rồi đối trang đầu/ranh quyển trước khi coi là nối tiếp đúng bản; không cộng đầu mối này vào 0 HTTP body/PDF mới của phạm vi hiện tại.
