# AI-01 — Bát Tự — Tứ Trụ, Chính Ấn và Không Vong

**Nhánh được ghi nhận:** `ai-01`  
**PR được ghi nhận:** 13 (không xác minh trực tiếp tại thời điểm lập)  
**Mốc commit:** c5a630583d96f4a55a56924bd141b193e600a694 (mốc lịch sử, không phải HEAD đã xác minh)  
**Tình trạng phát hành:** nghiên cứu/kiểm thử; **không được suy là đã hợp nhất hoặc được engine chấp nhận**.

## 1. Nguồn và phạm vi

《五行精紀》 quyển XIX (論正印), XXV (論三刑); 《三命通會》 WYG III (論空亡), WYG II (論遁月時); bản số Shidian, Wikisource dùng làm chỉ mục chứ không coi là nhân chứng cổ độc lập.

## 2. Nội dung nghiên cứu đã khôi phục

- Xây dựng hồ sơ đối chiếu các mục S06, S08–S12, C19 về Chính Ấn, Phúc Tụ, Phá Phúc, Văn Chương và Lâm Không Ấn. Giữ riêng các dị văn `五位俱`/`或四位`, `月日時胎`/`月時胎`, `無交涉`/`無沙`, `庚子得乙丑`/`庚子得丑`; không chọn bừa bản chữ duy nhất.
- Ở ví dụ bốn trụ `甲午 癸酉 丙子 壬辰`, kiểm 旬空 theo hai chi: năm→giờ, ngày→tháng, giờ→năm; năm–giờ tương hỗ. Cùng ví dụ có `辰酉` Lục hợp và `子午` Lục xung. Các phương án chọn một chi Không Vong làm thay đổi quan hệ nên không được đồng nhất mô hình toán với kết luận của cổ thư.
- Duyệt đủ **518.400** tổ hợp hình thức năm/tháng/ngày/giờ × ba phương pháp. Theo báo cáo: điều kiện bốn dấu hiệu xuất hiện lần lượt **20 / 0 / 2** tổ hợp; không dùng các con số này làm tỷ lệ sinh thực tế hay xác suất ứng nghiệm.
- Phân biệt `--model-only` (kiểm logic) với kiểm ảnh và SHA byte nguồn WYG thực tế (thiếu nguồn phải dừng). Hướng xác lập quan hệ `臨空印` vẫn ở trạng thái `engine=blocked`.

## 3. Kiểm thử được ghi nhận

17/17 test trong ZIP gốc đã chạy lại ở lần tổng hợp trước; báo cáo riêng ghi 80/80 test Không Vong ngoại tuyến. Trừ phần có log/tệp gốc trong bộ lưu, các số liệu là kết quả báo cáo lịch sử, không được chạy lại toàn bộ trong phiên này.

## 4. Tệp và mã đã tạo/được nhắc đến

`AI01_CONTINUATION_PATCH_2026-10-31.zip` (byte gốc), `AI01_CONTINUATION_REPORT.md` (byte gốc), `AI01_TEST_RESULTS.txt` (byte gốc), các patch Không Vong, WYG3 cross-axis/joint fingerprint và handoff (chỉ bản trích văn bản khi truy xuất được).

## 5. Điều chưa hoàn tất, giới hạn nguồn và hướng nối tiếp

Chưa kiểm lại ảnh gốc WYG II/III, NLC các tập, không được tự chốt chữ dị bản hoặc đưa logic phán đoán vào engine. Patch Không Vong ngày 01/11 chưa push do GitHub 403; PR #13 chỉ là trạng thái lịch sử.

---
