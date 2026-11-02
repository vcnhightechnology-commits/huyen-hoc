"""Resolve stale private-stage labels; frozen source and fixture files stay byte-identical."""
from pathlib import Path
from hashlib import sha256
import json
W=Path(__file__).resolve().parent.parent
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
changes=[('home-p08-grid-priority','tmp/home-p08-grid-priority-staging'),('home-month-spatial','tmp/home-month-spatial-staging')]
for name,stage in changes:
 s=W/stage/'README.md';d=W/'v53/research'/name/'README.md';text=s.read_text(encoding='utf-8-sig')
 if name=='home-p08-grid-priority':text=text.replace('Phạm vi đang ở nghiên cứu riêng, chưa tiếp nhận vào manifest V53 hoặc site. Tiếp nhận sau khi đóng lô có ích cùng các điều kiện còn mở; không tạo thêm gói ZIP chỉ cho phần nhỏ này. Gói phát hành V53 hiện hành được kiểm theo báo cáo Lưỡng hiện và audit riêng.','Phạm vi đã tiếp nhận vào nghiên cứu V53 trong HOME_SPATIAL_CONTEXT_REPORT.md; không đưa vào site. Gói nguồn tổng hợp được kiểm sau lô có ích cùng các điều kiện mới, không tạo thêm snapshot ZIP. Audit gói tại recovery/research-release/FINAL_VERIFICATION.json phải khớp manifest V53 hiện hành.')
 else:text+='\nĐã tiếp nhận vào nghiên cứu V53 theo HOME_SPATIAL_CONTEXT_REPORT.md. Gói chỉ được gọi là xác minh khi FINAL_VERIFICATION.json khớp manifest hiện hành; dữ liệu nguồn và các kỳ vọng freeze không thay.\n'
 s.write_text(text,encoding='utf-8');d.write_bytes(s.read_bytes())
 p=W/'v53/qa'/name/'PROMOTION_IDENTITIES.json';m=read(p)
 for row in m['byteExactFiles']:
  if row['target']==d.relative_to(W).as_posix():row.update(bytes=d.stat().st_size,sha256=sha256(d.read_bytes()).hexdigest())
 write(p,m)
p=W/'PENDING_RESEARCH_STATE.json';d=read(p);old=d.get('pendingVerifiedResearchScopes',[])
if old:
 assert len(old)==1 and old[0]['file']=='tmp/bazi-triad-stars-staging/WORK_STATE.json'
 assert(W/'v53/qa/bazi-triad-stars/RELEASE_RESULTS.json').is_file()
 d['previousPendingVerifiedResearchScopesBeforeCurrentMetadataSync']=old;d['pendingVerifiedResearchScopes']=[]
 d['pendingVerifiedMetadataDisposition']={'scope':'bazi-triad-stars','status':'already-integrated-earlier;removed-stale-private-claim','report':'v53/BAZI_STARS_HARMS_REPORT.md','sourceOrEngineRerun':False}
write(p,d)
print('Synced current research adoption labels and removed one stale pending-private pointer; frozen source bytes unchanged.')
