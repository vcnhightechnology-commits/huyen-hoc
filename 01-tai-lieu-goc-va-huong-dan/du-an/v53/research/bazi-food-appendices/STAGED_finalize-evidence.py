from pathlib import Path
from hashlib import sha256
from PIL import Image, ImageChops
import json
w=Path.cwd();b=w/'tmp/bazi-food-appendices-staging'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
write=lambda p,x:p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
sha=lambda p:sha256(p.read_bytes()).hexdigest()
qa=read(b/'QA_IMAGES.json');assert len(qa['records'])==6
for x in qa['records']:
 x['actuallyViewed']=True
 assert sha(w/x['sourceFile'])==x['sourceSHA256'] and sha(b/x['file'])==x['sha256']
 assert ImageChops.difference(Image.open(w/x['sourceFile']).convert('RGB').crop(x['cropBox']),Image.open(b/x['file']).convert('RGB')).getbbox() is None
qa['viewScope']='Five expanded full-page images and six native crops actually inspected. Extra crop widens the same195column, not a new witness. Canonical 己/巳 role readings remain explicit editorial readings, not all-character collation.'
write(b/'QA_IMAGES.json',qa)
res=read(b/'REFERENCE_RESULTS.json');assert len(res['checks'])==9 and all(x['ok'] for x in res['checks'])
assert res['summary']['finalHHCTenGodQueries']==86
context=read(w/'v53/research/bazi-food-source/CONTEXTS.json')
links={}
def link(ids,module,note):
 for id in ids:
  links.setdefault(id,[]).append(dict(module=module,sha256=sha(w/module),scope=note,wholeContextApplied=False))
core=read(w/'v53/research/bazi-food-core/SELECTED_PREDICATES.json')
link(sorted({x['parent'] for x in core['clauses']}),'v53/research/bazi-food-core/core-reference.mjs','Selected exact clauses and explicitly declared research premises; not all subsidiary conditions.')
link(['FOOD-00-C20'],'v53/research/bazi-food-seats/food-seat-reference.mjs','Named five-family listed coordinate set only; remaining 祿馬旺相 and outcomes open.')
link(['FOOD-00-C15'],'v53/research/bazi-food-owl-exceptions/owl-exception-reference.mjs','Eight source-role exception premise audits; natal anchors/effectiveness/priority still open.')
special='v53/research/bazi-food-source/special-food-reference.mjs'
# Explicit provenance for already preserved special-food fields. Links do not mean full clauses are implemented.
special_scopes={
 'FOOD-07-C02':'戊day/庚申hour base coordinates, not a formed pattern.',
 'FOOD-07-C03':'甲丙卯寅 visible year/month hits; no automatic effective hidden combination.',
 'FOOD-07-C04':'Prose seal preference/autumn-winter retained; strength/priority declarations not inferred.',
 'FOOD-07-C05':'戊午/戊寅 difficult-day coordinates only.',
 'FOOD-07-C06':'effectiveMonthWealthOfficerPriority is an explicit caller declaration, not an evaluated month-pattern test.',
 'FOOD-07-C09':'Poem 要無官印 stored against prose 愛財星印綬; no adjudicated priority.',
 'FOOD-07-C11':'Printed 高燿 chart and year甲/month庚 counterexample coordinate shape, effective control still declared.',
 'FOOD-07-C12':'不專秋冬生 retained against earlier seasonal preference; no automatic exclusive season gate.',
 'FOOD-10-C02':'癸day/庚申hour base coordinate, not whole 六癸 method.',
 'FOOD-10-C03':'Named hidden mechanism and effectiveHiddenCombination declaration only; not proof of actual 虛合.',
 'FOOD-10-C04':'Visible 戊己丙/巳午寅 source-local raw hits, not final rejection.',
 'FOOD-10-C05':'dayStrong/sealStrong declarations only; no gold-water luck or outcome classifier.',
 'FOOD-10-C06':'胡懋功 literal chart projected in earlier source probe; no new independent example here.',
}
special_text=(w/special).read_text(encoding='utf-8')
for field in ['baseCoordinatesMatch','source195ControlledJiaCounterexampleShape','difficultDayCoordinates','sourceProseVsPoemSealConflict','sourceProseAutumnWinterVsCommentaryNotExclusive','effectiveMonthWealthOfficerPriority','effectiveHiddenCombination']:
 assert field in special_text
