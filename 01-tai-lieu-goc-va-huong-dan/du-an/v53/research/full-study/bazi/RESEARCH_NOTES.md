> Bổ sung hiện hành: ngày chưa rõ giờ nay có cận sớm/muộn qua đủ1.440phút, xem `../../../BIRTH_HOUR_RANGE_REPORT.md`. Vẫn không dựng giờ sinh hoặc một mốc duy nhất; các mẫu0/6/12/18/23h được nêu dưới là minh họa của đợt trước.

> Phạm vi mới 26/10/2026: `../../../BAZI_RELATION_LOCATIONS_REPORT.md` ghi vị trí Thập thần ở can lộ/tàng can và sửa lời đọc bị mất trong TXT/in khi thu gọn; 37/37 kiểm chính, 240 lá số thật/3.020 vị trí. Đọc thêm bốn đơn vị trên ảnh Uyên Hải 109–111 đã lưu, 11 cặp quan hệ, hai mệnh đề WYG chưa đối ảnh. Sai khác can giờ Tý muộn 23:30 HHC/lunar sect2 giữ riêng trong `../../bazi-relation-locations/RUNTIME_COMPARISON.json`; không đổi engine hoặc hoàn tất cách cục.

> Cập nhật mới nhất: `../../../BAZI_LATE_ZI_OPTION_REPORT.md` đã tìm được nhân chứng ảnh trực tiếp NCL-000002203, thêm lựa chọn can giờ Tý muộn theo ngày kế nhưng giữ mặc định/hồ sơ cũ; 97/97 kiểm chính. Các ghi chú chưa tìm được ảnh hoặc engine chưa đổi ở những mốc trước giữ giá trị lịch sử. Ma trận cách cục vẫn chưa hoàn tất.

# Bát tự: đại vận và giới hạn khi đọc nguyệt lệnh

Phạm vi hiện hành: `../../../BAZI_MONTH_STEMS_REPORT.md` giữ đủ can tháng, Thập thần và can lộ ngay trong phần nguyệt lệnh; 91 kiểm chính đạt. Ảnh quyển 5 CADAL06066041 thêm10mệnh đề mục tiêu/ba mục, 16 cặp can ngày–chi tháng; bốn Chính Quan ở can khác bản khí đã được kiểm runtime và giữ rõ. Đây là phạm vi đối ảnh cụ thể, không sửa các tệp chép số gốc hoặc nhận toàn chương đã hiệu khảo. 68b “không có Thực” vẫn chưa có ảnh trong phạm vi mới vì HTTP429 trang138. Ma trận đọc có bổ sung imageCollation để tránh lặp.

Ngày rà: 26-10-2026. Tài liệu nội bộ, không đưa vào thư mục site phát hành. Đây là phạm vi đã kiểm chứng về phép tính và các đoạn sách nêu dưới, không phải hiệu khảo xong toàn bộ Tam Mệnh/Uyên Hải hay chứng minh dự báo đời người.

## Kết quả có thể tích hợp

- Lập hướng và chuỗi đại vận theo âm dương **can năm trụ**, giới tính quy ước của phép an vận, **tháng trụ theo tiết**. Dương nam/âm nữ thuận; âm nam/dương nữ nghịch. Không dùng năm âm lịch đổi vào Tết để thay năm trụ đổi tại Lập Xuân.
- Tính khoảng thời gian thực tới **tiết** mở tháng tiếp theo khi thuận, từ tiết trước tới giờ sinh khi nghịch. Đây là 12 tiết mở tháng, không lấy 24 tiết khí hoặc ngày mùng một âm lịch.
- Giữ số lẻ năm/tháng/ngày/giờ khởi vận. Không làm tròn 1 năm 8 tháng thành 2 tuổi.
- Mỗi đại vận tiến/lùi 1 can chi tính từ tháng trụ, dài 10 năm theo quy ước. Đoạn sinh tới khởi vận là đoạn riêng, không gán luôn can chi tháng trụ thành đại vận thứ nhất.
- Trình bày nguyệt chi, bản khí/tàng can và thập thần; chỉ ra can tàng nào lộ ở can năm/tháng/giờ. Việc các quan hệ ấy hiện diện chưa đủ để xác nhận cách cục, hỷ kỵ hoặc dụng thần.

