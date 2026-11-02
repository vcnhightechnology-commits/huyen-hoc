# 建破魁罡: giữ riêng khung ngày và khung phương

Đọc mở rộng hai ảnh nguồn đã giữ: P08 PDF131 và 選擇要略 ITKC244. Hai crop native khớp RGB. Đây là hai ngữ cảnh của hai tác phẩm, không phải một truyền bản P08 mới. Không tải thêm ảnh, không tăng vị trí đã đọc đầu.

Ở P08, đoạn dẫn bảng ngày viết `若值建破魁罡等雖有吉星固當迴避`. Đoạn trước còn có mệnh đề riêng về 玉皇帝星/天皇帝星/紫微帝星 trực nhật. Không suy rằng mệnh đề này thắng mọi điều kiêng, cũng không tự giải thứ tự khi cùng xuất hiện. Chữ nhỏ của 220 ô nhãn đang mờ chưa được giải quyết bằng caption.

Ở ITKC244, đề mục là `建破魁罡方`; thân đoạn nói `其殺止占方道` rồi nêu điều kiện sao đến phương cho `宅舍修作`. Giữ nguyên khung phương. Nhãn 建/破 trong bảng ngày không đủ để xác lập phương đang bị chiếm; một cờ “có sao tốt” không thay cho toàn bộ điều kiện riêng của đoạn. Cách nối giữa 三奇/祿馬/陽龍陰兎/走馬六壬/等吉星 vẫn chưa mã hóa thành AND/OR.

Hàm `inspectDeclaredKuigangContext` chỉ tiếp nhận tiền đề khai báo, với system và frame đúng cặp. Nhánh ngày trả mệnh đề tránh cục bộ, nhánh phương trả mệnh đề thuận cục bộ khi đủ điều kiện đã xác lập. Hai mệnh đề có thể cùng tồn tại mà kết luận tổng thể vẫn null. Không sinh ngày, tháng, phương, sao, khuyến nghị sửa nhà hoặc dự đoán kết quả.

Ba tệp được đóng băng trước triển khai. Sáu nhóm kiểm đạt: 36 khung ba giá trị, 252 bất biến null, bốn khung không hỗ trợ và bảy đầu vào sai. Kiểm nguồn đối SHA-256 và pixel hai crop. Đây là kiểm chức năng tham chiếu văn bản, không đối chiếu engine lịch mới; không chạy lại 720 truy vấn lịch đã có.

Bản chữ đầu dùng 兔; audit giữ riêng dạng ảnh 兎, không sửa freeze. Dữ liệu trước chuẩn bị ghi actuallyViewed=false; READING_AUDIT ghi lượt xem sau đó. Các câu về tổn thất/hiệu quả được giữ như lời nguồn lịch sử, chưa có kiểm chứng thực nghiệm.

Phạm vi đã tiếp nhận vào nghiên cứu V53 trong HOME_SPATIAL_CONTEXT_REPORT.md; không đưa vào site. Gói nguồn tổng hợp được kiểm sau lô có ích cùng các điều kiện mới, không tạo thêm snapshot ZIP. Audit gói tại recovery/research-release/FINAL_VERIFICATION.json phải khớp manifest V53 hiện hành.
