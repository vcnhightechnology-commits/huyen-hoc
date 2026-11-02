> Cập nhật tiếp theo: `FORTUNE_CONTEXT_REPORT.md`. Byte và kiểm tra của báo cáo khoảng giờ này là mốc trước đó; mã và chức năng Bát tự giữ nguyên trong đợt vận hạn.

# Khoảng khởi vận khi chưa rõ giờ sinh — V53, 26/10/2026

Kết quả Bát tự nay trình bày **mốc khởi vận sớm nhất và muộn nhất** khi người dùng chọn chưa rõ giờ sinh. Mười chặng đại vận có khoảng khởi và khoảng chuyển sang vận kế. Không điền một giờ sinh giả, không dựng trụ giờ và không gán một ngày giao vận duy nhất.

Nếu ba trụ năm/tháng/ngày có thể thay đổi trong ngày sinh, mô-đun tiếp tục yêu cầu bổ sung giờ thay vì ghép các lá số khác nhau. Điều này bao gồm ngày đi qua tiết mở tháng/năm và lựa chọn đổi ngày từ23h khi chưa rõ giờ. Khi nhập đủ giờ/phút, kết quả trở lại phép tính một mốc đã có.

## Cách tính và giới hạn

Dùng đúng engine HHC và quy ước khởi vận theo phút đang chọn. Thử đủ1.440phút sinh được hỗ trợ từ00:00đến23:59 của ngày và múi giờ đã nhập. Mỗi khả năng được lập lại Bát tự thật, kiểm ba trụ ổn định, tính chiều vận, phần lẻ khởi vận và mười chặng với quy tắc cộng/kẹp ngày cuối tháng đã có. Lấy cực trị riêng ở cả11ranh chặng; không chỉ lấy giờ0/trưa/23h hoặc thay bằng nhãn tuổi năm.

Các khoảng là **cận của tập khả năng**, không khẳng định mọi thời điểm ở giữa đều đạt được. Độ phân giải theo phút và sai khác lịch tiết khí đã biết vẫn giữ nguyên: mẫu cũ có mốc HHC/lunar chênh tối đa124giây, quy đổi có thể khác6giờ giao vận. Không mở rộng sự trùng của một ngày mẫu thành mọi ngày hoặc mọi truyền phái. Không thêm cách làm tròn theo chi giờ hoặc tự chọn dụng thần.

Bộ nhớ đệm tối đa20ngày/cấu hình chỉ ởRAM, không localStorage. Dữ liệu trả về được tách khỏi bản lưu để sửa một kết quả không làm hỏng lần đọc khác. Lưu hồ sơ vẫn chỉ lưu đầu vào, không lưu giờ neo hoặc khoảng tính sẵn; mở hồ sơ tính lại. Các ô giờ/phút giữ trống khi chưa rõ giờ.

## Nguồn

Tái dùng Tam Mệnh WYG quyển2 đoạn66a–68a và các byte thư viện lunar-typescript1.8.6 đã lưu, đã nghiên cứu trong `research/full-study/bazi/RESEARCH_NOTES.md`. Đoạn sách cho chiều vận/tỷ lệ ba ngày một năm/phần lẻ và mười năm một chặng; việc quét phút, lấy cực trị và cộng lịch dương kẹp ngày là triển khai số hóa được nêu riêng. Không gán phép quét1.440phút cho nguyên văn sách. Không tải thêm bản sách hoặc gói npm trong phạm vi này. Liên kết byte/SHA ở `research/unknown-hour-range/SOURCE_AUDIT.json`.

## Kiểm tra

**108/108 kiểm tự động đạt:**8kiểm engine mới,16kiểm trình duyệt mới,50hồi quy lõi và34hồi quy các phần mở rộng trước. Chi tiết:

-12ngày/cấu hình,17.280lần lập Bát tự có giờ thật và264cực trị ranh: trùng hoàn toàn khoảng của mô-đun mới. Có29/2, cuối tháng,1900/2100, hai giới vàUTC−12/0/+5:30/+7/+8/+14. Đây là kiểm nhất quán cùng engine, không gọi là lịch độc lập.
-Ngày15/10/2026UTC+8, cảhai giới:2.880lần `lunar-typescript.getYun(...,2)` thật khớp từng mốc và hai cực trị. Các mốc tiết ở ngày mẫu này có cùng phần phút; sai khác của các ngày khác không bị xóa.
-Chặn trụ bất định, độc lập với giờ neo nội bộ, tách bộ nhớ đệm, không thay dữ liệu đầu vào. Mười khoảng chuyển nối đúng khoảng khởi của hàng sau.
-Lưu/mở/TXT/in, nhập giờ rồi bỏ giờ, đổi quy ước ngày,320/390/768/1440px; bảng cuộn nội bộ và có nhắc vuốt ngang.0lỗiJavaScript/HTTP của bản độc lập.
-PDF4trang giữ hai cận và đủ10khoảng chuyển; đã xem cả4trang và ảnh điện thoại trước phát hành.

TệpQA: `qa/unknown-hour-range/`. Mã đổi: `bazi-cycles.js`, `full-study.css`. Engine lịch/lập trụ, biểu mẫu/lưu hồ sơ, quan hệ can, vận hạn Tử vi, mặt bằng đo thực giữ nguyên byte. Snapshot trước phạm vi: `archives/v53-before-unknown-hour-range/`. HTMLgốc/V53/site và haiZIP được đồng bộ sau kiểm manifest; tiếp tục cùngV53, không xuất bản.

Tái kiểm: `node v53/scripts/verify-unknown-hour-range.mjs`, `node v53/scripts/verify-unknown-hour-range-browser.mjs`, `python v53/scripts/verify-unknown-hour-range-release.py --no-write`.

## Byte phát hành

HTML657.356byte, SHA-256`ec15e8bbda0445be2acfaa8c2c1a1b7fccc391bf22a91819ff25b5119948ee52`. Ba bản gốc/V53/site đồng nhất;862tệp trongmanifest. Góiweb chỉ`index.html`và`HUONG_DAN.md`, giữ toàn bộ nghiên cứu/QAngoàisite. Kiểm đồngnhất ở`qa/unknown-hour-range/RELEASE_RESULTS.json`.
