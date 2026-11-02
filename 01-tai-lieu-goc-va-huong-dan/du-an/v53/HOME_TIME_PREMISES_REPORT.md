# Nhà ở — phạm vi sửa chữa trong 月論

Ngày29/10/2026. Nghiên cứu nội bộ, chỉ mở rộng hồ sơ nguồn và hàm tham chiếu riêng.

Ảnh cơ quan xác nhận một điểm chức năng: một điều kiêng **sửa chỗ có sẵn** không thể tự biến thành quy tắc cấm mọi việc hoặc lời cho phép xây nhà. Trong đoạn丘公暗刀殺, sách nêu ngoại lệ `若鼎新造作則不避忌`; trong hai đoạn土公/遊龍伏龍 còn có ngoại lệ riêng liên quan土公敗日, đoạn遊龍伏龍 nêu thêm動土. Bộ mới giữ riêng các tiền đề này và trả chưa rõ khi thiếu, không tự dự đoán kết quả đời sống.

## Chuỗi nguồn và độ phủ

Từ mục lục cơ quan ITKC đã lưu, theo node tháng `ITKC_GO_1508A_0020_000_0060`, DCI `ITKC_GO_1508A_0020_000_0060_2017_001_XML`; metadata chỉ ảnh in240–247. Theo từng next-index trong viewer công khai để lấy8JPEG, giữ18bodyHTTP200/TLS/byte/SHA-256 gồm mục lục, bản số, metadata/navigations và8ảnh. Các lần POST chỉ đọc navigation. Không nhận master/container gốc hoặc thêm bản độc lập của Dương Trạch Thập Thư. Đây cùng tác phẩm liên quan選擇要略 của lượt bảng tháng trước; không tính thêm tác phẩm mới. Niên đại/copy bản khắc còn mở; mã2017vàcopyright2016 của sản phẩm số không xác minh năm khắc bản gốc.

Đã xem đầy đủ8ảnh này, gồm phần kết年論 ở240 và mở日論 ở247; không nói8ảnh là8trang toàn chữ thuộc月論. Lập19xử trí cấp mục cho toàn chương tháng. Bốn mục có vị từ chọn lọc được đối ảnh; chưa áp trọn19mệnh đề và các hiệu lực/thứ tự ưu tiên của cả chương. Tám crop cuối khớpRGB và đã xem; một crop遊龍 ban đầu thiếu cột cuối đã loại, giữ ngoài gói chứng cứ.

## Bốn vị từ cục bộ

| Mục | Điều kiện được giữ | Điểm chưa được tự suy |
|---|---|---|
| 丘公暗刀殺 | Sửa đổi chỗ đang bị quy tắc chiếm; dựng mới có ngoại lệ riêng | Chưa sinh đủ bản đồ tháng/năm; lời ứng lên người nhà không kiểm chứng |
| 大小耗星 | Tháng và chỗ được nêu, chỉ sửa tại đó | Không đồng nghĩa mọi việc khác được phép |
| 土公 | Sửa chỗ được nêu; ngoại lệ土公敗日 phải khai báo rõ | Không tự tìm ngày bại hoặc biến thành cách hóa giải |
| 遊龍伏龍 | Sửa đổi chỗ được nêu; ngoại lệ cần cả土公敗日 và動土 | Không bỏ mất điều kiện động thổ; không chứng minh hậu quả thị lực |

Bốn ví dụ vị trí được in:甲子năm/tháng2→chuồng lợn;甲子năm/tháng3→廳堂;tháng1→cửa trong mục大小耗;tháng1→bếp trong mục土公. Trường hợp ngoài danh sách là chưa biết, không là không có quy tắc. Hai ví dụ không ghi năm không tạo thành bằng chứng bảng mọi năm. Chưa nối vị trí cổ với tâm phòng hay hướng cửa của mặt bằng hiện đại.

Câu `止論月分不問節氣` ở Ám Đao và `只論月分並不問節氣` ở Du/Phục Long có phạm vi địa phương. Hai mục大小耗/土公 nói tháng, không tự thêm câu不問節氣cho chúng. Các nhóm thai gia súc có lời tháng/không tiết khí riêng nhưng không được mở thành lịch sinh nở hoặc ứng dụng cho người. Đoạn刀砧/千斤 phân biệt忌日並方và止忌方; không gộp ngày và phương. Những đoạn kể hỏa hoạn, bệnh tật, tổn hại hoặc nghi thức được lưu để đọc lịch sử, không đưa vào hành động/biện pháp khuyến nghị trên web.

## Hàm và kiểm chứng

`sourceLocalRepairScope` buộc đúng nguồn/mục, thao tác sửa có sẵn hay dựng mới, gốc tháng đã khai báo, tương ứng vị trí và các tiền đề ngoại lệ true/false/null. Bỏ một tiền đề sẽ giữ chưa rõ. Kết quả chỉ là sự hạn chế trong đúng mệnh đề, không trả ngày tốt, cho phép thi công, cát hung tổng thể hay kết quả thực nghiệm. Các gốc tháng số âm/tiết khí/không rõ chưa được chuyển tự động.

`sourcePrintedMonthlySite` chỉ trả bốn vị trí ví dụ trên; không nội suy thành bảng60năm×12tháng. Không có bộ lịch mới hoặc thay engine hiện hành.

Bản chép,8crop,18body và module được băm trước kiểm đầu. Các bảng kỳ vọng ngoại lệ được viết tường minh trong script kiểm sau mốc băm này. **7nhóm kiểm đạt**;672khung đầu vào hợp lệ,504khung không khai báo đúng tháng vẫn chưa rõ, kiểm đủ bốn ví dụ và bảng ba trị cho ngoại lệ. Tái dùng4ví dụ lịch đã thực thi trong `home-day-markers/ACTUAL_RUNTIME.json`, giữ SHA và tách khỏi số mới:0đối tượng lịch/0getZhiXing/0chartHHC/0iztro mới. Bốn ví dụ cache chỉ minh họa tháng âm số khác khung chi tháng của engine, không xác minh gốc tháng của sách này.

```powershell
node v53/research/home-time-premises/test-reference.mjs --no-write
python v53/scripts/verify-home-time-premises-sources.py --no-write
python v53/scripts/verify-home-time-premises-release.py --no-write
```

Nguồn, suy luận, crop, hàm và QA ngoài site. Giữ bản đã hoàn tất5458tệp trước phạm vi này. HTML707.411byte, site, engine, content vàZIPweb giữ nguyên; ứng viên Kiến Lộc tiếp tục chờ browserQA. Toàn kho vẫn mở; phần nguyệt luận chưa giải được720ô nhãn ngày hay năm/tháng của P08và vị trí cửa/phòng.
