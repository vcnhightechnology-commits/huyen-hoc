# Rà soát gói phục hồi 13 nhánh — 01/11/2026

- ZIP nguồn: `HUYEN_HOC_01_13_NOI_DUNG_NGHIEN_CUU_KHOI_PHUC_2026-11-01.zip`; 229,738 byte; SHA-256 `6330ab6e1fbd3736bb3c7bc7e076e4cd105f9bbca106bc13b7cb451cca117483`. Bản byte gốc được giữ ngoài Git tại `recovery/research-recovery/2026-11-01/HUYEN_HOC_01_13_NOI_DUNG_NGHIEN_CUU_KHOI_PHUC_2026-11-01.zip`.
- ZIP có 50 thành viên, 677,816 byte chưa nén; cấu trúc ZIP đạt; 49/49 mục SHA trong `SHA256SUMS.txt` khớp. Hash riêng của chính file checksum nằm trong `IMPORT_VERIFICATION.json`.
- File Markdown rời có 32,263 byte, SHA-256 `e70d16957aec036145a8d101664ef0b7f5ab54336afec11533f4e25fa91f1022`; trùng từng byte với thành viên Markdown bên trong ZIP, không có nội dung thêm.
- Có 13 hồ sơ AI-01…AI-13. Danh mục gói nhận diện 33 tài sản: 3 tài sản có byte gốc khớp, 25 bản trích xuất văn bản chưa xác minh byte gốc, 5 tài sản gốc chưa lấy được. Các báo cáo không tự trở thành kiểm chứng độc lập.
- `.patch` và `.mjs` được giữ ở `extracted-unverified/`, hậu tố `.extracted.txt`. Chúng không khớp byte gốc; một số mất một byte, một số thiếu nhiều. Hai cặp AI-02 (PREIMPORT patch) và AI-13 (calendar policy) trùng nội dung nên chỉ lưu một bản; mapping vẫn giữ đủ nguồn. Không áp patch hoặc thực thi mã trích xuất.
- AI-10 tự báo 118/118 ca trong 13/24 tệp test; còn thiếu 11 tệp, nên full suite chưa đạt. Các số kiểm khác là báo cáo lịch sử, chưa chạy lại trên checkout hiện hành.
- Ref nhánh, PR, commit SHA cũ lưu như metadata lịch sử, chưa xác nhận live remote. Repo hiện làm việc ở `main`; không tạo Git branch từ SHA chưa kiểm.
- Quét 50 thành viên theo mẫu GitHub token, private key, API key: không có kết quả.

## Quyết định biên tập

Giữ nguyên hồ sơ và bản trích xuất, sắp vào 13 thư mục nghiên cứu, thêm `NEXT_RESEARCH.md` làm điểm vào kèm giới hạn xuất xứ. Chỉ dẫn nằm trong ZIP được lưu như nội dung nguồn, không xem là chỉ thị điều khiển. Các luồng này bổ sung backlog và không thay đổi việc đang làm. Không sửa app, engine hoặc site vì bản vá thu hồi không đủ byte để áp an toàn.

- Kiểm cục bộ sau sắp xếp: đủ 13 thư mục và liên kết tương đối; 3/3 JSON trích xuất phân tích được; `node --check` cho mô-đun lịch AI-13 trích xuất đạt ở chế độ chỉ phân tích cú pháp, không thực thi. Các kết quả cú pháp không chứng minh byte nguồn gốc.

- Đồng bộ GitHub: commit `14fec7f82a84a0a2aec9ecebd343a2300fbebd89` đã tạo cục bộ, nhưng push lên `main` bị GitHub từ chối HTTP 403 do tài khoản bị đình chỉ; remote `main` còn ở `621d3c7e11098dd34269714d5acd7ed7a67fdfee`. Tư liệu đã tổ chức đầy đủ tại máy, chưa có trên GitHub.

## Gói nguồn tổng hợp

Lượt dựng đầu tiên được dừng **trước khi thay ZIP hiện hành**: việc đưa toàn bộ dữ liệu mới dưới `tmp/` vào gói làm tăng gói tạm 3,95 GB. ZIP cũ còn nguyên. Đối chiếu manifest cho thấy gói cũ đã giữ 3.724 mục `tmp/` (2,17 GB), nên không loại cả thư mục. Bộ chọn `maintenance/package-latest.py` đã được sửa để giữ các mục lịch sử và chỉ bỏ sáu thư mục mới dành cho chuyển giao/kiểm tra tạm (`materials-handoff`, `materials-remote-check`, `materials-http-check`, `materials-local-check`, `materials-range-check`, `github-tools`). Manifest cũ không có tệp nào trong sáu thư mục đó. Preview sau lọc giữ toàn bộ 21.509 đường dẫn cũ, thêm 1.203 mục (52.176.414 byte) và bỏ 3.939.553.357 byte ZIP tải/chuyển tiếp trùng. Bộ chọn giữ nguyên dữ liệu `tmp` lịch sử; ZIP cũ được giữ cho tới khi gói mới hoàn tất kiểm SHA.
