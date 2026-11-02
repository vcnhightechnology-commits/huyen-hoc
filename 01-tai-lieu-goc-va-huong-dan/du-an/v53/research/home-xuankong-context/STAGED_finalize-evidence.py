from pathlib import Path
from hashlib import sha256
from PIL import Image,ImageChops
import json
b=Path(__file__).resolve().parent;w=b.parents[1]
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
write=lambda name,o:(b/name).write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
qa=read(b/'QA_IMAGES.json')
for x in qa['records']:
 src=w/x['sourceFile'];p=b/x['file'];assert sha256(src.read_bytes()).hexdigest()==x['sourceSHA256']and sha256(p.read_bytes()).hexdigest()==x['sha256']
 assert ImageChops.difference(Image.open(src).convert('RGB').crop(x['cropBox']),Image.open(p).convert('RGB')).getbbox()is None
 x['actuallyViewed']=True
write('QA_IMAGES.json',qa)
records=[]
for p in range(94,101):
 f=w/f'v53/research/home-yangzhai-door-water/raw-p{p:03}.jpg';records.append(dict(sourcePDFPage=p,file=f.relative_to(w).as_posix(),bytes=f.stat().st_size,sha256=sha256(f.read_bytes()).hexdigest(),fullRawImageActuallyViewed=True,newReadPosition=False,scope='Expanded re-reading of source division and critical voices; not every glyph/case/line exchange transcribed or implemented.'))
write('RAW_REVIEW.json',dict(date='2026-10-28',records=records,newTianyigePositions=0))
write('MANUAL_SOURCE_ANCHORS.json',dict(date='2026-10-28',records=[
 dict(id='XK94-FAMILY',sourcePDFPage=94,literalYangMarks=list('乾坎艮震'),literalYinMarks=list('巽離坤兌'),context='Eight symbolic trigram labels. Following prose separately calls east/north rooms yang and west/south rooms yin; a measured-plan adapter is not established by assigning trigram direction.',notBirthFuyuanGroup=True,notWaterMountainGrouping=True),
 dict(id='XK94-INITIAL',sourcePDFPage=94,selectedLiteral='氣口首門為初爻永不變更',disposition='Initial gate/source frame anchor only; full carry/exchange algorithm unresolved, no first-draw automation.'),
 dict(id='XK95-VOICE',sourcePDFPage=95,context='Poem, annotation, and compiler stance distinguish the exchange method from other named house rules; references 天乙巨門 and later numbered combinations are not merged.',disposition='Preserve argumentative voices, not consensus.'),
 dict(id='XK96-97-OUTCOMES',sourcePDFPages=[96,97],context='Kinship, illness, death and timing claims with direction/line/year-month premises.',disposition='Historical/interpretive source claims only; not deployed as diagnoses, events or family predictions.'),
 dict(id='XK98-BALANCE',sourcePDFPage=98,selectedLiteral='陽房多必損陰人陰房多必損陽人',sourceVoice='Annotation arguing that balanced yin and yang is enough; practical efficacy not established.',disposition='Only arithmetic comparison of complete declared source counts; never infer historical health/wealth claims.'),
 dict(id='XK98-100-SEVEN',sourcePDFPages=[98,99,100],context='Seven numbered combinations, 青龍/黃蛇/赤蛇 labels and directions, star attributions, bodily and household outcomes. Annotation distinguishes these from 裝卦 and says 天乙巨門 absent there.',disposition='Not a complete seven-state exchange implementation; source-layer/model identification and efficacy remain open.')]))
result=read(b/'REFERENCE_RESULTS.json');assert len(result['checks'])==5 and all(x['ok']for x in result['checks'])
summary='P08玄空94–100raw重讀7位置/0新位置；新具名參照分離乾坎艮震陽/巽離坤兌陰，不自動等同出生東西四命或放水陰陽。5檢達，8HHCdirections真調用+8既有放水參照調用，各有4分類差異；這是框架差異，不是engine錯。已宣告且完整的來源房數才比較多寡/相等，空/缺/面積/現代樓層不代入，不推病財。另12圖69格第二版本逐格處置：64格四字段匹配，5格行字未確；0強填。9新nativecrop匹配像素(2段/7字形)。全方法/交門換象初爻/中宮和現代幾何仍未建立。'
nexts=['Hoànthiệnthuật交門/換象/初爻theogiọngnguồn vàđủcácgốcchuyểncư/phòng/cửavàhướngtrướcgiảilàđộđúngmặtbằng;khôngđồngnhất玄空vớibộPhiTinhhiệnđại.',
 'NămôhànhnhânchứngC86/3,C87/2,C89/3,C90/1/6vẫnchưachắcnétchữ;64ôkhớpđủtrườngkhôngphảihiệuquảthực. C84木1/6giữnguyêntheohaiđồin.',
 'Bảnggiờđínhchính144ôđãkhớp;vai tròcột日/ranhlịch/720ôtháng/ma trận tuổi/thước cònmở. LuânphiênBáttựvượngsuy/cáchcục,Tửvi童限火鈴CanhNhâm/khởihạn,DịchB02/B03/MaiHoa. Khônglặptải/kiểmđãđạt;nghiêncứu/QAngoàisite,khôngxuấtbản.']
write('WORK_STATE.json',dict(date='2026-10-28',catalogueID='P08',status='named-polarity-frame-guards-and69witness-cell-dispositions-verified',sourceDirectory='v53/research/home-xuankong-context',latestReport='v53/HOME_XUANKONG_CONTEXT_REPORT.md',completedStep=summary,next=nexts,newHTTPRequests=0,newSourcePositions=0,sourcePositionsExpandedReviewed=7,completeRuntimeChecks=5,actualHHCDirectionsCalls=8,actualWaterReferenceCalls=8,sourceFigureCellsReviewed=69,fullyResolvedFigureCellMatches=64,partialElementReadings=5,all69FullyMatched=False,fullSourceMethodApplied=False,consumerChanged=False,wholeCatalogueCompleted=False))
print('Recorded7expandedrawreviews/2nativecrops/5checks;fullmethodremainsopen')
