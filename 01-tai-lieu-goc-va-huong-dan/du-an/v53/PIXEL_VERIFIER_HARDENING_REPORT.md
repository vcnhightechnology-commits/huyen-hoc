# Siết kiểm chứng ảnh ở hai verifier

Ngày28/10/2026. Phát hiện ImageChops.difference trênRGBA rồi gọi getbbox mặc định có thể chỉ xét alpha. Khi RGB đổi mà alpha giữ nguyên, hiệu alpha bằng0 có thể che khác biệt màu. Đây là lỗ hổng trong cách kiểm ảnh, không phải thay đổi dữ liệu an sao hoặc web.

Chỉ sửa ba lời gọi getbbox tại verify-bazi-food-six-pillars-sources.py(1) và verify-liuyao-b03-triad-clause-sources.py(2): thêm alpha_only=False. Giữ bản trước và sau cùng byte/SHA tạiqa/pixel-verifier-hardening. So byte chứng minh không có thay đổi khác ngoài tham số; các phép soRGB đã đúng giữ nguyên. Kiểm AST chính ba biểu thức với mẫu crop thật trong bộ: bản nguyên khớp; đổi một pixelRGB cùngalpha bị từchối; đổi alpha bị từchối. Phảnvídụ xác nhận mặc định cũ bỏ sót RGB.

Hai source-verifier được chạy --no-write sau sửa. Bộ Bát tự vẫn giữ kết quả trước: ba crop; bộ B03 vẫn giữ bốn crop và tái dựng PDF khớp. Không gọi engine, không sửa ảnh, dữ liệu chép hay kết quả đã lưu. Gói5069 trước scopeTửvi giữ nguyên trongarchives/v53-before-tuvi-lower-printed-cases; oldscriptsđúngbyte5069cóthểtruyvết.

Bổ sung này đóng cùng phạmvi Tửvi đang tiếp nhận, không tạo bản mới chỉ để tăng số. Site/HTML707411byte/webZIP nguyên byte. Các bản nghiên cứu và staging lịch sử vẫn giữ nguyên; không nói mọi bộ kiểm ảnh trong toàn kho đều đã được kiểm lại. Ma trận toàn tác phẩm còn mở.
