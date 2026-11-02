# Phi Thiên–Đảo Xung: bù bốn mặt tờ và giữ riêng các giọng nguồn

Ngày 28/10/2026. Tiếp tục M01 trong V53. Web, engine phát hành và gói web nguyên byte. Nguồn, corpus, môđun tham chiếu và QA nằm ngoài site.

Đã lưu thêm bản quét [CADAL 06056481 quyển năm trên Commons](https://commons.wikimedia.org/wiki/File:CADAL06056481_三命通會·卷五.djvu): **10.808.462 byte, 230 vị trí**, SHA-256 `4f273322b3fd4339789e1408e0bbb4ea15a7956e5e508c6f99fced264e0b53ee`. SHA-1 `8dd4e5a566348ba56c2c3fb4f888dfac33349436` và kích thước khớp API. Ba body HTTP 200/TLS (API, trang mô tả ghim, DjVu) được giữ nguyên byte và header. Đây là nguồn kho gán CADAL/Chiết Giang, chưa phải byte tải từ máy chủ cơ quan hoặc chữ ký nhà xuất bản.

Đã xem trực tiếp **chín vị trí mới 187–195**, tạo **sáu crop native khớp pixel**. Hai ranh văn bản: ảnh cũ 188/93b khớp nội dung ảnh mới 188, ảnh cũ 189/96a khớp nội dung ảnh mới 193. Bốn vị trí 189–192 mới có mặt tờ **94a–95b**, bù được đoạn đứt trong bộ đối chiếu trước. Chín ảnh có bốn mặt nội dung chưa có trong khoảng ảnh cũ và năm vị trí nội dung chồng lắp. Số tờ lẻ được đọc trên ảnh; hậu tố a/b là ký hiệu mặt theo trình tự, không giả là chữ được in. Container cũ 226 vị trí giữ nguyên, chưa tuyên bố tìm toàn container hoặc sửa nó.

Hai bản có bố cục/văn bản thuộc họ Tứ Khố tương ứng. Khác byte và thêm bốn ảnh không tự thành một bản in hay nguồn học thuật độc lập. Mới xem 9/230 vị trí của bản mới; chưa hiệu khảo mọi chữ hoặc đọc hết quyển. Bản chép số cũ vẫn nguyên byte, các cách đọc can/chi 己/巳 được ghi là chuẩn hóa biên tập có khai báo.

Phân loại **17 ngữ cảnh / 1.620 codepoint** của Phi Thiên và Đảo Xung, kể cả hai tiêu đề, thơ, lời “lại nói”, phản ví dụ và lời bình kết. Ba danh sách có tên được giữ riêng:

| Giọng | Danh sách ngày nêu trong nguồn |
|---|---|
| Phi Thiên, văn xuôi | 庚子、壬子、辛亥、癸亥 |
| Đảo Xung, văn xuôi hai ngày | 丙午、丁巳 |
| Đảo Xung, đoạn “lại nói” sáu ngày | 丙午、丙寅、丙戌、丁巳、丁未、丁卯 |

Lời bình cuối Đảo Xung ưu tiên hai ngày Bính Ngọ/Đinh Tỵ; không xóa lời sáu ngày. Bộ sáu ngày không tự kế thừa các cửa kiểm của bộ hai ngày. Kiểm hiện diện 寅午戌 và số can 丙 chỉ trả tọa độ nhìn thấy, không xác nhận hợp cục hay ngưỡng 多/有力.

Lời bình cuối Phi Thiên phân biệt hai trường hợp được gọi Thương Quan và hai trường hợp không phải; đó không phải một danh sách giảm điều kiện vào cách từ bốn ngày xuống hai. Khi **khai báo tọa độ tháng cùng chi trong phép so**, bảng tàng can bản khí và hàm HHC thật cho 庚/癸, 壬/癸, 辛/壬, 癸/壬 lần lượt là Thương Quan, Kiếp Tài, Thương Quan, Kiếp Tài. Phép so không suy tháng sinh thực từ tên nhật trụ hay xác lập quy ước lịch của sách.

Sáu tọa độ cơ chế giữ đúng can Quan và chi được nhắc: 庚子→午/丁, 壬子→午/己, 辛亥→巳/丙, 癸亥→巳/戊, 丙午→子/癸, 丁巳→亥/壬. **Không thêm trụ ảo vào bốn trụ thực**. Các chi/can hợp, ràng buộc, lộ can và “điền thực” chỉ được kiểm hiện diện riêng; điều kiện hiệu lực vẫn chưa xác lập.

Nhóm sáu chi hợp được nêu chung trong câu Đảo Xung chưa tự chia vào từng nhật trụ. Với Đinh Tỵ, nguồn nêu cả 申 và 辰 trong lời ràng buộc; bảng Lục Hợp hiện hành cho đối tác của 巳 là 申. Giữ nguyên 辰 như lời nguồn với cơ chế chưa xác lập, không ép mọi “ràng buộc” thành định nghĩa Lục Hợp hoặc gọi chênh lệch này là lỗi engine. Nguồn cũng nói trường hợp Quan/Sát có lực có thể được xét theo cách khác, không được dùng mọi can Quan hiện ra làm điều kiện loại tuyệt đối.

**Tám kiểm đạt một lượt**, gồm 180 tọa độ ngày khả dĩ qua ba danh sách, kiểm phủ định chéo, dữ liệu thiếu, phạm vi và bản sao đầu ra. Gọi thật **10 hàm Thập Thần HHC** (sáu can Quan, bốn tọa độ nhãn tháng nói trên), **22 truy vấn bảng lunar** (mười tàng can, sáu xung, sáu Lục Hợp). Đây là so tọa độ; không có lá số lịch, HHC bazi, iztro, ngày sinh lịch sử hoặc kết quả vận hạn mới được xác nhận.

Ma trận 90 ngữ cảnh nay có **42 liên kết bộ phận / tiền đề / phép so**, **48 ngữ cảnh chưa có liên kết**; thêm mười cha so với ma trận 32/58 trước. Không cha hoặc toàn mục nào được xác nhận áp trọn. Mọi điều kiện phụ, giọng nguồn chưa hòa giải và hiệu lực vẫn mở; các lời phẩm trật, tai họa, sức khỏe, con cái không chuyển thành dự báo thực tế.

Khảo sát còn tìm được hồ sơ **06590 của Quốc gia Đồ thư quán Đài Loan** mô tả bản Minh Vạn Lịch sáu năm 1578, mười hai quyển/mười hai sách. Chỉ xem metadata bằng công cụ web, không giữ body byte hay xem ảnh; không lấy hồ sơ bản 1578 để chứng thực bản WYG hiện dùng, không vượt widget xác minh. Ctext trả 403 được ghi lại và không tìm đường vượt chặn. Dữ liệu khám phá giữ riêng trong `DISCOVERY.json` để tiếp tục khi có bằng chứng mới.
