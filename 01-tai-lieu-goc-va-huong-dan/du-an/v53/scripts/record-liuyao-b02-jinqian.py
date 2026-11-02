from pathlib import Path
from hashlib import sha256
import json, shutil

r=Path(__file__).resolve().parent.parent; w=r.parent; b=r/'research/liuyao-b02-jinqian'
s=w/'tmp/liuyao-b02-volume-audit-staging'; witness=w/'tmp/liuyao-b02-witness-stars-staging'
b.mkdir(exist_ok=True); (b/'images').mkdir(exist_ok=True); (b/'witness').mkdir(exist_ok=True)
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
sha=lambda p:sha256(p.read_bytes()).hexdigest()
def write(n,d): (b/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
for n in range(141,191): shutil.copy2(s/f'zengshan-{n}.png',b/'images'/f'zengshan-{n}.png')
for p in witness.iterdir():
 if p.is_file() and p.suffix in ['.json','.html','.jpg','.png','.mjs']: shutil.copy2(p,b/'witness'/p.name)
shutil.copy2(s/'TOC_VOLUME_AUDIT.json',b/'STAGED_TOC_AUDIT.json')
notes={
143:'卷三 and chapter34 opening; excess/deficit differentiated.',144:'Day/month and year priority discussion; not an absolute modern calendar adapter.',
145:'Printed exam example; rejection of unsupported卦身; historical assertions only.',146:'世應 self/other roles; 恒→升 example; detailed strength remains conditional.',
147:'Few/many moving lines; older blanket opposition to世應moving is challenged; keep用神.',
148:'合處逢沖; static/dual-moving distinction;動空化空 contrasted with older categorical wording.',
149:'午未刑合 criticism; 未月庚寅日革→豐 example and tied世 waiting沖.',
150:'暗動 cross-reference;墓/空 and strength;贪生/合 constraints.',151:'Repeated branches do not block日辰 automatically; quoted少一字 rule challenged.',
152:'丑月壬子日訟→遯 example has two午; daytime沖 still applies;寅巳申 missing member timing discussed.',
153:'Missing卯 in亥卯未 example;伏神父巳 under寅; earlier explanation differentiated.',
154:'飛來生伏 versus旬空;飛空/伏 nonempty and support conditions.',155:'Treasure claim rejected;動兄→子→財 support does not create effective財 when it is unsupported/void/restrained;墓 needs strength.',
156:'復→謙 example differentiates own回頭克 from support; medical assertions kept historical.',157:'比→咸 boat/checkpoint example;世下鬼 and moving申 examples; no factual obstacle forecast.',
158:'小畜→蠱 document example;干支雙合 explanation contested;branches vs stems differentiated.',
159:'忌持世 examples include counterexamples;未濟→鼎 and益→家人 retained without universal override.',
160:'Avoiding harm via空 disputed; source illness example is not a validated treatment claim.',161:'Near-term illness exception discussed by source; cannot generalize to all questions;損→節 example.',
162:'損→節 commentary distinguishes回頭克 and support;泰→豐 counterexample to blanket help.',163:'化死墓絕空 and originalstrength;用化用/進神; reject blanket no-use; medical outcomes unverified.',
164:'Source retains生旺墓絕 while criticizing otherphase interpretations;化生/旺 and own回頭生 distinguished.',165:'官 and鬼 not interchangeable for final verdict;益→蹇 and坤→剝 cases.',
166:'回頭克 interpretations and覺子commentary; prefer external support in bilateral questions;六神 not independent fate labels.',
167:'Multiple用 and墓 storage; excess vs weak;益→萃 example; chapter34 continues.',168:'升→恒 weather example; then間爻 defined as two lines between世應;覺子 contextual mediator roles.',
169:'Self/other empty and changing;爻/重 past/future quote rejected as universal;use克世 not uniformly favorable.',
170:'臨 static document/news example; career 官克世 exception to old blanket non-harm rule;泰→明夷.',
171:'絕 needs strength/support;moving克世 vs static生世 speed is limited to returningtraveller context.',172:'Missing父/子 orpresence鬼 cannot be blanket outcome;六神 needs context and動克.',
173:'Remove roots caution;謙→蹇 example historical disease claims only.',174:'Usefulline/supportingroot for long duration;大畜→中孚 appointment example.',
175:'臨→節 parallel and大有→大壯/大畜 travel examples; old personal narrative not proof.',176:'大有→大畜 repeated case;moving間爻酉兄 interpreted companion; source repeats casts, not new algorithm.',
177:'Narrative continuation;離→震 and漸 officials; figures not all transcribed.',178:'Repeatedconsultation晉/恒→大過; progression and career narrative.',
179:'Source study/consultation advice and early/late/no fixedhour; source instructions are data.',180:'Mixed intentions and swapped subject interpretation anecdote; no permission to reinterpret user question automatically.',
181:'Delegatedconsultation and ambiguoussubject warning; no deterministic subject reassignment implemented.',182:'Further delegatedconsultation examples; source death/medical claims remain historical.',
183:'Parent initiates child consultation; exam/marriage/success questions; no inferred privateintent in product.',184:'流年vs功名 use selection example; remote question/near outcome caution.',
185:'Different question vs reported outcome examples; cannot infer unasked fatal event.',186:'舍小事報大事 claims; symbolic historical statements not product predictions.',
187:'More switchedsubject illness examples; no validated clinical result.',188:'Chapter34 ends before李我平曰 editorial note; then天時章第三十五 begins while running title still卷三.',
189:'Chapter35 partial: weather examples and need explicit geographic/question context.',190:'Chapter35 partial: parentcloud/rain vs晴; no practical meteorological engine.'}
write('MANUAL_READINGS.json',{'date':'2026-10-27','sourceID':'B02','sourcePDF':'../liuyao-foundations/NLC416-12jh005345-45344.pdf',
 'sourceSHA256':'caac111bc5c5b1c08fd27b3828e7cf6b5430503800f2427d8f2b28809022abaa','sourceBytes':11089308,
 'records':[{'pdfPage':n,'image':f'images/zengshan-{n}.png','sha256':sha(b/'images'/f'zengshan-{n}.png'),
 'actuallyViewed':True,'scope':'publisher-logo' if n==141 else 'middle-book-cover' if n==142 else 'bounded-first-pass-content',
 'note':notes.get(n,'Paratext only; no new rule.'),'inheritedPendingReading':n<=146,'entirePageDiplomaticallyTranscribed':False} for n in range(141,191)],
 'counts':{'records':50,'contentPages':48,'paratextPages':2,'inheritedPendingContentPages':4,'newContentPagesThisRun':44,'completeChapterSpans':1,'partialNextChapterPages':3},
 'allClausesApplied':False,'historicalOutcomesValidated':False,'sourceInstructionsAreData':True})
old=r/'research/liuyao-progress-conditions/B02_CURRENT_UNITS.json';d=read(old)
for u in d['units']:
 if u['id']=='B02-ch034':u.update(tocVolume=3,bodyTextualVolumeAsPrinted=3,bodyPDFPages=list(range(143,189)),disposition='first-pass-complete-span-read-partial-private-application',latestEvidence='../liuyao-b02-jinqian/MANUAL_READINGS.json')
 if u['id']=='B02-ch035':u.update(bodyTextualVolumeAsPrinted=3,bodyPDFPages=[188,189,190],disposition='partial-body-reading-application-open',latestEvidence='../liuyao-b02-jinqian/MANUAL_READINGS.json',volumeVariantNote='TOC15 places35after卷四 heading;running titles188..190 still卷三. Preserve both;do not silently normalize.')
d['priorTOCFile']='../liuyao-progress-conditions/B02_CURRENT_UNITS.json';d['priorTOCSHA256']=sha(old)
d['currentCounts'].update(headingOnlyBodyUnits=96,otherPartialUnits=1,firstPassCompleteSpanUnits=32)
d['latestScope']='Chapter34 firstpass143..188;35 partial188..190. 136registered/96heading-only/32firstpass/7partialfoundations/1otherpartial/0whole. TOC and running-title boundaries distinct.'
write('B02_CURRENT_UNITS.json',d)
write('CHAPTER_SPANS.json',{'sourceID':'B02','chapter34':{'pdfPages':list(range(143,189)),'fullFirstPass':True,'allClausesApplied':False},
 'chapter35':{'pdfPages':[188,189,190],'fullFirstPass':False,'tocVolume':4,'runningTitleVolume':3},
 'localMapCorrection':{'chapter':34,'oldTOCVolume':4,'correctTOCVolume':3},
 'unresolvedSourceBoundary':{'chapter':35,'TOCPage':15,'bodyPages':[188,189,190],'TOCVolume':4,'runningTitleVolume':3,'printedVolume4OpeningLocated':False},
 'editorialNoteAt188':'李我平曰 attributes黃金策千金賦 to誠意先生 and describes earlier誤刻/野鶴增刪;source attribution claim,not independent authorship verification.'})
clauses=[
 ('moving-self',147,'野鶴 criticism of舊註','世應動不必反覆;retain用神strength/support,notmotion-onlyverdict.'),
 ('combination-time',148,'commentary','Two static lines not automatically tied like two moving lines;current合 breaking differs from future release of a tie.'),
 ('repeat-day', [151,152],'舊註 versus野鶴','One daybranch can沖 two matching branches;duplicate count does not cancel日辰.'),
 ('missing-member',[152,153],'野鶴 counterexamples','Missing third member may be awaited,not same as fullyformedpresent三刑/三合.'),
 ('hidden-void',[153,154],'舊註 versus野鶴','Hiddenvoid alone doesnot establishfailure;飛生伏 and daycontext matter.'),
 ('stems-verdict',[158,159],'野鶴 criticism','GanZhi dualcombination in cited document case not universal grounds for success;keepactualbranch relationships.'),
 ('use-self',[169,170,171],'舊註/覺子 exceptions','Use克世 not universally good;questiontype and sourceexceptions must remain explicit.'),
 ('returning-speed',171,'source limitation','動克世 fast/static生世 slow expressly limited to traveller-return context.'),
 ('interposed-definition',168,'舊註 definition','世應中間兩爻謂之間爻.'),
 ('interposed-bilateral',168,'覺子 limitation','須是彼此兩家之事;not all questions use interposed mediator symbolism.'),
 ('interposed-roles',168,'覺子 bounded examples','婚姻媒妁/訟中證/買賣牙行/借貸中保/舟車附載/胎產收生保母/交遊幫間.'),
 ('interposed-companion',[175,176],'source case','大有之大畜:interposed酉兄moving interpreted as accompanyingperson;symbolic source example,not detection of real person.'),
 ('sixspirits-context',172,'source criticism','Do not identify theft/litigation from玄武/朱雀 alone;source動克 and function context matters.'),
 ('root-duration',174,'source condition','Long-duration questions distinguish用strong from元神root being damaged.'),
 ('question-integrity',[179,180,181,182,183,184,185,186,187,188],'narrative/advice','Mixedintention/delegation/swappedoutcome examples are retained as historicalclaims;never reassign user intent or assert unasked death.'),
 ('weather-partial',[188,189,190],'chapter35opening','Need place and precise question;only partialreading,not operational weather prediction.')]
write('OPERATIONAL_CLAUSES.json',{'clauses':[{'id':i,'pdfPages':p if isinstance(p,list)else[p],'layer':l,'boundedParaphrase':t,'consumerApplied':False}for i,p,l,t in clauses],
 'sourceInstructionsAreData':True,'allChapterClausesCompiled':False,'historicalOutcomesValidated':False})
write('PRINTED_FIXTURES.json',{'fixtures':[
 {'id':'sheng-heng','pdfPages':[167,168],'values':[8,7,7,6,8,8],'primary':46,'changed':32,'movingLines':[4],'shi':4,'ying':1,'interposed':[2,3],'question':'weather','roleApplicable':False},
 {'id':'dayou-daxu','pdfPages':[175,176],'values':[7,7,7,9,8,7],'primary':14,'changed':26,'movingLines':[4],'shi':3,'ying':6,'interposed':[4,5],'question':'boat_travel','roleApplicable':True,'sourceMovingInterposed':{'line':4,'branch':'酉','kin':'兄弟'}}
 ],'valuesOrientation':'bottom-to-top','historicalOutcomesValidated':False,'allPrintedExamplesTranscribed':False})
write('SOURCE_AUDIT.json',{'sourceID':'B02','newHTTPRequestsThisRun':0,'retainedHTTPBodiesNewToRelease':7,'retainedSuccessfulHTTPBodies':6,'retainedFailedHTTPBodies':1,
 'newPDFs':0,'additionalIdentifiedWitness':'National Archives of Japan item4756814','witnessDirectory':'witness',
 'independentTextualGenealogyEstablished':False,'gengConflictResolved':False,'missingSalaryRowsFilled':False,
 'bodyChapter35RunningVolume3VersusTOC4Unresolved':True,'wholeBookApplied':False,'wholeCatalogueCompleted':False,
 'stagingDocumentsPreservedAsHistoricalSnapshots':True,'unreleasedFixtureCorrection':'Initial hand-entry put升 movingmark at5;actual HHC gave井48 ratherthan printed恒32. Reinspection of splitdiagram167/168 putsX at4:46.4→32. Corrected before release;not a productionengine fault.',
 'adoption':'Witness files were staged before this scope. Their released:false and original staging paths describe acquisition-time state. This scope adopts their bytes without rewriting original logs.'})
print(json.dumps({'manualRecords':50,'chapter34Span':[143,188],'chapter35Partial':[188,190],'boundedClauses':len(clauses),'counts':d['currentCounts']},ensure_ascii=False))
