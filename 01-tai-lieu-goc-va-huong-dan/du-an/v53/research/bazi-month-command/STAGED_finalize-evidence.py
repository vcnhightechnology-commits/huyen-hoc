from pathlib import Path
from hashlib import sha256
from PIL import Image,ImageChops
import json
b=Path(__file__).resolve().parent;w=b.parents[1]
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
save=lambda name,o:(b/name).write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
render=read(b/'LOCAL_RENDERS.json');closing=read(b/'CLOSING_RENDER.json');assert len(render['records'])==8 and len(closing['records'])==1
for x in closing['records']:x['actuallyViewed']=True;x['scope']='Chapter closing argument and next heading observed; not whole following chapter.'
if not any(x['page']==73 for x in render['records']):render['records']+=closing['records']
save('LOCAL_RENDERS.json',render);save('CLOSING_RENDER.json',closing)
qa=read(b/'QA_IMAGES.json')
src=b/'p73.png';out=b/'p73-month-only-close-native.png'
qa['records'].append(dict(sourceFile=src.name,file=out.name,sourceContainerPage=73,cropBox=[720,250,2100,2870],sha256=sha256(out.read_bytes()).hexdigest(),resampled=False,actuallyViewed=True))
assert len(qa['records'])==6
for x in qa['records']:
 src=b/x['sourceFile'];p=b/x['file'];assert sha256(p.read_bytes()).hexdigest()==x['sha256']
 assert ImageChops.difference(Image.open(src).convert('RGB').crop(x['cropBox']),Image.open(p).convert('RGB')).getbbox()is None;x['actuallyViewed']=True
save('QA_IMAGES.json',qa)
table=read(b/'MANUAL_COMMAND_TABLES.json')
next(x for x in table['records']if x['variant']=='chapter-prose'and x['monthBranch']=='巳')['sourceContainerPages']=[67,68]
next(x for x in table['records']if x['variant']=='chapter-prose'and x['monthBranch']=='丑')['sourceContainerPages']=[68,69]
save('MANUAL_COMMAND_TABLES.json',table)
src=w/'v53/research/four-items/sources/KR3g0042_002.txt';txt=src.read_text(encoding='utf-8');start=txt.index('論人元司事');end=txt.index('論四時節氣',start)
out=b/'RETAINED_DIGITAL_COMMAND_SECTION.txt';out.write_text(txt[start:end],encoding='utf-8',newline='\n')
save('SOURCE_DISPOSITIONS.json',dict(date='2026-10-28',sourceContainer='v53/research/bazi-season-strength/CADAL06066038.djvu',sourceSHA256='7a53f35982f0b946281d0e393c5d6ddcce1fd091aea83c11af6a06bcdfe6a85e',
 retainedDigital=dict(file=src.relative_to(w).as_posix(),sha256=sha256(src.read_bytes()).hexdigest(),decodedSliceFile=out.name,sliceSHA256=sha256(out.read_bytes()).hexdigest(),sliceNotOriginalHTTPBytes=True),
 voices=[dict(kind='chapter-exposition',positions=[66,67,68,69],disposition='Twelve allocations copied as one named list; 艮土/坤土 retained without replacing with a stem.'),
 dict(kind='cited-Yujing',positions=[69,70,71],disposition='Twelve alternative rows and stated annual numbers; do not treat table order as time succession or repair32/26/380vs360 totals.'),
 dict(kind='cited-Zuixingzi-and-critique',positions=[71,72,73],disposition='Claims five elements72days/earth4times18 and argues against fixed3/5/7day slicing and reducing qi to those day limits; source stance, not validated natural law.'),
 dict(kind='chapter-close',position=73,selectedLiteral='支中所藏止以月論年日時不論',disposition='Scope of this argument is monthly; not a command to remove current fixed hidden-stem table from other pillars.')],
 noPriorityOrSourceTruthAdjudicated=True,noDateOrDominantStemAdapter=True,sourceWholeVolumeRead=False,newHTTPRequests=0,newContainers=0,
 viewCounts=dict(thisScopeDistinctPositions=9,chapterPositionsWithFirstPass=[66,67,68,69,70,71,72,73],outsideBoundaryPosition=65,totalDistinctVolume2PositionsAcrossTwoScopes=17,containerPositions=232),
 consumerChanged=False,wholeCatalogueCompleted=False))
res=read(b/'REFERENCE_RESULTS.json');assert len(res['checks'])==5 and all(x['ok']for x in res['checks'])
summary='Nhânnguyêntưsựquyển2:9ảnhnative65–73(8vịtríchương/1ranhngoài),6cropkhớppixel;tổngquyển2đãxem17/232. Chép2danh sách12tháng/24hàng/69mụcngày:tổngvănxuôi360,bảngdẫn玉井358(酉32/子26);lờigiớithiệuchotámcan35ngày+hathổ50tính380kháccâu360,giữảnh/sốkhôngsửa.5kiểm,24truyvấnbảngtàngcanlunar thật:6bộkhớp/16khác/2khôngđốivì艮土坤土chưagáncan;khônggọilà16lỗiengine. APItra bảngbuộcnguồn/biếnthể/khung,khônggánngày,tưlệnh,trọngsốhoặcghéptàngcanhiệnhành. Giữlờiphêcáchchẻ3/5/7ngàyvàphạmvichỉtháng,khôngđồngnhấtvượngsuy.Toànphươngpháp/cảkhovẫnmở,webnguyênbyte.'
nexts=['Chưa có thuật ngày thực nào được xác lập từhai bảng bất nhất. Đọc/đối riêngpha/tiết vàcácgiọngcủa玉井/醉醒子/淵源淵海,khôngtựgánquyềnưu tiênhoặcsửa32/26/380về30/360.',
 'Giữ艮土/坤土chưagáncan,vai tròthứtựbảng/chiađầugiữa/cuốitháng/ranhngàyvẫnmở.Câu支中所藏止以月論khôngthaychobảngtàngcan4trụhiện hành;24truyvấnchỉsohệdữliệukhác.',
 'Quyển2mới17/232vịtrí;季節25ôcó夏水因chưaphânloại,ThựcThần9nhómchọn/81chưavàmọiđiềukiệnphụ;nhàở/Tửvi/Dịchcònmở.Tiếpphầnđộclậpkhithiếunhânchứng,khônglặptảivàkiểmđãđạt;nghiêncứu/QAngoàisite,khôngxuấtbản.']
state=read(b/'WORK_STATE.json');state.update(status='two-named-month-command-lists-24rows69entries-verified',sourceDirectory='v53/research/bazi-month-command',latestReport='v53/BAZI_MONTH_COMMAND_REPORT.md',completedStep=summary,next=nexts,positionsViewed=list(range(65,74)),newContainerPositionsViewed=9,
 totalVolume2DistinctPositionsViewed=17,sourceRows=24,allocationEntries=69,completeRuntimeChecks=5,actualLunarHiddenStemTableQueries=24,newCalendarChartCalls=0,nativeCropsViewedPixelMatched=6,fullCalendarCommandMethodApplied=False,consumerChanged=False,wholeCatalogueCompleted=False)
save('WORK_STATE.json',state)
print('Verified24rows69entries/9nativepositions/6crops/5checks;6match16different2unresolved')
