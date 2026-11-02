# Tử vi: đọc liên cung và nhãn trạng thái sao

Ngày 26/10/2026. Tách ba lớp: vị trí tính được, bảng truyền bản được chọn, và lời gợi mở do biên tập.

- Tam phương tứ chính: cung đang đọc, hai cung cách bốn/tám địa chi và cung đối diện cách sáu. Mã thực thi đối chiếu `iztro@2.6.2` đã lưu trong V46; xem `lib/astro/analyzer.js`, `FunctionalAstrolabe.js`, `FunctionalSurpalaces.js`. Tài liệu chính thức: https://docs.iztro.com/en_US/learn/astrolabe và https://docs.iztro.com/posts/star . Không tải lại gói đã có.
- Bảng trạng thái 14 chính tinh ×12 địa chi: chọn đúng `lib/data/stars.js` của gói trên, hàng bắt đầu tại Dần, đổi sang chỉ số vật lý Tý của HHC bằng `(chi-2) mod12`. Có bảy nhãn, không quy thành điểm tổng. Đây là một bảng được định danh, không phải chứng minh mọi cổ bản nhất trí.
- Tái đọc hai ảnh đã lưu `research/fortune-table/official-088.jpg` và `official-089.jpg`;088 nửa trái là bảng sáu chi Tý–Tỵ,089 nửa phải là Ngọ–Hợi. Đọc các nhóm chữ viết tắt vào `tuvi/MANUAL_BRIGHTNESS_GROUPS.json`, không dùng bảng phần mềm điền ô thiếu. Sau đó lấy thêm hai phản hồi `/full/full/` để đọc sáu chỗ chưa rõ: canvas công bố6300×4750 nhưng **JPEG thực nhận chỉ3000×2262**, không gọi là ảnh6300px hoặc JP2master. URL/byte/SHA/TLS trong `tuvi/HIRES_RESPONSES.json`.
- Phân loại168vị trí chính tinh×chi: **162ô gán được một hàng rõ,1ô in mâu thuẫn hai hàng,5ô chưa thấy chữ sao tương ứng**. 15/162 ô rõ khác bảng iztro đang chọn;147khớp. Ảnh rõ thêm giải quyết梁 ở Mão–Miếu; 破 tại Mùi in ở cảMiếu vàVượng nên không tự chọn một hàng. Không coi5ô không thấy chữ là sao không tồn tại hoặc mặc định Bình. Ở Ngọ, hàng得地 có相 còn bảng iztro xếp Miếu. Giữ các khác biệt, chưa thay bảng bằng một nhân chứng đơn lẻ.
- Văn bản số Toàn Thư quyển3 có nhiều chỗ dùng 三方四正; nó không đủ làm bằng chứng cho lời khẳng định sự kiện đời sống. Bản số: https://zh.wikisource.org/wiki/紫微斗數全書/卷三 . Chỉ dùng để định vị chủ đề; các lần đọc ảnh/can Canh/Nhâm/khởi hạn đã được định danh riêng trong `FORTUNE_WITNESS_REPORT.md`.
-22 lời đọc hai chính tinh cùng cung là biên tập theo các chủ đề đã có của14sao, không phải trích phú, bản dịch hoặc kết luận cách cục cổ truyền. Chỉ hiện khi cả hai thực sự ở cùng cung. Không gom sao từ cung tam hợp thành đồng cung, không chuyển sao khi vô chính diệu.

## Dị bản chưa hợp nhất

Can Canh của ảnh cơ quan cho Đồng Khoa/Tướng Kỵ, còn bảng đang dùng là Âm Khoa/Đồng Kỵ. Nhâm ảnh ủng hộ Phủ Khoa, iztro mặc định dùng Tả Phù. Lời cổ bản khởi đại hạn từ cung kề khác mô hình hiện tại khởi tại Mệnh theo cục. Các trường hợp này là những truyền bản khác nhau; chưa đủ căn cứ chọn một công thức chung để thay mọi bảng.

Không thêm lựa chọn khởi từ cung kề khi chưa phân định tuổi khởi, thứ tự cung và trường hợp đồng hạn. Không gọi việc bảo tồn dị bản là đã giải quyết dị bản. Mô-đun mới không thay `engine.js`, `fortune.js` hoặc các khoảng hạn hiện hành.

## Kiểm chứng

`scripts/verify-full-study-engine.mjs` thực thi iztro thật trên144lá số, kiểm hình học theo chỉ số vật lý, độ phủ trạng thái và tính bất biến lá số. Kết quả số thực trong `qa/full-study/ENGINE_RESULTS.json` được tạo sau khi chạy, không lấy số dự kiến làm số đã đạt. Các hash tệp được ghi trong `TUVI_SOURCE_FILES.json`.

## Bổ sung sau các mô-đun ban đầu

Đã đọc bốn đoạn mục tiêu trong ba ảnh cơ quan90–92, kiểm14điều kiện đồng cung và thêm bối cảnh sao gốc vào kết quả vận hạn. Xem `../../FORTUNE_CONTEXT_REPORT.md` và `../fortune-context/MANUAL_READINGS.json` cho ngữ cảnh khác chữ/bảng và giới hạn. Cùng một bản in, không coi đây là nhân chứng độc lập giải quyết15ô khác hoặcCanh/Nhâm.
