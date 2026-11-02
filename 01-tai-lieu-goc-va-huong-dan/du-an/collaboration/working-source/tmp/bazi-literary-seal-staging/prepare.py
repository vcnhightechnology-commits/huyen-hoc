from pathlib import Path
from hashlib import sha256
from datetime import datetime,timezone
import json
B=Path(__file__).resolve().parent;W=next(p for p in B.parents if(p/'v53/engine.js').is_file())
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def write(n,d):(B/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def ident(p):return {'file':p.relative_to(W).as_posix(),'bytes':p.stat().st_size,'sha256':sha256(p.read_bytes()).hexdigest()}
assert not(B/'FREEZE.json').exists()and not(B/'literary-seal.mjs').exists()
unit=next(r for r in read(W/'tmp/bazi-seal-conditions-staging/CHAPTER_UNITS.json')['units']if r['id']=='S04')
first=[('戊寅','癸未'),('辛巳','甲戌'),('庚申','乙丑'),('癸亥','丙辰'),('乙亥','壬辰')]
second=[('戊午','癸未'),('庚子','乙丑'),('丁酉','壬辰'),('己卯','甲戌'),('辛酉','丙辰')]
write('MANUAL.json',{'sourceID':'TMTH003-WenzhangYin-literal-pairs','chapterUnit':unit,'rows':[{'id':f'{group}{i+1}','group':group,'root':a,'target':b,'sourceConnective':'見'if group=='A'else'得','sourceMechanismPhrase':'乃納音尅身干神復制'if group=='A'else'干神制支神合之類'}for group,rows in [('A',first),('B',second)]for i,(a,b)in enumerate(rows)],
 'rootNatalRole':None,'twoMechanismPhrasesNotMerged':True,'sourceYiHaiRenChenPreserved':True,'groupBStemControlDirectionAdjudicated':False,'sourceEfficacyValidated':False})
expected={'戊寅':'城头土','癸未':'杨柳木','辛巳':'白蜡金','甲戌':'山头火','庚申':'石榴木','乙丑':'海中金','癸亥':'大海水','丙辰':'沙中土','乙亥':'山头火','壬辰':'长流水','戊午':'天上火','庚子':'壁上土','丁酉':'山下火','己卯':'城头土','辛酉':'石榴木'}
sources=[];nayin={};elements={}
for name,key,ny,el in [('bazi-branch-penalty','rows','actual',None),('bazi-branch-clash','rows','actual',None),('bazi-branch-harm','pillars','actualNaYin','actualStemElement'),('bazi-triad-stars','cases','actualNaYin','actualStemElement'),('bazi-true-ghost-context','naYin','actual',None)]:
 file=f'v53/research/{name}/ACTUAL_RUNTIME.json';sources.append(ident(W/file))
 for index,r in enumerate(read(W/file)[key]):
  nayin.setdefault(r['pillar'],{'actual':r[ny],'file':file,'array':key,'index':index,'field':ny})
  if el:elements.setdefault(r['pillar'][0],{'actual':r[el],'file':file,'array':key,'index':index,'field':el})
file='v53/research/bazi-food-chain/ACTUAL_RUNTIME.json';sources.append(ident(W/file))
for s,e in read(W/file)['stemElements'].items():elements.setdefault(s,{'actual':e,'file':file,'object':'stemElements','key':s})
stemexpected=dict(zip('甲乙丙丁戊己庚辛壬癸','木木火火土土金金水水'));stems=sorted({p[0]for p in expected})
reuseNY=[{'pillar':p,'expected':e,'retained':nayin[p]}for p,e in expected.items()if p in nayin]
missingNY=[{'pillar':p,'expected':e}for p,e in expected.items()if p not in nayin]
reuseEl=[{'stem':s,'expected':stemexpected[s],'retained':elements[s]}for s in stems if s in elements]
missingEl=[{'stem':s,'expected':stemexpected[s]}for s in stems if s not in elements]
for r in reuseNY+reuseEl:assert r['retained']['actual']==r['expected']
union='v53/research/bazi-branch-union/ACTUAL_RUNTIME.json';sources.append(ident(W/union))
write('PLAN.json',{'sources':sources,'reuseNaYin':reuseNY,'missingNaYin':missingNY,'reuseStemElements':reuseEl,'missingStemElements':missingEl,
 'reuseBranchPartners':read(W/union)['partners'],'branchPartnerPayload':union,'newBranchPartnerQueries':0,'actualNewCalendarObjects':0})
write('EXPECTED.json',{'nayin':expected,'groupATargetNaYinControlsRoot':[True]*5,'groupARootStemControlsTarget':[True,True,True,True,False],
 'groupBBranchSixUnion':[True]*5,'groupBRootStemControlsTarget':[True,True,False,False,False],
 'ordinaryComparisonIsEditorialNotSourceMeaning':True,'mismatchDoesNotAuthorizeGlyphEmendation':True})
write('IDENTITY_INPUTS.json',{'files':[ident(W/p)for p in ['v46/node_modules/lunar-typescript/dist/index.cjs','tmp/bazi-seal-conditions-staging/CHAPTER_UNITS.json','tmp/bazi-source-seal-staging/images/p089.png','tmp/bazi-source-seal-staging/images/p090.png']], 'twoFullNativeImagesActuallyViewedInPriorContinuation':True,'newImagesViewedThisRun':0})
write('FREEZE.json',{'atUTC':datetime.now(timezone.utc).isoformat(),'referenceAndRuntimeAbsent':True,'files':[ident(B/n)for n in ['MANUAL.json','PLAN.json','EXPECTED.json','IDENTITY_INPUTS.json']],
 'newNaYinQueriesPlanned':len(missingNY),'newStemElementQueriesPlanned':len(missingEl),'newCalendarObjectsPlanned':0})
print(json.dumps({'frozenFiles':4,'pairs':10,'reusedNaYin':len(reuseNY),'newNaYinPlanned':len(missingNY),'reusedStemElements':len(reuseEl),'newStemElementsPlanned':len(missingEl)}))
