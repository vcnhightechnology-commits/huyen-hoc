from pathlib import Path
import json
r=Path(__file__).resolve().parent.parent;w=r.parent;b=r/'research/liuyao-commodity-boundary';q=r/'qa/liuyao-commodity-boundary'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
report='LIUYAO_COMMODITY_BOUNDARY_REPORT.md'
step=('B02:đọc24vịtríPDF301–324,khép16khoảng68–82gồm81lặp;chương83mớiđầu324,tiếp325. '
 'ĐốiTOC17vàbody317–318pháthiệnmapcũbỏhônnhân82vàgắnnhầmhànhhiểm81vào82:giữmapcũ136,thêm81-supp-a/sửa82婚姻thành137đơnvị130sốthường+7phụ. '
 'Sửanhãnlàmviệc75在→往;giữkhácTOC買貨賣貨/body囤貨賣貨73. Khôngsửasáchhoặcweb. '
 'Map137/82khoảngđọcđầu/47chỉđềmục/7nềnmộtphần/1mở83/0áphết. Bộriênggiữphảnbiện野鶴đốivớigánngũhành→hànghóa,cầnchỉrõmặthàng;giữnhãn翠毛khôngtựđổi翡翠. '
 '5kiểmđạt/1HHCthật旅56,sáunhãnchi-Lụcthân/Thế1Ứng4/haiTàiKimkhớp. 24ảnhSHA/3QAđãxem/2táirenderkhớppixel/33tệptiếpnhậnđúngbyte,modulechỉđổiimport. '
 '0HTTP/PDFmới/nhânchứngmới;khôngsuyhànghóa/giá/lãi/quyếtđịnhmua bánhoặckếtquảhônnhân. HTML/site/ZIPwebnguyênbyte,toànkhoactive.')
nexts=[
 'B02tiếp83từPDF325;đãđọc324chỉđầumục. Maphiệnhành137/82khoảngđọcđầu/47chỉđềmục/7nềnmộtphần/1mở83/0áphết. 137làđơnvịtrongmộtsách,khôngphảisốsách;fixedcatalogue40khôngđổi. KiểmphầnTOCcònlạitheobodykhigặpbấtđồng,khôngtựtin136mapcũlàđủ.',
 'Khônglặp24ảnh/旅56/5kiểmnguồnhànghóanếunguồnlogicgiữ.16khoảngđọcđầu68–82chưabiên dịchhếtđiềukiện;thânthuộc/hônnhân,giọngnguồn/ưu tiên/vượngsuy/thờivịđểriêng.2bảnghànghóacũchỉtríchchọnvàbịtácgiảphê,khôngdựngbộrecommendation/giá/lãi.',
 '19ngữcảnhthi/chứcvụtrước;nămýđịnhđơnthỉnhchưamãhóa;Tửvi童限/ranhnăm/selector1sao/火鈴星/CanhNhâm/khởihạn;DươngNhận47ngữcảnh/9cáchkhác;NhàởPhiTinh/lịch/Bắcthực,B03/MaiHoavẫnmở. Khôngretryendpoint403đểnéhạnchế.',
 'ỨngviênUIKiếnLộcvẫnriêngdobrowservôhiệuhóa,khôngvượtsetting. Nguồn/corpus/suyluận/QAngoàisite,khôngxuấtbản. Danhmục40/whole0,bốnlĩnhvựcactive;khôngtuyênbốhếtkho.'
]
write(b/'WORK_STATE.json',{'date':'2026-10-28','status':'corrected-working-source-map-and-commodity-inference-boundary-verified-full-conditions-active','catalogueID':'B02','latestReport':'v53/'+report,'completedStep':step,
 'summary':read(q/'RESULTS.json')['summary'],'sourceVerification':read(q/'SOURCE_RESULTS.json'),'sourceUnitMap':'v53/research/liuyao-commodity-boundary/B02_CURRENT_UNITS.json','next':nexts,
 'commodityInferenceRejectedByNamedAuthor':True,'sourceEmended':False,'fullConditionalRulesEncoded':False,'sourceOutcomesValidated':False,'consumerChanged':False,'wholeCatalogueCompleted':False,
 'releaseVerification':'v53/qa/liuyao-commodity-boundary/RELEASE_RESULTS.json;expected until final --no-write succeeds'})
