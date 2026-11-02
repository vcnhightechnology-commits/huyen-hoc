# AI-10 — hướng nghiên cứu tiếp theo

**Phạm vi:** Tam Thức — Kỳ Môn Độn Giáp, Lục Nhâm, Thái Ất

**Trạng thái:** hồ sơ phục hồi từ gói ngày 01/11/2026; ref Git/PR/SHA và số kiểm thử nêu trong hồ sơ là dữ liệu lịch sử, chưa xác nhận là trạng thái hiện hành. Đây là thư mục nghiên cứu, không phải Git branch được checkout.

## Hướng đang mở theo hồ sơ

Cần khôi phục đủ 24 test, chạy GitHub Actions và V53, đối nguồn S01/S02/S03 và rà người duyệt. PR #11 tiếp tục Draft.

## Vị trí dự án hiện tại nên đối chiếu trước

- `v53/research/library-current/COVERAGE.json (chưa xác định thư mục triển khai tương đương)`

Các đường dẫn trên là điểm tra cứu gợi ý; cần xác nhận đúng phạm vi nguồn trước khi tái dùng. Không chạy lại batch đã có payload. Chỉ nhận một quy tắc hoặc patch sau khi có byte nguồn đáng tin cậy, đối chiếu checkout hiện hành và chạy kiểm phù hợp.

## Bằng chứng phục hồi

- Bản bàn giao gốc: [`HANDOFF.md`](HANDOFF.md).
- Bản trích xuất chưa xác minh byte gốc: `evidence/extracted-unverified/`; không dùng `git apply` hoặc thực thi.
- Hash và ánh xạ nguồn nằm trong `../../IMPORT_VERIFICATION.json`.
