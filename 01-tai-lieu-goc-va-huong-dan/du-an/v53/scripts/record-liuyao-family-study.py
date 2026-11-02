from pathlib import Path
from hashlib import sha256
import json,shutil
from PIL import Image

r=Path(__file__).resolve().parent.parent;w=r.parent;b=r/'research/liuyao-family-study';q=r/'qa/liuyao-family-study';s=w/'tmp/liuyao-b02-family-staging'
assert not b.exists()and not q.exists(),'One-shot promotion; preserve prior source records'
b.mkdir();(b/'images').mkdir();q.mkdir()
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
write=lambda p,d:p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
sha=lambda p:sha256(p.read_bytes()).hexdigest()
pdf=r/'research/liuyao-foundations/NLC416-12jh005345-45344.pdf'
assert pdf.stat().st_size==11089308 and sha(pdf)=='caac111bc5c5b1c08fd27b3828e7cf6b5430503800f2427d8f2b28809022abaa'
notes={
232:'Reread chapter39 opening; chapter38 ending remains separate. Self is source root; no lifespan or clinical computation.',
233:'Chapter39 critiques five-years-per-line age arithmetic, reports forty years without confirmation and contrasts another twenty-year prediction. Source anecdotes are not validation.',
234:'Source says longevity focus differs from ordinary moving-generator preference. Calendar, strength, activity and outcome premises are not supplied by role presence.',
235:'Chapter39 ends; body heading 趨避章第四十 opens. Water danger narrative historical; no physical safety or death inference.',
236:'Avoidance chapter crossing/boat narrative and element/spirit hazard correspondences. Historical claims, not real-world safety instructions.',
237:'Dream narrative and moving money/wood harm roles; moral/social stereotypes not runtime classifications.',
238:'List of hazard questions and 子孫 preference. Death/disease and dream examples not factual outcome validation.',
239:'Source qualifies 子孫 presence by month-break/void and internal/external location; geometric presence alone is insufficient.',
240:'Internal/external avoidance and servant narrative. Historical servitude/moral judgments excluded from consumer interpretation.',
241:'Avoidance direction/self-generating element and 子孫 claims; military/disease cases historical only.',
242:'Source disputes automatic metal-to-fire opposition in an anecdote; uses question and actor context, not one unconditional element rule.',
243:'Element/spirit disease/death claims historical only; convicted-person narrative not a legal or health classifier.',
244:'父母壽元章第四十一 opens; explicitly asks father and mother separately. Quoted yin/yang method retained as a source voice, not automatic parent assignment.',
245:'Author criticizes indiscriminate same-cast parent interpretation using comparison cases; outcomes remain unvalidated.',
246:'Chapter41 ends with attempted rescue anecdote; no modern medical advice extracted. 兄弟章第四十二 opens.',
247:'Sibling questions explicitly distinguish harmony, support, future siblings and longevity. One kin role does not settle all questions.',
248:'Sibling counterexample and latent family narrative; 夫婦章第四十三 opens. Do not infer private family relations from a cast.',
249:'Spouse scope must distinguish longevity, growing old, harmony and affliction. Wife 財 takes precedence over 應 in this named passage; competing 黃金策 voice retained.',
250:'Wife and harmony narrative; no automatic marital breakdown or moral classification.',
251:'Multiple 財 roles, original/changed wife claims and location distinctions; no single use-line selected or family status inferred.',
252:'Chapter43 ends; 子嗣章第四十四 opens with future/additional/current-child question distinctions.',
253:'Offspring assertions distinguish presence/change/strength but outcomes and child counts unvalidated. Contemporary fertility diagnosis not extracted.',
254:'Original/changed descendant roles, age and adoption claims remain historical; no adoption, paternity or family relationship inference.',
255:'Author distinguishes upbringing from rank and critiques blanket honorific 吉神 claims. Historical child-death cases not consumer forecasts.',
256:'Author disputes predicting an infant future rank from a parent cast; general kin questions first inspect self, without manufacturing unasked outcomes.',
257:'Kin-question spillover discussion ends; 學業章第四十五 opens. Literary learning uses 父母 and 官, source traditions not modern exam probabilities.',
258:'Artisan 財/子孫 differs from literary learning. 治經章第四十六 opens with five named classics/elements and explicit single-classic question requirement.',
259:'Study-classic printed 益→觀 fixture: first moving 子父→未財. Further casts/claims retained separately, no source chronology or grades inferred.',
260:'Chapter46 ends; 延師章第四十七 opens. 父母 means teacher and books here, so symbolic kin is not automatically biological family.',
261:'Teacher chapter conditions, authority/fees/classroom relations and source self/response meanings. No automatic teacher-quality evaluation.',
262:'Teacher chapter ends; 求名章第四十八 stresses separate county/prefecture/circuit exam scopes. 童試章第四十九 opens.',
263:'Chapter49 ends; 歲科考章第五十 only opening read. Exam outcomes historical; not success or admissions predictions.'}
records=[]
for page in [15,*range(232,264)]:
 if page==15:
  dest=q/'toc-015.png';shutil.copyfile(s/'toc-015.png',dest);dpi=240
  note='Targeted reread of retained TOC15 at240dpi. Printed 趨避 agrees with body235; working normalized 超遷 is a transcription error, not a source variant.'
 elif page==232:dest=r/'research/liuyao-life-context/images/zengshan-232.png';dpi=144;note=notes[page]
 else:dest=b/'images'/f'zengshan-{page}.png';shutil.copyfile(s/dest.name,dest);dpi=144;note=notes[page]
 records.append({'pdfPage':page,'file':dest.relative_to(w).as_posix(),'sha256':sha(dest),'size':list(Image.open(dest).size),'dpi':dpi,'actuallyViewed':True,
  'newReadPositionThisScope':page>=233,'expandedPriorRead':page in[15,232],'allCharactersTranscribed':False,'note':note})
