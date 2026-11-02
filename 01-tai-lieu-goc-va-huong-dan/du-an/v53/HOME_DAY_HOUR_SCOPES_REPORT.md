# Nhà ở — mẫu ngày khai báo và điều kiện giờ theo nguồn

29/10/2026. Phạm vi nghiên cứu nội bộ: hai hàm mới, chưa nối vào kết quả người dùng.

Đối ảnh nhật luận và thời luận cho thấy không thể dùng một nhãn ngày/giờ rồi áp cùng danh sách việc kiêng cho mọi sách. Bản số còn có chữ làm đảo nghĩa câu: ảnh ghi **並忌此日**, bản số ghi **並起此日**. Hồ sơ mới giữ chứng cứ và cách đọc riêng, kiểm các điều kiện đã khép, để tránh tạo lời cho phép từ một lỗi chép hoặc từ sự im lặng của nguồn.

## Chuỗi nguồn và bản đọc

Từ ba bản số đã lưu ở phạm vi tổng luận, đọc metadata công khai của cơ quan ITKC: 日論 node `ITKC_GO_1508A_0020_000_0070` nối ảnh247–253; 時論 node `ITKC_GO_1508A_0020_000_0090` nối255–256. Theo navigation imgNext của viewer để lấy tiếp. Giữ17bodyHTTP200 qua TLS thường: hai metadata, bảy navigation chỉ đọc và támJPEG1640×2180 mới248–253/255–256. Tái dùng ảnh247 đã có từ nguyệt luận, không tải lại. URL/header/byte/SHA-256 giữ trong REQUESTS, nguồn bản số và ảnh247 tái dùng có băm riêng. Một lần gọi WindowsPowerShell5 bị lỗi tham số cục bộ trước yêu cầu mạng; sửa sang PowerShell hiện hành rồi thành công, giữ lỗi, không bỏ TLS hoặc vượt chặn.

Đã xem đủ chín vị trí, gồm tám mới và một tái đọc; lập18xử trí cấp mục ngày và4mục giờ. Đây cùng tác phẩm liên quan選擇要略; không thêm tác phẩm, master/container gốc hay ấn bản độc lập củaP08. Niên đại/copy khắc gốc vẫn chưa xác định từ metadata; copyright số2016/mãXML2017 không phải năm khắc được xác minh.

Tám crop cuối đã xem và khớpRGB; chín crop thử bị loại khỏi chứng cứ cuối. Sau lần kiểm đầu phát hiện lề trên tiêu đề旬中còn cắt đầu chữ, đã mở rộng lề và kiểmRGB/xem lại. Giữ `NATIVE_CROPS.json` và ảnh cũ trong mốc băm trước triển khai, dùng `NATIVE_CROPS_REVISED.json` làm bộ chứng cứ cuối, ghi `CROP_MARGIN_CORRECTION.json`. Thay lề không đổi chữ, ca kỳ vọng, module hay thực thi hàm; ảnh đầy đủ đã được đọc trước đó. Bộ đóng băng không bị viết lại.

## Những khác biệt có tác động

| Chỗ đọc | Ảnh | Bản số/nguồn liên quan | Xử lý |
|---|---|---|---|
| 天地轉殺, ảnh247 | 並忌此日 | 並起此日 | Giữ lỗi chép số riêng; không biến thành phép khởi công |
| Mục cuối nhật luận, ảnh253 | Tiêu đề刑隔, thân câu州隔 | Tiêu đề/thân số州鬲 | Giữ cả biến thể nội tại ảnh và chuẩn hóa số, chưa chọn chữ thắng |
| 用時法, ảnh256 | 日中空亡 | Số giữ日; chú giải cơ quan đề nghị旬 | Buộc chọn cách đọc rõ nếu xét lời ưu tiên chung đối với旬中 |
| 截路空亡, ảnh255 | Kiêng納表進章出行遠迴;修造安葬không tránh | P08kiêng出行嫁娶移徙,餘皆不忌 | Giữ hệ nguồn riêng; không sao danh sách hôn nhân/dời nhà từP08sangITKC |

Các khẳng định ứng nghiệm, hỏa hoạn, tổn hại, nghi thức trong nguồn được phân loại để nghiên cứu lịch sử; chưa là kết quả thực nghiệm hoặc hành động khuyến nghị trên web. Không coi các sách vô danh được dẫn trong một đoạn là sách độc lập vừa có byte gốc.

## Hàm và điều kiện

`sourceDeclaredDayPattern` chỉ trả mẫu nguồn có khớp hay không:

- 天地轉殺: bốn bộ mùa/tháng/chi được in: xuân2卯, hạ5午, thu8酉, đông11子. Mùa và tháng đều phải khai báo; không suy một trường từ trường kia.
- 天賊: đúng ba quan hệ **孟月滿日 / 仲月破日 / 季月開日**. Không tự xác định孟仲季hoặc trực ngày từ lịch. Truyện天狗明星守護 và điều kiện天狗下食時 được ghi riêng; không tự tính ngoại lệ.

