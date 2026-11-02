# HUYỀN HỌC 01–13 — BÁO CÁO TỔNG HỢP

**Ngày kiểm tra:** 01/11/2026. **Bản này là bộ chỉ mục + hồ sơ đã truy xuất, KHÔNG phải mã nguồn hoàn thiện của cả 13 nhánh.**

## 1. Phạm vi và tính xác thực

- Kho dự án đã biết: `https://github.com/dedaithien-sudo/huyen-hoc`.
- Kết nối GitHub trực tiếp bị lỗi HTTP 403 `Sorry. Your account was suspended`, không thể xác nhận HEAD, PR, CI hoặc tải toàn bộ nhánh vào phiên làm việc này.
- Thư viện cá nhân liệt kê 33 tệp thuộc AI-01/02/10/13. Có tên và dung lượng, không có file trên Library của 9 nhánh còn lại trong lần liệt kê này.
- Hệ thống chỉ cấp quyền materialize nội dung byte gốc của 3/33 tệp. 30 tệp khác vẫn ở Thư viện nhưng chưa thể đưa vào ZIP này; tuyệt đối không ghi nhầm là đã sao lưu.
- Đã tự chạy lại 17/17 unit test từ ZIP AI-01 có thể tải xuống; chưa chạy lại AI-02/10/13 vì không có đủ tệp raw.
- Các chỉ số còn lại lấy từ báo cáo nghiên cứu và lịch sử trao đổi trước, KHÔNG phải CI xác minh lại ngày hôm nay.

## 2. Kết quả từng nhánh

| Nhánh | Chuyên đề | Kết quả có bằng chứng lịch sử / cục bộ | Giới hạn hiện tại |
|---|---|---|---|
| AI-01 | Bát tự / Tứ trụ | 17/17 test bản vá truy xuất chạy lại; 80/80 test Không Vong cục bộ (theo báo cáo) | Có báo cáo và bản vá, bản Không Vong mới chưa push; chưa đối nguồn byte WYG |
| AI-02 | Tử Bình | 96/96 nhóm kiểm offline theo báo cáo | Patch tích lũy và ZIP trong Thư viện; chưa push phiên 01/11, còn đối ảnh nguyên bản |
| AI-03 | Tử Vi | 279 ca kiểm; 1.578 bất biến chưa xác định (theo lịch sử) | PR nháp lịch sử, chưa truy xuất được tệp nguồn trong phiên này |
| AI-04 | Lục Hào | 9/9 kiểm hồ sơ Q09 theo lịch sử | Chưa đối bản in đầy đủ; không có file byte gốc trong Thư viện liệt kê |
| AI-05 | Mai Hoa | 18 chủ đề/85 luận điểm theo lịch sử | Chỉ có ghi nhận kết quả và PR nháp trong lịch sử |
| AI-06 | Chu Dịch | 384 vị trí, 61 dị văn, 16 liên kết theo lịch sử | Đã có nghiên cứu/validator trên nhánh, chưa lấy được source hiện thời |
| AI-07 | Âm trạch | 234/234 kiểm trước đây; 14/14 unit mẫu | Bản ghi lịch sử, PR nháp; không có byte gốc tại thư viện đã liệt kê |
| AI-08 | Dương trạch | 7/7 kiểm Python theo lịch sử | Còn cần đối ảnh PDF bản in; nhánh chưa được xác minh lại |
| AI-09 | Trạch nhật | Quét 53.248 cấu hình và 35 ngày theo lịch sử | Hồ sơ nghiên cứu, chưa vận dụng engine hoặc xác minh lại GitHub |
| AI-10 | Tam Thức | 118/118 test máy; thiếu 11/24 file suite yêu cầu | Patch combined/incremental trên Thư viện chưa push; full suite CHƯA PASS |
| AI-11 | Hán Nôm | 225/225 kiểm theo lịch sử; 21 tập chỉ mục | PR nháp lịch sử; không có byte gốc trong thư viện liệt kê |
| AI-12 | Nhân tướng | 22/22 kiểm hồ sơ dữ liệu theo lịch sử | PR nháp, còn thiếu đối ảnh/hash và kiểm tích hợp |
| AI-13 | Lịch pháp | 36/36 mốc Jie 2024–2026 theo lịch sử; 2.412 mốc khảo sát | Có ZIP nghiên cứu chính sách lịch theo Thư viện, chưa kiểm checkout/CI nguồn đầy đủ |

## 3. Các bộ tệp đang lưu trong Thư viện

Chi tiết mọi tên tệp, dung lượng, đường dẫn gốc và trạng thái khôi phục có trong `DANH_MUC_33_TEP_THU_VIEN.csv`.

- AI-01: bản vá nguồn/công cụ nghiên cứu cũ trong `AI01_CONTINUATION_PATCH_2026-10-31.zip`, báo cáo và log đã truy xuất; Không Vong có ZIP/patch mới chỉ ở Thư viện, chưa có byte trong ZIP tổng hợp.
- AI-02: ZIP `AI02_CUMULATIVE_QA_M03_OFFLINE_BUNDLE_2026-11-01.zip` và bản vá tích lũy chỉ còn truy cập qua Thư viện, không nằm trong ZIP này.
- AI-10: bản vá `AI10_integrity_hardening_combined_2026-11-01.patch`, incremental và biên bản suite chỉ có trong Thư viện.
- AI-13: ZIP `AI13_authority_evidence_local_2026-11-01.zip`, module `calendar-authority-policy.mjs` chỉ có trong Thư viện.

## 4. Điều kiện nghiệm thu còn thiếu

1. Khôi phục quyền đọc GitHub, clone/fetch 13 nhánh và xác nhận commit, PR, file diff hiện hành.
2. Tải bản gốc của 30 tệp chưa được cấp xuất byte; giữ nguyên SHA-256 trước khi tổng hợp.
3. Bảo vệ `main` và engine sản phẩm; các bản vá nghiên cứu `research-only` không được coi là bản release.
4. Kiểm Git blob, chứng cứ ảnh gốc, kiểm thử đầy đủ, CI và review cho từng PR trước khi merge.
5. Đặc biệt AI-10 còn thiếu 11/24 tệp test; 118 test qua cục bộ KHÔNG đồng nghĩa full suite đạt.

## 5. Cách tìm nguồn

- Thư viện ChatGPT: xem các thư mục `huyền học 1`, `huyền học -2`, `huyền học 10`, `huyền học 13`.
- Đối chiếu file cụ thể qua bảng CSV, không dựa vào tên ZIP để suy ra đã đưa toàn bộ vào gói này.
- PR/nhánh trong bảng là mốc lịch sử cần xác minh lại, không phải trạng thái live GitHub.

## 6. Nội dung thực tế của ZIP bàn giao này

1. README_TONG_HOP.md (báo cáo).
2. TIEN_DO_13_NHANH.csv (ma trận tiến độ).
3. DANH_MUC_33_TEP_THU_VIEN.csv (đường dẫn tệp đã biết).
4. MAY_DOC_DUOC.json (chỉ mục máy đọc).
5. DU_LIEU_DA_LAY_DUOC (3 tệp byte gốc, không làm giả 30 tệp còn thiếu).
6. AI01_local_retest.log và SHA256SUMS.txt.
