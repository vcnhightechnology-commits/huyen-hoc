# V53 — đọc cung không có chính tinh cùng cung đối diện

Ngày 25/10/2026. Tiếp phần nâng chất lượng diễn giải trong `NEXT_STEPS.md`; giữ cùng V53. Bản hoàn thành trước sửa được giữ nguyên trong `archives/v53-before-opposite-reading/`, có HTML và cả hai ZIP.

## Vấn đề và cải tiến

Trước đây, khi cung không có chính tinh tọa thủ, phần đọc chỉ nhắc chung “đọc thêm cung đối diện”, nhưng chưa chỉ ra cung nào và chưa đưa người dùng đến phần đó. Cung Mệnh không có chính tinh còn nhận tiêu đề tổng quan chung, không gắn vào bố cục lá số cụ thể.

Nay phần đọc xác định đúng cung đối diện, địa chi và các chính tinh thực sự ở cung ấy. Có khối “Góc nhìn bổ sung · Cung đối diện” và nút đọc cung liên quan. Nút này đồng bộ danh sách chọn chủ đề, cung sáng trên lá số và diễn giải. Chọn lại cung gốc khôi phục đúng phần đọc ban đầu.

Ví dụ mẫu 20/05/1990, 08:30, nam, UTC+7: Mệnh tại Sửu không có chính tinh; đối diện là Thiên Di tại Mùi, có Thái Dương và Thái Âm. Những sao đó được ghi là **nằm tại Thiên Di**; không thêm vào danh sách sao Mệnh, không đổi lá số hoặc đưa ra kết luận tốt/xấu từ việc cung trống. TXT và bản in giữ nhãn phân biệt này.

Các cung đã có chính tinh giữ cách đọc trực tiếp hiện tại. Nếu một dữ liệu đầu vào giả lập có cung đối diện cũng không có chính tinh, không tạo sao hoặc bịa phần diễn giải. Hàm đọc dùng chỉ số vị trí của cung thay vì dựa vào thứ tự mảng. Chọn chỉ số không tồn tại trả lỗi rõ.

## Nguồn và giới hạn diễn giải

Dùng nguồn kỹ thuật gốc đã lưu: gói **iztro@2.6.2** trong V46. Đọc `lib/astro/analyzer.js`, `FunctionalPalace.js` và `FunctionalAstrolabe.js`. API `surroundedPalaces(...).opposite` trả cung cách sáu vị trí; `isEmpty()` xét các sao loại major. Đã kiểm lại đủ **209 tệp cài đặt** khớp từng byte tarball npm đã lưu và SHA-512 khớp metadata gốc. Không tải lại gói, không gọi phiên bản này là mới nhất.

Tarball SHA-256: `d44e96631c0506424c3aef25a7bba8e43e01729102d6a703720cbe224aec5403`. Kích thước và SHA-256 ba tệp nguồn liên quan nằm ở `qa/opposite-reading/source-audit.json` cùng phân loại vai trò nguồn.

Đây là căn cứ kỹ thuật cho **quan hệ vị trí và thành viên sao**, không phải nguồn xác nhận mọi học thuyết luận đoán. Văn bản diễn giải là nội dung văn hóa do dự án biên tập; khối bổ sung là cách tổ chức đọc dễ tiếp cận. Không mô tả nó là bản dịch cổ thư, không tự tuyên bố quy tắc “mượn sao” đã được hiệu khảo, không chuyển chính tinh vào cung trống và không thêm dự báo vượng/suy, bệnh, tiền bạc hay tương lai.

## Kiểm chứng

Thực thi iztro thật trên 100 đầu vào đã có, quy ước hiện tại/same được ghi rõ. Mục đích mới của lượt chạy là kiểm API cung đối diện và các sao tương ứng, không lặp lại thống kê 17 trường chỉ để tăng con số.

- **100 lần tạo lá số, 1.200 cung** được xét bằng API thật.
- **196 cung không có chính tinh**: vị trí đối diện và tập chính tinh ở đó khớp.
- **1.004 cung có chính tinh**: không tạo khối đối diện thay cho đọc trực tiếp.
- Dựng phần đọc/summary trên cả 100 lá số không làm thay đổi một byte JSON của chart.
- Mã engine số học, an sao và lịch vẫn nguyên SHA-256 so với bản lưu trước sửa.

Raw dữ liệu quan hệ từ API, dữ liệu đọc và sai khác nằm trong `qa/opposite-reading/engine-comparison.json`. Phạm vi này kiểm logic liên kết đọc, không phải kiểm chứng năng lực tiên đoán hay toàn bộ quy tắc của mọi truyền phái.

`verify-opposite-reading.mjs`: **21/21** kiểm tra đạt, gồm nguồn, quan hệ, cung trống, cung có sao, vị trí mảng đảo, nhãn TXT/in, chuyển liên kết, dropdown/chart, hồ sơ và bố cục 320/390/768/1440 px. Đã nhìn ảnh máy tính và điện thoại; không lỗi JavaScript hoặc HTTP từ bản HTML độc lập.

Chạy lại `verify.mjs`: **50/50** và `verify-experience.mjs`: **36/36**. Tổng ba bộ vừa chạy **107/107**. Kiểm tra bảo toàn trong bộ trải nghiệm được thu về các tệp cần tiếp tục giữ nguyên (engine, nội dung quẻ và ảnh); `content.js`/phần render của app được phép đổi cho cải tiến này và được bộ mới kiểm riêng. Các số 121/123 trước đó là hồ sơ những phạm vi khác, không cộng dồn vào tổng vừa chạy.

## Phát hành và tiếp tục

Build lại HTML độc lập, bản ở gốc workspace, `site/index.html` và hai gói V53. Nguồn, suy luận phát triển, kiểm thử, dữ liệu so engine và báo cáo vẫn ở tài liệu riêng, ngoài web sử dụng. Không xuất bản hoặc gửi cho người khác.

Phần đọc vô chính diệu đã có đường nối dữ liệu cụ thể; các hướng sâu hơn như tam phương, phối hợp sao hoặc văn bản truyền giải vẫn phải có phạm vi nguồn rõ trước khi thêm lời luận. Không tự biến liên kết đối diện đã kiểm tra thành chứng cứ cho những lớp luận giải chưa nghiên cứu.
