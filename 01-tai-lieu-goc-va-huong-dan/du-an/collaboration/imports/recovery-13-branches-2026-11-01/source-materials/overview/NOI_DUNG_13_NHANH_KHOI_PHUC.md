# Bộ khôi phục nội dung nghiên cứu 13 nhánh Huyền Học

Ngày lập: **01/11/2026** · Repository: `dedaithien-sudo/huyen-hoc`.

**Nguồn phục hồi:** (1) báo cáo/tệp cá nhân có thể truy xuất tại thời điểm lập; (2) nội dung ghi nhận trong các cuộc trò chuyện nghiên cứu 31/10–01/11/2026. Kết nối GitHub trả HTTP 403 `Sorry. Your account was suspended`, không thể cập nhật nguồn remote hoặc xác nhận PR/HEAD/CI hiện thời.

**QUAN TRỌNG:** Báo cáo từng nhánh trong thư mục này là **văn bản tái dựng** từ chứng cứ hiện còn, không phải các README/chương nghiên cứu gốc của kho GitHub. Bản trích văn bản tệp trong `03_BAN_VAN_BAN_TRICH_XUAT` không phải nguyên byte; các ZIP chưa truy xuất không nằm trong gói. Chỉ các tệp trong `02_TEP_GOC_DA_LAY_DUOC` là bản nguyên byte đã xác nhận.

---

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

# AI-03 — Tử Vi — Đại hạn, Tiểu hạn và Tứ Hóa

**Nhánh được ghi nhận:** `codex/ai-03-tu-vi`  
**PR được ghi nhận:** 2 (không xác minh trực tiếp tại thời điểm lập)  
**Mốc commit:** 712aa2ae9160c917c6a8021fa84b51389e75f0b0 (theo lịch sử)  
**Tình trạng phát hành:** nghiên cứu/kiểm thử; **không được suy là đã hợp nhất hoặc được engine chấp nhận**.

## 1. Nguồn và phạm vi

《紫微斗數全書》 (Tử Vi Toàn Thư), Shidian và các bảng Tứ Hóa theo nhiều dòng truyền bản.

## 2. Nội dung nghiên cứu đã khôi phục

- Khảo cứu quy trình khởi Đại hạn, Tiểu hạn, cung khởi, tuổi hạn và khác biệt phương pháp giữa các bản. Điểm đối chiếu chính là **Tiểu hạn nam thuận/nữ nghịch** trong một bản so với quy tắc **bốn nhóm chi/cung khởi** ở Shidian; hai hệ chưa được coi là tương đương.
- Lập ma trận **10 thiên can × 4 hóa** (Hóa Lộc, Hóa Quyền, Hóa Khoa, Hóa Kỵ), lưu các bất đồng thay vì xóa dị bản để ép khớp. Có nghiên cứu và QA đối với những tình huống đầu vào chưa đủ tiền đề.
- Đã báo cáo 279 ca kiểm và 1.578 vị trí bất định; những con số này là kiểm dữ liệu/ràng buộc, không phải bằng chứng dự đoán tử vi chính xác.
- Lần nghiên cứu trước ghi nhận 33 tệp và 6 commit riêng, PR #2 ở dạng nháp.

## 3. Kiểm thử được ghi nhận

Theo cuộc nghiên cứu trước: 279 ca kiểm; 1.578 bất biến/điểm không xác định được giữ lại. Trừ phần có log/tệp gốc trong bộ lưu, các số liệu là kết quả báo cáo lịch sử, không được chạy lại toàn bộ trong phiên này.

## 4. Tệp và mã đã tạo/được nhắc đến

Đã ghi nhận mã kiểm và các tệp ma trận/đối chiếu trên nhánh trong hội thoại; hiện không có bản sao nguyên byte thuộc nhánh này để đóng gói.

## 5. Điều chưa hoàn tất, giới hạn nguồn và hướng nối tiếp

Cần đối ảnh nguồn Tứ Hóa Canh, xác minh quy tắc tháng nhuận an Mệnh–Thân, Thân chủ Hỏa–Linh, miếu/vượng/hãm và khởi Đại hạn; chưa kiểm lại CI hoặc trình duyệt.

