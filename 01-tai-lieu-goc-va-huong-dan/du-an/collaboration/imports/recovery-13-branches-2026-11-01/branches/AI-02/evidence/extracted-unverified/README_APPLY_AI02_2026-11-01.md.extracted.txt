# Hướng dẫn áp dụng bản vá AI-02 (01/11/2026)

**Trạng thái:** bản vá đã kiểm thử cục bộ, **chưa được push GitHub** vì kết nối GitHub trả `403: Sorry. Your account was suspended`. Không có commit/PR mới được xác nhận trên GitHub trong lượt này.

## Nội dung

- `AI02_PREIMPORT_LOCK_PATCH_2026-11-01.patch`: bản vá một file hiện có và thêm bốn file trong thư mục nghiên cứu AI-02.
- `logs/`: nhật ký 44 + 13 + 13 + 6 nhóm kiểm Node.js thực chạy.
- `blob_sha_manifest.json`: SHA Git blob và SHA-256 của tệp bản vá cục bộ.

## Trước khi áp dụng

Mở **checkout của kho** `dedaithien-sudo/huyen-hoc` trên nhánh `codex/ai-02-tu-binh`. Đọc trạng thái mới nhất, đặc biệt nếu AI khác đã push sau khi patch được tạo. **Không force-push và không áp dụng đè lên file đang sửa dở.**

Kiểm tệp runner đang có đúng Git blob SHA trước vá:

```sh
git hash-object collaboration/parallel-research/submissions/AI-02/zi-ping-source-boundaries/run-ai02-evidence-gates.mjs
# Kỳ vọng: 6e7b87c3e3cd310b685b784e2c45a577905fc37f
```

Nếu SHA khác, hãy **đối chiếu và giải quyết xung đột thủ công**. Nếu đúng, tại **thư mục gốc repo**, chạy:

```sh
git apply --check AI02_PREIMPORT_LOCK_PATCH_2026-11-01.patch
git apply AI02_PREIMPORT_LOCK_PATCH_2026-11-01.patch
node collaboration/parallel-research/submissions/AI-02/zi-ping-source-boundaries/run-ai02-evidence-gates.mjs
node collaboration/parallel-research/submissions/AI-02/zi-ping-source-boundaries/test-gate-transcript-validation.mjs
node collaboration/parallel-research/submissions/AI-02/zi-ping-source-boundaries/test-evidence-runner-hardening.mjs
node collaboration/parallel-research/submissions/AI-02/zi-ping-source-boundaries/test-pre-import-lock.mjs
git diff --check
```

Kết quả đã quan sát trong phiên kiểm cục bộ: 44 + 13 + 13 + 6 = **76 nhóm PASS**, 17 đầu vào vẫn khóa SHA, không có nhóm tích hợp nào bị bỏ qua. Bốn tình huống thử chèn mã thực thi sớm đều bị chặn trước khi side effect được tạo.

## Sau khi quyền GitHub được khôi phục

1. Chạy lại kiểm trên checkout đầy đủ.
2. Review diff (chỉ thư mục `collaboration/parallel-research/submissions/AI-02/`).
3. Commit và push **không ép** lên nhánh AI-02; cập nhật nội dung PR #1. Không merge khi chưa review nguồn cổ.

**Giới hạn:** bộ kiểm không xác nhận tính đúng của sách in, ngày sinh thực, lịch pháp hoặc hiệu lực đoán mệnh; SHA không phải chữ ký ngoài repo và không ngăn chạy code nếu có race thay file sau khi kiểm.