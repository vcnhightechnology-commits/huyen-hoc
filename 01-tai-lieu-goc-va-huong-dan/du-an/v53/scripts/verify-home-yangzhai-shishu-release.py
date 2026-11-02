from pathlib import Path
from hashlib import sha256
import json,zipfile,sys,runpy,contextlib,io
r=Path(__file__).resolve().parent.parent;w=r.parent;b=r/'research/home-yangzhai-shishu';q=r/'qa/home-yangzhai-shishu';prepare='--prepare'in sys.argv
assert prepare or '--no-write'in sys.argv
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));sha=lambda data:sha256(data).hexdigest()
args=sys.argv[:]
try:
    sys.argv=['verify-home-yangzhai-shishu-sources.py','--no-write']
    with contextlib.redirect_stdout(io.StringIO()):runpy.run_path(str(r/'scripts/verify-home-yangzhai-shishu-sources.py'))
finally:sys.argv=args
source=read(q/'SOURCE_RESULTS.json');assert source['sourcePassingChecks']==6 and source['promotionIdentityHashesVerified']==116 and source['rawSourceCropsViewedAndPixelVerified']==4
archive=w/'archives/v53-before-home-yangzhai-shishu';snap=read(archive/'SNAPSHOT.json');assert snap['sourceManifestFiles']==3948 and snap['sourceZIPBytes']==2107772251
for x in snap['files']:
    p=archive/x['file'];assert p.stat().st_size==x['bytes']and sha(p.read_bytes())==x['sha256']
old=read(archive/'PACKAGE_MANIFEST.json');allowed={'NEXT_STEPS.md','research/EXHAUSTIVE_WORK_STATE.json','research/full-study/WORK_STATE.json','research/library-current/COVERAGE.json','research/library-current/COVERAGE.md'};unchanged=0
for x in old['files']:
    if x['file']in allowed:continue
    p=r/x['file'];assert p.stat().st_size==x['bytes']and sha(p.read_bytes())==x['sha256'],x['file'];unchanged+=1
state=read(w/'EXHAUSTIVE_WORK_STATE.json');assert state==read(r/'research/EXHAUSTIVE_WORK_STATE.json')and state['currentWork']['latestResearchReport']=='v53/HOME_YANGZHAI_SHISHU_REPORT.md'and state['currentWork']['catalogueID']=='P08'
coverage=read(r/'research/library-current/COVERAGE.json');assert coverage['counts']['catalogueRecords']==40 and coverage['counts']['wholeWorkApplied']==0 and coverage['counts']['status']['not_established']==26 and coverage['counts']['status']['research_only']==5
p08=next(x for x in coverage['catalogue']if x['id']=='P08');assert p08['currentStatus']=='research_only'and p08['currentSourceUnitCounts']['firstPassCompleteBodySpans']==2 and p08['currentSourceUnitCounts']['wholeUnitsApplied']==0
assert not read(r/'research/bazi-jianlu-context/CANDIDATE_STATUS.json')['browserTestsPassed']
html=(r/'Huyen_Hoc_Cac.html').read_bytes();assert len(html)==707411 and sha(html)=='549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857'and html==(w/'Huyen_Hoc_Cac.html').read_bytes()==(r/'site/index.html').read_bytes();assert sorted(p.name for p in(r/'site').iterdir())==['index.html']
for term in[b'home-yangzhai-shishu',b'sourceLayerCoordinate',b'YZSS-Tianyige-selected-chuangong']:assert term not in html
web=w/'Huyen_Hoc_Cac_V53_web.zip';assert web.read_bytes()==(archive/web.name).read_bytes()
with zipfile.ZipFile(web)as z:assert sorted(z.namelist())==['HUONG_DAN.md','index.html']and z.read('index.html')==html
payload=q/'RELEASE_RESULTS.json';files=[p for p in r.rglob('*')if p.is_file()and p.name!='PACKAGE_MANIFEST.json']
if prepare:count=len(files)+(0 if payload.exists()else 1)
else:
    m=read(r/'PACKAGE_MANIFEST.json');assert {p.relative_to(r).as_posix()for p in files}=={x['file']for x in m['files']};assert m['product']['sha256']==sha(html)
    for x in m['files']:
        data=(r/x['file']).read_bytes();assert len(data)==x['bytes']and sha(data)==x['sha256'],x['file']
    with zipfile.ZipFile(w/'Huyen_Hoc_Cac_V53_source.zip')as z:
        assert set(z.namelist())=={'v53/'+x['file']for x in m['files']}|{'v53/PACKAGE_MANIFEST.json'}and z.read('v53/PACKAGE_MANIFEST.json')==(r/'PACKAGE_MANIFEST.json').read_bytes()
        for x in m['files']:
            data=z.read('v53/'+x['file']);assert len(data)==x['bytes']and sha(data)==x['sha256'],x['file']
    count=len(m['files'])
out={'date':'2026-10-28','sourceVerification':source,'sourcePassingChecks':6,'privateCoordinateContexts':50,'privateBoundaryContexts':27,'originalRepositoryPDFBytes':151275796,'sourceContainerPDFPositions':195,'nativeSizedReencodedDerivativePositionsRead':40,'rawDCTStreamIdentitiesChecked':40,'rawSourceCropsViewedAndPixelVerified':4,'derivativeCropsViewedAndPixelVerified':4,'extractionCorrectionAuditRetained':True,'institutionItemCatalogIndependentlyValidated':False,'fullRawFortyImagesViewedNotClaimed':True,'fullFirstPassBodySpans':2,'manualContextGroups':46,'promotionIdentityHashesVerified':116,'moduleByteIdenticalToStaging':True,'newChartEngineExecutions':0,'fullSourceConditionsApplied':False,'modernFloorRoomGeometryAdapter':False,'sourceOutcomesValidated':False,'consumerChanged':False,'wholeCatalogueCompleted':False,'htmlBytes':len(html),'htmlSHA256':sha(html),'siteClean':True,'webZIPUnchanged':True,'previousSourceZIPPreservedBytes':2107772251,'unchangedEarlierV53Files':unchanged,'manifestFilesVerified':count,'sourceZIPFilesVerified':count+1}
if prepare:payload.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps({'preparedExpectedPayload':True,'manifestFilesAfterPackage':count,'requiresFinalNoWriteVerification':True}))
else:assert read(payload)==out;print(json.dumps({'finalReadOnlyVerificationPassed':True,**out},ensure_ascii=False))
