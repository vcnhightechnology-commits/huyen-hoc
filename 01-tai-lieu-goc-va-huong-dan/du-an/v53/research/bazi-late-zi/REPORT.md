# Can giờ Tý muộn: đã xác định cơ chế sai khác, chưa hợp nhất quy ước

> Mốc tiếp theo đã hoàn thành: `../../BAZI_LATE_ZI_OPTION_REPORT.md` có ảnh sách chỉ dẫn trực tiếp và hai ví dụ, lựa chọn can giờ tách riêng cùng kiểm tương thích hồ sơ. Báo cáo này và VERIFICATION.json giữ nguyên chứng cứ của bộ tính trước cải tiến; 3.720 khác biệt của mặc định vẫn có hiệu lực. Không chạy script audit hash của mốc cũ trên engine mới để suy ra có hồi quy.

26/10/2026. Nghiên cứu nội bộ, không thay sản phẩm và không tải lại nguồn. Phạm vi tiếp theo của `../../BAZI_RELATION_LOCATIONS_REPORT.md`.

## Điều đã xác định

Tại 09/08/2018 23:30 UTC+8, với ngày trụ đổi lúc 00:00, HHC tính ngày Quý Dậu và giờ Nhâm Tý; lunar-typescript 1.8.6 sect2 tính cùng ngày Quý Dậu nhưng giờ Giáp Tý. **Đây là hai chính sách can giờ khác nhau**:

- HHC lấy can giờ từ can của ngày trụ đang chọn. Chọn 00:00 thì 23 giờ vẫn dùng can ngày hiện tại; chọn 23:00 thì dùng can ngày kế tiếp.
- [Tài liệu chính thức của lunar](https://6tail.cn/calendar/lunar.bazi.html) nói cả hai sect đều lấy trụ giờ của ngày kế tiếp trong Tý muộn; sect chỉ đổi cách lấy ngày trụ. Tệp triển khai 1.8.6 thực tế cũng dùng `dayGanIndexExact` để tính can giờ, không dùng biến ngày nửa đêm `dayGanIndexExact2`.
- Test upstream đã giữ có mẫu 15/02/1988 23:30: sect2 ngày Canh Tý, sect1 ngày Tân Sửu, cùng giờ Mậu Tý. Chạy lại bản đã cài cho đúng kết quả đó. Không phải chỉ dựa vào mô tả hoặc mã giả.

Tài liệu và test upstream là chứng cứ về **quy ước của phần mềm**, không tự chứng minh phần mềm là truyền thống duy nhất đúng. Hai thư viện cùng họ cũng không là hai nguồn lịch độc lập.

## Đoạn sách đã đọc và giới hạn

Tái dùng bản chép số WYG Tam Mệnh Thông Hội quyển 2, commit Kanripo `7db72e5553de6ee4c45ed3980c6c67f8a6e451bf`:

| Mã trang | Nội dung đọc | Kết luận được phép |
|---|---|---|
| `002-43b`, 論時刻 | Nửa đầu giờ Tý trước nửa đêm thuộc ngày trước; nửa sau sau nửa đêm thuộc ngày hiện tại. | Sách có phân hai nửa giờ Tý theo ngày. Chưa phải một công thức ngoại lệ riêng cho can giờ 23 giờ. |
| `002-57b`–`002-58a`, 論遁月時 | Dẫn can ngày để khởi can giờ, đủ năm nhóm của phép ngũ thử độn; ví dụ Giáp Tý ngày/giờ. | Công thức thông thường được ghi rõ; đoạn này không trực tiếp nói lúc nửa đầu giờ Tý phải dùng can ngày trước hay ngày sau khi khởi giờ. |

Ba mã trang mới đọc là **văn bản số, chưa đối ảnh bản WYG**. Kết hợp hai đoạn thành một quyết định duy nhất về can giờ Tý muộn vẫn là bước suy luận. Không biến sự im lặng của đoạn thường thức thành bằng chứng bác bỏ hoặc chứng minh ngoại lệ. Giữ nguyên dạng chữ trong tệp nguồn, không tự sửa chữ 巳/己 trong câu vè rồi coi đó là một dị bản đã hiệu khảo.

## Phạm vi chạy thật

`VERIFICATION.json` ghi đầy đủ đầu vào, cả hai kết quả, định danh runtime và hash nguồn; script `../../scripts/audit-bazi-late-zi.mjs` tái tạo được.

- 60 ngày liên tiếp từ 09/08/2018, phủ cả chu kỳ 60 ngày; thêm 31/12/2019 và 29/02/2020 để bao gồm cuối năm/ngày nhuận.
- Mỗi ngày có 64 thời điểm: toàn bộ **23:00–23:59** và 00:00, 00:59, 01:00, 22:59. Chạy cả hai chính sách ngày HHC và sect tương ứng của thư viện tại UTC+8: **3.968 lần dựng Solar/EightChar thật, 7.936 phép so lá số**.
- Ba trụ năm/tháng/ngày khớp trong cả 7.936 phép so. Chính sách đổi ngày 23 giờ khớp cả trụ giờ 3.968/3.968. Chính sách nửa đêm khớp 248 mốc đối chứng và khác trụ giờ ở đủ 3.720 mốc 23 giờ; không gọi các mốc khác là kiểm khớp.
- Các sai khác phủ đủ mười can ngày, cùng chi Tý và can giờ thư viện tiến hai vị trí trong vòng mười can so với HHC. Đây là hệ quả của việc dùng can ngày kế, không phải chênh múi giờ được tự sửa.
- **9/9 kiểm nghiên cứu đạt.** Những kiểm này xác nhận cả sự khớp lẫn sai khác dự kiến, không nâng số 37 kiểm sản phẩm thành bằng chứng tất cả lá số giống thư viện. Không suy rộng sang mọi niên đại/múi giờ.

## Quyết định tích hợp

Chưa thay `engine.js` hoặc đầu vào người dùng. Cần nhân chứng ảnh/đoạn chú nói trực tiếp cách khởi can giờ ở hai nửa Tý, phân biệt tác giả/niên đại/truyền bản; nếu thêm lựa chọn can giờ, phải mô tả ý nghĩa cho người dùng và kiểm tương thích hồ sơ cũ, Thập thần, đại vận, chưa rõ giờ. Không âm thầm đổi lá số đã lưu hoặc gọi sect2 của thư viện là tương đương hoàn toàn với tùy chọn nửa đêm hiện có.

Kết quả nghiên cứu này giải thích chính xác nguồn sai khác và khoanh vùng kiểm thử. Vấn đề hợp nhất quy ước và toàn bộ bốn hướng nghiên cứu vẫn mở. Byte nguồn tái dùng ở `VERIFICATION.json.sources`, runtime ở `.runtime`; nguồn gốc tải ban đầu ở `../full-study/bazi/SOURCE_MANIFEST.json` và audit nguồn trước. Không có lần tải sách mới trong phạm vi này.
