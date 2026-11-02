from pathlib import Path
from hashlib import sha256
from PIL import Image,ImageChops
import json
b=Path(__file__).resolve().parent;w=b.parents[1];old=w/'v53/research/home-yangzhai-final-spans/selection'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
save=lambda name,o:(b/name).write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
qa=read(b/'CORRECTION_QA_IMAGES.json')
for x in qa['records']:
 assert x['actuallyViewed']and not x['resampled']
 src=w/x['sourceFile'];out=b/x['file'];assert sha256(src.read_bytes()).hexdigest()==x['sourceSHA256']and sha256(out.read_bytes()).hexdigest()==x['sha256']
 assert ImageChops.difference(Image.open(src).convert('RGB').crop(x['cropBox']),Image.open(out).convert('RGB')).getbbox()is None
table=read(b/'MANUAL_HOUR_TABLE.json');prior=read(old/'MANUAL_HOUR_TABLE.json')
assert table['columns'][:10]==prior['columns'][:10]
assert len(table['columns'])==12 and len(prior['columns'])==11
module=(b/'source-hour-reference.mjs').read_text(encoding='utf-8');before=(old/'source-hour-reference.mjs').read_text(encoding='utf-8')
changes=[("status:sourceLabel==='司命'?'literal-source-engine-discrepancy':'literal-source-coordinate'","status:'literal-source-coordinate'"),('coverageIncomplete:true','coverageIncomplete:false'),("pendingSourceLabels:['勾陳']","pendingSourceLabels:[]")]
for a,z in changes:assert before.count(a)==1;before=before.replace(a,z)
assert before==module
result=read(b/'REFERENCE_RESULTS.json');assert len(result['checks'])==6 and all(x['ok']for x in result['checks'])
assert len(result['fixtures'])==144 and all(x['match']and x['typeMatch']for x in result['fixtures'])
save('CORRECTION_RESULTS.json',dict(date='2026-10-28',unchangedPriorColumns=10,correctedSimingCells=12,addedGouChenCells=12,
 correctedCoordinates=144,actualLunarObjects=144,actualHourLabelQueries=144,actualHourTypeQueries=144,labelsMatchedAfterAliases=144,typesMatched=144,
 sourceHourDifferencesRemaining=0,old12DifferenceClaimRetracted=True,oldPendingColumnClaimRetracted=True,
 nativeCropsViewedPixelMatched=4,sourceHTTPRequests=0,newTianyigePositions=0,newIndependentWitnesses=0,
 neighborDayGuideSemanticRoleUnresolved=True,consumerChanged=False,wholeCatalogueCompleted=False,
 moduleOnlyThreeStatusCoverageEdits=True,priorWrongDataRetainedForAudit=True))
summary='ĐÍNH CHÍNH bảnggiờ P08:ảnh135đúngheader司命=午申戌子寅辰午申戌子寅辰,勾陳=未酉亥丑卯巳未酉亥丑卯巳. Trướclấy cột勾陳gán司命vàcoicột日kếbênlà勾陳chưachép;12khácengine làlỗichép/lệchcột,khôngphảidịbản. Giữ10cộtcũ,sửa12ô司命/thêm12ô勾陳;6kiểmmới/144Lunarobjects thật/144nhãngiờ+144loại:144khớpsaualias/0khác.4cropnativekhớppixel;0HTTP/vịtríPDFmới/nhânchứngmới. Vai tròtoànbộcột日nhóm tamhợpvẫnmở;chưaquyđổimúigiờ/ranhngày/tổngtuyểntrạch. HTML/site/ZIPweb/enginekhôngbịảnhhưởng,toànkhoactive.'
nexts=['Dùngbảnggiờđãđínhchính144ô/0khác;khôngtiếptụcđiềutradịbản司命từ12khácgiả. Vai tròcột日vàlịch/múigiờ/ranhgiờ/tổngtuyểntrạchcầnđốichứng.',
 'Tiếp63ôđồnhânchứng/cácđiềukiệntrungcung/phươngbên/cao-thấp/交門換象初爻;C84木1/6vẫnliteralcủahaiđồin,khôngtựsửa.720ôtháng/ma trận năm/tuổi/thướcvẫnmở.',
 'LuânphiênBáttựvượngsuy/cáchcục,Tửvi童限火鈴CanhNhâm/khởihạn,DịchB02/B03/MaiHoa. Khônglặptải/kiểmđãđạt;ứngviênKiếnLộcchờbrowserQAkhảdụng,khôngvượtsetting/khôngxuấtbản.']
save('WORK_STATE.json',dict(date='2026-10-28',status='corrected-hour-columns-144coordinates-verified',sourceDirectory='v53/research/home-hour-alignment',latestReport='v53/HOME_HOUR_ALIGNMENT_REPORT.md',completedStep=summary,next=nexts,
 supersededClaims=['HOME_FINAL_SPANS_REPORT:12司命source-engine discrepancies','HOME_FINAL_SPANS_REPORT:12勾陳untranscribedcells','HOME_COURTYARDS_REPORT:follow-up hour discrepancies/pendingcolumn'],
 independentNewEditionNotUsed=True,all144CoordinatesComplete=True,allCalendarSelectionConditionsApplied=False,neighborDayGuideSemanticRoleUnresolved=True,
 newHTTPRequests=0,newSourcePositions=0,consumerChanged=False,wholeCatalogueCompleted=False))
save('WITNESS_LEADS.json',dict(date='2026-10-28',toolOnlyExtractsNotRawHTTPBodies=True,records=[dict(url=f'https://zh.wikisource.org/wiki/欽定古今圖書集成/博物彙編/藝術典/第{p}卷',purpose='Locate another hour table if present',disposition='Web transcription/extraction did not establish a usable hour-table witness; do not infer printed table absent or count new facsimile acquisition.')for p in [677,678]]))
print('Fournativecropsverified;tenpriorcolumnsunchanged;12erroneousdifferencesretractedwithaudit')