d=read(w/'EXHAUSTIVE_WORK_STATE.json');d['date']='2026-10-28';d['currentWork'].update(catalogueID='B02',relatedCatalogueIDs=['B02'],work='增刪卜易 — 財貨問意、舊法反證與目錄缺漏',
 reason='Repair a source-unit omission and prevent automatic commodity inference where the named author rejects that very heuristic.',
 sourceDirectory='v53/research/liuyao-commodity-boundary',currentStep=step,latestResearchReport='v53/'+report,functionalBacklog='v53/research/liuyao-commodity-boundary/WORK_STATE.json',
 internalCommodityBoundary='v53/research/liuyao-commodity-boundary/commodity-boundary.mjs',currentB02UnitMap='v53/research/liuyao-commodity-boundary/B02_CURRENT_UNITS.json',currentTOC='v53/research/liuyao-commodity-boundary/B02_CURRENT_UNITS.json',
 sourceLimits='24newreadpositions/16firstpassspans;workingTOC137afterprovenomissionrepair,notwholeconditionalapplication.Only2selectedquotedcommoditymaps,explicitlyrejectedbynamedauthor;chapter83partial.',
 nextSourceLead={'sourceID':'B02-ch083-continue','status':'retained-source-reading-available','file':'v53/research/liuyao-commodity-boundary/B02_CURRENT_UNITS.json','remaining':' '.join(nexts)})
d['inProgressScope']='v53/research/liuyao-commodity-boundary/WORK_STATE.json';d['subsequentPriority'][0]=' '.join(nexts)
for p in[w/'EXHAUSTIVE_WORK_STATE.json',r/'research/EXHAUSTIVE_WORK_STATE.json']:write(p,d)
p=r/'research/full-study/WORK_STATE.json';d=read(p);d['date']='2026-10-28';d['latestResearchReport']=report;d['exhaustiveNext']=' '.join(nexts);item=next(x for x in d['items']if x['id']=='yi')
if step not in item['completed']:item['completed'].append(step)
if ' '.join(nexts)not in item['remaining']:item['remaining'].append(' '.join(nexts))
item['latestScope']='../liuyao-commodity-boundary/WORK_STATE.json';item['nextFile']='../liuyao-commodity-boundary/B02_CURRENT_UNITS.json';write(p,d)
p=r/'research/library-current/COVERAGE.json';d=read(p);d['date']='2026-10-28';entry=next(x for x in d['catalogue']if x['id']=='B02');entry['latestCommodityScope']=step
entry['currentSourceUnitCounts']={'registeredUnits':137,'regularNumberedUnits':130,'supplements':7,'firstPassSpans':82,'headingOnly':47,'partialFoundation':7,'otherPartial':1,'wholeUnitsApplied':0,'historical136UnitMapsRetained':True}
for f in['v53/'+report]+['v53/research/liuyao-commodity-boundary/'+n for n in['WORK_STATE.json','SOURCE_MANIFEST.json','MANUAL_READINGS.json','B02_CURRENT_UNITS.json','NUMBERING_AUDIT.json','COMMODITY_BOUNDARY.json','PROMOTION_IDENTITIES.json','commodity-boundary.mjs']]+['v53/qa/liuyao-commodity-boundary/'+n for n in['RESULTS.json','SOURCE_RESULTS.json']]:
 if f not in entry['currentEvidence']:entry['currentEvidence'].append(f)
d['latestFollowup']=report+': '+step;d['latestAcquisitionCounts']={'scope':report,'newHTTPRequests':0,'newOriginalContainers':0,'newViewedPDFPositions':24,'expandedPriorTOCPositions':1,'highResolutionQA':3,'firstPassSpansAdded':16,'workingRegisteredUnitsCorrectedFrom136To137':True,'wholeWorksApplied':0}
d['counts']['newDownloadsThisScope']=0;d['counts']['newDownloadsThisScopeBasis']='RetainedPDF:24newviewedpositions/TOC17reread/3QArenders.0HTTP/neworiginalcontainer/independentwitness. Sourceunitmap137notnewbookcount.'
assert d['counts']['catalogueRecords']==40 and d['counts']['wholeWorkApplied']==0;write(p,d)
note='Mốc Dịch — Giới hạn suy hàng hóa và sửa ma trận chương, 28/10/2026: `'+report+'`. '+step+'\n\n'
for p in[w/'PROJECT_RESEARCH_STATE.md',r/'NEXT_STEPS.md',r/'research/library-current/COVERAGE.md']:
 text=p.read_text(encoding='utf-8-sig')
 if not text.startswith(note):p.write_text(note+text,encoding='utf-8')
p=w/'PENDING_RESEARCH_STATE.json';d=read(p);d.update(date='2026-10-28',status='Liuyao-commodity-boundary-current-scope-active',workDirectory='v53/research/liuyao-commodity-boundary',currentWorkState='v53/research/liuyao-commodity-boundary/WORK_STATE.json',latestReport='v53/'+report,next=nexts,consumerChanged=False,wholeCatalogueCompleted=False)
d['previousStaging']={'directory':'tmp/liuyao-b02-wealth-staging','status':'promoted-reference-import-only-relocated','newViewedPositions':24,'firstPassSpansAdded':16,'next':'B02chapter83PDF325;fullconditionsandallfourdomainsactive'}
write(p,d)
print('Recorded source-unit omission repair and explicit commodity-inference rejection;wholebook remains active.')
