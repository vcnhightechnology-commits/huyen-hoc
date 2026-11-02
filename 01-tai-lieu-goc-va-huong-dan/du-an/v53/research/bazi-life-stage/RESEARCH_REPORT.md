# Hai thứ tự mười hai thuật ngữ trong Tam Mệnh Thông Hội

Ngày 29/10/2026. C05 Thực thần còn thiếu căn cứ giải từ nối, nên chuyển phần độc lập đã ghi mở: định nghĩa 寄生十二宮 ở quyển hai. Đọc lại bốn ảnh native 112–115 và bốn crop có tọa độ, không tải nguồn hoặc tạo vị trí nguồn mới. Đây là mở rộng cách đọc ảnh đã có, không phải nhân chứng mới.

## Điều đọc được

Văn dẫn trước liệt kê: 長生、沐浴、冠帶、臨官、帝旺、衰、病、死、墓、絶、胎、養. Ngay sau, tác phẩm dẫn 三命提要 với thứ tự: 受氣、受胎、成形、長生、沐浴、冠帶、臨官、帝旺、衰、病、死、墓. Các số thứ tự của hai lời không được dùng thay nhau. Dẫn tên 三命提要 trong tác phẩm không chứng minh đã thu nhận hoặc đối một bản sách độc lập ấy.

Nguồn nói rõ 受氣 còn gọi 絶/胞; 沐浴 còn gọi 敗; 墓 còn gọi 庫. Hai phép ghép 受胎↔胎 và 成形↔養 chỉ là ứng viên suy luận từ ngữ/ngữ nghĩa và vị trí vòng; đoạn này không có `又曰` xác lập chúng như các biệt danh vừa nêu. Bộ tra giữ riêng hai lời, không nhận 胎 hoặc 養 như biệt danh tự động của lời 三命提要. Các tương đồng từ vựng giữa hai lời được chỉ ra theo chính chữ chung, không gọi là xác minh toàn bộ mô hình giai đoạn.

Bản số đang giữ dùng ký tự `飬` (U+98EC), bản đọc làm việc từ ảnh ghi `養` (U+990A). Kiểm nối chuỗi đầu tiên đã phát hiện khác mã này; verifier chỉ đổi cặp chữ ấy trong chuỗi đối chiếu tạm, không sửa byte nguồn hoặc tệp kỳ vọng đã đóng băng. Nhật ký ở TRANSCRIPTION_COMPARISON.json. Không dùng chuẩn hóa Unicode tổng quát để bỏ qua các dị biệt khác.

Mười hai định nghĩa được ghi là ẩn dụ lịch sử về vạn vật. `病`, `死`, `墓` không trở thành chẩn đoán hoặc dự báo thọ mệnh của người nhập. Nguồn còn nói `見生旺者未必便作吉論` và `見休囚死絶未必便作凶言`. Các nhóm `胎生旺庫`/`死絶病敗` có lời hạn chế `亦大槩言之`; không tự mở 生/旺 thành nhãn cụ thể hoặc gán nhóm thành điểm cát hung.

## Chức năng đã làm trong staging

Hai hàm nội bộ tra đúng tên hệ nguồn và thuật ngữ, hoặc lấy thứ tự nguyên danh sách. Biệt danh chỉ được nhận trong đúng lời có văn nêu rõ. Các cách viết giản thể dùng riêng trong đối bảng runtime, không tự sửa văn nguồn hoặc mở rộng API nhận mọi chữ gần giống. Không nhận ngày sinh, trụ can chi, hướng thuận/nghịch hoặc lịch làm đầu vào; đoạn này chưa cung cấp thuật xác định giai đoạn cho mười can.

Kỳ vọng và dữ liệu nguồn được đóng băng trước triển khai và runtime. Đọc thật đúng một lần bảng `LunarUtil.CHANG_SHENG` của lunar-typescript 1.8.6; 12 nhãn khớp thứ tự của danh sách mở đầu sau năm phép đổi chữ giản/phồn được ghi tường minh. Đây là một bảng đã đọc, không phải 12 lá số, không so thứ tự đánh số của lời trích như thể cùng hệ. Không chạy lịch, HHC bốn trụ hoặc iztro vì chưa triển khai phép tính ngày sinh hoặc giai đoạn can chi.

Kiểm thử giữ hai thứ tự, bốn biệt danh minh thị, hai ghép suy luận không được tự nhận, các đầu vào ngoài phạm vi, bản sao dữ liệu và kết quả thực tế luôn chưa xác lập. Kiểm nguồn đối byte/SHA, ba tệp đóng băng và bốn crop RGB. Kết quả ở TEST_RESULTS.json và SOURCE_RESULTS.json.

## Giới hạn và bước tiếp

Chưa có luật xác định chi khởi, thuận nghịch âm dương hay ngày thực cho từng can từ đoạn này. Chưa mã hóa mạnh yếu toàn lá số, dụng thần, tác dụng hay ưu tiên của các điều kiện sinh phù/chế phục. Không ghép hệ 5 nhãn mùa vụ 旺相休囚死 vào 12 thuật ngữ; chữ 夏水因 vẫn giữ theo hồ sơ cũ. C05 Thực thần vẫn chưa liên kết; ma trận Thực thần giữ 44/46/0.

Phạm vi này hiện nằm hoàn toàn trong staging. V53 và gói nguồn vừa kiểm 5.790 tệp không bị sửa trong lượt này; không đưa nghiên cứu vào site. Tiếp theo cần đối phần nguồn cung cấp tọa độ can chi cho mười can, rà bảng đang có trước khi mở bộ tính, rồi tích hợp một batch nghiên cứu có ích và đóng gói một lần. Không coi từ điển thuật ngữ là đã áp trọn chương hoặc toàn tác phẩm.
