# Bảy mục nền và toàn bộ bảng đồ quẻ Tăng San

Ngày 28/10/2026. Đọc đủ khoảng của bảy mục đầu, đối 64 đồ quẻ gồm 384 dòng in và thêm bộ đọc nội bộ phân biệt hình ba hào với quẻ sáu hào. Giữ ba ô khác quy tắc trong sách dưới dạng chứng cứ nguồn. Web đang dùng giữ nguyên byte.

## Nguồn và phạm vi đọc

Tái dùng PDF `research/liuyao-foundations/NLC416-12jh005345-45344.pdf`, 11089308 byte, SHA-256 `caac111bc5c5b1c08fd27b3828e7cf6b5430503800f2427d8f2b28809022abaa`. Hồ sơ HTTP 200/TLS đã lưu được kiểm lại. Nhịp này không có HTTP, PDF, vị trí nguồn hay nhân chứng độc lập mới.

Đọc mở rộng 28 vị trí đã giữ 21–48; các ảnh cũ không đồng nghĩa đã đọc hết ở nhịp trước. Bảy khoảng: 八卦 21; 卦象圖 21–24; 八宮 24–45; 渾天甲子 45–46; 六親歌 46–47; 世應 47; 動變 47–48. Mục 八宮 gồm cả bảng 26–34, hội thoại 34–43 và ví dụ 44–45; không bỏ hội thoại khỏi độ phủ. Mục 用神 bắt đầu ngay trong 48, vẫn thuộc khoảng sau.

Ma trận có 137 đơn vị đọc lượt đầu theo khoảng, gồm 130 số thường và 7 mục phụ. Không còn mục nền chỉ đọc một phần theo khoảng. **0 đơn vị được tuyên bố áp dụng trọn**: chưa đối mọi chữ, lời tựa, điều kiện và ngoại lệ của cả sách; đây không phải tuyên bố toàn bộ 394 vị trí hoặc toàn kho đã khai thác hết. Bản đồ cũ 130/7 và các hồ sơ trước giữ nguyên để đối lịch sử.

## Bảng 64 đồ quẻ và ba ô sai khác

Nhập bảng trực tiếp từ ảnh, trước khi chạy đối chiếu: 64 danh tính/đồ hình, cung, Thế–Ứng và 384 dòng địa chi, hành, Lục thân. Những cột chạy qua trang được ghép bằng vị trí đồ hình, không lấy kết quả engine điền ô nguồn. 32 chữ `己` ở cột chi được giữ nguyên trong trường literal; chỉ trường làm việc quy về `巳` theo ngữ cảnh cột chi/lời bảng, không dùng cách đổi này cho can ngày `己` hoặc mọi chữ trong sách.

64 lượt HHC thật khớp danh tính hình, cung và Thế–Ứng khớp tham chiếu nội bộ. 384 nhãn chi làm việc khớp; có một ô hành và hai ô Lục thân khác:

| Vị trí | Chữ in giữ nguyên | Tọa độ theo quy tắc đã đọc |
|---|---|---|
| Quán 20, hào 3, PDF 26 | 卯土 | 卯木 |
| Trung Phu 61, hào 2, PDF 29 | 兄弟卯木 | 官鬼卯木 theo cung Cấn Thổ |
| Nhu 5, hào 1, PDF 33 | 父母子水 | 妻財子水 theo cung Khôn Thổ |

Ba crop từ render 360 dpi đã xem trực tiếp và khớp pixel. PDF 45–46 có bảng/quan hệ giúp đối quy tắc; riêng PDF 48 in lại quẻ Nhu với `妻財子水` ở hào đầu. Đây là đối chiếu trong **cùng ấn phẩm**, không phải nhân chứng văn bản độc lập. Không sửa PDF, không âm thầm thay nhãn literal, không đưa các ô khác ấy vào engine. `diagram-reference.mjs` trả riêng chữ in, tọa độ tính và danh sách khác biệt.

## Đồ ba hào, quẻ sáu hào và hào biến

