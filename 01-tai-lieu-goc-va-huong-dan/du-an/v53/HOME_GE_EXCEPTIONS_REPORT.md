# Nhật luận ITKC: các điều kiện 隔 còn lại

ITKC Nhật luận: đọc mở rộng ba ảnh251–253 đã giữ; mười đơn vị điều kiện biên tập dưới bảy nhóm đề mục. Hai ngoại lệ địa phương với tiền đề khai báo: vào núi để chặt gỗ có 吉星 đối với 林隔/山隔,祭祀 gặp 神在日 đối với 神隔; không tách hoạt động ghép hoặc mở rộng cầu phúc/quỷ lễ. Tám đơn vị giữ cách nối/danh sách/lồng điều kiện/phạm vi chưa rõ. Giữ đề mục 刑隔 khác thân 州隔/bản số 州鬲;種植合成收日 không tạo thêm loại ngày 合 từ dấu phẩy bản số. Bốn tệp freeze/18ca trước triển khai;7kiểm,27khung ba giá trị/135bất biến,20khung không hỗ trợ/5đầu vào sai.3cropRGB chấp nhận/2trial loại. Thực thi môđun 萬通火星 cũ kiểm không ghi đè;0engine lịch/lá số/HTTP/vị trí nguồn mới. Web nguyên byte,toàn kho còn mở.


Nghiên cứu nội bộ trên ba ảnh cơ quan ITKC quyển 2, trang 251–253 đã giữ. Không tải mới hoặc đọc lần đầu vị trí mới. Ảnh và bản số hiện đại cùng hồ sơ, không phải hai nhân chứng độc lập. Xem `SOURCE_REUSE.json` để giữ byte/SHA-256 và dẫn hồ sơ tiếp nhận cũ.

`MANUAL_CONDITIONS.json` chia mười đơn vị điều kiện biên tập dưới bảy nhóm đề mục. Đây là cách đọc làm việc có chọn, không phải bản chép ngoại giao hay thống kê toàn bộ tác phẩm. Hai câu ngắn có một phạm vi ngoại lệ địa phương khi tiền đề được khai báo đúng: vào núi để chặt gỗ có 吉星 đối với 林隔/山隔, và 祭祀 gặp 神在日 đối với 神隔. Cách đọc nhánh 如祭祀 là điều kiện riêng được ghi rõ; không tự biến danh sách trước đó thành ANY/ALL. Tám đơn vị còn lại có xử trí và trở ngại riêng; không thực thi điều kiện chưa rõ.

Ảnh giữ 種植合成收日: 合 là động từ trong cụm, dấu phẩy bản số không tạo thêm một loại ngày 合. Đề mục ảnh 刑隔 khác chữ 州隔 trong thân; bản số dùng 州鬲. Giữ cả ba vai, không sửa bản gốc hoặc nâng thành một truyền bản mới. Các chữ 隔/鬲 là đối chiếu tên tại chỗ, không tạo công thức lịch.

`lookupGeCondition(id)` trả hồ sơ điều kiện bất biến. `sourceGeException(input)` chỉ nhận hai câu ngắn, đúng nguồn/khung, marker và loại hoạt động; tiền đề `true/false/null` phải tường minh. Phạm vi vào núi chặt gỗ là một hoạt động ghép; vào núi riêng hoặc chặt gỗ không rõ nơi vẫn chưa xác lập. Thần cách không mở rộng sang cầu phúc hoặc 祭設鬼類. `localAvoidance=false` chỉ ghi ngoại lệ của chính điều nguồn; `overallSuitability`, `permissionToAct`, dự đoán, ngày lịch và ưu tiên liên điều đều null. Tiền đề false/null không suy ra mệnh đề đảo.

Không có bộ nhận ngày/sao/lục nhâm/tọa hướng và không có phép đối chiếu engine trong phạm vi này; vì vậy không gọi engine lịch hoặc lá số. Bảy nhóm kiểm dùng 18 kỳ vọng đã giữ trước triển khai, 27 khung ba giá trị, 135 bất biến không suy rộng, 20 khung không hỗ trợ, năm đầu vào sai, các ranh hoạt động và việc thực thi môđun 萬通火星 cũ để chứng minh không ghi đè. Không thay môđun cũ; miễn một cách không tự xóa kiêng của điều khác.

Ba crop được chấp nhận khớp RGB với ảnh gốc; hai crop thử vẫn giữ và loại khỏi bằng chứng chấp nhận. Crop thử 鬼隔 thiếu đề mục đã được mở rộng trước freeze. Bốn tệp nguồn/kỳ vọng đã freeze trước khi có môđun và test. Đường dẫn crop trong bảng là xuất xứ staging; các PNG đồng tên đi cùng thư mục là bản giữ đúng byte.

Kiểm tại thư mục này: `node test-ge-exception-reference.mjs` và `python verify-source.py`. Môđun bên cạnh nhận bản JSON cố định và dùng Node, dành cho nghiên cứu nội bộ. Không có dữ liệu hay giao diện nghiên cứu nào đưa vào site công khai. Không tuyên bố áp trọn Nhật luận hoặc toàn kho.


Bản trước được giữ tại `archives/v53-before-home-ge-exceptions`. Bản đọc và môđun tiếp nhận đúng byte từ staging theo `qa/home-ge-exceptions/PROMOTION_IDENTITIES.json`. Kiểm phát hành đọc toàn bộ manifest/ZIP và so bản trước, giữ HTML độc lập/site/web ZIP cùng byte; kết quả chuẩn bị trong `qa/home-ge-exceptions/RELEASE_RESULTS.json`, dấu kiểm cuối ngoài gói tại `PENDING_RESEARCH_STATE.json`.

Đồng bộ siêu dữ liệu ma trận: phần scope danh mục B02 từng còn mốc136/96/32 cũ, nay dẫn map137/137/0 đã giữ; P08 ghi đúng720tọađộ/500nhãn làm việc/220chưa rõ thay vì chỉ nhãn建破. Giữ nguyên trạng thái research_only/0tác phẩm áp trọn và lời cũ trong trường lịch sử; không tính đây là lượt đọc/engine mới.
