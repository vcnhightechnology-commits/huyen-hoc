"""Update continuation pointers after old mutable documents have been sealed."""
from pathlib import Path
import json
W=Path(__file__).resolve().parent.parent;R=W/'recovery/storage-consolidation'
assert json.loads((R/'SEALED_MUTABLE_HISTORY.json').read_text(encoding='utf-8'))['status']=='mutable-history-text-code-sealed-by-sha256'
lead='''Lưu trữ từ 29/10/2026: đọc STORAGE_POLICY.md và recovery/storage-consolidation/MAINTENANCE.json trước khi tiếp tục. Khi khóa active, chỉ hoàn tất hợp nhất/dọn; khi complete, tiếp nghiên cứu ở tmp/bazi-triad-stars-staging/WORK_STATE.json rồi 六害 từ vị trí209. Không tạo archives/v53-before-* hoặc giữ nhiều full ZIP. Nội dung riêng của các bản cũ tra theo SHA-256 tại recovery/consolidated-history/INDEX.sqlite; phục hồi bằng maintenance/restore-retained-file.py. Các mốc snapshot/kiểm ZIP bên dưới là lịch sử; kiểm hiện hành bằng maintenance/verify-current.py, gói nguồn tổng hợp bằng maintenance/package-latest.py. Bản phát hành V53 giữ nguyên, staging vẫn là công việc dở.\n\n'''
for name in ['WORK_RESUME.md','PROJECT_RESEARCH_STATE.md']:
 p=W/name;old=p.read_text(encoding='utf-8-sig')
 if not old.startswith('Lưu trữ từ 29/10/2026:'):p.write_text(lead+old,encoding='utf-8')
p=W/'PENDING_RESEARCH_STATE.json';d=json.loads(p.read_text(encoding='utf-8-sig'))
d['storageMaintenance']={'authoritativeStatus':'recovery/storage-consolidation/MAINTENANCE.json',
 'policy':'STORAGE_POLICY.md','priorityOverResearchWhileActive':True,
 'consolidatedHistoryIndex':'recovery/consolidated-history/INDEX.sqlite',
 'latestComprehensivePackageManifest':'recovery/storage-consolidation/LATEST_PACKAGE_MANIFEST.json',
 'currentProductVerification':'recovery/storage-consolidation/CURRENT_VERIFICATION.json',
 'previousSourceZIPFactsBelowAreHistorical':True,'chatHistoryUntouched':True}
d['next']=[x.replace('giữ bản cũ','giữ nội dung riêng qua chỉ mục tổng hợp') for x in d.get('next',[])]
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(W/'recovery/consolidated-history/README.md').write_text('''# Lịch sử tổng hợp theo SHA-256

Chính sách 29/10/2026 giữ một gói phát hành mới nhất mỗi loại. Dữ liệu riêng trong 227 ZIP, các tệp lịch sử và đối tượng Git được đối chiếu trước khi bỏ các bản lặp. INDEX.sqlite ánh xạ đường dẫn cũ, từng mục ZIP và Git OID tới SHA-256 và vị trí byte còn giữ. Mỗi nội dung lịch sử riêng có một mục content; nhiều xuất xứ cùng trỏ tới mục đó.

objects/ chứa nội dung lịch sử bất biến. Một số nguồn nhị phân lớn được tham chiếu ở đường dẫn đang dùng trong dự án; phải giữ những đường dẫn đó. Text/code lịch sử đã được niêm phong trong objects trước khi sửa các tệp trạng thái. Các bản HTML dùng trong site/build là bản làm việc hiện hành. v46 còn giữ thư viện mà công cụ nghiên cứu đang tham chiếu; v53 là bản phát hành hiện hành.

Phục hồi từng tệp lịch sử từ thư mục gốc dự án:

```powershell
python maintenance/restore-retained-file.py --container "archives/v53-before-bazi-branch-union/Huyen_Hoc_Cac_V53_source.zip" --member "v53/research/full-study/WORK_STATE.json" --output "tmp/restored-WORK_STATE.json"
```

Cũng có thể dùng --old-path với đường dẫn cũ đã lập chỉ mục. Công cụ từ chối ghi đè, kiểm SHA-256 và chỉ ghi trong dự án. Nội dung từng tệp được giữ đúng byte; không cam kết tái tạo nguyên byte vỏ ZIP/nén của mọi snapshot cũ. Băm vỏ gốc còn trong bảng containers để đối chiếu xuất xứ.

Gói Huyen_Hoc_Cac_V53_source.zip mới là gói tổng hợp dự án: V53, thư viện và nguồn cần dùng, nghiên cứu dở trong tmp, phục hồi chat, chỉ mục và nội dung lịch sử riêng. Đây là cấu trúc rộng hơn ZIP cũ chỉ chứa V53. Công việc staging chưa đồng nghĩa tính năng đã đưa lên web. Các bằng chứng kiểm ZIP cũ giữ giá trị lịch sử; dùng maintenance/verify-current.py cho kiểm hiện hành.

Lịch sử chat Codex trong .codex không bị dọn. Báo cáo kiểm và kết quả dung lượng nằm ở recovery/storage-consolidation/. Trạng thái hoàn tất có thẩm quyền ở MAINTENANCE.json và COMPLETION_RESULT.json ngoài gói.
''',encoding='utf-8')
(R/'NEXT_ACTIONS.md').write_text('''# Tiếp tục hợp nhất hoặc nghiên cứu

Đọc MAINTENANCE.json để biết trạng thái thật, không chạy lại collector chỉ vì đọc mốc cũ. Archives đã lập chỉ mục 227 container; Git đã bảo toàn 10.337 đối tượng. Các thư mục v47–v52 và text/code lịch sử đã gom trước khi cập nhật các chỉ dẫn gốc.

Nếu khóa còn active: đọc COLLECTION_STATE.json, CURRENT_VERIFICATION.json, LATEST_PACKAGE_MANIFEST.json, DELETION_PLAN.json, REMOVED_SNAPSHOTS.json và PRUNED_GIT_CHECKPOINTS.json (nếu có) để tiếp bước chưa đạt. Không khởi chạy hai tiến trình thu thập/đóng gói cùng lúc. Chỉ dọn theo plan đã xác minh. Chạy confirm-git-collection.py trước prune; không xóa nguồn riêng/chat. Kiểm hiện hành, xác minh toàn content và thử phục hồi sau xóa trước finalize-storage.py.

Nếu khóa complete: xem COMPLETION_RESULT.json rồi tiếp phần nghiên cứu đang dở trong PENDING_RESEARCH_STATE.json. Không chạy lại việc hợp nhất đã xong. Không tạo thêm full snapshot; cập nhật nguyên tử gói nguồn tổng hợp khi có phạm vi hữu ích. Giữ STORAGE_POLICY.md.
''',encoding='utf-8')
print('Storage continuation pointers updated; historical originals remain sealed.')
