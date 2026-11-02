# Các nhãn ghép trong bảng ngày P08 — mười cột đầu

Ngày29/10/2026. Tiếp phần720ô chưa chép đủ nhãn,không chạy lại720truy vấn lịch hoặc tải ảnh. Xem lại ảnh131 và132cũ để định vị,đọc chi tiết12hàng×10cột甲子–癸酉 trên ảnh131. Bổ sung crop native đủ lề từ ảnhraw,ba dải bốn tháng vàba vùng kiểm nhỏ;không OCR,không dùng công thức để điền ô.

Đọc được82ô có nhãn làm việc trong các nhóm天和/地和/人和/河魁/受死/建/破.38ô còn chưa đọc chốt,một ô vì nét mực/lề gáy che;600ô của50cột khác chưa chép trong phạm vi này. Đây là dữ liệu có trạng thái từng ô,không đánh đồng720tọađộ tra được với720nhãn đã đọc. Từ điển đang giữ không chốt chữ nhỏ từng được nghi là帝/寧/富;caption天皇帝星không được dùng để sửa ô.

Freeze đầu lưu bản đọc83ô;crop bổ sung cho tháng12/癸酉cho thấy chữ bịmực che nên hạ xuống chưa rõ. READING_AMENDMENT.json và SUPPLEMENT_FREEZE.json được lưu trước triển khai;freeze đầu không sửa,không đếm ô này là河魁. Các định vị建/破trong120ô khớp dữ liệu nguồn trước,không là một lần chạy engine mới.

HàmlookupSourceMonthCellbuộc đúng nguồn và tháng nguồn khai báo. Ô đọc được trả nhãn,bịmờ trả unresolved,ngoài120ô trả not-transcribed;không trường hợp nào trả tốt/xấu tổng thể. Thánglịch hiện đại/nhuận/tiếtkhí vẫn chưa xác lập và bị chặn. SourceMonth null hoặc day null giữ chưa rõ;không lấy thiếu dữ liệu làm trống hoặc vôkiêng.

Bảy nhóm kiểm tra quét720khung nguồn:120đã xem,82đọc/38chưa,600chưa chép;giữ ba dạng thiếu đầu vào,chặn khunglịch không hỗ trợ và đầu vào sai,đối freeze/correction.0engine HHC/lunar/iztro mới vì câu hỏi là chữ trong ảnh,không phải tọađộ lịch mới. Môđun tạm ởstaging,chưa đưa vàoV53/site hoặc tăng trạng thái toàn tác phẩm.

Tiếp đọc các cột còn lại và tìm ngữ cảnh giải chữ nhỏ bằng nhân chứng hợp lệ;giữ ô mờ chưa rõ thay vì sao mẫu. Nguồn có lờiưu tiên/kiêng trongcaption nhưng chưa được mã hóa như kếtluận ngày;không thay bằng lời khuyên cho người dùng.

## Bổ sung mười cột kế tiếp

Đã đọc thêm120ô甲戌–癸未trên ảnh132:81nhãn đọc/39chưa rõ. Cộnghai khối:240ô đã xem,163nhãn đọc/77chưa rõ;480ôcủa40cột khác chưa chép. Bảy nhóm kiểm vàAPIhiện hành dùng tổng mới,không lấy số120ởmốcđầu làm hiện trạng.

Bản nháp khối hai bị lệch tháng8cột5/6,khi đối marker cũ phát hiện;đọc lại ảnh thấy地和/破. Nháp không được chấp nhận. Lượt chuẩn bịdữ liệu dừng lỗi nhưng thao tác tiếp theo đã sửa đườngdẫn môđun trước khi freezekhối hai;chạy thử lúc đó lỗi thiếuMANUAL_SECOND_BLOCK.json,không có kết quả thành công. SECOND_BLOCK_FREEZE.json ghi rõ trình tự này;chỉ có khối đầu cófreeze trước triển khai. Khối hai được chốt trước lần chạy thành công,không gọiđó là kỳvọngmù trước triển khai. Giữ cảhai mức provenance táchbiệt.

## Bổ sung bốn khối cuối và sửa lề crop

Đã xem và nhập riêng480ô còn lại, đóng băng dữ liệu/kỳ vọng trước khi mở rộng hàm. Hiện đủ720tọađộ đã kiểm ảnh:500nhãn đọc được,220ôchưa chốt;không còn tọađộ chưa xem nhưng chưa thể gọi chép đủtoànbảng. Nhãn làm việc bổ sung墓/四廢,không tự chấm tốt/xấu.

Crop134-sixth-ten cũ cắt mấtcột癸亥và mộtphần壬戌. Đã xem raw134kèmheader,đổi sang cropnative đầyđủmười cột. Lầnnháptừcropthiếucột cómột số dòng lệch,giữ REMAINING_BLOCKS_INITIAL_FAILED_DRAFT.json;đối marker phát hiện,đọc lại ảnh và sửa trướcfreeze. Không ép marker vàoôchưađọc:tháng12/乙未mớiđểchưarõ trongkhi marker破cũ vẫn được bảo toàn riêng;không ghi đèchứngcứcũ. Không có lỗi hoặc thay đổi nào trên site người dùng.

Sáu khối dữ liệu và một đínhchính đọc được trả theo đúngtọađộ/crop. Trạngthái inspected khác transcribed;220unknownkhônglàtrống/khôngkiêng.11cropRGB và7nhóm kiểm quét720khung đạt,0calendar/HHC/iztromới. Các nhãn mờ,vốn tháng/nhuận/tiếtkhí,tínhđộc lậpnhânchứng vàưu tiên vẫn mở. Mã hiện ởstaging;chưaphát hành vàoV53.
