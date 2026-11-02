# Nghiên cứu tiếp: 將星/華蓋 và 咸池

Phạm vi này tiếp tục ngay trong lúc kiểm gói 六合/三合, chưa đưa vào gói phát hành. Tái dùng hai ảnh 204–205 đã xem ranh; giải mã/xem mới 206–209 từ DjVu giữ sẵn, không HTTP/container mới. Hai khoảng chương là 204–207 và 207–209; 207 chia sẻ,209 có ranh sang 六害. Không suy vị trí kết thúc từ số tờ: lần chọn đầu 206–208 còn thiếu phần kết, đã bổ sung/xem209 trước freeze.

Ba mươi tám đơn vị biên tập phủ 899 codepoint/902 UTF-16 unit của bản số định vị. Giữ mã entity KR chưa giải mã và chữ dị thể, không gọi đây là chép ngoại giao mọi chữ ảnh. Tách giọng 按 trong đề mục 咸池, các tên tác phẩm lồng và lời luận ứng nghiệm. Lời về ngoại hình, đạo đức, giới tính, bệnh tật, con cái, mất người hay giàu nghèo là nội dung lịch sử chưa xác minh; không dùng làm bộ phân loại hoặc dự đoán trên web.

Tham chiếu nội bộ `sourceStarCoordinate` chiếu 中位/底庫 lên bốn nhóm chi có bằng chứng tại chương trước, ghi rõ đây là bảng tọa độ biên tập. Không tự chọn gốc năm/ngày, không xác định cục đã thành. `READING_AMENDMENT.json` sửa cách diễn đạt biên tập đầu: chưa xác lập việc toàn nhóm phải thành cục hay không, nên `requiresFullTriadFormed=null`, `fullTriadFormationEvaluated=false`. Bảng freeze đầu giữ lịch sử, không ghi đè.

Với 咸池, 按 nói rõ quan hệ chi riêng là chưa đủ, còn cần 天干納音於地同類. Chưa đủ căn cứ chọn trụ nào làm đầu vào Nạp âm; hàm chỉ nhận tiền đề nguồn khai báo true/false/null. Nhánh này không tự lấy Nạp âm năm hoặc ngày. Các đầu ra chỉ là tọa độ và một điều kiện có chọn, mọi sao hiệu lực, cách hoàn chỉnh, vượng suy, ưu tiên, kết quả/nguy cơ y khoa/ngày lịch luôn null. Điều kiện cát tinh, chính ấn, kho/mộ, lộc mã, thuần tạp, không phá/xung và các giọng trái chiều vẫn mở.

Ảnh giữ hai ví dụ 庚辰見庚辰/辛丑見辛丑 trong lời dẫn 重金重蓋. Bốn truy vấn thư viện thật đã giữ sau freeze: hai bảng Nạp âm cho 白蜡金/壁上土 và hai bảng hành can đều 金. Không được suy cả hai đều Nạp âm Kim; nghĩa chữ 金 trong lời dẫn vẫn chưa chốt. Giữ riêng lời 三命云華蓋怕金木; không chọn thứ tự ưu tiên hoặc tự hòa giải hai giọng.

Năm tệp nguồn/kỳ vọng freeze trước triển khai/runtime; ba crop đã xem khớp RGB. Tám nhóm kiểm dùng sáu ca trước triển khai,2.880 khung tọa độ,60 raw-positive,12 nhánh 咸池 được khai báo đủ/12 nhánh chưa rõ, sáu khung tọa độ chưa rõ,20.244 bất biến null,22 khung không hỗ trợ/năm đầu vào sai. Lần kiểm sau chỉ sửa chính sách chưa rõ về thành cục theo amendment, không gọi lại runtime bốn truy vấn. Test,source checks đều đạt; không lá số hoặc đối tượng lịch mới.

Chạy `node test-star-reference.mjs` và `python verify-source.py`. Không chạy lại `run-actual-once.mjs` khi dữ liệu/công thức đối chiếu chưa đổi. Sau khi nối thêm một khoảng có ích, tích hợp cùng nguồn/QA/trạng thái/báo cáo và đóng gói một lần; giữ gói 六合/三合 vừa hoàn thành. Không sửa HTML/site hoặc công bố tác phẩm đã áp trọn từ phạm vi này.
