# Nhà ở: đủ24 tiết khí/phương vị và nạp giáp địa lý

Ngày27/10/2026. Bảy kiểm chức năng đạt; đối byte và pixel nguồn đạt. Hai mục 二十四節氣方位/八卦納甲三合 được liệt kê đủ phần bảng, tượng và văn trong phạm vi ảnh53–57. Bộ tham chiếu riêng tra phương vị theo tên tiết khí nguồn hoặc quẻ địa lý theo tọa độ nguồn. HTML/site/ZIPweb giữ nguyên; bốn lĩnh vực và toàn kho vẫn chưa hoàn tất.

## Chứng cứ và nội dung

Tái dùng 欽定協紀辨方書卷二/CADAL06056503.djvu,3.433.014byte, SHA-256`bfd3b76c55d62324919ab161c8c2ba2ecb129b3b2c59a3ab0428807e8f8278db`. Năm ảnh53–57 đã đọc được mở rộng;0HTTP/container/trang nguồn mới. Hai đồ53/55 được xem ở bốn hướng xoay, thêm hai crop chữ54/56; tổng4crop native/6xoay không nội suy được so lại từng pixel. Không OCR hoặc điền nét từ đáp án engine. Nguồn và ghi chép ngoài site.

Đồ53 có24 tên tiết khí/24 tọa độ; lời ảnh54 khớp đủ24 cặp. Đồ dùng Khảm/Chấn/Ly/Đoài tại bốn phương chính, không ghi Tý/Mão/Ngọ/Dậu; bốn thay tên tọa độ khi nối mô hình được khai báo. Năm alias tên tiết khí với thư viện hiện đại cũng khai báo riêng, không sửa chữ ảnh. Các phương vị độ là mô hình đều24vị trí đã nêu trong phạm vi trước, không là kinh độ Mặt Trời hoặc phép suy thời điểm thiên văn.

Nguồn nói bốn Lập/hai Phân/hai Chí ứng tám quẻ và nhắc Kỳ môn chín cục. Câu dẫn này chưa cung cấp đủ quy tắc chọn cục; không tạo tính năng Kỳ môn chỉ từ24 nhãn hướng.

Đồ55 và văn56 gồm:乾甲、坤乙、艮丙、巽辛、震庚亥未、兌丁巳丑、坎癸申辰、離壬寅戌. Tổng24 tọa độ thuộc8 quẻ; đọc đủ24 nét tượng. Sáu đoạn văn nạp giáp, kể cả dòng nối đầuảnh57, giữ riêng lời phê bình **其法不知所自來** (nguồn nói không biết phép ấy từ đâu tới), phần trích 啓蒙附論 và lý giải tiên/hậu thiên. Chưa đối riêng nhân chứng của sách được trích, không biến lập luận khí/chất/nước/lửa thành kết quả thực nghiệm.

Nạp giáp này thuộc tọa độ địa lý, khác gán can–chi từng hào: Khảm nhận Quý và Ly nhận Nhâm; Lục hào hiện có dùng Mậu/Kỷ cho hai quẻ tương ứng. `geographicalNaJia` yêu cầu tên hệ và một ký tự đúng bảng; không tự nhận Tý/Mão/Ngọ/Dậu hay Mậu/Kỷ thay tọa độ nguồn. Kết quả không sinh can–chi từng hào, lịch, phòng ở hoặc dự báo. Câu dẫn Cửu tinh/tịnh âm tịnh dương ởảnh57 chỉ được ghi nhận, chưa là toàn thuật toán của những phép ấy.

## Kiểm chứng

7 kiểm đạt:24 lần `HHC_MOUNTAINS.inspect` thật đối phương vị của mô hình;8 lần `HHC_ENGINE.hexNumber` thật đối24nét tượng/tám quẻ thuần;1 bảng tiết khí lunar-typescript1.8.6 thật đối tên/thứ tự24mục;2 lá số Lục hào tham chiếu riêng thực thi để kiểm Mậu/Kỷ không bị lẫn Quý/Nhâm. Không gọi phép so tên/thứ tự là hiệu chuẩn24 thời điểm tiết khí; không có thời điểm nguồn để đối. Đã kiểm đủ24 gán nạp giáp, tên hệ/alias tường minh, trảnull khi chưa biết và không sửa đầu vào. Probe khi còn ởtmp được lưu riêng; các lượt đó không cộng vào số thực thi tích hợp mới.

HTML gốc/V53/site707411byte giữ SHA`549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857`; ZIPweb344047byte giữ nguyên, site chỉindex.html. Snapshot trước`archives/v53-before-home-direction-tables/` giữ3164tệp/ZIP2037602853byte. Gói nguồn mới và manifest được đối byte sau đóng gói, kết quả`qa/home-direction-tables/RELEASE_RESULTS.json`. Không tăng phiên bản, xuất bản mạng hoặc sửa lịch sử.

Bản đồ12mục hiện hành kế thừa ba phạm vi nhà ở trước; bốn mục hẹp03/04/08/09 đã liệt kê phần văn/bảng, còn ứng dụng đo thực và những chương khác. Không coi Hiệp Kỷ là đã áp dụng trọnP03 Trạch Kinh. Chuyển khoảng trống độc lập Bát tự/cách cục và các điều kiện đầy đủ; Dịch/Tửvi còn theo backlog,40 hồ sơ vẫn whole0.

Tái kiểm: `node v53/scripts/test-home-direction-tables.mjs`; `python v53/scripts/verify-home-direction-tables-sources.py`; `python v53/scripts/verify-home-direction-tables-release.py --no-write`.
