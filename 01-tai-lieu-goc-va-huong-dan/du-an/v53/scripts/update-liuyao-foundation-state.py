from pathlib import Path
import json
r=Path(__file__).resolve().parent.parent;w=r.parent;b=r/'research/liuyao-foundation-span';q=r/'qa/liuyao-foundation-span'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
report='LIUYAO_FOUNDATION_SPAN_REPORT.md'
step=('B02: đọc đủ khoảng7mục nền1–7/PDF21–48 đã giữ,28vị trí mở rộng,0HTTP/vị trí nguồn/PDF/nhân chứng mới. Mục八宮24–45 bao gồm hội thoại và ví dụ,không chỉ bảng. Map137/137khoảng đọc đầu/0nền một phần/0áphết;không khẳng định đọc mọi chữ/lời tựa/394vị trí hoặc áp hết điều kiện. '
'Nhập trực tiếp64đồ hình/384dòng chi-hành-Lục thân trước đối engine:64HHC thật/cung/ThếỨng khớp,32chuẩn hóa己→巳 tường minh;giữ3ô khác ởQuán20-hào3卯土,TrungPhu61-hào2兄弟卯木,Nhu5-hào1父母子水. 3crop360đã xem/1cropnative48/2tái render khớppixel. '
'7kiểm đạt;thêm2HHC Nhu→Tụng5→6,bốn hào động1/3/4/6 và6nhãn gốc+4nhãn biến khớp,kin theoKhôn gốc. Tổng66HHC trongphạmvi;vídụ48kếthừatừuse-god,chạylạichoAPI3/6mới,khônglàvídụnguồnđộclậpmới;khônglặp vídụ44–45/23–24. Bốn hình47 có3hào,không tự thành6hào;module yêu cầu width tườngminh. '
'27nhóm ngữcảnh giữ cách họcgiảnlược riêng với điều kiện vượngsuy/hiệulực/chọnDụng;48inTài子khác33inPhụ子 trongcùng sách,khôngphải nhânchứng độclập. 28identity/2module chỉđổiimport;HTML/site/ZIPweb nguyênbyte,toànkhoactive.')
nexts=[
'B02:137đơnvị đã đọc lượtđầu theo khoảng/0áp trọn. Tiếpkiểm các điều kiện hoànchỉnh Dụng/Nguyên/Kỵ/Cừu,vượngsuy,hiệulực,ưu tiên,phảnvídụ vàgiọngnguồn;không quay lạiđếm7nền/64đồ/384dòng làtrang mới. Chưađối mọi chữ,lờitựa hoặc394vịtrí.',
'Giữ3ô nguồn20.3/61.2/5.1 riêng khỏi engine;32己→巳 chỉtrong cộtchi. Bốn hình47chỉ3hào;48Nhu→Tụngđộng1/3/4/6,kinbiếntheoKhôn gốc. Khônglặp66HHC nếu logicvànguồnkhôngđổi. Bảnso384hàng vẫnchỉcùngmộtấnphẩm,khônglàkiểmchứngtiênđoán.',
'B02còn100病/痘,chọndụng/飛伏/應期/合化制/ưu tiên/tranhluậngiọngnguồn. TOC106賣宅/body賃宅,110歸宅/body新宅giữriêng. Colophon393民國14tháng11,ngàykhôngghi/lịchthángkhôngtựquyGregorian.',
'Các lĩnhvực khácactive:Tửvi童限/火鈴/CanhNhâm/khởihạn;BátTự47ngữcảnhDươngNhận/9cáchkhác/vượngsuy;nhàPhiTinh/ranhlịch/Bắcthực;B03/MaiHoa/chữmở. BrowserUIvôhiệuhóa,khôngvượtsetting;mọinguồn/QAngoàisite,khôngxuấtbản. Danhmục40/whole0.'
]
write(b/'WORK_STATE.json',{'date':'2026-10-28','status':'foundational-first-pass-spans-and-printed-diagrams-verified-full-conditions-active','catalogueID':'B02','latestReport':'v53/'+report,'completedStep':step,'summary':read(q/'RESULTS.json')['summary'],'sourceVerification':read(q/'SOURCE_RESULTS.json'),'sourceUnitMap':'v53/research/liuyao-foundation-span/B02_CURRENT_UNITS.json','next':nexts,'fullConditionalRulesEncoded':False,'allImageCharactersCollated':False,'consumerChanged':False,'wholeCatalogueCompleted':False,'releaseVerification':'v53/qa/liuyao-foundation-span/RELEASE_RESULTS.json;expecteduntilfinal--no-write'})
d=read(w/'EXHAUSTIVE_WORK_STATE.json');d['date']='2026-10-28';d['currentWork'].update(catalogueID='B02',relatedCatalogueIDs=['B02'],work='增刪卜易 — 七個基礎章跨度與六十四圖逐行對照',reason='Close first-pass foundational spans and distinguish literal source cells,trigram dimensions and changed-kin anchors.',sourceDirectory='v53/research/liuyao-foundation-span',currentStep=step,latestResearchReport='v53/'+report,functionalBacklog='v53/research/liuyao-foundation-span/WORK_STATE.json',currentB02UnitMap='v53/research/liuyao-foundation-span/B02_CURRENT_UNITS.json',currentTOC='v53/research/liuyao-foundation-span/B02_CURRENT_UNITS.json',internalMotionReference='v53/research/liuyao-foundation-span/motion-reference.mjs',internalPrintedDiagramReference='v53/research/liuyao-foundation-span/diagram-reference.mjs',sourceLimits='137first-passspans/0wholeapplied.28retainedpositionsreviewed/384printedrowscollated/3literalcellmismatches,notall394positions/allcharacters/fullconditions.',nextSourceLead={'sourceID':'B02-complete-predicates-and-counterexamples','status':'full-source-conditional-extraction-active','file':'v53/research/liuyao-foundation-span/WORK_STATE.json','remaining':' '.join(nexts)})
d['inProgressScope']='v53/research/liuyao-foundation-span/WORK_STATE.json';d['subsequentPriority'][0]=' '.join(nexts)
for p in[w/'EXHAUSTIVE_WORK_STATE.json',r/'research/EXHAUSTIVE_WORK_STATE.json']:write(p,d)
p=r/'research/full-study/WORK_STATE.json';d=read(p);d['date']='2026-10-28';d['latestResearchReport']=report;d['exhaustiveNext']=' '.join(nexts);item=next(x for x in d['items']if x['id']=='yi')
if step not in item['completed']:item['completed'].append(step)
if ' '.join(nexts)not in item['remaining']:item['remaining'].append(' '.join(nexts))
item['latestScope']='../liuyao-foundation-span/WORK_STATE.json';item['nextFile']='../liuyao-foundation-span/B02_CURRENT_UNITS.json';write(p,d)
p=r/'research/library-current/COVERAGE.json';d=read(p);d['date']='2026-10-28';entry=next(x for x in d['catalogue']if x['id']=='B02');entry['latestFoundationSpanScope']=step
entry['currentSourceUnitCounts']={'registeredUnits':137,'regularNumberedUnits':130,'supplements':7,'firstPassSpans':137,'headingOnly':0,'partialFoundation':0,'otherPartial':0,'wholeUnitsApplied':0,'historical136UnitMapsRetained':True,'historical130FirstPassMapRetained':True}
for f in['v53/'+report]+['v53/research/liuyao-foundation-span/'+n for n in['WORK_STATE.json','SOURCE_MANIFEST.json','MANUAL_READINGS.json','B02_CURRENT_UNITS.json','FOUNDATIONAL_CONTEXTS.json','PRINTED_DIAGRAMS.json','SOURCE_ANOMALIES.json','MOTION_FIXTURES.json','PROMOTION_IDENTITIES.json','motion-reference.mjs','diagram-reference.mjs']]+['v53/qa/liuyao-foundation-span/'+n for n in['RESULTS.json','SOURCE_RESULTS.json','DIAGRAM_COMPARISON.json']]:
 if f not in entry['currentEvidence']:entry['currentEvidence'].append(f)
