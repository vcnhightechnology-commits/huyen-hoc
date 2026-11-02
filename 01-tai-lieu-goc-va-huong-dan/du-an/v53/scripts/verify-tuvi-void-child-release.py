from pathlib import Path
from hashlib import sha256
import json, sys, zipfile

r = Path(__file__).resolve().parent.parent
w = r.parent
b = r/'research/tuvi-void-child'
q = r/'qa/tuvi-void-child'
a = w/'archives/v53-before-tuvi-void-child'
read = lambda p: json.loads(p.read_text(encoding='utf-8-sig'))
sha = lambda data: sha256(data).hexdigest()
assert '--prepare' in sys.argv or '--no-write' in sys.argv
prepare = '--prepare' in sys.argv
old = read(a/'PACKAGE_MANIFEST.json')
assert len(old['files']) == 3521 and (a/'Huyen_Hoc_Cac_V53_source.zip').stat().st_size == 2073696063
html = (r/'Huyen_Hoc_Cac.html').read_bytes()
assert len(html) == 707411 and sha(html) == old['product']['sha256'] == '549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857'
assert html == (w/'Huyen_Hoc_Cac.html').read_bytes() == (r/'site/index.html').read_bytes() == (a/'Huyen_Hoc_Cac.html').read_bytes()
assert [p.name for p in (r/'site').iterdir()] == ['index.html']
mutable = {'NEXT_STEPS.md','research/EXHAUSTIVE_WORK_STATE.json','research/full-study/WORK_STATE.json','research/library-current/COVERAGE.json','research/library-current/COVERAGE.md'}
unchanged = 0
for f in old['files']:
    if f['file'] not in mutable:
        data = (r/f['file']).read_bytes()
        assert len(data)==f['bytes'] and sha(data)==f['sha256'], f['file']
        unchanged += 1
web = w/'Huyen_Hoc_Cac_V53_web.zip'
assert web.stat().st_size==344047 and web.read_bytes()==(a/web.name).read_bytes()
with zipfile.ZipFile(web) as z:
    assert sorted(z.namelist())==['HUONG_DAN.md','index.html'] and z.read('index.html')==html

cr, vr, src = read(q/'CHILD_RESULTS.json'),read(q/'VOID_RESULTS.json'),read(q/'SOURCE_RESULTS.json')
assert len(cr['checks'])==5 and len(vr['checks'])==7 and all(x['ok'] for x in cr['checks']+vr['checks'])
assert cr['summary']['actualHHCTuviCalls']==cr['summary']['actualIztroNatalCalls']==cr['summary']['actualNatalContexts']==12
assert cr['summary']['sourcePrintedOrdinalCoordinates']==6 and cr['summary']['privateOrdinalPalaceBindings']==72
expected = {'sourceJieluStemGroups':5,'sourceXunzhongCycleGroups':6,'canonicalWorkingBranchCoordinates':22,'explicitSiNormalizationOccurrences':2,
    'privateSourceYearBranchQueries':1440,'unresolvedSiQueries':264,'unresolvedSiMemberships':242,
    'actualHHCTuviCalls':60,'actualIztroDefaultNatalCalls':60,'actualIztroZhongzhouNatalCalls':60,'actualNatalContexts':60,
    'expandedPriorReadSourcePositions':1,'nativeQACrops':1,'newHTTPRequests':0,'newOriginalContainers':0,'newSourcePositions':0}
assert vr['summary']==expected
assert src['nativeCropsPixelVerified']==2 and src['promotionIdentityHashesVerified']==15
assert src['uniqueRuntimeFilesByteIdenticalToTarball']==10 and src['additionalRuntimeFilesVerified']==6
assert src['retainedSourceImagesVerified']==1 and src['uniqueExpandedPriorSourcePositions']==1
assert src['newHTTPRequestsThisHeartbeat']==0 and src['inheritedFailedHTTPRequests']==1 and src['inheritedFailedHTTPBodyBytes']==608
for key in ['originalJP2Acquired','sourceYearBoundaryAdapterEstablished','sourceSingleSoftwareStarSelectorAttested','sourceAgeCountingConventionResolved','wholeChildPassageTranscribed','practicalOutcomesValidated','consumerChanged','wholeCatalogueCompleted']:
    assert src[key] is False, key