---

# AI-04 — Lục Hào — Nạp Giáp, Quái Thân và cách chọn Dụng Thần

**Nhánh được ghi nhận:** `Nhánh AI-04 (tên ref chính xác chưa xác minh lại)`  
**PR được ghi nhận:** 4 (không xác minh trực tiếp tại thời điểm lập)  
**Mốc commit:** fb3be4e (mốc lịch sử rút gọn)  
**Tình trạng phát hành:** nghiên cứu/kiểm thử; **không được suy là đã hợp nhất hoặc được engine chấp nhận**.

## 1. Nguồn và phạm vi

Các truyền bản Lục Hào/Nạp Giáp, hồ sơ nguồn B02/B03, quy tắc Quái Thân và Nguyệt Quái Thân.

## 2. Nội dung nghiên cứu đã khôi phục

- Phân loại Q01–Q09, giữ riêng các trường hợp hai kiểu **卦身** thay vì gộp thành một “phương pháp Quái Thân” duy nhất.
- Hồ sơ B02 ghi dị bản **Đoài→Giải** với `辛卯` so với `辛亥`, cần đối chứng ảnh nguồn; B03 xây giả thuyết Nguyệt Quái Thân có tiền đề và kiểm chéo 8.748 tổ hợp hình thức.
- Có các mô-đun JavaScript và kiểm trạng thái/biên dạng dữ liệu; kết quả đưa vào hồ sơ nghiên cứu, chưa biến thành quy tắc phán quẻ cho engine.
- Lịch sử ghi nhánh hơn main 23 commit và Draft PR #4; SHA cụ thể không kiểm được ở lượt này.

## 3. Kiểm thử được ghi nhận

Q09: 9/9 hoặc 10/10 bài kiểm dữ liệu ở các vòng khác nhau; quét 8.748 tổ hợp theo báo cáo. Trừ phần có log/tệp gốc trong bộ lưu, các số liệu là kết quả báo cáo lịch sử, không được chạy lại toàn bộ trong phiên này.

## 4. Tệp và mã đã tạo/được nhắc đến

Hồ sơ Q09/Q03, tệp kiểm, README/trạng thái nhánh đã từng báo cáo; chưa thể xuất nguyên byte về bộ khôi phục.

## 5. Điều chưa hoàn tất, giới hạn nguồn và hướng nối tiếp

Q05 (Không, Phá, Phi Phục, Dụng thần), hình thành bảng nguồn/điều kiện cho Nguyên–Kỵ–Cừu thần, đối ảnh cổ thư và kiểm toàn checkout.

---

# AI-05 — Mai Hoa Dịch Số — Lục thần, Thể–Dụng, ngoại ứng

**Nhánh được ghi nhận:** `codex/ai-05-mai-hoa`  
**PR được ghi nhận:** 6 (không xác minh trực tiếp tại thời điểm lập)  
**Mốc commit:** Không có SHA cuối được xác minh lại  
**Tình trạng phát hành:** nghiên cứu/kiểm thử; **không được suy là đã hợp nhất hoặc được engine chấp nhận**.

## 1. Nguồn và phạm vi

《梅花易數》, bản in/scan năm 1925 (12 trang được tham chiếu trong nghiên cứu); phân biệt các truyền bản trong lập quẻ và chiết tự.

## 2. Nội dung nghiên cứu đã khôi phục

- Phát hiện trường `season` có thể bị nhầm với **địa chi** nếu dữ liệu thiếu kiểu/phạm vi; bổ sung kiểm rõ mùa, tháng, ngày và quy ước ngũ hành.
- Tách **Lục thần theo thiên can ngày** với cách giải thích nét chữ/chiết tự; không suy một quy tắc từ tên giống nhau của hai học phái.
- Ma trận theo dõi **18 chủ đề, 85 mệnh đề**, mỗi mệnh đề cần nguồn/điều kiện/ngoại lệ/trạng thái. Đã kiểm các cặp mùa–hành (25) và chi–hành (60) theo định nghĩa dữ liệu được khai báo.
- Hội thoại ghi 11 tệp mới, 2 tệp cập nhật, 26 commit trên nhánh và PR #6 nháp; chưa nhập vào engine.

