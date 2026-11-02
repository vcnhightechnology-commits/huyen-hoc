# B03: tiết kiến tháng, ví dụ Hỏa trường sinh và Phục thần cung Càn

27/10/2026. Nghiên cứu riêng, không ở `site`. Toàn kho **active-not-complete**.

## Khoảng đã đọc và giới hạn

Giữ nguyên PDF B03 `NLC892-GBZX0301013045-259368.pdf`, 50.191.031 byte, SHA-256 `5dcd7b5005b1e86f441a9350eefb7c0e9e628c47ab926b2a7d1bdd6691a4773d`. Đây là sách in 文成堂, tiêu đề trực tiếp ghi 光緒甲辰新鐫/1904; chỉ **quyển vật lý đầu**, 60 trang PDF, không đủ toàn tác phẩm 14 quyển văn bản.

Lượt này xem 17 trang PDF 22–38: 16 render mới ở 180dpi, một trang 22 được đọc mở rộng. Không thêm HTTP hoặc PDF gốc. Đọc các bài phú/quyết cuối quyển một đến dòng kết tại PDF 33 và đầu quyển hai với hình cung Càn, phần đầu cung Khảm đến PDF 38. Các bài phú được đọc lượt đầu có giới hạn, chưa chép và biên dịch hết mệnh đề. Không gọi toàn quyển một/toàn sách đã áp dụng xong; tiền tự và phần sau trang 38 vẫn mở.

## Chức năng tham chiếu mới

`research/liuyao-b03-boundaries/named-jie-reference.mjs` nhận **tên tiết gần nhất đã được xác nhận**, tra 12 dòng “月破定例” ở PDF 33:

| Tiết | Chi tháng | Chi bị tháng xung |
|---|---|---|
| Lập Xuân | Dần | Thân |
| Kinh Trập | Mão | Dậu |
| Thanh Minh | Thìn | Tuất |
| Lập Hạ | Tỵ | Hợi |
| Mang Chủng | Ngọ | Tý |
| Tiểu Thử | Mùi | Sửu |
| Lập Thu | Thân | Dần |
| Bạch Lộ | Dậu | Mão |
| Hàn Lộ | Tuất | Thìn |
| Lập Đông | Hợi | Tỵ |
| Đại Tuyết | Tý | Ngọ |
| Tiểu Hàn | Sửu | Mùi |

Thứ tháng “chính/nguyệt…” ở đây đi cùng **tiết kiến**, không được thay bằng ngày mùng một âm lịch. API không nhận năm/tháng/ngày Gregorian, số tháng âm hoặc 24 trung khí bất kỳ. Chữ truyền thống/bản giản thể của tên tiết được chuẩn hóa minh thị. Tên tiết phải là tiết đã qua, không phải tiết sắp tới. Nguồn không cung cấp UTC/múi giờ hay độ chính xác giây của thiên văn hiện đại.

Bộ nối gắn chi tháng và cờ xung thô vào quẻ đã tính; nếu có can chi ngày minh thị thì nối tọa độ tuần không đã kiểm ở phạm vi trước. Chưa tự quyết tháng phá còn tác dụng hay không, vượng suy, chọn Dụng thần hoặc dự báo. B03 và bộ cấu trúc B02 dùng chung tọa độ đã đối, nhưng ghi rõ không tuyên bố toàn bộ luật hai sách giống nhau.

PDF 22–23 in thứ tự 12 giai đoạn và ví dụ Hỏa trường sinh tại Dần, đi thuận, Mão mộc dục, Thìn quan đới. Hàm `firePhaseAtBranch` tạo 12 tọa độ: **3 vị trí nêu trực tiếp, 9 vị trí suy ra từ thứ tự và chiều đi in trong sách**. Vì vậy Hỏa đế vượng Ngọ/mộ Tuất/tuyệt Hợi được gắn nhãn suy ra trong **khung B03**. Không dùng kết quả này âm thầm lấp hai ô Hỏa còn chưa xác lập trong phạm vi B02; bộ B02 giữ nguyên byte và giới hạn bốn pha của tác giả. Không tự dựng bảng đủ năm hành từ các nhãn hình bàn tay chưa đối hết.

