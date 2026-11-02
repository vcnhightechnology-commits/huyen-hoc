from pathlib import Path
from hashlib import sha256
from PIL import Image,ImageChops
import json
b=Path(__file__).resolve().parent
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
save=lambda name,o:(b/name).write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
renders=read(b/'LOCAL_RENDERS.json')
for x in renders['records']:
 x['actuallyViewed']=True;x['folioCoordinate']=str((x['page']-1)//2)+('a'if x['page']%2 else 'b');x.pop('observedFolio',None)
 x['folioBasis']='Printed odd-leaf numeral actually read'if x['page']%2 else'Counterpart b side projected from adjacent printed odd-leaf numeral and continuous content; not a separately printed b suffix.'
 x['scope']='Expanded first-pass reading of targeted chapter/boundaries; not whole volume or all glyphs collated.'
save('LOCAL_RENDERS.json',renders)
rows=[('spring','春',dict(木='旺',火='相',土='死',金='囚',水='休')),
 ('summer','夏',dict(木='休',火='旺',土='相',金='死',水='因')),
 ('sixth-month-earth','六月',dict(木='囚',火='休',土='旺',金='相',水='死')),
 ('autumn','秋',dict(木='死',火='囚',土='休',金='旺',水='相')),
 ('winter','冬',dict(木='相',火='死',土='囚',金='休',水='旺'))]
records=[]
for phase,sourcePhase,states in rows:
 for element,literal in states.items():
  records.append(dict(phase=phase,sourcePhase=sourcePhase,element=element,literalState=literal,recognizedState=literal if literal in list('旺相休囚死')else None,
   sourceContainerPages=[110,111]if phase=='spring'else[111],glyphAdjudication='Native glyph retained; 因 not automatically emended to 囚'if literal=='因'else'Canonical state reading; full diplomatic typography not claimed'))
save('MANUAL_SEASON_TABLE.json',dict(date='2026-10-28',entryMethod='Manual five-phase table from new native source images before formula/engine comparison; preserve 因-like summer-water glyph as unclassified.',records=records,slots=25,recognizedStateSlots=24,unclassifiedLiteralSlots=1,
 sourceSixthMonthNotAutomaticallyFourSeasonalEnds=True,dateToSourcePhaseAdapterEstablished=False,fullNatalStrengthEstablished=False,sourceOutcomesValidated=False))
specs=[(111,'p111-summer-water-native.png',[1080,1000,1350,2840]),(110,'p110-title-native.png',[930,350,1200,2200]),
 (111,'p111-winter-soil-native.png',[280,1700,560,2500]),(111,'p111-autumn-fire-native.png',[500,650,780,1650]),
 (111,'p111-spring-metal-native.png',[1530,500,1820,1500]),(111,'p111-sixth-month-wood-native.png',[720,200,1000,1000])]
qa=[]
for p,name,box in specs:
 out=b/name;src=b/f'p{p}.png';im=Image.open(src).convert('RGB').crop(box);assert ImageChops.difference(im,Image.open(out).convert('RGB')).getbbox()is None
 qa.append(dict(sourceContainerPage=p,sourceFile=src.name,file=name,cropBox=box,sha256=sha256(out.read_bytes()).hexdigest(),resampled=False,actuallyViewed=True))
save('QA_IMAGES.json',dict(date='2026-10-28',records=qa))
save('READING_AUDIT.json',dict(date='2026-10-28',issue='Digital 夏水因 is also an 因-like glyph in native111; title110 clearly supplies 囚 category. Formula would suggest 囚 but no emendation established.',
 currentDecision='Keep literal因 with recognizedState:null; do not turn a common formula into a source reading.',
 phaseBoundaryIssue='六月土旺 is an explicit source label; this selected text does not establish modern calendar boundaries or all four季末18days.',
 sourceWarning=dict(containerPage=114,literal='見生旺者未必便作吉論見休囚死絶未必便作凶言',disposition='State labels must not become overall good/bad or health/financial outcomes.'),
 otherSection='Twelve寄生 stages and metaphors on112–115 remain distinct from five-state seasonal labels; no merge into current lunar ten-stem phase table.',
 sourceEditionIndependenceEstablished=False))
state=read(b/'WORK_STATE.json');state.update(status='native8positions-read25manualslots24recognized1literal-unclassified-module-pending',actuallyViewedPositions=list(range(109,117)),chapterTargetSpan=[110,111,112,113,114,115],boundaryPositions=[109,116],manualStateSlots=25,recognizedStateSlots=24,unclassifiedLiteralSlots=1,
 nativeCropsViewedPixelMatched=6,next=['Four other body囚glyphs and title囚viewed as native controls; summer-water因has distinct interior cross stroke. Preserve anomaly, seek another edition only if needed; do not emend fromformula.',
 'Implement bounded source-phase/element lookup with one unknown glyph; explicit null for unknown/date-derived phase; full strength and fortune remain null.',
 'Separate sixth-month soil label and five seasonal states from十二寄生 and whole natal strength. Finish proper QA/report/package after useful bounded scope.'])
save('WORK_STATE.json',state)
print('Recorded8nativepositions/25slots/24recognized/1unclassifiedliteral;nosourceemendation')
