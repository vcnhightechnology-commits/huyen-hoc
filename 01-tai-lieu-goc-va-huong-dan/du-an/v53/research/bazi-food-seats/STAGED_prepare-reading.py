from pathlib import Path
from hashlib import sha256
from PIL import Image
import json
b=Path(__file__).resolve().parent;w=b.parents[1];rows=[]
for page,name,box in [(177,'p177-seat-clause-start-native.png',[350,250,650,2870]),(178,'p178-seat-clause-native.png',[1300,250,2100,2860])]:
 src=w/f'v53/research/bazi-food-source/p{page}.png';out=b/name;Image.open(src).crop(box).save(out)
 rows.append(dict(sourceContainerPage=page,sourceFile=src.relative_to(w).as_posix(),sourceSHA256=sha256(src.read_bytes()).hexdigest(),file=name,cropBox=box,sha256=sha256(out.read_bytes()).hexdigest(),resampled=False,actuallyViewed=False))
(b/'QA_IMAGES.json').write_text(json.dumps(dict(date='2026-10-28',records=rows),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
manual=[dict(dayStems=list('甲乙'),foodStems=list('丙丁'),branches=list('寅卯巳午')),dict(dayStems=list('丙丁'),foodStems=list('戊己'),branches=list('辰戌丑未')),dict(dayStems=list('戊己'),foodStems=list('庚辛'),branches=list('巳午申酉')),dict(dayStems=list('庚辛'),foodStems=list('壬癸'),branches=list('申酉亥子')),dict(dayStems=list('壬癸'),foodStems=list('甲乙'),branches=list('亥子寅卯'))]
(b/'MANUAL_SEAT_CLAUSE.json').write_text(json.dumps(dict(date='2026-10-28',contextID='FOOD-00-C20',sourceContainerPages=[177,178],digitalFolios=['005-88a','005-88b'],records=manual,manualGroupRows=5,directListedBranchMemberships=20,
 correspondenceWithinEachStemPair='Day-food stem correspondence requires fixed 食神 relation from chapter context, not both food stems for each day.',
 codepointCollationComplete=False,sourceChapterFullStrengthDefinition=False,sourceOutcomeValidated=False,consumerApplied=False),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(b/'WORK_STATE.json').write_text(json.dumps(dict(date='2026-10-28',status='C20five-source-seat-groups-draft-awaiting-header-aligned-native-QA',sourceDirectory='tmp/bazi-food-seats-staging',newHTTPRequests=0,newSourcePositions=0,consumerChanged=False,wholeCatalogueCompleted=False,next=['View native clause crops, confirm five groups and 己/巳 source glyphs before module tests.','Keep source 食神見生旺 distinct from full strength or prediction; enforce actual fixed food relation and valid pillar parity.']),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('PreparedC20fivegroupdraftand2nativecrops;notyetverified')
