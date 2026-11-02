# B03: phần đầu, quyển một và bảng can tháng/can giờ

Ngày 27/10/2026. Nguồn, bản đọc và tham chiếu riêng nằm ngoài site.

## Byte nguồn và phạm vi đọc

Tái dùng PDF sách đóng1 đã giữ từ phạm vi nền: **50.191.031 byte/60 trang**, SHA256 `5dcd7b5005b1e86f441a9350eefb7c0e9e628c47ab926b2a7d1bdd6691a4773d`. Không HTTP hoặc PDF gốc mới; không nhân đôi PDF. SHA xác định byte tại máy, không là chữ ký nhà xuất bản. Sách1–6 cùng bộ không là sáu nhân chứng độc lập.

Khép lượt đọc có giới hạn PDF1–33: 33bản ghi,32nội dung/1bìa;19trang pending và14trang20–33 mở rộng từ ảnh đã có. Bảy render QA360dpi cho12crop, không thêm trang nguồn. Có57nhóm biên tập gồm bìa/tiêu đề/tựa/mục lục/bảng/câu; không gọi là57đơn vị áp dụng hết. Quyển1 kết trực tiếp ở33: `卜筮正宗卷之一終`. Kết hợp các phạm vi cũ, cả60ảnh vật lý sách1 đã được xem có giới hạn; **chưa chép ngoại giao toàn trang, chưa đối hết384chúhào hoặc áp hết mọi mệnh đề**.

## Tựa, mục lục và các lớp chứng cứ

Trang2 ghi `光緒甲辰新鐫 / 王洪緒輯 / 文成堂存板`; trang5 ghi `康熙己丑歲冬十月吳郡張景松書於蓉江草堂`; trang6–7 là lời tự thuật về thầy 新安楊廣含 và18hỏiđáp; trang15 có dạng tên 王維德洪緒輯. Giữ từng giọng và năm literal. Sửa nháp chưa phát hành 安郡 thành **吳郡** sau QA; không chuyển năm sang Gregory hoặc nhận đã xác minh độc lập phả hệ/đồng nhất mọi giọng.

Mục lục13–14 ghi số ví dụ cho18câu:5/11/4/12/5/4/14/7/6/5/8/13/11/4/7/4/5/6, tổng **131**. Đây là tổng số **sách tự ghi ở mục lục**, chưa là đếm đủ sơ đồ thân sách hoặc131quẻ đã chạy engine. Bản phát hành trước mới kiểm cấu trúc hai quẻ in ở đầu sách6; không tăng con số này bằng bảng hoặc tọa độ dựng riêng.

Các đoạn đạo đức, nghi lễ, trị bệnh, sự kiện nghiệm thuật và phê nguồn giữ là dữ liệu lịch sử của sách; không là chỉ thị người dùng hoặc chứng minh kết cục thực tế. Khung 卦身 của B03 vẫn riêng với lập trường B02. Mười mệnh đề có giới hạn nằm trong `OPERATIONAL_CLAUSES.json`; mọi điều kiện phụ chưa hoàn tất.

## Ba bảng có thể thực thi

Trang17:30cặp Nạp âm/60can chi. Đọc QA giữ **白蠟金**, **覆燈火**. Sáu mươi tọa độ đều khớp hành với lunar-typescript1.8.6;58tên khớp sau phép đổi chữ phồn–giản được ghi tường minh. Hai tọa độ **甲申/乙酉** giữ nguồn **井泉水**, runtime **泉中水**. Đây là khác tên; chưa chứng minh lỗi tính hoặc tương đương qua các nhân chứng lịch sử.

Trang24 `年上起月法`: năm 甲己 khởi 丙寅,乙庚戊寅,丙辛庚寅,丁壬壬寅,戊癸甲寅 rồi thuận hành. Trang25 `日上起時法`: ngày 甲己 khởi 甲子,乙庚丙子,丙辛戊子,丁壬庚子,戊癸壬子 rồi thuận hành. Có mười neo theo **cặp** in trực tiếp; khi tách từng can là20neo đơn,220tọa độ còn lại do biên tập khai triển theo quy tắc thuận hành. Không gọi240ô đều được in thành bảng đầy đủ trong sách.

`stem-coordinate-reference.mjs` cung cấp hai hàm riêng: **can năm + chi tháng đã xác nhận → can tháng**; **can ngày + chi giờ đã xác nhận → can giờ**. Đầu vào không nhận số tháng âm, giờ đồng hồ, múi giờ hoặc sức mạnh. Không tự chọn ranh Tết/Lập Xuân/tiết khí, đổi ngày lúc23h, Tý muộn hoặc thời gian chân thái dương. `定寅時法` trang25 có bối cảnh mùa/canh/điểm; chưa có căn cứ quy đổi đủ sang giờ dân dụng hiện đại, nên chưa thêm bộ quy đổi.

## Kiểm thực thi và bảo toàn

**8kiểm đạt**, với **240lời gọi HHC BátTự thật +300lunar thật**:120tọa độ can năm–chi tháng,120tọa độ can ngày–chi giờ,60Nạp âm. Kiểm tháng dùng ngày15trưa trong mười năm2000–2009; kiểm giờ dùng mười ngày1–10/1/2026 tại12chi với phút30, tránh23h. Nạp âm dùng60ngày liên tiếp lúc trưa chỉ để duyệt vòng canchi. Đây là bộ ca hữu hạn kiểm các tọa độ, không dựng ngày cổ hoặc chứng minh các quy ước lịch ở ranh. HHC và lunar có phụ thuộc liên quan, không gọi là hai nguồn học thuật độc lập. Tọa độ tháng/giờ đầu vào được xác nhận từ lịch thật chỉ phục vụ đối chiếu; bộ nguồn không trở thành adapter lịch.

Đủ120cặp đầu vào độc nhất ở mỗi bảng, khớp cột canchi của HHC và lunar; phiên bản/runtime giữ hash. Kiểm sai đầu vào/khóa thừa, bảo toàn đầu vào và14thamchiếu Lục hào trước. Ca và digest ở `qa/liuyao-b03-book1-tables/`. Không lặp4096bộ quẻ khi logic Nạp Giáp không thay đổi.

HTML độc lập/root/site giữ **707411byte**, SHA256 `549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857`; ZIPweb giữ344047byte. Snapshot trước `archives/v53-before-liuyao-b03-book1-tables/` giữ sourceZIP1899259205byte và2688tệp manifest. Kiểm toàn byte manifest/sourceZIP nằm trong `RELEASE_RESULTS.json`; không phát hành mạng.

Tiếp đối đủ64hình/384chúhào và quẻ/ngày/tiền đề thân18hỏiđáp; mạnh yếu/chân không/ứng kỳ/hiệu lực sinh cứu vẫn mở. Chữ thuyền sách5, kết cuối sách6 và nhân chứng độc lập/phả hệ chưa giải quyết. B02 vẫn136đơn vị/103thân mục mức đềmục/26khoảng đọc lầnđầu; ngày–tuầnkhông52mâu thuẫn. **0toàn sách được nhận đã áp hết; kho40nguồn/bốn hướng còn đang làm.**
