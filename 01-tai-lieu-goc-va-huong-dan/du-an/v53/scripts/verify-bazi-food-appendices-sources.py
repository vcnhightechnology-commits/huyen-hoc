from pathlib import Path
from hashlib import sha256
from PIL import Image, ImageChops
import json, sys
r=Path(__file__).resolve().parents[1];w=r.parent;b=r/'research/bazi-food-appendices';q=r/'qa/bazi-food-appendices'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
sha=lambda p:sha256(p.read_bytes()).hexdigest()
ident=read(b/'PROMOTION_IDENTITIES.json');assert len(ident['records'])==21
for x in ident['records']:
 p=w/x['file'];assert p.stat().st_size==x['bytes']and sha(p)==x['sha256'],x['file']
text=(b/'STAGED_test-appendices.mjs').read_text(encoding='utf-8')
for old,new in [
 ("from './appendix-reference.mjs'","from '../research/bazi-food-appendices/appendix-reference.mjs'"),
 ("const b=import.meta.dirname,w=resolve(b,'../..'),ctx={};","const b=resolve(import.meta.dirname,'../research/bazi-food-appendices'),w=resolve(b,'../../..'),ctx={};"),
 ("resolve(b,'REFERENCE_RESULTS.json')","resolve(w,'v53/qa/bazi-food-appendices/REFERENCE_RESULTS.json')")]:
 assert text.count(old)==1;text=text.replace(old,new)
assert text==(r/'scripts/test-bazi-food-appendices.mjs').read_text(encoding='utf-8')
ctx=read(b/'SELECTED_CONTEXTS.json');assert sha(w/ctx['source'])==ctx['sha256']=='c9179c1421a4521ce9bd0f5d48ab05e28a6a9ed11daf462927ad777343be0f68'
allctx=read(w/ctx['source'])['records'];original={x['id']:x for x in allctx}
assert len(ctx['records'])==17 and all(x==original[x['id']]for x in ctx['records'])
assert sum(len(x['text'])for x in ctx['records'])==426
d=read(b/'CLAUSE_DISPOSITIONS.json');assert len(d['records'])==17 and d['headings']==6 and d['nonHeadingContexts']==11
assert {x['parentContext']for x in d['records']}=={x['id']for x in ctx['records']}
assert all(not x['wholeClauseApplied']and not x['practicalOutcomeValidated']for x in d['records'])
table=read(b/'EXPLICIT_COORDINATES.json');assert len(table['records'])==23
assert len({x['system']for x in table['records']})==7
assert sum(x['system']=='daihe'for x in table['records'])==6
assert sum(x['system']=='hongluan-tianyin'for x in table['records'])==4
assert sum(x['system']=='mochi'for x in table['records'])==7
assert all(x['targetPositions']==[2,3]for x in table['records']if x['system']=='hongluan-tianyin')
assert all(x['requiredAnchorFrame']=='year'for x in table['records']if x['system']in ['fuxing','tongke-owl'])
qa=read(q/'QA_IMAGES.json');assert len(qa['records'])==6
for x in qa['records']:
 assert x['actuallyViewed']and not x['resampled']and sha(w/x['sourceFile'])==x['sourceSHA256']and sha(q/x['file'])==x['sha256']
 assert ImageChops.difference(Image.open(w/x['sourceFile']).convert('RGB').crop(x['cropBox']),Image.open(q/x['file']).convert('RGB')).getbbox()is None
source=read(b/'SOURCE_DISPOSITIONS.json')
for name in ['sourceContainer','digital']:assert sha(w/source[name]['file'])==source[name]['sha256']
assert [x['sourceContainerPage']for x in source['rawExpandedViews']]==[190,191,192,195,196]
for x in source['rawExpandedViews']:assert x['expandedActuallyViewed']and not x['newSourcePosition']and sha(w/x['file'])==x['sha256']
matrix=read(b/'CURRENT_CONTEXT_COVERAGE.json');assert len(matrix['records'])==90
assert {x['id']for x in matrix['records']}==set(original)
assert sum(bool(x['selectedModuleLinks'])for x in matrix['records'])==32
assert sum(not x['selectedModuleLinks']for x in matrix['records'])==58
assert matrix['counts']['coreSeatsOwlParents']==10 and matrix['counts']['earlierSpecialFoodProvenanceParents']==13 and matrix['counts']['newAppendixParents']==9
for x in matrix['records']:
 assert not x['wholeContextApplied']and not x['sourceOutcomeValidated']
 for link in x['selectedModuleLinks']:assert sha(w/link['module'])==link['sha256']and not link['wholeContextApplied']
res=read(q/'REFERENCE_RESULTS.json');assert len(res['checks'])==9 and all(x['ok']for x in res['checks'])
assert len(res['relations'])==26 and len(res['mechanisms'])==7 and len(res['derived'])==60
assert sum(x['actualTenGod']=='Thực Thần'for x in res['relations'])==24
assert sum(x['actualTenGod']=='Thiên Ấn'for x in res['relations'])==2
assert all(x['actualTenGod']=='Thực Thần'for x in res['derived'])
summary=res['summary'];assert summary['finalHHCTenGodQueries']==86 and summary['derivedValidPairCoordinatesChecked']==3600
assert summary['actualLunarLuTableQueries']==1 and summary['actualLunarCombinationTableQueries']==6
for x in res['actualModules']:assert sha(w/x['file'])==x['sha256']
assert source['runtimeRuns']==1 and not source['effectiveCombinationEstablished']and not source['sourceOutcomeValidated']
state=read(b/'WORK_STATE.json');assert not state['wholeCatalogueCompleted']and not state['fullAppendixMethodsApplied']
out=dict(date='2026-10-28',promotionIdentities=21,completeRuntimeChecks=9,sourceUnits=6,
 sourceParentContextsDispositioned=17,sourceCodepoints=426,literalCoordinateRecords=23,namedCoordinateSystems=7,
 nativeCropsViewedPixelMatched=6,expandedNativePositions=[190,191,192,195,196],
 actualHHCTenGodQueries=86,literalHHCTenGodQueries=26,derivedHHCTenGodQueries=60,
 actualLunarLuTableQueries=1,actualLunarCombinationTableQueries=6,
 derivedValidPairCoordinatesChecked=3600,derivedMatches=60,derivedSixtyRowTableNotPrinted=True,
 currentFoodParents=90,parentsWithPartialModuleOrDeclaredPremiseLinks=32,parentsWithoutLinks=58,
 earlierSpecialFoodProvenanceParentsPreviouslyExcludedFromTotal=13,newAppendixLinkedParents=9,wholeParentsApplied=0,
 newHTTPBodies=0,newSourcePositions=0,newContainers=0,newCalendarChartCalls=0,
 sourceNatalAnchorsFullyEstablished=False,effectiveCombinationEstablished=False,consumerChanged=False,wholeCatalogueCompleted=False)
p=q/'SOURCE_RESULTS.json'
if '--no-write'in sys.argv:assert read(p)==out
else:p.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
