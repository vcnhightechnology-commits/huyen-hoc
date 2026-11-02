# Phục đoạn: tách truyền bản và kiểm phản ví dụ chu kỳ

29/10/2026. Phạm vi nghiên cứu nội bộ; chưa thêm phép chọn ngày vào web.

Đã đối đoạn Phục đoạn của 選擇要略 trên ảnh ITKC249 với phần 伏斷日密日裁衣日 trong 協紀辨方書 quyển36. Tên giống nhau chưa xác lập cùng thuật. ITKC ghi 辰剋干 và ngoại lệ 合得四殺沒時則不忌; ảnh mở rộng xác nhận đủ câu ngoại lệ, không phát hiện sai chữ mới. Chưa giải xong gốc nghĩa 辰 hoặc cách xác định 四殺沒時, nên không tự lập bảng60ngày và không ghép ngoại lệ này vào thuật tú.

Hiệp Kỷ mô tả phép28tú, bảy điểm khởi nguyên, rồi chính người biên soạn phản bác tính nối liên tục của phép ấy. Trích dẫn một phương pháp trong sách không đồng nghĩa tác giả tán thành. Hàm mới chỉ tái dựng số học hữu hạn có khai báo nguồn để kiểm lời phản bác, mọi kết quả giữ useForRecommendations=false, ngày lịch và cát hung là null.

## Nguồn và bản đọc

Ba body HTTP200 qua TLS chuẩn, giữ URL/headers/byte/SHA trong research/home-fuduan/REQUESTS.json: trang Commons, PDF SSID-12152602 quyển33–36, và bản chép Wikisource quyển36 revision627179. PDF54.208.629byte/SHA256 3f6f81e7332a779dc8c43e8b69808e3f03449b8c595daea649529bea2c8d84ca có107vị trí; chỉ11vị trí đã xem lượt đầu,96chưa xem. Đây là một container mới để giải khoảng trống đã định, không phải107trang đã khai thác.

Bìa đọc 殿版縮印 / 協紀辨方書 / 卷三十三至三十六. Chưa xác lập nhà in, năm in, hoặc cùng bản vật lý với nhãn 四庫全書 của Wikisource. Ngày2023trong metadata PDF là ngày số hóa/container, không gán thành năm in. L01vàL02là hai hồ sơ truy cập cùng tác phẩm, không tính hai sách mới hoặc hai truyền bản độc lập.

Ba JPEG lấy qua pypdf.page.images đầu tiên bị kiểm byte phát hiện khác stream DCT nhúng. Giữ cả ba làm lịch sử, loại khỏi bằng chứng byte gốc. Sau đó trích chính /DCTDecode._data tại PDF1/98/99, lưu ba stream JPEG1512×2328 và đối từng byte với PDF. Khẳng định này chỉ về stream ảnh nằm trong container đã tải, không xác nhận bản số hóa gốc của cơ quan. Giữ một crop ITKC249 và bốn crop Hiệp Kỷ đã xem, cả năm khớp RGB đúng vùng nguồn. Hai crop ITKC thử thiếu đoạn/nhầm đề mục250 được loại. Xem RAW_DCT_IMAGES.json, NATIVE_CROPS.json, XIEJI_NATIVE_CROPS.json.

## Quy tắc và giới hạn phép kiểm

Đã chép thủ công84tên tú trong bảng 伏斷時立成: bảy cột in từ phải sang trái1/4/7/3/6/2/5, mười hai hàng 子…亥. Nhãn góc bảng in 日 được giữ nguyên; chưa ép thành ngày dân sự hay giờ đồng hồ. Các chú nhỏ 暗金/伏斷 chưa chép hết, chưa làm bộ tiên đoán. Tên28tú tuần hoàn, bảy điểm khởi 虛/奎/畢/鬼/翼/氐/箕 và bảy ví dụ văn xuôi được đóng băng trước viết module. Đây là một bảng có ví dụ chồng lặp, không phải91nhân chứng độc lập.

Với giả thiết nguồn:12thời mỗi ngày,60ngày mỗi khối,28tú đi tuần tự. Khối đầu bắt đầu 虛, bước cuối719là亢; bước720liên tục kế tiếp là氐. Khối thứ hai theo điểm khởi ghi lại bắt đầu奎, lệch12bước so với氐. Điều này tái dựng câu 尚隔十有二宿不能輪轉. Sáu biên còn lại là phép suy số học kiểm thêm, không sáu phản ví dụ được trích nguyên văn. Không diễn giải lời phê của sách thành một chứng minh về tác dụng cát hung.

Toàn bảy khối có5.040bước=180vòng28tú; việc tổng chu kỳ quay về điểm đầu không xóa độ nhảy ở từng biên khối. Bảy nguyên không được tự neo vào ngày dương lịch nào. Cả hai API riêng chỉ nhận đúng sourceID/frameID và chỉ số nguyên trong phạm vi; đầu vào thêm ngày, múi giờ, quy tắc ITKC hoặc giả định hàng bảng bị giữ chưa xác định.

## Kiểm và đóng gói

Tám nhóm kiểm đạt:84ô tên tú,7ví dụ nguồn,7kỳ vọng biên (1trích nguồn+6suy số học),5.040khung hữu hạn,4.452cặp lặp7ngày và4.844cặp lặp28bước.19khung không hỗ trợ trả null;14đầu vào sai bị chặn. Bảy tệp bằng chứng/kỳ vọng giữ SHA từ trước triển khai. Không chạy engine lịch hoặc lá số trong phạm vi số học này; không nhận phép modulo là một lần đối chiếu lunar/iztro.

51tệp staging đã chép và kiểm byte/SHA sang research/home-fuduan, có cả thử nghiệm bị loại với nhãn rõ. Kiểm nguồn còn xác nhận ba body, ba stream DCT, năm crop RGB, bản đọc chọn và freeze. Nguồn/corpus/QA nằm ngoài site. L01/L02chuyển sang research_only; danh mục vẫn40hồ sơ+16tham chiếu module có chồng lặp,0toàn tác phẩm đã áp hết. Phạm vi liên quan của P08 không tăng số trang đã đọc.

Snapshot trước thay đổi ở archives/v53-before-home-fuduan:5tệp đã đối SHA, manifest5.646tệp và sourceZIP2.949.955.032byte. HTML707.411byte/site/index.html/ZIPweb giữ nguyên. Gói nguồn được cập nhật cùng báo cáo/trạng thái; kết quả chuẩn bị trong QA chỉ được coi là kiểm phát hành khi lệnh --no-write hoàn tất.

Lệnh kiểm chỉ đọc (Python có pypdf/PIL):

    python v53/scripts/verify-home-fuduan-sources.py --no-write
    python v53/scripts/verify-home-fuduan-release.py --no-write

Các phần còn mở: nghĩa 辰/四殺沒時 của ITKC, gốc nguyên và hàng 日 của bảng, các chú cát hung, phần còn lại của107trang, cùng các quy tắc nhật/thời luận khác. Nghiên cứu này không khép toàn kho.
