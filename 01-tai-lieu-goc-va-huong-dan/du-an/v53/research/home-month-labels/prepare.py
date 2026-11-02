from pathlib import Path
from hashlib import sha256
from PIL import Image,ImageChops
import json
s=Path(__file__).resolve().parent;w=s.parent.parent
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
save=lambda n,d:(s/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
h=lambda p:sha256(p.read_bytes()).hexdigest()
assert not(s/'label-reference.mjs').exists()
# Manual image readings, columns from right (甲子) to left (癸酉).
# X remains unread; no presumed lemma for the disputed small glyph.
rows=['T X J D X T R X P T',
      'X D X J S R Q X T P',
      'R Q X T J X D X X X',
      'R D X T X J D X Q R',
      'P X T Q D R J T D X',
      'T P R X X X S J X D',
      'D S P R X Q T X J D',
      'Q R T P D R X S T J',
      'R X S T P X D Q X X',
      'D X Q R X P T X X D',
      'J R X X T D P R T Q',
      'T J X X Q X D P X Q']
days=['甲子','乙丑','丙寅','丁卯','戊辰','己巳','庚午','辛未','壬申','癸酉']
labels={'T':'天和','D':'地和','R':'人和','Q':'河魁','S':'受死','J':'建','P':'破','X':None}
old=read(w/'v53/research/home-day-markers/MANUAL_BUILD_BREAK_MARKERS.json')
records=[]
for month,text in enumerate(rows,1):
 cells=text.split();assert len(cells)==10
 for col,(day,code)in enumerate(zip(days,cells),1):
  original=next(r for r in old['records']if r['sourceMonth']==month and r['dayGanzhi']==day)
  assert original['selectedMarker']==({'J':'建','P':'破'}.get(code)),(month,day,code)
  records.append({'sourceMonth':month,'dayGanzhi':day,'sourceColumnFromRight':col,'sourcePage':131,'panel':'left','editorialCode':code,'workingLiteralLabel':labels[code],
    'readingStatus':'unresolved-glyph'if code=='X'else'selected-complete-cell-label-read',
    'sourceMonthBoundaryEstablished':False,'readingIsDiplomaticCollation':False})
source=w/'v53/research/home-yangzhai-final-spans/selection/raw-p131.jpg';crop=s/'first-ten-full-margins.png';box=[0,815,1220,1890]
im=Image.open(source).convert('RGB');derived=Image.open(crop).convert('RGB');assert ImageChops.difference(im.crop(box),derived).getbbox()is None
manual={'date':'2026-10-29','system':'P08-month-cell-labels-selected-甲子癸酉','entryMethod':'Manual reading of retained native grid; no formula or OCR cell completion. X is unresolved, not blank.','days':days,'sourceMonths':list(range(1,13)),'rowsByMonthColumnsRightToLeft':rows,'codeLegend':labels,'records':records,'remainingOtherDayColumns':50,'full720CellLabelsTranscribed':False,'unresolvedGlyphAliasAccepted':False,'consumerChanged':False}
save('MANUAL_CELLS.json',manual)
save('SOURCE_IDENTITIES.json',{'date':'2026-10-29','source':{'file':source.relative_to(w).as_posix(),'bytes':source.stat().st_size,'sha256':h(source)},'crop':{'file':crop.name,'boxXYXY':box,'bytes':crop.stat().st_size,'sha256':h(crop),'actuallyViewed':True,'RGBMatchesSource':True},'priorMarkerTable':{'file':'v53/research/home-day-markers/MANUAL_BUILD_BREAK_MARKERS.json','bytes':(w/'v53/research/home-day-markers/MANUAL_BUILD_BREAK_MARKERS.json').stat().st_size,'sha256':h(w/'v53/research/home-day-markers/MANUAL_BUILD_BREAK_MARKERS.json')},'unknownGlyphPriorAudit':'v53/research/home-day-markers/PRIVATE_GLYPH_READING_CORRECTION.json','newHTTPBodies':0,'newSourcePositions':0})
from collections import Counter
counts=Counter(r['editorialCode']for r in records)
save('EXPECTED_BEFORE_IMPLEMENTATION.json',{'date':'2026-10-29','sourceCoordinateCount':120,'readableCellCount':120-counts['X'],'unresolvedCellCount':counts['X'],'codeCounts':dict(counts),'fixedCases':[{'month':1,'day':'甲子','expected':'天和'},{'month':1,'day':'乙丑','expected':None},{'month':2,'day':'戊辰','expected':'受死'},{'month':2,'day':'庚午','expected':'河魁'},{'month':11,'day':'甲子','expected':'建'}],'other600CellsUnknown':True,'wholeCalendarRecommendationAlwaysNull':True,'newEngineCallsExpected':0})
files=[]
for n in ['MANUAL_CELLS.json','SOURCE_IDENTITIES.json','EXPECTED_BEFORE_IMPLEMENTATION.json']:
 p=s/n;files.append({'file':n,'bytes':p.stat().st_size,'sha256':h(p)})
save('PREIMPLEMENTATION_FREEZE.json',{'date':'2026-10-29','implementationExists':False,'files':files})
print(json.dumps({'manuallyInspectedCells':120,'readableCells':120-counts['X'],'unresolvedCells':counts['X'],'codeCounts':dict(counts)},ensure_ascii=False))
