# AI-01 — Báo cáo tiếp nối đối chiếu cổ thư, kiểm chứng và chuẩn bị phát triển

**Thời điểm lập:** 31/10/2026  
**Tình trạng:** Bản nghiên cứu độc lập, có mã bảo vệ ở chế độ *research-only*; **chưa tích hợp repository hoặc engine**.  
**Trọng tâm:** `五行精紀` quyển 19, `論正印`; bổ trợ bằng quyển 25, `論三刑`.

## A. Phạm vi và kỷ luật chứng cứ

Báo cáo không giả định AI-01 đã được nghiệm thu về học thuật chỉ vì có thư mục bàn giao `collaboration/imports/ai01-2026-10-31`. Phiên này không mở được chính repository, release `materials-v53` hay ảnh scan gốc; chưa đọc được nội dung thực tế các hồ sơ trạng thái bên trong repo, vì vậy các ID `S06`, `S08–S12`, `C19` chỉ giữ ở mức **ID được nhắc trong trao đổi trước**, không tự ánh xạ sang nội dung cụ thể.

Phân loại bằng chứng:
- **Bản chuyển chép điện tử:** trang văn bản từ Thức Điển Cổ Tịch, Wikisource (đã đọc trong phiên này).
- **Dị văn:** khác biệt chữ, tên đề mục, trật tự hay phạm vi cú pháp giữa các chuyển chép.
- **Đối ảnh:** so trực tiếp ảnh trang in/bản chép, **chưa thực hiện**.
- **Quy tắc engine:** điều kiện đầu vào rõ, diễn giải đã được thông qua, có thử nghiệm hồi quy, **chưa thực hiện**.

Đối chiếu đa website không tương đương chứng minh nhiều truyền bản độc lập: cùng một truyền bản có thể được OCR/chuyển tự ở nhiều website. Không chọn đa số làm chân bản.

## B. Nguồn đã tra cứu

