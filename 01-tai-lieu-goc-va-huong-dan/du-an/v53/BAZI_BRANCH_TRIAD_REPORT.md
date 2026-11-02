# Tam Mệnh quyển 2: 論支元三合

Đọc lượt đầu trọn khoảng chương trên sáu vị trí 199–204, kèm ranh ngoài 205. Vị trí 199 đã xem khi khép chương 六合; sáu vị trí 200–205 mới được xem trong phạm vi này. Ba PNG 200–202 đã giải mã ở phạm vi trước, được tái dùng đúng byte; bản ghi “chưa đọc” ở thời điểm freeze trước vẫn giữ lịch sử. Toàn chương đọc đầu không đồng nghĩa chép ngoại giao mọi chữ hay áp dụng hết điều kiện.

Văn bản số định vị riêng được giữ nguyên; bản sạch 807 codepoint/807 UTF-16 unit, chia 22 đơn vị có xử trí liên tục. Tách lời giải thời khắc, 精氣神, bốn nhóm ba chi, nhóm bốn chi Thổ, năm vai với gốc 丙/丁, hai ví dụ 三位禄格, các giọng dẫn và lời luận ứng nghiệm/đạo đức/nam nữ. Những nhận định về nhân cách, giới tính, ngoại hình, kiện tụng hoặc giàu nghèo là lời lịch sử chưa được kiểm chứng; không tạo bộ phân loại hoặc nội dung khuyến nghị trên web.

`sourceTriadPremises` nhận đúng nguồn, khung bốn ô địa chi được khai báo (mỗi ô là một chi hoặc null), tên nhóm, can gốc và gốc sinh nguồn khai báo. Không chọn can ngày/năm hoặc dựng lịch/lá số. Bốn nhóm ba chi xét ba chi phân biệt; 申子申 không thay cho 申子辰. Nhóm 辰戌丑未 xét đủ bốn chi riêng. Khi còn ô chưa biết, chỉ kết luận thiếu chắc nếu số chi thiếu vượt số ô chưa biết. Câu “若三字缺其一則化不成局” là điều kiện cần của nhánh ba chi: thiếu thì loại cách đọc đó, đủ tọa độ vẫn không chứng minh đã hóa thành cục. Không áp điều “ba chữ” lên nhóm bốn Thổ.

Hàm chỉ trả nhãn 印/財/本局/官局/傷局 cho 丙/丁 khi đủ tọa độ, giữ đúng vai rộng của nguồn. Không biến 傷局 thành riêng quan hệ cố định 傷官. Hai cổng tọa độ 三位禄格 chỉ ở 丙+巳酉丑 và 丁+寅午戌, không mở rộng sang tất cả can từ một công thức suy diễn. Hiệu lực, vượng suy, hành đã hóa, ưu tiên, kết quả và ngày lịch luôn null.

Ảnh 200 và bản số đều giữ “故申子申為水局”; không âm thầm sửa 申 thứ hai. Nhóm chuẩn 申子辰 có chứng cứ riêng tại đề mục 199 và bảng vai 201. Cụm 寅午戊 trong bản số được đối riêng với cách đọc ảnh 戌; bản sạch không sửa theo tọa độ chuẩn hóa. Không bổ sung một chữ giai đoạn còn thiếu từ chu kỳ hiện đại.

Năm tệp nguồn/kỳ vọng được freeze trước triển khai và runtime. Batch thật chạy HHC_BAZI_RELATIONS.god cho 20 cặp can khai báo, cùng hai truy vấn bảng Lộc lunar 1.8.6 cho 丙/丁. Tất cả khớp kỳ vọng đã giữ; không có đối tượng lịch/lá số. Bốn tọa độ hành Thổ của hai can gồm hai Thực Thần và hai Thương Quan, minh họa khác biệt vai rộng 傷局 với tên Thập thần phân âm dương; không phải lỗi engine. Không suy hiệu lực từ khớp tọa độ.

Tám nhóm kiểm dùng 12 ca trước triển khai, 20.736 khung bốn chi đã biết/103.680 truy vấn năm nhóm, đối tổng độc lập theo tổ hợp: mỗi nhóm ba chi có 252 khung đủ, nhóm bốn Thổ có 24. Thêm 71 khung thiếu dữ kiện, 726.341 bất biến không suy rộng, 18 khung không hỗ trợ và tám đầu vào sai. Ba crop chấp nhận khớp RGB; ba crop thử cắt phạm vi đã giữ và loại trước freeze. Test/kiểm gói tái dùng đầu ra thật, không gọi engine lần nữa.

Chạy `node test-triad-reference.mjs` và `python verify-source.py`. Script runtime là hồ sơ lần chạy tại staging, có chặn ghi đè, không dùng làm lệnh chạy lại. Nguồn, corpus, phòng kiểm định và so engine ở ngoài site. Chương 玉井 cuối còn thiếu thước đo hữu lực/đa kiến, hư hỏng 巳宫 và hợp hiệu lực; các phần này cùng mọi ưu tiên và kết quả sống vẫn mở.


Tích hợp cùng phạm vi 六合 trong một lần đóng gói; xem BAZI_BRANCH_COMBINATIONS_REPORT.md và qa/bazi-branch-combinations/RELEASE_RESULTS.json.
