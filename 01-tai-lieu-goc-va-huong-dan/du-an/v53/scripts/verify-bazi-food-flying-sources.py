from pathlib import Path
from hashlib import sha256,sha1
from PIL import Image,ImageChops
import json,sys
r=Path(__file__).resolve().parents[1];w=r.parent;b=r/'research/bazi-food-gap-witness';q=r/'qa/bazi-food-gap-witness'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
sha=lambda p:sha256(p.read_bytes()).hexdigest()
ident=read(b/'PROMOTION_IDENTITIES.json');assert len(ident['records'])==40
for x in ident['records']:
 p=w/x['file'];assert p.stat().st_size==x['bytes']and sha(p)==x['sha256'],x['file']
text=(b/'STAGED_test-flying.mjs').read_text(encoding='utf-8')
for old,new in [
 ("from './flying-reference.mjs'","from '../research/bazi-food-gap-witness/flying-reference.mjs'"),
 ("const b=import.meta.dirname,w=resolve(b,'../..'),ctx={};","const b=resolve(import.meta.dirname,'../research/bazi-food-gap-witness'),w=resolve(b,'../../..'),ctx={};"),
 ("resolve(b,'REFERENCE_RESULTS.json')","resolve(w,'v53/qa/bazi-food-gap-witness/REFERENCE_RESULTS.json')")]:
 assert text.count(old)==1;text=text.replace(old,new)
assert text==(r/'scripts/test-bazi-food-flying.mjs').read_text(encoding='utf-8')
req=read(b/'REQUESTS.json')['records'];assert len(req)==3
for x in req:assert x['status']==200 and x['TLSCertificateValidationEnabled']and (b/x['file']).stat().st_size==x['bytes']and sha(b/x['file'])==x['sha256']
acq=read(b/'ACQUISITION.json');raw=(b/acq['sourceFile']).read_bytes()
assert len(raw)==acq['sourceBytes']==10808462
assert sha256(raw).hexdigest()==acq['sourceSHA256']=='4f273322b3fd4339789e1408e0bbb4ea15a7956e5e508c6f99fced264e0b53ee'
assert sha1(raw).hexdigest()==acq['metadata']['sha1']=='8dd4e5a566348ba56c2c3fb4f888dfac33349436'
assert raw[:8]==b'AT&TFORM'and acq['metadata']['pagecount']==230
assert not acq['sourceWholeWorkRead']and not acq['institutionOriginalBytesDownloaded']
render=read(b/'LOCAL_RENDERS.json');assert len(render['records'])==9
assert [x['page']for x in render['records']]==list(range(187,196))
assert render['sourceSHA256']==acq['sourceSHA256']and render['containerPages']==230
assert sha(w/render['decoder'])==render['decoderSHA256']=='10a831d62cc7ced39c30c7350a11410402d082a0f0a5b073a88d3d7ca662add3'
for x in render['records']:
 p=b/x['file'];im=Image.open(p)
 assert x['actuallyViewed']and sha(p)==x['sha256']and im.size==(x['width'],x['height'])
 assert sha256(im.convert('RGBA').tobytes()).hexdigest()==x['pixelRGBA_SHA256']
qa=read(q/'QA_IMAGES.json');assert len(qa['records'])==6
for x in qa['records']:
 assert x['actuallyViewed']and not x['resampled']and sha(q/x['file'])==x['sha256']
 assert ImageChops.difference(Image.open(b/x['sourceFile']).convert('RGB').crop(x['cropBox']),Image.open(q/x['file']).convert('RGB')).getbbox()is None
