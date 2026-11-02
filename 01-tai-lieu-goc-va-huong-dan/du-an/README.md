# Huyền Học Các

Kho hiện hành: [dedaithien-sudo/huyen-hoc](https://github.com/dedaithien-sudo/huyen-hoc), công khai theo yêu cầu chủ dự án. Đợt bổ sung mới: [nghiên cứu AI-01 ngày 31/10/2026](collaboration/imports/ai01-2026-10-31/README.md), gồm Ngũ Hành Tinh Kỷ đối chiếu Tam Mệnh và chứng cứ WYG. Những liên kết tới tài khoản cũ trong hồ sơ gốc là xuất xứ lịch sử, không phải vị trí làm việc hiện hành.

Ứng dụng web và kho nghiên cứu Tử vi, Bát tự, Dịch học, Mai Hoa và nhà ở. Dự án đang phát triển; việc đọc một trang hoặc kiểm thử đạt không đồng nghĩa áp dụng hết một tác phẩm.

## Mở ứng dụng

Mở `Huyen_Hoc_Cac.html` bằng trình duyệt. Tệp HTML độc lập đã chứa nội dung cần thiết để sử dụng ngoại tuyến. Mã làm việc ở `v53/`; bản site sạch ở `v53/site/index.html`.

## Tiếp tục công việc

Đọc `AGENTS.md`, `STORAGE_POLICY.md`, `collaboration/START_HERE.md`, `POST_RELEASE_WORKING_FOLLOWUP.json`, rồi ma trận `v53/research/library-current/COVERAGE.json`. Trạng thái mới sau phát hành nằm ở chỉ dẫn làm việc, không suy từ báo cáo cũ rằng đã đóng gói phần mới.

Nguồn, bằng chứng và kiểm thử nằm ngoài site. Giữ khác biệt giữa truyền bản, chữ nguồn, quy ước biên tập, suy luận và điều chưa xác minh. Khi thiếu tiền đề, giữ trạng thái chưa biết.

## Phạm vi bản GitHub

Toàn bộ tư liệu đối chiếu hiện có được bàn giao riêng trong [bản phát hành materials-v53](https://github.com/dedaithien-sudo/huyen-hoc/releases/tag/materials-v53). Đọc [hướng dẫn tư liệu](collaboration/materials/README.md), [chỉ mục PDF/DjVu](collaboration/materials/SOURCE_BOOKS.md) và [điểm vào cho ChatGPT web](collaboration/WEB_HANDOFF_PROMPT.md). Các tệp lớn nằm trong release công khai, có SHA-256 và công cụ tải/khôi phục; không nằm trong lịch sử Git.

Nhánh Git chứa mã, tài liệu, bản chép văn bản và kết quả kiểm chứng nhỏ. PDF/DjVu/ảnh gốc, SQLite phục hồi và thư viện thực thi được bàn giao qua release; ZIP tổng hợp lặp lại nội dung và lịch sử chat Codex ngoài dự án giữ tại máy theo `STORAGE_POLICY.md`. Vì vậy chỉ clone nhánh Git chưa có toàn bộ kho bằng chứng; cần khôi phục các gói tư liệu cần thiết. Không tự đánh dấu một kiểm thiếu nguồn là đạt, hoặc tải lại nguồn chỉ để khôi phục số lượng.

Các bản chép và tài liệu bên thứ ba giữ xuất xứ trong hồ sơ nguồn; việc có trong kho không tự cấp giấy phép mới cho nội dung đó.

## Cộng tác

Mỗi đầu việc dùng nhánh `codex/<ten-viec>` và pull request. Đọc trạng thái mới trước khi sửa, ghi tệp đã sửa và kết quả kiểm chứng vào PR. Không tự triển khai website hoặc cập nhật gói nguồn lớn từ môi trường thiếu bằng chứng. Người điều phối tại máy kiểm chứng và hợp nhất các thay đổi.
