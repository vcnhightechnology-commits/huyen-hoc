from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json,subprocess,sys
B=Path(__file__).resolve().parent;W=next(p for p in B.parents if(p/'v53/engine.js').is_file())
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def ident(p):return {'file':p.relative_to(W).as_posix(),'bytes':p.stat().st_size,'sha256':sha256(p.read_bytes()).hexdigest()}
assert not(B/'NATIVE_REVIEW.json').exists()
source=W/'v53/research/bazi-jianlu-context/volume3/CADAL06066039.djvu'
assert ident(source)['sha256']=='2334006e3a46b16bdbf0bf6a79512d8d0c4b87a2ce2e8e1ff503121d8f2cffdc'
records=[]
for n,folio in [(88,'003-43b'),(89,'003-44a'),(90,'003-44b')]:
 p=B/f'images/p{n:03}.png';r=next(r for r in read(B/'RENDERS.json')['records']if r['page']==n);assert ident(p)['sha256']==r['sha256']
 records.append({**ident(p),'containerPosition':n,'printedFolioActuallyRead':folio,'fullImageActuallyViewed':True})
review={'date':'2026-10-30','status':'targeted-native-crossreference-read;whole-chapter-open','sourceContainer':ident(source),'records':records,
 'directNativeAnchors':[{'position':88,'literal':'論正印','definition':'正印者乃五行之正庫','groupLiteral':'金命見乙丑木癸未火甲戌水土壬辰丙辰是也'},
 {'position':89,'literal':'有華蓋印如亥卯未得癸未之類'},
 {'position':90,'literal':'諸印要逢庫墓','conditionalContinuations':['生旺扶助互換祿馬貴人併相合','刑衝破害三合六合上見鬼'],'wholeMeaningCompiled':False}],
 'nativeAndDigitalSelectedAnchorsAgree':True,'allCharactersDiplomaticallyCollated':False,
 'waterEarthGroupStillNotSplit':True,'sourceAnchor命MeaningFullyAdjudicated':False,'C19MeaningAdjudicated':False,
 'newNativeDerivatives':3,'positionsViewedInThisTargetedScope':[88,89,90],
 'globallyNewViewedPositionsCount':None,'globalPositionCountReason':'No authoritative volume3 read-union audit performed; do not infer new-to-catalogue count from new PNG derivatives.',
 'newHTTPBodies':0,'newOriginalContainers':0,'newIndependentEditions':0,'newEngineCalls':0,'consumerChanged':False,'wholeCatalogueCompleted':False,
 'next':'Continue remainder論正印at45aonward to bound 福聚/禍聚andothernamed印conditions; keep C19binding and source命anchor open. Localized image agreement supports the lexical lead, not a natal classifier or TenGod replacement.'}
write(B/'NATIVE_REVIEW.json',review)
subprocess.run([sys.executable,str(W/'maintenance/preserve-selected-history.py'),'POST_RELEASE_WORKING_FOLLOWUP.json'],check=True)
p=W/'POST_RELEASE_WORKING_FOLLOWUP.json';d=read(p);d.update(updatedAtUTC=datetime.now(timezone.utc).isoformat(),status='private-volume3-native-seal-crossreference-read;C19binding-open',nativeSourceReview='tmp/bazi-source-seal-staging/NATIVE_REVIEW.json',nativePositionsReviewed=[88,89,90],globallyNewViewedPositionsCount=None,next=review['next']);write(p,d)
write(B/'NATIVE_IDENTITIES.json',{'files':[ident(B/'NATIVE_REVIEW.json'),ident(B/'RENDERS.json'),ident(B/'render-native.mjs'),*[ident(B/f'images/p{n:03}.png')for n in [88,89,90]]],
 'frozenEarlierDigitalWorkPreserved':True,'newEngineCalls':0,'noAdditionalFullZIP':True})
print(json.dumps({'nativePositionsActuallyViewed':[88,89,90],'folios':['43b','44a','44b'],'C19MeaningAdjudicated':False,'newHTTPBodies':0,'newEngineCalls':0,'additionalWholeZIPs':0}))
