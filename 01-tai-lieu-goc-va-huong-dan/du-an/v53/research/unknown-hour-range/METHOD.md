# Đặc tả khoảng giờ chưa biết

Đầu vào vẫn là ngày dương, múi giờ cố định và quy ước ngày củaHHC. Khi`noTime=true`, không dùng mốc trưa làm câu trả lời. Lưới hỗ trợ của biểu mẫu là mọi giờ/phút với giây0: k=0..1439, giờ=floor(k/60), phút=k mod60. Độ phân giải này là quy ước đầu vào phần mềm, không phải độ chính xác lịch sử của mọi giờ sinh.

Mỗi k gọi`HHC_ENGINE.bazi` với`noTime=false`; so ba trụ đầu với dữ liệu ngày chưa rõ giờ. Bất kỳ khác biệt nào cũng hủy phạm vi chung. Với lá số có giờ xác định, gọi đúng`HHC_BAZI_CYCLES.inspect` để lấy ngày khởi và mười chặng. Không có nhánh công thức khởi vận riêng chỉ cho ngày chưa rõ giờ.

Ở11ranh, lấy min/max theo thời điểm lịch dương của bộy/m/d/hour/minute, lưu cảphút sinh làm chứng tích cực trị. Mỗi chặng nhận cận khởi thứi và cận kết thúc thứi+1. Thời gian kết thúc không bao gồm chính mốc bắt đầu chặng kế trong cách trình bày chặng đã có; các cận không tự tạo phân bố xác suất hoặc chứng minh mọi điểm giữa đều có thể là giờ giao vận.

Chiều vận dựa can năm theo tiết và giới quy ước. Mốc tiết mở tháng/chênh phút, phép chia4320/360/12 vàgiờ dư×2, cộng tuần tự năm→tháng→ngày→giờ, kẹp cuối tháng/năm: giữ nguyên triển khai đã kiểm. Các nguồn đã đọc khác cách cộng tháng lịch truyền thống phải được giữ riêng, không gọi phần mềm là tái hiện mọi chi tiết trong sách.

Từ chối/suppress: ba trụ không duy nhất, thiếu dữ liệu lá số, hoặc gặp thay đổi ba trụ trong quét ngày. Mô-đun không thay thuộc tính`start/offset`của ngày chưa biết thành một mốc; chúng vẫnnull. Các thuộc tính`range`, `startRange`, `endRange` được thêm rõ ràng. Can chi10chặng không đổi.

Đệm20cấu hình ngày/giới/múi/đổi ngày/trụ/tiết, chỉRAM. Khi trả từ đệm, sao chép dữ liệu. Hồ sơ chỉ giữ đầu vào vốn có, không tự nhận1.440khả năng là1.440bản ghi người dùng. Các ngày minh họa trongQA là fixture kiểm thuật toán, không phải dự báo hoặc hồ sơ thực.

Kết quả kiểm12trường hợp chưa ghi nhận cực trị bên trong lưới (đều ở đầu/cuối ngày trong mẫu); không dùng quan sát đó để bỏ quét các phút khác hoặc tuyên bố định lý về mọi lịch.
