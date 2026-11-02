from pathlib import Path
from hashlib import sha256
from PIL import Image
import json,subprocess,sys
v=Path(__file__).resolve().parent.parent;w=v.parent;r=v/'research/home-time-premises';q=v/'qa/home-time-premises';read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
def digest(p):
 h=sha256()
 with p.open('rb')as stream:
  for block in iter(lambda:stream.read(4*1024*1024),b''):h.update(block)
 return h.hexdigest()
ids=read(r/'PROMOTION_IDENTITIES.json')
for x in ids['files']:
 p=w/x['file'];assert p.stat().st_size==x['bytes']and digest(p)==x['sha256'],x['file']
requests=read(r/'REQUESTS.json');assert len(requests)==18
for x in requests:
 p=r/x['file'];assert x['status']==200 and x['standardTLSValidation'];assert p.stat().st_size==x['bytes']and digest(p)==x['sha256']
for n in range(240,248):assert Image.open(r/f'ITKC_BT_1508A_V002_{n}.JPG').format=='JPEG'and Image.open(r/f'ITKC_BT_1508A_V002_{n}.JPG').size==(1640,2180)
node=read(r/'itkc-month-theory-image-node.json');assert node['imginfo']['imgCur']=='223'and node['imginfo']['imgFile']=='ITKC_BT_1508A_V002_240'
for index in range(224,231):
 x=read(r/f'itkc-month-image-index-{index}.json');assert int(x['imginfo']['imgCur'])==index and x['imginfo']['imgFile']==f'ITKC_BT_1508A_V002_{index+17}'
native=read(r/'NATIVE_CROPS.json');assert len(native['records'])==8 and native['allFinalCropsViewed'];assert native['excludedNarrowTrialCrops']==1 and not(r/'youlong.png').exists()
for x in native['records']:
 src=r/Path(x['source']['file']).name;dst=r/Path(x['crop']['file']).name;assert digest(src)==x['source']['sha256']and digest(dst)==x['crop']['sha256'];im=Image.open(src);assert list(im.size)==x['sourceDimensions'];a=im.crop(x['boxXYXY']).convert('RGB');b=Image.open(dst).convert('RGB');assert a.size==b.size and a.tobytes()==b.tobytes();assert x['viewed']and x['accepted'];tamper=b.copy();rgb=tamper.getpixel((0,0));tamper.putpixel((0,0),((rgb[0]+1)%256,rgb[1],rgb[2]));assert a.tobytes()!=tamper.tobytes()
for x in read(r/'SOURCE_IDENTITIES.json')['retainedFiles']+read(r/'FUNCTION_REUSE_AUDIT.json')['retainedModules']:
 p=w/x['file'];assert p.stat().st_size==x['bytes']and digest(p)==x['sha256']
res=subprocess.run(['node',str(r/'test-reference.mjs'),'--no-write'],cwd=w,capture_output=True,text=True,encoding='utf-8');assert res.returncode==0,res.stdout+res.stderr;assert json.loads(res.stdout)==read(r/'REFERENCE_RESULTS.json')['summary']
contexts=read(r/'CONTEXT_DISPOSITIONS.json');assert len(contexts['sections'])==19 and contexts['allImageCharactersCollated']is False;assert all(not x['wholeClauseApplied']for x in contexts['sections']);assert 'excluded from product' in contexts['sections'][6]['disposition']
manual=read(r/'MANUAL_CLAUSES.json');assert len(manual['records'])==4 and manual['sourceUsesNoJieqiForAllRules']is False and manual['sourceMonthAutomaticallyEqualsNumericLunarMonth']is False
cache=read(r/'CACHED_CALENDAR_COUNTEREXAMPLES.json');assert len(cache['records'])==4 and cache['newCalendarObjects']==0 and cache['newZhiXingCalls']==0;assert digest(w/cache['source']['file'])==cache['source']['sha256']
lib=read(v/'research/library-current/COVERAGE.json');assert lib['counts']['catalogueRecords']==40 and lib['counts']['moduleSourceRecords']==16 and lib['counts']['wholeWorkApplied']==0;p08=next(x for x in lib['catalogue']if x['id']=='P08');assert p08['latestMonthlyRepairScopeCounts']=={'newSourceImages':8,'sectionDispositions':19,'selectedClausePredicates':4,'printedSiteExamples':4,'wholeMonthlyMethodApplied':False,'newCalendarEngineCalls':0}
html=(v/'Huyen_Hoc_Cac.html').read_bytes();assert len(html)==707411 and sha256(html).hexdigest()=='549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857';assert html==(w/'Huyen_Hoc_Cac.html').read_bytes()==(v/'site/index.html').read_bytes();assert sorted(p.name for p in(v/'site').iterdir())==['index.html'];assert b'ITKC-GO1508A.'not in html
out={'date':'2026-10-29','promotionIdentities':len(ids['files']),'HTTP200BodiesWithTLS':18,'newRelatedSourceImagePositions':8,'newIndependentP08Editions':0,'newOriginalMasterContainers':0,'nativeCropsRGBMatched':8,'excludedNarrowTrialCrops':1,'RGBTamperPositiveControl':True,'firstPassSectionDispositions':19,'selectedClausePredicates':4,'printedSiteExamples':4,'completeChecks':7,'acceptedReferenceFrames':672,'unsupportedMonthFramesUnknown':504,'cachedActualCalendarIllustrationsReused':4,'newHHCCharts':0,'newLunarObjects':0,'newZhiXingCalls':0,'newIztroCharts':0,'calendarBoundaryTimestampResolved':False,'leapMonthPolicyResolved':False,'globalNoJieqiRuleEstablished':False,'consumerChanged':False,'wholeCatalogueCompleted':False}
if '--no-write'not in sys.argv:(q/'SOURCE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
else:assert read(q/'SOURCE_RESULTS.json')==out
print(json.dumps(out))
