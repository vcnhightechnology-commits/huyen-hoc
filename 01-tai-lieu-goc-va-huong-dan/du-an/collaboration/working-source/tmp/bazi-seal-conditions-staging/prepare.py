from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json,re
B=Path(__file__).resolve().parent;W=next(p for p in B.parents if(p/'v53/engine.js').is_file())
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def write(n,d):(B/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def ident(p):return {'file':p.relative_to(W).as_posix(),'bytes':p.stat().st_size,'sha256':sha256(p.read_bytes()).hexdigest()}
assert not(B/'FREEZE.json').exists()and not(B/'fuju-reference.mjs').exists()
p=W/'v53/research/bazi-relations/sources/KR3g0042_003.txt';raw=p.read_text(encoding='utf-8');a=raw.index('　　論正印');b=raw.index('　　論徳秀',a);text=raw[a:b]
(B/'CHAPTER_EXCERPT.txt').write_text(text,encoding='utf-8')
clean=re.sub(r'<pb:[^>]+>|[\s¶]','',text)
starts=['論正印','有貴人夾印','有華蓋印','有文章印','諸印要逢庫墓','有年時見印','又有福聚印','有禍聚印','有破福成禍印','有帶煞印','有臨空印','有自刑印','凡論印']
indices=[clean.index(s)for s in starts];assert indices==sorted(indices)
units=[]
for i,start in enumerate(indices):
 end=indices[i+1]if i+1<len(indices)else len(clean);units.append({'id':f'S{i+1:02}','opening':starts[i],'start':start,'end':end,'text':clean[start:end],'wholeUnitApplied':False})
assert ''.join(r['text']for r in units)==clean
write('CHAPTER_UNITS.json',{'source':ident(p),'digitalStartFolio':'003-43b','digitalEndFolio':'003-46a','nextHeadingExcluded':'論徳秀','cleanCodepoints':len(clean),'cleaningPolicy':'Remove only pb markers, whitespace and paragraph markers; no glyph emendation.','units':units,'wholeChapterApplied':False})
write('MANUAL_FUJU.json',{'sourceID':'TMTH003-FujuYin-selected','literal':units[6]['text'],
 'fiveSourcePositions':['year','month','day','hour','fetal'],'allFiveRequired':True,
 'weakPremiseLiteral':'五位俱無氣衰敗','sameSealLiteral':'得正印偏印俱在此印上','storageStrongLiteral':'或庫或旺','restraintLiteral':'雖有煞神至是受制',
 'selectedLogic':'All five declared無氣衰敗 AND declared正印atthisseal AND declared偏印atthisseal AND (declared庫 OR declared旺). If煞神到is declared, require its declaredeffective制atthisseal.',
 'logicStatus':'Explicit conservative source-premise composition; subject/frame definitions and actual efficacy remain open.',
 'noShaBranchMeansNoRestraintRequiredByThisClause':True,'neitherSealEqualsOrdinaryTenGodAutomatically':True,
 'missingFetalCannotBeAssumedWeak':True,'sourceOutcomeValidated':False,'wholeContextApplied':False})
cases=[('all-weak-no-sha',[True]*5,True,True,True,None,False,None,True),
 ('missing-fetal',[True]*4+[None],True,True,True,False,False,None,None),
 ('one-not-weak',[True,False,True,True,True],True,True,True,True,False,None,False),
 ('no-storage-but-strong',[True]*5,True,True,False,True,False,None,True),
 ('neither-storage-nor-strong',[True]*5,True,True,False,False,False,None,False),
 ('sha-with-control',[True]*5,True,True,True,False,True,True,True),
 ('sha-control-missing',[True]*5,True,True,True,False,True,None,None),
 ('sha-uncontrolled',[True]*5,True,True,True,False,True,False,False),
 ('sha-unknown-control-present',[True]*5,True,True,True,False,None,True,True),
 ('sha-unknown-control-missing',[True]*5,True,True,True,False,None,None,None),
 ('pianyin-missing',[True]*5,True,None,True,True,False,None,None)]
write('EXPECTED.json',{'cases':[dict(zip(['id','weak','zhengAtSeal','pianAtSeal','storage','strong','shaArrives','shaControlled','match'],r))for r in cases], 'referenceFrame':'five-source-positions-and-same-seal-declarations'})
images=[]
for n,folio in [(88,'43b'),(89,'44a'),(90,'44b'),(91,'45a'),(92,'45b'),(93,'46a')]:
 images.append({**ident(W/f'tmp/bazi-source-seal-staging/images/p{n:03}.png'),'containerPosition':n,'folio':folio,'actuallyViewed':True})
write('SOURCE_IDENTITIES.json',{'files':[ident(p),ident(W/'v53/research/bazi-jianlu-context/volume3/CADAL06066039.djvu'),ident(W/'v53/research/bazi-pattern-extension/tooling/djvu.js'),ident(B/'CHAPTER_EXCERPT.txt')],
 'images':images,'readLevel':'Targeted full chapter span viewed; selected clauses, not diplomatic all-glyph collation.','globalNewViewedPositionCount':None,
 'newSourceImagesThisContinuation':3,'newHTTPBodies':0,'newOriginalContainers':0,'newIndependentEditions':0,'newEngineCalls':0})
write('FREEZE.json',{'atUTC':datetime.now(timezone.utc).isoformat(),'referenceAbsent':True,'files':[ident(B/n)for n in ['CHAPTER_UNITS.json','MANUAL_FUJU.json','EXPECTED.json','SOURCE_IDENTITIES.json']], 'manualCases':11,'newEngineCallsPlanned':0})
print(json.dumps({'frozenFiles':4,'chapterUnits':13,'cleanCodepoints':len(clean),'manualCases':11,'newEngineCalls':0}))
