# AI-13 — hướng nghiên cứu tiếp theo

**Phạm vi:** Lịch Pháp — Tiết Khí, Can Chi và quy ước lịch Việt Nam

**Trạng thái:** hồ sơ phục hồi từ gói ngày 01/11/2026; ref Git/PR/SHA và số kiểm thử nêu trong hồ sơ là dữ liệu lịch sử, chưa xác nhận là trạng thái hiện hành. Đây là thư mục nghiên cứu, không phải Git branch được checkout.

## Hướng đang mở theo hồ sơ

Cần chứng thực lịch hành chính gốc 1975 miền Nam, đối ảnh/PDF HKO và SHA, chạy đầy đủ CI và hồi quy chuyển ngày; chưa tự chọn lá số khi nguồn lịch mơ hồ.

## Vị trí dự án hiện tại nên đối chiếu trước

- `v53/research/month-boundaries`
- `v53/engine.js`
- `v53/research/library-current/COVERAGE.json`

Các đường dẫn trên là điểm tra cứu gợi ý; cần xác nhận đúng phạm vi nguồn trước khi tái dùng. Không chạy lại batch đã có payload. Chỉ nhận một quy tắc hoặc patch sau khi có byte nguồn đáng tin cậy, đối chiếu checkout hiện hành và chạy kiểm phù hợp.

## Bằng chứng phục hồi

- Bản bàn giao gốc: [`HANDOFF.md`](HANDOFF.md).
- Bản trích xuất chưa xác minh byte gốc: `evidence/extracted-unverified/`; không dùng `git apply` hoặc thực thi.
- Hash và ánh xạ nguồn nằm trong `../../IMPORT_VERIFICATION.json`.