## 3. Kiểm thử được ghi nhận

Theo lịch sử: 18 chủ đề/85 mệnh đề; 12/12 nhóm kiểm, 25 mùa–ngũ hành và 60 chi–ngũ hành. Trừ phần có log/tệp gốc trong bộ lưu, các số liệu là kết quả báo cáo lịch sử, không được chạy lại toàn bộ trong phiên này.

## 4. Tệp và mã đã tạo/được nhắc đến

Ma trận `THEORY_MATRIX`, tài liệu nguồn, test script và báo cáo trong lịch sử; không có bản sao byte gốc hiện truy xuất được.

## 5. Điều chưa hoàn tất, giới hạn nguồn và hướng nối tiếp

Dị bản lập quẻ, điều kiện Thể/Dụng và Hậu thiên thời-phương, ngoại ứng, đoán chữ; không gắn suy luận khi chưa xác định bản và ngữ cảnh.

---

# AI-06 — Chu Dịch — Kinh văn, Thập Dực và khảo dị

**Nhánh được ghi nhận:** `codex/ai-06-chu-dich`  
**PR được ghi nhận:** PR nháp có ghi nhận, chưa xác định số (không xác minh trực tiếp tại thời điểm lập)  
**Mốc commit:** Không kiểm được SHA HEAD hiện thời  
**Tình trạng phát hành:** nghiên cứu/kiểm thử; **không được suy là đã hợp nhất hoặc được engine chấp nhận**.

## 1. Nguồn và phạm vi

《周易》/《易經》, Thập Dực, Tự Quái, Tạp Quái, Thuyết Quái và các phiên bản văn bản cổ số hóa.

## 2. Nội dung nghiên cứu đã khôi phục

- Thiết lập không gian **64 quẻ × 6 hào = 384 vị trí**, phân biệt thứ tự quẻ/hào với nguồn ghi chép và các lời chú.
- Ghi **61 dị văn** và **16 vị trí đối chiếu hai nguồn**. Có 15/16 trùng chữ; trường hợp **Đại Súc quẻ 26, hào 3** có bất đồng `曰/日`, cần tách câu chính văn khỏi bình chú, không xem số hóa là nguyên bản tối hậu.
- Mở rộng Thập Dực: **10 thiên/7 nhóm**, Tự Quái có 63 quan hệ quẻ kề nhau nhưng chỉ 61 lời nối được xác định; xem riêng ranh 30→31 và mẫu thiếu `以`. Tạp Quái có các khác biệt trong cùng nguồn/trang, không coi nhầm thành hai ấn bản.
- Hồ sơ đã báo cáo `ALL_61_VARIANTS.json`, `CASE_LEDGER.json`, `THEORY_MATRIX.md`, `SOURCE_REGISTER.md`, `OPEN_QUESTIONS.md`, `audit_yi06.py`.

## 3. Kiểm thử được ghi nhận

Theo lịch sử: 384 vị trí hào, 61 dị văn, 16 liên kết đối chiếu; 15/16 khớp chữ. Trừ phần có log/tệp gốc trong bộ lưu, các số liệu là kết quả báo cáo lịch sử, không được chạy lại toàn bộ trong phiên này.

## 4. Tệp và mã đã tạo/được nhắc đến

Tên tệp nghiên cứu và validator được ghi nhận trong hội thoại; chưa truy xuất được nguyên mã/JSON của nhánh AI-06.

## 5. Điều chưa hoàn tất, giới hạn nguồn và hướng nối tiếp

Cần đối lại chữ với ảnh in/đồ hình và nguồn độc lập, chạy validator trên checkout đầy đủ và đánh dấu phân biệt chính kinh/truyện/chú.

---

# AI-07 — Âm Trạch — Táng Thư, Nhân Tử Tu Tri, Địa Lý Đại Thành

