from pathlib import Path
import json
r=Path(__file__).resolve().parent.parent;w=r.parent;b=r/'research/liuyao-exam-intent';q=r/'qa/liuyao-exam-intent'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
report='LIUYAO_EXAM_INTENT_REPORT.md'
step=('B02: đọc tiếp37vị tríPDF264–300,gồm34trang nội dung và3lá kết quyển/ấn/nhan đề286–288;khép19khoảng chương50–67,kểcảhai chương55,giữ263mởđầu đãđọc trước. '
      'Chương68mớiđọc299–300,tiếp301. Trích31mệnhđề giới hạn/19ngữcảnh câu hỏi,táchthi văn/thi võ/cấp廩/nhậnchức/đơnthỉnh/thânphận người hỏi vàgiaiđoạn côngtrình. '
      '8kiểmđạt:2HHC thật cho臨→師19→7,sáunhãnchi-Lụcthân/Thế2Ứng5/巳→寅khớp;kinbiến官là dẫnxuất,chưaintrựctiếp. 58trườnghợp thiếu phạmvi giữnull;nămýđịnh đơnthỉnh đãnêu nhưngchưamãhóa giữriêng. '
      '37ảnhSHA/3QA360đãxem/2táirenderkhớppixel,46tệp tiếpnhận đúngbyte;modulechỉđổiđườngdẫnimport. Map136/66khoảngđọclầnđầu/62chỉđềmục/7nềnmộtphần/1mở68/0áphết. '
      '0HTTP/PDFgốcmới/nhânchứngmới;khôngxếphạng/thiđỗ/việclàm/tiềnbạc/sứckhỏe/pháplý/an toàn côngtrình. HTML/site/ZIPweb nguyênbyte,toànkhovẫnactive.')
nexts=[
 'B02 tiếp chương68求財 từPDF301;đãđọc299–300chỉlàmởđầu. Map66khoảngđọclầnđầu/62chỉđềmục/7nềnmộtphần/1mở68/0áphết. Khônglặp37ảnh/臨→師/58caunknown/19ngữcảnhđãđạt nếu logicnguồnkhôngđổi.',
 '31mệnhđề/19ngữcảnhchỉlàphépchiếucâuhỏi,nămýđịnhđơnthỉnhkhácseek-statuschưamãhóa;vượngsuy/giọngnguồn/ưu tiên/sinhkhắc/hợphóa/ứngkỳ vàđiềukiệnchương50–67cònmở. 卦身chưathànhtươngđương世;phươngvịnguồnchưalàđịađiểmBắcthực;rankcụthểlàcâuhỏi,khônglàkếtquả.',
 'Tửvi:hai bảngsinh năm/22tọađộlàmviệcvà6số–cungđãkiểm;chữ巳己/ranhnăm/selector1sao/đưôi童限/khởihạn/火鈴星/CanhNhâm vẫn mở. MộtGETmax403tạm hạnchế từtrướcgiữbody;khôngretryđểnéchặn. DươngNhận47ngữcảnh/tầngtiềnđề,9mục cáchkhác;NhàởPhiTinh/lịch/Bắcthực/đồ49mộtbộtháng,B03/MaiHoa cònactive.',
 'ỨngviênUIKiếnLộcgiữriêngvìbrowservôhiệuhóa,khôngvượtsetting. Nguồn/corpus/suyluận/QAngoàisite;khôngxuấtbản. Danhmục40/whole0,bốnlĩnhvựcactive;khôngtuyênbốhếtkho.'
]
write(b/'WORK_STATE.json',{'date':'2026-10-28','status':'bounded-exam-office-intent-reference-verified-full-conditions-active','catalogueID':'B02','latestReport':'v53/'+report,
 'completedStep':step,'summary':read(q/'RESULTS.json')['summary'],'sourceVerification':read(q/'SOURCE_RESULTS.json'),
 'sourceUnitMap':'v53/research/liuyao-exam-intent/B02_CURRENT_UNITS.json','next':nexts,
 'fullConditionalRulesEncoded':False,'sourceOutcomesValidated':False,'consumerChanged':False,'wholeCatalogueCompleted':False,
 'releaseVerification':'v53/qa/liuyao-exam-intent/RELEASE_RESULTS.json;expected until final --no-write succeeds'})