for id,note in special_scopes.items():link([id],special,note)
new_source='v53/research/bazi-food-appendices/appendix-reference.mjs'
new_ids={x['parentContext'] for x in read(b/'EXPLICIT_COORDINATES.json')['records']}|{'FOOD-04-C03'}
assert len(new_ids)==9
for id in new_ids:
 links.setdefault(id,[]).append(dict(module=new_source,sha256=sha(b/'appendix-reference.mjs'),
  scope='Explicit listed coordinates / source year-anchor guard only; every whole clause remains unapplied.',wholeContextApplied=False))
assert len(links)==32
coverage_records=[]
for x in context['records']:
 coverage_records.append(dict(id=x['id'],unit=x['unit'],digitalCodepoints=len(x['text']),
  sourceFirstPassDisposition=x['disposition'],selectedModuleLinks=links.get(x['id'],[]),
  wholeContextApplied=False,remainingSubsidiaryConditionsOpen=True,sourceOutcomeValidated=False))
write(b/'CURRENT_CONTEXT_COVERAGE.json',dict(date='2026-10-28',source='v53/research/bazi-food-source/CONTEXTS.json',
 sourceSHA256=sha(w/'v53/research/bazi-food-source/CONTEXTS.json'),records=coverage_records,
 counts=dict(totalParents=90,parentsWithSelectedModuleOrDeclaredPremiseLinks=32,parentsWithoutSuchLinks=58,
  coreSeatsOwlParents=10,earlierSpecialFoodProvenanceParents=13,newAppendixParents=9,
  wholeParentsApplied=0,wholeSourceUnitsApplied=0),
 countingCorrection='Older10/80 counted core/seats/owl but omitted13already-presentzhuanshi/zhuanyin provenance links. Current32/58 explicitly includes those13 and9new appendixparents; neither count is whole-context application. Earlier10/80 reports preserved as historical scope counts.',
 moduleLinkIsNotFullRuleOrEvidenceOfEffectiveness=True))
raw=[dict(file=f'v53/research/bazi-food-source/p{n}.png',sha256=sha(w/f'v53/research/bazi-food-source/p{n}.png'),sourceContainerPage=n,expandedActuallyViewed=True,newSourcePosition=False) for n in [190,191,192,195,196]]
write(b/'SOURCE_DISPOSITIONS.json',dict(date='2026-10-28',
 sourceContainer=dict(file='v53/research/bazi-pattern-witness/CADAL06066041.djvu',sha256=sha(w/'v53/research/bazi-pattern-witness/CADAL06066041.djvu'),positions=226,
  provenance='Previously retained Commons/CADAL repository body; not a new download or publisher signature.'),
 digital=dict(file='v53/research/four-items/sources/KR3g0042_005.txt',sha256=sha(w/'v53/research/four-items/sources/KR3g0042_005.txt'),
  provenance='Previously pinned Kanripo WYG transcription; raw bytes retained, not original manuscript/whole facsimile collation.'),
 rawExpandedViews=raw,nativeCropsViewedPixelMatched=6,sourceUnitsSelected=6,sourceContextsDispositioned=17,
 sourceContextCodepoints=sum(x['digitalCodepoints'] for x in read(b/'CLAUSE_DISPOSITIONS.json')['records']),
 literalCoordinateRecords=23,actualHHCTenGodQueries=86,literalHHCTenGodQueries=26,derivedHHCTenGodQueries=60,
 actualLunarLuTableQueries=1,actualLunarCombinationTableQueries=6,
 completeRuntimeChecks=9,runtimeRuns=1,newHTTPRequests=0,newContainers=0,newSourcePositions=0,
 fullGlyphCollation=False,sourceImageFourFolioGapStillOpen=True,
 yearVersusDayGuardOnly=True,natalAnchorRolesForOtherPassagesEstablished=False,
 manyTargetJoinOperatorEstablished=False,effectiveCombinationEstablished=False,
 inclusive13Interpretation='Editorial inclusive advance12 derived coordinates, separate from one literal甲子→丙子example.',
 sourceOutcomeValidated=False,consumerChanged=False,wholeCatalogueCompleted=False))
