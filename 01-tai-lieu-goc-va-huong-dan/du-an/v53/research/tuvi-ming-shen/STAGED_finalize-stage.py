from pathlib import Path
from hashlib import sha256
import json
w=Path.cwd();b=w/'tmp/tuvi-juan2-staging';read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));write=lambda n,x:(b/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
summary='Tử vi T01: đã xem 25 ảnh JPEG mới49–73 từ cơ quan lưu trữ Nhật, 25HTTP200/TLS chuẩn/header/SHA; ba crop native khớp pixel. Quyển hai bắt đầu39 và kết phần nội dung ở73, quyển ba mở cùng73;73vị trí đầu đã đọc đầu liên tục,16vị trí cũ rời chỉ liên kết lưu giữ, tổng89/129vị trí có ảnh,40chưa. Trích sáu câu về an Mệnh–Thân: tháng từDần tiến, giờ từTý nghịch choMệnh/thuận choThân,ba ví dụ thángGiêng thường vàmột ví dụ thángGiêng nhuận giờDần. APIchỉ giải thángthường vàđúng ví dụ nhuậnin; chưa suy mọi thángnhuận hayđổi giờđồnghồ/lịch.7kiểm đạt1lượt,144HHC+144iztro2.6.2thật trênnămâm1985/ngày10/12tháng/12giờ,288tọađộMệnh–Thânkhớp. Chín nhãn giáp từảnh61giữ6夾貴/3夾敗;科權祿ba nhãnkhôngtựchọn2,劫空chưachốtaliasnguồn. Khôngchạylạibộgiápcũ hoặcđưađoáncáthungvàoweb;toànkhoactive.'
nexts=['Tiếp bản đồ quyển ba từ74 và các vị trí đã giữ; chỉ tải các khoảng thiếu82/84/86 và93–129, không lặp1–73 hoặc16ảnhcũ. Item129 hiện89vịtrí cóảnh/40chưa;đọc đầu không phải mã hóa hết từng điều kiện.', 'An Mệnh–Thân: giữ nguyên ví dụ閏正月生寅時ở73 và câu凡有閏月俱要依此為例. Chưa có cách ngoại suy tất cả tháng nhuận/ngày đầu/cuối từ câu này; đối tiếp quyểnba/nguồn độc lập, không ép chính sách hiện đại. Ba ví dụ thường/một ví dụ nhuận là khung khai báo, không tự gắn ngày lịch sử.', 'Quyển2từ39–73 đã đọc đầu các đoạn, chưa áp toàn bộ骨髓賦/女命/太微賦/補遺 vàcácbảng得地失陷/富貴貧賤. Tiếp từngmệnhđề đầyđủ,cungneovà旺陷/吉化/三方四正/大限小限,chưađưa lời giới/sức khỏe/nghèo giàu thành kết quả người dùng.', 'Danh sáchgiáp61có6nhãn thuận/3nhãn nghịch;科權祿khôngđồngnghĩahaibiên/劫空chưarõalias;giữnguyênphầnphụvề廟旺/吉星/化忌 vànhiềugiọng. Luânphiên48chaBáttự,Nhàởgiao môn/đổi tượng/720ôtháng,DịchB02/B03/MaiHoa. Nguồn/QA ngoàisite,UIKiếnLộcchờbrowserQA,khôngxuấtbản/toànkhochưahoàntất.']
req=read(b/'WINDOWS_TRUST_REQUESTS.json');manifest=w/'v53/research/fortune-followup/official-manifest.json';write('SOURCE_MANIFEST.json',dict(date='2026-10-28',institution='National Archives of Japan',item='https://www.digital.archives.go.jp/item/4468520',manifestFile=manifest.relative_to(w).as_posix(),manifestSHA256=sha256(manifest.read_bytes()).hexdigest(),images=req['records'],kind='Institution-served2200JPEGderivatives,notoriginalJP2',originalJP2BodiesAcquired=0,previousScope='v53/research/tuvi-flanking/SOURCE_MANIFEST.json',previousScopeImagesNotNewDownloads=18,editionYearEstablished=False))
# Correct the provisional first-pass note: the actual crop explicitly contains a leap example.
p=b/'FIRST_PASS_READINGS.json';f=read(p);x=next(x for x in f['records']if x['canvas']==73);x['provisionalNoteCorrection']='Initial note said leap handling not specified. Direct native crop shows a particular leap-first-month Yin-hour example and general 倣此 clause; general all-month mapping still unresolved.';write('FIRST_PASS_READINGS.json',f)
inv=read(w/'v53/research/tuvi-flanking/CURRENT_CANVAS_INVENTORY.json');new={x['canvas']:x for x in req['records']}
for x in inv['records']:
 x['newFirstPassReadThisScope']=x['canvas']in new
 for y in x['retainedDerivatives']:y['newThisScope']=False
 if x['canvas']in new:
  z=new[x['canvas']];x['retainedDerivatives']=[dict(file='v53/research/tuvi-ming-shen/'+z['file'],sha256=z['sha256'],newThisScope=True)]
inv['counts']=dict(manifestCanvases=129,newInstitutionJPEGBodies=25,previousPositionDerivatives=64,distinctRetainedPositions=89,positionsWithoutRetainedDerivativeInThisInventory=40,newFirstPassPositions=25,continuousFirstPassPositionsIncludingPrior=73);inv['scope']='Oneupperitem:89positionsretained,73continuousfirst-passpositions1–73and16oldnoncontiguouspositionsnotnewreads;notwholeworkorfullconditionsapplied.';assert sum(bool(x['retainedDerivatives'])for x in inv['records'])==89;write('CURRENT_CANVAS_INVENTORY.json',inv)
write('SOURCE_DISPOSITIONS.json',dict(date='2026-10-28',units=[dict(title=t,startCanvas=a,endCanvas=z,status='first-pass-context-only',wholeUnitApplied=False)for t,a,z in [('斗數骨髓賦註解 continuation',49,52),('女命骨髓賦註解',52,55),('太微賦註解',55,60),('補遺骨髓賦註解',60,61),('定富貴貧賤一十四等訣',61,67),('定富貴貧賤十等論',67,68),('十二宮諸星得地合格訣',68,69),('十二宮諸星失陷破格訣',69,70),('十二宮諸星得地富貴論',70,71),('十二宮諸星失陷貧賤論',71,71),('定富局/定貴局/定貧賤局/定雜局',71,73),('安身命例 opening',73,None)]],juanBoundary=dict(juan2LastTextCanvas=73,juan3TitleAndOpeningCanvas=73),selectedAlgorithm='Declared regular birthmonth/hour Ming/Shen + exact printed leap1Yin example',sourceGeneralLeapPolicyResolved=False,wholeJuan2Applied=False,wholeJuan3Applied=False,wholeBookApplied=False))
state=read(b/'WORK_STATE.json');state.update(status='twentyfive-images-and144-month-hour-source-ming-shen-contexts-verified-general-leap-open',sourceDirectory='v53/research/tuvi-ming-shen',latestReport='v53/TUVI_MING_SHEN_REPORT.md',completedStep=summary,next=nexts,nativeCropsViewedPixelMatched=3,selectedSourceReadings=6,printedRegularExamples=3,printedLeapSpecificExamples=1,completeRuntimeChecks=7,actualHHCTuviCalls=144,actualIztroNatalCalls=144,matchedSourceBranchCoordinates=288,newEngineCalls=288,sourceGeneralLeapPolicyResolved=False,wholeChapterApplied=False,sourceOutcomesValidated=False);write('WORK_STATE.json',state)
report='''# An Mệnh–Thân theo ảnh nguồn và giới hạn của ví dụ tháng nhuận

Ngày28/10/2026. '''+summary+'''

## Chứng cứ nguồn

25 ảnh JPEG2200×1659 tại https://www.digital.archives.go.jp/item/4468520, URL được suy đúng từ manifest đã giữ trước; mỗi body cóHTTP200,header,SHA-256 và xác thực chứng thư Windows chuẩn. Đây là dẫn xuất cơ quan phục vụ, không phải byte JP2gốc hoặc một bản in độc lập mới. Ba crop đã xem/khớp pixel, không OCR hay resample. Hash xác minh byte lưu cục bộ, không phải chữ ký publisher.

49–73 kết quyển hai và mở quyển ba ở trang trái73. FIRST_PASS_READINGS và SOURCE_DISPOSITIONS tách từng đoạn nữ mệnh/các phú/chú giải/danh sách cách/vượng hãm và các lời tiên đoán. Đã đọc đầu không đồng nghĩa từng chữ đã đối hết hoặc từng cách có đủ quy tắc tái lập. Những lời về sức khỏe, giới, phẩm trật, tình dục, nghèo giàu và tử vong là tuyên bố lịch sử của nguồn, không phải kết quả được xác minh. Ma trận89vị trí lưu/40chưa trên129canvas:73đầu liên tục mớiđọc đầu qua các lượt,16cũrời chỉliênkếtđộphủảnhlưu,khôngđếmđọc mới.

## Công thức và ví dụ

MING_SHEN_READINGS giữ6câu từảnh73:寅起正月 tiến đến tháng sinh, từđó起子時 nghịch đến giờ sinh choMệnh,thuận choThân. Ba ví dụ thángGiêng thường:Tý→MệnhDần/ThânDần,Sửu→MệnhSửu/ThânMão,Dần→MệnhTý/ThânThìn. Câu tiếp nêu **閏正月生寅時** cũng choTý/Thìn, rồi凡有閏月俱要依此為例. Ghi chú đọcđầu tạm “khôngnêu nhuận” đãđínhchínhtrước tiếpnhận,khôngtácđộngweb.

API sourceMingShen buộc tênnguồn,thángâm khai báo1–12/chi giờ/tìnhtrạng nhuận hoặcnull. Chỉ giải144tọađộ thángthường vàđúng vídụnhuậntháng1giờDần đãin. Cácnhuậnkhác,nhuậnchưa biết hoặc tháng/giờthiếu giữnull choMệnh/Thân; không giảcáchchia15ngày hoặcchuyểntháng. Cáchđánhchỉsốchi0–11vàmod12làbiểudiễnbiêntập côngkhai. APIkhôngđổilịchsinh/giờđồnghồ/hệgiờđịa phương. Ví dụnhuậnkhaitườngminhlàtọađộvănnguồn,khôngtựgánthànhmộtngàylịchsửcóthángnhuậnđãxácminh.

Bảy kiểm đạt một lượt:byte25ảnh,3vídụthường+1nhuậnin,144tọađộkhaitườngminh,chạy144HHC+144iztro2.6.2thật từ nămâm1985/ngày10/12thángthường×12giờ/hai giớixenkẽ/UTC+8,288tọađộMệnh/Thân khớp;null/đầuvào,9nhãngiáp,vàwebnguyênbyte. Khung1985/ngày10làbộđầuvàomớichoquytắcanMệnhThân,khôngchạylạibộgiáp1984/ngày15. Khớpphầnchi khôngxácminh cáckếtquảtínhcách/vậnhạn hay mọitruyềnbản. Runtimeghiđầuvào/dươnglịchtrunggian/kếtquảvàcấuhìnhrõràng.

## Danh sách giáp và phần chưa áp

Ảnh61có6nhãn夾貴:紫府/科權祿/日月/昌曲/魁鉞/左右;3夾敗:劫空/火鈴/羊陀. Đây là9nhãn, khôngphải9cặpsaođơn giản:科權祿làbanhãnbiếnhoá,chưađủphânphốihai phía;劫空chưachốtdanh tínhsao/aliascùngnguồn,khôngtựthếĐịaKhônghiệnđại. Hai hìnhhọc日月/昌曲đãkiểmởphạmvi trước,chỉliênkếtchứngcứcũ,khôngtínhlạitruntime ởđây. Phầnphụnêu吉星/廟旺/化忌khôngbịxóabởinhãnnhómthuận/nghịch. Chưađưa9nhãnthànhđoánkếtquảhoặcthaytoànphươngpháp.

## Tiếp tục

'''+ '\n\n'.join(nexts)+'\n\nHTMLđộclập/site/ZIPwebnguyênbyte,nguồn/QAngoàisite;giữsnapshot4842tệp/2706138912byteởarchives/v53-before-tuvi-ming-shen. Toànkhoactive,khôngtácphẩmđượctuyênbốápdụnghết.\n'
(b/'REPORT.md').write_text(report,encoding='utf-8')
print('Prepared25positions/6selectedreadings/3crops/7checks/144HHC144iztro; explicit printed leap example preserved, general leap remains open.')