d=read(w/'EXHAUSTIVE_WORK_STATE.json');d['date']='2026-10-28';d['currentWork'].update(catalogueID='B02',relatedCatalogueIDs=['B02'],
 work='增刪卜易 — 科試、官職、意向與問事分界',reason='Continue unread retained chapters and prevent misleading automatic role selection from topic,occupation or a petition keyword.',
 sourceDirectory='v53/research/liuyao-exam-intent',currentStep=step,latestResearchReport='v53/'+report,functionalBacklog='v53/research/liuyao-exam-intent/WORK_STATE.json',
 internalExamIntentReference='v53/research/liuyao-exam-intent/intent-reference.mjs',currentB02UnitMap='v53/research/liuyao-exam-intent/B02_CURRENT_UNITS.json',currentTOC='v53/research/liuyao-exam-intent/B02_CURRENT_UNITS.json',
 sourceLimits='19first-passspans/31boundedclauses/19namedquestioncontexts,notwholeconditionalcompiler.37newviewedPDFpositionsinclude3non-ruleleaves;chapter68stillpartial,fivepetitionmotivesunencoded.',
 nextSourceLead={'sourceID':'B02-ch068-continue','status':'retained-source-reading-available','file':'v53/research/liuyao-exam-intent/B02_CURRENT_UNITS.json','remaining':' '.join(nexts)})
d['inProgressScope']='v53/research/liuyao-exam-intent/WORK_STATE.json';d['subsequentPriority'][0]=' '.join(nexts)
for p in[w/'EXHAUSTIVE_WORK_STATE.json',r/'research/EXHAUSTIVE_WORK_STATE.json']:write(p,d)
p=r/'research/full-study/WORK_STATE.json';d=read(p);d['date']='2026-10-28';d['latestResearchReport']=report;d['exhaustiveNext']=' '.join(nexts)
item=next(x for x in d['items']if x['id']=='yi')
if step not in item['completed']:item['completed'].append(step)
if ' '.join(nexts)not in item['remaining']:item['remaining'].append(' '.join(nexts))
item['latestScope']='../liuyao-exam-intent/WORK_STATE.json';item['nextFile']='../liuyao-exam-intent/B02_CURRENT_UNITS.json';write(p,d)
p=r/'research/library-current/COVERAGE.json';d=read(p);d['date']='2026-10-28';entry=next(x for x in d['catalogue']if x['id']=='B02');entry['latestExamIntentScope']=step
for f in['v53/'+report]+['v53/research/liuyao-exam-intent/'+x for x in['WORK_STATE.json','SOURCE_MANIFEST.json','MANUAL_READINGS.json','B02_CURRENT_UNITS.json','BOUNDED_CLAUSES.json','SOURCE_CONTEXTS.json','PRINTED_FIXTURE.json','PROMOTION_IDENTITIES.json','intent-reference.mjs']]+['v53/qa/liuyao-exam-intent/'+x for x in['RESULTS.json','SOURCE_RESULTS.json']]:
 if f not in entry['currentEvidence']:entry['currentEvidence'].append(f)
d['latestFollowup']=report+': '+step;d['latestAcquisitionCounts']={'scope':report,'newHTTPRequests':0,'newOriginalContainers':0,'newViewedPDFPositions':37,'firstReadContentPositions':34,'nonRuleLeaves':3,'newHighResolutionQA':3,'inheritedOpeningNotReread':263,'firstPassSpansAdded':19,'wholeWorksApplied':0}
d['counts']['newDownloadsThisScope']=0;d['counts']['newDownloadsThisScopeBasis']='RetainedPDF unchanged:37newlyviewedpositions/34content+3nonruleleaves;3QAderivedrenders,noHTTP/neworiginalcontainer/independentwitness.'
assert d['counts']['catalogueRecords']==40 and d['counts']['wholeWorkApplied']==0;write(p,d)
note='Mốc Dịch — Thi cử, chức vụ và ý định câu hỏi, 28/10/2026: `'+report+'`. '+step+'\n\n'
for p in[w/'PROJECT_RESEARCH_STATE.md',r/'NEXT_STEPS.md',r/'research/library-current/COVERAGE.md']:
 text=p.read_text(encoding='utf-8-sig')
 if not text.startswith(note):p.write_text(note+text,encoding='utf-8')
p=w/'PENDING_RESEARCH_STATE.json';d=read(p);d.update(date='2026-10-28',status='Liuyao-exam-intent-current-scope-active',workDirectory='v53/research/liuyao-exam-intent',currentWorkState='v53/research/liuyao-exam-intent/WORK_STATE.json',latestReport='v53/'+report,next=nexts,consumerChanged=False,wholeCatalogueCompleted=False)
d['latestReleaseVerified']={'report':'v53/TUVI_VOID_CHILD_REPORT.md','date':'2026-10-28','manifestFiles':3549,'sourceZIPFiles':3550,'sourceZIPBytes':2075808140,'htmlUnchanged':True,'webZIPUnchanged':True,'verifiedBy':'python v53/scripts/verify-tuvi-void-child-release.py --no-write'}
d['previousStaging']={'directory':'tmp/liuyao-b02-exams-staging','status':'promoted-reference-body-import-only-relocated','newViewedPositions':37,'firstPassSpansAdded':19,'next':'B02chapter68PDF301,fullconditionsandallfourdomainsactive'}
write(p,d)
print('Recorded19 further first-pass spans and explicit intent projection;all conditional application remains active.')