**Nhánh được ghi nhận:** `codex/ai-07-am-trach`  
**PR được ghi nhận:** 5 (không xác minh trực tiếp tại thời điểm lập)  
**Mốc commit:** Không kiểm được SHA HEAD hiện thời  
**Tình trạng phát hành:** nghiên cứu/kiểm thử; **không được suy là đã hợp nhất hoặc được engine chấp nhận**.

## 1. Nguồn và phạm vi

《葬書》, 《人子須知》, 《地理大成》, các bảng nguồn/nhân chứng số.

## 2. Nội dung nghiên cứu đã khôi phục

- Tách **chính văn và chú giải** của Táng Thư, tránh gán lời người chú thành quy tắc chính thức của tác giả.
- Nhân Tử Tu Tri: báo cáo dị bản `而作詩歌`/`而不作诗歌` ở phàm lệ và khác biệt phân quyển **35/47**; không hợp nhất khi chưa rõ thư mục bản in.
- Địa Lý Đại Thành: ghi nhận **5 tập** và bất đồng nhan đề `理氣三訣/四訣` để đối chiếu tiếp.
- Đã lập đồ thị bản số (`WITNESS_GRAPH.json`), sổ mệnh đề (`CLAUSE_LEDGER.json`), 8 nguồn/bản số, 24 mệnh đề, 4 nhóm dị biệt cùng tài liệu đọc cho người Việt.
- Nhánh từng ghi nhận +21 commit và PR #5 nháp; kiểm 234/234 chỉ chứng minh nhất quán cấu trúc hồ sơ, không chứng minh một thuật phong thủy.

## 3. Kiểm thử được ghi nhận

Theo lịch sử: 234/234 kiểm dữ liệu và 14/14 bài unit mẫu. Trừ phần có log/tệp gốc trong bộ lưu, các số liệu là kết quả báo cáo lịch sử, không được chạy lại toàn bộ trong phiên này.

## 4. Tệp và mã đã tạo/được nhắc đến

`SOURCE_REGISTER.md`, `THEORY_MATRIX.json`, `VARIANT_AUDIT.md`, `KNOWLEDGE_ARTICLE_VI.md`, `OPEN_QUESTIONS.md`, `RESEARCH_STATE.json`, `WITNESS_GRAPH.json`, `CLAUSE_LEDGER.json`, script/test (tên ghi nhận, chưa xuất byte).

## 5. Điều chưa hoàn tất, giới hạn nguồn và hướng nối tiếp

Đối ảnh từng quyển và xác minh nhân chứng bản in độc lập; chưa đưa phép luận âm trạch vào bộ tính.

---

# AI-08 — Dương Trạch — 24 Sơn, Song Sơn và Phóng Thủy

**Nhánh được ghi nhận:** `codex/ai-08-duong-trach`  
**PR được ghi nhận:** 7 (không xác minh trực tiếp tại thời điểm lập)  
**Mốc commit:** Không kiểm được SHA HEAD hiện thời  
**Tình trạng phát hành:** nghiên cứu/kiểm thử; **không được suy là đã hợp nhất hoặc được engine chấp nhận**.

## 1. Nguồn và phạm vi

《陽宅十書》/Dương Trạch Thập Thư, chương `論放水第七`, scan PDF các trang 107, 109 và 110.

## 2. Nội dung nghiên cứu đã khôi phục

- So sánh bảng **24 Sơn** và các cặp **song sơn**; trong 12 cặp có 8 cặp được ghi nhận khác dòng bảng chính của nguồn đối chiếu — cần giữ đúng trường phái và phân loại.
- Bảng **phóng thủy** có dị biệt cụ thể ở hàng `未`; cần kiểm scan trang 110 trước khi xác nhận dữ liệu.
- Điều kiện bản văn `只放天干水為宜` (chỉ nên phóng nước Thiên Can) phải gắn với đúng phạm vi bảng, không áp dụng vô điều kiện.
- Có bộ `audit_crosswalk.py` kiểm bảng và 7/7 ca Python; 9 tệp nghiên cứu và PR #7 nháp theo lịch sử.

## 3. Kiểm thử được ghi nhận

