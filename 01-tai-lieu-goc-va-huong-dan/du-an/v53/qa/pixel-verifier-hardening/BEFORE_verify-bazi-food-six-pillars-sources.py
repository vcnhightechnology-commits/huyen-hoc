from pathlib import Path
from hashlib import sha256
from PIL import Image,ImageChops
import json,sys
r=Path(__file__).resolve().parents[1];w=r.parent;b=r/'research/bazi-food-six-pillars';q=r/'qa/bazi-food-six-pillars';read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));sha=lambda p:sha256(p.read_bytes()).hexdigest()
ident=read(b/'PROMOTION_IDENTITIES.json');assert len(ident['records'])==16
for x in ident['records']:
 p=w/x['file'];assert p.stat().st_size==x['bytes']and sha(p)==x['sha256'],x['file']
s=(b/'STAGED_test-six-pillars.mjs').read_text(encoding='utf-8')
for old,new in [("from'./source-pillar-example.mjs'","from'../research/bazi-food-six-pillars/source-pillar-example.mjs'"),("const b=resolve(import.meta.dirname),w=resolve(b,'../..'),","const b=resolve(import.meta.dirname,'../research/bazi-food-six-pillars'),w=resolve(b,'../../..'),"),("resolve(b,'REFERENCE_RESULTS.json')","resolve(w,'v53/qa/bazi-food-six-pillars/REFERENCE_RESULTS.json')")]:assert s.count(old)==1;s=s.replace(old,new)
assert s==(r/'scripts/test-bazi-food-six-pillars.mjs').read_text(encoding='utf-8')
source=read(b/'SOURCE_DISPOSITIONS.json')
for x in[source['sourceContainer'],source['sourceDecoder'],source['digitalTranscription']]+source['sourceImages']+source['runtimeProof']:
 p=w/x['file'];assert p.stat().st_size==x['bytes']and sha(p)==x['sha256'],x['file']
assert len(source['sourceImages'])==4 and source['expandedPriorSourcePositions']==4 and not source['newSourcePositions']and not source['newHTTPRequests']
assert read(w/'v46/node_modules/lunar-typescript/package.json')['version']=='1.8.6'
qa=read(b/'QA_IMAGES.json');assert len(qa['records'])==3
for x in qa['records']:
 assert x['actuallyViewed']and x['pixelMatch']and not x['resampled']and sha(b/x['file'])==x['sha256'];assert ImageChops.difference(Image.open(w/x['sourceFile']).convert('RGBA').crop(x['cropBox']),Image.open(b/x['file']).convert('RGBA')).getbbox()is None
freeze=read(b/'PRE_RUNTIME_TRANSCRIPTION.json');assert freeze['newRuntimeCallsAtFreeze']==0 and sha(b/freeze['file'])==freeze['sha256']
table=read(b/'MANUAL_PILLAR_EXAMPLES.json');assert len(table['records'])==6 and table['sourceRootPillar']=='甲子'and table['containerPage']==177 and table['printedFolio']=='005-88a'
assert table['records'][2]=={'targetPillar':'丙辰','sourceLabels':['正印']}
assert table['records'][3]=={'targetPillar':'丙午','sourceLabels':['自刑破命']}
ctx=read(b/'CONTEXT_AUDIT.json');assert sha(w/ctx['retainedContextSource'])==ctx['sha256'];original=read(w/ctx['retainedContextSource']);rows=original.get('records',original.get('contexts'))
for x in ctx['unchangedSelectedDigitalContexts']:assert x==next(y for y in rows if y['id']==x['id'])
assert not ctx['c19Disposition']['numericHalfMultiplierApplied']and ctx['c19Disposition']['sourceFortuneScore']is None
for x in ctx['furtherContextDispositions']:assert not x['computationallyImplemented']and not x['newCoverageLinkCounted']
coverage=read(b/'CURRENT_CONTEXT_COVERAGE.json');previous=read(w/coverage['previousMatrix']);assert sha(w/coverage['previousMatrix'])==coverage['previousMatrixSHA256']
assert len(coverage['records'])==90 and sum(bool(x['selectedModuleLinks'])for x in coverage['records'])==43 and sum(x['wholeContextApplied']for x in coverage['records'])==0
for before,after in zip(previous['records'],coverage['records']):
 if before['id']!='FOOD-00-C18':assert before==after
 else:
  assert not before['selectedModuleLinks']and len(after['selectedModuleLinks'])==1;assert after['selectedModuleLinks'][0]['sha256']==sha(b/'source-pillar-example.mjs')
assert coverage['counts']['parentsWithSelectedModuleOrDeclaredPremiseLinks']==43 and coverage['counts']['parentsWithoutSuchLinks']==47
res=read(q/'REFERENCE_RESULTS.json');assert len(res['checks'])==5 and all(x['ok']for x in res['checks']);assert len(res['cases'])==6
for x,row in zip(res['cases'],table['records']):
 assert x['targetPillar']==row['targetPillar']and x['sourceLabels']==row['sourceLabels']
 for key in['modernTenGod','modernBranchRelation','sourceRootNatalPosition','gatheringScore','halfMultiplier','wholeFoodPatternEstablished','strength','practicalOutcome']:assert x[key]is None
unique=res['uniqueRelation'];assert unique['actualHHCTenGod']=='Thực Thần'and unique['actualLunarTenGod']=='食神'and unique['actualHHCRelationCalls']==unique['actualLunarTenGodTableQueries']==1
assert res['branchProbe']['actualLunarClashPartner']=='午'and not res['branchProbe']['sourceSelfPunishmentMechanismAssigned']
summary=res['summary'];assert summary['canonicalFrameQueries']==3600 and summary['unsupportedBasisNullQueries']==1440 and summary['actualHHCRelationCalls']==summary['actualLunarTenGodTableQueries']==summary['actualLunarClashTableQueries']==1
state=read(b/'WORK_STATE.json');assert not state['wholeCatalogueCompleted']and not state['consumerChanged']and not state['sourceRootRoleResolved']and not state['remainingStemGeneralizationImplemented']
out=dict(date='2026-10-28',promotionIdentities=16,expandedPriorSourcePositions=4,newSourcePositions=0,newHTTPRequests=0,newOriginalContainers=0,newIndependentWitnesses=0,nativeCropsViewedPixelMatched=3,directlyPrintedCases=6,distinctComparedStemPairs=1,completeRuntimeChecks=5,actualHHCRelationCalls=1,actualLunarTenGodTableQueries=1,actualLunarClashTableQueries=1,canonicalFrameQueries=3600,unsupportedBasisNullQueries=1440,actualHHCBaziCharts=0,actualIztroCharts=0,linkedParentContexts=43,unlinkedParentContexts=47,wholeParentContextsApplied=0,sourceRootRoleResolved=False,remainingStemGeneralizationImplemented=False,sourceOutcomesValidated=False,consumerChanged=False,wholeCatalogueCompleted=False)
p=q/'SOURCE_RESULTS.json'
if '--no-write'in sys.argv:assert read(p)==out
else:p.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
