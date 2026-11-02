from pathlib import Path
from hashlib import sha256
import json
w=Path.cwd();b=w/'tmp/bazi-food-gap-witness-staging'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
write=lambda name,x:(b/name).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
sha=lambda p:sha256(p.read_bytes()).hexdigest()
res=read(b/'REFERENCE_RESULTS.json');assert len(res['checks'])==8 and all(x['ok']for x in res['checks'])
mapping=read(b/'FOLIO_MAPPING.json');assert len(mapping['recoveredGapFaces'])==4
coverage=read(w/'v53/research/bazi-food-appendices/CURRENT_CONTEXT_COVERAGE.json')
ids=['FOOD-01-C02','FOOD-01-C03','FOOD-01-C04','FOOD-01-C05','FOOD-01-C06','FOOD-01-C07','FOOD-01-C10','FOOD-02-C02','FOOD-02-C05','FOOD-02-C07']
assert len(ids)==10
for row in coverage['records']:
 if row['id']in ids:
  assert not row['selectedModuleLinks']
  row['selectedModuleLinks'].append(dict(module='v53/research/bazi-food-gap-witness/flying-reference.mjs',sha256=sha(b/'flying-reference.mjs'),
    scope='Selected named day-set/visible coordinate/priority-separation fields only; C01-C10 label has separate actual-engine comparison, not an automatic birth-month label.',
    sourceCoordinateComparisonFile='v53/qa/bazi-food-gap-witness/REFERENCE_RESULTS.json',wholeContextApplied=False))
coverage['date']='2026-10-28';coverage['counts'].update(parentsWithSelectedModuleOrDeclaredPremiseLinks=42,parentsWithoutSuchLinks=48,newFlyingDaoLinkedParents=10)
coverage['counts']['earlierScopeLinkedParents']=32
coverage['countingCorrection']='Previous32/58 source-link audit retained unchanged; add10new selected source-coordinate/engine-comparison parents. The32 already includes13old special-food provenance parents formerly omitted from narrow10/80. Links still do not establish whole-rule application.'
assert sum(bool(x['selectedModuleLinks'])for x in coverage['records'])==42
write('CURRENT_CONTEXT_COVERAGE.json',coverage)
requests=read(b/'REQUESTS.json')['records'];assert len(requests)==3
for x in requests:assert x['status']==200 and x['TLSCertificateValidationEnabled']and sha(b/x['file'])==x['sha256']
source=read(b/'ACQUISITION.json')
assert source['sourceBytes']==10808462 and source['metadata']['sha1']=='8dd4e5a566348ba56c2c3fb4f888dfac33349436'
write('SOURCE_DISPOSITIONS.json',dict(date='2026-10-28',
 newRepositoryContainer=dict(file='CADAL06056481.djvu',bytes=10808462,sha256=sha(b/'CADAL06056481.djvu'),sha1=source['metadata']['sha1'],positions=230,
   retainedHTTP200TLSBodies=3,apiSizeAndSHA1Matched=True,originalInstitutionServerBodyDownloaded=False),
 earlierRepositoryContainer=dict(file='v53/research/bazi-pattern-witness/CADAL06066041.djvu',bytes=10721582,sha256=sha(w/'v53/research/bazi-pattern-witness/CADAL06066041.djvu'),positions=226,unchanged=True),
 sourceFamily='Both repository descriptions label四庫全書/CADAL; text/layout anchors are related. Distinct repository body is not proof of an independently printed edition or separate historical authority.',
 decoder=dict(file='v53/research/bazi-pattern-extension/tooling/djvu.js',sha256=sha(w/'v53/research/bazi-pattern-extension/tooling/djvu.js'),unchanged=True),
 newContainerPositionsActuallyViewed=list(range(187,196)),newNativePNGDerivatives=9,nativeCropsViewedPixelMatched=6,
 novelTextImageFacesComparedWithPriorSpan=['005-94a','005-94b','005-95a','005-95b'],overlappingTextPositions=5,
 sourceWholeBookRead=False,independentEditionEstablished=False,fullGlyphCollation=False,
 original226ContainerGloballySearchedOrRepaired=False,retainedMissingIntervalNowAvailableInAnotherContainer=True,
 sourceContextsDispositioned=17,sourceContextCodepoints=1620,namedDaySets=3,literalMechanismCases=6,
 sourceOfficerVersusActualChartPillarDistinguished=True,sourceGenericDaoAttractionPoolNotPartitioned=True,
 sourceDingSiAdditionalLiteralRestraint='辰',standardSixCombineIsNotUniversalSourceRestraintDefinition=True,
 finalFeiCommentNotAlternativeTwoDayEligibility=True,
 finalLabelEngineComparisonUsesExplicitlyDeclaredSameBranchMonthCoordinateNotActualDate=True,
 finalChecks=8,runtimeRuns=1,actualHHCTenGodQueries=10,actualLunarHiddenStemTableQueries=10,
 actualLunarClashTableQueries=6,actualLunarSixCombineTableQueries=6,newCalendarChartCalls=0,
 wholeSourceMethodsApplied=False,sourceOutcomesValidated=False,consumerChanged=False,wholeCatalogueCompleted=False))
