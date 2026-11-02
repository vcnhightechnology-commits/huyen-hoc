from pathlib import Path
from hashlib import sha256
import json
from PIL import Image,ImageChops
b=Path(__file__).resolve().parent;w=b.parents[1]
save=lambda name,o:(b/name).write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
branches=list('寅卯辰巳午未申酉戌亥子丑')
prose=['艮土:5 丙:5 甲:20','甲:7 乙:23','乙:7 壬:5 戊:18','戊:7 庚:5 丙:18','丙:7 丁:23','丁:7 甲:5 己:18','坤土:5 壬:5 庚:20','庚:7 辛:23','辛:7 丙:5 戊:18','戊:5 甲:5 壬:20','壬:7 癸:23','癸:7 庚:5 己:18']
yujing=['己:7 丙:5 甲:18','乙:18 甲:9 癸:3','戊:18 乙:9 癸:3','丙:18 戊:7 庚:5','丁:18 丙:9 乙:3','己:18 乙:5 丁:7','庚:17 己:7 戊:3 壬:3','辛:20 庚:7 丁:5','戊:18 辛:7 丁:5','壬:18 甲:5 戊:7','癸:18 壬:5 辛:3','己:18 癸:7 辛:5']
rows=[]
for variant,items in [('chapter-prose',prose),('cited-Yujing-table',yujing)]:
 for i,(branch,text)in enumerate(zip(branches,items)):
  cells=[]
  for entry in text.split():
   label,n=entry.split(':');cells.append(dict(sourceLabel=label,canonicalStem=label if label in list('甲乙丙丁戊己庚辛壬癸')else None,days=int(n)))
  pages=([67]if i<4 else[68]if i<11 else[69])if variant=='chapter-prose'else([69]if i<3 else[70]if i<11 else[71])
  rows.append(dict(variant=variant,sourceMonthOrdinal=i+1,monthBranch=branch,entries=cells,arithmeticDayTotal=sum(c['days']for c in cells),sourceContainerPages=pages,
   printedOrderNotAutomaticallyChronological=True,dayOffsetAdapterEstablished=False))
assert len(rows)==24 and sum(len(x['entries'])for x in rows)==69
save('MANUAL_COMMAND_TABLES.json',dict(date='2026-10-28',method='Manual two literal variant lists before runtime comparison; canonical己reading declared for earth-stem positions, retaining 艮土/坤土 as labels with no assumed stem.',
 records=rows,sourceRows=24,allocationEntries=69,canonicalization='己/巳/已 shaped earth-stem tokens read canonically己 from stem role; literal repository bytes untouched, not full diplomatic glyph transcription.',
 sourceCalendarPhaseOrOffsetAdjudicated=False,sourceVariantsMerged=False,fullStrengthEstablished=False))
save('ARITHMETIC_AUDIT.json',dict(date='2026-10-28',proseRowsTotalDays=sum(x['arithmeticDayTotal']for x in rows if x['variant']=='chapter-prose'),
 yujingRowsTotalDays=sum(x['arithmeticDayTotal']for x in rows if x['variant']=='cited-Yujing-table'),
 yujingNonThirtyRows=[dict(monthBranch=x['monthBranch'],days=x['arithmeticDayTotal'])for x in rows if x['variant']=='cited-Yujing-table'and x['arithmeticDayTotal']!=30],
 source69AnnualCountIntro=dict(literalEachYangStemDays=35,literalEachYinStemDays=35,literalEachEarthStemDays=50,printedClaimedTotal=360,computedTotal=380,unresolved=True),
 notCorrectedToConventionalTotals=True,oneRepositoryEditionNotIndependentAuthoritativeProof=True))
specs=[(69,'p69-annual-numbers-native.png',[900,600,1430,2450]),(70,'p70-you-days-native.png',[930,1000,1210,2690]),(70,'p70-zi-days-native.png',[310,900,590,2650]),(71,'p71-season-earth-native.png',[1260,300,2090,2640]),(72,'p72-critique-native.png',[300,300,2100,2850])]
qa=[]
for p,name,box in specs:
 src=b/f'p{p}.png';out=b/name;Image.open(src).crop(box).save(out)
 qa.append(dict(sourceFile=src.name,file=name,sourceContainerPage=p,cropBox=box,sha256=sha256(out.read_bytes()).hexdigest(),resampled=False,actuallyViewed=False))
save('QA_IMAGES.json',dict(date='2026-10-28',records=qa))
render=json.loads((b/'LOCAL_RENDERS.json').read_text(encoding='utf-8'))
for x in render['records']:
 x['actuallyViewed']=True;x['scope']='Source month-command chapter/boundary first-pass expansion; not entire volume or all glyph collation.'
save('LOCAL_RENDERS.json',render)
save('WORK_STATE.json',dict(date='2026-10-28',catalogueID='M01',status='two-source-command-tables24rows69entries-awaiting-crop-QA-runtime',sourceDirectory='tmp/bazi-month-command-staging',
 sourceContainer='v53/research/bazi-season-strength/CADAL06066038.djvu',sourceContainerSHA256='7a53f35982f0b946281d0e393c5d6ddcce1fd091aea83c11af6a06bcdfe6a85e',
 positionsViewed=list(range(65,73)),newContainerPositionsViewed=8,newHTTPRequests=0,newRepositoryContainers=0,consumerChanged=False,wholeCatalogueCompleted=False,
 next=['View arithmetic/critique crops; do not repair totals or silently merge tables.','Implement named literal table lookup, not day-offset/weight/dominant-stem engine; compare fixed hidden-stem sets as a distinct system.']))
print('Manual24rows/69entries;prose360/Yujing358;32and26dayrows/380vs360introretained')
