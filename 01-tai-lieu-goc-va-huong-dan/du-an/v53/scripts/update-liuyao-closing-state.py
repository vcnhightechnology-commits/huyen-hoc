from pathlib import Path
import json
r=Path(__file__).resolve().parent.parent;w=r.parent;b=r/'research/liuyao-closing-context';q=r/'qa/liuyao-closing-context'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
report='LIUYAO_CLOSING_CONTEXT_REPORT.md'
step=('B02:tiếpnhận26vịtrí325–350/20khoảng83–102đãkiểmtrước,rồiđọcmới44vịtrí351–394/28khoảng103–130. Tổng70vịtríđưavàogói=65nộidung+5lákếtquyển/quảngcáo/ấn;nhịpnày44mới=40nộidung+4lá391–394,khônggọi70là70trangmới. '
 'Map137/130khoảngđọcđầu/7nềnmộtphần/0chỉđềmục/0áphết;chưađọctừngchữ/toànbộđiềukiện. 8kiểmmớiđạt/2HHCthật乾→小畜1→9,sáunhãnchi-Lụcthân/Thế6Ứng3/午官→未父khớp;13ngữcảnhnhàở/26cathiếuphạmvi,giữthânthuộc/nhà/thờiđiểm/nơichốnriêng. '
 '6kiểmhànhnhânkếthừa/2HHC旅→艮đãđạt,khôngchạylạiđểtăngsố;有病334giữýnghĩalỗicấutrúcDụng,khôngsuybệnhngườithật. 70ảnhSHA/6QA/2cropnative/3táirendermới+2kếthừa/90tệptiếpnhậnđúngbyte;haimodulechỉđổiimport. '
 'Đọctrựctiếpcuốnsách393ghi民國14tháng11出版/發行(năm1925),bổsungchứngcứngàyinriêngvớilờitựa1925vàấn394. GiữTOC106賣宅/body賃宅,110歸宅/body新宅;chữđề100chưaphânđịnh. '
 '0HTTP/PDFgốcmới/nhânchứngmới. Khôngthànhsơđồnhàthực/tọađộđịađiểm/đàosâu/khuyếnnghịxâydựng/ydược/pháplý/kếtquảgiađình. HTML/site/ZIPwebnguyênbyte,toànkhoactive.')
nexts=[
 'B02:137đơnvịhiệncó130khoảngđọcđầuvà7nềnmộtphần;khôngcònhàngchỉđềmụcnhưng0đơnvịđượctuyênbốáptrọn. Cầnđịnhvị/đọcđủkhoảng7mục1–7(八卦/卦象圖/八宮/渾天甲子/六親/世應/動變),rồilàmtiềnđề/phảnvídụ/tầnggiọngnguồntheobacklog,khônggọihếtB02hoặchếtkho.',
 'Khônglặp70ảnh/13ngữcảnhnhà/26caunknown/2fixtureHHCnếunguồnlogicgiữ. 17nhómngữcảnhcuối/13phépchiếuvà2câuhỏihànhnhânchưafullcompiler. Quyướcvượngsuy/飛伏/應期/合化制/chọnDụng/ưu tiêncònmở. Thânmệnh/Tài/giađình/nhà/tưcáchngườihỏiphảitáchrõ.',
 'Chữđề100病/痘giữchưaphânđịnh;TOC106賣宅vsbody賃宅,110歸宅vs新宅làkhácnguồnkhôngsửangầm. Colophon393in民國14tháng11出版/發行;ngàykhôngghi,lịchthángkhôngtựđổiGregorian. Bảncũnóichỉchắclờitựađượcgiữlịchsử;394chỉấn.',
 'Các lĩnhvựckhácvẫnactive:Tửvi童限/火鈴/CanhNhâm/khởihạn;BátTự47ngữcảnhDươngNhận/9cáchkhác/chuẩnvượngsuy;NhàởPhiTinh/lịch/Bắcthực;B03/MaiHoa/chữmở. BrowserUIvôhiệuhóa,khôngvượtsetting;nguồn/corpus/suyluận/QAngoàisite,khôngxuấtbản. Danhmục40/whole0.'
]
write(b/'WORK_STATE.json',{'date':'2026-10-28','status':'closing-first-pass-spans-and-explicit-house-traveler-contexts-verified-full-conditions-active','catalogueID':'B02','latestReport':'v53/'+report,'completedStep':step,
 'closingSummary':read(q/'CLOSING_RESULTS.json')['summary'],'inheritedTravelerSummary':read(q/'TRAVELER_RESULTS.json')['summary'],'sourceVerification':read(q/'SOURCE_RESULTS.json'),
 'sourceUnitMap':'v53/research/liuyao-closing-context/B02_CURRENT_UNITS.json','next':nexts,'newClosingChecks':8,'inheritedTravelerChecks':6,
 'fullConditionalRulesEncoded':False,'allImageCharactersCollated':False,'sourceOutcomesValidated':False,'consumerChanged':False,'wholeCatalogueCompleted':False,
 'releaseVerification':'v53/qa/liuyao-closing-context/RELEASE_RESULTS.json;expecteduntilfinal--no-writeverification succeeds'})