shutil.copyfile(s/'qa360-259.png',q/'qa360-259.png')
ranges={39:[232,235],40:[235,244],41:[244,246],42:[246,248],43:[248,252],44:[252,257],45:[257,258],46:[258,260],47:[260,262],48:[262,262],49:[262,263]}
manual={'date':'2026-10-28','sourcePDF':pdf.relative_to(w).as_posix(),'sourceSHA256':sha(pdf),'records':records,
 'chapterRanges':{str(k):{'pages':v,'wholeFirstPassRead':True,'wholeApplied':False}for k,v in ranges.items()},
 'chapter50':{'pages':[263],'wholeFirstPassRead':False,'wholeApplied':False},
 'counts':{'sourcePositionsRead':33,'newSourceReadPositions':31,'expandedPriorReadPositions':2,'newNativeContentRenders':31,'newHighResolutionQARenders':2,'newHTTPRequests':0,'newOriginalContainers':0},
 'allSubsidiaryClausesEnumerated':False,'sourceOutcomesValidated':False,'wholeCatalogueCompleted':False}
write(b/'MANUAL_READINGS.json',manual)
write(b/'SOURCE_MANIFEST.json',{'date':'2026-10-28','sourcePDF':manual['sourcePDF'],'sourceBytes':pdf.stat().st_size,'sourceSHA256':sha(pdf),
 'sourceProvenance':'Inherited original byte/TLS/provenance records in liuyao-foundations; no new HTTP request. New PNG renders are derived from that exact PDF, not newly downloaded source witnesses.',
 'images':records,'extraQA':[{'file':(q/'qa360-259.png').relative_to(w).as_posix(),'sha256':sha(q/'qa360-259.png'),'sourcePage':259,'dpi':360,'actuallyViewed':True,'newSourcePosition':False}],
 'newHTTPRequests':0,'newOriginalContainers':0,'independentNewWitnesses':0,'sourceInstructionsAreData':True})
