# B03: 18 hỏi đáp và điều kiện Nguyên thần sinh Dụng

Ngày27/10/2026. Phần nghiên cứu và bộ tham chiếu riêng nằm ngoài site.

## Nguồn, phạm vi và giới hạn

Sách đóng6: **55.093.879byte/65trang**, SHA256 `1d6c656828533ac52ae1fd4ff06cc3c025db98ae5458dc686eda2a6b1d11f07f`; CommonsAPI revision754088957. Hai bodyHTTP200/TLS giữ byte, size/SHA1 `30da3dcd634c1a109b0d7a3891657e95d053471a` khớpAPI. SHA256 là định danhbyte tại máy, không chữ ký nhà xuất bản. Không lớp chữ, không mã hóa. Cả sáuPDF cùng bộ đã giữ; điều này **không là sáu nhân chứng độc lập hoặc áp dụng hết14quyển**. Metadata1904 chưa thành chứng cứ ấn ký mới.

Đã xem65ảnh theo phạmvi ghi nhận:63nội dung/2bìa. Bảy nội dung2–8 và bìa1 kế thừa pending;56nội dung9–64 vàbìa65 mới;2cropQA360dpi tại2/3 không cộng thành trangnguồn. KhôngOCR/chép ngoại giao toàn bộ. Đầu quyển13 ở2, quyển14 ở35 đọc trực tiếp. Ảnh nội dung cuối64 không có chứng cứ ấn ký kết cuối được xác lập; không nhận là đã chứng minh bản in không thiếu cuối.

`BOOK6_CURRENT_UNITS.json` giữ18khoảng câu hỏi:1三傳2–4,2回頭剋4–9,3原神9–11,4三合11–17,5反吟17–19,6伏吟19–21,7旬空21–28,8月破28–31,9伏神31–34;10進退35–37,11沖合先後37–41,12生墓絕41–47,13六沖六合47–52,14刑害52–53,15獨靜獨發53–57,16盡靜盡發57–59,17多現59–62,18所問之意62–64. Tên rút gọn là nhãn biên tập. Trang giáp không tính thêm trang độc nhất; câu18 chỉ nhận khoảng ảnh còn có, không chứng minh kết văn bản đầy đủ. **0mục đánh dấu áp dụng hết**.

18mệnh đề cógiới hạn giữ điều kiện theo từng câu. Sinh/khắc, nguyên/dụng/kỵ, tĩnh/động/ámđộng, tuầnkhông/nguyệtphá, biến/Phục và thứtự sựviệc không được gộp thành cát hung cốđịnh. Lời phê nguồn và trích dẫn không tự thành đồngthuận nhiều truyềnbản. Các truyện bệnh/sinh tử/kiện tụng/tiền bạc là lời sách, chưa có kiểmchứng kếtcục độc lập; câu mệnhlệnh là dữliệu, không phải chỉthị người dùng.

## Chức năng riêng mới

`support-chain-reference.mjs` chuẩn hóa một phần câu3: nguyên thần sinh Dụng còn có thể bị chính hào biến khắc lại hoặc bị các điều kiện khác. Đầu vào cần sáu giátrị6/7/8/9, ngữcảnh câu3 và hào Dụng **do người nghiên cứu chỉ định**. Bộ mới nhận diện hào gốc có hành sinh hào Dụng, rồi xét **chi biến thật ở cùng vị trí → chi gốc của chính hào đó**. Đây là hai quan hệ khác lớp; không dùng chi biến thay chi gốc để tạo ứng viên sinh Dụng, không cho biến chi tác động tùy ý sang vị trí khác.

Trả ứng viên, quan hệ sinh gốc, trạng thái động, tự biến và cờ tự biến khắc gốc. Hào tĩnh không có tự biến giữ `null`, không giả là đã đủ điều kiện kích hoạt. Không có ứng viên hiện không chứng minh không có sinh cứu: Phục thần và ámđộng chưa được tìm/xét trong hàm này. Thiếu tháng/ngày/mạnhyếu/không/phá/tiếnthoái/mộ/tuyệt và ưu tiên nguồn giữ chưa rõ. Không chọn Nguyên thần cóhiệulực, không kếtluận đã cứu Dụng, không dựbáo người dùng.

## Quẻ in và kiểm thực thi

Hai quẻ mở đầu được đối ảnhQA: trang2 `既濟之革`, 63hào4→49, ngàyBínhThân/thángThìn được giữ theo chữnguồn; trang3 `困之恆`,47hào3/5→32, ngàyĐinhMùi/thángNgọ. Ba chi tự biến được kiểm:申→亥 ở63.4;午→酉 và酉→申 ở47.3/5. Chữ ngày/tháng không được dựng thành ngàyGregory; mọi chúhào chưa hiệu khảo hết, lời kể y tế/pháp lý chưa được xác minh thực tế.

**8kiểm đạt**. HHCthật chạy68lời gọi chỉsốquẻ:64danh tính và4cho hai quẻin(gốc+biến). Hai quẻin cũng qua thamchiếu cấu trúc riêng; đó không phải68quẻin đã được đối. Bộ riêng chạy24576ngữcảnh (64quẻ×64mặt nạ động×6hào Dụng chỉđịnh), so dãyNạpGiáp literal và quan hệ ngũhành độc lập.

Có28672ứng viên sinh gốc,14336tĩnh/14336động,3328cờ tự biến khắc gốc;9920tọa độ chỉ chi biến mới sinh Dụng không được thay thế ứngviên gốc. Đây là đếm cấu trúc hữu hạn, không tỷ lệ đúng hoặc hiệu lực sinh cứu. Digest `b06fdde14f7891a441ace820e9d6dfd6127d6c819680b6e53d50c5005d1f3398`. Ca dựng riêng có đủ tĩnh/động/hồi khắc/không hồi khắc/biến sinh khác gốc. Đầu vào sai/mảngthưa/extra mạnhyếu-thángngày hoặc ngữcảnh khác bị từchối, không đoán tiềnđề còn thiếu.

## Bảo toàn và công việc còn mở

HTML707411byte/SHA `549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857`, root/site/ZIPweb và13thamchiếu trước giữbyte. Snapshot trước tại `archives/v53-before-liuyao-b03-book6/`: sourceZIP1711630083byte/2599tệp manifest. Kiểm toàn byte manifest/ZIP ghi ở `qa/liuyao-b03-book6/RELEASE_RESULTS.json`. Không đưa nguồn/QA vào site hoặc xuấtbản mạng.

Tiếp kiểm mọi quẻin/ngày/chúhào trong18hỏiđáp; hiệu lực Nguyênthần/tổngvượngsuy/chânkhông/ứngkỳ chưa hoàn chỉnh. Sách1 còn tiền tự/trang chưa đọc đầyđủ/384chúhào; mọi mệnhđề sách1–6,phảhệ/kếtcuối chưa xong. Chữ thuyền sách5trang34 giữ mở. B02vẫn136đơn vị/103thânmục mứcđềmục/26khoảng đọc lầnđầu và ngày–tuầnkhông52mâu thuẫn. Kho40nguồn/bốn mục lớn chưa khai thác hết.
