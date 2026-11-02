# AI-06 — hướng nghiên cứu tiếp theo

**Phạm vi:** Chu Dịch — Kinh văn, Thập Dực và khảo dị

**Trạng thái:** hồ sơ phục hồi từ gói ngày 01/11/2026; ref Git/PR/SHA và số kiểm thử nêu trong hồ sơ là dữ liệu lịch sử, chưa xác nhận là trạng thái hiện hành. Đây là thư mục nghiên cứu, không phải Git branch được checkout.

## Hướng đang mở theo hồ sơ

Cần đối lại chữ với ảnh in/đồ hình và nguồn độc lập, chạy validator trên checkout đầy đủ và đánh dấu phân biệt chính kinh/truyện/chú.

## Vị trí dự án hiện tại nên đối chiếu trước

- `v53/research/yi-complete`
- `v53/research/yi-lines`
- `v53/research/yi-second-witness`

Các đường dẫn trên là điểm tra cứu gợi ý; cần xác nhận đúng phạm vi nguồn trước khi tái dùng. Không chạy lại batch đã có payload. Chỉ nhận một quy tắc hoặc patch sau khi có byte nguồn đáng tin cậy, đối chiếu checkout hiện hành và chạy kiểm phù hợp.

## Bằng chứng phục hồi

- Bản bàn giao gốc: [`HANDOFF.md`](HANDOFF.md).
- Bản trích xuất chưa xác minh byte gốc: `evidence/extracted-unverified/`; không dùng `git apply` hoặc thực thi.
- Hash và ánh xạ nguồn nằm trong `../../IMPORT_VERIFICATION.json`.
