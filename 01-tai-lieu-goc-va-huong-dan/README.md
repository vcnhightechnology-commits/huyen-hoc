# Tài liệu gốc và hướng dẫn cho các AI

- [Quy trình phối hợp](HUONG_DAN_PHOI_HOP.md).
- [Mã và tài liệu dự án giữ nguyên cấu trúc đường dẫn](du-an/README.md).
- [Trạng thái nghiên cứu](du-an/PROJECT_RESEARCH_STATE.md), [trạng thái máy đọc](du-an/EXHAUSTIVE_WORK_STATE.json), [độ phủ](du-an/v53/research/library-current/COVERAGE.json).
- [Danh mục sách nguồn](du-an/collaboration/materials/SOURCE_BOOKS.md), [manifest lịch sử nguồn tổng hợp](du-an/collaboration/materials/MANIFEST.json).
- [Danh mục tải từ GitLab](GITLAB_MATERIALS.json). Chỉ xem tư liệu là đã bàn giao trực tuyến khi `PUBLICATION_STATUS.json` ghi uploaded và từng asset đã kiểm SHA từ remote.
- [Chỉ mục byte checkout bàn giao](HANDOFF_FILES.json).

Các PDF/DjVu/ảnh và 11 ZIP dùng chung được tải từ Generic Package Registry của chính kho GitLab; chúng giữ byte nguồn đã có. Dùng `python restore-materials.py --list` để liệt kê hoặc `--file TEN --destination THU_MUC` để tải một asset và kiểm SHA-256. Sau đó dùng công cụ phục hồi của dự án với cache ZIP local. Với kho riêng tư, đặt GITLAB_TOKEN trong môi trường của máy thực thi; không ghi token vào tệp hoặc chat.

Bản nguồn 31/10 là mốc lưu trữ, còn mã/văn bản trong `du-an/` là trạng thái checkout khi bàn giao 02/11. Các thay đổi mới và nguồn bổ sung được ghi trong manifest bàn giao. Bằng chứng chưa tải thành công vẫn mang trạng thái mở.
