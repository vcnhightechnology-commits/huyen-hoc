# AI-02 — Tử Bình — Dụng Thần và phân tầng truyền bản

**Nhánh được ghi nhận:** `codex/ai-02-tu-binh`  
**PR được ghi nhận:** 1 (không xác minh trực tiếp tại thời điểm lập)  
**Mốc commit:** c7bfdc5 (mốc phát triển trước đó, không xác nhận HEAD hiện thời)  
**Tình trạng phát hành:** nghiên cứu/kiểm thử; **không được suy là đã hợp nhất hoặc được engine chấp nhận**.

## 1. Nguồn và phạm vi

《子平真詮》, 《神峰通考》, các nguồn Tử Bình về Dụng Thần/Quan–Quỷ/Thực Thần và những bản chép hiện đại; đối chiếu riêng nguyên văn – bình chú – bản dịch.

## 2. Nội dung nghiên cứu đã khôi phục

- Phân biệt định nghĩa/tiền đề **Dụng Thần** giữa các truyền thống; chưa gộp “Chân Thuyên” với “Thần Phong” thành một quy tắc chung. Nghiên cứu S06, S08–S12/C19 và các mối liên hệ C21, C22, C30, đặc biệt điều kiện Thực Thần. Hồ sơ Thực Thần có 90 đơn vị cha: 49 liên kết một phần, 41 chưa liên kết, 0 tuyên bố áp dụng hoàn toàn.
- Bảo toàn các cặp dị văn/biên tập `月神/用神`, `三丁食己/三丁倒食`, `衰右/衰中`, `立命/三命`, `原注云/原注去`; M03 tách lớp bình chú Nhậm Thị khỏi văn bản gốc và bản dịch, không lấy sách dịch làm bản in cổ độc lập. M05/M06 giữ các bất đồng `題/提`, `難通月氣/雖通月令`, chữ `或透甲` và dấu mốc revision nguồn số.
- Thực hiện cổng kiểm chứng nội dung trước khi Node import mã nghiên cứu: ghim 17 Git blob, kiểm 12 module/28 tham chiếu tệp literal; chặn thay đổi phụ thuộc và thêm kiểm thử đột biến. Bản vá mới tích lũy bao gồm khóa PREIMPORT và lớp dịch M03.
- Sáu nhóm suite sau áp mô phỏng cho kết quả 44 + 13 + 13 + 6 + 12 + 8 = **96**. Đây là thử nghiệm cục bộ, không chứng minh cổ thư đã được đối ảnh hoặc GitHub Actions đã chạy.

## 3. Kiểm thử được ghi nhận

Theo báo cáo 01/11: 96/96 nhóm kiểm Node.js trên nền cục bộ/mô phỏng. Trừ phần có log/tệp gốc trong bộ lưu, các số liệu là kết quả báo cáo lịch sử, không được chạy lại toàn bộ trong phiên này.

## 4. Tệp và mã đã tạo/được nhắc đến

`AI02_CUMULATIVE_QA_AND_M03_2026-11-01.patch` và README, bản vá PREIMPORT, manifest SHA-256 (đã trích văn bản); hai ZIP bundle gốc nằm trong Thư viện nhưng chưa xuất byte.

## 5. Điều chưa hoàn tất, giới hạn nguồn và hướng nối tiếp

Chưa đẩy phiên bản tích lũy 01/11 lên nhánh; cần đối ảnh `衰右/衰中`, xác minh cơ sở chứng cứ, chạy trên checkout đầy đủ và review PR #1. Không thay engine/main.

---
