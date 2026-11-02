from pathlib import Path
from hashlib import sha256
from PIL import Image,ImageChops
import json,sys,subprocess,tempfile
r=Path(__file__).resolve().parents[1];w=r.parent;b=r/'research/liuyao-b03-triad-clause';q=r/'qa/liuyao-b03-triad-clause';read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));sha=lambda p:sha256(p.read_bytes()).hexdigest()
ident=read(b/'PROMOTION_IDENTITIES.json');assert len(ident['records'])==20
for x in ident['records']:
 p=w/x['file'];assert p.stat().st_size==x['bytes']and sha(p)==x['sha256'],x['file']
s=(b/'STAGED_triad-clause-reference.mjs').read_text(encoding='utf-8');old="from'../../v53/research/liuyao-foundations/liuyao-reference.mjs'";assert s.count(old)==1;s=s.replace(old,"from'../liuyao-foundations/liuyao-reference.mjs'");assert s==(b/'triad-clause-reference.mjs').read_text(encoding='utf-8')
s=(b/'STAGED_test-triad-clause.mjs').read_text(encoding='utf-8')
for old,new in[("from'./triad-clause-reference.mjs'","from'../research/liuyao-b03-triad-clause/triad-clause-reference.mjs'"),("from'../../v53/research/liuyao-b03-volume4/triad-reference.mjs'","from'../research/liuyao-b03-volume4/triad-reference.mjs'"),("const b=resolve(import.meta.dirname),w=resolve(b,'../..'),","const b=resolve(import.meta.dirname,'../research/liuyao-b03-triad-clause'),w=resolve(b,'../../..'),"),("resolve(b,'REFERENCE_RESULTS.json')","resolve(w,'v53/qa/liuyao-b03-triad-clause/REFERENCE_RESULTS.json')")]:assert s.count(old)==1;s=s.replace(old,new)
assert s==(r/'scripts/test-liuyao-b03-triad-clause.mjs').read_text(encoding='utf-8')
source=read(b/'SOURCE_MANIFEST.json')
for x in[source['sourcePDF']]+source['sourceImages']+source['runtimeAndPriorReferenceIdentities']+[source['renderer']]:
 p=w/x['file'];assert p.stat().st_size==x['bytes']and sha(p)==x['sha256'],x['file']
for key in['retainedAcquisition','retainedHTTPRecords']:assert sha(w/source[key])==source[key+'SHA256']
assert source['sourcePDF']['bytes']==41224832 and source['sourcePDF']['sha256']=='c1e1027331d43769733c6011b4fe99e90928e9fde013fce563c8e9bad81c04bf'
assert source['newHTTPBodies']==source['newOriginalContainers']==source['newSourcePositions']==source['newIndependentWitnesses']==0
render=read(b/'RENDER_RECORD.json');assert render['cropActuallyViewed']and not render['renderWhole360Viewed']and render['oldWhole180RenderExpandedViewed'];assert sha(b/render['renderFile'])==render['renderSHA256'];assert render['renderSize']==[2304,1997]
qa=read(b/'QA_IMAGES.json');assert len(qa['records'])==4
for x in qa['records']:
 assert x['actuallyViewed']and x['pixelMatch']and not x['resampled']and sha(b/x['file'])==x['sha256'];assert ImageChops.difference(Image.open(b/render['renderFile']).convert('RGBA').crop(x['cropBox']),Image.open(b/x['file']).convert('RGBA')).getbbox()is None
# Reproduce one PDF-derived raster in an ephemeral directory, never alter retained research files.
with tempfile.TemporaryDirectory(prefix='hhc-b03-triad-qa-')as temporary:
 prefix=Path(temporary)/'p39';subprocess.run([source['renderer']['file'],'-r','360','-f','39','-l','39','-singlefile','-png',str(w/source['sourcePDF']['file']),str(prefix)],check=True,capture_output=True)
 assert ImageChops.difference(Image.open(prefix.with_suffix('.png')).convert('RGBA'),Image.open(b/render['renderFile']).convert('RGBA')).getbbox()is None
