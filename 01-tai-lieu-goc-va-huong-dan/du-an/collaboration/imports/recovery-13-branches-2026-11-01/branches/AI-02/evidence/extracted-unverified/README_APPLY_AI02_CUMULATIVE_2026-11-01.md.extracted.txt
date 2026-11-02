# Cập nhật AI-02 ngoại tuyến — bản vá tích lũy ngày 01/11/2026

**Trạng thái:** đã hoàn thiện và thử nghiệm cục bộ. **Chưa đẩy lên GitHub**: kết nối của tài khoản GitHub báo lỗi 403 `Sorry. Your account was suspended` ngay từ API đọc nhánh/PR. Không được hiểu bản ZIP/patch này là một commit mới hoặc PR đã cập nhật.

## Có gì mới?

Bản vá **tích lũy** bao gồm cả bản sửa từ lượt trước (ngăn mô-đun dự án chạy trước khi cổng SHA kiểm tệp) và phần phát triển hiện tại:

- `run-ai02-evidence-gates.mjs` giữ kiểm **17 Git blob** trước khi import mã nghiên cứu; bổ sung rà **12 mô-đun / 28 tham chiếu tệp literal** để phát hiện phụ thuộc `.mjs`, `.json`, `.js` mới không có trong khóa dù SHA của test và manifest đã được cập nhật.
- `test-pre-import-lock.mjs`: kiểm lỗi import chạy trước khóa SHA (6 nhóm).
- `test-gate-dependency-closure.mjs`: test **tái ghim SHA có chủ ý** để thử bỏ sót phụ thuộc, 12 nhóm, 8 trường hợp từ chối.
- `M03_TRANSLATION_LAYER_ADDENDUM_2026-11-01.json`, `audit-m03-translation-layer.mjs`, `test-m03-translation-layer.mjs`: tách chép số Hán văn khỏi lời Nhậm thị và bản dịch hiện đại, 8 nhóm và 31 sửa sai bị bác.
- Tài liệu ranh giới học thuật và báo cáo kết quả nằm ở thư mục `collaboration/parallel-research/submissions/AI-02/zi-ping-source-boundaries/`.

**Lưu ý:** Bản vá này **đã chứa bản vá PREIMPORT của lần trước**. Áp dụng **một lần duy nhất** lên runner gốc đúng Git blob `6e7b87c3e3cd310b685b784e2c45a577905fc37f`. Nếu bạn đã áp bản vá PREIMPORT lần trước, **không áp bản tích lũy này trực tiếp**; cần cherry-pick/tách riêng diff mới hoặc đối chiếu ba phía.

## Áp dụng an toàn trên checkout thực

1. Khôi phục quyền GitHub, lấy đầu nhánh `codex/ai-02-tu-binh` mới nhất. Không force-push. Kiểm `git status --porcelain` và bảo vệ mọi thay đổi chưa commit.
2. Tại gốc repo, kiểm SHA runner:

```sh
git hash-object collaboration/parallel-research/submissions/AI-02/zi-ping-source-boundaries/run-ai02-evidence-gates.mjs
# Runner cũ trên nhánh cần trả: 6e7b87c3e3cd310b685b784e2c45a577905fc37f
```

3. Nếu SHA phù hợp và không có xung đột tên tệp, dùng bản vá tích lũy mới:

```sh
git apply --check AI02_CUMULATIVE_QA_AND_M03_2026-11-01.patch
git apply AI02_CUMULATIVE_QA_AND_M03_2026-11-01.patch
cd collaboration/parallel-research/submissions/AI-02/zi-ping-source-boundaries
node run-ai02-evidence-gates.mjs
node test-gate-transcript-validation.mjs
node test-evidence-runner-hardening.mjs
node test-pre-import-lock.mjs
node test-gate-dependency-closure.mjs
node test-m03-translation-layer.mjs
```

4. Xác nhận **96 nhóm PASS** theo biên bản, 17 tệp checkpoint còn nguyên SHA, không có file ngoài AI-02, rồi quay lại gốc repo và chạy `git diff --check`. Review code; commit và push **không ép**, cập nhật PR #1 khi GitHub cho phép.

## Giới hạn

- Đây là kiểm thử Node.js **cục bộ**, không phải GitHub Actions hay CI toàn ứng dụng.
- Chỉ kiểm bao phủ **tham chiếu tệp dạng literal thông thường**; không chứng minh an toàn trước mọi JS computed expression, eval, race TOCTOU hay chỉnh sửa đồng thời cả runner và SHA.
- M03 chưa đối ảnh chữ `衰右/衰中` từ bản in có trang/folio và SHA-256 được ghi lại. Bản dịch hiện đại không được coi là một nhân chứng in.
- Không sửa `main`, engine, bản phát hành, ZIP hiện có của dự án hoặc `COVERAGE.json`.

## Tệp trong gói

- `AI02_CUMULATIVE_QA_AND_M03_2026-11-01.patch`: bản vá tích lũy chính.
- `reports/`: báo cáo nghiên cứu mới và trước đó.
- `logs/`: log Node.js của sáu suite và kết quả chạy sau khi áp trên nền mô phỏng.
- `snapshots/`: các tệp có thay đổi để đối chiếu thủ công nếu nhánh GitHub đã khác.
- `AI02_CUMULATIVE_FILE_HASHES_2026-11-01.json`: SHA-256 các tệp phân phối.