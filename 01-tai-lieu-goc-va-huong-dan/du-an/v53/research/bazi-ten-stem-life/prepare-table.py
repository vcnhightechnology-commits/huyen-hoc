from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone,timedelta
import json
s=Path(__file__).resolve().parent;w=s.parent.parent
save=lambda n,d:(s/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
h=lambda p:sha256(p.read_bytes()).hexdigest()
assert not(s/'coordinate-reference.mjs').exists()
stems=list('甲乙丙丁戊己庚辛壬癸');birth=list('亥午寅酉寅酉巳子申卯');death=list('午亥酉寅酉寅子巳卯申')
pages=[[10,11],[12,13],[14],[16],[18],[20],[21],[23],[25],[27]]
rows=[{'stem':a,'sourceBirthBranch':b,'sourceDeathBranch':d,'sourcePages':p,'voice':'initial-ten-stem-exposition','diplomaticGlyphCollationComplete':False}for a,b,d,p in zip(stems,birth,death,pages)]
manual={'date':'2026-10-29','system':'TMTH002-initial-ten-stem-birth-death','scope':'Only explicitly named birth/death coordinates, not all twelve stages or every voice in chapter.','rows':rows,'workingReadingNotes':['己/已-like glyphs in branch positions of 庚/辛 are recorded as working 巳 by the named-branch context; raw PNG and digital bytes unchanged.','邜/卯 retained source shape versus working branch 卯; no automatic global text replacement.','Death/live wood metaphors in paragraphs are not automatically the twelve-phase 死/長生 labels.'],'parallelVoices':[{'pages':[29],'voice':'論曰','note':'Supports 戊生寅/己生酉 and criticizes an alternative 戊生申/己生卯.'},{'pages':[30,31],'voice':'或曰 and reported systems','note':'Earth body/use and 寅/申/巳 alternatives; not adopted as additional starts in the initial table.'},{'pages':[34,35],'voice':'reported one-wood argument and subsequent conclusion','note':'Same生死 argument for paired stems appears before authorial 前説 conclusion; unresolved reference scope not silently equated to the initial table.'}],'fullChapterRead':False,'fullTwelveStageMatrixEstablished':False,'sourceEffectivenessValidated':False,'consumerChanged':False}
save('MANUAL_COORDINATES.json',manual)
save('EXPECTED_BEFORE_IMPLEMENTATION.json',{'beforeImplementation':True,'pairs':[{'stem':r['stem'],'branch':r[k],'expectedSourceMarker':label,'expectedLunarLabel':label}for r in rows for k,label in [('sourceBirthBranch','长生'),('sourceDeathBranch','死')]],'unlistedCoordinatesExpected':100,'sourceCoordinateCount':20,'actualNatalChartsExpected':0})
renders=json.loads((s/'CLAUSE_RENDERS.json').read_text(encoding='utf-8'))
for r in renders['records']:r['actuallyViewed']=True;r['readingScope']='Selected clauses/parallel voices; not every glyph of chapter.'
save('CLAUSE_RENDERS.json',renders)
freeze=[]
for n in ['MANUAL_COORDINATES.json','EXPECTED_BEFORE_IMPLEMENTATION.json','CLAUSE_RENDERS.json']:
 p=s/n;freeze.append({'file':n,'bytes':p.stat().st_size,'sha256':h(p)})
save('PREIMPLEMENTATION_FREEZE.json',{'frozenAt':datetime.now(timezone(timedelta(hours=7))).isoformat(),'implementationExists':False,'runtimeExists':False,'files':freeze})
print('Frozen10source-rows/20coordinates;runtime-not-executed.')
