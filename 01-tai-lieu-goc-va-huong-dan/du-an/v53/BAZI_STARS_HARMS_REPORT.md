# Tam Mệnh: 將星華蓋, 咸池 và 六害

Tam Mệnh quyển2: tích hợp nghiên cứu將星華蓋/咸池/六害 trong một batch. 11vị trí native204–214 riêng;9đọc đầu mới vào bản hiện hành(4từstaging cũ/5mới lượt này),209 chia sẻ. 71đơn vị biên tập/1616codepoint/1621UTF16,không71quy tắc hoàn chỉnh. Hàm tọa độ sao,điều kiện咸池 và ba hàm Lục hại giữ cặp danh nghĩa/chiều nguồn/bốn tiền đề khai báo/ví dụ乙酉→戊戌. Không ghi đè戌→酉無災 bằng hình học hợp-xung. 20truy vấn bảng đã giữ(4cũ/16mới),12Lục hợp tái dùng,0lá số. Hai bộ8+9nhóm kiểm và source checks đạt;nguồn/QA ngoài site,HTML/web nguyênbyte. Quyển2 hiện68/232vị trí xem đầu theo chỉ mục,164chưa xác lập;toànkho vẫn mở.


Phạm vi này tiếp tục ngay trong lúc kiểm gói 六合/三合, chưa đưa vào gói phát hành. Tái dùng hai ảnh 204–205 đã xem ranh; giải mã/xem mới 206–209 từ DjVu giữ sẵn, không HTTP/container mới. Hai khoảng chương là 204–207 và 207–209; 207 chia sẻ,209 có ranh sang 六害. Không suy vị trí kết thúc từ số tờ: lần chọn đầu 206–208 còn thiếu phần kết, đã bổ sung/xem209 trước freeze.

Ba mươi tám đơn vị biên tập phủ 899 codepoint/902 UTF-16 unit của bản số định vị. Giữ mã entity KR chưa giải mã và chữ dị thể, không gọi đây là chép ngoại giao mọi chữ ảnh. Tách giọng 按 trong đề mục 咸池, các tên tác phẩm lồng và lời luận ứng nghiệm. Lời về ngoại hình, đạo đức, giới tính, bệnh tật, con cái, mất người hay giàu nghèo là nội dung lịch sử chưa xác minh; không dùng làm bộ phân loại hoặc dự đoán trên web.

Tham chiếu nội bộ `sourceStarCoordinate` chiếu 中位/底庫 lên bốn nhóm chi có bằng chứng tại chương trước, ghi rõ đây là bảng tọa độ biên tập. Không tự chọn gốc năm/ngày, không xác định cục đã thành. `READING_AMENDMENT.json` sửa cách diễn đạt biên tập đầu: chưa xác lập việc toàn nhóm phải thành cục hay không, nên `requiresFullTriadFormed=null`, `fullTriadFormationEvaluated=false`. Bảng freeze đầu giữ lịch sử, không ghi đè.

Với 咸池, 按 nói rõ quan hệ chi riêng là chưa đủ, còn cần 天干納音於地同類. Chưa đủ căn cứ chọn trụ nào làm đầu vào Nạp âm; hàm chỉ nhận tiền đề nguồn khai báo true/false/null. Nhánh này không tự lấy Nạp âm năm hoặc ngày. Các đầu ra chỉ là tọa độ và một điều kiện có chọn, mọi sao hiệu lực, cách hoàn chỉnh, vượng suy, ưu tiên, kết quả/nguy cơ y khoa/ngày lịch luôn null. Điều kiện cát tinh, chính ấn, kho/mộ, lộc mã, thuần tạp, không phá/xung và các giọng trái chiều vẫn mở.

Ảnh giữ hai ví dụ 庚辰見庚辰/辛丑見辛丑 trong lời dẫn 重金重蓋. Bốn truy vấn thư viện thật đã giữ sau freeze: hai bảng Nạp âm cho 白蜡金/壁上土 và hai bảng hành can đều 金. Không được suy cả hai đều Nạp âm Kim; nghĩa chữ 金 trong lời dẫn vẫn chưa chốt. Giữ riêng lời 三命云華蓋怕金木; không chọn thứ tự ưu tiên hoặc tự hòa giải hai giọng.

Năm tệp nguồn/kỳ vọng freeze trước triển khai/runtime; ba crop đã xem khớp RGB. Tám nhóm kiểm dùng sáu ca trước triển khai,2.880 khung tọa độ,60 raw-positive,12 nhánh 咸池 được khai báo đủ/12 nhánh chưa rõ, sáu khung tọa độ chưa rõ,20.244 bất biến null,22 khung không hỗ trợ/năm đầu vào sai. Lần kiểm sau chỉ sửa chính sách chưa rõ về thành cục theo amendment, không gọi lại runtime bốn truy vấn. Test,source checks đều đạt; không lá số hoặc đối tượng lịch mới.

