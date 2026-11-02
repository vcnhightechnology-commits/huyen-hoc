# HUYỀN HỌC — Khôi phục nội dung AI-01 đến AI-13

Ngày dựng bộ: 01/11/2026. Đây là **bộ khôi phục hiện có**, không phải toàn bộ cây mã nguồn GitHub.

## ĐỌC Ở ĐÂU?

- `00_TONG_QUAN/NOI_DUNG_13_NHANH_KHOI_PHUC.md`: toàn bộ nội dung diễn giải có căn cứ từ 13 nhánh, đọc một tệp.
- `01_HO_SO_NGHIEN_CUU_13_NHANH/`: 13 báo cáo nghiên cứu riêng từng AI.
- `02_TEP_GOC_DA_LAY_DUOC/`: **3 tệp byte gốc** đã xác nhận (AI-01).
- `03_BAN_VAN_BAN_TRICH_XUAT/`: **25 bản text** đã khôi phục từ Library, một số bị cắt ngắn hoặc mất newline; chỉ được dùng để đọc/đối chiếu, **KHÔNG** sử dụng như `.patch` nguyên gốc hoặc đem áp tự động.
- `00_TONG_QUAN/DANH_MUC_33_TEP_VA_TINH_TRANG_KHOI_PHUC.csv`: 33 tài sản gốc, nguồn, dung lượng và trạng thái từng tệp.
- `04_BAO_CAO_CU/`: tài liệu tổng hợp của lần trước.

## GIỚI HẠN QUAN TRỌNG

- **5 ZIP gốc** được nhận diện trong Thư viện nhưng công cụ chưa xuất được byte hoặc nội dung (AI-01/02/13).
- 9 nhánh AI-03–AI-09, AI-11–AI-12 không có byte gốc trong các tệp Library đã thấy; nội dung báo cáo của chúng được **tái dựng từ những cuộc nghiên cứu cũ**. Không gọi các hồ sơ này là bản gốc `README`, `THEORY_MATRIX` hay source code thực tế.
- Kết nối GitHub `dedaithien-sudo/huyen-hoc` trả HTTP 403 `Sorry. Your account was suspended`. Mọi commit/PR trong báo cáo là **mốc lịch sử**, không xác nhận live HEAD; bản vá 01/11 của AI-01, AI-02 và AI-10 chưa push.
- **AI-10 chưa đạt full suite**: mới 13/24 tệp test, 118/118 ca local đạt, còn thiếu 11 test; không được trộn số ca chạy với số test được yêu cầu.
- Mọi nghiên cứu cổ thư phân biệt nguyên bản, diễn giải, dị văn, mô hình thử nghiệm; không tự đưa kết luận vào engine hay merge main.

## Mức khôi phục

- Hồ sơ nội dung: **13/13 nhánh**.
- Danh mục tệp cũ đã nhận diện: **33/33 tệp**.
- Bản byte gốc khôi phục: **3/33**.
- Bản trích text bổ sung: **25/33**.
- Tệp không xuất được: **5/33**.
- Trạng thái nhánh GitHub hiện thời: **chưa kiểm được**.

Không viết đè các nguồn cũ, không tái sử dụng bản text như patch trực tiếp. Trước khi tích hợp cần Git checkout gốc, đối hash, chạy test toàn bộ và review.
