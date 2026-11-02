from pathlib import Path
from hashlib import sha256
import json,shutil
w=Path.cwd();r=w/'v53';s=w/'tmp/home-yangzhai-fuyuan-staging'
b=r/'research/home-yangzhai-fuyuan';q=r/'qa/home-yangzhai-fuyuan'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
assert not b.exists() and not q.exists()
snap=read(w/'archives/v53-before-home-yangzhai-fuyuan/SNAPSHOT.json')
assert snap['sourceManifestFiles']==4074 and snap['sourceZIPBytes']==2340565337
result=read(s/'REFERENCE_RESULTS.json');assert len(result['checks'])==8 and all(x['ok'] for x in result['checks'])
assert read(s/'NATIVE_RESULTS.json')['rawDCTStreamIdentitiesVerified']==48
b.mkdir();q.mkdir();identities=[]
def copy(p,d):
    shutil.copyfile(p,d);assert p.read_bytes()==d.read_bytes()
    identities.append({'file':d.relative_to(w).as_posix(),'stagingFile':p.relative_to(w).as_posix(),
     'bytes':d.stat().st_size,'sha256':sha256(d.read_bytes()).hexdigest()})
qa={'QA_IMAGES.json','NATIVE_RESULTS.json','REFERENCE_RESULTS.json','TEST_FAILURE_AUDIT.json'}
for p in sorted(s.iterdir()):
    if not p.is_file():continue
    if p.name=='REPORT.md':d=r/'HOME_FUYUAN_YOUNIAN_REPORT.md'
    elif p.name in qa:d=q/p.name
    elif p.name=='WORK_STATE.json':d=b/'STAGED_WORK_STATE.json'
    elif p.suffix in ['.py','.mjs'] and p.name!='fuyuan-younian-reference.mjs':d=b/('STAGED_'+p.name)
    else:d=b/p.name
    copy(p,d)
for p in sorted((s/'qa').iterdir()):copy(p,q/p.name)
test=(s/'test-reference.mjs').read_text(encoding='utf-8')
test=test.replace("from './fuyuan-younian-reference.mjs'","from '../research/home-yangzhai-fuyuan/fuyuan-younian-reference.mjs'")
test=test.replace("const b=import.meta.dirname,w=resolve(b,'../..'),r=resolve(w,'v53');","const b=resolve(import.meta.dirname,'../research/home-yangzhai-fuyuan'),w=resolve(b,'../../..'),r=resolve(w,'v53');")
test=test.replace("resolve(b,'REFERENCE_RESULTS.json')","resolve(r,'qa/home-yangzhai-fuyuan/REFERENCE_RESULTS.json')")
(r/'scripts/test-home-fuyuan-younian.mjs').write_text(test,encoding='utf-8')
(b/'PROMOTION_IDENTITIES.json').write_text(json.dumps({'date':'2026-10-28','records':identities,
 'moduleByteIdenticalToStaging':True,'testOnlyThreePathRelocations':True,'passedRuntimeTestsNotRerunOnPromotion':True,
 'localIdentitiesNotPublisherSignatures':True},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'promotionIdentities':len(identities),'rawImages':48,'crops':12,'completeChecks':8}))
