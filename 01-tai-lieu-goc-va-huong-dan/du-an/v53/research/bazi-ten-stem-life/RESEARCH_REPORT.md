# Sinh–Tử của mười can: đối tọa độ theo đúng lớp lời nguồn

Ngày 29/10/2026. Đã đọc các đoạn mục tiêu trên 16 vị trí native mới và tái dùng ba ảnh ranh 9/10/35 đã xem trước. Đây là cùng DjVu CADAL06066038 đã giữ, không có HTTP, container hoặc nhân chứng độc lập mới. Chưa đọc trọn mọi trang hoặc mọi chữ của chương.

| Can | Chi nguồn gọi là Sinh | Chi nguồn gọi là Tử |
|---|---|---|
| 甲 | 亥 | 午 |
| 乙 | 午 | 亥 |
| 丙 | 寅 | 酉 |
| 丁 | 酉 | 寅 |
| 戊 | 寅 | 酉 |
| 己 | 酉 | 寅 |
| 庚 | 巳 | 子 |
| 辛 | 子 | 巳 |
| 壬 | 申 | 卯 |
| 癸 | 卯 | 申 |

Bảng chỉ thuộc lớp trình bày từng can ở đầu chương 論天干陰陽生死. Các đoạn 論曰, 或曰, lời dẫn các hệ và phản biện phía sau được ghi riêng; đặc biệt không lấy thuyết Thổ sinh Thân hoặc thể/dụng sinh Tỵ làm chi khởi bổ sung cho bảng này. Lập luận “một Mộc, cùng sinh tử” và kết luận 前説 cũng cần giữ nguyên ngữ cảnh trước khi xác định hệ tác giả chọn. Không tự gán tất cả các lời vào một bảng duy nhất.

Chi 巳 được ghi theo cách đọc làm việc từ ngữ cảnh địa chi ở đoạn 庚/辛; các dạng giống 己/已 trong ảnh và bản số không bị sửa byte. Ẩn dụ chết/sống của gỗ ở văn giải thích cũng không tự là nhãn giai đoạn của mọi tọa độ. Đối 己, câu vắt từ cuối ảnh19 sang đầu20; bổ sung ảnh19 và sửa danh sách dẫn chứng trong mã, giữ nguyên bảng đóng băng. Nhật ký EVIDENCE_SUPPLEMENT.json ghi rõ phần bổ sung không đổi hai giá trị tọa độ.

## Mã và kiểm chứng

`sourceBirthDeathCoordinate` buộc đúng hệ nguồn, can và chi chuẩn. Chỉ hai chi được nêu cho mỗi can trả nhãn 生/死. Một trăm tọa độ còn lại trả chưa được liệt kê trong các câu đã chọn, không mang nghĩa sai hoặc không có giai đoạn. Hàm không nội suy mười giai đoạn khác, không nhận ngày sinh, không gộp thuyết Thổ và không trả mạnh yếu, sức khỏe, thọ mệnh hoặc kết quả thực tế.

Bảng nguồn và 20 kỳ vọng đóng băng trước triển khai/runtime. Gọi thật `EightChar.prototype.getDiShi` của lunar-typescript1.8.6 đúng 20 lần với đối tượng chỉ khai báo can làm gốc và chỉ số can. Không dựng đối tượng lịch hoặc lá số giả; đây là phép chiếu tọa độ vào phương thức thật của thư viện. Hai mươi nhãn khớp với 長生/死 của lớp nguồn đã chọn. Kết quả này không xác minh toàn bộ chương, các thuyết khác hay khả năng tiên đoán.

Sáu nhóm kiểm xét đủ 120 tọa độ, giữ 20 mục nêu trực tiếp/100 mục chưa liệt kê, chặn đầu vào ngoài phạm vi và dữ liệu ngày sinh, tách thuyết Thổ, kiểm bản sao dữ liệu và đối kết quả runtime đã lưu. Không chạy lại engine khi kiểm thử.

## Trạng thái phát triển

Phần này và từ điển hai danh sách 12 thuật ngữ trong `tmp/bazi-life-stage-staging` hiện là bản phát triển nghiên cứu, chưa tích hợp vào V53 hoặc trang người dùng. Gói phát triển riêng giữ mã, ảnh và chứng cứ để xem xét trước đợt tích hợp lớn. Gói V53 5.790 tệp đã kiểm ở lượt trước vẫn giữ nguyên. Ma trận Thực thần 44/46/0 và các giới hạn C05 không đổi.

Bước tiếp: đọc đủ các trang còn thiếu của chương và định danh từng lớp dẫn/ý kết luận; chỉ xây bảng đủ 12 giai đoạn khi có căn cứ cho thứ tự và chiều. Sau đó tích hợp cùng từ điển thuật ngữ, kiểm nguồn và đóng gói V53 theo một batch hoàn chỉnh. Không lấy 20 nhãn khớp để tự sửa bộ tính người dùng hoặc công bố toàn kho hoàn tất.


## Mốc đọc liên tục bổ sung

Đã xem tám ảnh còn lại15/17/22/24/26/28/32/33, hoàn thành lượt đọc đầu liên tục27 vị trí9–35. CHAPTER_DISPOSITIONS.json định danh15khoảng biên tập gồm mở đầu,mười can vàcáclớplời. Chưa đối ngoại giao mọi chữ hay áp hết mọi mệnh đề. Kết luận前說 chưa đủ làm thuật chọn tự động;không mở toàn bảng12giai đoạn từ20tọađộ. Không gọi engine lại.
