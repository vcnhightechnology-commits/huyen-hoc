from pathlib import Path
from hashlib import sha256
from PIL import Image
import json
w=Path(__file__).resolve().parents[2];s=Path(__file__).resolve().parent;r=w/'v53'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
def write(name,d):(s/name).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
sha=lambda p:sha256(p.read_bytes()).hexdigest()
pdf=r/'research/liuyao-foundations/NLC416-12jh005345-45344.pdf'
assert sha(pdf)=='caac111bc5c5b1c08fd27b3828e7cf6b5430503800f2427d8f2b28809022abaa'
req=next(x for x in read(r/'research/liuyao-foundations/REQUESTS.json')['records']if x['file']==pdf.name)
assert req['status']==200 and req['tls']['authorized']and req['sha256']==sha(pdf)
images=[]
for n in range(21,49):
 p=r/f'research/{"liuyao-use-god"if n==48 else"liuyao-foundations"}/images/zengshan-{n}.png';im=Image.open(p)
 images.append({'pdfPage':n,'file':p.relative_to(w).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p),'size':list(im.size),'retainedDPIApprox':round(im.info['dpi'][0]),'actuallyViewed':True,'newSourcePosition':False,'readingLevel':'first-pass-full-unit-span;not-diplomatic-transcription'})
write('SOURCE_MANIFEST.json',{'date':'2026-10-28','sourcePDF':pdf.relative_to(w).as_posix(),'sourceBytes':pdf.stat().st_size,'sourceSHA256':sha(pdf),'retainedHTTPAndTLSRecord':'v53/research/liuyao-foundations/REQUESTS.json','retainedHTTPStatus':200,'retainedTLSAuthorized':True,'records':images,'retainedPositionsReviewed':28,'firstEverReadsNotClaimed':True,'newHTTPRequests':0,'newOriginalContainers':0,'newIndependentWitnesses':0,'allSourceCharactersCollated':False})
spans=[(1,'八卦',21,21,'八卦圖 on21;source names/family metaphors,not biological-outcome evidence.'),(2,'卦象圖',21,24,'Begins21,continues22–24 coin definitions and two polarity-recognition examples. Circle/cross are still original polarity for recognition,not the changed figure.'),(3,'八宮',24,45,'Begins八宮六十四卦名24;names24–26,all64printed diagrams26–34,dialogue34–43,full夬→姤 example44 and explanatory continuation45 before第四. Dialogue is part of span,not omitted.'),(4,'渾天甲子',45,46,'Heading45 through branch table and inner/outer bottom-up explanation46 before第五;does not by itself print every heavenly-stem coordinate.'),(5,'六親歌',46,47,'Heading46 through乾example and explanation47 before第六.'),(6,'世應',47,47,'Heading47 through stage positions and response offset before第七.'),(7,'動變',47,48,'Heading47 includes four THREE-line diagrams;continues48 full六-line需→訟 and original-palace kin note before第八.')]
chapterRanges=[{'id':f'B02-ch{n:03d}','printedNumber':n,'heading':h,'firstPDFPosition':a,'lastPDFPosition':b,'bodyPDFPages':list(range(a,b+1)),'reading':'first-pass-complete-span-read-partial-private-application','boundaryNote':note,'entireUnitApplied':False}for n,h,a,b,note in spans]
write('MANUAL_READINGS.json',{'date':'2026-10-28','chapterRanges':chapterRanges,'retainedSourcePositionsReviewed':list(range(21,49)),'newHTTPRequests':0,'allImageCharactersCollated':False,'fullConditionalCompiler':False,'oldBoundedReadingsUnchanged':'v53/research/liuyao-foundations/MANUAL_READINGS.json','firstPassNotProofOfCompleteApplication':True})
clauses=[
(21,'family-metaphors','乾為父/坤為母/震坎艮為長中少男/巽離兌為長中少女','Trigram mnemonics,not identification of actual family members or sex.'),
(22,'coin-symbols','一背為單/兩背為拆/三背為重/純字為交','Working6/7/8/9encoding inherited;keep coin-face semantics explicit.'),
(23,'recognition-original','圓兒仍算一點/叉兒仍算兩點','Recognition of original polarity does not yet flip moving lines.'),
(24,'eight-palace-names','八宮六十四卦名','Names and diagram sequence distinct from the complete prediction model.'),
(26,'instructional-table','初學點卦不會裝卦者須將占得之卦照此全圖裝','64diagram table is a source witness;three mismatching cells are retained,not silently treated as runtime truth.'),
(34,'simplified-dialogue-start','余不知五行焉知斷卦','Named conversation introducing a simplified teaching method.'),
(35,'simplified-self','不管卦中動與不動即照全圖內單看世爻','Quoted preliminary shortcut;later qualifications prevent elevating it to an unconditional runtime rule.'),
(35,'simple-outcomes','官鬼持世/子孫持世/妻財持世/兄弟持世','Source outcome claims,not empirically validated outcomes or safe public categorical forecasts.'),
(35,'ten-six-clash','此八宮頭一卦皆是六沖卦/天雷無妄雷天大壯亦是六沖卦','Ten named six-clash figures;identity is structural,not a clinical outcome adapter.'),
(36,'qualification','倘若稍知五行之理者不可以此為法','The source explicitly restricts its simplified method;do not collapse dialogue into the later full method.'),
(36,'missing-premises','空而不空/破而不破/墓而不墓/絕而不絕/真反吟假反吟','Named conditional concepts still require their later chapters;first-pass reading does not supply missing premises.'),
(37,'repeat-cast-voice','一卦不現再占一卦/不可又占他事','Conversation allows further casts for one clearly delimited concern;not an automatic multi-cast or universal Yi rule.'),
(37,'separate-subjects','一事而與衆人同其禍福者各占一卦決之','Source claim about several people;keep explicit subject/question and do not manufacture correlations or outcomes.'),
(38,'learning-sequence','先念渾天甲子六親歌/再學變動','Instructional sequence,not complete application status.'),
(38,'calendar-recording','先寫年月日辰再照六神章中寫出六神','Historical instruction needs explicit calendar/day-stem adapter;none inferred here.'),
(39,'self-context','自占吉凶者以世爻為用神','For explicitly self-focused question;not universal role across all subjects.'),
(39,'month-context','戌土/寅卯月/辰月/巳午月/未丑月/戌月/申酉亥子月','Examples attached to乾戌Self;separate month-control/clash/support/seasonal weakness and do not turn a single named month into complete strength.'),
(40,'day-moving-changed','日辰能生剋沖合/卦中之動爻/世爻自動變出之爻','Three further influence layers;does not authorize unconditional summing or a numerical score.'),
(41,'mixed-influences','兩處剋兩處生者須看旺衰/有生之名無生之實','Explicit conflict/strength qualification;no inference that all nominal support is effective.'),
(41,'calendar-role','不拘占得何卦卦內若以巳午之火作官星','Calendar symbol uses declared kin context;do not infer a person or event from a bare element.'),
(42,'multiple-parents','父母若兩爻俱動或俱不動擇其旺者/一爻動者擇其動者','Source choice includes strength premises and exceptions from later用神章;no complete automatic selector here.'),
(42,'opposite-desire','欲其吉者/欲其衰者','Question/desire changes source treatment;do not infer intent from casting time or user identity.'),
(43,'progressive-outline','此為綱領/後卷各章/由淺入深','Explicitly an outline pointing to later conditions,not a self-contained complete engine.'),
(45,'changed-kin-anchor','六親須照前卦而論也','Changed line kin uses original palace;夬→姤土 remains兄弟 under坤土,not父母 under乾金.'),
(46,'annotation-order','點卦由下點至上故裝五行亦由下而往上','Bottom-to-top line indexing;table images display top-to-bottom.'),
(47,'trigram-width','乾卦初爻動/乾卦上下動/坤卦中爻動/坤卦三爻動','Four diagrams have THREE lines. Do not convert them to full六-linehexagram identities without an explicit companion trigram.'),
(48,'changed-kin-anchor-again','變出之爻安六親者仍照正卦而安','Printed需→訟 example preserves坤土 as changed kin basis;not changed chart乾金.'),
]
write('FOUNDATIONAL_CONTEXTS.json',{'date':'2026-10-28','basis':'Bounded working anchors and interpretations,not a diplomatic transcription or complete clause inventory.','clauses':[{'id':f'F{i:02d}','pdfPage':n,'topic':topic,'workingSourceAnchor':text,'disposition':note}for i,(n,topic,text,note)in enumerate(clauses,1)],'sourceOutcomesValidated':False,'consumerApplied':False,'missingPremises':['effective-strength','use-line-priority-and-exceptions','calendar-boundary','source-voice-priority','full-later-conditional-rules']})
write('MOTION_FIXTURES.json',{'date':'2026-10-28','threeLinePDFPage':47,'orientation':'bottom-to-top','threeLineExamples':[{'id':'qian-first','values':[9,7,7],'primary':'乾','changed':'巽'},{'id':'qian-both-ends','values':[9,7,9],'primary':'乾','changed':'坎'},{'id':'kun-middle','values':[8,6,8],'primary':'坤','changed':'坎'},{'id':'kun-all-three','values':[6,6,6],'primary':'坤','changed':'乾'}],'sixLineExample':{'id':'xu-to-song','pdfPage':48,'values':[9,7,9,6,7,6],'primaryNumber':5,'changedNumber':6,'primaryPalace':'坤','primaryBranchKinBottomToTop':[['子','妻財'],['寅','官鬼'],['辰','兄弟'],['申','子孫'],['戌','兄弟'],['子','妻財']],'baseLine1MatchesReferenceButDiffersFromTable33':True,'baseLine1ReferenceKin':'妻財','changedBranchKin':[{'line':1,'branch':'寅','kin':'官鬼'},{'line':3,'branch':'午','kin':'父母'},{'line':4,'branch':'午','kin':'父母'},{'line':6,'branch':'戌','kin':'兄弟'}],'changedOwnPalaceIsNotKinAnchor':True},'threeLineEmbeddingsAreDerivedNotPrintedSixLineFixtures':True})
qa=read(s/'QA_RENDERS.json')
for x in qa['records']:
 x['cropActuallyViewed']=True;x['fullQAActuallyViewed']=False
 assert sha(s/x['qaFile'])==x['qaSHA256']and sha(s/x['cropFile'])==x['cropSHA256']
 a=Image.open(s/x['qaFile']).convert('RGB').crop(x['cropBox']);b=Image.open(s/x['cropFile']).convert('RGB');assert a.size==b.size and a.tobytes()==b.tobytes();x['cropPixelMatch']=True
