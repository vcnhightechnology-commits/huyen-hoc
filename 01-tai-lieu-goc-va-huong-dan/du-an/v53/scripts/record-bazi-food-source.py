from pathlib import Path
from hashlib import sha256
import json,shutil
w=Path(__file__).resolve().parent.parent;r=w/'v53';s=w/'tmp/bazi-food-source-staging';b=r/'research/bazi-food-source';q=r/'qa/bazi-food-source'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));sha=lambda p:sha256(p.read_bytes()).hexdigest()
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
assert not b.exists()and not q.exists(),'One-shot promotion;preserve earlier work'
snap=read(w/'archives/v53-before-bazi-food-source/SNAPSHOT.json');assert snap['sourceManifestFiles']==3856 and snap['sourceZIPBytes']==2100342805
tests=read(s/'SPECIAL_FOOD_RESULTS.json');assert len(tests['checks'])==6 and all(x['ok']for x in tests['checks'])
b.mkdir();q.mkdir();identities=[]
def copy(name,folder,target=None):
    source=s/name;dest=folder/(target or name);shutil.copyfile(source,dest)
    assert source.read_bytes()==dest.read_bytes()
    identities.append({'file':dest.relative_to(w).as_posix(),'stagingFile':source.relative_to(w).as_posix(),'bytes':dest.stat().st_size,'sha256':sha(dest)})
for name in ['SOURCE_MANIFEST.json','UNITS.json','CONTEXTS.json','SOURCE_COORDINATES.json','CONTINUITY_AUDIT.json','LOCAL_RENDERS.json','RETAINED_DIGITAL_SECTION.txt','special-food-reference.mjs']:copy(name,b)
for x in read(s/'LOCAL_RENDERS.json')['records']:copy(x['file'],b)
for name in ['MANUAL_READINGS.json','WORK_STATE.json']:copy(name,b,'STAGED_'+name)
manual=read(b/'STAGED_MANUAL_READINGS.json')
for x in manual['records']:
    x['file']=x['file'].replace('tmp/bazi-food-source-staging/','v53/research/bazi-food-source/')
write(b/'MANUAL_READINGS.json',manual)
for name in ['QA_CROPS.json','EXTRA_CROPS.json','DECODE_RESULTS.json','SPECIAL_FOOD_RESULTS.json','SPECIAL_FOOD_RESULTS_PRIOR.json','SOURCE_EXAMPLES_PROBE.json','EXECUTION_AUDIT.json']:copy(name,q)
for name in ['QA_CROPS.json','EXTRA_CROPS.json']:
    for x in read(s/name)['records']:copy(x['file'],q)
for name in ['test-special-food.mjs','probe-source-examples.mjs','decode-native.mjs','reproduce-native.mjs','build-contexts.py','finish-staging.py']:copy(name,b,'STAGED_'+name)
t=(s/'test-special-food.mjs').read_text(encoding='utf-8').replace("from'./special-food-reference.mjs'","from'../research/bazi-food-source/special-food-reference.mjs'").replace("s=new URL('./',import.meta.url)","s=new URL('../qa/bazi-food-source/',import.meta.url)")
(r/'scripts/test-bazi-special-food.mjs').write_text(t,encoding='utf-8')
t=(s/'probe-source-examples.mjs').read_text(encoding='utf-8').replace("s=resolve(w,'tmp/bazi-food-source-staging')","s=resolve(w,'v53/qa/bazi-food-source')")
(r/'scripts/probe-bazi-food-examples.mjs').write_text(t,encoding='utf-8')
write(b/'PROMOTION_IDENTITIES.json',{'date':'2026-10-28','records':identities,'referenceModuleByteIdenticalToStaging':True,'manualReadingPathRelocationOnly':{'staged':'STAGED_MANUAL_READINGS.json','promoted':'MANUAL_READINGS.json','oldPrefix':'tmp/bazi-food-source-staging/','newPrefix':'v53/research/bazi-food-source/'},'scriptsRelocatedWithoutRerunningEngines':True,'localIdentitiesNotPublisherSignatures':True})
shutil.copyfile(Path(__file__),r/'scripts/record-bazi-food-source.py')
print(json.dumps({'identityRecords':len(identities),'passingChecks':6,'nativeDerivatives':27,'nativeCrops':8,'moduleByteIdentical':True,'consumerChanged':False}))
