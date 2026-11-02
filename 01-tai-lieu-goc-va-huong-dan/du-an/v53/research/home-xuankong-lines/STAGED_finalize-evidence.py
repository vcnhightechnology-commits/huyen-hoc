from pathlib import Path
from hashlib import sha256
from PIL import Image,ImageChops
import json
w=Path.cwd();b=w/'tmp/home-xuankong-lines-staging'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
write=lambda name,x:(b/name).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
sha=lambda p:sha256(p.read_bytes()).hexdigest()
qa=read(b/'QA_IMAGES.json');assert len(qa['records'])==4
for x in qa['records']:
 assert sha(w/x['sourceFile'])==x['sourceSHA256']and sha(b/x['file'])==x['sha256']
 assert ImageChops.difference(Image.open(w/x['sourceFile']).convert('RGB').crop(x['cropBox']),Image.open(b/x['file']).convert('RGB')).getbbox()is None
 x['actuallyViewed']=True
write('QA_IMAGES.json',qa)
pdf='v53/research/home-yangzhai-shishu/Tianyige-330000-1705-0007405-yangzhai-shishu.pdf'
assert (w/pdf).stat().st_size==151275796 and sha(w/pdf)=='b6394102a995bb66df173452b37614b29d58e34ff85e08c43077006572ac48a5'
readings=[
 dict(id='carry-pair',sourcePDFPage=94,selectedReading='自乾方移至巽則先得一陽爻後得一陰爻自坤方移至艮則先得一陰爻後得一陽爻',
   disposition='Two printed examples and named symbolic polarity family only; final line positions after gate insertion not established.'),
 dict(id='first-room',sourcePDFPage=94,selectedReading='既移入宅所修第一口房則為三爻',
   disposition='Retained source ordinal, not an implemented less-than-five-room phase.'),
 dict(id='fixed-gate',sourcePDFPage=94,selectedReading='氣口首門為初爻永不變更',
   disposition='Gate is distinct initial line; its bit is supplied explicitly, not inferred or auto complemented.'),
 dict(id='room-sides',sourcePDFPage=94,selectedReading='凡修蓋東房北房一口則畫一陽爻修蓋西房南房一口則畫一陰爻',
   disposition='Declared cardinal source-room sides only; no modern measured diagonal plan/floor/area conversion.'),
 dict(id='five-units',sourcePDFPage=95,selectedReading='任修蓋房十座二十座只以五座次序為上五爻門為初爻其餘五座以前俱除起不筭',
   disposition='Explicit editorial model retains last five declared distinct source units in established sequence above gate; not proof of whole exchange method.'),
 dict(id='old-new-unit',sourcePDFPage=95,selectedReading='或修舊或創新俱筭一座',
   disposition='Each declared distinct source unit can be old-repair or new. No automatic claim that repeated work on one physical room creates multiple source units.'),
 dict(id='poem-flip',sourcePDFPage=95,selectedReading='先房返卦初爻定初陽返陰陰返陽次選門路四爻法',
   disposition='Poem return/complement phase and relation to prior fixed-gate prose unresolved; no gate-bit flip automatically applied.'),
]
write('MANUAL_READINGS.json',dict(date='2026-10-28',records=readings,
 selectedReadingsAreEditorialNotWholeGlyphDiplomaticCollation=True,rawBytesAndGlyphVariantsNotOverwritten=True,
 sourcePhysicalPlanInferenceValidated=False,wholeExchangeMethodApplied=False))
digital=w/'v53/research/home-yangzhai-courtyards/gjts676-pages/p89.txt'
write('RELATED_CONTEXT.json',dict(date='2026-10-28',file=digital.relative_to(w).as_posix(),sha256=sha(digital),
 text=digital.read_text(encoding='utf-8-sig'),kind='Previously retained GJTS compiled excerpt/transcription; not an independent authorial manuscript or new download.',
 containsFiveUnitClause=True,allFacsimileGlyphsHereCollated=False))
