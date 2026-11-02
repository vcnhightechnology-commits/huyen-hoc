# B03: đối đủ nhãn hào trong 64 hình tám cung

Ngày27/10/2026. Dữ liệu ảnh và bộ đối chiếu nằm ngoài site.

## Nguồn và bản đọc

Tái dùng sách đóng1 B03: **50.191.031byte/60trang**, SHA256 `5dcd7b5005b1e86f441a9350eefb7c0e9e628c47ab926b2a7d1bdd6691a4773d`. Không HTTP/PDF gốc mới hoặc nhân chứng khác. Cả26ảnh PDF34–59 được đọc mở rộng cho cột nhãn; không cộng26trang nguồn mới. Hai renderQA360dpi/2crop ở46/49 kiểm vị trí chú nhỏ và cột qua trang, giữ SHA.

`PRINTED_LINE_ROWS.json` chép thủ công theo ảnh: **64hình,384dòng can chi–Lục thân,128vị trí Thế/Ứng và56tọa độ Phục thần**. Chuỗi theo thứ tự ảnh trên xuống ứng với hào6→1. Nhãn 父/兄/官/財/子 là viết tắt biên tập cho 父母/兄弟/官鬼/妻財/子孫; không gọi là chép ngoại giao mọi chữ. Dòng nguồn không sinh bằng kết quả engine. Không sửa nhãn nguồn để làm khớp máy.

Sáu hình có cột qua trang:隨17ở46–47,蠱18ở49–50,蒙4ở51–52,大壯34ở54–55,萃45ở56–57,歸妹54ở58–59. Trang đầu đề có thể khác trang canchi; không lấy vị trí đầu đề làm vị trí mọi trường. Ảnh46 phân biệt申金chú quái thân ở隨 với午火子孫Phục ởhào4. Ảnh49giữ巳火子孫Phục ởhào5蠱; quái thân không thay vai trò Lục thân.

## Đối chiếu thực thi

**8kiểm đạt**. HHC thật gọi72lần:64lần kiểm danh tính sốquẻ cho64bộ giá trị tĩnh và8lần cho bốn quẻin câu3(gốc+biến). Bộ Lục hào riêng thực thi384gán canchi/Lụcthân,128vịtríThếỨng và **320truy vấn vai trò tường minh** (64×5vai trò). Bốn lớp này cần phân biệt: HHC kiểm sốquẻ; bộ riêng kiểm nhãn; nguồn in cung cấp chuẩn đối; không cộng chúng thành số quẻin độc lập hoặc engine dựbáo đã được xác thực.

Toàn384dòng canchi/Lục thân và128dấu khớp bộ riêng. 56tọa độ Phục in khớp cổng tìm Phục theo cung gốc khi vai trò cần hỏi không hiện trong sáu hào tĩnh. So cả vịtrí,chi,hành vàvai trò; không chỉ so tổng số. Kiểm không lấy quái thân申 ở隨 làm Phục, và giữ đúng巳 ở蠱. Không chỉ định Dụng có hiệu lực, không xét vượngsuy/khôngphá/ámđộng, không suy số Phục từ mọi mục tiêu không được hỏi. Mọi nguồn dòng/ca/digest nằm trong `research/liuyao-b03-line-labels` và `qa/liuyao-b03-line-labels`.

Không lặp4096mặt nạ động khi engine không đổi. Các ca ở đây là64hình in tĩnh; **chú hào biến, toàn bộ nét âm–dương, nhãn quái thân và mọi câu văn giải thích chưa được nhận đã đối hết**. Nhãn384dòng gốc không thay thế các trường ấy. Dị đầu đề筮/噬giữ hồ sơ cũ, không tự sửa theo tên quẻ chuẩn. Không xác minh kết cục chiêm nghiệm hoặc dựng ngàyGregory từ các hình.

## Bốn quẻ in của câu hỏi thứ ba

Đọc mở rộng sách6 PDF9–11, ba renderQA360dpi/bốn crop; cả bốn sơ đồ nằm trong khoảng câu3, khớp con số4của riêng câu3 trong mục lục. Không tính sơ đồ câu2còn ở bên phải trang9. `BOOK6_QUESTION3_FIXTURES.json` giữ ngày/tháng vàgiátrị hào động đọc từ ảnh:

- 申月戊辰日: 同人13hào5→離30;申→未.
- 卯月甲寅日: 困47hào1/4→節60;寅→巳,亥→申.
- 丑月戊子日: 同人13hào1/5→旅56;卯→辰,申→未.
- 寅月乙丑日: 升46hào3→師7;酉→午.

Tám lời gọi HHC xác nhận gốc/biến, bộ riêng kiểm sáu tọa độ tự biến vànăm ngữcảnh Dụng chỉđịnh. Ca升giữ cảhai vịtrí父亥2/5 để kiểm tọađộ, không tự chọn một; nguyên thần酉hào3động tự biến午hồi khắc được nhận diện với cảhai ngữcảnh. Không nhận điều này đã quyết hiệu lực cứu Dụng, chọn thời điểm hoặc xác minh lời bệnh/sinh tử của sách. Ca困có申do chính hào亥biến thành; không sửa quy tắc nguyên thần gốc thành trộn chi biến tùy ý. Bốn lời gọi lunar thật kiểm nhãn ngày vàtuầnkhông(戌亥/子丑/午未/戌亥) tại các mốc trưa dùng để duyệt vòng canchi; **không quy đổi ngày cổ sang Gregory**.

Sáu quẻin sách6 đã đối cấu trúc gồm hai ca phát hành trước vàbốn ca mới câu3; chưa đối hết mọi chú hào/điều kiện của sáu ca. Tổng131do mục lục ghi chưa là đếm toànthân sách hoặc131ca đãkiểm.

## Bảo toàn và phần tiếp theo

HTML707411byte/SHA256 `549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857`,root/site/ZIPweb và15thamchiếu Lục hào trước giữbyte. Site chỉ cóindex.html; nguồn vàQA nằm ngoài. Snapshot trước `archives/v53-before-liuyao-b03-all-annotations/` giữ sourceZIP1988642475byte/2751tệp manifest. `RELEASE_RESULTS.json` kiểm toànbyte manifest vàsourceZIP mới. Không xuất bản mạng.

Không tiếp tục gọi384dòng canchi/Lục thân/128dấu/56Phục là phần chưa làm. Tiếp các trường âm–dương/quái thân vàmệnhđề đầy đủ; sáu quẻin thực tế của18hỏiđáp đãđối cấu trúc, gồm4câu3. Tổng131là con số mục lục, chưa đếm toànthân sách. Mạnhyếu/chânkhông/ứngkỳ/hiệu lực Nguyênthần, chữthuyền sách5/kếtcuối sách6/nhânchứng độclập và ngàyB02PDF52 còn mở. B02vẫn136đơn vị/103thânmục đềmục/26khoảng đọc lầnđầu. **Chưa áp hết14quyển B03 hoặc toànkho40nguồn/bốn hướng.**
