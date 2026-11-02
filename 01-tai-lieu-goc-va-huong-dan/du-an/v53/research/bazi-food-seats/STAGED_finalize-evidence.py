from pathlib import Path
from hashlib import sha256
from PIL import Image,ImageChops
import json
b=Path(__file__).resolve().parent;w=b.parents[1]
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
save=lambda name,o:(b/name).write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
qa=read(b/'QA_IMAGES.json')
for x in qa['records']:
 src=w/x['sourceFile'];p=b/x['file'];assert sha256(src.read_bytes()).hexdigest()==x['sourceSHA256']and sha256(p.read_bytes()).hexdigest()==x['sha256']
 assert ImageChops.difference(Image.open(src).convert('RGB').crop(x['cropBox']),Image.open(p).convert('RGB')).getbbox()is None;x['actuallyViewed']=True
save('QA_IMAGES.json',qa)
table=read(b/'MANUAL_SEAT_CLAUSE.json');table['entryMethod']='Manual canonical stem/branch reading of five printed family lists; not diplomatic identity of every glyph.'
table['explicitEditorialNormalizations']=[dict(sourceForms='邜/夘',canonicalBranch='卯',basis='Declared canonical branch reading; source forms retained in digital corpus, not rewritten.'),dict(sourceForms='己/巳 in corresponding stem or branch positions',canonicalStem='己',canonicalBranch='巳',basis='Explicit role-based editorial canonicalization to the ten-stem or twelve-branch alphabet. Not asserted as independent proof of each printed stroke.')]
table['normalizationIsNotFullCharacterCollation']=True
save('MANUAL_SEAT_CLAUSE.json',table)
res=read(b/'REFERENCE_RESULTS.json');assert len(res['checks'])==5 and all(x['ok']for x in res['checks'])
assert res['actualHHCTenGodCalls']==100 and res['actualHHCBaziChartCalls']==2 and len(res['coordinates'])==600
save('SOURCE_DISPOSITIONS.json',dict(date='2026-10-28',selectedContext='FOOD-00-C20',sourceContextFile='v53/research/bazi-food-source/CONTEXTS.json',sourceContextSHA256='c9179c1421a4521ce9bd0f5d48ab05e28a6a9ed11daf462927ad777343be0f68',
 digitalSource='v53/research/bazi-food-source/RETAINED_DIGITAL_SECTION.txt',digitalFolios=['005-88a','005-88b'],imagePages=[177,178],newSourcePositions=0,newHTTPRequests=0,
 selectedClauseKind='Five canonical stem-family/seat lists under explicit orthographic editorial readings.',
 notApplied=['更帶祿馬旺相 and later practical outcome clauses','Full strength, source quantity, purity, effective combinations, priority or full food pattern','Other81parentcontexts and subsidiary clauses of the nine selected parents'],
 twoPreviousExamplesReprojectedNotNewIndependentCharts=True,historicalBirthDatesAttributed=False,sourceOutcomesValidated=False,consumerApplied=False))
summary='Thực Thần C20: đọc mở rộng hai ảnh177–178; chép năm nhóm can–chi theo cách đọc chuẩn hóa tường minh,20mục chi. Bộ tra cứu buộc gốc nhật can,đúng quan hệ Thực Thần và cặp can–chi khả dĩ;không lấy cả hai can của nhóm cho mỗi nhật can.5kiểm đạt,100truy vấn hàm Thập Thần HHC thật,600tọađộ hợp lệ/20tọađộ thuộc danh sách;2lá số HHC cũ chiếu tiêu chí mới cho vị trí[1,3]/[].Không phải hai ví dụ lịch sử mới hoặc xác nhận vượng suy.2cropnative khớppixel;0HTTP/vịtrí mới. C20là ngữ cảnh thứ9được chọn,còn81ngữ cảnh khác và mọi mệnhđề phụ;toàncách vẫn mở,web nguyênbyte.'
nexts=['Tiếp mệnh đề 更帶祿馬旺相 và các lớp lời bình/ưu tiên/hiệu lực trong C20,không biến tọa độ 食神見生旺 thành toàn vượng suy hoặc thành cách. Chuẩn hóa 己/巳/邜/卯 là cách đọc biên tập có ghi nhận,không ghi đè byte nguồn.',
 'Chín ngữ cảnh đã chọn mới có mệnh đề có giới hạn;81ngữ cảnh khác của90vẫn chưa vào môđun,điều kiện phụ và khoảngảnh94a–95b còn mở. Tiếp Thực/Ấn ngoại lệ hoặc cách khác có ảnh đầy đủ;khônglặpkiểmđãđạt.',
 'Nhà ở69ônhânchứng64khớp/5mờ;thuật交門換象初爻/ranhlịch/720ôtháng còn mở.Bảnggiờđínhchính144ô/0khác;khôngkhôi phục12khác giả. Tửvi童限火鈴CanhNhâm/khởihạn,DịchB02/B03/MaiHoa vẫn mở.Nghiêncứu/QAngoàisite,khôngxuấtbản.']
save('WORK_STATE.json',dict(date='2026-10-28',catalogueID='M01',status='C20canonical-seat-coordinates-verified-full-pattern-open',sourceDirectory='v53/research/bazi-food-seats',latestReport='v53/BAZI_FOOD_SEATS_REPORT.md',completedStep=summary,next=nexts,
 completeRuntimeChecks=5,sourceFamilyRows=5,canonicalBranchMemberships=20,actualHHCTenGodQueries=100,actualHHCBaziCharts=2,abstractCoordinateContexts=600,selectedSeatCoordinates=20,
 totalParentContexts=90,parentContextsWithSelectedClauses=9,otherParentContextsNotSelected=81,allSelectedParentsSubsidiaryClausesApplied=False,
 nativeCropsViewedPixelMatched=2,newHTTPRequests=0,newSourcePositions=0,newIndependentWitnesses=0,sourceImageFourFolioGapStillOpen=True,fullStrengthEstablished=False,consumerChanged=False,wholeCatalogueCompleted=False))
print('Verified2nativecrops/5groups;expliciteditorialreadingsrecorded;fullpatternopen')
