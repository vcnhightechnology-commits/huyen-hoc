from pathlib import Path
import json
root=Path(__file__).resolve().parent.parent;workspace=root.parent;base=root/'research/liuyao-b03-volume3'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
report='LIUYAO_B03_VOLUME3_REPORT.md';a=read(base/'ACQUISITION.json')
step=('B03sáchđóng2 đãtảibyte41224832/SHA c1e10273…/49trang,APIrevision754088942+PDF/2body200TLS. '
 'PDF2–29quyển3 đọc lầnđầu toànkhoảng:18luận+14đoạnbiện,32ảnh kểbìa1/v4đọcgiớihạn30–32;27mệnhđề giới hạn,khôngdung nguồnnhưlệnh. '
 'Bộ riêng táchphảnngâm phươngvịquái/chi hàobiến vàphụcngâmchitrùng;8tiến/8thoái.11kiểm/24HHCthật cho12cặpin,4096cặpnộibộ/12288chú:960phươngvị/252xungchi/252phục,1148cặpkhácgiữahailớpphảnngâm,512tiến512thoái. '
 'Giữ lờiB03phêB02/Phụcthần/thếthân/quáithân nhưlập trườngchưaphảiđồngthuận. HTML707411byte/site/ZIPweb/bảythamchiếutrướcgiữbyte. '
 'Chưa mọi mệnhđềv3/v4/tổngvượngsuy/chânkhông/chọnDụng/dựbáo;B02vẫn136/103/26,ngày52mở;toànkho chưa xong.')
nexts=['B03book2textualvolume4PDF33..48afterboundedincipit30..32;readactualending49beforeclaimingphysicalbookspancomplete.',
 'Compilefullconditionalpremises/strength/void/horizon/sourceexceptionsandcollatepolemicquotations;卦身and世身notmerged.',
 'B03remainingphysicalbooks3..6againstidentifiedgaps;B02remaining103heading-only/7partialfoundationunits,independentPDF52date-voidwitness.',
 'OtherMaiHoa/Bazi/Tuvi/Home/librarygapsremain;noallfour/wholeworkcompletionclaim.']
d=read(workspace/'EXHAUSTIVE_WORK_STATE.json');d['date']='2026-10-27';d['currentWork'].update(currentStep=step,latestResearchReport='v53/'+report,
 sourceDirectory='v53/research/liuyao-b03-volume3',internalB03LayerReference='v53/research/liuyao-b03-volume3/layer-reference.mjs',
 currentB03UnitMap='v53/research/liuyao-b03-volume3/VOLUME3_UNITS.json',functionalBacklog='v53/research/liuyao-b03-volume3/WORK_STATE.json')
d['currentWork']['sourceLimits']='B03physicalbooks1and2retainedandhashverified,notall6books/14textualvolumes;book2卷三first-passPDF2..29,卷四only30..32bounded. B02preface1925notverifiedprintdate;Wikisource卷01missing;Japan51canvasmanifest/5boundedspreadsnotcompleteindependenteditioncollation;NLCcatalogTLSfailuresretained;PDF52date-voidconflictandgenealogyopen.'
d['currentWork']['nextSourceLead']={'status':'downloaded-byte-verified-opening-read','sourceID':'B03-book2','file':'v53/research/liuyao-b03-volume3/'+a['file'],
 'sha256':a['sha256'],'bytes':a['bytes'],'sourceURL':a['commonsURL'],'remaining':'Book2PDF33..49unread;otherphysicalbooksnotacquired.'}
d['inProgressScope']='v53/research/liuyao-b03-volume3/WORK_STATE.json';d['subsequentPriority'][0]=' '.join(nexts)
for p in[workspace/'EXHAUSTIVE_WORK_STATE.json',root/'research/EXHAUSTIVE_WORK_STATE.json']:write(p,d)
write(base/'WORK_STATE.json',{'date':'2026-10-27','status':'private-three-layer-reference-complete-volume4-and-adjudication-active','sourceID':'B03-book2','relatedSourceID':'B02',
 'latestReport':'v53/'+report,'latestAcquisition':'ACQUISITION.json','privateReference':'layer-reference.mjs','unitMap':'VOLUME3_UNITS.json',
 'completedStep':step,'firstPassEighteenUnits':18,'firstPassPolemicUnits':14,'volume3RelevantSpanFirstPassRead':True,'allVolume3ClausesApplied':False,
 'newOriginalPDFs':1,'newRetainedHTTP200Bodies':2,'newLocalRenders':32,'manualPages':list(range(1,33)),'volume4BoundedPages':[30,31,32],
 'unreadPhysicalBook2Pages':list(range(33,50)),'next':nexts,'consumerChanged':False,'calendarAdapter':False,'overallStrengthModel':False,
 'functionalVoidAdjudication':False,'automaticUseGodSelection':False,'wholeBookApplied':False,'wholeCatalogueCompleted':False})
