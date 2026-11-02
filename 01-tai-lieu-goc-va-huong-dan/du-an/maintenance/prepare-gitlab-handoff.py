"""Prepare one text checkout for the user-requested GitLab handoff; do not copy binary bundles."""
from pathlib import Path
import hashlib, json, shutil, subprocess

W = Path(__file__).resolve().parent.parent
OUT = Path('\\\\?\\'+str(W / 'tmp/gitlab-handoff'))
PROJECT = OUT / '01-tai-lieu-goc-va-huong-dan/du-an'
BRANCHES = OUT / '02-nghien-cuu-13-nhanh'
RECOVERY = 'collaboration/imports/recovery-13-branches-2026-11-01'
URL = 'https://gitlab.com/hung-group7524844/huyen-hoc-project'

def write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding='utf-8', newline='\n')

def dump(path, obj):
    write(path, json.dumps(obj, ensure_ascii=False, indent=2)+'\n')

cmd = ['git', '-c', 'safe.directory='+W.as_posix()]
tracked = subprocess.check_output(cmd+['ls-files', '-z'], cwd=W).decode().split('\0')
untracked = subprocess.check_output(cmd+['ls-files', '--others', '--exclude-standard', '-z'], cwd=W).decode().split('\0')
files = sorted(set(p for p in tracked+untracked if p))
records = []
excluded = {'.pdf','.djvu','.zip','.png','.jpg','.jpeg','.webp','.sqlite','.exe','.dll','.7z','.rar','.jp2','.tif','.tiff','.gif','.pyc','.pem','.key'}
for rel in files:
    src = W / rel
    if not src.is_file():
        continue
    if src.suffix.lower() in excluded or src.name.startswith('.env') and src.name != '.env.example':
        raise ValueError('Unexpected binary/credential in Git selection: '+rel)
    dst = PROJECT / rel
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dst)
    records.append({'file': rel, 'bytes': src.stat().st_size, 'sha256':hashlib.file_digest(src.open('rb'),'sha256').hexdigest()})

