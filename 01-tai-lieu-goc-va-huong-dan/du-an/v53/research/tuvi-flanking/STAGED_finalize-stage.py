from pathlib import Path
from hashlib import sha256
import json
w=Path.cwd();b=w/'tmp/tuvi-minor-stars-staging';read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));write=lambda n,x:(b/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
summary='Tửvi T01:18ảnhJPEGcơquan mới31–48/18HTTP200/TLS/header/SHA đãxem,3cropnativekhớppixel. Quyển1hếtở38,quyển2bắtđầu39,khôngnhầm36làcuối.48vịtríđầuđọcđầuliêntục+16vịtrícũrời=64vịtrílưu/65chưa trongitem129;khôngphải áp hếtquyển1. Trích4ngữcảnhvề不可一例而斷,日月前後二宮夾命,昌曲亦如之vàtiêuđềkhác;API2cặpgiápchỉkiểmhìnhhọc,táchcunglâncận/cùngcung/tamhợp/đối,giữchưa rõphạmvi不逢空劫羊殺/miếuhãm/vậnhạn.7kiểmcơsở3456hìnhhọc/48khớp,144HHC+144iztrothật/576tọađộ/288ngữcảnh,4XươngKhúcgiáp/0NhậtNguyệttrongmẫungàyâm15. Tìmgiớihạnthêm165HHCkhungkhácngày/2iztrocho2caNhậtNguyệtgiápđềungàyâm2/chiMệnh未haihìnhhọcgiốngnhau,khôngphảivídụlịchsửhay2dạngđộclập. Tổngmớilượt309HHC/146iztro,580tọađộđốithamchiếu;khôngchạylại144cađãđạt. Khớpgiápkhôngthànhkhớptoàncách/cáthung;webnguyênbyte,toànkhoactive.'
nexts=['Tiếp ảnh49vàbảnđồtoànquyển2;sáuquyểntrongmục lụcchưaphảisáubodyitem上. Ma trậnitem129hiện64đãlưu/65chưa:49–73,82,84,86,93–129.1–48đãđọcđầu;khônglặptải/kiểmđãđạt.', 'Khai thác các điều kiện đầy đủ trongphụtinh31–38và骨髓賦39trởđi:不逢空劫羊殺chưarõphạmvicung/hiệulực;星格旺陷/三合/吉化/thânmệnh/vậnhạn chưaadapter,khôngtựchohìnhhọcgiápthànhcáthung. Tách phép夾với三方/拱/同宮/對照 vàcácgiọngvăn,cáthunglịch sửkhôngthànhdựđoánđờithực.', 'Giữ14profile/15giọnghànhbảntrước,khôngsửaLiêmTrinh木thànhtheokỳvọng hoặcgộp氣體.火鈴星TýNgọ/童限đuôichữ/khởihạn/CanhNhâm tiếpđộclậpđúngtruyềnbản,khiđủnguồn.', 'LuânphiênBáttự48chachưaliênkết/mọitiềnđềphụ,Nhàởgiao môn/đổi tượng/720ôtháng,DịchB02/B03/MaiHoa. Mọi nghiêncứu/QA ngoàisite,KiếnLộcUIchờbrowserQA,khôngxuấtbản/toànkhocònactive.']
req=read(b/'WINDOWS_TRUST_REQUESTS.json');manifest=w/'v53/research/fortune-followup/official-manifest.json'
write('SOURCE_MANIFEST.json',dict(date='2026-10-28',institution='National Archives of Japan',item='https://www.digital.archives.go.jp/item/4468520',manifestFile=manifest.relative_to(w).as_posix(),manifestSHA256=sha256(manifest.read_bytes()).hexdigest(),images=req['records'],kind='Institution-served2200JPEGderivatives,notoriginalJP2',originalJP2BodiesAcquired=0,previousScope='v53/research/tuvi-star-offices/SOURCE_MANIFEST.json',previousScopeImagesNotNewDownloads=30,editionYearEstablished=False))
inv=read(w/'v53/research/tuvi-star-offices/CURRENT_CANVAS_INVENTORY.json');new={x['canvas']:x for x in req['records']}
for x in inv['records']:
 x['newFirstPassReadThisScope']=x['canvas']in new
 for y in x['retainedDerivatives']:y['newThisScope']=False
 if x['canvas']in new:
  z=new[x['canvas']];x['retainedDerivatives']=[dict(file='v53/research/tuvi-flanking/'+z['file'],sha256=z['sha256'],newThisScope=True)]
inv['counts']=dict(manifestCanvases=129,newInstitutionJPEGBodies=18,previousPositionDerivatives=46,distinctRetainedPositions=64,positionsWithoutRetainedDerivativeInThisInventory=65,newFirstPassPositions=18,continuousFirstPassPositionsIncludingPrior=48)
inv['scope']='Item129positions:64retained,including48continuousfirst-passpositions1–48and16oldnoncontiguousretainedpositionsnotnewreadings;notallconditionsorwholeworkapplied.';assert sum(bool(x['retainedDerivatives'])for x in inv['records'])==64;write('CURRENT_CANVAS_INVENTORY.json',inv)
write('SOURCE_DISPOSITIONS.json',dict(date='2026-10-28',units=[dict(title=t,startCanvas=a,endCanvas=z,status='first-pass-context-only',wholeUnitApplied=False)for t,a,z in [('天魁天鉞/祿存/天馬',31,33),('化祿化權化科化忌',33,34),('擎羊陀羅及總論',34,35),('火星鈴星及四星總論',35,36),('天空地劫',36,36),('天傷天使天刑天姚',37,38),('天哭天虛',38,38),('斗數骨髓賦註解',39,None)]],juanBoundary=dict(juan1LastTextCanvas=38,juan2TitleAndOpeningCanvas=39),selectedGeometriesApplied=2,sourceExclusionScopeResolved=False,wholeJuan1Applied=False,wholeJuan2Applied=False,wholeBookApplied=False))
state=read(b/'WORK_STATE.json');state.update(status='eighteen-images-two-flanking-geometries-and-real-positive-contexts-verified-full-patterns-open',sourceDirectory='v53/research/tuvi-flanking',latestReport='v53/TUVI_FLANKING_REPORT.md',completedStep=summary,next=nexts,nativeCropsViewedPixelMatched=3,selectedSourceReadings=4,completeRuntimeChecks=7,knownGeometryContexts=3456,knownGeometryMatches=48,actualHHCTuviCalls=309,actualIztroNatalCalls=146,baseHHCTuviCalls=144,baseIztroCalls=144,targetedSearchHHCCalls=165,targetedPositiveIztroCalls=2,matchedStarBranchCoordinates=580,sourceFullPatternsApplied=False,sourceOutcomesValidated=False);write('WORK_STATE.json',state)
report='''# Tử vi: phép hai sao giáp Mệnh và các điều kiện chưa xác lập

Ngày28/10/2026. '''+summary+'''

## Nguồn

18JPEG2200×1659 mới từhttps://www.digital.archives.go.jp/item/4468520,URLđúngmanifest đãgiữ,18HTTP200/header/SHA256vàxáctrựcchứngthưWindowschuẩn.0bỏTLS/JP2gốc/nguồnbảninđộclậpmới. Đây làdẫnxuấtbytecơquanđãlưu,hashkhôngphảichữkýpublisher.1–30củabảntrướcnguyênbyte,khôngtảilại;16vịtrícũrời74–92chỉliênkếtđộphủlưu,khôngđếmđọc mớilượtnày. Ba cropnativekhớppixel/đãxem,khôngOCR/resample.

31–38kếtphụtinh:魁鉞/祿存/天馬,四化luận,văn羊陀/火鈴/空劫/天傷天使/天刑天姚/哭虛.36vẫncuộn1;38tráicókhungtrống,sau39tráimở卷之二/斗數骨髓賦註解.39–48đọcđầucácchúcúgiải,còntiếptừ49. Danh mụcvàranhkhôngđồngnghĩachépđầyđủtừngchữ/mãhóahếttiềnđề. Tuyênbốquyểncònmở.

## Chức năng và kiểm chứng

MANUAL_READINGSgiữ4ngữcảnh:不可一例而斷,日月trướcsauhaicung夾命kèmbấtphùng空劫羊殺,昌曲亦如之,tiêuđềkhácvề夾空夾劫/羊陀. APIinspectSourceFlankingbuộcnguồnđặttên,neocungMệnhkhaitườngminh,chínhxác2sao củacặpnguồn,chihoặcnull. Môhìnhbiêntậpchu kỳ12cung/haicunglâncận±1giữtáchcùngcung,đốidiện,tamhợp. Cùnghaisaomộtcunglâncậnkhôngđủhaiphía;khôngbiếtneogiữnull;biếtmộtsaongoàilâncậnđủbácbỏhìnhhọc dùsaokianull. KhôngsuycungThân từchữ身命hoặcphạmvi不逢;khôngcothiếudữliệulàđủđiềukiện.

7kiểmcơsởđạt1lượt:byte18ảnh,mệnhđề/phạmvikhác,3456tổhợphìnhhọcđãbiếtcủa2cặp/48khớp,null/đầuvào,144HHC+144iztrothật/576tọađộ/288ngữcảnh,lỗimấtđiềukiệnhoặccorruptbảntrảvề,vàwebnguyênbyte. Mẫunămâm1984/ngày15/12tháng/12giờ/hai giới xen kẽ/UTC+8:4XươngKhúcgiápMệnh,0NhậtNguyệt. KhônggọilàđãcócaNhậtNguyệtdươngtínhtừ144mẫu.

Do nhánhNhậtNguyệtchưacócadươngtínhthật,scriptđộclậptìmgiớihạncácngàyđượckhaitrongTARGETED_POSITIVE_RESULTS.165lờiHHCtìmra2ngữcảnhngàyâm2tháng1giờMùivàtháng2giờThân/năm1984;đềuneo未,TháiDương申/TháiÂm午.2iztrothậtđối4tọađộvàneokhớp. Haingữcảnhkhácđầuvàonhưngcùnghìnhhọc,khôngphải2hìnhdạngđộclập/vídụlịchsử;khôngchạyhếtmiềntìmkiếm,chỉdừngsau2đúngnhưkhaitrước,khôngchạylại144ca. Tổnglượt309HHC/146iztro,580tọađộđốithamchiếu;144khungnềnkhôngđượctínhthành288lálịchHHC. Khớpenginechỉkiểmtọađộ,môhìnhhìnhhọckhôngchứngminhcáthung/phẩmtrật/sứckhỏe/tàivận.

Mọi kếtquả fullSourceConditionsMatched vàpracticalOutcomegiữnull,kểcảhìnhhọcđúng. Khôngcófullpattern/outcomeđượcxácminh. Nguồnchưakhépphạmvi不逢空劫羊殺/星格/旺陷/三合/吉化/khungvậnhạn,khôngđưaquytắcchưađủvàogiao diện.

## Tiếp tục

'''+ '\n\n'.join(nexts)+'\n\nHTMLđộclập/site/ZIPwebnguyênbyte,nghiêncứu/nguồn/QAngoàisite. Giữsnapshot4794tệp/2692579507bytebảntrướcởarchives/v53-before-tuvi-flanking;toànkhoactive,0tácphẩmápdụnghết.\n'
(b/'REPORT.md').write_text(report,encoding='utf-8')
print('Prepared18sourcepositions/twoflankingAPIs/7basechecksplus2positivecontexts;309HHC146iztro,580comparedstarcoordinates.')
