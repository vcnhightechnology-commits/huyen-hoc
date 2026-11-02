# Cửa thông giữa các phòng — V53

Hoàn thành phạm vi ngày 26/10/2026, giữ cùng V53 và không xuất bản. Snapshot trước phạm vi: `../archives/v53-before-internal-doors/`. Đây là bước phát triển công cụ ghi mặt bằng, không phải hoàn tất phong thủy nhà ở hoặc bốn hướng nghiên cứu.

## Kết quả cho người dùng

Tại **Hướng nhà → Bố trí các phòng → Ghi mặt bằng theo kích thước**, thêm **Cửa thông giữa các phòng**. Chọn hai phòng có đoạn cạnh chung, nhập vị trí bắt đầu và rộng cửa. Gợi ý ngay dưới hàng nhập ghi tên hai phòng, chiều dài đoạn chung, chiều đo và tọa độ đầu đoạn; tránh tính nhầm offset từ góc riêng của từng phòng.

Hình vẽ dùng ký hiệu tím **N1, N2…** cho cửa nội bộ, giữ riêng cửa đi/cửa sổ trên viền ngoài. Danh sách kết quả ghi cặp phòng, đoạn chung và hai đầu cửa. TXT giữ toàn bộ số đo; SVG tải riêng có ký hiệu và tên cửa. In/PDF mở phần mặt bằng có kết quả, giấu ô nhập rồi khôi phục trạng thái thu gọn.

Đổi tên phòng giữ đúng liên kết và cập nhật tên trong ô chọn. Xóa phòng làm bỏ trống lựa chọn liên quan; các cửa không dùng phòng ấy giữ nguyên danh tính dù số thứ tự phòng thay đổi. Thêm/xóa/đổi số đo xóa bản vẽ cũ, tránh tải kết quả không còn khớp biểu mẫu. Dữ liệu chỉ ở phiên mở, không tự lưu hồ sơ hoặc gửi mạng.

Trên điện thoại, hai ô chọn phòng và tên cửa dùng cả chiều rộng hàng; phần gợi ý nhắc lại đầy đủ tên đã chọn. Ký hiệu N được tăng cỡ sau khi xem ảnh điện thoại/PDF. Không điền sẵn kích thước hay cửa mẫu vào form thật.

## Mô hình và giới hạn

Phòng vẫn là chữ nhật trong một khung chữ nhật một tầng. Đường ranh phòng được mô hình hóa không có bề dày. Hai phòng phải dùng chung một đoạn cạnh dài dương: chạm góc, tách nhau hoặc chồng diện tích không đủ điều kiện. Chưa nối qua bề dày tường hoặc khoảng hở giữa hai chữ nhật. Đây là giới hạn mô hình cần giữ khi diễn giải số đo.

Offset tính từ đầu trên/trái của **phần cạnh chung**, không tự lấy góc phòng. Cửa phải nằm trọn đoạn; nếu một phòng thứ ba chạm/phủ chiều dài dương của đoạn cửa thì báo lỗi để người dùng kiểm lại các vùng phòng. Hai cửa trùng một đoạn có thông báo độ dài trùng; chỉ chạm đầu không bị coi là trùng chiều dài. Tối đa60 cửa nội bộ, ngoài nhóm tối đa60 cửa/cửa sổ viền ngoài đã có.

Cửa nội bộ không có một pháp tuyến ra ngoài duy nhất, nên không tự gán hướng phong thủy, chiều mở cánh, độ thông gió hoặc đánh giá lối thoát từ nét cửa. Danh sách chỉ thể hiện cửa đã nhập. Tính diện tích phòng phủ, góc hướng phòng, bất định hướng,24sơn và cửa viền ngoài giữ nguyên dữ liệu kết quả cũ.

## Nguồn và quy ước triển khai

Không tải thêm nguồn bên ngoài trong phạm vi này. Mô hình đoạn chung/giao khoảng, tọa độ và mã phòng ổn định là quy ước hình học được mô tả tại `research/internal-doors/SPECIFICATION.md`, có ví dụ tính tay và phản ví dụ; không gán cho sách cổ chưa đọc.