Bốn hình PDF 47 là hình **ba hào**: Càn động đầu → Tốn; Càn động hai đầu → Khảm; Khôn động giữa → Khảm; Khôn động cả ba → Càn. Hình cuối không chỉ động hào thứ ba, cũng không tự là một quẻ Càn sáu hào. `motion-reference.mjs` yêu cầu chiều rộng 3 hoặc 6 tường minh. Với ba hào, danh tính quẻ sáu hào và quẻ ghép còn thiếu đều trả null.

Ví dụ sáu hào PDF 48 là Nhu → Tụng 5 → 6, có **bốn hào động 1, 3, 4, 6**. Hai lượt HHC thật xác nhận hình gốc/biến; sáu nhãn gốc và bốn nhãn biến đọc trên ảnh khớp. Hào 1 biến Dần Quan, hào 3/4 biến Ngọ Phụ, hào 6 biến Tuất Huynh. Nhãn biến vẫn theo cung Khôn Thổ của quẻ gốc; cung riêng của quẻ Tụng thuộc Ly chỉ là thông tin chẩn đối, không thay mốc Lục thân.

Ví dụ 48 đã có trong hồ sơ `liuyao-use-god` và bộ 14 kiểm trước. Hai lượt nhịp này kiểm bộ đọc 3/6 hào mới và đối nhãn mở rộng, không tính là một ví dụ nguồn độc lập mới. Ví dụ 44–45 Quải → Cấu đã có kiểm trước không chạy lại chỉ để cộng số. Hai ví dụ nhận dạng 23/24 cũng giữ kết quả trước; việc vòng/tréo được đọc theo âm dương gốc khác bước đảo hào để dựng quẻ biến.

## Tầng hội thoại và điều kiện còn thiếu

27 nhóm ngữ cảnh có xử trí riêng, không phải toàn bộ mệnh đề đã phân tích. Hội thoại trước giới thiệu cách đơn nhìn Thế; PDF 36 lại nói người đã hiểu Ngũ hành không thể lấy cách ấy làm pháp, PDF 43 gọi đây là cương lĩnh và dẫn về các chương sau. Các mệnh đề kết quả, sức khỏe, may rủi của cách giản lược không trở thành kết quả tự động cho người dùng.

Giữ riêng lực sinh/khắc theo tháng, ngày, hào động, hào biến; nguồn yêu cầu xét vượng suy khi ảnh hưởng trái nhau và phân biệt có tên sinh với có thực sinh. Không tự cộng số hoặc chọn Dụng khi chưa đủ tiền đề. Lời cho phép gieo lại thuộc hội thoại/câu hỏi đang xét; chưa tạo quy tắc đa quẻ chung cho mọi truyền bản. Nhãn thân thuộc, nhu cầu người hỏi, lịch và giới hạn chủ thể tiếp tục phải khai báo rõ.

## Kiểm chứng và gói

7 kiểm chức năng mới đạt. Có 66 lượt HHC thành công: 64 hình tĩnh từ bảng và 2 hình của ví dụ động kế thừa được chạy qua bộ đọc mới; không coi 384 dòng hoặc 4 hình ba hào là 384/4 trường hợp dự báo độc lập. Hai phép giải mã lại 26/230 dpi và 29/360 dpi khớp pixel; bốn crop gốc/QA khớp pixel. 28 byte-identity tiếp nhận và hai module chỉ thay import được kiểm riêng. Chạy lại kiểm sau tiếp nhận chỉ khi có thay đổi hoặc lỗi mới.

HTML gốc/V53/site giữ 707411 byte, SHA-256 `549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857`; ZIP web giữ nguyên. Snapshot trước phạm vi: `archives/v53-before-liuyao-foundation-span/`, manifest 3778, ZIP nguồn 2095344337 byte. Nguồn, corpus, bộ đọc và QA nằm ngoài site; không xuất bản mạng. ZIP nguồn/manifest hiện hành được đồng bộ và kiểm đọc lại bằng `scripts/verify-liuyao-foundation-release.py --no-write`.

Tiếp tục các điều kiện đầy đủ của Dụng/Nguyên/Kỵ/Cừu, vượng suy, hiệu lực, ưu tiên và phản ví dụ; các nhánh Tử vi, Bát tự, nhà ở, B03/Mai Hoa còn mở. Không gọi hoàn tất sách từ một bảng đối chiếu hoặc lượt đọc đầu.