## Đối chiếu Phục thần và điều kiện

Tám hình cung Càn tại PDF 34–37 được khóa theo thứ tự Càn 1, Cấu 44, Độn 33, Bĩ 12, Quán 20, Bác 23, Tấn 35, Đại hữu 14. Sáu truy vấn Phục thần có vị trí/chi/hào che đã đối engine thật:

- Cấu: Tài Dần Mộc hào 2 dưới Hợi Thủy.
- Độn: Tử Tý Thủy hào 1 dưới Thìn Thổ.
- Bĩ: Tử Tý Thủy hào 1 dưới Mùi Thổ.
- Quán: Huynh Thân Kim hào 5 dưới Tỵ Hỏa.
- Bác: Huynh Thân Kim hào 5 dưới Tý Thủy.
- Tấn: Tử Tý Thủy hào 1 dưới Mùi Thổ.

Càn/Đại hữu có đủ năm loại Lục thân; không vì hàm có khả năng liệt kê gốc cung mà tự buộc dùng thêm Phục thần. Ví dụ Quán còn bàn Kim trường sinh Tỵ; quan hệ Hỏa khắc Kim đơn thuần không đủ làm kết luận Phục thần vô dụng.

Sáu dòng tuần không tại B03 PDF 33 khớp sáu tọa độ B02 PDF 93. Các bài về động/không/Dụng–Nguyên–Kỵ ở PDF 29–30 vẫn có tiền đề vai trò, động/tĩnh, khắc và khung câu hỏi; không ép thành một cờ “không = mất tác dụng”. B03 có bài/hình **卦身** trong khoảng đã đọc, trong khi B02 có lời bác bỏ ở PDF 100. Hai lập trường được lưu riêng, chưa nhập phép tính quái thân vào khung B02. Mâu thuẫn ngày Tân Mão/lời Dần Mão không của B02 PDF 52 tiếp tục mở, không được sáu dòng tuần không giống nhau tự giải quyết.

## Kiểm chứng và gói

`node v53/scripts/verify-liuyao-b03-boundaries.mjs`: **11/11 kiểm đạt**. Chạy thật HHC: 8 lần số quẻ và 36 lần Bát Tự; chạy thật `lunar-typescript 1.8.6`: 36 lá số lịch. Kiểm hash runtime trước khi dùng. Có 12 mẫu giữa tháng và 24 mẫu cách trước/sau 12 tiết năm 2026 đúng 24 giờ, theo **quy ước kiểm hiện đại UTC+8 minh thị**. Không kiểm giây ranh tiết, không suy rằng sách cổ quy định múi giờ đó, không coi kết quả Bát Tự là bằng chứng mọi luật Lục Hào giống Bát Tự.

768 ngữ cảnh = 12 tiết × 64 cấu trúc nguồn, 4.608 cờ chi hào chính, 384 cờ xung tháng. Digest `103c0eb52ecd7062391b7c73e801e2d2647c608ce6d86594f0bc6d71d67249c2`. Tọa độ được kiểm; ứng nghiệm chuyện đời chưa xác minh.

HTML/root/site vẫn 707.411 byte/SHA-256 `549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857`, ZIP web 344.047 byte giữ nguyên. Snapshot trước phạm vi giữ ZIP nguồn 952.118.401 byte/2.177 tệp manifest. Gói nguồn hiện tại có báo cáo, script, ảnh và kết quả kiểm riêng; không đưa corpus lên trang công khai.

Tiếp B03 sau trang 38/các quyển vật lý còn thiếu, ma trận toàn đề mục B03, điều kiện mạnh yếu/chân không/phản phục và khác biệt truyền bản. B02 vẫn 136 đơn vị, 103 thân mục mức đề mục, 26 khoảng đọc lần đầu; không hạ số còn mở của B02 chỉ vì đọc một đoạn B03 tương tự. Các nhánh Mai Hoa/Bát Tự/Tử Vi/nhà ở và 40 bản ghi kho nguồn còn mở.
