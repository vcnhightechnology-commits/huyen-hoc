from pathlib import Path
from hashlib import sha256
from PIL import Image,ImageChops
import json,sys,tarfile
r=Path(__file__).resolve().parents[1];w=r.parent;b=r/'research/tuvi-ziwei-anchor';q=r/'qa/tuvi-ziwei-anchor'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));sha=lambda p:sha256(p.read_bytes()).hexdigest()
ident=read(b/'PROMOTION_IDENTITIES.json');assert len(ident['records'])==79
for x in ident['records']:
 p=w/x['file'];assert p.stat().st_size==x['bytes']and sha(p)==x['sha256'],x['file']
s=(b/'STAGED_test-ziwei-anchor.mjs').read_text(encoding='utf-8-sig')
for old,new in [("from'./source-ziwei-anchor.mjs'","from'../research/tuvi-ziwei-anchor/source-ziwei-anchor.mjs'"),("const b=resolve(import.meta.dirname),w=resolve(b,'../..'),","const b=resolve(import.meta.dirname,'../research/tuvi-ziwei-anchor'),w=resolve(b,'../../..'),"),("resolve(b,'REFERENCE_RESULTS.json')","resolve(w,'v53/qa/tuvi-ziwei-anchor/REFERENCE_RESULTS.json')"),("x.file.startsWith('tmp/')?resolve(w,x.file):resolve(b,x.file)","resolve(b,x.file.split('/').at(-1))")]:
 assert old in s,old;s=s.replace(old,new)
assert s==(r/'scripts/test-tuvi-ziwei-anchor.mjs').read_text(encoding='utf-8')
src=read(b/'SOURCE_MANIFEST.json');assert sha(w/src['manifestFile'])==src['manifestSHA256'];manifest=read(w/src['manifestFile'])['sequences'][0]['canvases'];assert len(manifest)==129
assert len(src['images'])==40 and {x['canvas']for x in src['images']}=={82,84,86,*range(93,130)};assert len(src['higherResolutionImages'])==3
for x in src['images']+src['higherResolutionImages']:
 p=b/Path(x['file']).name;assert p.stat().st_size==x['bytes']and sha(p)==x['sha256'];assert x['status']==200 and x['TLSCertificateValidationEnabled']and len(x['responseHeaders'])>0
 width=4200 if x in src['higherResolutionImages']else 2200
 assert Image.open(p).width==(3000 if width==4200 else width);assert x['requestedURL']==manifest[x['canvas']-1]['images'][0]['resource']['@id'].replace('/full/max/',f'/full/{width},/')
assert all(x['actuallyViewed']for x in src['images']);assert src['originalJP2Bodies']==0 and src['newIndependentEditionCount']==0
for f in ['DIAGRAM_CROPS.json','HIRES_CROPS.json','NUMERAL_CROPS.json']:
 for x in read(b/f):
  source=b/Path(x['source']).name
  if not source.exists():source=w/x['source']
  dest=b/x.get('file',f"diagram-{x['name']}-native.png")if 'name'in x else b/x['file']
  assert x['viewed']and x['pixelMatch'];assert ImageChops.difference(Image.open(source).convert('RGB').crop(x['box']),Image.open(dest).convert('RGB')).getbbox()is None
  if 'sha256'in x:assert sha(dest)==x['sha256']
initial=read(b/'INITIAL_TRANSCRIPTION_FREEZE.json');assert initial['runtimeCallsThisScopeAtFreeze']==0 and sha(b/'INITIAL_ZIWEI_DAY_DIAGRAMS.json')==initial['sha256'];assert sha(b/'ZIWEI_DAY_DIAGRAMS.json')==read(b/'TRANSCRIPTION_FREEZE.json')['sha256']
tab=read(b/'ZIWEI_DAY_DIAGRAMS.json');assert len(tab['records'])==5 and tab['printedCoordinates']==150
lookup={}
for x in tab['records']:
 assert sorted(d for c in x['cells']for d in c['dayNumeralsNormalized'])==list(range(1,31))
 for c in x['cells']:
  for d in c['dayNumeralsNormalized']:lookup[x['cucNumber'],d]=c['branch']
