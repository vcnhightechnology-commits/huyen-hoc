# V53 — chuyển từ giao diện nghiên cứu sang trải nghiệm người dùng

Ngày thực hiện: 25/10/2026. Phạm vi theo yêu cầu mới nhất: làm lại web cho người dùng dễ tiếp cận, đưa kết quả và diễn giải ra trước; đưa nguồn kiến thức, suy luận phát triển và hồ sơ nghiên cứu khỏi giao diện sử dụng.

Cập nhật đọc cung không có chính tinh: xác định cung đối diện và các sao ở đó, phân biệt rõ phần bổ sung và cho mở cung liên quan. Đã chạy iztro thật trên 100 chart/1.200 cung, giữ nguyên bộ tính; ba bộ liên quan đạt **107/107**. Xem `OPPOSITE_READING_REPORT.md`. Không tuyên bố đây là hiệu khảo quy tắc mượn sao hoặc xác nhận tính tiên đoán.

Cập nhật giao diện sau khảo sát website: phần đầu gọn hơn, thẻ hành động và mô tả đủ cho năm công cụ, chữ đọc chính 15–16 px, xanh ngọc/nền giấy và tương phản rõ. Phần tính/nội dung/app giữ nguyên byte. Xem `EXPERIENCE_REPORT.md`; 36 kiểm tra mới + 50 hồi quy + 35 ảnh đạt **121/121** trong phạm vi này. Các số kiểm tra khác bên dưới là hồ sơ của những phạm vi trước.

Cập nhật tiếp cùng V53: thêm xác định năm âm từ ngày dương cho Bản mệnh/Hướng nhà và sửa lỗi Enter → Lưu khi sự kiện đổi ô đến muộn. Xem `YEAR_LOOKUP_REPORT.md`; hiện ba bộ kiểm thử đạt **99/99**. Bản phát hành đầu tiên được giữ trong `archives/v53-first-consumer/` ngoài thư mục nguồn V53.

Cập nhật sau đó: bỏ giờ/phút sinh tự điền, chặn engine biết giờ khi thiếu dữ liệu và tránh biến thời điểm neo của hồ sơ chưa biết giờ thành giờ sinh thật. Xem `BIRTH_TIME_REPORT.md`. Bốn bộ liên quan vừa chạy đạt **123/123** (50 + 38 + 11 + 24); có 48 lần chạy iztro thật, khớp 816 trường trên phạm vi giờ đã nêu. Các số 61/99 ở phần lịch sử thể hiện phạm vi trước cập nhật này. Tranh và CSS giữ nguyên.

## Kết quả

Đã xây giao diện mới độc lập, thay vì che các khối cũ bằng CSS. Năm công cụ: Tử vi, Bát tự, Bản mệnh, Hướng nhà, Gieo quẻ. Mỗi công cụ có biểu mẫu riêng, trạng thái chưa nhập, thông báo nhập sai và kết quả đọc được ngay. Dùng nền giấy, xanh trầm, chữ serif ở tiêu đề; không tải font, ảnh, thư viện hoặc dịch vụ từ bên ngoài.

Tử vi đưa bốn chủ đề chính lên trước, cho chọn đủ 12 chủ đề và mở lá số 12 cung khi cần. Bát tự hiển thị bốn trụ, Nhật chủ và biểu đồ sự hiện diện của ngũ hành. Khi chưa biết giờ, không dựng trụ giờ; nếu ngày đó đi qua mốc chuyển trụ, giữ các khả năng và hoãn diễn giải bố cục chưa xác định. Bản mệnh hiển thị nạp âm, cung phi và gợi ý màu. Hướng nhà trình bày đủ tám hướng, bốn hướng phù hợp và hướng người dùng muốn xem. Quẻ có thể gieo từng hào, gieo đủ hoặc nhập sáu hào; quẻ chủ, quẻ biến và hào động được phân biệt.

Kết quả thay đổi khi đầu vào thay đổi: giao diện xóa kết quả và các nút xuất cũ, tránh lưu hoặc tải nhầm kết quả không còn tương ứng biểu mẫu. Lưu hồ sơ là hành động rõ ràng, tối đa 20 hồ sơ trên thiết bị. Có mở lại, xóa, tải bản đọc TXT và in. Không nhập tự động kho lưu của giao diện nghiên cứu cũ.

## Tách nội dung công khai và tài liệu nội bộ

HTML phát hành chỉ chứa giao diện, mã tính cần dùng và văn bản diễn giải. Không chứa thư viện sách, ảnh nhân chứng, corpus Hán văn, bảng đối chiếu engine, byte nguồn, URL nguồn, nhật ký suy luận hay báo cáo nghiên cứu. Các mục Cổ thư, Học thuật và các phòng kiểm định không còn là màn hình của bản người dùng. Không có liên kết HTTP trong sản phẩm và không có yêu cầu HTTP khi thực thi bản HTML ngoại tuyến.

Hồ sơ nguồn và các bản V46–V52 vẫn ở nơi lưu cũ. Báo cáo này, mã tái lập và bằng chứng kiểm thử nằm ngoài `site/`, không được ghép vào HTML hoặc gói web. Bản offline phải chứa JavaScript để tính tại thiết bị; sự tách biệt này không phải mã hóa hay cơ chế chống xem mã nguồn. Nếu cần giữ kín thuật toán khi phát hành trực tuyến, đó là phạm vi máy chủ riêng trong tương lai.

## Bộ tính và giới hạn

