# Mô hình mặt bằng chữ nhật và góc hướng

Ngày26/10/2026. Đây là đặc tả phép tính hình học mới, không phải trích sách, bảng Phi tinh hoặc quy tắc lựa chọn hướng nhà của một truyền phái.

## Đầu vào

KhungW×D mét, W,D∈[0,1;1000]. X tăng sang phải, Y tăng xuống dưới, gốc(0,0) ở góc trên trái. Trục đi lên sơ đồ có phương vịA từ Bắc thật theo chiều kim đồng hồ, A∈[0°,360°]. Bất định gócε∈[0°,180°]. Chưa nhận sai số độ dài/tọa độ hoặc nhà không chữ nhật.

Phòngr=(x,y,w,d),1–30phòng; x,y không âm, w,d≥0,01m và hình phòng nằm trong khung. Sai số số thực so ranh1e-8m. Tên tối đa60ký tự, thoátHTML khi render. Cửa0–60đoạn, loại cửađi/cửasổ, cạnh trên/phải/dưới/trái. Trên/dưới: offsettừtráisangphải; trái/phải: offsettừtrênxuốngdưới. Đoạn phải nằm trọn trên cạnh.

## Kết quả

Tâm khungC=(W/2,D/2); tâm phòngP=(x+w/2,y+d/2). Nếu khoảngCP≤1e-8m, không tính góc. Nếu khác0:

`bearing = normalize(atan2(P.x-C.x, -(P.y-C.y))*180/pi + A)`.

Mũi Bắc trên bản vẽ dùng vector`(-sin A, -cos A)` trong hệtọađộmàn hình. Vì A90°nghĩalàhướng lêncủahình đangchỉĐông, Bắcphảihướngsangtrái trên hình; không nhầm quay mũi tên cùngchiềuA.

Pháp tuyến ra ngoài cạnh: trênA, phảiA+90, dướiA+180, tráiA+270, chuẩn hóa[0,360). Truyền góc vàε vào bộHHC_BEARING vàHHC_MOUNTAINS hiện hành. Quyước0saisố/miềnđóngkhiε>0 giữ đúng các bộ đó. Không suy ra cách xácđịnh tọa/hướng của nhà nhiều cửa từ pháp tuyến hình học.

Diện tích tổngW×D; diện tích từngphòngw×d. Liệt kê các giao cặp có bề ngang và sâu dương, không coi cạnh chung là phần chồng. Diện tích phòng phủ là diện tích hợp, không phải tổngdiệntíchphòng trừ tổnggiao cặp (cách sau sai khi có giao ba phòng). Tính hợp bằng các lát giữa mọi đầuX, hợp khoảngY của các phòng trên lát rồi nhân độrộnglát. Phần chưa gán=max(0,tổng−hợp). Không gọi phần chưa gán là diện tích sử dụng/sàn theo tiêu chuẩn pháp lý.

Kiểm các đoạn cửa trùng trên cùng cạnh theo độdài giao; khác cạnh không tự ghép thành một cửa. Tâm khung trong một phòng và tâm khung chạm ranh phòng là hai trạng thái riêng. Không tự gán vùngtrungcung theo một tỷ lệ hình học chưa cónguồn.

## Căn cứ nguồn tái dùng

`../full-study/home/RULE_24_MOUNTAINS.json`, nguồnCADAL06056503 HiệpKỷ quyển2 đãđọcảnh5–7, và `../../mountains.js`/`bearing-guide.js` có đốichiếutrước. Các nguồn này xácđịnh các nhóm sơn/thứtựđối, khôngxácnhậnphươngánđặtphòngmới. Manifest liênkếtvàSHA256 ở `REUSED_SOURCES.json`; không tải thêmbyte từInternet trongphạmvihìnhhọcnày.

Cácfixturediệntích vàtọađộnhỏ trong `scripts/verify-measured-plan.mjs` là vídụkiểmtra do tácgiảđặtra đểbiếtkếtquảchínhxác, khôngphảiđạidiệnnhàthực củangườidùng. Biểu mẫu không nạp các sốmẫu này.
