from pathlib import Path
from hashlib import sha256
import json,shutil
w=Path.cwd();r=w/'v53';s=w/'tmp/home-yangzhai-shishu-staging';b=r/'research/home-yangzhai-shishu';q=r/'qa/home-yangzhai-shishu'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));sha=lambda p:sha256(p.read_bytes()).hexdigest()
assert not b.exists()and not q.exists();snap=read(w/'archives/v53-before-home-yangzhai-shishu/SNAPSHOT.json');assert snap['sourceManifestFiles']==3948 and snap['sourceZIPBytes']==2107772251
assert len(read(s/'LAYER_RESULTS.json')['checks'])==6 and all(x['ok']for x in read(s/'LAYER_RESULTS.json')['checks'])and read(s/'NATIVE_RESULTS.json')['rawDCTStreamIdentitiesVerified']==40
b.mkdir();q.mkdir();ids=[]
def copy(p,dest):
    shutil.copyfile(p,dest);assert p.read_bytes()==dest.read_bytes();ids.append({'file':dest.relative_to(w).as_posix(),'stagingFile':p.relative_to(w).as_posix(),'bytes':dest.stat().st_size,'sha256':sha(dest)})
qa={'CROPS.json','RAW_CROPS.json','NATIVE_RESULTS.json','LAYER_RESULTS.json','NATIVE_FAILURE_AUDIT.json'}
crops={x['file']for name in ['CROPS.json','RAW_CROPS.json']for x in read(s/name)['records']}
for p in sorted(s.iterdir()):
    if not p.is_file():continue
    if p.name in qa or p.name in crops:dest=q/p.name
    elif p.name=='WORK_STATE.json':dest=b/'STAGED_WORK_STATE.json'
    elif p.suffix in ['.py','.mjs']and p.name!='layer-coordinate-reference.mjs':dest=b/('STAGED_'+p.name)
    else:dest=b/p.name
    copy(p,dest)
copy(w/'tmp/fetch-home-yangzhai-shishu.mjs',b/'STAGED_fetch-home-yangzhai-shishu.mjs')
original=(s/'test-layer-coordinate.mjs').read_text(encoding='utf-8');test=original.replace("from'./layer-coordinate-reference.mjs'","from'../research/home-yangzhai-shishu/layer-coordinate-reference.mjs'").replace("new URL('LAYER_RESULTS.json',import.meta.url)","new URL('../qa/home-yangzhai-shishu/LAYER_RESULTS.json',import.meta.url)");(r/'scripts/test-home-yangzhai-layer-coordinate.mjs').write_text(test,encoding='utf-8')
out={'date':'2026-10-28','records':ids,'moduleByteIdenticalToStaging':True,'testOnlyImportAndOutputPathsChanged':True,'originalPDFByteIdenticalToStagingAndHTTPResponse':True,'pypdfDerivativesNotRawImages':True,'passedTestsNotRerunForCounts':True,'localIdentitiesNotPublisherSignatures':True}
(b/'PROMOTION_IDENTITIES.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');shutil.copyfile(Path(__file__),r/'scripts/record-home-yangzhai-shishu.py')
print(json.dumps({'promotionIdentities':len(ids),'PDFBytes':(b/'Tianyige-330000-1705-0007405-yangzhai-shishu.pdf').stat().st_size,'derivativesViewed':40,'rawSourceCropsViewed':4,'sourceStreamIdentityCount':40}))
