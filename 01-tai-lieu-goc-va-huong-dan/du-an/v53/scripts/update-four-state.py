from pathlib import Path
import json
root=Path(__file__).resolve().parent.parent
p=root/'research/four-items/WORK_STATE.json'
s=json.loads(p.read_text(encoding='utf-8'))
s.update(date='2026-10-26',completed=['yi','bazi','home','tuvi'],status='complete',report='v53/FOUR_ITEMS_REPORT.md',verification={'engine':14,'policies':7,'browser':47,'regression':50,'home':40,'experience':36,'totalPassed':194,'actualIztroHoroscopeCalls':178},limits='Completed the four bounded items, not the entire library or all traditions; see source notes and report.')
p.write_text(json.dumps(s,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(root/'NEXT_STEPS.md').write_text('''# Trạng thái sau khi hoàn thành bốn mục — 26/10/2026

Yêu cầu “làm tiếp cho tới khi xong 4 mục” đã hoàn thành trong phạm vi xác định ở `research/four-items/WORK_STATE.json`. Đọc `FOUR_ITEMS_REPORT.md` trước khi tiếp tục; không mở lại bốn mục chỉ để tăng số phiên bản hoặc số lượt tải.

1. Kinh Dịch: đủ 384/384 hào thường có lời đọc riêng; hai bổ sung Càn–Khôn giữ riêng. Không còn 372 hào dùng lời chung. Bản 12 hào và kiểm kê thư viện trước đây là mốc lịch sử; độ phủ hiện tại ở `research/four-items/COVERAGE_UPDATE.json`. Lời biên tập không phải bản dịch sát chữ hoặc hiệu khảo ảnh trọn bộ.
2. Bát tự: Thập thần/tàng can có trong luồng kết quả. Đọc ảnh Uyên Hải trang 54/trang in 三六, 12 tập hợp tàng can; 100 cặp quan hệ và 12 bảng khớp thư viện chạy thật. Tam Mệnh Thông Hội ghim commit; không gộp bảng phân ngày tư lệnh vào tàng can cố định, không tự chấm vượng suy/chọn dụng thần.
3. Nhà ở: đủ tám đồ hình/64 nhãn NDL đã so engine; công cụ đo hướng nhận đối tượng, bất định, chuẩn Bắc và từ thiên, lưu/khôi phục/TXT. Bảy khu vực bố trí phòng vẫn qua hồi quy. NDL là bản Nhật chuyển biên, chưa xác minh quy ước năm sinh→cung phi hoặc 24 sơn.
4. Tử vi: có nút mở nhanh vận hạn, chọn ngày, đại hạn/năm/tháng, Tiểu hạn/Tứ Hóa, lưu/mở/TXT/in. 178 lần gọi horoscope iztro thật; ghi riêng hiệu chỉnh tháng nhuận, đồng hạn và khác biệt Nhâm Hóa Khoa. Đây là đọc chủ đề cung theo thời gian, chưa tổng hợp toàn bộ sao thành dự báo sự kiện.

Sáu bộ kiểm đạt 194/194; `engine.js` giữ nguyên byte. HTML độc lập, bản gốc, site và hai gói cập nhật cùng V53. Snapshot trước phạm vi: `../archives/v53-before-four-items/`. Nguồn mới và ghi chép: `research/four-items/SOURCE_NOTES.md`; nguồn/QA không đưa vào site hoặc gói web.

## Những hướng thực sự còn mở

- Hiệu khảo Kinh Dịch bằng ảnh ấn bản và xử lý bảy khác dạng đã ghi ở V49, khi có nhân chứng đủ rõ; không coi việc thêm lời đọc là giải quyết dị bản.
- Đọc ảnh các đoạn Tứ Hóa/Đẩu Quân/đại hạn; phân định cách áp bảng can vào lưu niên, cách khởi hạn và quy ước của từng truyền bản. Giữ Nhâm Thiên Phủ/Tả Phù tách biệt.
- Tìm nguyên bản Trung Quốc định danh tốt cho Bát trạch và quy ước năm/cung phi; mặt bằng có Bắc, cửa/cửa sổ, kích thước thực nếu phát triển công cụ bố trí. Không suy từ 64 nhãn sang công năng mọi phòng.
- Giờ địa phương lịch sử cần xác minh IANA và mốc đổi giờ trước khi tự điền múi giờ nơi sinh.
- Nghiên cứu lịch 1906/2057 và sóc gần nửa đêm nếu có tài liệu đương thời hoặc nguồn độc lập mới. Không tải lại cùng JPL/HKO chỉ để tăng lượt.

Kho sách **chưa áp dụng hết**: 40 hồ sơ BOOKS và 16 hồ sơ mô-đun có chồng lặp/portal, không phải 56 toàn văn đã học. Các trang Wikisource thiếu nội dung hoặc metadata không chắc vẫn bị hạ mức chứng cứ. Đã có scan Uyên Hải có thư mục xác định để bổ sung phần tàng can; không nâng mọi nguồn Uyên Hải cũ thành đã xác minh.

Ưu tiên giao diện mới nhất của người dùng tiếp tục có hiệu lực: dễ tiếp cận, chỉ kết quả và diễn giải; nguồn, corpus, suy luận nghiên cứu và bảng engine ở tài liệu riêng. Các yêu cầu hình ảnh, khảo sát bố cục, nhập giờ thật, tự đổi năm âm, đọc cung đối diện và bố trí phòng đã hoàn thành, xem các báo cáo lịch sử tương ứng. Chỉ sửa tiếp khi có lỗi, nguồn tốt hơn hoặc một cải tiến cụ thể.

Không tự xuất bản, gửi cho người khác, sửa các bản V46–V52 hoặc phá hủy snapshot. Khi có phạm vi mới hoàn chỉnh, cập nhật nguồn V53, build, kiểm thử phù hợp, báo cáo và gói; không đổi số chỉ để có bản mới.
''',encoding='utf-8')
print('Updated the current four-item completion state and remaining research backlog.')