summary=('Đã kiểm sáu mục kèm Thực Thần qua 17 ngữ cảnh: 23 bản ghi tọa độ cho bảy hệ có tên, '
 'trong đó hai ví dụ đảo thực giữ riêng. Phúc Tinh giữ gốc năm, Hồng Loan Thiên Ấn giữ đích ngày/giờ; '
 'không đổi thành nhật can hoặc sao Tử vi. Hai danh sách nhiều trụ còn giữ từng token, chưa tự chọn AND/OR. '
 'Mặc Trì có các cặp khác chi, không ép cùng chi. Sáu crop từ năm ảnh cũ đã xem/khớp pixel. '
 'Chín kiểm đạt một lần; 86 truy vấn Thập Thần HHC thật (26 tọa độ in/60 cặp suy từ đếm bao gồm), '
 'một bảng Lộc và sáu bảng hợp can lunar thật. 3600 cặp can–chi khả dĩ kiểm phép đếm13=tiến12, '
 'không phải 60 dòng nguồn in. Ma trận90 cha có32 liên kết phần/tuyên bố tiền đề,58 chưa liên kết: '
 '10 core/seats/owl +13 liên kết môđun chuyên thực/chuyên ấn cũ từng bị bỏ khỏi tổng +9 cha mới. '
 'Không cha/mục nào áp trọn; 0 chart lịch/HHCbazi/iztro mới,0HTTP/vị trí/container mới; web nguyên byte, toàn kho còn mở.')
nexts=[
 'Tiếp các mệnh đề chưa có phép tái lập: 飛天祿馬/倒衝祿 với giọng nguồn khác nhau và khoảng ảnh94a–95b. Không giả nghĩa 多/有力/純陰/純陽/合住/羈絆 hoặc tự điền trụ bị ẩn.',
 'Thiên Trù còn vai gốc và cùng vị trí can–chi; Phúc Tinh còn phép 本旬/餘例推, cách ghép nhiều đích; 同窠 còn vai gốc/互換生旺帶祿貴; 帶合 chưa chứng hiệu lực; Hồng Loan Thiên Ấn chưa rõ gốc; Mặc Trì chưa rõ phép chọn hai đích. Nguồn tiên đoán tài lộc, con cái, sức khỏe và phẩm trật giữ ngoài diễn giải dự báo.',
 'Ma trận90 ghi liên kết bộ phận/tuyên bố nghiên cứu, không đồng nghĩa áp hết32 cha.58 cha chưa liên kết cùng mọi điều kiện phụ còn mở. C15 chữ/gốc/hiệu lực/ưu tiên, mùa 夏水因, bảng tư sự32/26/380v360 và toàn vượng suy vẫn mở.',
 'Luân phiên phần độc lập Nhà ở交門換象初爻/720ôtháng/ranhlịch, Tửvi童限火鈴CanhNhâm/khởihạn, DịchB02/B03/MaiHoa. Không lặp tải/kiểm đã đạt. Nghiên cứu/QA ngoài site; UI KiếnLộc chờ browserQA khả dụng, không vượt setting và không xuất bản.'
]
write(b/'WORK_STATE.json',dict(date='2026-10-28',status='six-appendix-coordinate-and90-parent-link-audit-verified-full-methods-open',
 catalogueID='M01',sourceDirectory='v53/research/bazi-food-appendices',latestReport='v53/BAZI_FOOD_APPENDICES_REPORT.md',
 completedStep=summary,next=nexts,sourceUnitsSelected=6,sourceContexts=17,literalCoordinateRecords=23,
 nativeCropsViewedPixelMatched=6,passingChecks=9,actualHHCTenGodQueries=86,actualLunarLuTableQueries=1,
 actualLunarCombinationTableQueries=6,parentsWithPartialModuleLinks=32,parentsWithoutModuleLinks=58,
 fullAppendixMethodsApplied=False,wholeSourceParentsApplied=0,newSourcePositions=0,newHTTPRequests=0,
 newCalendarChartCalls=0,consumerChanged=False,wholeCatalogueCompleted=False))
print(json.dumps(dict(sourceContexts=17,literalCoordinateRecords=23,sourceContextCodepoints=sum(len(x['text'])for x in read(b/'SELECTED_CONTEXTS.json')['records']),
 completeChecks=9,partialLinkedParents=32,unlinkedParents=58)))