Nguồn ngày dùng khung khai báo rõ. Các gốc tháng âm số/tiết khí/không biết trảnull, chưa tự nối tháng nhuận hay ranh mùa. Không khớp một mẫu không trở thành “ngày tốt”; kết quả cho mọi hoạt động và ngày tổng thể vẫnnull.

`sourceHourParagraph` giữ hai lớp riêng: điều kiêng của đoạn gọi tên và lời ưu tiên có điều kiện trong用時法. Các hoạt động nói rõ ở截路và旬中được trả theo đoạn; hoạt động không nói tới vẫnnull. Cách đọc “日” in sẵn hoặc “旬” do chú giải được khai báo riêng. Lời ưu tiên chỉ được ghi khi caller xác nhận **toàn bộ ngữ cảnh四大吉時/黃道吉星/吉神到時**, không suy ANY/ALL hoặc tính các sao từ API này. Vị từ ưu tiên riêng không tự xóa điều kiêng: kết quả hợp nhất/khuyến nghị tổng thể luônnull vì thứ tự và các hệ tính chưa được giải đầy đủ.

Đoạn造葬修方用時 còn giữ通天竅/走馬六壬/天罡,吉神到山到向và tham chiếu修方依前例; chưa tạo lịch sao hoặc thuật toán chọn giờ từ những tên gọi đó. Không có adapter giờ địa phương, múi giờ nguồn, Tý sớm/muộn hoặc phép chuyển từ nhãn sang giờ đồng hồ mới.

## Thực thi và kiểm chứng

Đóng băng36tệp cùng28ca kỳ vọng trước triển khai và lần kiểm đầu. Cả28ca kỳ vọng giữ nguyên; hiệu chỉnh sau kiểm chỉ là lề crop tiêu đề. Bảy nhóm kiểm đạt:3.588khung mẫu ngày,594khung giờ,2.691khung sai gốc thời gian giữ chưa xác định,20đầu vào sai/thiếu/thêm trường hoặc suy ngang quy tắc bị từ chối. Kiểm immutability/SHA của mốc băm và bảo toàn kết quảnull ở giới hạn.

Đã thực thi15lần hàm P08hiện có `sourceJieluActivityScope`, ba trạng thái×năm hoạt động để so phạm vi nguồn. Ghi rõbuild/burial được ánh xạ vào “other” củaAPIcũ; kết quả đó là phạm vi hàm cũ, không bao trọn mọi quy tắcP08. Khi đã khai báo截路, P08cho kiêngmarriage/relocation, ITKCđể hoạt động đó chưa được đoạn này nói rõ;travelcùng được nói tới. Không chọn nguồn thắng hoặc chứng minh hai hệ tính cùng tên là đồng nhất.

Kế hoạch vàSHA moduleP08giữ trước batch;15kết quả thực thi được lưu. Các kiểm sau chỉ đọc cache,0lần gọi lạiP08,0đối tượnglịch,0chartHHCvà0iztromới. Không cần tạo lá số Tử vi để kiểm một danh mục thao tác nhà ở.

```powershell
node v53/research/home-day-hour-scopes/test-reference.mjs --no-write
python v53/scripts/verify-home-day-hour-scopes-sources.py --no-write
python v53/scripts/verify-home-day-hour-scopes-release.py --no-write
```

## Độ phủ và phát hành

Hai mẫu ngày và phạm vi điều kiện giờ chưa áp hết22mệnh đề. Mười sáu mục nhật luận khác vẫn cần khép:白虎theo vị trí sảnh,伏斷với克và四殺沒時,正/傍四廢,火星và các隔theo công việc. Danh sách chi/ngũ hànhnạpâm/trực/sao ở火鬲/水鬲/地鬲không được tự thay bằng AND/OR chưa xác minh. Lịch nguồn, lớp ưu tiên, toàn bộ các trường hợp hoạt động và bằng chứng hiệu lực đều còn mở.

Bản5570tệp/sourceZIP2.928.966.046byte trước phạm vi đã được sao và kiểmSHA ở`archives/v53-before-home-day-hour-scopes/`. V53cũ giữbyte ngoài năm tài liệu trạng thái được nêu trong verifier. HTML707.411byte/sitechỉindex.html/ZIPweb giữ nguyên; nguồn/corpus/suy luận/QA ngoài site. Toàn kho40hồ sơ+16tham chiếu có chồng lặp vẫn đang khai thác;0toàn tác phẩm đã áp hết. Bản Kiến Lộc chờbrowserQAdoWorktắt browser; không tự phát hành ứng viên chưa kiểm.
