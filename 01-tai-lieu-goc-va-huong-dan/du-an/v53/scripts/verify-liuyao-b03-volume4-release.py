from pathlib import Path
from hashlib import sha256
import json, sys, zipfile
root=Path(__file__).resolve().parent.parent; w=root.parent
base=root/'research/liuyao-b03-volume4'; qa=root/'qa/liuyao-b03-volume4'
archive=w/'archives/v53-before-liuyao-b03-volume4'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
sha=lambda b:sha256(b).hexdigest()
old=read(archive/'PACKAGE_MANIFEST.json'); manifest=read(root/'PACKAGE_MANIFEST.json')
html=(root/'Huyen_Hoc_Cac.html').read_bytes()
assert len(html)==707411 and sha(html)==old['product']['sha256']==manifest['product']['sha256']=='549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857'
assert html==(w/'Huyen_Hoc_Cac.html').read_bytes()==(root/'site/index.html').read_bytes()==(archive/'Huyen_Hoc_Cac.html').read_bytes()
assert sorted(p.name for p in (root/'site').iterdir())==['index.html']
mutable={'NEXT_STEPS.md','research/EXHAUSTIVE_WORK_STATE.json','research/full-study/WORK_STATE.json','research/library-current/COVERAGE.json','research/library-current/COVERAGE.md'}
unchanged=0
for f in old['files']:
    if f['file'] not in mutable:
        assert sha((root/f['file']).read_bytes())==f['sha256'], f['file']
        unchanged+=1
assert (archive/'Huyen_Hoc_Cac_V53_source.zip').stat().st_size==1150284497
web=w/'Huyen_Hoc_Cac_V53_web.zip'
assert web.stat().st_size==344047 and web.read_bytes()==(archive/web.name).read_bytes()
with zipfile.ZipFile(web) as z:
    assert sorted(z.namelist())==['HUONG_DAN.md','index.html']
    assert z.read('index.html')==html and z.read('HUONG_DAN.md')==(root/'README.md').read_bytes()
assert {p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file() and p.name!='PACKAGE_MANIFEST.json'}=={f['file'] for f in manifest['files']}
for f in manifest['files']:
    b=(root/f['file']).read_bytes()
    assert len(b)==f['bytes'] and sha(b)==f['sha256'],f['file']
with zipfile.ZipFile(w/'Huyen_Hoc_Cac_V53_source.zip') as z:
    assert set(z.namelist())=={'v53/'+f['file'] for f in manifest['files']}|{'v53/PACKAGE_MANIFEST.json'}
    assert z.read('v53/PACKAGE_MANIFEST.json')==(root/'PACKAGE_MANIFEST.json').read_bytes()
    for f in manifest['files']:
        b=z.read('v53/'+f['file'])
        assert len(b)==f['bytes'] and sha(b)==f['sha256'],f['file']
e=read(qa/'ENGINE_RESULTS.json'); s=e['summary']
assert len(e['checks'])==9 and all(c['ok'] for c in e['checks'])
assert s['actualHHCHexCalls']==64 and s['privateFigureMotionContexts']==4096 and s['groupsPerContext']==6
assert (s['completeGroups'],s['qualifyingGroups'],s['witnesses'])==(2048,1120,2816)
assert s['graphDigest']=='4e7a98afc24472077d21fa5f46770705293f61245b6f12b4b77f851dcccb3191'
assert s['perGroup']['tiger-snake-monkey']['complete']==s['perGroup']['ox-dog-goat']['complete']==0
manual=read(base/'MANUAL_READINGS.json')
assert manual['counts']=={'manualRecords':20,'newLocalRenders':17,'newContentPages':16,'newCoverPages':1,'expandedEarlierBoundedPages':3,'volume4ContentSpanPages':19}
assert [r['pdfPage'] for r in manual['records']]==list(range(30,50))
for r in manual['records']:assert sha((base/r['image']).read_bytes())==r['sha256']
assert sha((base/manual['sourcePDF']).read_bytes())==manual['sourceSHA256']=='c1e1027331d43769733c6011b4fe99e90928e9fde013fce563c8e9bad81c04bf'
assert manual['opening']['pdfPage']==30 and manual['ending']['pdfPage']==48
assert manual['ending']['literalReading']=='卜筮正宗卷之四終'
assert manual['newOriginalPDFs']==manual['newHTTPBodies']==0
assert not manual['wholePhysicalBookApplied'] and manual['physicalBook2PageCoverage']['unreadPages']==[]
assert len(read(base/'OPERATIONAL_CLAUSES.json')['clauses'])==30
assert read(base/'SOURCE_AUDIT.json')['unreadPhysicalBook2Pages']==[]
state=read(w/'EXHAUSTIVE_WORK_STATE.json')
assert state==read(root/'research/EXHAUSTIVE_WORK_STATE.json') and state['status']=='active-not-complete'
assert state['currentWork']['latestResearchReport']=='v53/LIUYAO_B03_VOLUME4_REPORT.md'
assert state['currentWork']['nextSourceLead']['status']=='downloaded-byte-verified-first-pass-page-coverage-complete'
full=read(root/'research/full-study/WORK_STATE.json')
assert full['overallStatus']=='active-not-complete' and full['latestConsumerReport']=='MEIHUA_LAYERS_REPORT.md'
assert full['latestResearchReport']=='LIUYAO_B03_VOLUME4_REPORT.md'
coverage=read(root/'research/library-current/COVERAGE.json')
assert coverage['counts']['wholeWorkApplied']==coverage['counts']['newDownloadsThisScope']==0
assert coverage['counts']['status']=={'inherited_rule_claim':4,'partial_active':5,'research_only':4,'not_established':27}
assert len(next(c for c in coverage['catalogue'] if c['id']=='B03')['localPossession'])==2
work=read(base/'WORK_STATE.json')
assert work['physicalBook2AllPagesViewedWithRecordedScope'] and not work['wholeBookApplied'] and not work['wholeCatalogueCompleted']
toc=read(root/'research/liuyao-void-motion/B02_CURRENT_UNITS.json')['currentCounts']
assert (toc['registeredUnits'],toc['headingOnlyBodyUnits'],toc['firstPassCompleteSpanUnits'])==(136,103,26)
assert read(root/'qa/liuyao-b03-volume3/RELEASE_RESULTS.json')['manifestFilesVerified']==2302
for token in [b'triad-reference.mjs',b'TRIAD_TABLES.json',b'OPERATIONAL_CLAUSES.json']:assert token not in html
out={'date':'2026-10-27','checks':9,**s,'manualRecords':20,'newLocalRenders':17,'expandedEarlierReadings':3,
 'volume4ContentPages':19,'newContentPages':16,'coverPages':1,'newHTTPBodies':0,'newOriginalPDFs':0,
 'physicalBook2AllPagesViewedByRecordedScope':True,'wholeBookApplied':False,'wholeCatalogueCompleted':False,
 'effectiveFormationModel':False,'changedOrCalendarTriadCompletion':False,'consumerChanged':False,
 'htmlBytes':len(html),'htmlSHA256':sha(html),'siteClean':True,'webZIPUnchanged':True,'priorEightReferencesPreserved':True,
 'previousSourceZIPPreservedBytes':1150284497,'unchangedEarlierV53Files':unchanged,
 'manifestFilesVerified':len(manifest['files']),'sourceZIPFilesVerified':len(manifest['files'])+1}
if '--no-write' in sys.argv:assert read(qa/'RELEASE_RESULTS.json')==out
else:(qa/'RELEASE_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,ensure_ascii=False))