d=read(w/'EXHAUSTIVE_WORK_STATE.json');d['date']='2026-10-28';d['currentWork'].update(catalogueID='B02',relatedCatalogueIDs=['B02'],work='增刪卜易 — 卷末、家宅問意與來源年款',
 reason='Finish first reading of previously heading-only closing chapters while preserving incomplete foundational/conditional work and source-specific question boundaries.',
 sourceDirectory='v53/research/liuyao-closing-context',currentStep=step,latestResearchReport='v53/'+report,functionalBacklog='v53/research/liuyao-closing-context/WORK_STATE.json',
 internalHouseContext='v53/research/liuyao-closing-context/house-context.mjs',internalTravelerContext='v53/research/liuyao-closing-context/traveler-context.mjs',
 currentB02UnitMap='v53/research/liuyao-closing-context/B02_CURRENT_UNITS.json',currentTOC='v53/research/liuyao-closing-context/B02_CURRENT_UNITS.json',
 sourceLimits='137units:130first-passspans+7partialfoundations/0wholeapplied.70positionspromoted,44newthisturn/26priorstaging.13house/2travelerquestioncontextsnotfullconditionalcompiler.393datedcolophonnewlyread,notindependentwitness.',
 nextSourceLead={'sourceID':'B02-foundations1-7-full-span-reading','status':'partial-foundational-span-and-full-conditions-still-open','file':'v53/research/liuyao-closing-context/B02_CURRENT_UNITS.json','remaining':' '.join(nexts)})
d['inProgressScope']='v53/research/liuyao-closing-context/WORK_STATE.json';d['subsequentPriority'][0]=' '.join(nexts)
for p in[w/'EXHAUSTIVE_WORK_STATE.json',r/'research/EXHAUSTIVE_WORK_STATE.json']:write(p,d)
p=r/'research/full-study/WORK_STATE.json';d=read(p);d['date']='2026-10-28';d['latestResearchReport']=report;d['exhaustiveNext']=' '.join(nexts);item=next(x for x in d['items']if x['id']=='yi')
if step not in item['completed']:item['completed'].append(step)
if ' '.join(nexts)not in item['remaining']:item['remaining'].append(' '.join(nexts))
item['latestScope']='../liuyao-closing-context/WORK_STATE.json';item['nextFile']='../liuyao-closing-context/B02_CURRENT_UNITS.json';write(p,d)
p=r/'research/library-current/COVERAGE.json';d=read(p);d['date']='2026-10-28';entry=next(x for x in d['catalogue']if x['id']=='B02');entry['latestClosingScope']=step
entry['currentSourceUnitCounts']={'registeredUnits':137,'regularNumberedUnits':130,'supplements':7,'firstPassSpans':130,'headingOnly':0,'partialFoundation':7,'otherPartial':0,'wholeUnitsApplied':0,'historical136UnitMapsRetained':True}
entry['latestColophonEvidence']={'file':'v53/research/liuyao-closing-context/COLOPHON_AUDIT.json','sourcePDFPage':393,'literalPublicationDate':'中華民國十四年十一月出版','literalDistributionDate':'中華民國十四年十一月發行','commonEraYear':1925,'printedMonth':11,'dayUnstated':True,'independentNewWitness':False,'sourceEmended':False}
for f in['v53/'+report]+['v53/research/liuyao-closing-context/'+n for n in['WORK_STATE.json','SOURCE_MANIFEST.json','TRAVELER_MANUAL_READINGS.json','CLOSING_MANUAL_READINGS.json','B02_CURRENT_UNITS.json','HOUSE_CONTEXTS.json','TRAVELER_CONTEXT.json','COLOPHON_AUDIT.json','BOUNDED_CLAUSES.json','PROMOTION_IDENTITIES.json','house-context.mjs','traveler-context.mjs']]+['v53/qa/liuyao-closing-context/'+n for n in['CLOSING_RESULTS.json','TRAVELER_RESULTS.json','SOURCE_RESULTS.json']]:
 if f not in entry['currentEvidence']:entry['currentEvidence'].append(f)
d['latestFollowup']=report+': '+step;d['latestAcquisitionCounts']={'scope':report,'newHTTPRequests':0,'newOriginalContainers':0,'newViewedSourcePositionsThisTurn':44,'newBodyPositionsThisTurn':40,'currentTurnNonRuleLeaves':4,'priorStagingPositionsPromoted':26,'uniquePositionsPromoted':70,'expandedPriorTOCPositions':2,'sourceQARendersPromoted':6,'firstPassSpansAddedToPackage':48,'wholeWorksApplied':0}
d['counts']['newDownloadsThisScope']=0;d['counts']['newDownloadsThisScopeBasis']='RetainedPDFunchanged:44newviewedpositions+26priorstagingpositionspromoted,not70newdownloads.6QAderivatives/2priorTOCrereads,0HTTP/container/independentwitness.'
assert d['counts']['catalogueRecords']==40 and d['counts']['wholeWorkApplied']==0;write(p,d)
note='Mốc Dịch — Nhà ở, hành nhân và niên khoản cuối sách, 28/10/2026: `'+report+'`. '+step+'\n\n'
for p in[w/'PROJECT_RESEARCH_STATE.md',r/'NEXT_STEPS.md',r/'research/library-current/COVERAGE.md']:
 text=p.read_text(encoding='utf-8-sig')
 if not text.startswith(note):p.write_text(note+text,encoding='utf-8')
p=w/'PENDING_RESEARCH_STATE.json';d=read(p);d.update(date='2026-10-28',status='Liuyao-closing-context-current-scope-active',workDirectory='v53/research/liuyao-closing-context',currentWorkState='v53/research/liuyao-closing-context/WORK_STATE.json',latestReport='v53/'+report,next=nexts,consumerChanged=False,wholeCatalogueCompleted=False)
if'inProgressStaging'in d:d['previousStaging']={**d.pop('inProgressStaging'),'status':'promoted-to-v53-liuyao-closing-context-full-conditions-active'}
write(p,d)
print('Recorded closing source spans,question boundaries and datedcolophon;sevenfoundations andfullconditionalwork remainactive.')