res=read(b/'REFERENCE_RESULTS.json');assert len(res['checks'])==7 and all(x['ok']for x in res['checks'])
write('SOURCE_DISPOSITIONS.json',dict(date='2026-10-28',sourcePDF=dict(file=pdf,bytes=151275796,sha256=sha(w/pdf),positions=195,
  kind='Previously retained processed repository PDF; institutional-original server body/imprint authentication not established in this scope.'),
 sourceRawImages=[dict(file=f'v53/research/home-yangzhai-door-water/raw-p{n:03}.jpg',sha256=sha(w/f'v53/research/home-yangzhai-door-water/raw-p{n:03}.jpg'),sourcePDFPage=n,expandedActuallyViewed=True,newReadPosition=False)for n in [94,95]],
 nativeCropsViewedPixelMatched=4,newHTTPRequests=0,newContainers=0,newReadSourcePositions=0,
 selectedSourceReadings=7,manualReadingIsNotAllCharacterCollation=True,
 lastFiveOrderToUpperLinesDeclaredEditorial=True,
 lessThanFiveRoomCarryInsertionPhaseImplemented=False,gateComplementResolved=False,
 distinctSourceUnitsAndCompleteTailAreDeclaredNotAutomaticallyInferred=True,
 repeatedPhysicalRoomRepairCountingResolved=False,modernPlanAdapterEstablished=False,
 runtimeChecks=7,runtimeRuns=1,actualHHCHexNumberCalls=64,newCalendarChartCalls=0,
 hexEncodingComparisonNotHousePredictionEvidence=True,
 sourceWholeMethodApplied=False,sourceOutcomesValidated=False,consumerChanged=False,wholeCatalogueCompleted=False))
summary=('P08裝卦:đọc mở rộng raw94–95 và4cropnative khớppixel,0HTTP/vị trí/container mới. '
 'Giữ7mệnhđề đọc chọn:hai ví dụ chuyển乾→巽/坤→艮,phòng đầu là爻3,門初爻,cácphòng東北陽/西南陰, '
 'năm đơnvị theo thứtự và sửa cũ/xây mới,thơ初陽返陰. Module riêng môhình tườngminh giữ năm đơnvị nguồn cuối, '
 'đặt trên hào cửa khai báo;đòi thứtự/đuôicuối/đơnvịphânbiệt đã xác lập,không lấy tầng đứng/diệntích. '
 'Sửa cũ và xây mới mỗi đơnvị khai báo tínhmột;không tự đếm nhiều lần sửa cùng phòng. '
 'Dưới5phòng không tự chèn2hào chuyển cư;hào cửa không tự đảo theo thơ. '
 '7kiểm đạt một lượt,64lần HHChexNumber thật phủ64mã hào vàneoCàn/Khôn/KýTế/VịTế; '
 'chỉ kiểm mã quẻ,không xác minh thuật nhà ở hay cát hung. Toànphươngpháp/đổi hào/plan hiệnđại/hiệuquả vẫn mở;web nguyênbyte,toànkho active.')
nexts=[
 'Tiếp nghĩa phối hợp hai hào chuyển cư, phòng đầu “爻3”, chèn cửa làm hào đầu và thơ “初陽返陰陰返陽”: chưa tự chọn quyền ưu tiên hay đảo cửa. Mô hình năm đơn vị là phép sắp xếp có nhãn, chưa khép toàn giao môn/đổi tượng.',
 'Cần định nghĩa đủ “một phòng/một tòa” trong nguồn, thứ tự và đuôi cuối, vai sửa cùng một phòng, hướng cửa và phân loại mặt bằng có phương chéo/nhà nhiều tầng. Không tự biến 乾坎艮震 symbolic thành nhóm mệnh hoặc khu vực đo hiện đại.',
 'P08 vẫn195/195 đọc đầu,0đơnvị áphết;69ônhânchứng64đủ/5hành mờ,720ôtháng/ranhlịch/bảngtuổi/thước còn mở. Không lặp bảng giờ144đãkhớp. Báttựma trận42/48 vànhânchứngbù94a–95b đãlưu,không mô tả lại là chưa có ảnh ở mọi nguồn.',
 'Luân phiên Tửvi童限火鈴CanhNhâm/khởihạn và DịchB02/B03/MaiHoa có tiền đề đủ. KiếnLộcUI tiếp tục riêng khi browserQA chưa khả dụng;nghiên cứu/QA ngoài site,không vượt setting và không xuất bản.'
]
write('WORK_STATE.json',dict(date='2026-10-28',catalogueID='P08',status='declared-five-room-line-window-and64-hex-encoding-verified-full-exchange-open',
 sourceDirectory='v53/research/home-xuankong-lines',latestReport='v53/HOME_XUANKONG_LINES_REPORT.md',completedStep=summary,next=nexts,
 expandedSourcePositions=2,newReadSourcePositions=0,nativeCropsViewedPixelMatched=4,selectedSourceReadings=7,
 completeRuntimeChecks=7,actualHHCHexNumberCalls=64,newCalendarChartCalls=0,newHTTPRequests=0,
 fullXuanKongExchangeMethodApplied=False,modernPlanAdapterImplemented=False,sourceOutcomesValidated=False,
 consumerChanged=False,wholeCatalogueCompleted=False))
print(json.dumps(dict(completeChecks=7,actualHHCHexNumberCalls=64,crops=4,consumerChanged=False)))
