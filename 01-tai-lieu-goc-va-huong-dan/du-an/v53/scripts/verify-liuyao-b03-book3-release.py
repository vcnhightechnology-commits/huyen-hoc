from pathlib import Path
from hashlib import sha256
import json,sys,zipfile
root=Path(__file__).resolve().parent.parent;w=root.parent
base=root/'research/liuyao-b03-book3';qa=root/'qa/liuyao-b03-book3';archive=w/'archives/v53-before-liuyao-b03-book3'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));sha=lambda b:sha256(b).hexdigest()
old=read(archive/'PACKAGE_MANIFEST.json');manifest=read(root/'PACKAGE_MANIFEST.json');html=(root/'Huyen_Hoc_Cac.html').read_bytes()
assert len(html)==707411 and sha(html)==old['product']['sha256']==manifest['product']['sha256']=='549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857'
assert html==(w/'Huyen_Hoc_Cac.html').read_bytes()==(root/'site/index.html').read_bytes()==(archive/'Huyen_Hoc_Cac.html').read_bytes()
assert sorted(p.name for p in(root/'site').iterdir())==['index.html']
mutable={'NEXT_STEPS.md','research/EXHAUSTIVE_WORK_STATE.json','research/full-study/WORK_STATE.json','research/library-current/COVERAGE.json','research/library-current/COVERAGE.md'}
unchanged=0
for f in old['files']:
 if f['file']not in mutable:
  assert sha((root/f['file']).read_bytes())==f['sha256'],f['file'];unchanged+=1
assert len(old['files'])==2381 and(archive/'Huyen_Hoc_Cac_V53_source.zip').stat().st_size==1299612174
web=w/'Huyen_Hoc_Cac_V53_web.zip';assert web.stat().st_size==344047 and web.read_bytes()==(archive/web.name).read_bytes()
with zipfile.ZipFile(web)as z:
 assert sorted(z.namelist())==['HUONG_DAN.md','index.html']and z.read('index.html')==html and z.read('HUONG_DAN.md')==(root/'README.md').read_bytes()
assert{p.relative_to(root).as_posix()for p in root.rglob('*')if p.is_file()and p.name!='PACKAGE_MANIFEST.json'}=={f['file']for f in manifest['files']}
for f in manifest['files']:
 b=(root/f['file']).read_bytes();assert len(b)==f['bytes']and sha(b)==f['sha256'],f['file']
with zipfile.ZipFile(w/'Huyen_Hoc_Cac_V53_source.zip')as z:
 assert set(z.namelist())=={'v53/'+f['file']for f in manifest['files']}|{'v53/PACKAGE_MANIFEST.json'}
 assert z.read('v53/PACKAGE_MANIFEST.json')==(root/'PACKAGE_MANIFEST.json').read_bytes()
 for f in manifest['files']:
  b=z.read('v53/'+f['file']);assert len(b)==f['bytes']and sha(b)==f['sha256'],f['file']
e=read(qa/'ENGINE_RESULTS.json');s=e['summary']
assert len(e['checks'])==10 and all(c['ok']for c in e['checks'])and e['htmlSHA256']==sha(html)
assert s=={'actualHHCHexCalls':64,'actualLunarCalls':180,'distinctLunarNoonDates':62,'referenceAnchorDays':60,
 'privateSelectedLineContexts':46080,'rawVoidContexts':7680,'exitHistogram':{str(i):768 for i in range(1,11)},
 'graphDigest':'84ba0913c10c6897ccdb93de0c40a88aeaeb0ad6621093ab4d98d9c9c2417bba',
 'newSourceRenders':43,'expandedEarlierPages':8,'QAOnlyRenders':2,'firstPassSectionSpans':12,'newOrCompletedSectionSpans':8,'boundedOperationalClauses':20}
manual=read(base/'MANUAL_READINGS.json');assert len(manual['records'])==51
assert manual['counts']=={'manualRecords':51,'newLocalRenders':43,'newContentPages':41,'coverPages':2,
 'expandedEarlierContentPages':8,'QAOnlyRenders':2,'physicalBookContentPagesNowFirstPassViewed':65,'physicalBookAllPagesViewedByRecordedScope':67}
