# HUYỀN HỌC CÁC — TỔNG HỢP TÀI LIỆU NGHIÊN CỨU / AI-01

**Tính đến ngày:** 31/10/2026. Gói được sắp xếp lại theo các kết quả của cuộc trò chuyện.

## Đọc theo thứ tự

1. `00_BAT_DAU_O_DAY.md`: hướng dẫn gói này và các giới hạn.
2. `01_TONG_HOP_KET_QUA_AI01.md`: nội dung toàn bộ các đợt nghiên cứu AI-01 được ghi nhận ở cuộc trò chuyện, các luận điểm chính, việc tiếp tục và phân biệt loại chứng cứ.
3. `02_AI01_NGU_HANH_TINH_KY/`: **toàn bộ 11 tệp hiện có** của đợt nghiên cứu đối chiếu Ngũ Hành Tinh Kỷ ↔ Tam Mệnh Thông Hội, bao gồm bài học, sáu thẻ tri thức, khảo dị, sổ nguồn, hai ca Tứ trụ, 18 luận điểm, việc còn mở, trình kiểm và báo cáo trạng thái.
4. `03_AI01_NHAP_GITHUB/`: bản vá nguyên gốc có thể nhập về repository (khi quyền ghi được phục hồi). Không tự áp dụng lên source khác phiên bản.
5. `04_CHUNG_CU_WYG_DA_TAO/`: các gói chứng cứ WYG còn có sẵn trong môi trường — gồm atlas câu Chính Ấn, các hồ sơ folio/bản scan WYG quyển 7 và ảnh minh họa (dùng như chứng cứ kỹ thuật, **không phải bộ cổ thư hoàn chỉnh**).
6. `05_CHI_MUC_PR_GITHUB.md`: tài liệu các đợt trước đã có trên GitHub, gồm PR #16, #17, #18, kèm đường dẫn từng tài liệu.
7. `SHA256_MANIFEST.json`: danh sách hash SHA-256 các tệp thực sự trong gói (không gồm manifest để tránh vòng phụ thuộc).

## Phân biệt cái **có trong ZIP** với cái **chưa tải được**

**Đã nằm nguyên vẹn trong ZIP:** 11 tài liệu/bảng/script AI-01 mới, bản vá Git đã tạo, các chứng cứ WYG ZIP/ảnh đang có, phần tổng hợp và danh mục liên kết PR.

**Chưa thể sao chép nguyên tệp từ repo sang ZIP:** các tệp bài học và ma trận đã đẩy tại PR #16 và PR #18, cũng như toàn bộ tệp chia 13 luồng tại PR #17. Lý do: kết nối GitHub hiện trả HTTP 403 (`Sorry. Your account was suspended`) khi đọc/ghi. **Đây là bản tổng hợp đầy đủ nhất của các tệp có sẵn trong phiên**, không phải ảnh chụp nguyên byte toàn bộ repo hay release `materials-v53`. Các nội dung quan trọng từ PR trước được ghi trong `01_TONG_HOP_KET_QUA_AI01.md` và link để mở nguyên bản khi quyền repo được sửa.

## Trạng thái và an toàn

- **PR #16:** đã viết hai bài học/khảo cứu Chính Ấn từ WYG, vẫn là PR nháp khi kiểm lần gần nhất.
- **PR #17:** chia 13 AI / 40 danh mục / 16 module-source, CI pass; PR nháp.
- **PR #18:** nghiên cứu Lộc–Mệnh–Thân, hai Chính Ấn; CI pass; PR nháp.
- **Đợt Ngũ Hành Tinh Kỷ bổ sung:** tài liệu cục bộ đã được tạo và có bản vá; GitHub chưa nhận do 403.
- Bản chép số và PDF ảnh cổ thư có cấp bằng chứng khác nhau; đừng tuyên bố đã hiệu khảo PDF ảnh nếu mới đọc bản số.
- Không coi nội dung cổ thư là kết luận khoa học về vận mệnh/nhân phẩm/sức khỏe. Không tự merge, đè `main`, sửa engine hay gói phát hành.

## Trang liên quan

Repository: https://github.com/thanthiende1-alt/huyen-hoc-cac

PR #16: https://github.com/thanthiende1-alt/huyen-hoc-cac/pull/16

PR #17: https://github.com/thanthiende1-alt/huyen-hoc-cac/pull/17

PR #18: https://github.com/thanthiende1-alt/huyen-hoc-cac/pull/18
