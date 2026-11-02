from pathlib import Path
from hashlib import sha256
from PIL import Image,ImageChops
import json,sys
r=Path(__file__).resolve().parents[1];w=r.parent;b=r/'research/bazi-food-seats';q=r/'qa/bazi-food-seats'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
sha=lambda p:sha256(p.read_bytes()).hexdigest()
ident=read(b/'PROMOTION_IDENTITIES.json');assert len(ident['records'])==13
for x in ident['records']:
 p=w/x['file'];assert p.stat().st_size==x['bytes']and sha(p)==x['sha256'],x['file']
text=(b/'STAGED_test-food-seats.mjs').read_text(encoding='utf-8')
for old,new in [("from './food-seat-reference.mjs'","from '../research/bazi-food-seats/food-seat-reference.mjs'"),("const b=import.meta.dirname,w=resolve(b,'../..'),c={};","const b=resolve(import.meta.dirname,'../research/bazi-food-seats'),w=resolve(b,'../../..'),c={};"),("resolve(b,'REFERENCE_RESULTS.json')","resolve(w,'v53/qa/bazi-food-seats/REFERENCE_RESULTS.json')")]:assert text.count(old)==1;text=text.replace(old,new)
assert text==(r/'scripts/test-bazi-food-seats.mjs').read_text(encoding='utf-8')
table=read(b/'MANUAL_SEAT_CLAUSE.json');assert len(table['records'])==5 and sum(len(x['branches'])for x in table['records'])==20
assert table['normalizationIsNotFullCharacterCollation']and len(table['explicitEditorialNormalizations'])==2
assert table['records']==[
 dict(dayStems=list('甲乙'),foodStems=list('丙丁'),branches=list('寅卯巳午')),dict(dayStems=list('丙丁'),foodStems=list('戊己'),branches=list('辰戌丑未')),dict(dayStems=list('戊己'),foodStems=list('庚辛'),branches=list('巳午申酉')),dict(dayStems=list('庚辛'),foodStems=list('壬癸'),branches=list('申酉亥子')),dict(dayStems=list('壬癸'),foodStems=list('甲乙'),branches=list('亥子寅卯'))]
qa=read(q/'QA_IMAGES.json');assert len(qa['records'])==2
for x in qa['records']:
 src=w/x['sourceFile'];p=q/x['file'];assert x['actuallyViewed']and not x['resampled']and sha(src)==x['sourceSHA256']and sha(p)==x['sha256']
 assert ImageChops.difference(Image.open(src).convert('RGB').crop(x['cropBox']),Image.open(p).convert('RGB')).getbbox()is None
source=read(b/'SOURCE_DISPOSITIONS.json');assert sha(w/source['sourceContextFile'])==source['sourceContextSHA256']=='c9179c1421a4521ce9bd0f5d48ab05e28a6a9ed11daf462927ad777343be0f68'
res=read(q/'REFERENCE_RESULTS.json');assert len(res['checks'])==5 and all(x['ok']for x in res['checks'])
assert res['actualHHCTenGodCalls']==100 and len(res['relationChecks'])==100 and sum(x['sourceFoodRelation']for x in res['relationChecks'])==10
assert len(res['coordinates'])==600 and sum(x['food']for x in res['coordinates'])==60 and sum(x['member']for x in res['coordinates'])==20
assert res['actualHHCBaziChartCalls']==2 and [x['matchingPillarIndices']for x in res['chartProjections']]==[[1,3],[]]
assert all(x['historicalBirthDateAttributed']is False for x in res['chartProjections'])
coverage=read(r/'research/library-current/COVERAGE.json');item=next(x for x in coverage['catalogue']if x['id']=='M01')
assert item['foodParentContextSelection']['parentsWithSelectedClauses']==9 and item['foodParentContextSelection']['otherParentsNotSelected']==81
assert not read(b/'WORK_STATE.json')['wholeCatalogueCompleted']and not res['fullC20ClauseConditionsApplied']
assert sha(r/'engine.js')=='39f08bd1887faca4d35f7ad415ebf596621010d530b489212774d5cbf99040e6'
assert sha(r/'bazi-relations.js')=='a1599a0ddbe716f02111e56f5da82943bd2878356fc3959a411fbffc8bd8e6d0'
out=dict(date='2026-10-28',promotionIdentities=13,completeRuntimeChecks=5,sourceFamilyRows=5,canonicalBranchMemberships=20,
 actualHHCTenGodCalls=100,actualHHCBaziCalls=2,abstractValidCoordinateContexts=600,foodRelationCoordinates=60,selectedSeatCoordinates=20,
 previousSourceExamplesReprojected=2,newIndependentSourceExamples=0,selectedParentContexts=9,otherParentsNotSelected=81,nativeCropsViewedPixelMatched=2,
 editorialGlyphNormalizationsExplicit=True,newHTTPBodies=0,newSourcePositions=0,consumerChanged=False,fullStrengthEstablished=False,fullC20ClauseConditionsApplied=False,wholeCatalogueCompleted=False)
p=q/'SOURCE_RESULTS.json'
if '--no-write'in sys.argv:assert read(p)==out
else:p.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
