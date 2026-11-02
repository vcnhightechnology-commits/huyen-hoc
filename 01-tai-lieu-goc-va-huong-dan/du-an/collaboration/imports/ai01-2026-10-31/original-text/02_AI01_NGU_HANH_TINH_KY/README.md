# AI-01 — Bàn giao nghiên cứu bổ sung Huyền Học Các (31/10/2026)

**Chủ đề:** Đối chiếu Chính Ấn / Ấn bản gia / Quan Ấn–Quỷ Ấn của **《三命通會》** với **《五行精紀》 quyển 19**. Đã tìm được **hai ví dụ Tứ trụ từ lời dẫn mang tên 《天元變化書》**, mười hai điểm khác biệt giữa hai tác phẩm, phương pháp kiểm can–tháng/can–giờ và bảng Nạp âm, kèm bài học tiếng Việt có thể giao cho biên tập.

**GitHub hiện có vấn đề:** Connector GitHub trả HTTP 403 **“Sorry. Your account was suspended”**, vì vậy gói này **KHÔNG** phải một PR đã được push. Không nói đã cập nhật repo.

## Nội dung sẵn có

Thư mục đích nằm dưới `collaboration/parallel-research/submissions/AI-01/quan-an-quy-an-wuxing-jingji/`:

- `KNOWLEDGE_ARTICLE_VI.md` — bài học nhiều phần, phân tích lý luận và hai ví dụ (đầu ra chính).
- `SOURCE_REGISTER.md` — nguồn theo tác phẩm và giới hạn chứng; link NLC scan cần đối ảnh.
- `COLLATION_AND_VARIANTS.md` — đối chiếu 12 chỗ khác nhau, giải thích tại sao không sửa chữ cổ.
- `CASE_ANALYSIS.md` — trường hợp **Quan Ấn** và **Quỷ Ấn** theo bốn trụ, hành Nạp âm, phương pháp khởi tháng và giờ.
- `THEORY_MATRIX.csv` — bảng luận điểm có thể nhập nghiên cứu (không phải rules engine).
- `OPEN_QUESTIONS.md` — nhiệm vụ nghiên cứu tiếp và hướng giao AI khác.
- `CHECK_SOURCE_EXAMPLES.py` — kiểm nhất quán cấu trúc **văn bản được chép**, không phải engine bói toán, ảnh scan hoặc bằng chứng ứng nghiệm.

## Nhập vào repository khi quyền ghi khôi phục

1. Vào repo `thanthiende1-alt/huyen-hoc-cac`, kiểm tra nhánh `main`, PR #18 và #17 lúc thao tác, đọc `AGENTS.md` + `STORAGE_POLICY.md`. Tránh chồng đường dẫn với AI khác.
2. Checkout nhánh riêng AI-01 phù hợp; có thể tiếp tục `codex/ai01-luming-shen-seal-theory` của PR #18 **nếu PR đó vẫn còn phù hợp**. Copy **nguyên thư mục dưới `collaboration/`** từ gói này vào repository; không tự sao chép file PDF lớn vào Git.
3. Chạy `python collaboration/parallel-research/submissions/AI-01/quan-an-quy-an-wuxing-jingji/CHECK_SOURCE_EXAMPLES.py`. Kiểm bài học và nguyên văn WYG; phần ảnh NLC vẫn phải kiểm thủ công khi truy cập được.
4. Gửi PR **nháp** nêu rõ hai tác phẩm, **không** coi bản sao điện tử là nhân chứng độc lập; ghi `consumerChanged=false`, `engineCalls=0`, không tăng `COVERAGE.json`.

**Không** sửa `v53/Huyen_Hoc_Cac.html`, ZIP, release, engine, source WYG, `POST_RELEASE_WORKING_FOLLOWUP.json`, `EXHAUSTIVE_WORK_STATE.json`. Một bài viết lý luận có dẫn chứng **không phải** việc khẳng định mệnh lý đã được khoa học chứng thực.

## Tham chiếu chính

- https://asklingxi.com/zh-tw/books/wuxing-jingji/19-jinshen/02-zhengyin
- https://www.shidianguji.com/zh/book/NGJ892411999013122114408/chapter/1lmyjad4zcsvn
- https://zh.wikisource.org/zh-hant/三命通會_(四庫全書本)/卷03
- https://zh.wikisource.org/zh-hant/三命通會/卷二
- https://commons.wikimedia.org/wiki/File:NLC892-2621-209417_五行精紀_第4冊.pdf (đã định vị; **chưa đọc ảnh**)