## Căn cứ sách đã đọc cụ thể

Nguồn văn bản: Tam Mệnh Thông Hội 三命通會, Minh Vạn Dân Anh, bản WYG do Kanripo chép số, commit `7db72e5553de6ee4c45ed3980c6c67f8a6e451bf`. Đã đọc văn bản có mã trang, chưa đối chiếu ảnh WYG của toàn bộ các đoạn. Khi dẫn phải gọi là bản chép số WYG; không mô tả thành đã đọc ảnh nguyên bản của mọi trang.

Quyển 2: `../../four-items/sources/KR3g0042_002.txt`, SHA-256 `b0f9badc8aff64ee137392277eb2f7a428c39a9d8c9faa3154f79c626c2131b4`.

| Mã trang WYG | Đoạn đã đọc | Ý nghĩa và ranh giới áp dụng |
|---|---|---|
| 002-66a–66b, 論大運 | “大運則一辰十嵗折除以三日為年”; “陽男隂女大運以生日後未來節氣日時為數順而行之”; “隂男陽女大運以生日前過去節氣日時為數逆而行之” | Cơ sở hướng vận, tỷ lệ 3 ngày/1 năm và một vận 10 năm. Việc chọn đúng 12 tiết được đối chiếu thêm với API/triển khai thư viện, không tự đọc chữ 節氣 thành mọi mốc trong 24 tiết khí. |
| 002-67a | “今人行運多用約法論以一嵗竒八月起運便以二嵗殊不明折除實厯之數也” | Nguồn phản đối việc bỏ phần lẻ khi báo tuổi khởi vận. |
| 002-67b–68a | Một thời thần dư/thiếu quy ra một tuần 10 ngày; “從此…後十週年方換一運” | Còn có bàn về tháng đủ/thiếu và tháng nhuận theo lịch truyền thống. Không tuyên bố cách cộng lịch dương của thư viện tái hiện mọi chi tiết này. |
| 002-56b–57a, 論五行旺相休囚死並寄生十二宫 | “見生旺者未必便作吉論見休囚死絶未必便作凶言如生旺太過宜乎制伏死絶不及宜乎生扶妙在識其通變” | Vượng không tự động là tốt, suy không tự động là xấu. Không chuyển 12 trường sinh thành điểm số may mắn hoặc lời dự báo tai nạn/sức khoẻ. |
| 002-59b, 論年月日時 | “以日干為主却以年月時合㸔生尅制化旺相休囚取立格局” | Cần toàn cấu trúc, không chỉ đếm hành hoặc chỉ xét một bản khí nguyệt chi. |
| 002-33a–36a, 論人元司事 | Các bảng phân nhật khí khác nhau; trang 35b–36a chất vấn “豈可以幾日為限哉” | Phải tách **tập hợp tàng can cố định** khỏi **bảng tư lệnh theo số ngày**. Không lấy số ngày 5/7/18 thành tỷ lệ khí duy nhất, không im lặng trộn hai bảng. |

Quyển 5: `../../four-items/sources/KR3g0042_005.txt`, SHA-256 `1ebdd92feaa57496b702f962ad6fafd4f19c17e98c38a94b40f626ef321dd997`.

- `005-1a–3a`, 論古人立印食官財名義: đặt nhật can làm “ta”, phân nhóm ta sinh/sinh ta/ta khắc/khắc ta và âm dương. Đây là phân loại quan hệ, chưa là đánh giá cát hung.
- `005-5a–5b`, 論正官: “正官先㸔月令然後方㸔其餘”; đoạn sau còn xét lộ can, nhật chủ, tài/ấn, thương quan, thất sát, hình/xung/phá/hại. Vì vậy thấy Chính Quan ở bản khí không đủ xác nhận Chính Quan cách thành lập.
- `005-6b`: “日主用神太盛宜時以節制之日主用神漸衰宜時以補助之”. Có điều kiện thịnh/suy và toàn cấu trúc, không hướng dẫn lấy hành ít nhất làm dụng thần.
- `005-7a`: “取官星不必專泥月令支辰或月干或年日時支干只一處有不曽損傷皆可取用”. Sách còn nêu những cách xét ngoài nguyệt chi. Một quy tắc “bản khí = cách cục duy nhất” sẽ bỏ mất ngay sự khác biệt nội bộ này.

