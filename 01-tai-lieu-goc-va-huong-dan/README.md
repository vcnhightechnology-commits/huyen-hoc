# Tài liệu gốc và hướng dẫn cho các AI

- [Quy trình phối hợp](HUONG_DAN_PHOI_HOP.md).
- [Mã và tài liệu dự án](du-an/README.md), [trạng thái nghiên cứu](du-an/PROJECT_RESEARCH_STATE.md), [trạng thái máy đọc](du-an/EXHAUSTIVE_WORK_STATE.json), [ma trận độ phủ](du-an/v53/research/library-current/COVERAGE.json).
- [Danh mục sách nguồn](du-an/collaboration/materials/SOURCE_BOOKS.md), [manifest gốc](du-an/collaboration/materials/MANIFEST.json), [manifest tải GitHub hiện hành](GITHUB_MATERIALS.json).
- [Chỉ mục byte checkout bàn giao](HANDOFF_FILES.json), [trạng thái tải lên](../PUBLICATION_STATUS.json).

Nguồn lớn gồm 11 ZIP tổng hợp đã có, các PDF/ảnh bổ sung và hai ZIP người dùng gửi. Tái sử dụng đúng byte, không đưa ZIP/binary lớn vào Git. Các đường dẫn GitHub cũ trong bản tài liệu gốc là lịch sử. Nơi tải hiện hành: release `materials-2026-11-02` của `vcnhightechnology-commits/huyen-hoc`.

Liệt kê: `python restore-materials.py --list`. Tải một asset và kiểm SHA-256: `python restore-materials.py --file hhc-materials-001.zip --destination /path/to/cache`. Công cụ dùng GitHub CLI (`gh`) đã đăng nhập, hoặc thêm `--anonymous` khi kho công khai. Không ghi token vào tệp/chat.

Sau khi tải các ZIP cần thiết, dùng mã phục hồi trong `du-an/maintenance/materials.py` với `--cache /path/to/cache --destination /path/to/evidence` và bộ chọn `--path`, `--prefix` hoặc `--all`. Không thêm `--download` vào lệnh phục hồi cũ vì manifest gốc còn giữ đích lịch sử. Công cụ này kiểm byte ZIP và từng nguồn sau giải nén. Mã/văn bản checkout 02/11 có thể mới hơn bộ nguồn 31/10; không ghi đè mã mới bằng snapshot tư liệu cũ.

Các giới hạn chứng cứ và hồ sơ AI-01 mới nhất nằm ở báo cáo facsimile trong dossier được dẫn ở mục AI-01. Mỗi thay đổi mã cần kiểm phù hợp và Pull Request; ghi rõ nguồn chưa có, dị văn và suy luận.
