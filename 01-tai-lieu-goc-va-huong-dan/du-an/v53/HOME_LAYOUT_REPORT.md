# Bổ sung nhà ở và vị trí các phòng — V53

Hoàn thành ngày 25/10/2026 theo yêu cầu “nghiên cứu bổ sung về phong thuỷ nhà ở, vị trí các phòng”. Cập nhật cùng V53; giữ bản trước tại `../archives/v53-before-home-guide/`.

## Kết quả trên web

Trong **Xem hướng nhà** có hai lựa chọn: **Hướng theo tuổi** và **Bố trí các phòng**. Đường dẫn `#directions` giữ phần tra cung phi hiện có; `#home` mở phần nhà ở mới, không đòi hỏi năm sinh. Vẫn có năm công cụ chính, không làm người dùng chọn thêm một bộ máy nghiên cứu.

Bảy khu vực: cửa vào, phòng khách, phòng ngủ, bếp/bàn ăn, phòng tắm/vệ sinh, góc làm việc và không gian thờ. Mỗi khu có gợi ý vị trí, quan hệ với khu bên cạnh, đoạn tham khảo phong thủy và câu hỏi rà soát điều kiện thực tế. Có hình nhà SVG tự dựng cùng màu xanh/ngà, bộ biểu tượng nét đồng bộ và sơ đồ tương tác.

Người dùng có thể ghi một vùng cho mỗi khu, gồm tám phía và phần giữa nhà. Bắc nằm trên sơ đồ. Nhiều phòng có thể cùng một vùng; không giả lập va chạm hay diện tích từ dữ liệu không có kích thước. Vị trí ghi nhớ và câu trả lời của các phòng độc lập. Chưa rõ là một trạng thái riêng, không tự chuyển thành tốt hoặc xấu.

Gợi ý thay đổi theo quan sát: đường đi đang vướng, thiếu đường thải ra ngoài, có mùi, dấu ẩm, thiếu sáng, chói, tiếng động hoặc thiếu riêng tư. Vùng Tây/Đông chỉ gợi mở kiểm tra tiếp xúc nắng nếu có cửa/tường tương ứng, không suy cửa mở từ vị trí phòng. Không chấm điểm vận khí hoặc tự gán mọi phòng vào hướng hợp tuổi.

Trên điện thoại, sơ đồ là khối mở thêm; người dùng thấy nội dung phòng sớm hơn. Có thể tải TXT và in/lưu PDF phòng đang đọc; bản tải chứa các vị trí đã ghi, câu trả lời, gợi ý và giới hạn. Thông tin nhà ở chỉ giữ trong phiên, không tự lưu `localStorage`, không trộn vào hồ sơ ngày sinh. Mở hồ sơ hướng theo tuổi từ màn hình nhà ở đưa lại đúng kết quả nhìn thấy được.

## Nghiên cứu và độ đúng

Đã quan sát trực tiếp hai ảnh lời tựa *相宅書敘* để kiểm sự phân biệt phương vị, hướng và khu bếp/bếp nấu. Không gọi chúng là bản toàn văn *Dương Trạch Tam Yếu*. Các gợi ý bố trí hiện đại do dự án biên tập, không giả làm trích dịch cổ thư. Nguồn hiện đại dùng cho ánh sáng, độ ẩm, đường thải và lối đi được tách khỏi quan niệm văn hóa. Chi tiết và liên kết nguồn ở `research/home/RESEARCH_NOTES.md`.

Lưu 8 thân phản hồi HTTP 200 gồm 6 HTML và 2 JPEG, có độ dài và SHA-256. Hai phản hồi 403 từ CDC được giữ như lỗi, không nhận là byte bài gốc; YourHome hết thời gian chờ được ghi rõ. Ghi chép đọc bằng công cụ web giữ riêng trong `WEB_OBSERVATIONS.json`. Không vượt chặn truy cập. SHA xác nhận toàn vẹn bản tải, không phải chứng nhận khoa học cho phong thủy hoặc chữ ký nhà xuất bản.

Các bộ `engine.js`, `engine-runtime.js`, `content.js`, `yi-content.js`, `art.js` giữ nguyên byte so với snapshot trước phạm vi. Không chỉnh lịch, sao, Bát tự hoặc công thức cung phi. Lượt hồi quy thực thi cả engine V53 và V52 đã lưu trên 336 lá số Tử vi, 288 cấu hình Bát tự và 402 tổ hợp năm/giới tính, không phát hiện chênh lệch trong mẫu. Không tải lại hoặc chạy thêm iztro chỉ để kiểm lại một bộ tính chưa thay đổi; đối chiếu iztro thật của phạm vi trước vẫn giữ nguyên và không được tính thành thử nghiệm mới ở đây.

## Kiểm chứng

**126/126 kiểm tra đạt trên HTML cuối**:

- 40 mới: phân loại chưa biết/đã quan sát/cần xem lại; chiều câu hỏi đúng; bản đồ/ô chọn đồng bộ; dữ liệu từng phòng độc lập; nhiều phòng cùng vùng; xóa vị trí; loại nhà; liên kết trực tiếp/lùi trang; mở hồ sơ cũ từ `#home`; TXT/in; không tự lưu; không nguồn nghiên cứu trong DOM; hash nguồn; byte bộ tính không đổi.
- 50 hồi quy công cụ và engine: Tử vi, Bát tự, bản mệnh, hướng theo tuổi, Gieo quẻ, lưu/mở/xóa, điều kiện đầu vào và bố cục.
- 36 trải nghiệm: năm lựa chọn công cụ, chữ và tương phản chính, đầu trang, bản đọc, in và riêng tư.

Màn hình nhà ở không tràn ngang ở 320, 390, 650, 768, 1024, 1440 px. Kiểm ảnh chụp desktop/mobile; không thấy chữ đè hình. Không lỗi JavaScript hoặc yêu cầu HTTP từ HTML độc lập. In giữ gợi ý, phần vị trí bằng chữ và kết quả rà soát, ẩn sơ đồ nhập và biểu mẫu tuổi. Hồ sơ ngày sinh cũ vẫn tính lại khi mở; không đưa dữ liệu nhà vào hồ sơ đó.

Tái lập: `node scripts/build.mjs`, `node scripts/verify-home-guide.mjs`, `node scripts/verify.mjs`, `node scripts/verify-experience.mjs`, `python scripts/package.py` từ thư mục `v53`. Trình duyệt Playwright dùng runtime cục bộ của máy; đường dẫn phụ thuộc môi trường. Các kết quả JSON/ảnh và ví dụ TXT ở `qa/home-guide/`, `qa/test-results.json`, `qa/experience/test-results.json`.

## Phát hành và giới hạn

Đã cập nhật HTML độc lập, HTML gốc tiện mở, `site/index.html`, manifest và hai gói ZIP. `site/` chỉ có HTML; gói web chỉ HTML và hướng dẫn. Nguồn nghiên cứu, ảnh cổ, kết quả kiểm thử và báo cáo chỉ nằm trong gói nguồn. Không xuất bản lên mạng hoặc sửa các bản V46–V52.

Chưa phân tích mặt bằng đo đạc, cửa sổ và tọa hướng thực tế; sơ đồ không phải phương án xây dựng hay phép tính trung cung. Chưa mã hóa Phi tinh, hướng bếp điện theo truyền phái hoặc một bảng phòng tốt/xấu cố định. Các hướng nghiên cứu tiếp theo nằm trong `research/home/RESEARCH_NOTES.md` và `NEXT_STEPS.md`.
