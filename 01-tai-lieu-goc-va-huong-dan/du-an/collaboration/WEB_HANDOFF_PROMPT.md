# Nhiệm vụ tiếp tục cho ChatGPT web / Codex

Dự án công khai: [dedaithien-sudo/huyen-hoc](https://github.com/dedaithien-sudo/huyen-hoc), nhánh `main`.

## Trạng thái đồng bộ

Gói 13 nhánh ở commit cục bộ `14fec7f82a84a0a2aec9ecebd343a2300fbebd89`; lần push bị GitHub từ chối HTTP 403 do tài khoản bị đình chỉ. Nếu đang đọc GitHub, commit đó và chỉ mục 13 nhánh chưa có trên remote; `main` trực tuyến còn ở `621d3c7e11098dd34269714d5acd7ed7a67fdfee`.

## Đọc trước

1. `AGENTS.md` và `STORAGE_POLICY.md`.
2. `PROJECT_RESEARCH_STATE.md`, `EXHAUSTIVE_WORK_STATE.json`, `v53/NEXT_STEPS.md` và `v53/research/library-current/COVERAGE.json`.
3. `collaboration/START_HERE.md` và `collaboration/imports/recovery-13-branches-2026-11-01/BRANCH_INDEX.md`.
4. `collaboration/materials/README.md`, `SOURCE_BOOKS.md`, `FILE_INDEX.json` để tìm đúng tư liệu nguồn.

## Công việc hiện hành

Tiếp từ `EXHAUSTIVE_WORK_STATE.json`, không mở lại việc đã làm chỉ để tăng số kiểm. Trạng thái hiện tại ghi M01 — Thực thần C16/C23/C31; mục tiếp theo gồm điều kiện C19/C21, C22, C30, C35 và các hướng luân phiên B02/P08/Tử Vi. Ma trận và báo cáo hiện hành là chuẩn đối chiếu.

13 thư mục `collaboration/imports/recovery-13-branches-2026-11-01/branches/AI-01`…`AI-13` là các luồng nghiên cứu được khôi phục để chọn cho phạm vi sau. Ref nhánh/PR/SHA và kết quả test ghi trong các handoff là lịch sử, chưa được xác minh với remote hiện tại. Danh mục 33 tài sản chỉ có 3 bản byte gốc, 25 bản trích xuất chưa xác minh byte và 5 tệp gốc không lấy được; đặc biệt AI-10 thiếu 11/24 tệp test. Không áp bản vá trích xuất. File Markdown rời do người dùng gửi trùng từng byte với bản trong ZIP, không phải nguồn nội dung bổ sung.

## Truy cập nguồn

Tư liệu công khai ở release [`materials-v53`](https://github.com/dedaithien-sudo/huyen-hoc/releases/tag/materials-v53). Dùng chỉ mục file và `maintenance/materials-range.py` để lấy đúng khoảng byte; cần ghi hash và xác nhận đã thực sự đọc/xem ảnh. Nếu connector không tải hoặc giải nén được, nêu rõ giới hạn. Không coi bản chép số là nhân chứng độc lập.

## Quy tắc làm việc

Giữ riêng nguyên văn, bản chép, quy ước, suy luận và phần chưa xác minh. Hoàn thiện quy tắc có đủ tiền đề theo từng truyền bản; khi thiếu nguồn, chuyển sang nhánh độc lập có thể làm. Ghi tiến độ và kiểm chứng trong tài liệu nội bộ, không hỏi người dùng sau mỗi tiểu mục có thể làm độc lập.

Khi sửa mã, tạo nhánh riêng `codex/<ten-viec>` từ `main` và gửi PR nếu phiên có quyền ghi. Chỉ chạy kiểm phù hợp với thay đổi. Giữ corpus, nguồn, QA, suy luận và bảng engine ngoài site; web chỉ trình bày kết quả, diễn giải dễ hiểu. Không tự triển khai site, tạo snapshot ZIP lặp, hoặc tuyên bố toàn kho đã hoàn tất khi còn mục mở.