Tái dùng nguồn Hiệp Kỷ/CADAL06056503 và bảng24sơn đã kiểm trước để giữ tính hướng viền ngoài. Container nguồn vẫn **3.433.014 byte**, SHA-256 `bfd3b76c55d62324919ab161c8c2ba2ecb129b3b2c59a3ab0428807e8f8278db`. Các nguồn này không được dùng làm bằng chứng cho cách đặt cửa giữa phòng. Byte/SHA từng nguồn và mô-đun tái dùng ở `research/internal-doors/REUSED_SOURCES.json`; tài liệu và QA ở ngoài site.

`engine.js`, `app.js`, nội dung bảy phòng, bảng hướng/sai số/24sơn, Bát tự, Tử vi và Kinh Dịch giữ nguyên byte so với snapshot ngay trước. Không chạy lại iztro hoặc lunar-typescript để tăng số đối chiếu khi không đổi những phép tính ấy.

## Kiểm thử

**137/137 kiểm chính đạt:**20 hình học/tích hợp mới,27 trình duyệt mới,40 hồi quy nhà ở và50 hồi quy lõi. Bộ40 dùng lại các xác nhận đã có với baseline là snapshot trước cửa nội bộ; runner lịch sử giữ nguyên. Kết quả mới ở `qa/internal-doors/`; hồi quy lõi ở `qa/test-results.json`.

- Cạnh chung ngang/đứng và chỉ chung một phần, thứ tự chọn phòng đảo, cửa dùng hết đoạn/chạm đầu,17 đầu vào sai, ba kiểu không kề hợp lệ, phòng thứ ba, cửa trùng/chỉ chạm đầu và sai số tính toán1e-8m.
- **50 mô hình góc/bất định** cho kết quả diện tích/phòng/cửa ngoài/24sơn giống hệt module trước thay đổi; tọa độ cửa nội bộ không đổi khi xoay cách quy hướng. Đây là kiểm tương thích với phiên bản trước, không phải đối chứng bằng một thư viện hình học độc lập.
- Đổi tên/xóa phòng và đổi chỉ số, sự kiện nhập trễ, lỗi số đo xóa kết quả cũ, tên có ký tự HTML, tải TXT/SVG, lưu trong phiên và khôi phục trạng thái sau in.
- Màn hình320/390/768/1440px không tràn ngang; bộ nhà ở còn kiểm650/1024px. Không lỗi JavaScript hoặc HTTP từ HTML độc lập. Không đưa nguồn/corpus/ma trận nghiên cứu lên trang người dùng.

PDF mẫu **ba trang** ở chế độ print thật, đã render và xem đủ ba trang. Tên hai cửa, hai cặp phòng, hai đầu đoạn và cửa viền ngoài còn đủ; nhóm cửa nội bộ giữ cùng một trang trong mẫu, form bị giấu. Kiểm trích chữ/hash tại `qa/internal-doors/PDF_RESULTS.json`. Không coi mẫu ba phòng/hai cửa này bao phủ mọi số lượng hay mọi bố cục in.

Các fixture là dữ liệu kiểm do tác giả đặt, không phải sơ đồ nhà thực của người dùng. 137 là số nhóm kiểm nêu trên; không cộng50 mô hình hoặc ba trang PDF thành số lượt kiểm bổ sung.

## Mã và phát hành

Thêm `home-internal-doors.js`, tích hợp vào `home-measured-plan.js`, CSS, `index.html` và `scripts/build.mjs`. Không đổi các mô-đun tính lịch/an sao/đại vận. Đồng bộ root HTML, HTML V53, `site/index.html`, README và hai ZIP sau khi kiểm.

HTML **677.537 byte**, SHA-256 `eb1425292f680ac60dd1af57ac805f6312d209ad92d72c4f6499de0502d9ff22`. Gói web chỉ có HTML độc lập và hướng dẫn; gói nguồn có mã, nguồn tái dùng, đặc tả và QA. `verify-internal-doors-release.py --no-write` kiểm manifest/từng byte trong ZIP và snapshot cuối phạm vi.

Nhà méo/lõm/nhiều tầng, tường có bề dày, cách xác định tọa/hướng theo truyền phái, ranh năm cung phi và Phi tinh vẫn còn mở. Các hướng Bát tự/Tử vi/Kinh Dịch giữ backlog hiện hành, không bị đánh dấu hoàn tất bởi tính năng mới này.
