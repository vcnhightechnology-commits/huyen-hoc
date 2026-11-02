# AI-05 — hướng nghiên cứu tiếp theo

**Phạm vi:** Mai Hoa Dịch Số — Lục thần, Thể–Dụng, ngoại ứng

**Trạng thái:** hồ sơ phục hồi từ gói ngày 01/11/2026; ref Git/PR/SHA và số kiểm thử nêu trong hồ sơ là dữ liệu lịch sử, chưa xác nhận là trạng thái hiện hành. Đây là thư mục nghiên cứu, không phải Git branch được checkout.

## Hướng đang mở theo hồ sơ

Dị bản lập quẻ, điều kiện Thể/Dụng và Hậu thiên thời-phương, ngoại ứng, đoán chữ; không gắn suy luận khi chưa xác định bản và ngữ cảnh.

## Vị trí dự án hiện tại nên đối chiếu trước

- `v53/research/meihua`
- `v53/research/meihua-methods`
- `v53/research/meihua-reading`
- `EXHAUSTIVE_WORK_STATE.json#previousMaiHoaWork`

Các đường dẫn trên là điểm tra cứu gợi ý; cần xác nhận đúng phạm vi nguồn trước khi tái dùng. Không chạy lại batch đã có payload. Chỉ nhận một quy tắc hoặc patch sau khi có byte nguồn đáng tin cậy, đối chiếu checkout hiện hành và chạy kiểm phù hợp.

## Bằng chứng phục hồi

- Bản bàn giao gốc: [`HANDOFF.md`](HANDOFF.md).
- Bản trích xuất chưa xác minh byte gốc: `evidence/extracted-unverified/`; không dùng `git apply` hoặc thực thi.
- Hash và ánh xạ nguồn nằm trong `../../IMPORT_VERIFICATION.json`.
