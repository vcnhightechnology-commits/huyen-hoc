"""Freeze bounded day/direction source contexts before implementing their inspector."""
from pathlib import Path
from hashlib import sha256
from PIL import Image
import json,itertools
W=Path(__file__).resolve().parents[2];B=Path(__file__).resolve().parent
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def write(n,d):(B/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def ident(p):return {'file':p.relative_to(W).as_posix(),'bytes':p.stat().st_size,'sha256':sha256(p.read_bytes()).hexdigest()}
assert not (B/'PREIMPLEMENTATION_FREEZE.json').exists()
sources=[('v53/research/home-yangzhai-final-spans/selection/raw-p131.jpg','p131-introduction.png',(1250,235,2445,1915)),('v53/research/home-time-premises/ITKC_BT_1508A_V002_244.JPG','itkc244-direction.png',(980,240,1530,2090))]
records=[]
for source,name,box in sources:
 p=W/source;im=Image.open(p);im.crop(box).save(B/name)
 records.append({'source':ident(p),'sourceSize':list(im.size),'crop':ident(B/name),'boxXYXY':list(box),'transform':'native RGB crop; no rescale, OCR or reconstruction','actuallyViewed':False})
write('SOURCE_IDENTITIES.json',{'date':'2026-10-29','records':records,'newHTTPBodies':0,'newSourcePositions':0,'newIndependentWitnesses':0})
write('MANUAL_CONTEXTS.json',{'scope':'Two selected passages, not complete source priority or all table labels.','records':[
 {'system':'P08-DAY-INTRO-131','source':'陽宅十書','frame':'declared-day-table-context','position':131,'literalSelected':'若值建破魁罡等雖有吉星固當迴避','literalImperialClause':'若遇玉皇帝星天皇帝星紫微帝星直日則不避年月方向凶忌造作無礙','disposition':'The named-day avoidance and imperial-star claim are retained separately. Their simultaneous priority and full imperial predicates remain unresolved. The inspector only evaluates the selected avoidance clause.','smallCellGlyphsResolved':False,'wholeClauseApplied':False},
 {'system':'ITKC-MONTH-DIRECTION-244','source':'選擇要略','frame':'declared-monthly-direction-context','position':244,'heading':'建破魁罡方','literalSelected':'其殺止占方道若得三奇祿馬陽龍陰兔走馬六壬等吉星到方宅舍修作尤宜用之','disposition':'A direction-only passage and a whole declared star-condition predicate. No AND/OR between named star systems is inferred; generic benefic presence is insufficient. No derivation of occupied direction, star arrival, month or date.','wholeClauseApplied':False}
 ],'newCalendarObjects':0,'newEngineCalls':0,'consumerChanged':False})
rows=[]
for system,frame in [('P08-DAY-INTRO-131','declared-day-table-context'),('ITKC-MONTH-DIRECTION-244','declared-monthly-direction-context')]:
 for affected,benefic,listed in itertools.product([False,None,True],repeat=3):
  if system.startswith('P08') and listed is not None:continue
  # Manually specified truth semantics, frozen before implementation.
  if system.startswith('P08'):avoid=affected;exception=None
  else:avoid=None;exception=False if False in (affected,listed) else True if affected is True and listed is True else None
  rows.append({'input':{'system':system,'frame':frame,'activity':'printed-dwelling-work','affectedContextConfirmed':affected,'genericBeneficPresent':benefic,'listedStarClauseSatisfied':listed},'expectedLocalAvoidanceClaim':avoid,'expectedLocalFavourableClaim':exception})
write('EXPECTED_CONTEXTS.json',{'frames':rows,'frozenBeforeImplementation':True,'allOverallRecommendations':None,'consumerApplied':False})
write('PREIMPLEMENTATION_FREEZE.json',{'date':'2026-10-29','stage':'before context inspector exists','files':[ident(B/n)for n in ['SOURCE_IDENTITIES.json','MANUAL_CONTEXTS.json','EXPECTED_CONTEXTS.json']],'newEngineCalls':0})
print(json.dumps({'frozenFiles':3,'expectedFrames':len(rows),'crops':2}))
