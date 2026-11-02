# Luận Chính Ấn — chương nguồn và điều kiện năm vị trí

Đã đọc ảnh native CADAL06066039 ở vị trí88–93, tờ43b–46a. Chương bắt đầu `論正印` ở88 và kết thúc trước `論徳秀` ở93. Không kéo phần Đức Tú vào chương Chính Ấn. Ba ảnh91–93 được giải mã mới từ container đã giữ; ba ảnh88–90 kế thừa lượt đối chiếu trước. Không HTTP/container/truyền bản mới. Chưa kiểm hợp tập toàn kho để đếm vị trí mới toàn thư viện; giữ chỉ số này null thay vì cộng sáu trang vào tổng.

Bản số WYG ghim revision được phân thành13đơn vị biên tập, phục nguyên đúng690codepoint sau bỏ marker trang, paragraph và khoảng trắng. Không emend chữ; không nhận690chữ là690quy tắc hoặc toàn bộ chữ ảnh đã hiệu khảo ngoại giao. Câu đầu định nghĩa正印theo五行正庫, tách rõ với quan hệ Thập thần của can ngày. Nhóm水土壬辰丙辰giữ chung, không tự phân壬辰choThủy/丙辰choThổ.

Các đơn vị:

- S01: định nghĩa, bản gia/đế tọa/thai nguyệt, các điều kiện sinh khắc và lời lịch sử về người. Chưa đủ định nghĩa `命`, không chọn nạp âm năm hoặc nhật can tự động.
- S02: quý nhân giáp ấn, hai ví dụ丙丁/甲戌với酉亥và壬癸/壬辰với卯巳. Đây là các hệ gốc có tên nguồn; chưa hợp vào lá số hoặc tự chọn mọi gốc năm/ngày.
- S03: Hoa Cái Ấn, ví dụ亥卯未得癸未. Cách nối ba chi vẫn mở, không tự yêu cầu đủ ba hay chỉ một chi.
- S04: Văn Chương Ấn, giữ hai cụm ví dụ riêng:納音尅身干神復制và干神制支神合. Không coi mọi cặp là cùng một cơ chế.
- S05: các điều kiện庫墓、生旺、扶助、互換祿馬、貴人、相合và hình/xung/phá/hại/kiến quỷ; chưa dựng ưu tiên hoặc tổng hiệu lực.
- S06: Phượng Hoàng Hàm Ấn có một chuỗi bốn trụ được nguồn in cho虞尚書. Chuỗi nguồn không tự xác lập ngày sinh lịch sử hoặc vai trò mọi cặp.
- S07: Phúc Tụ Ấn, điều kiện năm vị trí và đồng vị ấn được chọn cho mô-đun riêng dưới đây.
- S08: Họa Tụ Ấn, ví dụ癸巳/壬辰và水俱墓於辰. Nguồn còn giải以巳為命; không mặc định nhật chủ癸hoặc suy nhiều nước từ đếm trụ.
- S09: Phá Phúc Thành Họa Ấn,水人/水印và月日時胎多帶土、本家印見鬼盛. `多`/`盛`và hai nhánh liên kết còn cần định nghĩa.
- S10: Đới Sát Ấn, ví dụ壬子/壬辰丙辰vàđiều kiện反尅本命/無福神往還. Không đồng nhất nhãn貴煞với hằng số Thất Sát hiện hành.
- S11: Lâm Không Ấn có印落空亡、支無六合、見官貴. Chưa chọn cách gộp hoặc tự lấy tuần không từ lịch chưa kiểm.
- S12: Tự Hình Ấn, ví dụ庚戌/乙丑và丑戌相刑. Không đổi tên nguồn thành cặp自刑của engine hiện hành; ý nghĩa nguồn phải đứng riêng.
- S13: kết luận真五行與納音同氣và lời gia đình/thọ chất của nguồn; chưa chuyển thành dự báo đời sống.

Tham chiếu Phúc Tụ chỉ nhận đúng nguồn/khung và khai báo boolean/null cho năm vị trí `year/month/day/hour/fetal` cùng sáu thuộc tính tại cùng ấn. Khớp tiền đề chọn cần cả năm vô khí suy bại,正印và偏印cùng tại đây, và庫hoặc旺. Cụm `雖有煞神至是受制` được biểu diễn bảo thủ: nếu có Sát đến thì cần hiệu lực chế đã khai báo; nếu chưa rõ Sát có đến nhưng biết chế được thì nhánh này vẫn thỏa, còn phần khác vẫn độc lập. Đây là phép ghép tiền đề tường minh theo cách đọc đã ghi, không tự nhận nghĩa nguồn đã giải hoàn toàn.

Không tính thai nguyên, sức lực, hiệu lực chế Sát hay ánh xạ正印/偏印sang trường Thập thần. Không suy庫墓từ chi, hoặc nhãn vượng từ mùa/sinh-vượng. Không chấm phúc/họa, tiền tài, sức khỏe hoặc gia đình. Đầu ra chỉ kiểm sự khớp của những tiền đề đã được người nghiên cứu khai báo; nhận diện Phúc Tụ trọn vẫn null.

Đã niêm phong4tệp trước mã,11ca thủ công. Sáu nhóm kiểm gồm243khung yếu/vượng khai báo năm vị trí và729khung sáu thuộc tính đồng vị; oracle điền tất cả giá trị boolean cho null để kiểm đối chiếu ba giá trị. Tổng992khung/11904bất biến null,12đầu vào sai. Không gọi engine vì đây là phép ghép tiền đề văn bản, không so lịch/khí/thập thần mới. Source check kiểm SHA container/decoder/bản chép/ảnh, offset và phục nguyên chương.

Liên hệ C19 nay có ảnh chương正印vàcụm華蓋印thực sự, nhưng còn thiếu chỉ dấu trực tiếp để khẳng định C19dùng đúng toàn hệ ấy. `福聚`/`禍聚`trong chương Chính Ấn cũng có điều kiện riêng, không tự thay danh sách Thực thần C19. Mô-đun nhãn C18trước đó và mô-đun chương3này giữ hai gốc nguồn riêng; không tăng ma trận parentThực thần49/41/0khi chưa tiếp nhận có tên.

Đây là công việc riêng sau gói C16/C23/C31, chưa trong manifestV53/ZIPmốcđó. Tiếp việc nghĩa nguồn `命`, cách nối ví dụ Hoa Cái Ấn, các điều kiện S08–S12 và vị trí thật của C19. Tái dùng các kết quả engine đã lưu nếu có phép đối tọa độ mới cần thiết; không dùng sự đồng ý engine để phân định văn pháp hoặc tên nguồn.