write(OUT/'README.md', '''# Huyền Học Các — bàn giao cộng tác GitLab

Kho được sắp xếp theo yêu cầu chủ dự án ngày 02/11/2026.

1. [Tài liệu gốc, mã dự án và hướng dẫn chung](01-tai-lieu-goc-va-huong-dan/README.md).
2. [13 mục nghiên cứu dành cho các AI](02-nghien-cuu-13-nhanh/README.md).

Mỗi AI đọc AGENTS.md và quy trình phối hợp trước, chọn đúng AI-01…AI-13 rồi tạo nhánh Git `codex/ai-xx-ten-viec`. Ưu tiên trực tiếp hiện hành là AI-01. Tệp nguồn lớn được cung cấp qua Package Registry, có danh mục byte/SHA-256 trong mục 1; không đưa chúng vào Git.

Các hồ sơ được nhập từ máy chủ dự án, bao gồm công việc chưa commit ở máy đó. Chỉ mục bàn giao xác nhận byte của tập được chuyển; không xác nhận mọi luận điểm cổ thư hoặc toàn bộ dự án đã hoàn tất. Các liên kết GitHub/PR cũ bên trong tài liệu gốc là lịch sử. Nơi cộng tác mới là kho GitLab này.
''')
write(OUT/'AGENTS.md', '''# Hướng dẫn cho mọi AI

- Gốc mã nguồn vận hành là `01-tai-lieu-goc-va-huong-dan/du-an/`. Chạy lệnh của dự án tại đó, đọc AGENTS.md và STORAGE_POLICY.md trong gốc này.
- Đọc `01-tai-lieu-goc-va-huong-dan/HUONG_DAN_PHOI_HOP.md` và README của đúng mục AI trong `02-nghien-cuu-13-nhanh/`.
- Mỗi AI chỉ ghi trong phạm vi đã nhận trên nhánh `codex/ai-xx-ten-viec`; mở Merge Request để tích hợp. Không tự merge hoặc force-push nhánh chung.
- Giữ nguyên nguồn gốc, byte/SHA-256, dị bản, quy ước và phần chưa xác minh. Không thực thi patch/mã trích chưa xác minh.
- Nguồn/corpus/phòng kiểm định nằm ngoài site. Chỉ sửa engine khi đủ tiền đề, chạy engine thật và kiểm phù hợp. Ghi giới hạn kiểm chứng.
- Một bộ nguồn tổng hợp dùng chung cho 13 AI. Không sao chép full ZIP hoặc tải lại batch đã lưu. Không xóa tư liệu duy nhất/lịch sử chat.
''')
write(OUT/'.gitignore', '/.publish-state/\n**/node_modules/\n**/__pycache__/\n*.pyc\n*.zip\n*.pdf\n*.djvu\n*.png\n*.jpg\n*.jpeg\n*.webp\n*.sqlite\n.env\n.env.*\n*.pem\n*.key\n')
write(OUT/'01-tai-lieu-goc-va-huong-dan/README.md', '''# Tài liệu gốc và hướng dẫn cho các AI

- [Quy trình phối hợp](HUONG_DAN_PHOI_HOP.md).
- [Mã và tài liệu dự án giữ nguyên cấu trúc đường dẫn](du-an/README.md).
- [Trạng thái nghiên cứu](du-an/PROJECT_RESEARCH_STATE.md), [trạng thái máy đọc](du-an/EXHAUSTIVE_WORK_STATE.json), [độ phủ](du-an/v53/research/library-current/COVERAGE.json).
- [Danh mục sách nguồn](du-an/collaboration/materials/SOURCE_BOOKS.md), [manifest lịch sử nguồn tổng hợp](du-an/collaboration/materials/MANIFEST.json).
- [Danh mục tải từ GitLab](GITLAB_MATERIALS.json). Chỉ xem tư liệu là đã bàn giao trực tuyến khi `PUBLICATION_STATUS.json` ghi uploaded và từng asset đã kiểm SHA từ remote.
- [Chỉ mục byte checkout bàn giao](HANDOFF_FILES.json).

Các PDF/DjVu/ảnh và 11 ZIP dùng chung được tải từ Generic Package Registry của chính kho GitLab; chúng giữ byte nguồn đã có. Dùng `python restore-materials.py --list` để liệt kê hoặc `--file TEN --destination THU_MUC` để tải một asset và kiểm SHA-256. Sau đó dùng công cụ phục hồi của dự án với cache ZIP local. Với kho riêng tư, đặt GITLAB_TOKEN trong môi trường của máy thực thi; không ghi token vào tệp hoặc chat.

Bản nguồn 31/10 là mốc lưu trữ, còn mã/văn bản trong `du-an/` là trạng thái checkout khi bàn giao 02/11. Các thay đổi mới và nguồn bổ sung được ghi trong manifest bàn giao. Bằng chứng chưa tải thành công vẫn mang trạng thái mở.
''')
write(OUT/'01-tai-lieu-goc-va-huong-dan/HUONG_DAN_PHOI_HOP.md', '''# Quy trình phối hợp nghiên cứu

1. Đọc AGENTS.md ở gốc kho, rồi vào `du-an/` đọc chính sách lưu trữ, trạng thái nghiên cứu, NEXT_STEPS và ma trận độ phủ. Các con trỏ M01 cũ được giữ; yêu cầu mới đang ưu tiên AI-01.
2. Chọn README của một trong 13 mục. Đọc hồ sơ phục hồi và thư mục submission được dẫn; ghi rõ phạm vi đang nhận trong `WORK_LOG.md` của mục đó trên nhánh riêng.
3. Mở nhánh `codex/ai-xx-ten-viec` từ nhánh chung hiện hành. Xác nhận base commit; tránh sửa chồng engine hoặc trạng thái chung với AI khác. Đề xuất thay đổi trạng thái chung qua Merge Request.
4. Lấy đúng nguồn theo manifest, kiểm SHA-256 trước đọc. Phân biệt nguồn gốc, bản chép, ảnh dẫn xuất, quy ước, suy luận và chưa xác minh. Lưu tọa độ trang/tờ, URL và phần ảnh đã thực sự đọc. Không đếm URL hoặc bản chép web thành truyền bản độc lập.
5. Mỗi luận điểm ghi đầy đủ điều kiện, ngoại lệ, chủ thể và vị trí trụ. Không lấp chỗ thiếu bằng kiến thức hiện đại hoặc điểm số tùy ý. Quy tắc chưa đủ điều kiện giữ trong nghiên cứu, không đưa thành kết luận tự động.
6. Nếu thay mã, thực thi engine thật và kiểm phù hợp. Tái dùng payload đã giữ khi có thể; không tự gọi số kiểm lịch sử là kiểm hiện tại. Không đưa corpus, QA hay bảng so engine lên giao diện người dùng.
7. Cập nhật WORK_LOG, nguồn, câu hỏi mở, kết quả kiểm và bước tiếp. Merge Request ghi rõ tệp sửa, căn cứ, giới hạn, dữ liệu cần tải thêm. Không tự merge hoặc tạo nhiều bản ZIP phát hành.

Hồ sơ phục hồi có 3/33 tài sản byte gốc; 25 bản trích chưa xác minh byte và 5 tài sản chưa lấy được. AI-10 mới có 13/24 tệp kiểm theo hồ sơ. Không thực thi mã trích để chứng minh các số cũ. Những giới hạn này phải tiếp tục đi theo kết quả nghiên cứu.

Lưu ý AI-01: ghi chú đối ảnh mới nhất đã cập nhật cách đọc can tháng ở scan NLC 06857 p.50; một số hồ sơ cũ vẫn ghi chưa phân xử. Ưu tiên báo cáo facsimile hiện hành, giữ lịch sử trước đó và chưa coi dị văn là một luật engine.
''')
rows=[]
for i in range(1,14):
    aid=f'AI-{i:02d}'
    b=json.loads((W/RECOVERY/'branches'/aid/'BRANCH.json').read_text('utf-8-sig'))
    link=f'../../01-tai-lieu-goc-va-huong-dan/du-an/{RECOVERY}/branches/{aid}'
    text=f'''# {aid} — {b['name']}

Đây là mục phối hợp hiện hành của {aid}. Hồ sơ nguồn được giữ một bản tại mục 1.

- [Việc cần tiếp tục]({link}/NEXT_RESEARCH.md).
- [Bàn giao khôi phục]({link}/HANDOFF.md).
- [Metadata và giới hạn]({link}/BRANCH.json).
- [Quy trình chung](../../01-tai-lieu-goc-va-huong-dan/HUONG_DAN_PHOI_HOP.md).

Tạo nhánh `codex/{aid.lower()}-ten-viec`. Ghi công việc và kết quả mới trong thư mục này; đề xuất sửa mã trong gốc `01-tai-lieu-goc-va-huong-dan/du-an/`. Tài liệu được trỏ bằng liên kết tương đối để giữ một bản nguồn có thẩm quyền. Ref PR/Git trong hồ sơ cũ là lịch sử.
'''
    if i==1:
        text+=f'\nƯu tiên hiện tại: [Đối ảnh mới nhất]({link}/AI01_FACSIMILE_COLLATION_2026-11-01.md), [sổ 20 đơn vị Chính Ấn]({link}/AI01_WXJJ_VOL19_SEAL_UNIT_LEDGER_2026-11-01.json), [submission AI-01](../../01-tai-lieu-goc-va-huong-dan/du-an/collaboration/parallel-research/submissions/AI-01/). Có ghi chú mới về p.33 trực tuyến và cách đọc `己卯` ở NLC 06857 p.50; chưa đưa vào engine.\n'
    write(BRANCHES/aid/'README.md',text)
    write(BRANCHES/aid/'WORK_LOG.md',f'# {aid} — nhật ký phối hợp\n\nChưa có AI nhận việc qua kho GitLab. Điền base commit, phạm vi nhận, nguồn đã đọc, thay đổi, kiểm chứng, trở ngại và bước tiếp trong nhánh làm việc. Không ghi việc tải lên thành nghiên cứu đã hoàn thành.\n')
    rows.append({'id':aid,'name':b['name'],'directory':f'02-nghien-cuu-13-nhanh/{aid}','status':'open-unassigned','sourceDossier':f'01-tai-lieu-goc-va-huong-dan/du-an/{RECOVERY}/branches/{aid}'})
