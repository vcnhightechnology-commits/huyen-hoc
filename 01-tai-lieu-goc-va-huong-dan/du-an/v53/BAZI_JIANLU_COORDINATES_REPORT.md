# Bát tự: mười tọa độ Kiến Lộc và tiền đề giờ

Đã trích đủ mười hàng can ngày/chi tháng/trụ giờ từ đoạn Kiến Lộc ở ảnh DjVu223–224, tờ WYG113a–b. Đây là mở rộng hai trang đã giữ và đã đọc có mục tiêu; **0trang nguồn mới,0HTTP/container mới**. Một crop QA từ byte native223 xác nhận 己亥. Hàng癸 nằm qua223–224,không gán toàn câu cho một tờ. Container226trang giữSHA013ce4861680a2bf08b811050c45a45bb2d3ce9d164f7e2341d7070bd5cb2c1a; bản sốSHA1ebdd92feaa57496b702f962ad6fafd4f19c17e98c38a94b40f626ef321dd997. Hai vật mang cùng họ WYG không được coi là hai truyền bản độc lập.

| Can ngày | Chi tháng nguồn | Trụ giờ in |
|---|---|---|
|甲|寅|壬申|
|乙|卯|辛巳|
|丙|巳|己亥|
|丁|午|庚子|
|戊|巳|甲寅|
|己|午|乙丑|
|庚|申|丙戌|
|辛|酉|丁酉|
|壬|亥|戊申|
|癸|子|己未|

Ba chỗ bản số giữ巳 trong vị trí can (丙…巳亥,巳日…,癸…巳未) trong khi ảnh/chuẩn hóa theo vai trò là己. Lưu literal bản số riêng,không sửa byte so khớp. Các vị trí chi巳 vẫn giữ巳. Nghi vấn tính nhẩm ban đầu rằng丙日己亥 bất khả thi **đã bị bác bỏ**: khởi戊子 và đếm đến亥 cho己亥. Không có lỗi sách hay lỗi sản phẩm cần sửa; dùng乙亥 chỉ làm đối chứng âm tính.

## Tham chiếu và kiểm chứng thực thi

`jianlu-reference.mjs` là công cụ riêng so tọa độ, yêu cầu khai báo rõ can ngày. Chi tháng hoặc giờ chưa biết trảnull; sai tọa độ trảfalse. Có kiểm khả năng phối can ngày/can giờ theo quy ước Ngũ Thử Độn đã lưu nguồn riêng trước đây,không suy phép này từ riêng chữ宜. Đủ ba trường chỉ nghĩa khớp dòng nguồn;thành cách/vượng suy/dụng thần/kết quả vẫnnull. Không tự chọn ranh lịch hiện đại cho chương cổ. Lời liền sau về見煞 và không quá nhiều sát vẫn là tiền đề,chưa trở thành phép chấm tốt/xấu.

**9kiểm đạt**,có120lời gọi HHC Bát tự và120lời gọi lunar-typescript1.8.6 thật trên10ngày hiện đại×12giờ,bốn trụ khớp toàn mẫu. Runtime được kiểm byte theo audit đã giữ. Mỗi hàng giờ nguồn có một fixture thực thi khớp đầy đủ can ngày/chi tháng/trụ giờ. Cả10cóThấtSát tại can lộ hoặc tàng chi trụ giờ theo bảng cấu trúc đang dùng;không từ đó suy sát hữu lực hay phú quý. 120ngữcảnh canngày×chitháng riêng phân biệt đúng10tọađộ tháng;đây không phải120lời gọi thư viện khác. Thiếu/sai/null,đầu vào không hợp lệ và bảo toàn dữ liệu được kiểm.

Probe dò fixture trước bộkiểm giữ riêng:10HHC,41lunar dò ngày và10lunar sofixture;không cộng gộp chúng thành ca nguồn độc lập hoặc gọi phép đối runtime là chứng cứ nghiệm lý. Ngày2020chỉ dựng ví dụ cho phép tính,không phải ngày sinh lịch sử. Bảng38mệnhđề vàma trận10đềmục trước giữ nguyênbyte;phạm vi mới thêm10hàng tọa độ,không đổi38thành48mệnhđề hay tuyên bốđãhếtchương.

## Bảo toàn và tiếp tục

Snapshot trước giữ2901tệp/sourceZIP2017947166byte ở`archives/v53-before-bazi-jianlu-coordinates/`. RootHTML/V53/site707411byte/SHA549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857,ZIPweb344047byte giữnguyên;site chỉindex.html. Nguồn/QA ởngoài site;không xuất bản mạng.

Tiếp trọn điều kiện từng cách/mùa/căn/thân/tài-quan-ấn-thực/chế-hợp vàthamchiếu trước về禄/羊刄煞 trong đúng truyền bản;niênđại/độđủcontainer/NCL1915và487–486còn mở. Tửvi/Nhàở/KinhDịch vàtoàn40nguồn vẫn**active-not-complete**.
