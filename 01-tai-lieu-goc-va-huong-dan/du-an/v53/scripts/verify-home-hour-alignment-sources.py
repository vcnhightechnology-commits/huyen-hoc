from pathlib import Path
from hashlib import sha256
from PIL import Image,ImageChops
import json,sys
r=Path(__file__).resolve().parents[1];w=r.parent;b=r/'research/home-hour-alignment';q=r/'qa/home-hour-alignment'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
sha=lambda p:sha256(p.read_bytes()).hexdigest()
ident=read(b/'PROMOTION_IDENTITIES.json');assert len(ident['records'])==20
for x in ident['records']:
 p=w/x['file'];assert p.stat().st_size==x['bytes']and sha(p)==x['sha256'],x['file']
text=(b/'STAGED_test-corrected-hour-reference.mjs').read_text(encoding='utf-8')
for old,new in [("from './source-hour-reference.mjs'","from '../research/home-hour-alignment/source-hour-reference.mjs'"),("const b=import.meta.dirname,w=resolve(b,'../..'),system=SOURCE_HOUR_SYSTEM;","const b=resolve(import.meta.dirname,'../research/home-hour-alignment'),w=resolve(b,'../../..'),system=SOURCE_HOUR_SYSTEM;"),("resolve(b,'REFERENCE_RESULTS.json')","resolve(w,'v53/qa/home-hour-alignment/REFERENCE_RESULTS.json')")]:assert text.count(old)==1;text=text.replace(old,new)
assert text==(r/'scripts/test-home-hour-alignment.mjs').read_text(encoding='utf-8')
prior=r/'research/home-yangzhai-final-spans/selection';old=read(prior/'MANUAL_HOUR_TABLE.json');table=read(b/'MANUAL_HOUR_TABLE.json')
assert table['columns'][:10]==old['columns'][:10]and len(table['columns'])==12 and table['directEnteredCells']==144
assert table['columns'][10]['sourceLabel']=='司命'and ''.join(table['columns'][10]['hoursByDayBranch'])=='午申戌子寅辰午申戌子寅辰'
assert table['columns'][11]['sourceLabel']=='勾陳'and ''.join(table['columns'][11]['hoursByDayBranch'])=='未酉亥丑卯巳未酉亥丑卯巳'
module=(prior/'source-hour-reference.mjs').read_text(encoding='utf-8')
for a,z in [("status:sourceLabel==='司命'?'literal-source-engine-discrepancy':'literal-source-coordinate'","status:'literal-source-coordinate'"),('coverageIncomplete:true','coverageIncomplete:false'),("pendingSourceLabels:['勾陳']","pendingSourceLabels:[]")]:assert module.count(a)==1;module=module.replace(a,z)
assert module==(b/'source-hour-reference.mjs').read_text(encoding='utf-8')
qa=read(q/'CORRECTION_QA_IMAGES.json');assert len(qa['records'])==4
for x in qa['records']:
 p=q/x['file'];src=w/x['sourceFile'];assert x['actuallyViewed']and not x['resampled']and sha(src)==x['sourceSHA256']and sha(p)==x['sha256']
 assert ImageChops.difference(Image.open(src).convert('RGB').crop(x['cropBox']),Image.open(p).convert('RGB')).getbbox()is None
res=read(q/'REFERENCE_RESULTS.json');assert len(res['checks'])==6 and all(x['ok']for x in res['checks'])
assert len(res['fixtures'])==144 and all(x['match']and x['typeMatch']for x in res['fixtures'])
assert res['actualLunarObjects']==res['actualHourLabelQueries']==res['actualHourTypeQueries']==144
correction=read(q/'CORRECTION_RESULTS.json');assert correction['old12DifferenceClaimRetracted']and correction['oldPendingColumnClaimRetracted']
assert read(b/'READING_CORRECTION_AUDIT.json')['notEngineBug']
coverage=read(r/'research/library-current/COVERAGE.json');p08=next(x for x in coverage['catalogue']if x['id']=='P08')
assert p08['currentHourReference']=='v53/research/home-hour-alignment/source-hour-reference.mjs'
assert p08['currentSourceUnitCounts']['manualHourCells']==144 and p08['currentSourceUnitCounts']['pendingHourCells']==p08['currentSourceUnitCounts']['retainedHourDifferences']==0
ex=read(w/'EXHAUSTIVE_WORK_STATE.json');assert ex['currentWork']['internalHourReference']=='v53/research/home-hour-alignment/source-hour-reference.mjs'
assert not any('12司命'in x or '12勾陳'in x for x in ex['subsequentPriority'])
out=dict(date='2026-10-28',promotionIdentities=20,completeRuntimeChecks=6,correctedManualCoordinates=144,unchangedPriorColumns=10,correctedSimingCells=12,addedGouChenCells=12,
 actualLunarObjects=144,actualHourLabelQueries=144,actualHourTypeQueries=144,allLabelAndTypeMatches=144,remainingSourceHourCoordinateDifferences=0,prior12DifferencesRetractedAsTranscriptionError=True,
 nativeCropsViewedPixelMatched=4,neighborDayGuideSemanticRoleUnresolved=True,newSourceHTTPBodies=0,newSourcePositions=0,newIndependentWitnesses=0,consumerChanged=False,allCalendarSelectionConditionsApplied=False,wholeCatalogueCompleted=False)
p=q/'SOURCE_RESULTS.json'
if '--no-write'in sys.argv:assert read(p)==out
else:p.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