Chạy `node test-star-reference.mjs` và `python verify-source.py`. Không chạy lại `run-actual-once.mjs` khi dữ liệu/công thức đối chiếu chưa đổi. Sau khi nối thêm một khoảng có ích, tích hợp cùng nguồn/QA/trạng thái/báo cáo và đóng gói một lần; giữ gói 六合/三合 vừa hoàn thành. Không sửa HTML/site hoặc công bố tác phẩm đã áp trọn từ phạm vi này.



Đọc lượt đầu sáu vị trí native209–214 từ DjVu đã giữ;209 tái dùng ranh 咸池,210–214 là năm vị trí đọc mới. Lựa chọn đầu210–213 còn thiếu đoạn kết;214 được giải mã/xem trước freeze và chứa ranh sang三刑. Không HTTP/container/nhân chứng độc lập mới. Sáu PNG khớp băm RGBA;hai crop đã xem/khớp RGB. Bản số được giữ nguyên entity/glyph:33 đơn vị biên tập phủ717codepoint/719UTF16; không phải33 quy tắc nguyên tử hoàn chỉnh hoặc đối ngoại giao mọi chữ ảnh.

Ba hàm riêng trong harm-reference.mjs: nhận diện sáu cặp danh nghĩa và chiều lời văn; kiểm bốn điều kiện nguồn được khai báo true/false/null; nhận diện đúng cặp ví dụ乙酉→戊戌. Sáu dòng giải thích hợp với chi xung được giữ riêng; cách suy cơ học không ghi đè酉人見戌則凶/戌人見酉無災. Cặp chi danh nghĩa vẫn có thể đúng trong chiều được văn nguồn nói無災. Các câu này là nhãn lời văn lịch sử, không kết luận tai họa hay an toàn của người dùng. API buộc nguồn và khung tọa độ, không tự lấy năm/ngày, lập lá số hoặc đưa kết luận lên web.

午帶丑干真鬼,卯帶辰干真鬼,寅巳干神往來有鬼 và申亥納音相剋 là bốn tiền đề được chọn. Chỉ nhận giá trị nguồn khai báo; không tự gán真鬼 bằng Thập thần, can thường hay một hệ Nạp âm tùy chọn. Cát hung, vượng suy, ưu tiên, thành cách, sức khỏe, giới tính, đạo đức và kết quả luôn chưa xác minh. Các điều kiện羊刃/劫煞/官符,命宮/日時/身命宮 cùng lời貴自貴害自害 được ghi xử trí nhưng chưa thành bộ luận tổng thể.

Mười sáu truy vấn thư viện thật sau freeze:12 bảng xung và2 Nạp âm/2 hành can. Tái dùng12 bảng Lục hợp cũ,không gọi lại. 乙酉 là泉中水/can木,戊戌 là平地木/can土; vì vậy真金/真火 của ví dụ không được tự hiểu theo hai bảng hiện hành ấy. Đầu mối quyển5/10 trong TRUE_GHOST_OPEN_LEADS.json chỉ là bản số chưa đối ảnh; giữ các hệ riêng, không lấy tên giống nhau làm quy tắc đã khép.

Năm tệp bằng chứng/kỳ vọng freeze trước triển khai/runtime. Chín nhóm kiểm đạt:169khung cặp/12cặp dương có thứ tự/25khung chưa rõ;2.028khung điều kiện/38chưa rõ;3.721khung ví dụ/1khớp đúng chiều;59.180bất biến null,14khung không hỗ trợ và17đầu vào sai. Các kiểm sau không chạy lại engine. Tiếp三刑 từ214 đã xem ranh hoặc đầu mối真五行 có ảnh; không công bố chương/tác phẩm áp trọn.


## Lưu trữ và kiểm hiện hành

Không giữ full ZIP trước sửa. Nội dung trạng thái/manifest trước thay đổi đã được gom theo SHA-256 tại chỉ mục lịch sử và bảng revisions. Mỗi thư mục nghiên cứu có PROMOTION_IDENTITIES trong QA. Dùng maintenance/verify-current.py và recovery/research-release/FINAL_VERIFICATION.json; các lệnh snapshot trong báo cáo cũ chỉ là lịch sử. Staging được tiếp nhận đúng byte; các hướng dẫn tạo snapshot cũ bên trong README được thay bởi STORAGE_POLICY.md.

Tiếp: Tiếp論三刑 từ214 đã xem ranh;215trở đi chưa đọc trong phạm vi này. Giữ các tên刑 theo từng giọng,đừng lấy nhãn dân gian hiện hành ghi đè nguồn. Đầu mối真五行/真鬼 quyển5/10 mới là bản số chưa đối ảnh;không tự ghép Nạp âm,Thập thần hoặc hành can. Không gọi lại20truy vấn bảng/12Lục hợp đã giữ.
