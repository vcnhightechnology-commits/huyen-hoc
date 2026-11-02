# AI-01 — hướng nghiên cứu tiếp theo

**Phạm vi:** Bát Tự — Tứ Trụ, Chính Ấn và Không Vong

**Trạng thái theo yêu cầu người dùng 01/11/2026:** AI-01 hiện là nhánh được ưu tiên. Đã đối chiếu WYG II/III theo SHA, xem một phần hai scan NLC khác số hiệu của 五行精紀 quyển 19 (NLC 06857 PDF 47–50; NLC 892-2621-209417 PDF 30–31), chạy engine thật chỉ để kiểm lịch, và tìm song hành từ vựng `交涉`. Ảnh thứ hai xác nhận `福聚印` và `年月日時胎`; transcription 识典 cùng dãy số hóa chép `年月時胎`, chưa chứng minh được ảnh trang nào là nguồn transcription. Đã xác nhận *宋史藝文志* có mục thư mục `通真子玉霄寶鑑經一卷`; WXJJ dẫn tên 玉霄寶鑑 trong các quyển 1/3/4/19/20/25, nhưng chưa tìm thấy bản văn độc lập. Scan Trương thị NCL-06584 (240.79 MB) vẫn chưa đối ảnh; sơ đồ tám witness chỉ có trang giới thiệu ấn bản khảo hiệu. Xem [AI01_PROGRESS_2026-11-01.md](AI01_PROGRESS_2026-11-01.md), [AI01_FACSIMILE_COLLATION_2026-11-01.md](AI01_FACSIMILE_COLLATION_2026-11-01.md), [AI01_YUXIAO_BIBLIOGRAPHIC_NOTE_2026-11-01.md](AI01_YUXIAO_BIBLIOGRAPHIC_NOTE_2026-11-01.md), [AI01_JIAOSHE_LEXICAL_NOTE_2026-11-01.md](AI01_JIAOSHE_LEXICAL_NOTE_2026-11-01.md), [AI01_SOURCE_VARIANTS_2026-11-01.json](AI01_SOURCE_VARIANTS_2026-11-01.json). Can tháng ví dụ đầu tờ 七 vẫn chưa phân xử. Không tích hợp suy luận vào engine/site; AI-01 còn mở.

**Trạng thái:** hồ sơ phục hồi từ gói ngày 01/11/2026; ref Git/PR/SHA và số kiểm thử nêu trong hồ sơ là dữ liệu lịch sử, chưa xác nhận là trạng thái hiện hành. Đây là thư mục nghiên cứu, không phải Git branch được checkout.

## Hướng đang mở theo hồ sơ

Ảnh facsimile WXJJ tập 第3冊 được xem một phần; tập 第4冊 mới xem ảnh preview trang 30–31, chưa lưu PDF gốc và chưa hiệu khảo toàn quyển. Ảnh WYG II/III chưa kiểm trực tiếp; `交涉` có song hành từ vựng nhưng chưa có định nghĩa thao tác. Nhan đề 玉霄寶鑑經 có chứng cứ thư mục; văn bản độc lập và quan hệ với câu trích WXJJ còn mở. NCL-06584 là scan ứng viên khác, chưa đối ảnh. Không tự chốt chữ tờ 七 còn mờ hoặc đưa logic phán đoán vào engine. Patch Không Vong ngày 01/11 chưa push do GitHub 403; PR #13 chỉ là trạng thái lịch sử.

## Vị trí dự án hiện tại nên đối chiếu trước

- `v53/research/bazi-branch-union`
- `v53/research/bazi-branch-clash`
- `collaboration/imports/ai01-2026-10-31`

Các đường dẫn trên là điểm tra cứu gợi ý; cần xác nhận đúng phạm vi nguồn trước khi tái dùng. Không chạy lại batch đã có payload. Chỉ nhận một quy tắc hoặc patch sau khi có byte nguồn đáng tin cậy, đối chiếu checkout hiện hành và chạy kiểm phù hợp.

## Ưu tiên lượt nghiên cứu kế

- Record 识典 `NGJ8922621209348` được nối với cùng dãy mã số hóa NLC 892-2621; còn mở mắt xích tới ảnh trang cụ thể. Không đồng nhất transcription với một physical witness độc lập.
- Ưu tiên lấy đúng trang trong NLC 第4冊 chứa `天元變化書/支干有交涉` và ví dụ `癸巳…卯月`; so với PDF trang 50 của NLC 06857 để xử lý `乙/己/已`. Chỉ giữ ảnh xem trang lẻ và SHA, không tải PDF toàn tập. Nếu mở lại NCL-06584, trước hết định vị bằng chỉ mục/viewer rồi mới lấy trang mục tiêu; không tải 240.79 MB toàn tập. Khi render PDF local, dùng `-scale-to` hoặc crop; không render full page 180 dpi.
- Kiểm tra xem dự án đã có *八種五行精紀箋訂* hay trích dẫn apparatus trong bộ tài liệu hiện hữu trước khi tìm thêm nguồn; trang giới thiệu hiện tại chỉ là tài liệu thứ cấp để định hướng danh mục witness.
- Tìm văn bản độc lập hoặc trích đoạn khác của 玉霄寶鑑經; *宋史藝文志* chỉ xác nhận mục thư mục. Giữ phân biệt nhan đề, lời dẫn, bản văn và suy luận.
- Không thay `五位俱`/`五位中或四位`, không nhập 福聚/權 thành một luật, không sửa engine/site cho tới khi tiền đề và witness được xác lập.

## Bằng chứng phục hồi

- Bản bàn giao gốc: [`HANDOFF.md`](HANDOFF.md).
- Bản trích xuất chưa xác minh byte gốc: `evidence/extracted-unverified/`; không dùng `git apply` hoặc thực thi.
- Hash và ánh xạ nguồn nằm trong `../../IMPORT_VERIFICATION.json`.
