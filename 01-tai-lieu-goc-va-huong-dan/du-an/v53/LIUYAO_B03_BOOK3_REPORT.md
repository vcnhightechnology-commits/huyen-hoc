# B03: khép lượt đọc sách đóng thứ ba và tọa độ ra tuần

Ngày 27/10/2026. Hồ sơ nghiên cứu nội bộ; không thêm nguồn hoặc bảng kiểm vào site người dùng.

## Phạm vi và nhận dạng

Tái sử dụng PDF sách đóng thứ ba đã giữ byte ở phạm vi trước: **56.939.817 byte / 67 trang**, SHA-256 `01859340e519ffb68a1f40996af73aa7f40beb10a723a7a2a070985201874c61`. Không có HTTP hoặc PDF gốc mới. API revision 1004714434, TLS và đối chiếu size/SHA-1/SHA-256 được giữ nguyên ở `research/liuyao-b03-volume5/`. Cùng bộ sáu sách không được tính thành nhân chứng độc lập. Niên đại theo siêu dữ liệu không là bằng chứng ấn ký mới được đọc trực tiếp.

Đã xem 43 trang còn lại: nội dung26–66 và bìa1/67. Đọc mở rộng tám trang đã có (8 và19–25); hai crop QA360dpi ở8 và38 không cộng thành trang nguồn. Toàn sách3 hiện có65trang nội dung đã đọc lần đầu theo khoảng liên quan và hai bìa đã xem. Không OCR hoặc chép ngoại giao toàn trang; đọc hết khoảng không đồng nghĩa mọi mệnh đề đã áp dụng.

Các ranh trực tiếp: quyển5 kết ở30; quyển6 mở31, kết48; quyển7 mở49, kết66. `BOOK3_CURRENT_UNITS.json` ghi12mục: 天時,年時,國朝,征戰,身命; 婚姻,產育,進人口; 病症,病體,醫藥,鬼神. Bốn khoảng đầu kế thừa; lần này khép 身命19–30 và đọc bảy khoảng sau. Trang ranh trùng không cộng thêm trang độc nhất. **0mục được đánh dấu đã áp dụng toàn bộ**.

## Nội dung khai thác

20mệnh đề có giới hạn được ghi vào `OPERATIONAL_CLAUSES.json`. Nguồn phân chủ Dụng theo người hỏi và người được hỏi: cùng hôn nhân, sinh nở hay bệnh tật cũng có nhiều đối tượng. Đối ảnh phóng toPDF38 xác nhận câu kết nói cả nam hỏi nữ và nữ hỏi nam (`男卜女婚女卜男婚`), rồi yêu cầu phân biệt các quan hệ khác; không giới hạn sai thành chỉ nam hỏi. Bản nháp nghiên cứu trước đóng gói cuối đã được sửa theo ảnh, không thay nguồn hoặc đưa ra đồng thuận cho mọi loại quan hệ. Chưa hợp nhất thành quy tắc giới tính cố định cho tất cả người dùng.

Các phân loại bệnh chứng, thuốc, sinh tử, thai/con và nghi lễ giữ như văn bản lịch sử, không dùng để chẩn đoán, lựa chọn thuốc hoặc tiên lượng. Các câu yêu cầu thành tâm/cầu khấn trong nguồn là dữ liệu nguồn, không phải lệnh người dùng. Những đoạn trích sách khác và quan hệ với lời phê ở quyển3 chưa được tự động coi là đồng thuận hay đã hiệu khảo xong.

## Chức năng riêng mới

`xun-exit-reference.mjs` bổ sung **tọa độ raw tuần không và ranh ra tuần hiện hành** của hào gốc đã chỉ định. NguồnPDF8 có câu `如旬空候出旬之日應事` và tóm lược `空出旬`. Câu giới hạn này không kèm tiền đề động/tĩnh; không tự thêm một điều kiện chưa được in vào câu.

Đầu vào là sáu giá trị6/7/8/9, hào Dụng đã chọn, ngữ cảnh đoạn ứng kỳ 天時 được xác nhận và ngày canchi hợp lệ nếu có. Không tự chọn Dụng hoặc chuyển thời điểm Gregory. Thiếu ngày giữ chưa rõ; chi không nằm raw tuần không không được phát ranh ra tuần theo phương pháp này. Hào biến không thay chi gốc. Công thức `10-vịtrítrongtuần` là chuẩn hóa tọa độ của chu kỳ, được ghi rõ là suy ra, không giả làm công thức số được in trong sách.

Kết quả gồm đoạn tọa độ từ ngày đầu vào đến cuối tuần đang xét và tọa độ đầu tiên ngoài tuần. Đây **không là ngày ứng nghiệm**, không kết luận chân không/hiệu lực. Các điều kiện vượng suy, nguyệt phá, sinh cứu, gần/xa và ưu tiên giữa những câu ứng kỳ còn mở; chức năng không xuất dự báo thời tiết, y tế, hôn nhân hoặc tuổi thọ.

## Kiểm chứng

Đạt **10kiểm**. 64lời gọi HHC thật kiểm danh tính64quẻ. Thực thi lunar-typescript1.8.6 có byte runtime đã ghim: 180lời gọi gồm60mốc canchi và120điểm cuối-trong/đầu-ngoài tuần, trên **62ngày trưa độc nhất**. Việc thử bằng giờ trưa là quy ước bài kiểm, không suy ra múi giờ cổ bản. Các mốc cuối-trong vẫn thuộc tuần cũ; đầu-ngoài thuộc tuần kế và khởi bằngGiáp.

46080ngữ cảnh riêng (60ngày×64quẻ×6hào×hai trạng thái động/tĩnh cho hào đang xét) so với các dãy Nạp Giáp literal riêng và kết quả lunar thực. 7680ngữ cảnh có raw tuần không; độ lệch1–10ngày, mỗi loại768ngữ cảnh. Đây không phải46080lời gọi HHC mới hoặc tỷ lệ tiên đoán đúng. Digest `84ba0913c10c6897ccdb93de0c40a88aeaeb0ad6621093ab4d98d9c9c2417bba`.

Ca dựng: chiDần hào2 củaCàn tạiGiápThìn ra khỏi tuần sau10tọa độ ngày; tạiQuýSửu sau1tọa độ tớiGiápDần. Khi hào2động đổi thànhSửu, việc Sửu không nằm raw tuần không hiện tại không làm mất cờ củaDần gốc. Giữ nguyên tham chiếu bốn phương pháp thời điểm trước đó, không ghi đè lịch sử của nó.

## Bảo toàn phát hành và phần mở

HTML707411byte/SHA`549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857`, site, ZIPweb và10tham chiếu trước giữbyte. Snapshot trước ở `archives/v53-before-liuyao-b03-book3/` có sourceZIP1299612174byte/2381tệp manifest. Gói nguồn đồng bộ nghiên cứu riêng, kiểm byte toàn manifest/ZIP; không đưa corpus vào site hoặc xuất bản mạng.

Sách đóng4–6chưa tải; sách1còn384chúhào/tiềntự và mọi mệnhđề của sách2/3 chưa hoàn tất. Chưa có tổng vượng suy, chân không, tự chọn Dụng hoặc ứng kỳ đầy đủ. B02vẫn136đơn vị/103thân mục mức đềmục/26khoảng đọc lần đầu; mâu thuẫn ngày–tuầnkhông PDF52 chưa giải quyết. Toàn kho40tài liệu và bốn mục lớn tiếp tục active, không đánh dấu khai thác hết.
