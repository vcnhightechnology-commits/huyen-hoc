# B03 quyển ba: phản ngâm, phục ngâm, tiến–thoái và khác biệt phương pháp

Ngày công việc: 27/10/2026. Nghiên cứu riêng ngoài `site`; toàn kho **active-not-complete**.

## Nguồn mới và khoảng đọc

Đã tải byte PDF quyển vật lý thứ hai qua [trang nguồn Commons](https://commons.wikimedia.org/wiki/File:NLC892-GBZX0301013045-259365_%E5%8D%9C%E7%AD%AE%E6%AD%A3%E5%AE%97_%E5%8D%81%E5%9B%9B%E5%8D%B7_%E7%AC%AC2%E5%86%8A.pdf), sau khi lấy API imageinfo/revision. Hai phản hồi HTTP 200/TLS xác thực được giữ; không tải lại quyển trước.

- PDF: **41.224.832 byte**, 49 trang, SHA-256 `c1e1027331d43769733c6011b4fe99e90928e9fde013fce563c8e9bad81c04bf`, SHA-1 `fb4f1aca26238121204b48bd0bff55f480f526cb`; kích thước và SHA-1 khớp API.
- Revision trang mô tả: **754088942**, thời điểm 25/04/2023. `ACQUISITION.json`/`REQUESTS.json` giữ URL, byte, hash, thời điểm và TLS; API cũng có hash riêng.
- Container kiểm trực tiếp: 49 trang, không mã hóa, không lớp chữ; không OCR. Trang PDF 2 in **卜筮正宗卷之三 / 十八論**, dòng người biên soạn 王維德洪緒. Đây là chứng cứ đọc trực tiếp; nhãn 1904/sáu sách đóng vẫn là metadata nối bộ, không phải một trang ấn ký mới đã đọc.
- Đây là ảnh chụp sách in được sao cơ học và tải nguyên byte, không gọi là thủ bút tác giả hay tự xác nhận là sơ bản. Đã có sách đóng 1 và 2, chưa đủ sáu sách đóng/14 quyển văn bản.

Đã xem **32 ảnh mới**: PDF 1 bìa; 2–29 toàn khoảng nội dung quyển ba, gồm 18 luận ở 2–13 và 14 đoạn biện luận/phê bình ở 14–29; PDF 29 có dòng kết quyển ba. PDF 30 mở quyển bốn, 30–32 chỉ đọc đầu đoạn có giới hạn. PDF 33–49 chưa được tính là đã đọc. Khép lượt đọc khoảng quyển ba không đồng nghĩa đã biên dịch hết mọi mệnh đề hoặc áp dụng toàn quyển.

## Chức năng nội bộ đã bổ sung

`research/liuyao-b03-volume3/layer-reference.mjs` tách ba lớp cấu trúc:

1. **Phản ngâm ở tầng quái/phương vị**: Càn–Tốn, Khảm–Ly, Cấn–Khôn, Chấn–Đoài. Có thể ở nội quái, ngoại quái hoặc cả hai.
2. **Phản ngâm ở chi hào thực sự biến**: chi đổi sang chi đối xung. Đây là lớp khác; không lấy tên quái đối phương vị thay cho phép xung chi.
3. **Phục ngâm ở tầng quái đã đổi**: ba chi Nạp giáp tại cùng nửa quẻ lặp lại, dù can thay đổi và hình quái khác. Càn→Chấn là ví dụ; quẻ tĩnh giữ nguyên không tự gắn “phục ngâm” chỉ vì chi trước/sau giống nhau.

Chỉ các hào thực sự động có chú hào biến. Các chi sau của cả nửa quẻ chỉ dùng làm chẩn đoán tầng quái, gắn nhãn rõ; không biến thành chú biến của hào tĩnh. Hàm giữ riêng lớp nào trùng và không tự đặt ưu tiên hay kết luận sự kiện.

Hai đối chứng có ý nghĩa: Càn 1→Tốn 57 có phản ngâm phương vị cả hai nửa nhưng không hào động nào đổi sang chi xung; Khôn 2→Tốn 57 là đối chứng tổng hợp có hào 2/3/5/6 đổi chi xung nhưng không thuộc bốn cặp phương vị trên. Không thể gom hai lớp thành một cờ duy nhất. Càn 1→Chấn 51 có bốn hào động, các chi tương ứng lặp lại trong khi can khác.

Thêm tọa độ **tám cặp tiến thần/tám cặp thoái thần** ở hào động: Hợi→Tý, Dần→Mão, Tỵ→Ngọ, Thân→Dậu và vòng Thổ Sửu→Thìn→Mùi→Tuất→Sửu; thoái là chiều ngược. Chỉ xác định chuyển chi; chưa xét có khí hay không, tiến/thoái có tác dụng hay thời điểm. Không coi tiến luôn tốt hoặc thoái luôn xấu.

## Kiểm chứng

`node v53/scripts/verify-liuyao-b03-volume3.mjs`: **11/11 kiểm đạt**. Mười hai cặp tên quẻ in được tái dựng hào động theo chênh lệch trước/sau và chạy **24 lời gọi số quẻ HHC thật**; sách không in đủ đầu vào tiền hào/ngày cho các ví dụ này, nên dữ liệu tái dựng được ghi là suy ra từ cặp quẻ.

4.096 cặp cấu trúc nội bộ được kiểm bằng oracle phương vị, Nạp giáp và vòng chi độc lập, 12.288 chú hào động. Đây là lần kiểm chức năng phân lớp mới, không gọi lại 8.192 lần engine cũ để cộng số. Có 960 cặp mang phản ngâm phương vị, 252 cặp có phản ngâm chi hào, 252 cặp phục ngâm và **1.148 cặp khác nhau về sự có mặt giữa hai lớp phản ngâm**. Có 512 chú tiến/512 chú thoái; thêm 144 đối chiếu chi đôi. Digest `dcc0482f674726bb230d6f4f88735da3310054122154e322475a75516b470a9f`.

Các con số đo độ bao phủ phép phân loại cấu trúc, không đo độ đúng dự báo đời thực. Tổng vượng suy, chân không, chọn Dụng thần, lịch/ranh ngày và hiệu lực cuối vẫn để chưa xác lập.

## Khác biệt truyền bản và phần chưa xử lý

27 bản ghi diễn giải giới hạn giữ riêng vai trò Nguyên–Kỵ–Thù, Nhật–Nguyệt, không/phá, sinh–tuyệt, hợp–khắc và phần luận đầu quyển bốn. Quyển ba trực tiếp phê bình Tăng San Bốc Dịch, Dịch Lâm Bổ Di, Bốc Phệ Toàn Thư về một số cách lấy Phục thần, thế thân, thần sát, người được hỏi, hỗ quẻ, đại/tiểu hạn, nhà ở và hôn nhân. Đây là **lời phê bình của tác giả B03**; chưa độc lập kiểm nguyên văn mọi sách bị trích, không được chuyển thành bằng chứng hiện đại rằng một phía đúng hoặc sai.

“Thế thân” 子午持世身居初… bị phê bình tại PDF 17–18 là một cách khác với bài “an nguyệt quái thân” trong sách đóng trước. Giữ hai tên/phương pháp riêng, chưa thêm một thuật toán “thân” chung. Các chuyện bệnh, chết sống, thần sát, thành bại, phúc đức hoặc yêu cầu thành kính trong sách là dữ liệu lịch sử, không phải chỉ dẫn cho người dùng hay bằng chứng độ chính xác y học. Những quy tắc chọn đối tượng theo người hỏi không được rút thành thế luôn nam/ứng luôn nữ hoặc luôn lấy ứng cho mọi người khác.

Mâu thuẫn B02 PDF 52 ngày Tân Mão/lời Dần Mão không vẫn mở. Chỉ mục B02 giữ 136 đơn vị, 103 thân mục đề mục, 26 khoảng đọc lần đầu; không giảm số mở chỉ vì B03 bàn chủ đề tương tự. Quyển ba mới hoàn tất lượt đọc khoảng; từng mệnh đề/điều kiện và các tranh luận còn cần đối chiếu.

## Đồng bộ và tiếp tục

HTML/root/site giữ **707.411 byte**, SHA-256 `549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857`, ZIP web **344.047 byte**. Bảy bộ tham chiếu trước và báo cáo lịch sử giữ nguyên byte; module mới ở gói nguồn riêng, không đưa corpus vào web hoặc tự xuất bản mạng. Snapshot trước phạm vi giữ ZIP nguồn **1.030.931.341 byte**/2.247 tệp manifest.

Tiếp quyển bốn sau PDF 32 và các sách đóng còn thiếu; tách câu gốc/lời chú/ngoại lệ thành mô hình tiền đề, sau đó mới xét một chức năng Lục Hào hoàn chỉnh cho người dùng. Các phần B02, Mai Hoa, Bát Tự, Tử Vi, nhà ở và toàn kho vẫn còn mục mở. Không đánh dấu toàn sách, bốn hướng hoặc toàn kho đã xong.
