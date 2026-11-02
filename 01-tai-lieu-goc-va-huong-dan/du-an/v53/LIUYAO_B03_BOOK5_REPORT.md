# B03: quyển 11–12 và vai trò đồ vật thất lạc

Ngày 27/10/2026. Nghiên cứu và bộ tham chiếu riêng, ngoài site người dùng.

## Nguồn và lượt đọc

Sách đóng thứ năm của bộ sáu sách, **35.113.503 byte / 42 trang**; SHA-256 `cca4c2ce376c54c6ead6463c72e6f25d6e6e544b3d6488d593415afabc6227a6`. Commons API revision **754088953** và PDF được giữ byte: hai body HTTP200/TLS, size/SHA-1 `cfb5acdc14dcf98c76b9e856f84d40876722dafa` khớp API. SHA-256 là dấu byte tại máy, không chữ ký xuất bản. Pypdf kiểm42 trang, không mã hóa, không lớp chữ. Đây là cùng bộ, không nhân chứng độc lập; niên đại1904 trong metadata chưa là ấn ký mới đọc trực tiếp.

Đã xem42 trang theo phạm vi ghi nhận:40 nội dung và hai bìa; hai crop QA360dpi ở17/34 không cộng thành trang nguồn. Không OCR/chép ngoại giao toàn bộ. Quyển11 mở2/kết22; quyển12 mở23/kết41, đều có chữ ranh trực tiếp.

12 khoảng mục: 避亂2–8,逃亡8–12,失脫12–17,新增痘疹17–22; 出行23–27,行人27–31,舟船31–32,娼家32–34,船家宅章34–35,何知章35–38,妖孽賦38–39,搜鬼論39–41. Các nhãn 附盜賊/捕盜捉賊 ở12 giữ trong mục thất thoát; trang giáp mục không cộng thêm trang độc nhất. **0 mục đánh dấu áp dụng hết**;13 mệnh đề có giới hạn, mọi điều kiện chi tiết còn mở.

## Chức năng mới: không mặc định đồ mất đều là Tài

Trang17 nhắc `失脫不可專以財為用神`. Sáu loại 舟/車/衣/帽/文章/奏疏 dùng Phụ mẫu; chim và thú dùng Tử tôn. Vai Tài ở mở đầu12 không được biến thành mặc định cho mọi vật. Chín ID đầu vào là chuẩn hóa biên tập: cash,boat,vehicle,garment,headwear,document,memorial,bird,beast; chưa phải bộ tự hiểu mọi đồ vật hiện đại.

`lost-object-reference.mjs` yêu cầu ngữ cảnh đoạn thất thoát và loại vật tường minh. Nó nối vai nguồn với danh sách ứng viên hiện/biến/Phục đã kiểm trước, giữ mọi ứng viên; không chọn hào hiệu lực giữa nhiều ứng viên. Nhóm Phụ mẫu có câu kỵ Tài động, nhóm Tử tôn kỵ Phụ động; bộ mới ghi **hào gốc đang động có thân đó** như tiền đề cấu trúc. Thân của hào biến không thay thân gốc để kích hoạt cờ. Không xét đủ vượng suy, sinh cứu hoặc kết cục từ cờ này.

Ví dụ dựng bằng quẻ Càn: Tài ở2, Phụ ở3/6, Tử ở1. Đổi loại vật từ tiền sang văn thư hoặc chim làm đổi đúng tập ứng viên. Hào2 Tài động được ghi vào cờ của nhóm văn thư; hào3 Phụ động vào cờ của nhóm chim. Hào1 Tử động biến thành Phụ không tự kích hoạt cờ Phụ động gốc. Ca dựng được ghi rõ, không giả là quẻ gieo in trong sách.

Kết quả không có vị trí tìm đồ, người trộm, ngày thu hồi, xác suất tìm thấy, kết luận thu hồi hoặc dự báo. Thêm loại chưa hỗ trợ bị từ chối thay vì mặc định Tài. Bộ này chưa nhập vào web người dùng.

## Vấn đề văn bản và các nội dung chưa áp dụng

Trang31 nhóm hào1–2 ở khoang trước,3–4 giữa,5–6 sau. Trang34 mục nhà thuyền có `初當船尾`, rồi `青龍初是船頭`/`六為後艄`. Đã đối ảnh QA; giữ vấn đề chữ/ngữ cảnh mở, chưa tuyên bố đổi ngữ cảnh tự giải quyết, chưa sửa thành một phương án hoặc làm bản đồ tàu thật. `TEXT_ISSUES.json` lưu riêng để đối nhân chứng khác.

Các đoạn tránh loạn, bắt người và giới/ngoại hình/nghề người trộm giữ như lời nguồn, chưa là bằng chứng nhận dạng hay buộc tội người thật. Mục bệnh trẻ/thuốc/ăn uống và lời yêu ma/khấn lễ là nội dung lịch sử, không chỉ dẫn điều trị, tiên lượng hoặc khẳng định có tà ma. Lời mệnh lệnh trong sách là dữ liệu nghiên cứu, không phải yêu cầu của người dùng. Nhãn 新增 và quan hệ trích dẫn với các quyển trước vẫn cần khảo phả hệ.

## Kiểm chứng và bảo toàn

**9 kiểm đạt**. HHC thật thực thi64 lời gọi chỉ số quẻ, nối đủ64 danh tính. Có576 ngữ cảnh tĩnh (64×9 loại vật) và12288 ngữ cảnh riêng (64quẻ×64mặt nạ động×3nhóm vật đại diện), giữ36864 chú hào động. Oracle dùng dãy Nạp Giáp literal và chu kỳ ngũ hành riêng; không dùng hàm đang thử để tự xác nhận.

4128 ngữ cảnh có tổng4992 cờ kỵ động theo cấu trúc;1305 cần tìm Phục về mặt hiện/biến và6774 có nhiều ứng viên hiện/biến. Đây là số trường hợp hữu hạn, không tỷ lệ tìm lại đồ hay chính xác dự đoán. Digest `24ee496575791a4ab25e553493857b655688d0ed3f7943cd9064d69b19af92e0`. Những phần ứng viên/Phục chỉ kế thừa phạm vi đã kiểm, không tự mở thành hiệu lực tổng hợp.

HTML707411byte/SHA `549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857`, site/ZIP web và12 tham chiếu trước giữ byte. Snapshot trước tại `archives/v53-before-liuyao-b03-book5/`: sourceZIP1587943851byte/2533tệp manifest. Kiểm toàn byte manifest/ZIP ở `qa/liuyao-b03-book5/RELEASE_RESULTS.json`; nghiên cứu không vào site hoặc xuất bản mạng.

Mọi mệnh đề sách1–5,384chúhào/tiền tự, vượng suy/chân không, tự chọn Dụng và ứng kỳ đầy đủ vẫn mở; sách6 chưa tải tại mốc này. B02 còn136đơn vị/103thân mục mức đề mục/26khoảng đọc lần đầu, mâu thuẫn ngày–tuần không52 chưa giải quyết. Kho40nguồn và bốn mục lớn chưa khai thác hết.
