# Kinh Dịch: làm rõ điều kiện và quan hệ trong lời đọc

Hoàn thành phạm vi ngày 26/10/2026, cùng V53. Snapshot trước phạm vi: `../archives/v53-before-yi-context-refinement/`. Nghiên cứu nằm ngoài site; không xuất bản.

## Kết quả cho người dùng

Chỉnh **sáu lời đọc** dùng chung trong hào đang động và phần đọc đủ sáu hào:

| Vị trí | Điều làm rõ |
|---|---|
| Đại Tráng34.4 | Hàng rào mở và xe có chỗ đỡ đi cùng nguyên tắc, chừng mực; không diễn thành cứ có sức thì tiến. |
| Tấn35.5 | Bớt tính công/lợi trước mắt để làm phần việc có ích, vẫn cần cách làm đúng; sửa cách nói thiếu rõ “thu mất”. |
| Khốn47.4 | Trợ giúp đến chậm và một kết nối bị cản; mở rộng cách đọc cũ chỉ nhấn “phương tiện chưa phù hợp”. Đổi tiêu đề thành “Gỡ điều níu bước khi giúp nhau”. |
| Đỉnh50.4 | Vạc làm đổ phần ăn chung gợi trách nhiệm và ảnh hưởng đến người khác; xem năng lực, chỗ hỗ trợ và cách giao việc. |
| Hoán59.1 | Làm rõ trợ giúp kịp lúc từ người phù hợp khi tình thế mới bắt đầu rời rạc. |
| Trung Phu61.4 | Giữ sự ngay thẳng khi cam kết riêng xung đột trách nhiệm chung; trao đổi ranh giới và tôn trọng người liên quan, thay lời khuyên quá rộng về buông liên kết cũ. |

Khảm29.4 được đọc thêm chú nhưng **giữ nguyên**: lời hiện có về giản dị/thành thực và kênh trao đổi phù hợp vẫn hợp ngữ cảnh. Không sửa một mục chỉ vì vừa đọc thêm nguồn.

Các lời mới là gợi mở biên tập hiện đại, không phải dịch sát chữ hoặc áp nguyên quan hệ quân/thần, trên/dưới, âm/dương vào phẩm chất cá nhân. Không xác định ai đang cản trở người dùng, không hứa một kết thúc tốt hay bảo đảm thành công. Phần chỉ dẫn chiêm nghiệm trên web không kèm corpus, dị văn, số trang hoặc tranh luận nghiên cứu.

**378/384 lời đọc thường còn lại** giữ nguyên; hai lời Dụng Càn/Khôn, dữ liệu Hán, phép gieo, quẻ biến, chọn hào và các công cụ khác giữ nguyên byte. Chỉ một tiêu đề trong sáu bản ghi đổi, năm tiêu đề còn lại giữ.

## Nguồn và phương pháp