methods=[
 {'id':'b02-ch041-parent','pages':[244,245],'subjects':['father','mother'],'questions':['longevity'],'roles':[('parent','父母')],'sourceVoice':'chapter41 author; quoted yin/yang convention not automatically applied'},
 {'id':'b02-ch042-sibling','pages':[247,248],'subjects':['sibling'],'questions':['harmony','support','future-sibling','longevity'],'roles':[('sibling','兄弟')],'sourceVoice':'chapter42 explicit question distinction'},
 {'id':'b02-ch043-spouse','pages':[249,250,251],'subjects':['wife','husband'],'questions':['longevity','grow-old','harmony','affliction'],'roles':[('wife','妻財')],'unextractedSubjects':['husband'],'sourceVoice':'chapter43 author separates 財 from competing 應-wife convention; husband role not directly extracted in this bounded span'},
 {'id':'b02-ch044-offspring','pages':[252,255,256],'subjects':['offspring'],'questions':['current-child','additional-child','future-child','upbringing','rank'],'roles':[('descendant','子孫')],'sourceVoice':'chapter44 distinguishes existence/upbringing/rank and warns against retrospective/infant rank inference'},
 {'id':'b02-ch045-literary','pages':[257],'subjects':['self'],'questions':['literary-study'],'roles':[('writing','父母'),('office','官鬼')],'sourceVoice':'chapter45 儒學 opening; not a universal meaning for 父母'},
 {'id':'b02-ch045-artisan','pages':[258],'subjects':['self'],'questions':['artisan-study'],'roles':[('source-use-role','妻財'),('source-generator-role','子孫')],'sourceVoice':'chapter45 百工 paragraph; named source-use kin group does not select a line or prove efficacy'},
 {'id':'b02-ch046-classic','pages':[258,259,260],'subjects':['self'],'questions':['specified-classic'],'roles':[('writing','父母'),('office','官鬼')],'sourceVoice':'chapter46 author requires specifying one classic; element labels are source coordinates, not recommendations'},
 {'id':'b02-ch047-teacher','pages':[260,261],'subjects':['self'],'questions':['teacher'],'roles':[('teacher','父母'),('books','父母')],'sourceVoice':'chapter47 explicitly uses 父母 for 師長 and 詩書; same candidate set may have two semantic roles'},
 {'id':'b02-ch048-exam-stage','pages':[262],'subjects':['self'],'questions':['specified-exam-stage'],'roles':[],'sourceVoice':'野鶴: county/prefecture/circuit scopes require separate questions; no automatic stage inference'},
 {'id':'b02-ch049-first-exam','pages':[262,263],'subjects':['self'],'questions':['first-exam'],'roles':[('writing','父母'),('office','官鬼')],'sourceVoice':'chapter49 source stage is historical, not a modern admissions equivalence'}]
for m in methods:m['roles']=[{'id':i,'kin':k}for i,k in m['roles']]
classics=[{'name':n,'element':e,'sourceTerm':t}for n,e,t in[('春秋','金','春秋'),('毛詩','木','毛詩'),('書經','水','書經'),('禮記','火','禮記'),('易經','土','易經')]]
write(b/'SOURCE_CONTEXTS.json',{'date':'2026-10-28','methods':methods,'classics':classics,'historicalExamStages':['county','prefecture','circuit'],
 'sourceInstructionsAreData':True,'automaticQuestionInference':False,'allConditionalRulesCompiled':False,'practicalOutcomesValidated':False,
 'scope':'Private structural source projection. User target/subject/question cannot be inferred from roles. No chronology, strength, chosen use-line, prognosis, fertility, marriage or admissions result.'})
