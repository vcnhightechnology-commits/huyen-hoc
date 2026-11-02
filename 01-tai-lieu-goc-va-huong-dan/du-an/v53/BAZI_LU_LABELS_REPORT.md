# Bát tự: đủ 50 cặp nhãn Lộc, bảng kho Lộc và bản đồ ngữ cảnh

Ngày 27/10/2026. Đã trích đủ 50 cặp can–trụ được gán nhãn trong đoạn Lộc của Tam Mệnh Thông Hội quyển ba, thêm 10 tọa độ kho Lộc. Chín kiểm đạt. Bộ tra riêng trả đúng nhãn nguồn và giữ các tiền đề chưa rõ; không sinh kết luận vận mệnh. Web hiện hành nguyên byte.

## Chứng cứ và phạm vi

Tái dùng CADAL06066039.djvu/10619960 byte/230 ảnh, SHA256`2334006e3a46b16bdbf0bf6a79512d8d0c4b87a2ce2e8e1ff503121d8f2cffdc`; lượt tải, mô tả và TLS ở `research/bazi-jianlu-context/volume3/`. Nguồn này đã được giữ và đọc trong phạm vi trước. **0HTTP,0container,0trang nguồn mới**; mở rộng sáu ảnh cũ 4–8 và13. Không sao chép lại ảnh/PDF, không gọi sáu lượt đọc mở rộng là sáu nguồn mới. Đã so sáu SHA PNG và pixel RGBA với log giải mã nguyên byte.

Bảng bắt đầu ở ảnh4, tờ1b; tiếp ảnh5–8 đến đầu tờ3b. Ghi chú trước rằng cả50hàng nằm ở5–8 được đính chính tại đây: hàng甲 bắt đầu4,甲寅 vắt4→5; câu đa凶 của丁戊午 vắt5→6;庚申長生祿大吉 vắt6→7;癸壬子 nằm8. Lưu folio/ảnh từng hàng. Nhận diện các hàng không dựa vào việc tất cả phải giống vòng quay của thư viện.

Bản số đã giữ tại commit ghim, SHA256`267fda36d206bfd153d9377441adb5f99f96c39a594a5f7ebdf3e4dd226e9b87`. Trích đoạn bảng giữ nguyên marker/literal. Nhãn có trường tìm kiếm chuẩn hóa凶/㓙/㐫、德/徳、值/値;己/巳 chỉ chuẩn theo vai trò can/chi, không thay toàn văn. Đây là đọc đối nhãn và câu mục tiêu, chưa phải bản chép ngoại giao mọi chữ ảnh. Cùng họWYG chưa thành nhân chứng độc lập.

## Những gì được áp dụng riêng

`SOURCE_ROWS.json` có10nhóm×5trụ, đủ50cặp và8câu chung. Nhãn và mệnh đề nguyên ý được giữ như lời nguồn, không là dự báo đã xác minh. Câu俱吉/俱凶 được gán nhóm biên tập tường minh; riêng câu cuối nhóm戊 có giới hạn phạm vi: ít nhất hai mục cuối乙巳/丁巳, chưa xác lập nó bao trùm mọi mục trước. Những mục không ghi mệnh đề riêng giữ chuỗi rỗng, không lấp kết luận từ hàng bên cạnh:丙辛巳、乙己卯、戊辛巳、己丙午.

Mỗi truy vấn buộc tên hệ, một can nguồn và trụ ứng viên hợp lệ; không nhận甲丑 hoặc thiếu trường. `null` là chưa biết; một trụ hợp lệ không có trong nhóm trảkhông-có-cặp-này-trong-bảng, không phải lời xấu. Can nguồn không tự gán năm/ngày sinh. Cùng癸巳 có hai tên/câu khác nhau ở丙 và戊; giữ cả hai theo can được người gọi khai báo.

