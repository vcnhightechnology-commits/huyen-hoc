from pathlib import Path
from hashlib import sha256
from PIL import Image
import json,subprocess,sys
v=Path(__file__).resolve().parent.parent;w=v.parent;r=v/'research/home-general-premises';q=v/'qa/home-general-premises';read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
def digest(p):
 h=sha256()
 with p.open('rb')as f:
  for b in iter(lambda:f.read(4*1024*1024),b''):h.update(b)
 return h.hexdigest()
ids=read(r/'PROMOTION_IDENTITIES.json')
for x in ids['files']:
 p=w/x['file'];assert p.stat().st_size==x['bytes']and digest(p)==x['sha256'],x['file']
requests=read(r/'REQUESTS.json');assert len(requests)==23
for x in requests:
 p=r/x['file'];assert x['status']==200 and x['standardTLSValidation'];assert p.stat().st_size==x['bytes']and digest(p)==x['sha256'];assert x['url'].startswith('https://db.itkc.or.kr/')
for n in range(257,267):
 im=Image.open(r/f'ITKC_BT_1508A_V002_{n}.JPG');assert im.format=='JPEG'and im.size==(1640,2180)
node=read(r/'itkc-general-image-node.json');assert node['imginfo']['imgCur']=='240'and node['imginfo']['imgFile']=='ITKC_BT_1508A_V002_257'
for idx in range(241,250):
 n=read(r/f'itkc-general-image-index-{idx}.json');assert int(n['imginfo']['imgCur'])==idx and n['imginfo']['imgFile']==f'ITKC_BT_1508A_V002_{idx+17}'
native=read(r/'NATIVE_CROPS.json');assert len(native['records'])==6 and native['allFinalCropsViewed']and native['excludedNarrowTrialCrops']==4
for x in native['records']:
 s=r/Path(x['source']['file']).name;p=r/Path(x['crop']['file']).name;assert digest(s)==x['source']['sha256']and digest(p)==x['crop']['sha256'];assert x['viewed']and x['accepted'];a=Image.open(s).crop(x['boxXYXY']).convert('RGB');b=Image.open(p).convert('RGB');assert a.size==b.size and a.tobytes()==b.tobytes();t=b.copy();c=t.getpixel((0,0));t.putpixel((0,0),((c[0]+1)%256,c[1],c[2]));assert a.tobytes()!=t.tobytes()
for n in ids['excludedTrialCropsRemainOnlyInStaging']:assert not(r/n).exists()
for x in read(r/'SOURCE_IDENTITIES.json')['retainedFiles']+read(r/'FUNCTION_REUSE_AUDIT.json')['retainedModules']:
 p=w/x['file'];assert p.stat().st_size==x['bytes']and digest(p)==x['sha256']
res=subprocess.run(['node',str(r/'test-reference.mjs'),'--no-write'],cwd=w,capture_output=True,text=True,encoding='utf-8');assert res.returncode==0,res.stdout+res.stderr;summary=read(r/'REFERENCE_RESULTS.json')['summary'];assert json.loads(res.stdout)==summary
assert len(read(r/'CONTEXT_DISPOSITIONS.json')['sections'])==15 and all(not x['wholeClauseApplied']for x in read(r/'CONTEXT_DISPOSITIONS.json')['sections'])
manual=read(r/'MANUAL_PREMISES_REVISED.json');assert len(manual['records'])==4;anchors=next(x for x in manual['records']if x['id']=='anchor')['cases'];assert len(anchors)==8 and next(x for x in anchors if x['id']=='residential-named-hall')['sourceAnchor']=='茶亭，向中一間'
correction=read(r/'READING_CORRECTION.json');assert correction['detectedAfterInitialPassingTests']and not correction['initialTestsFailed']and not correction['actualCalendarRerun'];assert read(r/'initial-qualification-omission/REFERENCE_RESULTS.json')['summary']['preImplementationManualCases']==34
runtime=read(r/'ACTUAL_RUNTIME.json');assert runtime['actualLunarObjects']==runtime['actualJieQiTables']==2 and not runtime['sourceRelativeDayCountingResolved'];assert not runtime['consumerApplied']
lib=read(v/'research/library-current/COVERAGE.json');assert lib['counts']['catalogueRecords']==40 and lib['counts']['moduleSourceRecords']==16 and lib['counts']['wholeWorkApplied']==0;p08=next(x for x in lib['catalogue']if x['id']=='P08');assert p08['latestGeneralPremiseCounts']['selectedPremiseFunctions']==4 and not p08['wholeWorkApplied']
html=(v/'Huyen_Hoc_Cac.html').read_bytes();assert len(html)==707411 and sha256(html).hexdigest()=='549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857';assert html==(w/'Huyen_Hoc_Cac.html').read_bytes()==(v/'site/index.html').read_bytes();assert sorted(p.name for p in(v/'site').iterdir())==['index.html'];assert b'ITKC-GO1508A.'not in html
out={'date':'2026-10-29','promotionIdentities':len(ids['files']),'HTTP200BodiesWithTLS':23,'newRelatedSourceImagePositions':10,'newIndependentP08Editions':0,'newOriginalMasterContainers':0,'nativeCropsRGBMatched':6,'excludedTrialCrops':4,'RGBTamperPositiveControl':True,'firstPassGeneralSectionDispositions':15,'selectedPrivatePremiseFunctions':4,'symbolicAnchorConfigurations':8,**summary,'actualNewLunarObjects':2,'actualNewJieQiTables':2,'newHHCCharts':0,'newIztroCharts':0,'dailyAndHourDigitalHeadingsNotFacsimileCollated':22,'sourceRelativeDayCountingResolved':False,'sourceTimezoneAssigned':False,'wholeCatalogueCompleted':False}
if '--no-write'not in sys.argv:(q/'SOURCE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
else:assert read(q/'SOURCE_RESULTS.json')==out
print(json.dumps(out))