write(BRANCHES/'README.md','# 13 mục nghiên cứu cho các AI\n\nMỗi mục có điểm vào, hồ sơ và nhật ký riêng. Nhánh Git được tạo khi nhận việc; các mục dưới đây là thư mục phối hợp.\n\n'+'\n'.join(f"- [{b['id']} — {b['name']}]({b['id']}/README.md)" for b in rows)+'\n')
dump(BRANCHES/'BRANCHES.json',rows)
dump(OUT/'01-tai-lieu-goc-va-huong-dan/HANDOFF_FILES.json',{'date':'2026-11-02','sourceHead':subprocess.check_output(cmd+['rev-parse','HEAD'],cwd=W,text=True).strip(),'includesWorkingTreeEdits':True,'files':records})
m=json.loads((W/'collaboration/materials/MANIFEST.json').read_text('utf-8-sig'))
assets=[dict(b,local=str(W/'tmp/materials-handoff'/b['file'])) for b in m['bundles']]
for p in (W/'v53/research/bazi-relations/evidence/facsimiles').glob('*'):
    if p.is_file():
        assets.append({'file':p.name,'bytes':p.stat().st_size,'sha256':hashlib.file_digest(p.open('rb'),'sha256').hexdigest(),'local':str(p)})
for p in [Path.home()/'Downloads/HUYEN_HOC_CAC_AI01_TONG_HOP_TOAN_BO_TAI_LIEU_2026-10-31.zip', W/'recovery/research-recovery/2026-11-01/HUYEN_HOC_01_13_NOI_DUNG_NGHIEN_CUU_KHOI_PHUC_2026-11-01.zip']:
    if p.is_file():
        assets.append({'file':p.name,'bytes':p.stat().st_size,'sha256':hashlib.file_digest(p.open('rb'),'sha256').hexdigest(),'local':str(p)})
for a in assets:
    a['url']='https://gitlab.com/api/v4/projects/hung-group7524844%2Fhuyen-hoc-project/packages/generic/hhc-materials/2026-11-02/'+a['file']
dump(OUT/'01-tai-lieu-goc-va-huong-dan/GITLAB_MATERIALS.json',{'schema':'hhc.gitlab.materials.v1','project':URL,'assets':[{k:v for k,v in a.items() if k!='local'} for a in assets]})
shutil.copyfile(W/'maintenance/gitlab-restore-materials.py',OUT/'01-tai-lieu-goc-va-huong-dan/restore-materials.py')
dump(W/'tmp/gitlab-upload-plan.json',{'checkout':str(OUT),'project':URL,'assets':assets})
dump(OUT/'PUBLICATION_STATUS.json',{'status':'prepared-awaiting-gitlab-authentication','date':'2026-11-02','gitPushed':False,'binaryAssetsUploaded':False})
print(json.dumps({'checkout':str(OUT),'textFiles':len(records),'textBytes':sum(r['bytes'] for r in records),'researchSections':len(rows),'assets':len(assets),'assetBytes':sum(a['bytes'] for a in assets)},ensure_ascii=False))
