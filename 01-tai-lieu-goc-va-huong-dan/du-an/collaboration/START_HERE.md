# Điểm tiếp tục cho cộng tác GitHub

Kho hiện hành công khai: [dedaithien-sudo/huyen-hoc](https://github.com/dedaithien-sudo/huyen-hoc), nhánh `main`. Tư liệu nguồn trong release [`materials-v53`](https://github.com/dedaithien-sudo/huyen-hoc/releases/tag/materials-v53) cũng là công khai.

## Đồng bộ mới nhất

Commit cục bộ `14fec7f82a84a0a2aec9ecebd343a2300fbebd89` chứa bộ 13 nhánh, nhưng chưa lên GitHub: remote trả HTTP 403 vì tài khoản bị đình chỉ. Bản `main` trực tuyến vẫn ở `621d3c7e11098dd34269714d5acd7ed7a67fdfee`.

## Trạng thái cần đọc trước khi tiếp tục

- `PROJECT_RESEARCH_STATE.md` và `EXHAUSTIVE_WORK_STATE.json`: phạm vi, trạng thái và ưu tiên hiện hành. Công việc đang mở vẫn là M01, Thực thần C16/C23/C31; các mục C19/C21/C30 và các hướng B02/P08/Tử Vi được ghi tại `subsequentPriority`.
- `v53/research/library-current/COVERAGE.json`: ma trận độ phủ hiện hành. `v53/NEXT_STEPS.md` là nhật ký hướng tiếp nối, không dùng các mốc lịch sử làm trạng thái live.
- `collaboration/imports/recovery-13-branches-2026-11-01/BRANCH_INDEX.md`: 13 luồng phục hồi, bản bàn giao và hướng cho lần nghiên cứu sau. Đây là thư mục nghiên cứu; Git hiện làm việc trên `main`, không phải 13 nhánh mã đang xác minh.
- `collaboration/imports/ai01-2026-10-31/README.md` và `IMPORT_VERIFICATION.json`: tư liệu AI01 trước đó, nội dung chưa được biến thành quy tắc engine.
- `collaboration/materials/README.md` và `collaboration/WEB_HANDOFF_PROMPT.md`: cách truy cập nguồn công khai và hướng dẫn cho phiên web.

## Giới hạn chứng cứ của bộ 13 nhánh

ZIP phục hồi ngày 01/11/2026 có hash được ghi trong `IMPORT_VERIFICATION.json`; file Markdown rời khớp từng byte với bản bên trong ZIP. Danh mục gói ghi 3/33 tệp byte gốc, 25 bản text trích xuất chưa xác minh byte gốc và 5 tệp gốc không lấy được. Các patch trích xuất không được áp tự động. Báo cáo AI-10 xác nhận mới 13/24 tệp test, thiếu 11 tệp nên full suite chưa đạt. Số liệu kiểm ở handoff là tuyên bố lịch sử cho đến khi chạy lại trên checkout đầy đủ.

## Cách tiếp tục

Làm theo con trỏ hiện hành, giữ nguyên dị bản/truyền bản và ghi nguồn, byte/SHA-256, giới hạn, suy luận cùng kiểm chứng trong tài liệu nội bộ. Khi mã thay đổi, tạo nhánh `codex/<ten-viec>` từ `main`, chạy kiểm phù hợp và gửi PR nếu phiên có quyền ghi. Web chỉ trình bày kết quả dễ hiểu; giữ corpus, nguồn, QA và bảng so engine ngoài site. Không tạo snapshot ZIP lặp hoặc tự xem toàn kho là đã hoàn tất.