clauses=[
 ('age-arithmetic-rejected',[233],'author','Five years per line, followed by another cast for thirty-year blocks, explicitly rejected after forty-year experience; no lifespan formula extracted.','historical-method-critique'),
 ('longevity-root',[232,234],'chapter39','Self root and generator claims need strength/calendar/activity premises; general preference for moving 元神 does not transfer unchanged to this question.','conditional-open'),
 ('longevity-static-not-proof',[234,235],'chapter39','Static/moving/void/grave claims are historical, not clinical or death outcome validation.','historical-only'),
 ('avoidance-usefulness',[235],'chapter40','Source advocates 趨吉避凶; this is source text, not authorization or evidence to prescribe physical avoidance.','source-instruction-is-data'),
 ('hazard-analogies',[236,237,238],'chapter40','Element/spirit illness, water/fire, dream and social analogies are historical; no practical hazard classifier.','historical-only'),
 ('child-presence-qualified',[239],'覺子','子孫 favorable presence is qualified by 月破/旬空, timing and question context; mere presence insufficient.','conditional-open'),
 ('inner-outer-directions',[239,240,241],'chapter40','Internal/external 忌神 placement and generation directions require named premises; not physical safety routing.','conditional-open'),
 ('element-not-blanket',[242],'author','Counterexample rejects one blanket metal/fire conclusion; positive structural generation is not proven protective efficacy.','counterexample-open'),
 ('disease-correspondences',[243],'chapter40','Body organ/element/death correspondence is historical, not a diagnosis.','historical-only'),
 ('parents-separate',[244],'chapter41','Father, mother and grandparents are to be asked separately; source kin 父母 does not identify one biological person by itself.','explicit-question-guard'),
 ('parent-polarity-voices',[244,245],'quoted-old-method-vs-author','陽父陰母 is quoted; author later disputes conclusions from same-cast indiscriminate parent readings. Preserve voices instead of automatic polarity choice.','named-voices-unresolved'),
 ('parent-outcomes',[245,246],'chapter41','Anecdotal longevity and rescue reports not validated; no timing or medical intervention derived.','historical-only'),
 ('sibling-question',[247],'chapter42','Harmony/support/future-sibling/longevity are distinct questions and cannot all be read from one kin presence.','private-explicit-focus'),
 ('sibling-future-past',[248],'author','Source distinguishes future questions from past events; do not infer unknown parentage or family history.','scope-guard'),
 ('spouse-question',[249],'chapter43','Longevity/growing old/harmony/affliction are distinct; one cast concerns one subject.','private-explicit-focus'),
 ('wife-vs-response',[249],'author-vs黃金策','Author prioritizes 財-wife over response-wife when roles conflict; this bounded projection records candidates but never chooses a use-line.','named-source-candidates'),
 ('wife-multiple',[251],'chapter43','Original/changed multiple 財 and location distinctions do not by themselves identify real spouse, remarriage or harm.','conditional-open'),
 ('harmony-not-all',[250,251,252],'chapter43','Historical separation/growing-old anecdotes are not modern relationship classification.','historical-only'),
 ('offspring-question',[252],'chapter44','Existing child, additional children, future child and upbringing questions must be clear; avoid changing target after reading.','private-explicit-focus'),
 ('offspring-original-changed',[253,254],'chapter44','Original/changed descendant roles and strength have separate conditions; no child counts or fertility prognosis.','conditional-open'),
 ('adoption-paternity',[254,255],'chapter44','Age/adoption/lineage claims remain historical; no inference of real family relationships.','historical-only'),
 ('upbringing-not-rank',[255,256],'author','Author separates raising a child from future rank, disputes honorific 吉神 blanket status and predicting an infant career from parent cast.','scope-guard'),
 ('unasked-spillover',[256,257],'chapter44-end','Source discusses unasked other-person effects, but these anecdotes do not authorize hidden medical or family predictions.','historical-only'),
 ('literary-role',[257],'chapter45儒學','Writing 父母 and office 官 are source groups; strength/activity/qualifiers still open.','private-source-groups'),
 ('artisan-role',[258],'chapter45百工','Source uses 財 as 用神 and 子孫 as 元神 for 百工; this is a kin role designation, not selection of one use-line.','private-source-groups'),
 ('profession-voices',[257,258],'chapter45multiplevoices','九流 and spirit-profession polemics remain source voices, not classifications of people or scientific medicine.','historical-only'),
 ('five-classics',[258],'chapter46','金春秋/木毛詩/水書經/火禮記/土易經 are five source labels; not 五行 stem aliases or a modern study recommendation.','private-source-coordinates'),
 ('classic-explicit',[258],'覺子','不可概問須指定一經而卜之: require explicit classic, never choose it from a cast.','private-question-guard'),
 ('classic-case',[259,260],'chapter46','益→觀 role labels are structurally compared; repeated casts and retrospective success do not validate exam outcomes or modern chronology.','printed-fixture-only'),
 ('teacher-dual-parent',[260],'chapter47','父母 represents teacher and books in this question; semantic role does not make it biological parent.','private-dual-role'),
 ('teacher-change',[261],'chapter47','Activity/change/fee/self-response conditions retained, no automatic real teacher-quality evaluation.','conditional-open'),
 ('exam-stage',[262],'野鶴','County/prefecture/circuit examination scopes asked separately; a county result cannot settle later circuit success.','private-stage-guard'),
 ('first-exam-role',[262,263],'chapter49','父旺官興 qualified by source stage, useful-line/strength/activity/calendar; no modern admissions probability.','private-source-groups'),
 ('later-exam-open',[263],'chapter50-opening','歲科考 only opening read; do not mark chapter50 first-pass-complete or equate historical stages to modern school types.','partial-open'),
 ('toc-transcription',[15,235],'sourceimages','Working normalized 超遷 corrected to 趨避 on TOC/body evidence; original PDF and historical maps unchanged.','working-transcription-correction')]