Theo lịch sử: 7/7 Python unit tests đạt. Trừ phần có log/tệp gốc trong bộ lưu, các số liệu là kết quả báo cáo lịch sử, không được chạy lại toàn bộ trong phiên này.

## 4. Tệp và mã đã tạo/được nhắc đến

`audit_crosswalk.py`, dữ liệu crosswalk, tests, `README.md`, `SOURCE_REGISTER.md`, `THEORY_MATRIX.md`, `OPEN_QUESTIONS.md`, `RESEARCH_STATE.json` (chưa xuất nguyên byte).

## 5. Điều chưa hoàn tất, giới hạn nguồn và hướng nối tiếp

Đối ảnh trang 107 (âm dương), 109 (điều kiện), 110 (hàng 未); không gộp song sơn hoặc suy quy tắc duy nhất khi các truyền bản khác nhau.

---

# AI-09 — Trạch Nhật — Khâm Định Hiệp Kỷ Biện Phương Thư

**Nhánh được ghi nhận:** `codex/ai-09-trach-nhat`  
**PR được ghi nhận:** 8 (không xác minh trực tiếp tại thời điểm lập)  
**Mốc commit:** 9afb4c2cdd2 (mốc lịch sử rút gọn)  
**Tình trạng phát hành:** nghiên cứu/kiểm thử; **không được suy là đã hợp nhất hoặc được engine chấp nhận**.

## 1. Nguồn và phạm vi

《欽定協紀辨方書》 quyển 11, 35, 36; bản/scan CADAL 06056527; NDL/CiNii và ứng viên sách in 1911 上海錦章書局/SSID-13464303.

## 2. Nội dung nghiên cứu đã khôi phục

- Giữ cấu trúc **dẫn nguồn → lời phê bình → giới hạn áp dụng** tại các quyển 11/35/36, có 8 cặp dẫn/phê không nên rút gọn thành một quy tắc tốt/xấu.
- Khảo các ngày **Dương Công Kỵ**, **Thần tại**, Tứ Bất Tường, Tuần Sơn Nhị Thập Tứ Thần Sát; báo cáo đối chiếu có chênh **35/31** mục Thần tại theo cách cắt nguồn.
- Bảo lưu dị tự `夘` so với `卯` trong các biểu thức như `丁夘/己夘/辛夘/乙夘` thay vì tự chuẩn hóa để đạt test.
- Tạo tập quét 4.096 cấu hình và 53.248 phép kiểm; báo cáo chỉ **2 cấu hình** khớp đủ 13 mốc đang xét. Đó là kiểm khớp dữ liệu, không chứng minh đúng phong tục/trạch nhật ứng dụng.
- Theo lịch sử có 18 tệp nghiên cứu, PR #8 nháp.

## 3. Kiểm thử được ghi nhận

Theo lịch sử: kiểm 4.096 cấu hình × 13 mốc = 53.248 đối chiếu. Trừ phần có log/tệp gốc trong bộ lưu, các số liệu là kết quả báo cáo lịch sử, không được chạy lại toàn bộ trong phiên này.

## 4. Tệp và mã đã tạo/được nhắc đến

Bảng dẫn chứng/dị bản, hồ sơ Thần tại, scripts đánh giá, nguồn/register; không có tệp gốc AI-09 xuất được trong lần này.

## 5. Điều chưa hoàn tất, giới hạn nguồn và hướng nối tiếp

Đối ảnh CADAL và NDL/CiNii, xác định truyền bản, giới hạn theo Dụng sự; chưa nhập engine.

---

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

# AI-11 — Hán Nôm — Chỉ mục nguồn và khảo dị kinh truyện

**Nhánh được ghi nhận:** `codex/ai-11-han-nom`  
**PR được ghi nhận:** 10 (không xác minh trực tiếp tại thời điểm lập)  
**Mốc commit:** 9680aa12ac66b7d9a70c0746bef59275337185f9 (mốc lịch sử)  
**Tình trạng phát hành:** nghiên cứu/kiểm thử; **không được suy là đã hợp nhất hoặc được engine chấp nhận**.

