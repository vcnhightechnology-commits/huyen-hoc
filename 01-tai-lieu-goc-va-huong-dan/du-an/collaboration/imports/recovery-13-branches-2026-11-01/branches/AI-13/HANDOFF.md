# AI-13 — Lịch Pháp — Tiết Khí, Can Chi và quy ước lịch Việt Nam

**Nhánh được ghi nhận:** `codex/ai-13-lich-phap`  
**PR được ghi nhận:** 12 (không xác minh trực tiếp tại thời điểm lập)  
**Mốc commit:** a6c925f44fd7 (mốc trước, chưa kiểm HEAD)  
**Tình trạng phát hành:** nghiên cứu/kiểm thử; **không được suy là đã hợp nhất hoặc được engine chấp nhận**.

## 1. Nguồn và phạm vi

Bảng tiết khí HKO 2026, các văn bản về quy ước lịch Việt Nam như QĐ 121-CP (08/08/1967) và thông tư 01-VLDC (19/08/1967); tư liệu lịch sử Bắc/Nam 1968–1975.

## 2. Nội dung nghiên cứu đã khôi phục

- Thiết lập **calendar-boundaries.mjs**, kiểm UTC/múi giờ, ranh tiết và Can Chi. Các vòng báo 5.427 phép kiểm UTC–múi giờ, 12/12 mốc Jie 2026 khớp nguồn HKO đến phút; kiểm 48/48 biên và 5/5 nhãn ngày. Không hiểu các con số như chứng minh toàn bộ lịch pháp đã đúng.
- Phát hiện cần tách **nơi sinh**, **cơ quan/cộng đồng phát hành lịch**, **quy ước nhãn âm lịch**, **múi giờ dân sự**. Ví dụ năm 1974 với mốc 16:30 UTC cho nhãn ngày khác khi dùng offset +7/+8 hoặc quy tắc đổi ngày 23:00; đây là kiểm độ nhạy, không xác nhận quy tắc cho mọi vùng.
- Module `calendar-authority-policy.mjs` trả hai ứng viên +7/+8 khi chưa xác minh chuyển đổi nguồn lịch Nam 1975; cờ `autoChooseReleasedChart=false`, giữ trạng thái bất định dù hai nhãn đôi lúc trùng nhau. Phân biệt GMT+7 chính thức miền Bắc từ 01/01/1968 với giờ dân sự/nguồn lịch miền Nam.
- Một vòng ghi 15 tệp, 7 commit, PR #12 Draft; ZIP `AI13_authority_evidence_local_2026-11-01.zip` nằm trong Thư viện nhưng byte ZIP chưa trích xuất, chỉ hai bản văn module thu hồi được.

## 3. Kiểm thử được ghi nhận

Theo lịch sử: 12/12 tiết Jie HKO 2026 đến phút; 48/48 kiểm ranh; 5/5 nhãn Can Chi; các vòng riêng báo 36/36 mốc và 2.412 mốc khảo sát. Trừ phần có log/tệp gốc trong bộ lưu, các số liệu là kết quả báo cáo lịch sử, không được chạy lại toàn bộ trong phiên này.

## 4. Tệp và mã đã tạo/được nhắc đến

`calendar-authority-policy.mjs` và bản `(1)` có văn bản trích xuất; hồ sơ `SOURCE_REGISTER.md`, `THEORY_MATRIX.md`, `OPEN_QUESTIONS.md`, `RESEARCH_STATE.json`, các test trong lịch sử (chưa lấy byte).

## 5. Điều chưa hoàn tất, giới hạn nguồn và hướng nối tiếp

Cần chứng thực lịch hành chính gốc 1975 miền Nam, đối ảnh/PDF HKO và SHA, chạy đầy đủ CI và hồi quy chuyển ngày; chưa tự chọn lá số khi nguồn lịch mơ hồ.

---
