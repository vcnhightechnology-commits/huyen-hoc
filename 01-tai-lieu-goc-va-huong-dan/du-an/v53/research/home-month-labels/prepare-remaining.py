from pathlib import Path
from hashlib import sha256
from collections import Counter
import json
s=Path(__file__).resolve().parent;w=s.parent.parent
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
old=read(w/'v53/research/home-day-markers/MANUAL_BUILD_BREAK_MARKERS.json')
legend={**read(s/'MANUAL_CELLS.json')['codeLegend'],'M':'墓','F':'四廢'}
rows=[
['P D S Q R X J T X X','R P T D X R X J S T','X X P S R Q D T J X','Q T M P D X X R X J','R X M T P X D Q R T','X T Q X D P T X X X','J R X X T S P D X Q','D J R T Q D R P T D','X X J T R X S T P X','X R X J T X Q D M P','X Q R T J X D X M R','R S X D R J X X Q X'],
['D M P R S Q T X J X','Q M D P R T X D X J','D X X X P S R Q X T','T X Q D X P R X X T','J D R X T D P X R X','S J X R Q D T P X X','R X J T X X D S P R','X S R J T D Q M R P','D Q X X J X R X S T','X X X T R J D X Q R','P T D Q R T J X R X','X X X S X R S J X X'],
['X X R D P T S Q D X','S R Q X T P D R X T','J T D X D X P S R Q','X J D X Q R X P F X','T D J R T X D R P X','X X S J R D Q X R P','X Q T X J D X X R S','T D X S R J T D Q D','P X D Q X X J X R X','D P F X X T X J D X','T D P R T Q D R J X','Q X F P X S X D R J'],
['J T X X T X P F S Q','T J S D Q X F P T D','X T J X D X F F P S','X T X J D X Q R X P','T Q D R J T D X R F','X X X X S J X T Q F','P F X Q T X J D X X','X P T D X S R J T D','S F P X T Q X X J X','Q R X P T X X D X J','T X D F P R T T D R','R X Q F T P X S X X']]
blocks=[];errors=[]
for block_index,grid in enumerate(rows,2):
 original=old['blocks'][block_index];days=[original['days'][i:i+2]for i in range(0,20,2)];records=[]
 for month,line in enumerate(grid,1):
  for col,(day,code)in enumerate(zip(days,line.split(),strict=True),1):
   previous=next(x for x in old['records']if x['sourceMonth']==month and x['dayGanzhi']==day)
   if code!='X'and previous['selectedMarker']!={'J':'建','P':'破'}.get(code):errors.append({'block':block_index+1,'month':month,'day':day,'column':col,'manualCode':code,'priorMarker':previous['selectedMarker']})
   records.append({'sourceMonth':month,'dayGanzhi':day,'sourceColumnFromRight':col,'sourcePage':original['page'],'panel':original['panel'],'editorialCode':code,'workingLiteralLabel':legend[code],'readingStatus':'unresolved-glyph'if code=='X'else'selected-complete-cell-label-read','evidenceCrop':original['file'],'priorSelectedMarker':previous['selectedMarker'],'sourceMonthBoundaryEstablished':False,'readingIsDiplomaticCollation':False})
 counts=Counter(x['editorialCode']for x in records)
 p=(s/'sixth-ten-complete.png')if block_index==5 else w/'v53/research/home-day-markers'/original['file']
 blocks.append({'block':block_index+1,'days':days,'rowsByMonthColumnsRightToLeft':grid,'sourceImage':p.relative_to(w).as_posix(),'sourceImageSHA256':sha256(p.read_bytes()).hexdigest(),'records':records,'codeCounts':dict(counts),'readableCells':120-counts['X'],'unresolvedCells':counts['X']})
draft={'date':'2026-10-29','entryMethod':'Manual native-image readings; X means unread, not blank. No formula fills.','codeLegend':legend,'blocks':blocks,'priorMarkerDiscrepancies':errors,'newHTTPBodies':0,'newSourcePositions':0,'newEngineCalls':0}
(s/'REMAINING_BLOCKS_DRAFT.json').write_text(json.dumps(draft,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'blocks':4,'manualCells':480,'markerDiscrepancies':errors},ensure_ascii=False))
if errors:raise SystemExit(2)