freeze=read(b/'PRE_RUNTIME_READING.json');assert freeze['newRuntimeCallsAtFreeze']==0 and sha(b/freeze['file'])==freeze['sha256']
table=read(b/'FULL_CLAUSE.json');assert len(table['groups'])==6 and len(table['clauses'])==4;assert '必須見全有兩爻動則刑合得一爻起'in table['literalReading'];assert '如一爻動則刑合不得兩爻起了'in table['literalReading'];assert '縱見全倘俱安靜便不成刑合了'in table['literalReading'];assert not table['allThreeActiveAddressedByThisPassage']and not table['activeFactsAutomaticallyComputedFromCalendar']
correction=read(b/'READING_CORRECTION.json');assert sha(w/correction['previousTable'])==correction['previousSHA256']and sha(w/correction['oldReference'])==correction['oldReferenceSHA256'];assert correction['currentLiteral']==table['literalReading']and correction['oldFilesPreserved']and not correction['consumerAffected']
res=read(q/'REFERENCE_RESULTS.json');assert len(res['checks'])==5 and all(x['ok']for x in res['checks']);assert len(res['declarations'])==162 and len(res['vectors'])==4
counts={True:0,False:0,None:0}
for x in res['declarations']:
 group=next(g for g in table['groups']if g['id']==x['groupID']);assert set(n['branch']for n in x['members'])==set(group['members'])
 active=sum(n['active']is True for n in x['members']);unknown=any(n['active']is None for n in x['members']);expected=None if unknown or active==3 else active==2;assert x['localPremisePass']is expected;counts[expected]+=1
 assert x['sourceFormation']is None and x['strength']is None and x['practicalOutcome']is None
assert counts=={True:18,False:24,None:120}
assert [x['actualHHCChangedNumber']for x in res['vectors']]==[1,44,6,64]
for i,x in enumerate(res['vectors']):
 assert x['kind']=='editorial-mechanical-test-vector;notprintedsourcecast'and x['actualHHCPrimaryNumber']==1;assert x['sourceWitness']['knownActiveCount']==i;assert x['sourceWitness']['localPremisePass']is([False,False,True,None][i]);assert x['sourceWitness']['raisedLine']==(5 if i==2 else None)
assert res['summary']['actualHHCHexNumberCalls']==4 and not res['summary']['printedSourceCastsNew']and not res['summary']['fullSourceFormationImplemented']
audit=read(b/'EXECUTION_AUDIT.json');assert audit['runtimeBatches']==1 and audit['actualHHCHexNumberCalls']==4 and not audit['previousAttempt']['executed'];assert audit['previousAttempt']['nextHumanContinueRetrySucceeded']
state=read(b/'WORK_STATE.json');assert not state['wholeCatalogueCompleted']and not state['consumerChanged']and not state['fullSourceFormationImplemented']
out=dict(date='2026-10-28',promotionIdentities=20,expandedPriorSourcePositions=2,newSourcePositions=0,newHTTPRequests=0,newOriginalContainers=0,newIndependentWitnesses=0,nativeCropsViewedPixelMatched=4,renderReproductionsPixelMatched=1,sourceGroups=6,boundedClauses=4,completeRuntimeChecks=5,ternaryDeclaredContexts=162,localPass=18,localFail=24,unresolved=120,mechanicalVectors=4,newPrintedCasts=0,actualHHCHexNumberCalls=4,actualIztroCalls=0,previousSourceAndModulePreserved=True,oldLiteralAndOperationalThresholdSuperseded=True,fullSourceFormationImplemented=False,sourceOutcomesValidated=False,consumerChanged=False,wholeCatalogueCompleted=False)
p=q/'SOURCE_RESULTS.json'
if '--no-write'in sys.argv:assert read(p)==out
else:p.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
