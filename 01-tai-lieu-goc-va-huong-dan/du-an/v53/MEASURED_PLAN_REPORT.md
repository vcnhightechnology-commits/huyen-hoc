> Bản cập nhật sau phạm vi mặt bằng: `BIRTH_HOUR_RANGE_REPORT.md`. Các byte/kiểm tra trong báo cáo mặt bằng này là mốc hoàn thành trước đó; chức năng mặt bằng và mã nguồn của nó được giữ nguyên.

# Mặt bằng theo số đo — V53, 26/10/2026

Đã thêm mục **Ghi mặt bằng theo kích thước** tại **Hướng nhà → Bố trí các phòng**. Mục thu gọn mặc định, không cần ngày sinh. Đây là bước tiếp theo của hạng mục mặt bằng/Bắc/kích thước/cửa thực còn mở, không phải hoàn tất toàn bộ phong thủy nhà ở hoặc bốn hướng nghiên cứu.

Người dùng nhập khung một tầng chữ nhật, ngang/sâu theo mét, hướng lên trên của sơ đồ theo Bắc thật và bất định góc. Mỗi phòng là một chữ nhật có tọa độ X/Y từ góc trên trái; có thể ghi cửa đi/cửa sổ trên bốn cạnh ngoài. Không tự điền góc đo hoặc kích thước. Hiện giới hạn30phòng/60cửa, chiều khung0,1–1.000m; nhà méo/lõm/nhiều tầng và cửa nội bộ chưa mô hình hóa.

## Kết quả và phép tính

- Hình SVG có kích thước, số phòng, vị trí cửa/cửa sổ, tâm khung và mũi Bắc quay theo góc thật đã nhập. SVG tải riêng có cả chú giải tên/diện tích phòng; không phụ thuộc ảnh hoặc mạng.
- Tâm phòng so với tâm khung cho khoảng cách và góc hướng. Tâm trùng nhau thì không tạo góc giả. Phòng chứa tâm hoặc chạm tâm tại ranh được ghi riêng. Hướng của tâm không đại diện mọi điểm trong một phòng.
- Hướng nhìn ra ngoài một cạnh lấy pháp tuyến cạnh theo hình học. Tái dùng bộ tám hướng và24sơn đã kiểm nguồn trước, giữ mọi khả năng trong miền sai số. Không tự xem một cạnh/cửa là hướng nhà của mọi phép phong thủy, không thay lựa chọn vị trí tương đối trong bộ gợi ý7phòng cũ.
- Các phòng vượt khung bị từ chối; chạm cạnh hợp lệ. Phòng chồng nhau được báo diện tích giao. Diện tích phòng phủ tính hợp các chữ nhật bằng các dải X và hợp khoảngY, nên chồng ba phòng không bị cộng/trừ sai. Cửa trùng đoạn trên cùng cạnh cũng có thông báo.
- Thay số đo/thêm/xóa hàng làm xóa bản vẽ cũ; sự kiện `change` đến muộn với cùng dữ liệu không xóa kết quả vừa tính. Lỗi này được phát hiện khi thử bấm tải và đã sửa bằng chữ ký dữ liệu biểu mẫu.

Tải TXT giữ đủ số đo, phòng, cửa, hướng, vùng sai số và giới hạn mô hình; tải SVG giữ bản vẽ cùng tên phòng. In tự mở mục có kết quả, giấu phần nhập và trả lại trạng thái sau in. Số đo chỉ tồn tại trong bộ nhớ phiên; đổi mục nhà ở vẫn giữ, tải lại trang thì xóa. Không tự lưu localStorage hoặc gửi dữ liệu đi.

## Căn cứ và ranh giới nguồn

Mô hình chữ nhật, hệ tọa độ, tâm hình, hợp diện tích và phép quay là quy ước hình học triển khai được định nghĩa đầy đủ trong `research/measured-plan/SPECIFICATION.md`. Không gán các quy ước chia phòng này cho một đoạn sách cổ chưa đọc. Bảng24sơn tái dùng `research/full-study/home/RULE_24_MOUNTAINS.json` và ảnh Hiệp Kỷ đã lưu; không tải lại hoặc nâng số lượng nguồn. Bảng hướng/sai số giữ nguyên byte. Chưa áp quy tắc Phi tinh hoặc tự chấm phòng/cửa cát hung. Ranh năm cung phi và các dị bản Tử vi/Bát tự vẫn giữ trong backlog.

## Kiểm chứng

**133/133 kiểm tra tự động đạt:**18kiểm hình học mới,25kiểm trình duyệt mới,40hồi quy nhà ở và50hồi quy lõi. Mẫu gồm giao ba phòng, phòng nằm trong nhau, cạnh chung, tâm trùng/tâm trên ranh,9góc quay,8ranh hướng,4cạnh cửa,13dữ liệu sai, nhãn có ký tựHTML, sự kiện nhập muộn,TXT/SVG/in và320/390/768/1440px. Không lỗiJavaScript hoặcHTTP từHTMLđộc lập.

PDF thử chế độprint thật có3trang, giữ đủ hai phòng/hai cửa, diện tích và hướng, giấu ô nhập/nút điều hướng. Đã xem cả3trang và ảnh điện thoại; tăng cỡ số phòng và nhãn trênSVG để đọc rõ hơn. LầnQA trước tạoPDF theo `screen` do kịch bản giữ chế độemulate; đã sửa kịch bản và tạo lạiPDF chế độprint trước phát hành. TệpQA hiện hành ở `qa/measured-plan/`.

Mã thêm: `home-measured-plan.js`, `home-measured-plan.css`; đăng ký vào `index.html`/`scripts/build.mjs`. `engine.js`, `app.js`, `home-guide.js`, `home-content.js`, `bearing-guide.js`, `mountains.js` giữ nguyên byte. Snapshot trước phạm vi: `archives/v53-before-measured-plan/`. Nguồn,HTMLđộc lập,sitevàhaiZIP cập nhật cùngV53 sau kiểmtra; không xuất bản.

Kiểm lại: `node v53/scripts/verify-measured-plan.mjs`, `node v53/scripts/verify-measured-plan-browser.mjs`, `python v53/scripts/verify-measured-plan-release.py --no-write`.

## Byte phát hành

HTML hiện hành654.730byte, SHA-256`74d397db30d9b14c83dba0f5dfbb76aa9285d1a8c9e92540b9c8870a034dad2d`. Ba bản gốc/V53/site đồng nhất;838tệp trongmanifest. Góiweb chỉhai tệpHTML/hướngdẫn;gói nguồn cótài liệu/QAriêng. Kếtquảkiểm đồngnhất ở`qa/measured-plan/RELEASE_RESULTS.json`;bảnsnapshottrướcgiữ nguyên.