Giữ nguyên khác biệt ngữ nghĩa: **甲土/丙水為財** ởảnh4 và**丁木/辛水** ởảnh7 chưa phải hệ hành can thông thường. Không sửa thành甲木/丙火/丁火/辛金 hoặc gọi財 ấy làThập thần hiện đại. `截路空亡` ởbảng chỉ là nhãn nguồn; không tự tính旬空 hiện đại để “sửa” nhãn. Lời chủ phú quý, nghèo, nghề, giới tính hoặc đời sống cá nhân giữ lịch sử, không chuyển thành kết quả người dùng.

Ảnh13/tờ6a nêu bốn nhóm khoLộc:甲乙→未、丙丁→戌、戊己壬癸→辰、庚辛→丑, đủ10tọa độ. `luStorage` yêu cầu tên hệ riêng; đây không tự thành mộ ngũ hành thường, tam hợp mộ hoặc phép chấm vận. Câu ví dụ甲乙亥多而得未 có chữ“nhiều” chưa định lượng; khớp nhánh kho chưa trảđã thỏa toàn câu hay tốt xấu.

Thân bản số luậnLộc có **2217Unicodecodepoint** sau bỏ khoảng trắng/¶/marker folio, được chia **28ngữ cảnh liên tục** và gán xửtrí toàn khoảng. Có2218UTF16unit vì𤣥 là mộtcodepoint/two code units; offset phải tính codepoint. Bộ kiểm ban đầu đã bắt chênh lệch này, được sửa trong kiểm hồ sơ, không đổi nguồn hay phần mềm người dùng. Entity`&KR0339;` vẫn nằm trong thân bản số; lượt đốiảnh trước đọc嗤 giữ riêng, không âm thầm sửa byte.

28ngữ cảnh gồm định nghĩa, bảng, các loại生成/名位/眞/進退/會合/食神/祿頭/旬中/天祿/干支合/互換/朝元/夾合/祿堂/建向近合, kho/hợp/củng, lời bàn ngựa và giới hạn. Có xửtrí hết một bản đồ văn bản không có nghĩa đã biên dịch đầy đủ điều kiện hoặc xác minh các sách được trích. Những tiền đề như兩傍, thai/thời vị, thần phụ, vượng suy, khí hóa và định nghĩa “nhiều” vẫn mở. Bảng50nhãn đã trích đủ không phải cả luậnLộc hoặc toàn tác phẩm đã áp hết.

## Kiểm chứng và bảo toàn

9kiểm đạt:600truy vấn riêng (10can×60trụ) có đúng50cặp trong bảng;120ngữ cảnh riêng khoLộc;null/sai trường/trụ bất khả thi/bảo toàn dữ liệu;8nhóm câu chung và28khoảng văn bản. Thực thi thật60lượt`LunarUtil.getJiaZiIndex` từlunar-typescript1.8.6 đã kiểm byte, xác nhận các ứng viên đều thuộc vòng60trụ. Không gọi tra chỉ số này là60lá số sinh, nguồn độc lập về ý nghĩaLộc hoặc chứng cứ ứng nghiệm. **0lời gọi lá số sinh mới** vì phạm vi tra nhãn không đổi ranh lịch/can ngày/phép vận;10tọa độtháng và14HHC/10lunar của phạm vi trước không chạy/cộng lại.

Snapshot trước giữ3262tệp/sourceZIP2055857311byte ở`archives/v53-before-bazi-lu-labels/`. RootHTML/V53/site707411byte giữ SHA`549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857`;ZIPweb344047byte nguyên;site chỉindex.html. UIKiếnLộc trước vẫn ở thư mục ứng viên nghiên cứu, chưaQA trìnhduyệt/in vì browser bị tắt; không vượt setting và không coi UI đã phát hành. Nguồn/QA ngoài site, không đổi số phiên bản hoặc xuất bản mạng. Gói mới được đốimanifest/ZIP sau đóng gói.

Tái kiểm: `node v53/scripts/test-bazi-lu-labels.mjs`; `python v53/scripts/verify-bazi-lu-labels-sources.py`; `python v53/scripts/verify-bazi-lu-labels-release.py --no-write`. Cácđiều kiện Bát tự, Tửvi, Nhàở, Dịch và40hồ sơ vẫn active/whole0.