Uyên Hải: scan NTL-9900014379, 1926, 207 trang; SHA-256 PDF `664bccd1ea4706c609df8ea6cd69a4565db97dc277e876fc22eb125ea41dcc9f`. Trang 54/trang in 三六, 又地支藏遁歌 đã có kiểm tra 12 tập hợp tàng can ở hồ sơ trước. Việc xem thêm ảnh mục Chính Quan/Tài/Ấn/Thực được ghi riêng trong `YUANHAI_FOUR_RELATIONS.json`; các trang dò tìm không tự tính là đã hiệu khảo hết sách.

### Rà bổ sung bốn nhóm trong scan Uyên Hải

Đã đọc trực tiếp các đoạn liên quan và chú biên trên ảnh PDF 96–97, 101–108; SHA ảnh có trong JSON riêng. Đã chép tay 10 cặp can cho mỗi nhóm Chính Quan, Chính Ấn, Chính Tài, Thực Thần từ chú biên, rồi chạy lunar-typescript và hàm quan hệ HHC: **40/40** cặp khớp cả hai engine.

| Nhóm | Vị trí scan | Ví dụ quan hệ cơ bản |
|---|---|---|
| Chính Quan | PDF96, 卷二 一五, 正官論 | Giáp gặp Tân; Ất gặp Canh: khắc ta, khác âm dương. |
| Chính Ấn | PDF101–103, 卷二 二〇–二二, 論印綬 | Giáp gặp Quý; Ất gặp Nhâm: sinh ta, khác âm dương. Chương cũng bàn Thiên Ấn, không gọi mọi sinh ta là Chính Ấn. |
| Chính Tài | PDF104–106, 卷二 二三–二五, 論正財 | Giáp gặp Kỷ; Ất gặp Mậu: ta khắc, khác âm dương. PDF105 nói rõ tài được bàn cả thiên/chính trong đoạn ấy. |
| Thực Thần | PDF107–108, 卷二 二六–二七, 論食神 | Giáp gặp Bính; Ất gặp Đinh: ta sinh, cùng âm dương. Câu “生我財神” trong văn mạch là Thực sinh Tài: Giáp → Bính → Mậu; không được đảo thành Thực sinh nhật chủ. |

Ba tứ trụ chép từ trang sách được chạy `Solar.fromBaZi` rồi đi ngược lại `getEightChar()` và quan hệ tàng can. Tìm được 6 ngày tương thích trong khoảng1800 tới năm hiện tại của thư viện; các ngày đó **không phải kết luận về ngày sinh của nhân vật trong sách**.

- PDF103: **Mậu Tuất – Canh Thân – Quý Dậu – Canh Thân**. Nguyệt can Canh là Chính Ấn của Quý; bản khí Thân cũng Canh; năm Mậu là Chính Quan. Ngày tương thích gồm 24-08-1958 16:00 và 09-08-2018 16:00 UTC+8.
- PDF105: **Tân Sửu – Đinh Dậu – Đinh Tỵ – Đinh Mùi**. Bản khí Dậu là Tân, **Thiên Tài** của Đinh; Canh tàng trong Tỵ mới là Chính Tài. Ca có mặt trong chương 論正財 không biến mọi quan hệ của nó thành Chính Tài. Ngày tương thích gồm 06-10-1901 14:00 và 21-09-1961 14:00 UTC+8.
- PDF108: **Kỷ Mùi – Kỷ Tỵ – Đinh Mùi – Tân Sửu**. Hai can Kỷ là Thực Thần của Đinh; bản khí Tỵ là Bính, **Kiếp Tài**. Ngày tương thích 09-05-1859 02:00 UTC+8 được lunar tái dựng; nằm ngoài dải lịch HHC1900–2100 nên không báo đó là ca kiểm lịch HHC. Hàm quan hệ HHC vẫn đối chiếu trực tiếp 40 cặp can đã đọc.