for r in manual['records']+manual['qaImages']:assert sha((base/r['image']).read_bytes())==r['sha256']
assert sha((base/manual['sourcePDF']).read_bytes())==manual['sourceSHA256']=='01859340e519ffb68a1f40996af73aa7f40beb10a723a7a2a070985201874c61'
assert manual['newHTTPBodies']==manual['newOriginalPDFs']==0
assert set(manual['inheritedFirstPassPages'])|{r['pdfPage']for r in manual['records']}==set(range(1,68))
assert manual['unviewedPhysicalBookPages']==[]and not manual['entireBookApplied']
units=read(base/'BOOK3_CURRENT_UNITS.json');assert len(units['units'])==12 and units['counts']['newOrCompletedSpanUnits']==8
assert all(u['relevantSpanFirstPassRead']and not u['entireUnitApplied']for u in units['units'])and not units['allClausesApplied']
assert len(read(base/'OPERATIONAL_CLAUSES.json')['clauses'])==20
assert read(base/'XUN_EXIT_CLAUSE.json')['motionQualifierInThisBoundedSentence']is None
audit=read(base/'SOURCE_AUDIT.json');assert audit['all67PagesViewedWithRecordedScopes']and not audit['wholeBookApplied']and audit['unviewedPages']==[]
state=read(w/'EXHAUSTIVE_WORK_STATE.json');assert state==read(root/'research/EXHAUSTIVE_WORK_STATE.json')and state['status']=='active-not-complete'
assert state['currentWork']['latestResearchReport']=='v53/LIUYAO_B03_BOOK3_REPORT.md'and state['currentWork']['nextSourceLead']['status']=='downloaded-byte-verified-book3-first-pass-page-coverage-complete'
full=read(root/'research/full-study/WORK_STATE.json');assert full['overallStatus']=='active-not-complete'and full['latestResearchReport']=='LIUYAO_B03_BOOK3_REPORT.md'and full['latestConsumerReport']=='MEIHUA_LAYERS_REPORT.md'
coverage=read(root/'research/library-current/COVERAGE.json');assert coverage['counts']['wholeWorkApplied']==coverage['counts']['newDownloadsThisScope']==0
assert coverage['counts']['status']=={'inherited_rule_claim':4,'partial_active':5,'research_only':4,'not_established':27}
assert len(next(c for c in coverage['catalogue']if c['id']=='B03')['localPossession'])==3
work=read(base/'WORK_STATE.json');assert work['all67PagesViewedByRecordedScope']and not work['wholeBookApplied']and not work['wholeCatalogueCompleted']
assert read(w/'PENDING_RESEARCH_STATE.json')['status']=='book3-first-pass-pages-complete-current-scope-active'
toc=read(root/'research/liuyao-void-motion/B02_CURRENT_UNITS.json')['currentCounts'];assert(toc['registeredUnits'],toc['headingOnlyBodyUnits'],toc['firstPassCompleteSpanUnits'])==(136,103,26)
assert read(root/'qa/liuyao-b03-volume5/RELEASE_RESULTS.json')['manifestFilesVerified']==2381
for token in[b'xun-exit-reference.mjs',b'BOOK3_CURRENT_UNITS.json',b'XUN_EXIT_CLAUSE.json']:assert token not in html
out={'date':'2026-10-27','checks':10,**s,'newHTTPBodies':0,'newOriginalPDFs':0,'manualRecords':51,'newContentPages':41,
 'newCoverPages':2,'totalBook3ContentPagesViewedByScope':65,'all67Book3PagesViewedByScope':True,'wholeBookApplied':False,
 'wholeCatalogueCompleted':False,'functionalVoidModel':False,'fullTimingAdjudicator':False,'consumerChanged':False,
 'htmlBytes':len(html),'htmlSHA256':sha(html),'siteClean':True,'webZIPUnchanged':True,'priorTenReferencesPreserved':True,
 'previousSourceZIPPreservedBytes':1299612174,'unchangedEarlierV53Files':unchanged,
 'manifestFilesVerified':len(manifest['files']),'sourceZIPFilesVerified':len(manifest['files'])+1}
if '--no-write'in sys.argv:assert read(qa/'RELEASE_RESULTS.json')==out
else:(qa/'RELEASE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,ensure_ascii=False))
