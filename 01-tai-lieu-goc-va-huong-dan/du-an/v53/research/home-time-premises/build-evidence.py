from pathlib import Path
from html.parser import HTMLParser
from hashlib import sha256
from PIL import Image
import json,re
w=Path.cwd();b=w/'tmp/home-time-premises-staging'
def put(n,d):(b/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def ident(p):return {'file':p.relative_to(w).as_posix(),'bytes':p.stat().st_size,'sha256':sha256(p.read_bytes()).hexdigest()}
class Divs(HTMLParser):
 def __init__(self):super().__init__();self.active=None;self.depth=0;self.rows=[]
 def handle_starttag(self,t,a):
  a=dict(a)
  if self.active is not None:self.depth+=1
  elif t=='div'and any(c in a.get('class','').split()for c in ['xsl_para_tit','xsl_para']):self.active={'kind':'title'if 'xsl_para_tit'in a.get('class','')else'body','text':''};self.depth=1
 def handle_data(self,d):
  if self.active is not None:self.active['text']+=d
 def handle_endtag(self,t):
  if self.active is not None:
   self.depth-=1
   if self.depth==0:self.active['text']=' '.join(self.active['text'].split());self.rows.append(self.active);self.active=None
p=Divs();p.feed((b/'itkc-month-theory.html').read_text(encoding='utf-8'));records=[]
for x in p.rows:
 if x['kind']=='title':records.append({'id':f'MONTH-{len(records)+1:02d}','digitalHeading':x['text'].removeprefix('○ ').strip(),'digitalText':''})
 else:records[-1]['digitalText']+=x['text']
assert len(records)==19,len(records)
pages=[[241],[241],[241],[241,242],[242],[242,243],[243,244],[244],[244],[244],[244,245],[245],[245],[245],[245,246],[246],[246],[246,247],[247]]
notes=['Spatial repair only; age/outcome claim not implemented.','Small-versus-large repairs and special stars have unresolved context/join; no verdict.','Two alternatives for co-location involving 打頭火 or annualfire丙丁; no automatic activation.','Small/large repair and benefic-star condition; source effects unverified.','Explicit existing-repair/new-build distinction and no-jieqi source claim; two printed year/month/site examples.','Centre-only repair and star exception; no health/outcome or building action.','Historical music/ritual/burning/sacrifice passage retained for audit; excluded from product actions/remedies.','Direction-only建破魁罡 with conditionalstaroverride; not all日建破.','開山only; auspicious-month warning/outcomes not harmonized.','Direction-only; source outcome not established.','Facing/repair operation plus nooverride source claim; no physicalfireprediction.','Daily co-location required; no automatic fire/outcome.','Lists severalstars and at-least-one condition for repair; no inferreddate/directionpositions.','Monthly target plus repair only; no new-build/generaloutcomerule.','Januarydoor example and repair-only restriction; no all12monthlocations invented.','Januarystove example; 土公敗日 explicit exception preserved unknown until declared.','Repair-only and nojieqi source claim; 土公敗日動土 exception separate; attributed備要/一本 claim kept.','Nojieqi/monthclaim with animalpregnancylabels; not mappedto human natal/calendar predictions.','刀砧忌日並方 vs千斤方 only; differentdomains not merged.']
for i,x in enumerate(records):x.update({'sourcePositions':pages[i],'firstPassViewed':True,'allImageCharactersCollated':False,'disposition':notes[i],'wholeClauseApplied':False,'sourceOutcomeValidated':False,'consumerApplied':False})
put('CONTEXT_DISPOSITIONS.json',{'date':'2026-10-29','digitalFile':ident(b/'itkc-month-theory.html'),'sections':records,'sectionCount':19,'newSourceImages':8,'spanIncludesYearEndingAndDayOpening':True,'allImageCharactersCollated':False,'wholeMonthlyMethodApplied':False})
c=json.loads((b/'NATIVE_CROPS.json').read_text(encoding='utf-8'))
for x in c['records']:
 a=Image.open(w/x['source']['file']).crop(x['boxXYXY']).convert('RGB');d=Image.open(w/x['crop']['file']).convert('RGB');assert a.size==d.size and a.tobytes()==d.tobytes();x['viewed']=True;x['accepted']=True;x['scope']='Selected visible predicate only; overlapping crops/pages retain preceding/following clause.'
c['allFinalCropsViewed']=True;put('NATIVE_CROPS.json',c)
clauses=[{'id':'qiu-angdao','parent':'MONTH-05','title':'丘公暗刀殺','sourcePositions':[242],'selectedLiterals':['止忌修換','若鼎新造作則不避忌','又論其殺止論月分不問節氣'],'calendarClaim':'month-division-explicitly-not-jieqi-local-only','existingRepairOnly':True,'newBuildExplicitException':True,'hasTugongBaiDayException':False},
{'id':'monthly-hao','parent':'MONTH-15','title':'大小耗星','sourcePositions':[245,246],'selectedLiterals':['其殺止論月分','如正月在門戶只忌正月內修整門戶'],'calendarClaim':'month-division-stated;notexplicitno-jieqiinthisparagraph','existingRepairOnly':True,'newBuildExplicitException':False,'hasTugongBaiDayException':False},
{'id':'tugong','parent':'MONTH-16','title':'土公','sourcePositions':[246],'selectedLiterals':['其殺止論月分','如正月在竈正月之內只忌修整竈','如用土公敗日則不忌'],'calendarClaim':'month-division-stated;notexplicitno-jieqiinthisparagraph','existingRepairOnly':True,'newBuildExplicitException':False,'hasTugongBaiDayException':True},
{'id':'youlong-fulong','parent':'MONTH-17','title':'遊龍伏龍','sourcePositions':[246],'selectedLiterals':['各月所值之處止忌修換只論月分並不問節氣','如用土公敗日動土則不避忌'],'calendarClaim':'month-division-explicitly-not-jieqi-local-only','existingRepairOnly':True,'newBuildExplicitException':False,'hasTugongBaiDayException':True}]
put('MANUAL_CLAUSES.json',{'date':'2026-10-29','system':'ITKC-GO1508A.月論.local-repair-scope.v1','selectedPredicatesOnly':True,'sourceHeadingFollowsInstitutionTranscription':True,'calendarBoundaryTimestampResolved':False,'leapMonthTreatmentResolved':False,'sourceUsesNoJieqiForAllRules':False,'sourceMonthAutomaticallyEqualsNumericLunarMonth':False,'sourceEffectsValidated':False,'records':clauses})
examples=[{'id':'qiu-jiazi-month2','clause':'qiu-angdao','yearGanzhi':'甲子','monthOrdinal':2,'site':'pig-enclosure','literal':'甲子年二月在猪牢'},{'id':'qiu-jiazi-month3','clause':'qiu-angdao','yearGanzhi':'甲子','monthOrdinal':3,'site':'hall','literal':'甲子年三月占廳堂'},{'id':'hao-month1','clause':'monthly-hao','yearGanzhi':None,'monthOrdinal':1,'site':'doorway','literal':'如正月在門戶'},{'id':'tugong-month1','clause':'tugong','yearGanzhi':None,'monthOrdinal':1,'site':'stove','literal':'如正月在竈'}]
put('PRINTED_SITE_EXAMPLES.json',{'date':'2026-10-29','system':'ITKC-GO1508A.月論.four-printed-sites.v1','records':examples,'yearNullMeansSourceDidNotSpecifyYearNotAllYearsEstablished':True,'fullTwelveMonthTableDerived':False,'modernRoomGeometryMapped':False})
source=w/'v53/research/home-day-markers/ACTUAL_RUNTIME.json';prior=json.loads(source.read_text(encoding='utf-8-sig'));put('CACHED_CALENDAR_COUNTEREXAMPLES.json',{'date':'2026-10-29','source':ident(source),'records':prior['boundary'][:4],'newCalendarObjects':0,'newZhiXingCalls':0,'purpose':'Four retained actual lunar-typescript coordinate examples with differentnumericmonth/enginebranch. Reusedcacheonly;doesnotproveITKCmonthlyboundary.','originalBatchCountsNotAddedAgain':True})
put('SOURCE_IDENTITIES.json',{'date':'2026-10-29','institutionNode':'ITKC_GO_1508A_0020_000_0060','originalEditionNotEstablished':True,'sameInstitutionalWorkAsPreviousMonthWitness':True,'newInstitutionalWorks':0,'newP08IndependentEditions':0,'newSourceImagePositions':8,'newOriginalMasterContainers':0,'positions':list(range(240,248)),'retainedFiles':[ident(p)for p in [w/'v53/research/home-month-witness/itkc-imageviewer-root.html',w/'v53/research/home-month-witness/ACQUISITION_AND_LIMITS.json',source]],'sourceClaimsNotUserInstructions':True})
put('WORK_STATE.json',{'date':'2026-10-29','status':'19sectionsfirstpass/4selectedclausesread;compilerandtestsnext','catalogueID':'P08','relatedWork':'選擇要略','newSourceImages':8,'sectionDispositions':19,'selectedClausePredicates':4,'nativeCropsViewed':8,'cachedCalendarExamplesReused':4,'newActualHHCCharts':0,'newActualLunarObjects':0,'consumerChanged':False,'wholeSourceApplied':False})
print(json.dumps({'sectionDispositions':19,'selectedClauses':4,'printedSiteExamples':4,'cachedBoundaryExamples':4,'newCalendarObjects':0}))