Các ca này củng cố việc tách nhận diện quan hệ khỏi xác nhận cách cục. Không có kết luận rằng đã giải hết chính cách, ngoại cách, thành/bại/cứu ứng hay tác dụng dự báo.

## Quy ước số học và API thật

Nguồn kỹ thuật chính thức đã tải byte: [6tail: 八字](https://6tail.cn/calendar/lunar.bazi.html); SHA-256 `604d8db11a9ea5877a0cab600dae55e795943692d76aafea8f594a7c727c3968`. Các bản `Yun.ts`, `DaYun.ts`, `Solar.ts`, test và npm metadata được giữ với SHA/commit ở `SOURCE_MANIFEST.json`.

Thư viện đã thực thi: lunar-typescript **1.8.6**, gitHead `a376ec2b8fd1b3069e24c92801bab8707fccd49d`; lunar-javascript **1.7.7**, gitHead `eecd5d12c8221b82ce574dc2bad2d7aefcb46e56`. Hai thư viện cùng tác giả/họ thuật toán; sự khớp giữa hai bản không phải hai chứng cứ lịch pháp độc lập.

```js
const solar = Solar.fromYmdHms(2026, 10, 15, 12, 37, 0);
const eight = solar.getLunar().getEightChar();
const yun = eight.getYun(1, 2); // 1 nam/0 nữ; đối số2: quy ước khởi vận theo phút
yun.isForward();
yun.getStartYear(); yun.getStartMonth();
yun.getStartDay(); yun.getStartHour();
yun.getStartSolar().toYmdHms();
yun.getDaYun(10); // index0: trước khởi vận, canchi rỗng; index1..9 là đại vận thật
```

`EightChar.setSect()` là quy ước **đổi nhật trụ tại giờ Tý**, tách biệt `getYun(gender, sect)` là quy ước **tính khởi vận**. Không đồng nhất hai tham số vì chúng cùng tên sect. `getYun()` không truyền sect mặc định **1**, trong khi EightChar mặc định sect **2**.

Với sect2, đặt Δ là khoảng phút:

1. `year=floor(Δ/4320)`, bỏ số phút ấy.
2. `month=floor(remainder/360)`, bỏ số phút ấy.
3. `day=floor(remainder/12)`, bỏ số phút ấy.
4. `hour=remainder*2`.

Đây là quy đổi truyền thống dạng 360 ngày/12 tháng cho **độ tuổi quy đổi**, không phải lời khẳng định một năm thiên văn có 360 ngày. Giữ nguyên 4 thành phần; không đổi toàn bộ sang số ngày theo 365.2425 rồi cộng thời gian thực.

Sect1 dùng số ngày và chi giờ (mỗi thời thần quy 10 ngày khởi vận), không lấy phút. `23h` được xử lý riêng như chi giờ chỉ số11 khi đếm khoảng; không nên giản lược thành `floor(hour/2)`.

`getStartSolar()` cộng **tuần tự** năm → tháng → ngày → giờ. Cộng năm hạ 29/2 về 28/2 khi năm đích không nhuận. Cộng tháng hạ ngày về cuối tháng đích nếu vượt số ngày. Ví dụ 2000-02-29 +1năm +1tháng cho 2001-03-28; 2024-01-31 +1tháng cho 2024-02-29. JavaScript `Date.setMonth` tự tràn ngày không tái hiện quy tắc này. Mỗi vận tiếp theo có thể lấy ngày khởi vận cộng 10*k năm với quy tắc kẹp ngày đã công bố; đây là lựa chọn triển khai cần phân biệt bảng nhãn năm của DaYun.

Chuỗi đại vận thứ `k>=1` dùng `dir=+1/-1`; `can=mod(monthP.s+dir*k,10)`, `chi=mod(monthP.b+dir*k,12)`. `DaYun.getStartAge()` là `startYear - birthYear + 1`, nhãn tuổi theo năm, không phải tuổi đủ. Không dùng riêng getStartYear/getEndYear để xác định một ngày đầu năm trước/sau giao vận: chúng chia dải **năm lịch**; ngày giao vận còn phần tháng/ngày/giờ.

## Kết quả chạy và sai khác được giữ lại

Chạy `node v53/scripts/full-bazi-runtime.mjs`: 127 thời điểm sinh (10 năm mẫu từ 1900 đến 2100, 12 tháng, thêm mốc quanh Lập Xuân/23h/29-2) × 2 giới × 2 quy ước = **508** ca.

- TypeScript và JavaScript khớp 508/508 ca bao gồm mốc khởi vận, hướng, offset, chuỗi và thập thần tháng.
- HHC và lunar khớp 508/508 hướng vận/tháng trụ; 5.080 nhãn can chi của chuỗi đúng theo tháng trụ và chiều vận.
- 254/254 ca sect2 khớp công thức chia phút nếu sử dụng chính mốc tiết của lunar.
- **Không khẳng định HHC khớp tuyệt đối mốc khởi vận lunar**: 144/254 ca sect2 khác offset. Khác mốc tiết tối đa 124 giây; khoảng phút khác tối đa 3 phút, tương ứng 6 giờ trong khởi vận quy đổi. Ca lớn nhất trong mẫu: nam 2100-04-15 12:37 UTC+8, tiết Lập Hạ của HHC là 09:23Z; lunar là 09:20:56Z.
- HHC dùng bảng mốc UTC làm tròn phút; `Solar.subtractMinute` bỏ giây ở từng đầu mút. Hai việc không đồng nghĩa. Giữ giới hạn chính xác theo phút của bảng, cảnh báo sát tiết và lựa chọn lịch pháp đã có.
- Các ca chỉ so trực tiếp ở **UTC+8**, tương thích lịch tiết của Solar. Solar API không nhận múi giờ tuỳ chọn. Khi dùng HHC ở UTC+7/múi khác, tính chênh giữa instant UTC bằng lịch tiết HHC; không đưa giờ địa phương đó vào Solar rồi gọi kết quả là so cùng instant.
- Chưa biết giờ sinh có thể đổi tuổi khởi vận đáng kể: 1 giờ thật tương ứng khoảng5ngày khởi vận. Các mẫu 0/6/12/18/23h trong JSON chỉ minh hoạ sự biến thiên; không chứng minh toàn bộ khoảng cực trị. Không điền trưa giả để báo một mốc chính xác.

Ví dụ UTC+8, 15-10-2026 12:37, năm Bính Ngọ, tháng Mậu Tuất:

| Quy ước theo phút | Nữ | Nam |
|---|---|---|
| Chiều | Nghịch | Thuận |
| Khởi vận sau sinh | 2năm 3tháng 20ngày 16giờ | 7năm 8tháng 26ngày 6giờ |
| Ngày khởi vận | 05-02-2029 04:37 | 11-07-2034 18:37 |
| Ba vận đầu | Đinh Dậu, Bính Thân, Ất Mùi | Kỷ Hợi, Canh Tý, Tân Sửu |

Mẫu này HHC/lunar trùng offset. Quy ước theo chi giờ cho nữ 2năm 3tháng 20ngày, nam 7năm 9tháng; đó là khác quy ước đã công bố, không tự coi là lỗi phần mềm.

## Phần chưa được kết luận

Chưa tự an dụng thần, định cách cục thành/bại, chấm điểm vượng suy, dự đoán bệnh/tử vong/giàu nghèo. Chưa hợp nhất tất cả hệ thống phân nhật tư lệnh, cách cục đặc biệt, hoặc cách cộng nhuận tháng truyền thống. Hồ sơ này không chứng nhận nội dung dự báo của sách là hiệu quả thực nghiệm. Nó xác minh phạm vi văn bản, tính minh bạch của quy ước và phép tính có thể tái chạy.
