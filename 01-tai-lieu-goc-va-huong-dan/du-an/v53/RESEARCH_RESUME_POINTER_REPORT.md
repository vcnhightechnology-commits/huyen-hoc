# Sửa đường dẫn tiếp tục nghiên cứu B02

29/10/2026. Sửa trạng thái nội bộ; chức năng người dùng giữ nguyên.

COVERAGE.json đã ghi B02 có137đơn vị và137khoảng đọc lượt đầu, nhưng trường currentB02UnitMap vẫn trỏ hồ sơ jinqian cũ136đơn vị/32khoảng đọc đầu/96chỉ đề mục. Khi theo đường dẫn cũ, phần Thiên thời tưởng còn chờ tích hợp dù module, ví dụ và báo cáo đã phát hành từ27/10. Đã trỏ trường này tới liuyao-foundation-span/B02_CURRENT_UNITS.json; phần latestLocalReadingScope cũng trỏ đúng tóm tắt nền mới nhất. Giữ đường dẫn/tóm tắt trước đó trong trường lịch sử, bảo toàn12bản đồ đã có.

## Phạm vi sửa và kiểm

Bản đồ hiện hành137đơn vị/137khoảng đọc đầu/0chỉ đề mục/0áp trọn được chọn theo báo cáo nền đã phát hành, không tự chọn bản có con số lớn nhất. RESUME_INDEX.json ghi rõ hai phạm vi Thiên thời: vai trò191/201vàHằng–ĐạiQuá đã có nên tái dùng; đầy đủ vượng suy/hiệu lực/thời điểm vẫn mở. Chỉ mục mới chỉ bao hai phạm vi B02, chưa là bộ chống trùng cho toàn kho.

research-resume-preflight.py chỉ đọc: kiểm đường dẫn, byte/SHA của bản đồ, đối counts vớiCOVERAGE,137IDriêng và0entireUnitApplied. Phạm vi hoặc danh mục chưa kê trả cần xem độ phủ; không tự coi đã làm hết. Nếu đường dẫn quay về hồ sơ cũ, counts mâu thuẫn hoặc SHA đổi, công cụ dừng để kiểm nguồn. Không nạp engine hoặc chạy quẻ.

Bảy nhóm kiểm đạt, gồm bốn phản kiểm: tái hiện đường dẫn cũ, thay số khoảng, thay SHA và gán toàn bộ137đã áp hết đều bị phát hiện. Bảo toàn danh mục40hồ sơ/16tham chiếu chồng lặp và0toàn tác phẩm đã áp hết; không đổi độ phủ sách từ việc sửa một đường dẫn.

## Lượt làm lặp và bảo toàn chứng cứ

Trước khi phát hiện chỉ dẫn cũ, đã đọc lại đúng phần Thiên thời và viết một module thử trongtmp, gọi thêm2HHC.hexNumber/1compilecho32→28. Những lần này là **chạy lặp**,0ca nguồn độc lập mới; không cộng vào độ phủ hoặc nói là kiểm chứng mới. Module thử không được đưa vàoV53. Báo cáo LIUYAO_WEATHER_ROLES_REPORT.md, module weather-reference.mjs và fixture đã có được dùng lại nguyên byte.

Một lệnh ghép đã render191–198ở180DPI dù bước kiểm thư mục mới báo tồn tại, làm thay tám ảnh dẫn xuất staging144DPI. Đã giữ riêng tám bản180DPI, render phục hồi vào thư mục cách ly, đối đúng cả8SHAđã lưu từ27/10 rồi mới chép lại staging. Tám ảnh gốc staging đã trở lại byte cũ; PDF và mọi bản phát hành không chịu ảnh hưởng. Lỗi thao tác và kết quả phục hồi được ghi trong DUPLICATE_WORK_AUDIT.json. Không nhận việc render lại là trang nguồn mới.

## Gói và cách tiếp tục

Snapshot bản5630tệp/sourceZIP2.949.932.278byte trước sửa đã được sao và kiểmSHA ở archives/v53-before-liuyao-b02-weather/. Tên thư mục được giữ từ lúc chuẩn bị phần tưởng là mới; snapshot nay dùng cho sửa nối trạng thái, không là bản phát hành Thiên thời mới. Những tệpV53cũ giữ nguyên trừ năm tài liệu trạng thái được liệt kê trong verifier. HTML707.411byte/site/index.html/ZIPweb giữ nguyên; nguồn, suy luận vàQA ở ngoài site.

Lệnh chỉ đọc:

    python v53/scripts/research-resume-preflight.py --catalogue B02 --scope weather-voices-and-heng-case
    python v53/scripts/research-resume-preflight.py --catalogue B02 --scope complete-weather-strength-and-timing
    python v53/scripts/test-research-resume-preflight.py --no-write
    python v53/scripts/verify-research-resume-pointer-release.py --no-write

Tiếp các điều kiện chưa khép của B02 và các khoảng trống Bát tự/Tử vi/nhà ở; tra COVERAGEvàchỉ mục hiện hành trước khi dùng staging cũ.137khoảng đọc đầu không đồng nghĩa áp trọn137chương. Toàn kho vẫn đang khai thác.
