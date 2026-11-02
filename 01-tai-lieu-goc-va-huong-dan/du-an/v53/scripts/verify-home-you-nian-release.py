from pathlib import Path
from hashlib import sha256
import json,sys,zipfile
r=Path(__file__).resolve().parent.parent;w=r.parent;b=r/'research/home-you-nian';q=r/'qa/home-you-nian';a=w/'archives/v53-before-home-you-nian'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));sha=lambda data:sha256(data).hexdigest()
old=read(a/'PACKAGE_MANIFEST.json');m=read(r/'PACKAGE_MANIFEST.json');html=(r/'Huyen_Hoc_Cac.html').read_bytes()
assert len(old['files'])==2915 and(a/'Huyen_Hoc_Cac_V53_source.zip').stat().st_size==2018013895
assert len(html)==707411 and sha(html)==m['product']['sha256']==old['product']['sha256']=='549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857'
assert html==(w/'Huyen_Hoc_Cac.html').read_bytes()==(r/'site/index.html').read_bytes()==(a/'Huyen_Hoc_Cac.html').read_bytes()
assert [p.name for p in(r/'site').iterdir()]==['index.html']
mutable={'NEXT_STEPS.md','research/EXHAUSTIVE_WORK_STATE.json','research/full-study/WORK_STATE.json','research/library-current/COVERAGE.json','research/library-current/COVERAGE.md'}
unchanged=0
for f in old['files']:
 if f['file']not in mutable:assert sha((r/f['file']).read_bytes())==f['sha256'],f['file'];unchanged+=1
web=w/'Huyen_Hoc_Cac_V53_web.zip';assert web.stat().st_size==344047 and web.read_bytes()==(a/web.name).read_bytes()
with zipfile.ZipFile(web)as z:assert sorted(z.namelist())==['HUONG_DAN.md','index.html']and z.read('index.html')==html
assert {p.relative_to(r).as_posix()for p in r.rglob('*')if p.is_file()and p.name!='PACKAGE_MANIFEST.json'}=={f['file']for f in m['files']}
for f in m['files']:
 data=(r/f['file']).read_bytes();assert len(data)==f['bytes']and sha(data)==f['sha256'],f['file']
with zipfile.ZipFile(w/'Huyen_Hoc_Cac_V53_source.zip')as z:
 assert set(z.namelist())=={'v53/'+f['file']for f in m['files']}|{'v53/PACKAGE_MANIFEST.json'}
 assert z.read('v53/PACKAGE_MANIFEST.json')==(r/'PACKAGE_MANIFEST.json').read_bytes()
 for f in m['files']:
  data=z.read('v53/'+f['file']);assert len(data)==f['bytes']and sha(data)==f['sha256'],f['file']
qa=read(q/'RESULTS.json');nt=read(q/'NAMED_TABLE_RESULTS.json');sr=read(q/'SOURCE_RESULTS.json')
assert len(qa['checks'])==9 and len(nt['checks'])==4 and all(x['ok']for x in qa['checks']+nt['checks'])
assert qa['summary']=={'actualHHCDirectionsCalls':8,'conditionalHHCLabels':64,'privateRelations':128,'directSmallStarCells':64,'directNonselfPairs':56,'sourcePolicyContexts':128,'differingLabels':40,'literalMatchingLabels':16,'selfRoleOnly':8}
assert nt['summary']=={'namedMountainAssignments':48,'monthlySourceRows':12,'calendarAdapters':0,'actualHHCEngineCalls':0}
assert sr['nativePNGAndPixelHashesVerified']==103 and sr['combinedFirstPassImagePositions']==110 and sr['sourceUnitsLocated']==12
assert not sr['P03FacsimileResolved']and not sr['allSourceClausesApplied']
st=read(w/'EXHAUSTIVE_WORK_STATE.json');assert st==read(r/'research/EXHAUSTIVE_WORK_STATE.json')and st['status']=='active-not-complete'
assert st['currentWork']['catalogueID']=='P03'and st['currentWork']['latestResearchReport']=='v53/HOME_YOU_NIAN_REPORT.md'
cov=read(r/'research/library-current/COVERAGE.json');assert cov['counts']['catalogueRecords']==40 and cov['counts']['wholeWorkApplied']==0 and cov['counts']['newDownloadsThisScope']==0
full=read(r/'research/full-study/WORK_STATE.json');assert full['latestResearchReport']=='HOME_YOU_NIAN_REPORT.md'and full['latestConsumerReport']=='MEIHUA_LAYERS_REPORT.md'
assert read(w/'PENDING_RESEARCH_STATE.json')['status']=='Home-you-nian-atomic-extraction-active'
assert read(r/'qa/bazi-jianlu-coordinates/RELEASE_RESULTS.json')['manifestFilesVerified']==2915
for term in[b'home-you-nian',b'you-nian-reference',b'named-table-reference']:assert term not in html
out={'date':'2026-10-27','checks':13,**qa['summary'],**nt['summary'], # namedtables havezeroenginecalls separatelybelow
 'actualHHCDirectionsCalls':8,'actualHHCEngineCallsInNamedTables':0,'nativePNGAndPixelHashesVerified':103,'priorImageReadings':7,'combinedFirstPassImagePositions':110,
 'nativeContentPages':95,'blankPages':5,'paratextPages':3,'sourceUnitsLocated':12,'sourcePixelCalibration':True,'P03FacsimileResolved':False,
 'retainedFailedHTTPBodies':3,'newOriginalContainers':0,'wholeCatalogueCompleted':False,'allAtomicClausesApplied':False,'consumerChanged':False,
 'htmlBytes':len(html),'htmlSHA256':sha(html),'siteClean':True,'webZIPUnchanged':True,'previousSourceZIPPreservedBytes':2018013895,
 'unchangedEarlierV53Files':unchanged,'manifestFilesVerified':len(m['files']),'sourceZIPFilesVerified':len(m['files'])+1}
out.pop('actualHHCEngineCalls',None)
if '--no-write'in sys.argv:assert read(q/'RELEASE_RESULTS.json')==out
else:(q/'RELEASE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,ensure_ascii=False))