mapping=read(b/'FOLIO_MAPPING.json');assert [x['newContainerPage']for x in mapping['recoveredGapFaces']]==[189,190,191,192]
assert [x['folio']for x in mapping['recoveredGapFaces']]==['005-94a','005-94b','005-95a','005-95b']
assert [(x['oldPage'],x['newPage'])for x in mapping['comparedOldBoundaryPositions']]==[(188,188),(189,193)]
assert not mapping['original226ContainerGloballySearchedOrRepaired']
ctx=read(b/'SELECTED_CONTEXTS.json');assert sha(w/ctx['source'])==ctx['sha256']=='c9179c1421a4521ce9bd0f5d48ab05e28a6a9ed11daf462927ad777343be0f68'
allctx={x['id']:x for x in read(w/ctx['source'])['records']}
assert len(ctx['records'])==17 and sum(len(x['text'])for x in ctx['records'])==1620
assert all(allctx[x['id']]==x for x in ctx['records'])
d=read(b/'CLAUSE_DISPOSITIONS.json');assert len(d['records'])==17 and all(not x['wholeContextApplied']for x in d['records'])
table=read(b/'DAY_AND_COORDINATE_TABLES.json');assert [len(x['days'])for x in table['daySets']]==[4,2,6]
assert len(table['mechanismCases'])==6 and not table['finalFeiComment']['notAnAlternativeTwoDayEligibilityList']is False
assert next(x for x in table['mechanismCases']if x['id']=='dao-dingsi')['printedRestraintBranchPool']==['申','辰']
matrix=read(b/'CURRENT_CONTEXT_COVERAGE.json');assert len(matrix['records'])==90
assert sum(bool(x['selectedModuleLinks'])for x in matrix['records'])==42
assert sum(not x['selectedModuleLinks']for x in matrix['records'])==48
previous={x['id']:x for x in read(r/'research/bazi-food-appendices/CURRENT_CONTEXT_COVERAGE.json')['records']}
added=0
for x in matrix['records']:
 assert not x['wholeContextApplied']and not x['sourceOutcomeValidated']
 assert all(link in x['selectedModuleLinks']for link in previous[x['id']]['selectedModuleLinks'])
 if len(x['selectedModuleLinks'])>len(previous[x['id']]['selectedModuleLinks']):added+=1
 for link in x['selectedModuleLinks']:assert sha(w/link['module'])==link['sha256']and not link['wholeContextApplied']
assert added==10
res=read(q/'REFERENCE_RESULTS.json');assert len(res['checks'])==8 and all(x['ok']for x in res['checks'])
assert len(res['officers'])==6 and all(x['actualTenGod']=='Chính Quan'for x in res['officers'])
assert [x['actualTenGod']for x in res['labels']]==['Thương Quan','Kiếp Tài','Thương Quan','Kiếp Tài']
assert len(res['mechanisms'])==6 and next(x for x in res['mechanisms']if x['caseID']=='dao-dingsi')['additionalPrintedRestraintTokens']==['辰']
summary=res['summary'];assert summary['actualHHCTenGodQueries']==10 and summary['actualLunarHiddenStemTableQueries']==10
assert summary['actualLunarClashTableQueries']==6 and summary['actualLunarSixCombineTableQueries']==6 and summary['validDayMembershipCoordinates']==180
for x in res['actualModules']:assert sha(w/x['file'])==x['sha256']
source=read(b/'SOURCE_DISPOSITIONS.json');old=source['earlierRepositoryContainer']
assert sha(w/old['file'])==old['sha256']=='013ce4861680a2bf08b811050c45a45bb2d3ce9d164f7e2341d7070bd5cb2c1a'
assert source['runtimeRuns']==1 and not source['independentEditionEstablished']and not source['sourceWholeBookRead']
state=read(b/'WORK_STATE.json');assert not state['wholeCatalogueCompleted']and not state['fullSourceMethodsApplied']
out=dict(date='2026-10-28',promotionIdentities=40,completeRuntimeChecks=8,newRetainedHTTP200TLSBodies=3,
 newRepositoryContainerBytes=10808462,newRepositoryContainerPositions=230,newRepositorySHA256=acq['sourceSHA256'],
 newNativePositionsViewed=9,nativeCropsViewedPixelMatched=6,recoveredGapFaces=['005-94a','005-94b','005-95a','005-95b'],overlappingTextPositions=5,
 old226ContainerUnchanged=True,independentEditionEstablished=False,wholeBookRead=False,
 sourceParentContextsDispositioned=17,sourceCodepoints=1620,namedDaySetSizes=[4,2,6],literalMechanismCases=6,
 validDayMembershipCoordinates=180,actualHHCTenGodQueries=10,actualLunarHiddenStemTableQueries=10,
 actualLunarClashTableQueries=6,actualLunarSixCombineTableQueries=6,additionalLiteralRestraint='丁巳:辰',
 virtualTargetAddedToActualPillars=False,sourceActualCalendarPolicyEstablished=False,
 currentFoodParents=90,partialLinkedParents=42,unlinkedParents=48,wholeParentsApplied=0,
 newCalendarChartCalls=0,consumerChanged=False,wholeCatalogueCompleted=False)
p=q/'SOURCE_RESULTS.json'
if '--no-write'in sys.argv:assert read(p)==out
else:p.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