p=root/'research/full-study/WORK_STATE.json';d=read(p);d['latestResearchReport']=report;d['exhaustiveNext']='B03physicalbook2acquired49pages/41.2MB:卷三PDF2..29first-passcomplete32units,卷四only30..32bounded;continue33..49/fullpremisecompilation,polemiccollationandlaterbooks3..6. B02counts136/103/26unchanged;otherlibrarygapsremain.'
yi=next(x for x in d['items']if x['id']=='yi');entry='B03book2verified49pages/41224832bytes/c1e10273..APIrevision754088942:32newimages,卷三2..29first-pass18discussions14polemics,卷四30..32bounded. Private3layersdirectionalFanYin/changedbranchFanYin/branchFuYin+8advance8retreat;11checks24actualHHChex/4096privatepairs12288movingannotations/1148layer-presencedisagreements.27boundedclauses;historicalpolemicandmedicalclaimsnotinstructionsoroutcomeproof. Consumer/sevenpriorreferencesunchanged.'
if entry not in yi['completed']:yi['completed'].append(entry)
yi['latestScope']='../liuyao-b03-volume3/OPERATIONAL_CLAUSES.json'
yi['remaining']=[s for s in yi['remaining']if not s.startswith('LiuYaoB03:volume2spanread/')]
yi['remaining'].append('LiuYaoB03:book1full384lineannotations/prefaces/introductionnotcomplete;book2卷三spanreadbutallclausesnotcompiled,卷四33..49unread;books3..6unacquired. Fullstrength/functionalvoid/FanFupriority/卦身/世身/dateadapterunresolved. B02still103heading-onlyunits/PDF52date-voidconflict.')
write(p,d)
p=root/'research/library-current/COVERAGE.json';d=read(p);b=next(x for x in d['catalogue']if x['id']=='B03')
b['scope']='B03sáchđóng1/2giữbyte;quyển2bảnđồ64hình/chọnhiệnbiếntrướcPhục,quyển3(PDF2–29sách2)đọctoànkhoảng18luận14biện. Bộriêng táchphảnngâm phươngvị/xungchi/phụcngâmchi và8tiến8thoái. Chưa mọi mệnhđề/384chúhào/tiềntự/quyển4/cácsách3–6/hiệulực hoặc côngkhai.'
b['localPossession']=['Sáchđóng1PDF60trang/50191031byte/SHA5dcd7b50…;title1904đãđọcởphạmvinền,khôngtoàn14quyển. Cácrender/đọcgiớihạntừngphạmvilưuriêng;Wikisource卷01vẫnthiếu.',
 'Sáchđóng2PDF49trang/41224832byte/SHA'+a['sha256']+';APIrevision754088942+PDF/TLS/hashđối,PDF2in卷之三/十八論,PDF30bắtđầu卷之四. ChỉPDF1–32đãxem,33–49cònmở.']
b['latestLocalReadingScope']='Sáchđóng2:32render mới,quyển3đọclầnđầutoànkhoảng28trangnộidung+3đầuv4/bìa;27mệnhđề,11kiểm/24HHCthật/4096cặpnộibộ12288chú.1PDFmới2body200;chưađồngthuậngiữacácsáchhoặcdựbáo.'
files=['v53/'+report]+['v53/research/liuyao-b03-volume3/'+n for n in['ACQUISITION.json','REQUESTS.json','SOURCE_AUDIT.json','PDF_CONTAINER_CHECKS.json','MANUAL_READINGS.json','VOLUME3_UNITS.json','LAYER_TABLES.json','SOURCE_FIXTURES.json','OPERATIONAL_CLAUSES.json','layer-reference.mjs']]+['v53/qa/liuyao-b03-volume3/ENGINE_RESULTS.json']
for f in files:
 if f not in b['currentEvidence']:b['currentEvidence'].append(f)
d['latestFollowup']=report+':B03book2newPDF49pages,卷三first-pass18+14units/卷四incipitonly;11checks/24actualHHC/4096privatepairs.32newimages/2HTTP200;no sourceconsensus/strength/verdictpromotion,consumerunchanged/wholework0.'
d['latestAcquisitionCounts']={'scope':report,'originalPDFs':1,'retainedHTTP200Bodies':2,'newLocalRenders':32,'manualImageRecords':32,'volume3ContentPages':28,'boundedNextVolumePages':3,'coverPages':1,'fullBooksApplied':0};d['counts']['newDownloadsThisScope']=2
assert d['counts']['wholeWorkApplied']==0;write(p,d)
note=('Mốc B03–Luận3 27/10/2026: `'+report+'` tải sáchđóng2/49trang41224832byte/SHA c1e10273…/APIrevision754088942+PDF2body200TLS.32ảnhmới,quyển3/PDF2–29đọc lầnđầu toànkhoảng18luận14biện;v4chỉ30–32. '
 '27mệnhđềriêng/11kiểm24HHCthật;4096cặpnộibộ12288chú,960phảnngâmphươngvị/252xungchi/252phụcngâm,1148khácgiữahailớp,512tiến512thoái. '
 'LờiB03phêB02/cácsáchkhácgiữlậptrườngchưaphảiđồngthuận;HTML707411byte/site/ZIPweb/bảythamchiếutrướcgiữbyte. TiếpPDF33–49/mọimệnhđề/sách3–6;B02vẫn136/103/26,ngày52mở;toànkho chưa hoàn tất.\n\n')
for p in[workspace/'PROJECT_RESEARCH_STATE.md',root/'NEXT_STEPS.md',root/'research/library-current/COVERAGE.md']:
 s=p.read_text(encoding='utf-8-sig')
 if s.startswith('Mốc B03–Luận3 27/10/2026:'):s=s.split('\n\n',1)[1]
 p.write_text(note+s,encoding='utf-8')
print('Book2/volume3privateclassificationandfirst-passreadingrecorded;all-libraryworkremainsactive.')
