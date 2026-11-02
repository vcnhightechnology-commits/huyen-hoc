# Tam Mệnh quyển 2: 論支元六合

Đọc lượt đầu tám vị trí 192–199 trong container CADAL06066038 đã giữ, cùng một ranh ngoài 191. Giữ ranh đề mục trên ảnh 192 và ranh sang 論支元三合 trên 199; không đoán từ số tờ. Lần chọn đầu 195–202 bắt đầu quá muộn, đã bổ sung 191–194. Ba ảnh 200–202 chỉ giải mã, chưa được xem và không tính đã đọc. Đây là chín vị trí mới được xem, không phải chín lượt tải hoặc toàn bộ quyển 232 vị trí.

Bản số Kanripo WYG ghim SHA-256 là văn bản định vị riêng với ảnh CADAL; không mặc định cùng truyền bản. Giữ nguyên bản gốc, slice thô và bản sạch 1.087 codepoint/1.090 UTF-16 unit. Mười bốn đơn vị biên tập phủ liên tục bản sạch, mỗi đơn vị có xử trí; không đồng nghĩa toàn bộ chữ ảnh đã đối hoặc mọi mệnh đề đã thực thi. Nguồn lồng tên 廣録/珞琭子/經/天元變化書 và 周禮 được giữ theo giọng dẫn; không tính thành năm tác phẩm độc lập đã tiếp nhận.

Tham chiếu nội bộ có ba hàm:

- `sourceUnionPair`: sáu cặp tọa độ, kèm nguyên cụm lời mười hai hướng theo giọng 天元變化書云. Tọa độ cặp đối xứng, cụm lời theo hướng giữ bất đối xứng; không đổi 福輕/福盛/大利 thành điểm số hay dự đoán.
- `sourceUnionMonth`: mười hai hàng tháng nguồn, 月建/địa chi của tú và tên tú đúng bản đọc. Không quy đổi ngày hiện đại, tháng nhuận/tiết khí hoặc vị trí thiên văn.
- `sourceHiddenUnion`: đúng hai ví dụ 合禄/合馬 với gốc sinh được khai báo, đích không thấy và đối tác thấy. Chỉ ba trị cho tiền đề nguồn. Không chọn gốc năm hay ngày, không xác nhận phạm vi quan sát đầy đủ và không tự áp lên mảng bốn trụ.

Chuẩn hóa tọa độ 戍→戌, 已→巳, 夘→卯 được khai báo; bản sạch nguyên chữ. Giữ câu 申為二隂六三得九數 dù số gọi tên và biểu thức cộng không nhất quán. Câu 合貴 trong ảnh có gốc giữa chưa chốt, bản số là 甲戍庚人; không tự điền 戊 hay dùng làm gốc. Danh sách 丑未/子午 chưa tự chọn AND/OR. Năm cặp 往來/隔六合 của lời 廣録, phép hóa hiệu lực, ưu tiên, hai ví dụ chỉ hai trụ, và lời nam nữ đều có xử trí mở riêng. Không dựng lá số hoặc ngày sinh lịch sử từ hai trụ.

Năm tệp dữ liệu/ảnh/kỳ vọng đã freeze trước triển khai và trước chạy thư viện. Batch thực tế chạy lunar-typescript 1.8.6 đúng tệp ghim hash, 12 truy vấn bảng HE_ZHI_6 và một truy vấn LU[甲], đều khớp tọa độ đã giữ trước; không tạo lịch/lá số. Không có kiểm đối công thức 馬, tính thiên văn hoặc kết quả sống. `ACTUAL_RUNTIME.json` giữ đầu ra; script `run-actual-once.mjs` là script lần chạy tại staging, có chặn ghi đè, không chạy lại khi kiểm gói.

Tám nhóm kiểm: 144 cặp/12 cặp có hướng thuộc danh sách; 12 truy vấn tháng và 12 cụm lời theo hướng; 10 ca kỳ vọng cụ thể; 18 khung ba giá trị; 1.218 bất biến không suy rộng; 43 khung không hỗ trợ; chín đầu vào sai; hash và phủ liên tục văn bản. Không gọi lại thư viện khi test. Ba crop chấp nhận và một crop thử loại đều khớp RGB; crop đầu ảnh 198 thiếu ngữ cảnh mép phải đã mở rộng trước freeze.

Chạy `node test-union-reference.mjs` và `python verify-source.py`. Nguồn, corpus, suy luận và QA ở ngoài site. HTML, engine công khai và web ZIP không đổi. Không coi tám ảnh đọc đầu/mười bốn xử trí là cả chương hoặc cả kho đã áp dụng hết.
