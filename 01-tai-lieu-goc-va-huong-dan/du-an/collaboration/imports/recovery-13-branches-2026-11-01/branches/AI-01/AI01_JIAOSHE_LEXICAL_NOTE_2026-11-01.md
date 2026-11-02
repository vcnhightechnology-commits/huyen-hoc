# AI-01 — ghi chú đối chiếu từ ngữ 交涉

**Ngày:** 01/11/2026 · **Trạng thái:** tìm được một ngữ cảnh song hành trong cùng tác phẩm; chưa tìm được định nghĩa thao tác.

## Đoạn đang xét

Trong 《三命通會》 WYG quyển 3, tờ 003-44b, đoạn Chính Ấn ghi `得土印支干有交涉者名官印無交涉者名鬼印`. Đây là một mệnh đề phân loại: nếu có `支干有交涉` thì gọi Quan Ấn, nếu không thì gọi Quỷ Ấn. Câu không nêu rõ các trụ nào được so với nhau hoặc quan hệ nào đủ điều kiện.

## Song hành trong cùng tác phẩm

WYG quyển 2, tờ 002-100b, trong đoạn bàn 六合 và lời dẫn `廣録`, ghi `更得天干納音有交涉尢吉` (bản văn dùng chữ `尢`; chuẩn hóa thành `尤` nếu trích dẫn phải được đánh dấu biên tập). Câu này nằm sau danh sách quan hệ chi/Can–Ngũ hành/Nạp âm và cách gọi 隔六合, rồi chuyển sang 合祿、合馬、合貴. Tệp `v53/research/bazi-branch-union/CHAPTER_CLEAN.txt` chứa cùng đoạn; đó là bản trích cùng vị trí TMTH, **không** tính thêm witness độc lập. Trạng thái nghiên cứu M01 tại `v53/research/bazi-branch-union/WORK_STATE.json` đã ghi rõ không tự động hóa cách hiểu của cụm 納音交涉; ghi chú này không thay đổi M01.

## Điều quan sát được và điều chưa thể suy ra

- Trong ngữ cảnh quyển 2, `交涉` có thể mô tả một dạng liên hệ giữa thiên can và Nạp âm trong hệ luận hợp. Điều này khiến cách hiểu rộng “có tương quan/liên hệ” là một giả thuyết từ vự cảnh có cơ sở hơn việc gán nghĩa thuật ngữ hiện đại quá hẹp.
- Quyển 3 lại ghép `交涉` với `支干`, trong lời phân biệt Quan Ấn/Quỷ Ấn. Hai vị trí dùng cùng từ trong một tác phẩm không chứng minh hai phép có cùng toán tử hoặc cùng tập đầu vào.
- Chưa có câu nào trong các đoạn đã đối chiếu chỉ rõ phải xét trụ năm với trụ ngày, can với chi cùng trụ, quan hệ sinh-khắc-hợp, hay tất cả cặp can-chi. Hai ví dụ WXJJ giúp khảo sát nhưng không đủ để chứng minh tính cần/đủ của một predicate.
- Vì vậy chưa đặt ra một hàm `jiaoshe()`, chưa dùng bảng hợp để nhận dạng, và chưa biến nó thành điều kiện phân loại trong engine.

## Kiểm tra byte và giới hạn

Các câu TMTH nằm trong hai tệp local đã khớp `MANIFEST.json` tại lần kiểm AI-01: `KR3g0042_002.txt` (123.566 byte, SHA-256 `b0f9badc8aff64ee137392277eb2f7a428c39a9d8c9faa3154f79c626c2131b4`) và `KR3g0042_003.txt` (118.504 byte, SHA-256 `267fda36d206bfd153d9377441adb5f99f96c39a594a5f7ebdf3e4dd226e9b87`). Bằng chứng hiện là văn bản WYG đã giữ trong dự án; lượt này không xác minh ảnh gốc WYG.

## Hướng tiếp tục

Tìm thêm câu dùng `交涉` trong cùng tác phẩm/nguồn được dẫn và khảo sát đầy đủ hai ví dụ WXJJ theo từng quan hệ cụ thể. Chỉ có thể lập định nghĩa máy khi nguồn nêu phạm vi cặp được xét và điều kiện đủ rõ; nếu không, giữ nội dung ở dạng giải thích lịch sử có dẫn đoạn.