write(b/'BOUNDED_CLAUSES.json',{'date':'2026-10-28','clauses':[{'id':i,'sourcePages':p,'sourceVoice':v,'disposition':d,'status':st,'outcomeValidated':False}for i,p,v,d,st in clauses],
 'allSubsidiaryClausesEnumerated':False,'wholeChaptersApplied':False,'sourceInstructionsAreData':True})
write(b/'PRINTED_FIXTURES.json',{'date':'2026-10-28','fixtures':[{'id':'B02-259-Yi-to-Guan','sourcePDFPage':259,'primaryHan':'益','changedHan':'觀','primary':42,'changed':20,
 'valuesBottomToTop':[9,8,8,8,7,7],'movingLines':[1],'sourceBaseLabelsBottomToTop':[{'branch':x,'kin':k}for x,k in[('子','父母'),('寅','兄弟'),('辰','妻財'),('未','妻財'),('巳','子孫'),('卯','兄弟')]],
 'sourceChangedLabels':[{'line':1,'branch':'未','kin':'妻財'}],'sourceSelfLine':3,'sourceResponseLine':6,'historicalDayLabel':'酉月丙子日','historicalDateMappedToGregorian':False,'sourceOutcomeValidated':False}]})
units=read(r/'research/liuyao-life-context/B02_CURRENT_UNITS.json');units['date']='2026-10-28';units['supersedesForCurrentWork']='../liuyao-life-context/B02_CURRENT_UNITS.json; historical prior file retained byte-identical'
for u in units['units']:
 n=u['printedNumber']
 if not u['supplement']and n in ranges:
  lo,hi=ranges[n];u.update(bodyPDFPages=list(range(lo,hi+1)),disposition='first-pass-complete-span-conditional-extraction-open',bodyTextualVolumeAsPrinted=4,latestEvidence='../liuyao-family-study/MANUAL_READINGS.json',entireUnitApplied=False)
 if u['id']=='B02-ch040':
  assert u['normalizedHeading']=='超遷';u['normalizedHeading']='趨避';u['workingTranscriptionCorrection']={'old':'超遷','new':'趨避','evidencePDFPages':[15,235],'sourceEmended':False}
 if u['id']=='B02-ch050':u.update(bodyPDFPages=[263],disposition='partial-body-reading-application-open',bodyTextualVolumeAsPrinted=4,latestEvidence='../liuyao-family-study/MANUAL_READINGS.json',entireUnitApplied=False)
units['currentCounts']={'registeredUnits':136,'regularNumberedUnits':130,'supplements':6,'headingOnlyBodyUnits':81,'partialFoundationUnits':7,'otherPartialUnits':1,'firstPassCompleteSpanUnits':47,'wholeUnitsApplied':0}
write(b/'B02_CURRENT_UNITS.json',units)
print('Promoted31 new retained-PDF source positions, reread2prior positions, recorded11first-pass spans and bounded question/semantic mappings; not whole-applied.')