| ID | Nguồn | Vị trí tìm | Loại |
|---|---|---|---|
| SD_TRAD_19 | [識典古籍 bản phồn thể](https://www.shidianguji.com/zh/book/NGJ892411999013122114408/chapter/1lmyjad4zcsvn) | Quyển 19, 論正印, khoảng dòng web 57–246 | Chuyển chép |
| SD_SIMP_19 | [识典古籍 bản giản thể](https://www.shidianguji.com/book/NGJ8922621209348/chapter/1lnvyvqxghstk) | Quyển 19, 论正印, khoảng dòng web 55–200 | Chuyển chép |
| WKS_19 | [Wikisource](https://zh.wikisource.org/zh-hans/%E4%BA%94%E8%A1%8C%E7%B2%BE%E7%B4%80) | Quyển 19, 论正印, khoảng dòng web 5148–5223 | Chuyển chép |
| SD_TRAD_25 | [識典古籍 Quyển 25](https://www.shidianguji.com/book/NGJ892411999013122114408/chapter/1lmyjaikl6tkj) | 論三刑 | Chuyển chép |
| WKS_25 | [Wikisource](https://zh.wikisource.org/zh-hans/%E4%BA%94%E8%A1%8C%E7%B2%BE%E7%B4%80) | Quyển 25, 论三刑, khoảng dòng 6491–6543 | Chuyển chép |

Các vị trí “dòng web” là số dòng hiển thị khi truy xuất web, **không phải** số trang của bản gốc. SHA-256, số trang gốc, kho ảnh và hình thức kiểm tra chữ viết còn thiếu.

## C. Các kết quả nghiên cứu, theo mức độ ảnh hưởng đến engine

### AI01-R01 — Ngũ hành Chính Ấn (五行正印): năm tên ấn

Ở mục đầu `論正印`, ba nguồn liệt kê cùng năm loại: Ất Sửu–Kim ấn, Quý Mùi–Mộc ấn, Nhâm Thìn–Thủy ấn, Giáp Tuất–Hỏa ấn, Bính Thìn–Thổ ấn. Dạng chữ `甲戌` và `甲戍` cần lưu nguyên trong dữ liệu nguồn.

**Hệ quả:** Những tên trên liên quan cách diễn đạt ngũ hành, “bản gia ấn” (本家印), và điều kiện đặc thù của văn bản. Không đồng nhất với ten-god `正印` của hệ Bát tự hiện đại. Chưa có tiền đề để biến năm nhãn thành năm dự đoán chắc chắn.

### AI01-R02 — Điều kiện tầng bậc và điều kiện triệt tiêu

Các đoạn về “bản gia ấn” nêu thêm nhu cầu xét vượng, cùng loại tác khố, lộc mã, giáp quý, hoa cái; các đoạn suy giảm xét khắc phá, không vong và sát. Cùng có ấn không đủ để suy ra mức kết quả, đẳng cấp hay thành tựu của nhân vật. Đây là một hệ thống điều kiện và ngoại lệ cần được biểu diễn rõ ràng.

**Yêu cầu kỹ thuật:** Định danh từng điều kiện, nguồn thuật toán, trục năm/tháng/ngày/giờ/thai, giá trị `known/false/unknown`, thứ tự ưu tiên; thiếu điều kiện -> không luận chắc chắn.

### AI01-R03 — 財庫印: dị bản đảo hướng

| Nhân chứng văn bản | Dạng được chuyển chép | Ghi chú |
|---|---|---|
| SD_TRAD_19 | 火人→水印 | Chủ thể Hỏa, ấn Thủy |
| SD_SIMP_19 | 水人→火印 | Chủ thể Thủy, ấn Hỏa |
| WKS_19 | 水人→火印 | Chủ thể Thủy, ấn Hỏa |

Đây là khác biệt đảo vai trò, có thể khiến kết quả thuật toán đổi hẳn. **Quyết định tạm thời:** giữ cả hai, đánh dấu xung đột, không dùng số lượng website làm phiếu bầu.

### AI01-R04 — 自刑印, 刑印, 自刑殺: không đồng bộ tên mục

Ba nguồn có các cách đặt tiêu đề khác nhau đối với ví dụ `庚戌` gặp `乙丑`. Để bảo tồn lịch sử, sử dụng khóa nghiên cứu trung lập `AI01-R04`, kèm trường tiêu đề riêng theo nhân chứng. Không tự gộp các tiêu đề thành một thuật toán “tự hình”.

### AI01-R05 — 禍聚印: dạng chữ 巳/已 mang hậu quả ngữ nghĩa

Ở đoạn ví dụ Quý Tỵ gặp Nhâm Thìn, bản Wikisource có `癸巳`/`以巳為命`, các bản Thức Điển lại xuất hiện `癸已`/`以已爲命`. Về mặt chữ Hán, `巳` chỉ chi Tỵ, `已` là chữ khác. Văn bản liên kết mệnh với yếu tố hỏa trong một lập luận ngũ hành, khiến việc lẫn chữ có tác động đến cách hiểu.

**Chưa được phép:** tự đổi mọi `已` thành `巳` trên toàn corpus, áp dụng công thức lấy ngũ hành của nhật can để thay ngũ hành mệnh, tự suy ra “quá nhiều thủy” chỉ từ số lượng can chi.

### AI01-R06 — 破福成禍印: `鬼盛`/`癸盛`

Wikisource ghi `鬼盛`; các bản Thức Điển khảo sát có `癸盛`. Hai dạng khác nhau cả ký tự lẫn nghĩa có thể suy ra; cần ảnh gốc hoặc nhân chứng cổ văn đáng tin cậy để quyết định. Tạm không tạo phép kiểm “quỷ thịnh”/“quý thịnh” trong engine.

### AI01-R07 — 文章印: năm cặp dẫn chứng có thể lập bảng tra

Bản Wikisource liệt kê năm cặp (giữ dưới dạng *minh họa được trích từ chữ*, không phải công thức đủ điều kiện):

| Chủ thể ghi trong đoạn | Đối tượng được nêu | Tình trạng |
|---|---|---|
| 戊寅 | 癸未 | Tra cứu văn bản |
| 辛巳 | 甲戌 | Có dị tự 辛已 ở một bản chuyển chép |
| 庚申 | 乙丑 | Tra cứu văn bản |
| 癸亥 | 丙辰 | Tra cứu văn bản |
| 乙亥 | 壬辰 | Có đối chiếu trực tiếp ở hai bản |

Đoạn này có giải thích thêm về nạp âm và quan hệ can; vì vậy “có thấy cặp trong lá số” không có nghĩa đã đủ quy tắc cách cục. Vẫn chưa chắc “見” yêu cầu các trụ nào nếu không giải quyết văn cảnh và xác định chủ thể.

### AI01-R08 — 又文章印: ngữ đoạn rối, chưa cấu trúc hóa

Ba bản chuyển chép có sai khác đáng kể ở đoạn “lại Văn Chương Ấn”, gồm cặp đầu và ranh giới câu ở các cặp sau. Không nên lấy chuỗi OCR thiếu dấu phân đoạn để suy ra danh sách tất định. Đoạn kết có nhắc đến nhật/thời; không được tự lan điều kiện đó sang toàn bộ nhóm Văn Chương Ấn ở đoạn trước.

### AI01-R09 và R10 — Đối chiếu chéo với 論三刑 quyển 25

Quyển 25 chia hình thành nhiều loại: `丑刑戌` nằm trong nhóm “thị thế hình” (恃勢刑), còn nhóm “tự hình” (自刑) đề cập 辰、午、酉、亥 tự hình. Ở đoạn bình về những cặp cùng loại, văn bản nêu một ví dụ `乙丑` hình `庚戌`, nhưng đồng thời phân biệt cả nạp âm tương sinh/tương khắc và vai chủ–khách.

**Kết luận kỹ thuật:** ví dụ `庚戌` gặp `乙丑` trong chương ấn **không phải** ví dụ hai chi giống nhau tự hình. Thuật toán phải có các khái niệm riêng: (1) quan hệ tam hình có hướng, (2) quan hệ nạp âm giữa hai can chi, (3) danh mục ấn, (4) vai năm chủ/các trụ khách nếu văn cảnh yêu cầu, (5) trạng thái nhập/không nhập hình. Chỉ suy từ hai địa chi là thiếu.

### AI01-R11 — Ranh giới nghiệm thu và phát hành

Tất cả record hiện ở trạng thái `engine_admission: blocked`. `cross_text_consistent` có nghĩa được nhiều *chuyển chép* ủng hộ, **không** có nghĩa ảnh gốc đã đối xong hoặc quy tắc đã có thể đưa vào engine. Không có bất kỳ record nào trong gói này được tự chuyển sang `approved`.

## D. Thiết kế kỹ thuật thực hiện trong gói bàn giao

### D1. Mô hình dữ liệu

`data/catalog.json` giữ nguồn tham chiếu, 11 claim nguyên tử, trạng thái, dị bản, tiền đề nghiệm thu, 6 cặp ví dụ, và cổng phát hành. Source có `image_checked: false`, `file_sha256: null` cho đến khi được đối ảnh và kiểm tra checksum thực tế.

### D2. Bộ tra cứu đối chứng (`ai01.core.lookup_example`)

Trả về `textual_example_found` hoặc `example_not_in_catalog`; **không** trả `true/false` cách cục, độ tốt/xấu hay điểm số. Hàm chỉ so khớp chính xác chuỗi (NFC) và không tự chuyển `巳↔已`, `戌↔戍`, giản thể ↔ phồn thể. Cặp đảo chiều không coi là tương đương.

### D3. Bộ chặn phát hành (`ai01.core.validate_catalog`)

Nếu record bị gắn `engine_admission: approved`, `image_checked: true` mà chưa có ảnh, hoặc `release_gate.allow_engine_activation: true`, bộ kiểm tra báo lỗi và chặn tra cứu. Không được dùng hệ thống này làm bằng chứng đủ điều kiện xuất bản sau này: khi có ảnh gốc và review, cần thiết kế **giai đoạn nghiệm thu mới** thay vì đổi flag để né guard.

### D4. Kiểm thử hồi quy

Đã thiết kế các ca sau: dữ liệu hợp lệ; chặn tự nâng engine; chặn tự nhận đối ảnh; SHA-256 sai; nguồn tham chiếu vô hiệu; ID trùng; ví dụ không có record; thứ tự cặp đảo; phân biệt hình ấn với văn chương ấn; không đồng hóa 已/巳; không trả luận đoán khi gặp cặp dẫn chứng; không coi dữ liệu catalog rỗng là bằng chứng phủ định cổ thư.

## E. Ma trận công việc nghiên cứu tiếp theo

| Mã | Công việc | Chứng cứ phải có | Điều kiện hoàn thành |
|---|---|---|---|
| AI01-N01 | Đọc thực tế thư mục AI-01 trong repo | commit/branch, README, JSON, các review | Mapping hồ sơ cũ↔mới không sai |
| AI01-N02 | Khớp trục `S06, S08–S12, C19` | `EXHAUSTIVE_WORK_STATE.json`, followup pointer | Nêu được chính xác từng ID |
| AI01-N03 | Đối ảnh ba dị bản quan trọng | Trang sách của quyển 19 từ `materials-v53`, hash gốc | Tên mục, 財庫印, `鬼/癸` xác lập hoặc giữ dị văn |
| AI01-N04 | Đối ảnh `已/巳/戍/戌` | Trích đúng hàng/cột bản gốc | Nêu rõ truyền bản nào và vì sao |
| AI01-N05 | Thống kê đầy đủ điều kiện Chính Ấn | Khai triển tất cả đoạn mệnh đề và nguồn phụ | Có danh mục tiền đề + ngoại lệ |
| AI01-N06 | Đánh giá mối quan hệ chương 19 ↔ 25 | Chứng cứ về hình có hướng, nạp âm, vai chủ khách | Không đồng nhất tự hình với thị thế hình |
| AI01-N07 | Viết engine candidate đầy đủ nếu được duyệt | Đặc tả + test payload + review | Không còn điều kiện `unknown` trong ca nghiệm thu |
| AI01-N08 | Hồi quy và kiểm kho | Tập test hiện hữu, SHA-256, quy tắc lưu trữ | Không làm lệch bản site/phát hành |

## F. Ma trận trường hợp mẫu phục vụ kiểm thử khi có engine

- `乙亥`–`壬辰`: nhận diện được trích dẫn Văn Chương Ấn; **chưa** luận đoán kết quả.
- `壬辰`–`乙亥`: không tự đảo hướng lời dẫn.
- `庚戌`–`乙丑`: nhận diện ví dụ hình ấn; **không** gọi là chi giống nhau tự hình.
- `辛巳`–`甲戌`: nhận diện dạng đọc Wikisource; lưu độc lập dạng dị tự `辛已`.
- `癸巳`–`壬辰`: không tự đánh giá Họa Tụ Ấn vì thiếu điều kiện thủy, mộ và đối ảnh.
- `水命`–`火印`: không khẳng định Tài Khố Ấn do xung đột nguồn.
- `火命`–`水印`: cũng không khẳng định Tài Khố Ấn do xung đột nguồn.
- Chỉ có `壬辰` nhưng thiếu thông tin lộc mã/giáp quý/hoa cái: không luận cách cục cao.
- Năm mệnh khác nhật can: không được tráo vị trí âm thầm.
- Thiếu giờ sinh: trả `unknown` cho mọi điều kiện yêu cầu giờ.

## G. Ghi chú an toàn và quyền hạn

Gói này không chứa token, dữ liệu riêng tư, ảnh gốc, bản sao corpus lớn hoặc tệp nhị phân của repository. Chưa clone/push/commit/PR; việc tích hợp phải được thực hiện sau khi người dùng kết nối GitHub hoặc cung cấp checkout. Trong khi chưa xác minh `STORAGE_POLICY.md` thực tế, không được làm tác vụ dọn dẹp/xóa hoặc tạo release.

**Đề xuất PR khi được truy cập:** `codex/ai01-wxjj-witness-collation` với một thay đổi *documentation + research evidence + tests* trước; đề xuất PR engine riêng sau đối ảnh và review.