write('QA_RENDERS.json',qa)
cmp=read(s/'DIAGRAM_COMPARISON.json');assert len(cmp['differences'])==3
write('SOURCE_ANOMALIES.json',{'date':'2026-10-28','differences':[{**x,'cropFile':f'anomaly-crop-{x["pages"][0]}.png','cropDirectlyViewed':True,'status':'literal-source-versus-bounded-rule-mismatch','sourceNotEmended':True}for x in cmp['differences']],'sameEditionNoIndependentWitness':True,'source26Line3Literal':'卯土','source29Line2Literal':'兄弟卯木','source33Line1Literal':'父母子水','threeLine47IsNotSixLineChart':True,'all384RowsIndependentFromRuntimeInput':True,'independenceMeaning':'Manual table input from same retained edition,not an independent edition or predictive outcome dataset.'})
units=read(r/'research/liuyao-closing-context/B02_CURRENT_UNITS.json')
for x in chapterRanges:
 u=next(u for u in units['units']if u['id']==x['id']);u['bodyPDFPages']=x['bodyPDFPages'];u['disposition']=x['reading'];u['latestEvidence']='MANUAL_READINGS.json';u['boundaryNote']=x['boundaryNote']
units['currentCounts'].update(partialFoundationUnits=0,firstPassCompleteSpanUnits=137)
units['date']='2026-10-28';units['wholeBookApplied']=False
units['latestUpdate']='Seven foundational spans read,137first-passunits;384printeddiagramrowscollatedwith3retainedmismatches/32explicit己→巳normalizations. Notall394positions/allcharacters/fullconditions/allprefaces.'
write('B02_CURRENT_UNITS.json',units)
print(json.dumps({'retainedPositionsReviewed':28,'firstPassSpansAdded':7,'boundedContextGroups':len(clauses),'firstPassUnitsCurrent':137,'sourceMismatches':3,'sourceCharactersFullyCollated':False}))
