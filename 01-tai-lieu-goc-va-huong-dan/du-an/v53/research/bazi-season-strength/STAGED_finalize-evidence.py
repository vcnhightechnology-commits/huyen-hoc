from pathlib import Path
from hashlib import sha256,sha1
from PIL import Image,ImageChops
import json
b=Path(__file__).resolve().parent;w=b.parents[1]
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
save=lambda name,o:(b/name).write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
requests=read(b/'REQUESTS.json')['records'];assert len(requests)==3
for x in requests:
 p=b/x['file'];assert p.stat().st_size==x['bytes']and sha256(p.read_bytes()).hexdigest()==x['sha256']and x['status']==200 and x['TLSCertificateValidationEnabled']
assert sha1((b/'CADAL06066038.djvu').read_bytes()).hexdigest()=='7ee461bd944fbf23fcf0a0011aff5882214bca5c'
render=read(b/'LOCAL_RENDERS.json');assert render['containerPages']==232 and len(render['records'])==8
for x in render['records']:
 p=b/x['file'];im=Image.open(p);assert x['actuallyViewed']and sha256(p.read_bytes()).hexdigest()==x['sha256']and sha256(im.convert('RGBA').tobytes()).hexdigest()==x['pixelRGBA_SHA256']
qa=read(b/'QA_IMAGES.json');assert len(qa['records'])==6
for x in qa['records']:
 src=b/x['sourceFile'];p=b/x['file'];assert x['actuallyViewed']and sha256(p.read_bytes()).hexdigest()==x['sha256']
 assert ImageChops.difference(Image.open(src).convert('RGB').crop(x['cropBox']),Image.open(p).convert('RGB')).getbbox()is None
res=read(b/'REFERENCE_RESULTS.json');assert len(res['checks'])==5 and all(x['ok']for x in res['checks'])and len(res['coordinates'])==25
save('TEST_METADATA_EDIT_AUDIT.json',dict(date='2026-10-28',initialCompleteChecks=5,finalCompleteChecks=5,doNotAggregateAsTenIndependentChecks=True,
 edit='Renamed a false-sounding historical assertion sixthMonthMeansAllFourSeasonEnds to precise implementation fact allFourSeasonEndsAdapterEstablished:false.',
 lookupDataOrAlgorithmChanged=False,actualCalendarOrHHCEngineCallsAcrossBothRuns=0,consumerChanged=False))
summary='Tam Mệnh quyển2:giữ thêmDjVukhoCommons/CADAL06066038,10858550byte/232vịtrí,SHA2567a53f359…/APIkhớpSHA1/size,3HTTP200TLS.Xem8vịtrí109–116(6nộidung/2ranh) và6cropnativekhớppixel.Chéptrướcso25ô/5pha春夏六月秋冬:24nhãnchuẩn,1literal夏水因chưaphânloại;ảnhgiữnétchữ因khácbốn囚đốichứng,khôngsửatừcôngthức.Có2APItra nhãn/profilenguồn,5kiểmcuối;0lịch/HHCđượcgọivìkhôngsoenginehayđổi thuật lịch.Khôngtựgán六月vớibốn季末18ngày,haysuyvượngsuy/cáthungtoànlá số.Lời見生旺未必吉/休囚死絶未必凶đượcgiữ,các12寄生táchriêng.Toàn232vịtrí/cácthuyếtkhácchưađọc,hồsơcơquanCADALchưađộc lậpxáclập;webnguyênbyte,toànkhoactive.'
nexts=['Tìm nhân chứng hợp lệ cho夏水因nếu có,giữliteralhiện tại và24nhãnchuẩn;không tựép囚từbảngphổthông. Đọc phần季令/人元司事trước khépánhxạngàythựcvào pha,đặcbiệt六月土旺vàbốn季末.',
 'Phânbiệt5nhãnmùavụvới12寄生vàvượngsuytoànlá số;nguồn114nóisinhvượngchưa chắc吉/休囚死絕chưa chắc凶.Phần12địnhnghĩađọclầnđầu chưaápđầyđủ,mọichươngquyển2kháccònmở.',
 'Tiếp81ngữcảnh Thực thần chưa chọn vàđiềukiệnphụtrong9đãchọn;nhàở69ô64khớp/5mờ,交門換象初爻/ranhlịch/720ôtháng;Tửvi童限火鈴CanhNhâm/khởihạn,DịchB02/B03/MaiHoa.Nghiêncứu/QAngoàisite,khônglặptải/kiểmđãđạt,khôngxuấtbản.']
state=read(b/'WORK_STATE.json');state.update(status='selected-seasonal-labels25slots24recognized1unclassified-verified',sourceDirectory='v53/research/bazi-season-strength',latestReport='v53/BAZI_SEASON_LABELS_REPORT.md',completedStep=summary,next=nexts,
 completeRuntimeChecks=5,sourceLookupSlots=25,recognizedStateSlots=24,unclassifiedLiteralSlots=1,newHTTP200TLSBodies=3,newRepositoryContainers=1,newRepositoryContainerBytes=10858550,
 nativeCropsViewedPixelMatched=6,actualCalendarOrHHCEngineCalls=0,sourceWholeVolumeRead=False,fullNatalStrengthEstablished=False,consumerChanged=False,wholeCatalogueCompleted=False)
save('WORK_STATE.json',state)
print('Verified3HTTPbodies/8nativepositions/6crops/25slots/5finalchecks;notwholevolumeorfullstrength')
