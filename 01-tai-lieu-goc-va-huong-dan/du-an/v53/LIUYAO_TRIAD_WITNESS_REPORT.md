# Tam hợp: giữ dị bản một/ba hào động theo từng nguồn

29/10/2026. Đối thêm đúng khoảng chữ còn mở; không sửa bản NLC và chưa lập bộ thành cục hoàn chỉnh.

Bản NLC416-12jh005345-45344 tại vị trí78 ghi 一卦之內有一交動而合局者一也. Ảnh Cục Lưu trữ Quốc gia Nhật Bản, hồ sơ4756814/増刪卜易２, canvas8 ghi câu tương ứng 一卦之內有三交動而合局者一也. Hai bản khác 一/三. Giữ chữ 交 trong bản đọc ngoại giao; nhãn hào dùng 爻 là phép chuẩn hóa theo đúng ngữ cảnh, không thay chữ hàng loạt. Đường dẫn nguồn Nhật: https://www.digital.archives.go.jp/item/4756814 ; mã lưu trữ 子０５９－０００８-0002.

Đã đối chọn ba tọa độ: câu thứ nhất khác số một/ba; câu hai hào động/một hào không động và câu một minh động/một ám động được tính hai động cùng đọc trong hai bản. Chưa nhận rằng cả hai bản giống nhau mọi chữ hoặc truyền bản độc lập về phả hệ. Bộ ảnh Nhật đã có metadata trong kho từ phạm vi trước; lần này thêm bốn ảnh của cùng hồ sơ đã biết, không phải thêm một sách hay một bản in độc lập mới được định danh.

## Nguồn ảnh và giới hạn độ phân giải

Tái dùng metadata/manifest53canvas đã giữ. Bốn URL tài nguyên đúng trong manifest trả HTTP200, TLS authorized=true quan sát tại socket, lưu nguyên response/headers/SHA/UTC. Canvas3và26chỉ giúp định vị nội dung;8và9là khoảng đích. Cả bốn đã xem tổng quan, không nhận53canvas đã đọc. Canvas49bị403ở phạm vi trước không được thử lại hoặc đổi đường dẫn để vượt chặn.

URL tài nguyên ghi full/max/native nhưng ảnh thực nhận3000×2073, khác kích thước6150×4250trong manifest. Giữ rõ DIMENSION_AUDIT.json: đây là JPEG dịch vụ cung cấp, không có JP2 gốc hoặc PDF mới, không nhận ảnh đầy kích thước gốc. Ba crop cuối đã xem ở kích thước nguồn nhận được và đối RGB; một crop thử thiếu lề phải được giữ và loại trước freeze. NLC78được đọc lại từ ảnh đã giữ,0vị trí NLC mới.

REQUESTS.json có trường ngày đầu container27/10do mẫu fetch cũ ghi cố định; bốn retrievedUTC thật đều29/10. REQUEST_DATE_AUDIT.json nêu lỗi nhãn này; giữ nguyên ledger đã đóng băng và byte response, không sửa ngầm để tạo lịch sử đẹp. Không có tải mới ngày27/10trong phạm vi này.

## Phần phát triển cụ thể

witness-triad-reference.mjs yêu cầu chọn sourceID. Bản Nhật có phép nhận diện ứng viên tọa độ rất hẹp: ba thành viên Tam hợp đều là hào gốc minh động, đúng ba thành viên này, và các hào gốc còn lại được khai báo rõ không hoạt động. Có hào khác động/ám động hoặc chưa rõ hoạt động thì giữ chưa xác định. Đây là một tập con bảo thủ dựa câu 三交動, chưa chốt mọi nghĩa của câu ấy; ba hoạt động có một ám động chưa được tự đồng nhất với tập con ba minh động này.

Với sourceID NLC, câu 一交動 và cách hiểu số đếm vẫn chưa phân xử, không đổi sang ba. Mô-đun NLC, map137đơn vị và engine giữ nguyên SHA. Các cấu trúc mode2/hào biến/nội ngoại đã có được tái dùng; không đưa ngưỡng B03 sang B02.

Ứng viên tọa độ không là cục có hiệu lực: effectiveFormation/transformedElement/calendarEpoch/practicalOutcome vẫn null. Các đoạn chờ ngày tháng bổ túc, điền thực 空破 và xung khai nhập mộ được giữ; chưa có adapter tính ngày hoặc thứ tự ưu tiên để suy ứng nghiệm. Khung thiếu sourceID hoặc gán lịch/đổi số đếm tùy ý bị từ chối.

## Engine thật, ca kiểm và bảo toàn

Năm tệp bản đọc/kỳ vọng/nguồn đóng băng trước triển khai. Chín ca kỳ vọng được ghi trước viết hàm và trước chạy engine. Ví dụ tổng hợp [6,8,6,8,6,8] có quẻ gốc Khôn2, biến Ký Tế63, các hào1/3/5động; chi gốc từ dưới 未/巳/卯/丑/亥/酉. Hai lần gọi HHC_ENGINE.hexNumber thật xác nhận hai mã quẻ so với phép chiếu cấu trúc. Đây là ví dụ tổng hợp,0quẻ in trong sách mới, không phải chứng minh phép Tam hợp hoặc kết quả tiên đoán. ACTUAL_RUNTIME.json giữ hai lần thực thi; script một lần từ chối ghi đè hồ sơ đã có. Test/QAđọc lại payload, không gọi HHC lặp.

Tám nhóm kiểm đạt:9ca kỳ vọng,64mẫu động tổng hợp,4khung nguồn không hỗ trợ,7đầu vào sai,3khung điền thực/nhập mộ/chưa biết,5tệp freeze giữ SHA.27tệp staging được đưa vào research/liuyao-triad-witness/ và đối byte/SHA. Module triển khai chỉ đổi đường dẫn import so với bản staging được giữ;6phụ thuộc nguồn/map/engine không đổi.

Snapshot trước thay đổi tại archives/v53-before-liuyao-triad-witness/ giữ năm tệp đã đối SHA,manifest5.733tệp/sourceZIP3.039.699.952byte. HTML707.411byte/site chỉ index.html/ZIPweb nguyên byte. Nguồn, suy luận và QA ở ngoài site. Danh mục40hồ sơ+16tham chiếu chồng lặp,0toàn tác phẩm áp hết; B02vẫn137khoảng đọc đầu/0đơn vị áp trọn. Không đổi các mốc lịch sử hoặc tự nâng trạng thái cả chương.

Lệnh kiểm chỉ đọc (Python có PIL):

    python v53/scripts/verify-liuyao-triad-witness-sources.py --no-write
    python v53/scripts/verify-liuyao-triad-witness-release.py --no-write

Payload chuẩn bị chỉ là kỳ vọng đóng gói; xác nhận cuối cần --no-write hoàn tất sau tạo ZIP. Các việc còn mở: ngữ nghĩa trọn mode1ở mỗi bản, phối hợp minh/ám/hào biến, căn khí/vượng suy, điền thực/nhập mộ, hào Dụng/Thế và thứ tự ưu tiên. Dị bản rõ hơn giúp chọn mô hình nghiên cứu đúng nguồn, chưa khép toàn Tam hợp hoặc toàn kho.
