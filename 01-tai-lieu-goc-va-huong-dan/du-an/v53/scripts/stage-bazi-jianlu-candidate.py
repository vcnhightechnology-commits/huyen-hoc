from pathlib import Path
from hashlib import sha256
import json,shutil,zipfile
r=Path(__file__).resolve().parent.parent;w=r.parent;a=w/'archives/v53-before-bazi-jianlu-context';b=r/'research/bazi-jianlu-context';c=b/'consumer-candidate'
assert c.resolve().is_relative_to(w.resolve())
c.mkdir(exist_ok=False)
names=['Huyen_Hoc_Cac.html','bazi-month-context.js','bazi-cycles.js','bazi-locations.css','index.html','scripts/build.mjs']
for name in names:
 src=r/name;dest=c/name;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dest)
# Restore only files changed in this scope. Historical release sources and the
# user HTML remain byte-identical; the new standalone candidate is preserved.
old=json.loads((a/'PACKAGE_MANIFEST.json').read_text(encoding='utf-8'))
with zipfile.ZipFile(a/'Huyen_Hoc_Cac_V53_source.zip')as z:
 for name in names:
  if name=='bazi-month-context.js':continue
  raw=z.read('v53/'+name);assert sha256(raw).hexdigest()==next(x['sha256']for x in old['files']if x['file']==name)
  (r/name).write_bytes(raw)
# Move the new unreferenced module to its preserved candidate folder. Both
# checked absolute paths are inside the workspace; no recursive operation.
unused=r/'bazi-month-context.js';assert unused.resolve().is_relative_to(w.resolve())
assert unused.read_bytes()==(c/'bazi-month-context.js').read_bytes()
unused.replace(c/'bazi-month-context.js')
out={'date':'2026-10-27','status':'functional-candidate-verified-visual-integration-pending',
 'candidateStandalone':'v53/research/bazi-jianlu-context/consumer-candidate/Huyen_Hoc_Cac.html',
 'playwrightLaunch':'spawn EPERM','inAppBrowser':'Local browser use disabled in Work settings',
 'browserTestsPassed':False,'visualQAComplete':False,'pdfQAComplete':False,'consumerChanged':False,
 'currentHTMLBytes':len((r/'Huyen_Hoc_Cac.html').read_bytes()),'candidateHTMLBytes':len((c/'Huyen_Hoc_Cac.html').read_bytes()),
 'next':'When a browser is available, run the candidate browser test, inspect screenshots/PDF, then integrate the preserved files; do not present current UI as updated.'}
(b/'CANDIDATE_STATUS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,ensure_ascii=False))
