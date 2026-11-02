from pathlib import Path
from hashlib import sha256
import json, shutil
w=Path.cwd();a=w/'archives/v53-before-tuvi-ming-shen'
assert not a.exists();a.mkdir()
def digest(p):
 h=sha256()
 with p.open('rb') as f:
  for block in iter(lambda:f.read(4*1024*1024),b''):h.update(block)
 return h.hexdigest()
records=[]
for name,src in [('Huyen_Hoc_Cac_V53_source.zip',w/'Huyen_Hoc_Cac_V53_source.zip'),
 ('Huyen_Hoc_Cac_V53_web.zip',w/'Huyen_Hoc_Cac_V53_web.zip'),
 ('PACKAGE_MANIFEST.json',w/'v53/PACKAGE_MANIFEST.json'),
 ('Huyen_Hoc_Cac.html',w/'Huyen_Hoc_Cac.html'),
 ('EXHAUSTIVE_WORK_STATE.json',w/'EXHAUSTIVE_WORK_STATE.json')]:
 dst=a/name;shutil.copyfile(src,dst)
 assert src.stat().st_size==dst.stat().st_size and digest(src)==digest(dst)
 records.append(dict(file=name,bytes=dst.stat().st_size,sha256=digest(dst)))
assert len(json.loads((a/'PACKAGE_MANIFEST.json').read_text(encoding='utf-8'))['files'])==4842
assert records[0]['bytes']==2706138912
(a/'SNAPSHOT.json').write_text(json.dumps(dict(date='2026-10-28',sourceManifestFiles=4842,
 sourceZIPBytes=2706138912,localIdentitiesNotPublisherSignatures=True,files=records),indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(preservedFiles=5,sourceManifestFiles=4842,sourceZIPBytes=2706138912)))