assert read(r/'qa/bazi-yangren-conditions/RELEASE_RESULTS.json')['manifestFilesVerified']==3521
work = read(b/'WORK_STATE.json')
assert not work['wholeCatalogueCompleted'] and not work['consumerChanged'] and not work['firstMajorPeriodStartResolved']
state = read(w/'EXHAUSTIVE_WORK_STATE.json')
assert state==read(r/'research/EXHAUSTIVE_WORK_STATE.json') and state['status']=='active-not-complete'
assert state['currentWork']['latestResearchReport']=='v53/TUVI_VOID_CHILD_REPORT.md' and state['currentWork']['catalogueID']=='T01'
coverage = read(r/'research/library-current/COVERAGE.json')
assert coverage['counts']['catalogueRecords']==40 and coverage['counts']['wholeWorkApplied']==0 and coverage['counts']['newDownloadsThisScope']==0
full = read(r/'research/full-study/WORK_STATE.json')
assert full['latestResearchReport']=='TUVI_VOID_CHILD_REPORT.md' and full['latestConsumerReport']=='MEIHUA_LAYERS_REPORT.md'
assert read(w/'PENDING_RESEARCH_STATE.json')['status']=='Tuvi-void-child-current-scope-active'
candidate = read(r/'research/bazi-jianlu-context/CANDIDATE_STATUS.json')
assert not candidate['browserTestsPassed'] and not candidate['consumerChanged']
for term in [b'tuvi-void-child',b'void-reference',b'ordinal-reference',b'NAJ4468520-canvas80-jielu-pair']:
    assert term not in html

result = q/'RELEASE_RESULTS.json'
files = [p for p in r.rglob('*') if p.is_file() and p.name!='PACKAGE_MANIFEST.json']
if prepare:
    count = len(files)+(0 if result.exists() else 1)
else:
    manifest = read(r/'PACKAGE_MANIFEST.json')
    assert {p.relative_to(r).as_posix() for p in files}=={f['file'] for f in manifest['files']}
    assert manifest['product']['sha256']==sha(html)
    for f in manifest['files']:
        data = (r/f['file']).read_bytes()
        assert len(data)==f['bytes'] and sha(data)==f['sha256'], f['file']
    with zipfile.ZipFile(w/'Huyen_Hoc_Cac_V53_source.zip') as z:
        assert set(z.namelist())=={'v53/'+f['file'] for f in manifest['files']}|{'v53/PACKAGE_MANIFEST.json'}
        assert z.read('v53/PACKAGE_MANIFEST.json')==(r/'PACKAGE_MANIFEST.json').read_bytes()
        for f in manifest['files']:
            data=z.read('v53/'+f['file'])
            assert len(data)==f['bytes'] and sha(data)==f['sha256'], f['file']
    count = len(manifest['files'])
out = {'date':'2026-10-28','newVoidChecks':7,'inheritedChildChecks':5,'voidSummary':expected,'inheritedChildSummary':cr['summary'],
    'sourceImagesVerified':1,'nativeCropsPixelVerified':2,'promotionIdentityHashesVerified':15,'uniqueRuntimeFilesByteIdenticalToTarball':10,
    'newHTTPRequestsThisHeartbeat':0,'inheritedFailedHTTPBodies':1,'uniqueExpandedPriorSourcePositions':1,
    'newOriginalContainers':0,'newSourcePositions':0,'wholeCatalogueCompleted':False,'consumerChanged':False,
    'sourceYearBoundaryAdapterEstablished':False,'sourceSingleStarSelectorAttested':False,'sourceAgeCountingConventionResolved':False,
    'wholeChildPassageTranscribed':False,'practicalOutcomesValidated':False,
    'htmlBytes':len(html),'htmlSHA256':sha(html),'siteClean':True,'webZIPUnchanged':True,'previousSourceZIPPreservedBytes':2073696063,
    'unchangedEarlierV53Files':unchanged,'manifestFilesVerified':count,'sourceZIPFilesVerified':count+1}
if prepare:
    result.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'preparedExpectedPayload':True,'manifestFilesAfterPackage':count,'requiresFinalNoWriteVerification':True}))
else:
    assert read(result)==out
    print(json.dumps({'finalReadOnlyVerificationPassed':True,**out},ensure_ascii=False))
