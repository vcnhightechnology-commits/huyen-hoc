# Bát tự: vị trí Thập thần và lời đọc trong bản xuất — V53

Ngày hoàn thành phạm vi: 26/10/2026. Tài liệu nội bộ; nguồn sách, ảnh và báo cáo không đưa vào thư mục `site/`.

## Thay đổi cho người dùng

Trong Bát tự → Thập thần & tàng can → **Đọc các quan hệ và vị trí xuất hiện**, mỗi quan hệ nay có hai nhóm riêng: **Can lộ** và **Trong tàng can**. Từng dòng chỉ đúng trụ, can và chi liên quan; bản khí được ghi rõ. Can ngày là Nhật chủ để đối chiếu, không được đếm thêm thành một vị trí Tỷ Kiên lộ can. Khi chưa rõ giờ, chỉ ba trụ đã biết được trình bày; ngày có trụ bất định tiếp tục chặn phần đọc này.

Đã tái hiện lỗi của bản trước: khi phần lời đọc đang thu gọn, TXT không chứa câu diễn giải Chính Quan có trên web. Khối này nay dùng cơ chế mở tạm khi xuất TXT hoặc in, rồi khôi phục trạng thái ban đầu. Không cần người dùng mở từng khối trước. PDF cũng giữ đủ vị trí và lời đọc; tiêu đề đại vận đi cùng đoạn nội dung thay vì nằm riêng cuối trang.

Thông tin mới mô tả vị trí trong sơ đồ. Không chuyển sự hiện diện, số lần xuất hiện hoặc bản khí thành điểm vượng suy, kết luận cách cục hay dụng thần. Các câu diễn giải đã có giữ nguyên. `engine.js`, `app.js`, mô-đun đại vận, vận hạn, nhà ở và dữ liệu Kinh Dịch giữ byte so với snapshot trước phạm vi.

## Nguồn thực sự đã khai thác

