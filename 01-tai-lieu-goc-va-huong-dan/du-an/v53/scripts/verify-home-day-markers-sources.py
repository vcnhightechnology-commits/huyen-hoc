from pathlib import Path
from hashlib import sha256
from PIL import Image,ImageChops
import json,subprocess,sys
v=Path(__file__).resolve().parent.parent;w=v.parent;b=v/'research/home-day-markers';q=v/'qa/home-day-markers';read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
def digest(p):
 h=sha256()
 with p.open('rb')as stream:
  for x in iter(lambda:stream.read(4*1024*1024),b''):h.update(x)
 return h.hexdigest()
ident=read(b/'PROMOTION_IDENTITIES.json')
for r in ident['records']:
 p=v/r['file'];assert p.stat().st_size==r['bytes']and digest(p)==r['sha256'],r['file']
assert{r['file']for r in ident['records']}=={p.relative_to(v).as_posix()for p in b.iterdir()if p.is_file()and p.name!='PROMOTION_IDENTITIES.json'}|{'qa/home-day-markers/RESULTS.json','HOME_DAY_MARKERS_REPORT.md','scripts/verify-home-day-markers-sources.py'}
s=read(b/'SOURCE_IDENTITIES.json');parent=read(w/s['parentAcquisition']);assert parent['sha256']==s['sourcePDFSHA256']==digest(w/s['sourcePDFFile']);assert not parent['independentTextualWitnessCompared'];assert len(s['records'])==4
for r in s['records']:
 p=w/r['file'];assert p.stat().st_size==r['bytes']and digest(p)==r['sha256'];assert Image.open(p).size==(r['width'],r['height'])and r['actuallyViewed']
crops=[]
for file in ['NATIVE_CROPS.json','SUPPLEMENTARY_CROPS.json','GLYPH_CROPS.json']:crops+=read(b/file)['records']
assert len(crops)==18 and sum(r['acceptedForLiteralProof']for r in crops)==15
for r in crops:
 assert r['actuallyViewed']and not r['resampled'];assert digest(w/r['sourceFile'])==r['sourceSHA256']and digest(b/r['file'])==r['sha256'];assert (b/r['file']).stat().st_size==r['bytes'];assert ImageChops.difference(Image.open(w/r['sourceFile']).crop(r['cropBox']).convert('RGB'),Image.open(b/r['file']).convert('RGB')).getbbox()is None
im=Image.open(b/crops[0]['file']).convert('RGB');changed=im.copy();p=changed.getpixel((0,0));changed.putpixel((0,0),((p[0]+1)%256,p[1],p[2]));assert ImageChops.difference(im,changed).getbbox()is not None
manual=read(b/'MANUAL_BUILD_BREAK_MARKERS.json');assert len(manual['blocks'])==6 and manual['markerOccurrences']=={'建':60,'破':60};assert not manual['wholeTableLabelsTranscribed']and not manual['calendarAdapterImplemented'];assert sum(r['selectedMarker']is None for r in manual['records'])==600
for block in manual['blocks']:
 assert len(block['days'])==20 and len(block['rows'])==12
 for i,txt in enumerate(block['rows'],1):
  assert len(txt)==10
  for c,letter in enumerate(txt):
   day=block['days'][2*c:2*c+2];row=next(x for x in manual['records']if x['sourceMonth']==i and x['dayGanzhi']==day);assert row['evidenceCrop']==block['file']and row['selectedMarker']=={'J':'建','P':'破','.':None}[letter]
reuse=read(b/'FUNCTION_REUSE_AUDIT.json');assert digest(w/reuse['file'])==reuse['sha256']and reuse['newActualHourCalls']==0;assert read(b/'SEARCH_LEADS.json')['newWitnessesAccepted']==0
proc=subprocess.run(['node',str(b/'test-reference.mjs'),'--no-write'],cwd=w,capture_output=True,text=True,encoding='utf-8');assert proc.returncode==0,proc.stdout+proc.stderr;tests=json.loads(proc.stdout);assert tests==read(q/'RESULTS.json')
assert (w/'EXHAUSTIVE_WORK_STATE.json').read_bytes()==(v/'research/EXHAUSTIVE_WORK_STATE.json').read_bytes();coverage=read(v/'research/library-current/COVERAGE.json');p08=next(x for x in coverage['catalogue']if x['id']=='P08');assert p08['currentSourceUnitCounts']['selectedDayMarkerContexts']==720 and not p08['currentSourceUnitCounts']['dayCellLabelsFullyTranscribed']and coverage['counts']['wholeWorkApplied']==0
html=v/'Huyen_Hoc_Cac.html';assert html.stat().st_size==707411 and digest(html)=='549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857';assert html.read_bytes()==(w/'Huyen_Hoc_Cac.html').read_bytes()==(v/'site/index.html').read_bytes();assert sorted(p.name for p in(v/'site').iterdir())==['index.html']
out=dict(date='2026-10-29',promotionIdentities=len(ident['records']),expandedPreviouslyReadSourcePositions=4,newHTTPRequests=0,newSourcePositions=0,newOriginalContainers=0,newIndependentEditions=0,nativeCropsRGBMatched=18,acceptedLiteralCrops=15,excludedTruncatedCrops=2,excludedUncertainGlyphCrops=1,RGBTamperPositiveControl=True,selectedMarkerCoordinates=720,buildOccurrences=60,breakOccurrences=60,cellsWithNeitherSelectedMarker=600,wholeTableLabelsTranscribed=False,completeRuntimeChecks=tests['completeChecks'],actualLunarObjects=2560,actualZhiXingCalls=720,selectedRuntimeFrames=720,selectedMarkerMismatches=0,boundaryIllustrations=24,invalidMonthBasisRejections=2880,runtimeBatches=1,testsRerunCalendarObjects=0,actualHHCCharts=0,actualIztroCharts=0,sourceMonthBoundaryResolved=False,calendarAdapterImplemented=False,consumerChanged=False,wholeCatalogueCompleted=False)
if '--no-write'in sys.argv:assert read(q/'SOURCE_RESULTS.json')==out
else:(q/'SOURCE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
