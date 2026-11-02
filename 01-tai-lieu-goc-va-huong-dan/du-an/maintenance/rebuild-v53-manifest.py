from pathlib import Path
from hashlib import sha256
import json
W=Path(__file__).resolve().parent.parent;V=W/'v53';p=V/'PACKAGE_MANIFEST.json';m=json.loads(p.read_text(encoding='utf-8-sig'));files=[]
for f in sorted(V.rglob('*')):
 if not f.is_file() or f==p:continue
 h=sha256()
 with f.open('rb') as src:
  for b in iter(lambda:src.read(8*1024*1024),b''):h.update(b)
 files.append({'file':f.relative_to(V).as_posix(),'bytes':f.stat().st_size,'sha256':h.hexdigest()})
m['files']=files;m['policy']='SHA-256 file identities, not publisher signatures. Research stays outside site/. One comprehensive latest source ZIP under STORAGE_POLICY.md; historical unique bytes retained by consolidated index.'
p.write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps({'manifestFiles':len(files),'sourceZIPBuildNotStarted':True}))
