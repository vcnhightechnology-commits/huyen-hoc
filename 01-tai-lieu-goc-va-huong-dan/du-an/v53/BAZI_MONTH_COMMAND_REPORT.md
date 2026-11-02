# Nhân nguyên tư sự: giữ riêng hai bảng phân ngày và lời phê bình

Ngày 28/10/2026. M01 tiếp tục ở V53. Phạm vi này không tạo phép chọn can tư lệnh theo ngày sinh và không thay bảng tàng can hiện hành.

Tái dùng DjVu quyển hai CADAL 06066038 đã tải/kiểm ở phạm vi trước; 0 HTTP, 0 container mới. Giải mã native **chín vị trí 65–73**: tám vị trí có phần chương Nhân nguyên tư sự 66–73 và một ranh ngoài 65. 73 gồm lời kết chương và đầu mục tiếp theo, không tính đã đọc trọn chương tiếp. Tổng hai phạm vi quyển hai hiện có **17/232 vị trí được xem**, chưa toàn quyển. **Sáu crop mới đã xem và khớp pixel**.

Chép trực tiếp **hai danh sách có tên**, mỗi danh sách 12 tháng, tổng **24 hàng/69 mục phân ngày**. Danh sách văn xuôi và bảng dẫn theo *Ngọc Tỉnh* khác số ngày lẫn thành viên. Nhãn 艮土/坤土 trong văn xuôi được giữ nguyên, chưa tự chuyển thành Mậu hoặc Kỷ; các vị trí can đất có dạng chữ 己/已/巳 được đọc chuẩn hóa Kỷ theo vai trò mười can và ghi rõ là biên tập, không sửa byte nguồn.

Kiểm số trên ảnh cho thấy văn xuôi cộng **360** ngày; bảng dẫn *Ngọc Tỉnh* cộng **358**: tháng Dậu 20+7+5=**32**, tháng Tý 18+5+3=**26**. Lời giới thiệu ghi tám can mỗi can 35 ngày, Mậu/Kỷ mỗi can 50 ngày, tính thành **380**, nhưng câu in vẫn ghi tổng 360. Giữ nguyên các số và chỉ ghi phép cộng; chưa đủ căn cứ kết luận số nào do in sai hoặc cách sửa. Không ép mỗi hàng về 30 hay tổng về 360.

Phần dẫn Túy Tỉnh Tử và lời bình sau bảng nói một khung khác: bốn hành mỗi hành 72 ngày, Thổ bốn mùa mỗi phần 18 ngày; tiếp theo phê cách gò khí vào giới hạn ba/năm/bảy ngày và bàn chủ–khách, đầu–giữa–cuối. Đây là lập trường nguồn và các cách trình bày khác nhau, chưa phải đồng thuận hoặc phép lịch đã xác minh. Lời kết “chi trung sở tàng chỉ dĩ nguyệt luận…” được giữ trong ngữ cảnh lập luận này; không dùng để xóa tàng can năm/ngày/giờ ở chức năng đang dùng.

API riêng yêu cầu tên nguồn, biến thể, chi tháng và khung **danh sách phân ngày nguồn**. Nó trả nguyên hàng và tổng cộng, không giả định thứ tự in là chuỗi thời gian để cộng dồn ngày. Chọn khung tàng can cố định/ngày lịch thực hoặc thiếu biến thể thì không trả hàng. Can tư lệnh thực, độ lệch ngày từ tiết, trọng số chuẩn hóa, ưu tiên truyền bản, toàn vượng suy và kết quả thực đều để trống.

**Năm kiểm đạt**, gồm **24 truy vấn thật bảng tàng can lunar-typescript** để đối các hệ dữ liệu: sáu bộ can trùng, 16 bộ khác, hai bộ chưa thể đối chính xác vì có 艮土/坤土. Đây là khác loại danh sách, **không phải 16 lỗi engine** hoặc kiểm chứng hiệu lực tư lệnh. Ví dụ bảng nguồn tháng Tý có Nhâm–Quý hoặc Quý–Nhâm–Tân, trong khi bảng tàng can cố định có Quý; không ghi đè bên nào để ép khớp. Không chạy lá số lịch, HHC hoặc iztro vì không đối phép lịch mới.

Một số dữ liệu chỉ là tọa độ nguồn có giới hạn: cần tiếp tục ấn bản khác, vai trò bảng in, cách chia đầu–giữa–cuối và ranh tiết/ngày trước khi có bộ chuyển ngày thực. Bảng mùa vụ 25 ô trước vẫn giữ 夏水因 chưa phân loại; đọc chương phân ngày này chưa giải quyết chữ đó hoặc toàn phương pháp khí lực. Thực Thần vẫn chín ngữ cảnh chọn một phần/81 chưa vào môđun; các chương khác, Nhà ở, Tử vi và Dịch còn mở.

Giữ mọi bản đã hoàn thành. HTML độc lập/site sạch/ZIP web/engine nguyên byte. Nguồn, bảng, phép cộng và QA nằm ngoài site; không xuất bản mạng.
