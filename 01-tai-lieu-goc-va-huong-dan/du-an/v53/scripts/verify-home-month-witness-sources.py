from pathlib import Path
from hashlib import sha256
from PIL import Image
import json,subprocess,sys
v=Path(__file__).resolve().parent.parent;w=v.parent;r=v/'research/home-month-witness';q=v/'qa/home-month-witness';read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
def digest(p):
 h=sha256()
 with p.open('rb')as stream:
  for block in iter(lambda:stream.read(4*1024*1024),b''):h.update(block)
 return h.hexdigest()
ids=read(r/'PROMOTION_IDENTITIES.json');assert len(ids['files'])==42
for x in ids['files']:
 p=w/x['file'];assert p.stat().st_size==x['bytes']and digest(p)==x['sha256'],x['file']
assert ids['attemptedActualBatches']==2 and ids['failedBatchCount']==1 and ids['successfulBatchCount']==1 and ids['totalHHCCompassCallsIncludingFailure']==4
for x in read(r/'SOURCE_IDENTITIES.json')['retainedFiles']:
 p=w/x['file'];assert p.stat().st_size==x['bytes']and digest(p)==x['sha256'],x['file']
requests=read(r/'REQUESTS.json');assert len(requests)==13
for x in requests:
 p=r/x['file'];assert x['status']==200 and x['standardTLSValidation'];assert p.stat().st_size==x['bytes']and digest(p)==x['sha256']
for name in ['itkc-V002-034.JPG','itkc-V002-035.JPG']:assert Image.open(r/name).format=='JPEG'and Image.open(r/name).size==(1640,2180)
c=read(r/'NATIVE_CROPS.json');assert len(c['records'])==8 and c['allFinalEightViewed']and c['excludedNarrowTrialCropCount']==1;assert not(r/'crop-tian-dao.png').exists()
for x in c['records']:
 src=r/x['sourceFile'];dst=r/x['cropFile'];assert digest(src)==x['sourceSHA256']and digest(dst)==x['cropSHA256'];im=Image.open(src);assert list(im.size)==x['sourceDimensions'];a=im.crop(x['boxXYXY']).convert('RGB');b=Image.open(dst).convert('RGB');assert a.size==b.size and a.tobytes()==b.tobytes();assert x['viewed']and x['accepted'];tamper=b.copy();rgb=tamper.getpixel((0,0));tamper.putpixel((0,0),((rgb[0]+1)%256,rgb[1],rgb[2]));assert a.tobytes()!=tamper.tobytes()
res=subprocess.run(['node',str(r/'test-witness.mjs'),'--no-write'],cwd=w,capture_output=True,text=True,encoding='utf-8');assert res.returncode==0,res.stdout+res.stderr;assert json.loads(res.stdout)==read(r/'TEST_RESULTS.json')['summary']
original=read(v/'research/home-month-gods/MANUAL_MONTH_GOD_TABLES.json');wealth=next(x for x in original['records']if x['id']=='month-wealth');assert wealth['cells'][1]['literal']is None and wealth['cells'][7]['literal']is None
lib=read(v/'research/library-current/COVERAGE.json');p08=next(x for x in lib['catalogue']if x['id']=='P08');assert p08['monthlyRelatedWitnessCounts']=={'relatedITKCManualCells':84,'sameLiteral':77,'differentLiteral':5,'P08UnresolvedRetained':2,'newIndependentP08Editions':0,'wholeRelatedWorkApplied':False};assert lib['counts']['catalogueRecords']==40 and lib['counts']['moduleSourceRecords']==16 and lib['counts']['wholeWorkApplied']==0
acq=read(r/'ACQUISITION_AND_LIMITS.json');assert acq['institutionYearField']is None and not acq['originalUnderlyingEditionIdentified']and not acq['originalCopyMatchedSNU1724'];assert not acq['SNULocalResponseBytesObtained'];assert read(r/'WASEDA_TRANSPORT_FAILURE.json')['publisherPDFBytesObtained']is False and read(r/'SNU_TRANSPORT_FAILURE.json')['originalResponseBytesRetained']is False
html=(v/'Huyen_Hoc_Cac.html').read_bytes();assert len(html)==707411 and sha256(html).hexdigest()=='549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857';assert html==(w/'Huyen_Hoc_Cac.html').read_bytes()==(v/'site/index.html').read_bytes();assert sorted(p.name for p in(v/'site').iterdir())==['index.html'];assert b'ITKC-GO1508A'not in html
out={'date':'2026-10-29','promotionIdentities':42,'retainedLocalHTTP200Bodies':13,'failedLocalAcquisitions':2,'newRelatedFacsimilePositions':2,'newP08SourcePositions':0,'newOriginalContainers':0,'newIndependentP08Editions':0,'nativeCropsRGBMatched':8,'excludedNarrowTrialCrops':1,'RGBTamperPositiveControl':True,'manuallyReadRelatedCells':84,'P08SameLiteralCells':77,'P08DifferentLiteralCells':5,'P08OriginalUnresolvedCells':2,'differentCentreStemCoordinates':5,'institutionDigitalImageDiscrepancies':1,'duplicateWikisourceDiscrepancyNotIndependent':True,'completeChecks':7,'unknownBasisFrames':336,'missingMonthFrames':7,'actualSuccessfulBatchCompassCalls':2,'actualFailedBatchCompassCalls':2,'totalActualCompassCallsIncludingFailure':4,'successfulRuntimeBatches':1,'failedRuntimeBatches':1,'newCompassCallsFromReplay':0,'actualNatalCharts':0,'actualIztroCharts':0,'realSourceCellExactBearingsAssigned':0,'sourceMonthBoundaryResolved':False,'consumerChanged':False,'wholeCatalogueCompleted':False}
if '--no-write'not in sys.argv:(q/'SOURCE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
else:assert read(q/'SOURCE_RESULTS.json')==out
print(json.dumps(out))