Tái dùng [Commons NCL-00037 周易本義](https://commons.wikimedia.org/wiki/File:NCL-00037_%E5%91%A8%E6%98%93%E6%9C%AC%E7%BE%A9.pdf), **95.666.503 byte**,325 trang, SHA-256 `83472d8eb932ad44de18a552e54304947a01f994abbda5b534440db01026fa31`. Không tải PDF hoặc nguồn HTTP mới. Niên đại1710/乾隆15/1750 trong các danh mục vẫn còn mâu thuẫn, chưa đọc được đề ký năm; giới hạn định danh và phả hệ giữ như `research/yi-second-witness/PROVENANCE.md`. Không nâng mức chắc chắn chỉ vì đọc thêm trang nội dung.

Đọc trực tiếp **bảy đơn vị chú in đen trên tám trang ảnh**:143,163,166,207,217,241,247–248. Bảy ảnh đã lưu từ trước; trang248 được trích nguyên byte JPEG nhúng từ cùng PDF để đọc phần chú Trung Phu tiếp trang247. Không OCR, không chép/áp chú đỏ. Ảnh thực1713×1240, không lấy2675×1937 trong metadata làm độ phân giải đã đọc.

`verify-yi-commentary-images.py` giải trích lại cả tám trang bằng pypdf và so **đúng byte JPEG**, chiều thật/hash với bản lưu. Riêng248:304.182 byte, SHA-256 `ec548b8d515c6a83df7451112e720f6329c32414fc4d12d405f48cec67a89f61`. `IMAGE_AUDIT.json` liên kết từng trang; ảnh mới chỉ là trang của PDF cũ, không phải nhân chứng khác. Các bản chép16hào/năm đoạn chú trước đó và audit384hào của bản1874 giữ nguyên byte.

**Không cộng bảy vị trí này thành bảy hào mới đã hiệu khảo:** lời hào của chúng đã đối ở phạm vi trước. Công việc mới là đọc những đoạn chú chưa ghi nhận, tách ngữ cảnh nguồn khỏi ứng dụng hiện đại. Đỉnh50.4 từng đọc chú dạng chữ; lượt này đọc thêm câu về trách nhiệm/năng lực, không gọi lại chú dị thể là phát hiện mới.

Một số điểm nguồn có ảnh hưởng trực tiếp:

- Đại Tráng nói không đẩy tính cương đến cực điểm; Tấn còn điều kiện về đức/cách làm sau lời bỏ tính công/lợi. Không bỏ các vế điều kiện để tạo lời hứa thuận lợi.
- Khốn giải cản trở giữa các vị trí hào và trợ giúp chưa đến được. Chính người chú ghi **未詳/疑** khi bàn một phần hình tượng kim xa; giữ sự chưa rõ, không biến thành chẩn đoán xe/phương tiện thực.
- Đỉnh nói trách nhiệm nặng và không đảm đương; hình tượng nguồn không phải bằng chứng cho năng lực, giới tính hoặc hình phạt của người dùng. Chữ bản văn/chú dị thể cũ giữ riêng.
- Hoán bàn thời điểm ban đầu và nương trợ lực. Trung Phu bàn cặp hào và lòng tin với vị trí trên; không tự biến “絕類” thành mệnh lệnh cắt đứt một quan hệ đời thực.
- Khảm còn cách ngắt câu nghi lễ và hình tượng cửa lấy sáng; ứng dụng chọn cách nói/kênh tiếp nhận là biên tập, không phải quyền bỏ qua ranh giới người khác.

Từng đoạn ngắn, lớp văn bản, trang, điều chưa chắc và quyết định biên tập ở `research/yi-commentary-context/MANUAL_READINGS.json`. Bản trước/sau của sáu lời ở `CONSUMER_CHANGES.json`. Một người đọc bằng mắt, có rà lại ảnh tại các điểm nêu trên; không gọi là hai độc giả độc lập hoặc hiệu khảo trọn sách.

## Kiểm chứng

**41/41 kiểm chính đạt:**15 nguồn/runtime và26 trình duyệt. So byte xác nhận đúng sáu bản ghi thay đổi; engine/app/corpus Hán/Càn–Khôn và mọi mô-đun không liên quan nguyên byte so với snapshot ngay trước. Chạy đúng sáu mô-đun Yi nhúng trong HTML, không lấy một bản mã khác để suy kết quả.

**24 ca engine thật có mục tiêu**: sáu quẻ × bốn tập hào (không động, vị trí mới đọc, một vị trí khác, cả sáu). Giữ đúng quẻ/hào được chọn và cùng lời trong phần chọn/đủ sáu hào. 64 cấu hình tĩnh chỉ dùng tìm mẫu quẻ; không gọi chúng là64 ca đối chứng độc lập. Không lặp4096 phương án đã đạt ở lượt trước khi phép gieo/chọn hào không đổi. Đối byte và các ca có mục tiêu phù hợp với phạm vi chỉ đổi nội dung.

Trình duyệt kiểm cả sáu lời, gợi ý thực hành, sáu tệp TXT, nội dung in, thu gọn được khôi phục, lưu/mở đầu vào Trung Phu, đổi đầu vào xóa kết quả cũ.320/390/768/1440px không tràn; đã xem ảnh điện thoại Khốn/Trung Phu. Không lỗiJavaScript, khôngHTTP từ HTML độc lập, không lộ nguồn/nghiên cứu.

Không tạo PDF mới vì không đổi bố cục hoặc CSS; đã kiểm chế độ print thật cho từng lời và ẩn form. Không gọi kiểm chế độ in là đã xem PDF xuất. Lượt này không chạy lại iztro, lunar-typescript hoặc bộ hồi quy nhà ở vừa đạt vì dữ liệu/công cụ ấy nguyên byte. Các kết quả cũ giữ nguyên theo phạm vi của chúng.

## Đồng bộ và bước tiếp

Chỉ `yi-complete-data.js` thay trong mã sản phẩm; build HTML độc lập và đồng bộ root/site/hai ZIP cùng V53 sau kiểm gói. HTML678.173 byte; SHA theo manifest và `qa/yi-commentary-context/RELEASE_RESULTS.json`. Gói web chỉ HTML/hướng dẫn; ảnh, đối chiếu và QA ở gói nguồn riêng. Snapshot giữ bản cửa nội bộ đã hoàn tất. Không xuất bản.

Cần tiếp tục xác minh định danh/đề ký của nhân chứng, các đoạn chú còn tác động nghĩa và vấn đề nhà khắc của bản1874. Không tải lại cùngPDF, lặp các đoạn đã đọc hoặc gọi bảy đơn vị chú là học hết Kinh Dịch. Toàn bộ bốn hướng nghiên cứu vẫn **active-not-complete**.