Trích các hàm số học, hằng số và bảng tiết khí đang dùng ở V52; dựng facade có kiểm tra đầu vào. So sánh trực tiếp với V52 được chạy trong trình duyệt, không thay bằng công thức kỳ vọng viết lại trong bộ kiểm thử. Các sao, Mệnh–Thân, cục và cờ cung được giữ nhất quán trên mẫu hồi quy. Đây là xác nhận không làm sai bộ tính cũ trong phạm vi mẫu, không phải bằng chứng mới về khả năng tiên đoán.

Múi giờ mặc định Việt Nam UTC+7. Người sinh ở nơi khác chọn độ lệch UTC trong tùy chọn; trang không tự suy đoán giờ mùa hè từ quốc gia. Có giữ tùy chọn ngày Tý muộn và tháng nhuận, với mặc định tương ứng bộ tính đã dùng. Công cụ năm sinh dùng năm âm đã biết hoặc đổi từ ngày dương đầy đủ theo lịch âm áp dụng; không lấy năm dương thay năm âm hay dùng Lập Xuân. Ngoại lệ chưa giải quyết 03/02/1916 UTC+8 yêu cầu nhập năm âm xác nhận. Xem báo cáo bổ sung để biết phạm vi nguồn kiểm chứng.

Giữ nhắc đối chiếu ngày âm cho bảy khoảng lịch nhạy đã xác định ở V51, bằng thông báo ngắn, không lộ hồ sơ nguồn. Đây không phải bảng lịch công bố đầy đủ hay bảo đảm các ngày không cảnh báo đều đã được đối chiếu độc lập. Phạm vi năm 1900–2100.

Diễn giải là nội dung biên tập theo hình tượng của 14 chính tinh, 12 cung, năm hành và 64 quẻ. Không dùng số lượng ngũ hành làm kết luận vượng suy. Gợi ý theo vị trí hào động là văn bản chiêm nghiệm, không giả làm bản dịch hào từ gốc. Không đưa dự báo chắc chắn về sức khỏe, tài chính hoặc hôn nhân. Các lớp nghiên cứu chuyên sâu và so sánh lưu niên cũ vẫn có trong bản lưu V52, chưa đưa vào luồng sử dụng mới.

## Tham khảo cách tổ chức

Đã xem [biểu mẫu Tử vi Việt Nam trên tuvi.vn](https://tuvi.vn/tuvivietnam) để tham khảo luồng nhập ngày, lịch, giới tính và xem lá số. Không sao chép thiết kế, nội dung luận giải hoặc nhận kết quả từ trang đó làm dữ liệu kiểm chứng. Thiết kế và văn bản của V53 được soạn lại cho dự án.

## Kiểm chứng

- 50 kiểm tra hồi quy và chức năng trong `qa/test-results.json`; 11 kiểm tra cuối trong `qa/final-check-results.json`; 38 kiểm tra bổ sung trong `qa/year-helper/test-results.json`: đạt 99/99. Hai bộ đầu đã được chạy lại sau cập nhật.
- 336 lá số Tử vi: vị trí toàn bộ sao và thông tin cung khớp V52; gồm nam/nữ, nhiều giờ, tháng nhuận, ba lựa chọn tháng nhuận và hai lựa chọn ngày.
- 288 cấu hình Bát tự: trụ và ngũ hành khớp V52; có hai lựa chọn ngày, biết/không biết giờ, UTC+7/+8/+5:30 và ngày gần chuyển tiết.
- 402 tổ hợp năm và giới tính: nạp âm và cung phi khớp V52 trong toàn dải năm hỗ trợ.
- 64 tổ hợp âm/dương ánh xạ đủ 64 quẻ khác nhau; có nội dung diễn giải. Gieo từng hào, gieo đủ, hào động và quẻ biến hoạt động.
- Thử cả năm mục ở 320, 390, 768 và 1440 px; không tràn ngang trang. Lá số rộng cuộn trong vùng riêng. Đã nhìn ảnh màn hình máy tính, điện thoại và giao diện in.
- Kiểm tra ngày không tồn tại, tháng nhuận không tồn tại, bỏ trống, thiếu giờ tại mốc chuyển trụ, vô hiệu kết quả cũ, lưu/mở/xóa hồ sơ, TXT, nút in, Escape đóng dialog và chuỗi nhập có ký tự HTML.
- Không lỗi JavaScript, không yêu cầu HTTP từ HTML phát hành trên lượt kiểm tra chính.
- 605 tệp bản lưu trong manifest V52 giữ nguyên byte; bỏ qua tệp trạng thái dự án vốn được cập nhật theo tiến độ.

Các kết quả là kiểm thử tự động cục bộ trên Chromium và rà soát ảnh; chưa phải thử nghiệm với một nhóm người dùng hoặc cam kết hỗ trợ mọi trình duyệt cũ.

## Tái lập và phát hành

`node v53/scripts/build.mjs` tạo HTML độc lập từ `index.html`, CSS và bốn tệp JS. Không cần npm install. Các script kiểm thử dùng Playwright đã có trong môi trường làm việc; đường dẫn runtime được ghi trong script.

`extract-engine.mjs` và `extract-yi.mjs` dùng V52 trong workspace để tái trích bảng/hàm; không cần chạy chúng cho mỗi thay đổi giao diện. Mã HTML/CSS/JS hiện tại đủ để build bản web độc lập.

`scripts/package.py` đóng gói web và nguồn, ghi manifest SHA-256. Hash dùng nhận dạng tệp cục bộ, không phải chữ ký nhà phát hành. Gói web chỉ chứa `index.html` và hướng dẫn sử dụng; gói nguồn chứa mã dự án, báo cáo và bằng chứng kiểm thử riêng.