## 1. Nguồn và phạm vi

Các nguồn Hán Nôm V01/V02 và bộ kinh/truyện Chu Dịch; hồ sơ khảo dị Đại Súc 26.3.

## 2. Nội dung nghiên cứu đã khôi phục

- Lập chỉ mục **21 tập**, theo dõi **11 tham chiếu** và ánh xạ nguồn/nguyên văn/chú giải; không trộn các lớp văn bản.
- Trường hợp **Đại Súc quẻ 26 hào 3** có khả năng đọc `曰`/`日`; công việc tập trung truy vết vị trí câu chữ theo nhân chứng, không quyết định đúng sai chỉ bằng một bản số hóa.
- Dữ liệu, mã/validator kiểm cấu trúc 225/225 theo lịch sử; báo cáo 18 tệp, 7 commit và PR #10 nháp.
- Phạm vi là thư mục/khảo dị, không sửa engine, không hợp thức hóa dự đoán bằng số ca test.

## 3. Kiểm thử được ghi nhận

Theo lịch sử: 225/225 kiểm cấu trúc. Trừ phần có log/tệp gốc trong bộ lưu, các số liệu là kết quả báo cáo lịch sử, không được chạy lại toàn bộ trong phiên này.

## 4. Tệp và mã đã tạo/được nhắc đến

Chỉ mục tập, bảng tham chiếu, dữ liệu khảo dị và scripts trong các commit lịch sử; không có byte gốc AI-11 tại Thư viện đã truy cập.

## 5. Điều chưa hoàn tất, giới hạn nguồn và hướng nối tiếp

Cần ảnh gốc/folio, SHA-256 ảnh/PDF, kiểm nhân chứng in độc lập và Node trên checkout hoàn chỉnh.

---

# AI-12 — Nhân Tướng — Thần Tướng Toàn Biên, Ma Y Tướng Pháp

**Nhánh được ghi nhận:** `codex/ai-12-nhan-tuong`  
**PR được ghi nhận:** 9 (không xác minh trực tiếp tại thời điểm lập)  
**Mốc commit:** Không xác minh SHA cuối hiện thời  
**Tình trạng phát hành:** nghiên cứu/kiểm thử; **không được suy là đã hợp nhất hoặc được engine chấp nhận**.

## 1. Nguồn và phạm vi

《神相全編》 (Thần Tướng Toàn Biên) và 《麻衣相法》 (Ma Y Tướng Pháp); các mẫu thư mục Harvard 1465–1620, Nagoya 1651, Kobe 1807.

## 2. Nội dung nghiên cứu đã khôi phục

- Tập trung hồ sơ N01–N03; dựng **niên biểu các chứng nhân in**, không mặc định nguồn có niên đại gần nhau là cùng một văn bản hoặc cùng truyền bản.
- Tách các mốc **1651, 1805, 1806, 1807** trong đối chiếu thư mục với chứng cứ văn bản thực tế; lưu mức độ xác thực riêng cho ngày và tác phẩm.
- Tạo EVIDENCE/niên biểu/mã kiểm, báo cáo **22/22** ca; hội thoại ghi 33 tệp khác main, 14 commit, PR #9 Draft.
- Nghiên cứu chỉ làm công tác thư mục/đọc văn bản, không lập thuật toán xác định đặc điểm hay phán đoán con người từ ảnh.

## 3. Kiểm thử được ghi nhận

Theo lịch sử: 22/22 kiểm hồ sơ dữ liệu. Trừ phần có log/tệp gốc trong bộ lưu, các số liệu là kết quả báo cáo lịch sử, không được chạy lại toàn bộ trong phiên này.

## 4. Tệp và mã đã tạo/được nhắc đến

Hồ sơ niên biểu, bảng nguồn EVIDENCE và script theo lịch sử; chưa thể truy xuất byte các tệp AI-12.

## 5. Điều chưa hoàn tất, giới hạn nguồn và hướng nối tiếp

Đối ảnh trang sách/PDF, SHA-256 và tính độc lập của truyền bản; thử Node CLI trên checkout đầy đủ.

---

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
