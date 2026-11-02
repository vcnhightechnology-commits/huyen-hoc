# AI-11 — hướng nghiên cứu tiếp theo

**Phạm vi:** Hán Nôm — Chỉ mục nguồn và khảo dị kinh truyện

**Trạng thái:** hồ sơ phục hồi từ gói ngày 01/11/2026; ref Git/PR/SHA và số kiểm thử nêu trong hồ sơ là dữ liệu lịch sử, chưa xác nhận là trạng thái hiện hành. Đây là thư mục nghiên cứu, không phải Git branch được checkout.

## Hướng đang mở theo hồ sơ

Cần ảnh gốc/folio, SHA-256 ảnh/PDF, kiểm nhân chứng in độc lập và Node trên checkout hoàn chỉnh.

## Vị trí dự án hiện tại nên đối chiếu trước

- `v53/research/library-audit`
- `v53/research/library-current/COVERAGE.json`
- `v53/research/yi-*`

Các đường dẫn trên là điểm tra cứu gợi ý; cần xác nhận đúng phạm vi nguồn trước khi tái dùng. Không chạy lại batch đã có payload. Chỉ nhận một quy tắc hoặc patch sau khi có byte nguồn đáng tin cậy, đối chiếu checkout hiện hành và chạy kiểm phù hợp.

## Bằng chứng phục hồi

- Bản bàn giao gốc: [`HANDOFF.md`](HANDOFF.md).
- Bản trích xuất chưa xác minh byte gốc: `evidence/extracted-unverified/`; không dùng `git apply` hoặc thực thi.
- Hash và ánh xạ nguồn nằm trong `../../IMPORT_VERIFICATION.json`.