summary=('Bổ sung DjVu CADAL06056481 qua ba bodyHTTP200/TLS,10808462byte/230vị trí, '
 'SHA2564f273322…/API khớpSHA1 vàsize. Đã xem9vị trí187–195 và6cropnative khớppixel; '
 'đối hai ranh cũ188/93b và189/96a với bản mới188/193, bù trực tiếp bốn mặt94a–95b ở189–192. '
 'Hai bản quét cùng họWYG, chưa xác lập bản in độc lập; không sửa container226 cũ. '
 'Phân loại17ngữ cảnh/1620codepoint PhiThiên–ĐảoXung; ba giọng danh sách4/2/6ngày và lời bình hai 傷官 giữ riêng. '
 'Sáu tọa độ Quan/chi được nêu kiểm10hàm ThậpThầnHHC thật và22bảnglunar(10tàngcan/6xung/6hợp). '
 'Tám kiểm đạt một lượt/180tọa độ ngày; 辰 được nguồn nêu bên cạnh申 vẫn giữ, không ép thành định nghĩa六合. '
 'Không tạo Quan ảo thành trụ thật, không lấy số chi làm 多/有力 hoặc tự giải ưu tiên 官煞/填實. '
 'Ma trận90 có42liên kết phần/48chưa,0cha áp trọn.0lá số lịch/HHCbazi/iztro mới;web nguyênbyte,toànkho mở.')
nexts=[
 'Hai mục PhiThiên/ĐảoXung có ảnh bù và tọa độ, chưa khép 多/有力/純陰陽/合住/羈絆/điều kiện tháng và hiệu lực xung,hợp; các giọng cùng thơ và ưu tiên官煞/填實 vẫn song hành. Không coi Quan được mời ra là trụ có thật hoặc lấy nhãn tháng khai báo thành lịch sinh.',
 'Bản mới9/230vị trí, không phải đọc hết sách hay bản in độc lập. Bốn mặt94a–95b nay có nhân chứng quét cùng họ kháccontainer; đừng lặp tải hoặc tiếp tục mô tả là chưa có ảnh ở mọi nguồn. Bản226cũ và các audit lịch sử giữ nguyên. Lead NCLTaiwan06590 là metadata1578 riêng, chưa xem ảnh hoặc bù chứng cứWYG, không vượt verificationwidget.',
 'Ma trận42/48 là liên kết bộ phận/tuyên bố tiền đề, không phải42ngữ cảnh áp hết. Tiếp48cha chưa liên kết và mọi mệnh đề phụ; C15 chữ/gốc/hiệu lực/ưu tiên, sáu mục kèm và toàn vượngsuy/夏水因/tưsự32/26/380v360 còn mở.',
 'Luân phiên vấn đề độc lập lớn Nhàở交門換象初爻/720ôtháng/ranhlịch;Tửvi童限火鈴CanhNhâm/khởihạn;DịchB02/B03/MaiHoa. Nghiên cứu/nguồn/QA ngoài site;KiếnLộcUI chờ browserQA khả dụng,không vượt setting,không xuất bản.'
]
old=read(b/'WORK_STATE.json')
old.update(status='four-gap-faces-recovered-three-voice-coordinate-audit-verified-full-methods-open',
 sourceDirectory='v53/research/bazi-food-gap-witness',latestReport='v53/BAZI_FOOD_FLYING_REPORT.md',completedStep=summary,next=nexts,
 passingChecks=8,actualHHCTenGodQueries=10,actualLunarHiddenStemTableQueries=10,actualLunarClashTableQueries=6,
 actualLunarSixCombineTableQueries=6,newCalendarChartCalls=0,parentsWithPartialLinks=42,parentsWithoutLinks=48,
 wholeSourceParentsApplied=0,fullSourceMethodsApplied=False)
write('WORK_STATE.json',old)
print(json.dumps(dict(completeChecks=8,retainedHTTPBodies=3,recoveredFaces=4,parentsWithPartialLinks=42,consumerChanged=False)))