d['latestFollowup']=report+': '+step;d['latestAcquisitionCounts']={'scope':report,'newHTTPRequests':0,'newOriginalContainers':0,'newViewedSourcePositionsThisTurn':0,'retainedPositionsReviewed':28,'sourceAnomalyCropsViewed':3,'nativeMotionCropViewed':1,'firstPassSpansAddedToPackage':7,'printedDiagrams':64,'printedLineRows':384,'sourceMismatchesRetained':3,'wholeWorksApplied':0}
d['counts']['newDownloadsThisScope']=0;d['counts']['newDownloadsThisScopeBasis']='28retainedpositions21–48reviewed;3QAderivedpages/4viewedcrops/2pixelreproductions.0HTTP/newpositions/containers/independentwitness.137firstpassunitsnotfullapplication.'
assert d['counts']['catalogueRecords']==40 and d['counts']['wholeWorkApplied']==0;write(p,d)
note='Mốc Dịch — Bảy mục nền và bảng64đồ quẻ,28/10/2026: `'+report+'`. '+step+'\n\n'
for p in[w/'PROJECT_RESEARCH_STATE.md',r/'NEXT_STEPS.md',r/'research/library-current/COVERAGE.md']:
 t=p.read_text(encoding='utf-8-sig')
 if not t.startswith(note):p.write_text(note+t,encoding='utf-8')
p=w/'PENDING_RESEARCH_STATE.json';d=read(p);d.update(date='2026-10-28',status='B02-foundation-span-and-full-conditions-active',workDirectory='v53/research/liuyao-foundation-span',currentWorkState='v53/research/liuyao-foundation-span/WORK_STATE.json',latestReport='v53/'+report,next=nexts,consumerChanged=False,wholeCatalogueCompleted=False);write(p,d)
print('Recorded7foundation spans,64printed diagrams,3source mismatches andexplicit3/6lineboundary;fullconditions andall4domainsremainactive.')
