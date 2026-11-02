# Bảng 後天時方: đọc đủ vị trí nhãn — 27/10/2026

Đã đọc trực tiếp phần nhãn của60hàng can chi ×12vị trí chi trên PDF207–212/trang in19–24, thay cho mốc trước chỉ kiểm khóa hàng. `research/meihua-hour-table/PHYSICAL_CELLS.txt` giữ bản ghi thủ công720vị trí; `HOUR_TABLE.json` nối khóa,vị trí,trang và trạng thái. **707vị trí có nhãn đọc được,12vị trí không thấy nhãn,một vị trí còn chữ mở**. Có13vị trí nhiều chữ,721chữ đơn đọc được vàmột□; không gọi721chữ là721ô. Dấu`+` liệt kê các chữ cùng vị trí,không khẳng định đó là từ ghép hay thứ tự ngữ pháp.

Chữ còn mở ở Đinh Mùi/子, giữ`□+死`, có dạng gần怒/恕. Không chọn theo ngữ cảnh hoặc suy một kết luận từ chữ bên cạnh. Crop native/nearest4x giúp đọc chữ Quý Mão/午 là`伐`; nghĩa dùng của chữ này vẫn chưa được xác lập. Nhãn`禍` giữ khác`祿`. Cột thứ sáu chuẩn hóa thành chi`巳`; dạng in gần`己` không trở thành thiên can. Đây là bản đọc vị trí nhãn chuẩn hóa,chưa phải bản chép ngoại giao mọi nét chữ.

Mười hai vị trí không thấy nhãn được giữ trống,không có giá trị mặc định. Chưa biết sự vắng đó thuộc chủ ý hay khuyết in. Chín hàng đã đọc đủ không có đúng một`罡`: có hàng không có,có hàng hai hoặc ba; hàngĐinh Mùi còn chữ mở giữ số lượng chưa kết luận. Giả thuyết chép mẫu chỉ theo chi cho48hàng sau cho188/576vị trí trùng,388khác. Đây là phản ví dụ cho cách tự điền bảng bằng mẫu,không phải388lỗi bản in đã chứng minh.

Đầu bảng có các mảnh chắc chữ`子日子罡起`,`五敗七破位`,`十禍日皆同`; bốn vị trí tương ứng ở hàngGiáp Tý khớp. Nếu thử mở rộng bốn điểm đó sang cả năm hàng có chiTý,chỉ15/20khớp. Sự mở rộng ấy là **giả thuyết kiểm tra**,không phải quy tắc đã giải mã từ văn bản. Các chữ/cú pháp khác trong đoạn dẫn,nghĩa từng nhãn/nhãn ghép,thứ tự ưu tiên và quy ước lịch/giờ vẫn mở. Nạp Giáp trước bảng và phép xem chữ sau bảng không tự cung cấp những tiền đề còn thiếu.

**14/14 kiểm nguồn/runtime đạt**. Tất cả720vị trí nối đúng60khóa/12cột và bản ghi thủ công cóSHA riêng. Hai tệp lunar-typescript1.8.6 chạy thật khớp kiểm kêbyte trước. Chạy720lá số HHC và720lá số tham chiếu trên60ngày từ01/01 đến01/03/2026,12thời điểm00:30–22:30,cùngUTC+8/đổi ngày00:00/sect2: can chi ngày và chi giờ khớp,đi qua đúng toàn720tọa độ nguồn. Đây chỉ là kiểm sự nhất quán tọa độ của một lựa chọn phần mềm; không chứng minh bảng dùng lịch Gregory,ranh Tý hoặc múi giờ đó,và không kiểm độ đúng lời đoán. Không đưa phép chuyển ngày này vào API tra bảng hoặc giao diện.

`hour-reference.mjs` chỉ nhận khóa hàng in và chi đã xác định,tra nhãn gốc,trả bản sao. Nó giữ ô trống/chữ mở và không tạo lời đoán/điểm/ngày ứng nghiệm. Dữ liệu,nguyên văn,nguồn và QA ở ngoài site. Biểu mẫu và tính năng người dùng không đổi trong phạm vi này.

Không HTTP,OCR hoặc sách/trang nội dung mới. Sáu trang bảng là đọc mở rộng nhãn; PDF206/213 chỉ đọc ranh ngữ cảnh có giới hạn. PDF gốc5.621.631byte/SHAaf608094…và232PNG trước giữ nguyên. Sáu render300dpi cùng20crop/phóng nearest là dẫn xuất QA; mọi vị trí được xem qua các vùng ảnh,hai chữ khó xem thêm ở độphóng lớn. Pixel không được thay chữ hoặc bổ sung chi tiết. Mốc chỉ số cũ với0ô chép giữ nguyên như tài liệu lịch sử,có liên kết sang bản ghi mới.

HTML707.411byte/SHA549cb415…,toàn JS/CSS,site vàZIPweb giữ byte bản bốn lớp đã qua98kiểm/PDF4trang. Chỉ nghiên cứu,trạng thái,manifest vàgói nguồn cập nhật. Snapshot trước tại `archives/v53-before-meihua-hour-table/` giữ sourceZIP843.408.029byte/webZIP344.047byte vàmanifest1.811tệp. Kiểm đóng gói tại `qa/meihua-hour-table/RELEASE_RESULTS.json`.

Đã có quyết định và bản ghi cho mọi vị trí bảng; còn một chữ,giải nghĩa/đầu vào vànhân chứng độc lập. Hai chữ khó của bảng vật tượng vẫn giữ riêng. Tiếp mệnh đề phụ vàđiều kiện đầy đủ của năm quyển cùng các nhánh khác trong kho; không lặp khóa hàng hoặc chép lại720vị trí để tăng số,không nhận toàn sách/toàn kho hoàn tất.