corr=read(b/'READING_CORRECTIONS.json');assert len(corr['corrections'])==4 and not corr['consumerAffected'];assert {(x['branch'],x['correctedDecimal'],x['literal'])for x in corr['corrections']}=={('巳',14,'十四'),('午',17,'十七'),('酉',24,'廿四'),('戌',27,'廿七')}
res=read(q/'REFERENCE_RESULTS.json');old=read(b/'INITIAL_REFERENCE_RESULTS.json');assert len(res['checks'])==6 and all(x['ok']for x in res['checks']);assert len(old['mismatches'])==4 and not res['mismatches'];assert res['actualHHCTuviCalls']==160 and res['hhcSelectionCalls']==10 and res['hhcSourceComparisonCalls']==150 and res['actualIztroNatalCalls']==150;assert res['postCorrectionChartInvocations']==0
assert len(res['runtime'])==150 and {(x['cuc'],x['input']['d'])for x in res['runtime']}==set(lookup)
for a,z in zip(old['runtime'],res['runtime']):
 for k in ['input','solar','cuc','iztroCuc','hhcBranch','iztroBranch']:assert a[k]==z[k]
 assert z['source']['branch']==z['hhcBranch']==z['iztroBranch']==lookup[z['cuc'],z['input']['d']]
 assert z['source']['practicalOutcome']is None
assert sha(r/'engine.js')==res['engineSHA256']=='39f08bd1887faca4d35f7ad415ebf596621010d530b489212774d5cbf99040e6'
proof=read(r/'research/tuvi-masters/SOURCE_MANIFEST.json');tgz=w/proof['runtimeTarball'];assert sha(tgz)==proof['runtimeTarballSHA256']=='d44e96631c0506424c3aef25a7bba8e43e01729102d6a703720cbe224aec5403'
with tarfile.open(tgz,'r:gz')as t:
 for x in proof['runtime']:
  p=w/x['file'];assert p.stat().st_size==x['bytes']and sha(p)==x['sha256'];assert p.read_bytes()==t.extractfile('package/'+x['file'].split('/iztro/',1)[1]).read()
assert len(proof['runtime'])==4
inv=read(b/'CURRENT_CANVAS_INVENTORY.json');assert len(inv['records'])==129 and all(x['retainedDerivatives']and x['firstPassViewedIncludingPreviousScopes']for x in inv['records'])
for x in inv['records']:
 for z in x['retainedDerivatives']:assert sha(w/z['file'])==z['sha256']
first=read(b/'FIRST_PASS_READINGS.json');assert len(first['records'])==56 and first['newPositionsViewed']==40 and first['priorPositionsExpanded']==16 and first['printedBodyLastCanvas']==127;assert first['endpaperFragmentCanvas']==128 and first['blankRearSurfaceCanvas']==129 and not first['wholeItemRulesApplied']and not first['allSixJuanBodyPresentInThisItem']
state=read(b/'WORK_STATE.json');assert not state['wholeCatalogueCompleted']and not state['consumerChanged']and not state['wholeItemRulesApplied']
out=dict(date='2026-10-28',promotionIdentities=79,newInstitutionJPEGDerivativeBodies=43,headerSets=43,newDistinctPositions=40,priorPositionsExpanded=16,continuousPhysicalPositionsFirstPassViewed=129,retainedDistinctPositions=129,printedBodyLastCanvas=127,endpaperFragmentCanvas=128,blankRearSurfaceCanvas=129,nativeCropsViewedPixelMatched=14,sourceCoordinates=150,sourceCoordinatesMatchedBothEngines=150,individualEngineBranchChecks=300,actualHHCTuviCalls=160,hhcSelectionCalls=10,actualIztroNatalCalls=150,actualRuntimeBatchInvocations=1,postCorrectionActualChartCalls=0,manualNumeralCorrections=4,completeFinalChecks=6,pinnedIztroRuntimeFiles=4,requestedHigherResolutionWidth=4200,actualHigherResolutionWidth=3000,originalJP2Bodies=0,newIndependentEditions=0,consumerChanged=False,wholeItemRulesApplied=False,wholeCatalogueCompleted=False)
p=q/'SOURCE_RESULTS.json'
if '--no-write'in sys.argv:assert read(p)==out
else:p.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
