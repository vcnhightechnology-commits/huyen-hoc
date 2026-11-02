# Bộ tham chiếu vị trí bảng 後天時方

`PHYSICAL_CELLS.txt` có60dòng theo khóa hàng in và12vị trí子丑寅卯辰巳午未申酉戌亥. `HOUR_TABLE.json` nối720vị trí vớiSHA/trang/trạng thái:707đọc nhãn,12không thấy nhãn,1chữ mở. `+` chỉ liệt kê các chữ cùng vị trí;`-` là không thấy nhãn,□là chữ chưa quyết. Không suy ô trống thành cát hoặc lỗi in.

`hour-reference.mjs` là tra cứu nội bộ bằng khóa/chi có sẵn,không có API ngày dương hoặc lời đoán. `SOURCE_PREMISES_AND_GAPS.json` phân biệt mảnh chữ đã đọc,giả thuyết vàđầu vào còn mở. Chín hàng không có đúng một罡,388/576vị trí khác giả thuyết chép mẫu theo chi;không tự sửa dữ liệu theo vòng quay.

14kiểm nguồn/runtime,720lần chạy HHC và720lần lunar-typescript thật chỉ kiểm tọa độ ngày/chi giờ của lựa chọnUTC+8/00:00. Không phải kiểm dự báo hoặc xác minh quy ước lịch của bản in. Xem `../../MEIHUA_HOUR_TABLE_REPORT.md` vàQA. Nguồn/QA ngoài site,toàn sách chưa hoàn tất.
