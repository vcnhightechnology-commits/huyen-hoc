from pathlib import Path
from hashlib import sha256
import json,sys,subprocess
from PIL import Image,ImageChops
v=Path(__file__).resolve().parent.parent;w=v.parent;r=v/'research/home-activity-clauses';q=v/'qa/home-activity-clauses'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
def identity(p,x):
 b=p.read_bytes();assert len(b)==x['bytes']and sha256(b).hexdigest()==x['sha256'],str(p)
def mapped(p):return r/Path(p).name if p.startswith('tmp/home-activity-clauses-staging/')else w/p
promo=read(r/'PROMOTION_IDENTITIES.json')
for x in promo['files']:identity(r/x['file'],x)
reuse=read(r/'SOURCE_REUSE.json');assert len(reuse['sourceImages'])==6 and reuse['newHTTPBodies']==reuse['newSourcePositions']==0
for x in reuse['sourceImages']+[reuse['digitalBody'],reuse['digitalOriginalHTML']]:identity(w/x['file'],x)
accepted=0;excluded=0
for x in read(r/'NATIVE_CROPS.json')['records']:
 identity(mapped(x['source']['file']),x['source']);identity(mapped(x['crop']['file']),x['crop'])
 assert x['viewed']
 if not x['accepted']:assert x['exclusionReason'];excluded+=1;continue
 a=Image.open(mapped(x['source']['file'])).convert('RGB').crop(x['boxXYXY']);b=Image.open(mapped(x['crop']['file'])).convert('RGB')
 assert ImageChops.difference(a,b).getbbox()is None;accepted+=1
assert accepted==8 and excluded==5
f=read(r/'PREIMPLEMENTATION_FREEZE.json');assert f['implementationExists']is False and len(f['files'])==3
for x in f['files']:identity(r/x['file'],x)
m=read(r/'MANUAL_CLAUSES.json');assert len(m['readings'])==8 and m['sourceCalendarAdapter']is None and m['modernGeometryAdapter']is None
assert m['readings']['fire-water-ge']['implementedPredicate']is None
assert m['readings']['tianhuo']['literal'][1]=='諸曆書並云忌蓋屋蓋寮舍蓋船'
assert '諸書並云' in (w/reuse['digitalBody']['file']).read_text(encoding='utf-8-sig')
e=read(r/'EXPECTED_BEFORE_IMPLEMENTATION.json');assert len(e['manualCases'])==45 and e['writtenBeforeImplementation']is True
proc=subprocess.run(['node',str(r/'test-activity-clause-reference.mjs')],capture_output=True,text=True,encoding='utf-8',check=True)
tests=json.loads(proc.stdout);assert tests==read(r/'REFERENCE_RESULTS.json')==read(q/'REFERENCE_RESULTS.json')
out={'date':'2026-10-29','passed':True,'promotedFilesVerified':len(promo['files']),'reusedSourceImagesVerified':6,'newHTTPBodies':0,'newSourcePositions':0,'newIndependentWitnesses':0,'acceptedNativeCropsRGBMatched':accepted,'excludedTrialCrops':excluded,'preimplementationFilesUnchanged':3,'sourceClauseReadingGroups':8,'implementedClauseGroups':7,'manualExpectedCases':45,'selectedImageDigitalDifference':'image諸曆書/digital諸書','referenceTests':tests,'consumerChanged':False,'wholeWorkApplied':False}
if '--no-write'in sys.argv:assert read(q/'SOURCE_RESULTS.json')==out
else:(q/'SOURCE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,ensure_ascii=False))
