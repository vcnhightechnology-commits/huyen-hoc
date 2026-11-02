# AI-10 — Tam Thức — Kỳ Môn Độn Giáp, Lục Nhâm, Thái Ất

**Nhánh được ghi nhận:** `codex/ai-10-tam-thuc`  
**PR được ghi nhận:** 11 (không xác minh trực tiếp tại thời điểm lập)  
**Mốc commit:** 3fba778df2db68cd0fdbb472a271b1322dcc66ae (mốc cuối ghi nhận trước lỗi 403)  
**Tình trạng phát hành:** nghiên cứu/kiểm thử; **không được suy là đã hợp nhất hoặc được engine chấp nhận**.

## 1. Nguồn và phạm vi

《遁甲演義》, 《六壬大全》, 《太乙金鏡式經》; tệp `SOURCE_ANCHORS.json`, ghi riêng sách, thiên và cách diễn giải.

## 2. Nội dung nghiên cứu đã khôi phục

- Chia ba trục riêng: **S01** Nhật gia Độn Giáp (bảng 60 ngày/20 nhóm, kiểm đầu giờ/cung), **S02** Lục Nhâm (9 phép tiền đề nhập thủ, phân biệt các cách đọc/nhân chứng), **S03** Thái Ất (chuỗi chia 360→60 và 360→72→24). Giữ những trường hợp nguồn chưa đủ dữ liệu ở trạng thái chưa xác định.
- Một vòng kiểm toán S02 từng liệt kê **144/192 trạng thái**, với **120 vị trí nhập nhằng** theo báo cáo; không lấy pass của validator để tuyên bố thuật số hoàn tất.
- Bộ kiểm nguồn còn có lỗ hổng: thu hẹp test manifest trong worktree có thể vẫn `--run-git-head` pass, phụ thuộc `new URL` động không bị phát hiện, manifest rỗng dẫn đến tự khám phá test ngoài vùng. Bản vá integrity ngày 01/11 sửa ba tình huống và kiểm lại 118/118 ca local.
- Dùng audit dependency closure không chạy mã của nguồn, ghim Git HEAD tại máy, từ chối URL động không kiểm được; SHA của Git HEAD tại máy **không đồng nghĩa xác thực remote**. Báo cáo 01/11 nêu 13 tệp có/24 bắt buộc, vì vậy chế độ strict vẫn trả lỗi là đúng.
- Nhiều patch, báo cáo, TAP và JSON trạng thái đã trích xuất được dạng text; **chưa push** patch mới lên GitHub do 403.

## 3. Kiểm thử được ghi nhận

118/118 ca cục bộ trong 13 tệp hiện có; manifest bắt buộc 24 tệp, thiếu 11; full suite CHƯA đạt. Trừ phần có log/tệp gốc trong bộ lưu, các số liệu là kết quả báo cáo lịch sử, không được chạy lại toàn bộ trong phiên này.

## 4. Tệp và mã đã tạo/được nhắc đến

`AI10_integrity_hardening_combined_2026-11-01.patch`, incremental patch, `AI10_dependency_hardening_2026-11-01.patch`, báo cáo `INTEGRITY_GATES`, TAP, manifest (bản văn bản trích xuất; riêng combined có thể không đầy đủ).

## 5. Điều chưa hoàn tất, giới hạn nguồn và hướng nối tiếp

Cần khôi phục đủ 24 test, chạy GitHub Actions và V53, đối nguồn S01/S02/S03 và rà người duyệt. PR #11 tiếp tục Draft.

---