Không tải thêm sách trong lượt này. Tái dùng PDF **評註淵海子平** đã lưu, ấn bản 1926 theo [hồ sơ NTL-9900014379](https://taiwanebook.ncl.edu.tw/zh-tw/book/NTL-9900014379), 90.837.030 byte, SHA-256 `664bccd1ea4706c609df8ea6cd69a4565db97dc277e876fc22eb125ea41dcc9f`. Ba ảnh trang PDF 109–111 là ảnh render cục bộ từ PDF, không gọi là byte ảnh tải gốc từ cơ quan.

Đọc thêm bốn đơn vị có mục tiêu trên ba trang ấy: mười cặp can Thương Quan ở chú in phía trên; ví dụ can năm/tháng/giờ lộ Thực; một cặp Giáp–Nhâm Thiên Ấn trong chú; và các đoạn về Quan lộ/ngữ cảnh Thương Quan. Phân biệt chính văn với chú in. Mười một cặp quan hệ mới đọc khớp HHC và bảng thư viện thật. Không đưa lời phán tính cách cổ vào kết quả người dùng.

Đọc thêm hai mệnh đề của **bản chép số WYG** Tam Mệnh Thông Hội quyển 5: `005-5b` phân biệt chi tàng/can thấu và `005-68b` giới hạn cách gọi Đảo Thực khi không có Thực. Tệp Kanripo ghim commit `7db72e5553de6ee4c45ed3980c6c67f8a6e451bf`, SHA-256 `1ebdd92feaa57496b702f962ad6fafd4f19c17e98c38a94b40f626ef321dd997`. Hai mệnh đề này **chưa được đối ảnh WYG trong lượt này**.

Hồ sơ chính xác: `research/bazi-relation-locations/MANUAL_READINGS.json`, `SOURCE_AUDIT.json` và `RUNTIME_COMPARISON.json`. Có bốn phản ví dụ chạy thật để tách Thiên Ấn khỏi Đảo Thực, Quan tàng khỏi Quan lộ, quan hệ chỉ lộ can và quan hệ cùng có ở hai lớp. Không gọi bốn đơn vị đọc là hoàn tất mười mục cách cục hoặc toàn tác phẩm.

## Kiểm chứng bằng chương trình thật

- **16/16 kiểm nguồn và mô-đun đạt.** Thực thi lunar-typescript **1.8.6** đã giữ trong V46, kiểm lại byte của package và tệp thực thi theo audit cũ. Đây là xác nhận định danh tệp cục bộ, không phải chữ ký nhà phát hành hay một lần tải mới.
- **240 lá số thật**: 60 ngày liên tiếp từ 09/08/2018, mỗi ngày lúc 00:30, 08:30, 16:30 và 22:30, UTC+8, đổi ngày lúc nửa đêm. So cả bốn trụ trước rồi mới so quan hệ qua API Thập thần/can tàng của thư viện: **3.020 vị trí khớp**, phủ đủ mười quan hệ ở cả hai lớp. Không suy rộng sang mọi múi giờ hoặc mọi giờ.
- Ba ca chưa rõ giờ, hai ca trụ bất định, bốn phản ví dụ; kiểm không đột biến dữ liệu. Bỏ trường vị trí mới thì các trường và lời đọc cũ khớp bản trước trên 240 ca.
- **21/21 kiểm trình duyệt đạt**: TXT mặc định thu gọn và mở sẵn, vị trí cụ thể, lưu/mở bằng tính lại từ đầu vào, không dựng giờ khi thiếu, phục hồi trạng thái trước/sau in, xóa kết quả khi sửa đầu vào, không tràn ngang ở 320/390/768/1440 px. Không có yêu cầu HTTP hoặc lỗi JavaScript trong bản HTML độc lập.
- PDF cuối **bảy trang**, đã render và xem đủ; có cả hai lớp vị trí và câu diễn giải từng bị thiếu. Form, ảnh đầu trang, nút thao tác và dữ liệu nghiên cứu không xuất hiện. Tiêu đề nguyệt lệnh không bị tách khỏi đoạn đầu. Chứng cứ cuối mang tiền tố `final-print-`; các ảnh `print-page-*` và `print-contact.png` là bản render thử cũ bằng chế độ màn hình, không dùng để kết luận bản in.

Tổng hai bộ kiểm chính: **37/37 đạt**, kèm kiểm văn bản PDF và xem ảnh thủ công. Script tái chạy: `scripts/verify-bazi-relation-locations.mjs`, `scripts/verify-bazi-relation-locations-browser.mjs`, `scripts/verify-bazi-relation-locations-pdf.py`. Script tái hiện lỗi cũ: `scripts/check-bazi-relation-export-before.mjs`. QA: `qa/bazi-relation-locations/`.

## Sai khác giờ Tý muộn còn mở

Đối chiếu riêng **09/08/2018 23:30, UTC+8, đổi ngày lúc nửa đêm**: HHC trả `戊戌 庚申 癸酉 壬子`; lunar-typescript với `EightChar.setSect(2)` trả `戊戌 庚申 癸酉 甲子`. Ba trụ đầu khớp, can giờ khác. Đây là sai khác quy ước có sẵn, được giữ riêng ngoài 240 ca khớp; không đổi bộ tính trong lượt này.

Cần đối nguồn về can giờ Tý sớm/muộn, đọc chính xác quy tắc của thư viện và xác định chính sách sản phẩm trước khi hợp nhất. Không lấy lựa chọn sect của ngày làm bằng chứng tự động rằng thư viện cũng đổi quy tắc can giờ. Mười mục cách cục, vượng suy/dụng thần, các dị bản Tử vi, năm/Phi tinh nhà ở và phần hiệu khảo Kinh Dịch còn lại vẫn mở.

Đã nghiên cứu tiếp cơ chế cụ thể trong `research/bazi-late-zi/REPORT.md`: tài liệu chính thức, test upstream và triển khai thật đều xác nhận thư viện dùng ngày kế để tính giờ Tý muộn trong cả hai sect. 9/9 kiểm nghiên cứu, 7.936 phép so bao gồm đủ 60 phút ở 62 ngày: chính sách 23 giờ khớp; chính sách nửa đêm khác đúng 3.720 mốc Tý muộn. Ba mã trang WYG về nửa giờ Tý và phép khởi giờ mới đọc ở bản số, chưa đối ảnh và chưa trực tiếp phân định ngoại lệ can giờ. Bộ tính sản phẩm vẫn giữ nguyên.

## Phát hành cục bộ

Giữ V53. Snapshot trước phạm vi: `../archives/v53-before-bazi-relation-locations/`, gồm HTML, hai ZIP, manifest và mô-đun cũ. Nguồn sửa trực tiếp tại `bazi-relations.js`, CSS mới `bazi-locations.css`; build nhúng đầy đủ vào HTML độc lập. Bản gốc, `v53/Huyen_Hoc_Cac.html`, `site/index.html`, ZIP web và ZIP nguồn được đồng bộ và kiểm lại theo manifest khi đóng gói. `site/` chỉ chứa `index.html`; ZIP web chỉ có HTML và hướng dẫn. Kết quả kiểm phát hành cuối ở `qa/bazi-relation-locations/RELEASE_RESULTS.json`. Không triển khai lên mạng.
