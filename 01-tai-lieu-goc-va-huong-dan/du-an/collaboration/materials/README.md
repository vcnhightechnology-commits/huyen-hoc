# Tư liệu để đối chiếu độc lập

Kho hiện hành đã chuyển sang công khai `dedaithien-sudo/huyen-hoc` theo xác nhận của chủ dự án. Khi bản phát hành đã mở, có thể tải chọn lọc không cần đăng nhập: `python maintenance/materials-range.py --anonymous --path v53/research/bazi-relations/sources/KR3g0042_003.txt --destination /path/to/evidence`. Gói bổ sung AI01 nằm cạnh 11 gói nguồn, hướng dẫn riêng ở `collaboration/imports/ai01-2026-10-31/README.md`. Những biên bản xác minh cũ mang tên tài khoản bị khóa là chứng cứ lịch sử; xem `collaboration/REPOSITORY_MIGRATION.json` và biên bản chuyển kho mới.

Tư liệu được bàn giao trong bản phát hành công khai [`materials-v53`](https://github.com/dedaithien-sudo/huyen-hoc/releases/tag/materials-v53). `MANIFEST.json` ánh xạ từng đường dẫn gốc đến SHA-256, kích thước, gói tải và thành viên trong gói. Những tệp trùng byte dùng chung một đối tượng, nhưng vẫn giữ đủ đường dẫn và xuất xứ. `SOURCE_BOOKS.md` liệt kê các PDF/DjVu gốc theo mã băm để chọn đúng gói.

Manifest đầy đủ khoảng 8 MB, dành cho công cụ khôi phục. Với phiên chỉ đọc GitHub, dùng `FILE_INDEX.json` để chọn tệp chỉ mục nhỏ theo phạm vi trong `file-index/`; mỗi tệp có đường dẫn nguồn, SHA-256, kích thước và gói chứa nó. Ví dụ phạm vi `v53/research/bazi-jianlu-context` nằm ở `file-index/v53--research--bazi-jianlu-context.json`. `SUMMARY.json` ghi số lượng và dung lượng, `UPLOAD_VERIFICATION.json` ghi mã băm máy chủ đã đối chiếu.

Phạm vi: tư liệu hiện có trong dự án tại thời điểm bàn giao, gồm nguồn PDF/DjVu/ảnh, bản chép, dữ liệu thực thi đã lưu, mã kiểm chứng, thư viện `v46/node_modules`, các phần nghiên cứu đang dở và chỉ mục lịch sử hợp nhất cùng đối tượng của nó. Không bao gồm thư mục `.git`, hồ sơ đăng nhập, công cụ đăng nhập GitHub, thư mục chat Codex ngoài dự án hoặc ZIP toàn bộ lặp lại dữ liệu đã bàn giao. Mọi loại trừ cụ thể được ghi trong manifest. Tư liệu không có tại máy, chưa tải được hoặc chưa xác minh vẫn là mục mở của ma trận nghiên cứu.

Ngoài tệp hiện hành, những phiên bản byte riêng còn nằm trong ZIP nguồn phát hành trước được giữ dưới đường dẫn phục hồi `recovery/materials-historical-source-package/`. Trường `historicalSourcePackageCoverage` ghi đối chiếu tất cả thành viên của gói cũ với kho đối tượng được bàn giao. Không thay tệp hiện hành bằng biến thể lịch sử này. Việc giữ nội dung thành viên không có nghĩa tái tạo y nguyên phần vỏ ZIP hoặc phát hành lại ứng dụng.

## Phiên có môi trường chạy lệnh và quyền GitHub

Cần Python 3 và GitHub CLI đã được chủ tài khoản đăng nhập trong môi trường đó. Không đưa token vào mã, chat, URL hoặc commit. Để lấy đúng tệp nguồn, ưu tiên cách tải HTTP Range đã được kiểm trên nguồn thật; script chỉ nhận các byte nén của đối tượng được chọn, khôi phục và kiểm SHA-256 gốc:

```sh
python maintenance/materials-range.py --path v53/research/bazi-relations/sources/KR3g0042_003.txt --destination /path/to/evidence
python maintenance/materials-range.py --prefix tmp/bazi-source-seal-staging/images/ --destination /path/to/evidence
```

Thông tin đăng nhập chỉ dùng với API GitHub; header xác thực không được chuyển tiếp sang máy chủ tải có liên kết ký sẵn. Script từ chối máy chủ bỏ qua khoảng byte yêu cầu, tệp không khớp mã băm và việc ghi đè tệp khác nội dung. Tải cả gói khi cần kiểm gói hoặc khôi phục nhiều phạm vi:

```sh
python maintenance/materials.py --prefix v53/research/bazi-jianlu-context/volume3/ --list
python maintenance/materials.py --prefix v53/research/bazi-jianlu-context/volume3/ --download --destination /path/to/evidence
```

Để dựng toàn bộ dữ liệu của thời điểm bàn giao trong một thư mục độc lập:

```sh
python maintenance/materials.py --all --download --destination /path/to/hhc-materials
```

Script chỉ tải các gói cần thiết, kiểm SHA-256 gói và từng tệp trước khi sử dụng, giữ nguyên byte, không ghi đè tệp khác byte đã có. Chọn thư mục trống để dựng bản đầy đủ; mã ở nhánh GitHub mới hơn có thể khác snapshot tư liệu. Sau đó dùng checkout GitHub hiện hành làm mã làm việc và nguồn khôi phục làm bằng chứng, thay vì ghi đè mã mới bằng snapshot cũ. Trong môi trường không có GitHub CLI, tải các gói cần thiết bằng giao diện Releases rồi đặt vào thư mục chỉ định bằng `--cache`.

## Phiên ChatGPT web chỉ đọc qua kết nối GitHub

Đọc `SOURCE_BOOKS.md`, manifest, bản chép và báo cáo trong kho để định vị nguồn. Việc có quyền đọc kho không tự chứng minh phiên đó có thể tải/giải nén release asset riêng tư, đọc DjVu, xem ảnh hoặc chạy kiểm thử. Nếu công cụ hiện có không hỗ trợ, phải ghi rõ giới hạn và yêu cầu đưa đúng nguồn cần đọc vào một phiên có môi trường thực thi hoặc đính kèm tài liệu phù hợp. Không gọi việc đọc bản chép là đã đối ảnh gốc.

Tài liệu chính thức: [GitHub trong ChatGPT](https://help.openai.com/en/articles/11145903-connecting-github-to-chatgpt). Khả năng đọc, chỉnh sửa và đẩy thay đổi tùy bề mặt sản phẩm; nếu chỉ có quyền đọc, trả patch hoặc kết quả nghiên cứu thay vì tự nhận đã push.

## Tiếp tục nghiên cứu và kiểm chứng

Đọc `AGENTS.md`, `STORAGE_POLICY.md`, `POST_RELEASE_WORKING_FOLLOWUP.json`, `EXHAUSTIVE_WORK_STATE.json`, `v53/NEXT_STEPS.md` và ma trận mới nhất. Các đường dẫn `tmp/` trong manifest là phần làm việc có thật tại thời điểm bàn giao; bản gốc và các seal lịch sử giữ nguyên, không hiệu chỉnh seal cũ để hợp thức hóa bytes mới. Kiểm phát hành ngày 30/10 chỉ chứng minh mốc đó, không tự chứng minh snapshot bàn giao ngày 31/10 là phát hành ứng dụng mới.

Kiểm nguồn có thể dùng toàn bộ byte được khôi phục; các script gắn đường dẫn Windows cố định có thể cần chỉnh trong nhánh riêng trước khi chạy trên Linux. Không chạy lại `run-once` hoặc batch lịch/engine đã lưu chỉ để tăng số. Giữ bản gốc, bản chép, quy ước và suy luận riêng; không đưa corpus, phòng kiểm định hoặc bảng so engine lên site. Mọi nhánh còn mở trong ma trận vẫn mở sau việc bàn giao này.
