from pathlib import Path
from hashlib import sha256
from PIL import Image,ImageChops
import json,re
w=Path.cwd();b=w/'tmp/tuvi-full-volume-staging'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
write=lambda name,x:(b/name).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
sha=lambda p:sha256(p.read_bytes()).hexdigest()
req=read(b/'WINDOWS_TRUST_REQUESTS.json');assert len(req['records'])==12
for x in req['records']:
 p=b/x['file'];assert x['status']==200 and x['TLSCertificateValidationEnabled']and sha(p)==x['sha256']and p.stat().st_size==x['bytes']
 assert Image.open(p).size==(2200,1659)
 x['actuallyViewed']=True
write('WINDOWS_TRUST_REQUESTS.json',req)
qa=read(b/'QA_IMAGES.json')
for x in qa['records']:
 assert sha(b/x['file'])==x['sha256']
 assert ImageChops.difference(Image.open(b/x['sourceFile']).convert('RGB').crop(x['cropBox']),Image.open(b/x['file']).convert('RGB')).getbbox()is None
 x['actuallyViewed']=True
qa['scope']='Five inspected crops from twelve inspected JPEG derivatives; not original JP2 or whole-character collation.'
write('QA_IMAGES.json',qa)
notes={1:'Physical upper-volume cover: 紫微斗數全書/上; colour and ruler target, ownership/catalogue labels. No date inferred from stamps.',2:'Title: 陳希夷先生著/紫微斗數全書/南陽堂較梓; opposite contents begins 壹卷/貳卷. Attribution is printed source claim, not historical authorship authentication.',3:'Contents finishes second-juan headings and lists third-juan methods: chart setup, stars, four transformations, 大限/小限/童限, 命主/身主 and diagrams. Heading presence does not mean complete rules read/applied.',4:'Contents labels 肆卷/伍卷/陸卷: twelve-palace chapters, pattern/character/children claims and luck periods. Predictions retained historically, not evidence of practical efficacy.',5:'Contents end and 卷之一 opening 太微賦; printed editorial names require separate diplomatic reading, not assumed biography.',6:'太微賦 continuation: body/life, support, palace, strength and combinations. Direct first-pass context only, no fully encoded conditional rules.',7:'太微賦 closes; 形性賦 starts. Physical/personality claims are source claims, not validated traits.',8:'形性賦 continues then 續形性賦 heading. Context distinguishes star strength, combinations and palace. No diagnoses or deterministic traits produced.',9:'續形性賦 closes then 星垣論. Discusses star elements and placements with multiple premises, not universal simple element scoring.',10:'星垣論 closes then 斗數準繩 heading. Same-name headings/ordering are recorded, not imposed from digital editions.',11:'斗數準繩 continues then 斗數發微論 starts; strength, 命身, 三方 and opposite context are research premises.',12:'斗數發微論 closes then 增補太微賦 starts; source explicitly says 吉無絕吉/凶不皆凶/吉凶無絕 and keeps強實/弱 at issue. These are constraints on interpretation, not a new scoring engine.'}
write('FIRST_PASS_READINGS.json',dict(date='2026-10-28',records=[dict(canvas=n,file=x['file'],sha256=x['sha256'],actuallyViewed=True,note=notes[n],allCharactersCollated=False,wholeConditionalRulesApplied=False)for n,x in enumerate(req['records'],1)],sourceTextualJuanCountShownInContents=6,physicalItem='4468520 upper-volume manifest',wholeSixJuanBodiesPresentInThisItemVerified=False,printedAttributionIsNotAuthenticatedAuthorship=True))
manifest=w/'v53/research/fortune-followup/official-manifest.json';canvases=read(manifest)['sequences'][0]['canvases']
prior={}
for p in (w/'v53/research').rglob('official-*.jpg'):
 if p.parent.name not in ['fortune-context','fortune-followup','fortune-table']:continue
 m=re.search(r'official-0*(\d+)\.jpg$',p.name)
 if m:prior[int(m[1])]=p
assert len(prior)==16
inventory=[]
new={x['canvas']:x for x in req['records']}
for n,c in enumerate(canvases,1):
 paths=[]
 if n in new:paths.append(dict(file=(b/new[n]['file']).relative_to(w).as_posix(),sha256=new[n]['sha256'],newThisScope=True))
 if n in prior:paths.append(dict(file=prior[n].relative_to(w).as_posix(),sha256=sha(prior[n]),newThisScope=False))
 inventory.append(dict(canvas=n,canvasID=c['@id'],institutionResource=c['images'][0]['resource']['@id'],retainedDerivatives=paths,newFirstPassReadThisScope=n in new,wholeSourceUnitApplied=False))
assert len(inventory)==129 and sum(bool(x['retainedDerivatives'])for x in inventory)==28
write('CURRENT_CANVAS_INVENTORY.json',dict(date='2026-10-28',manifestFile=manifest.relative_to(w).as_posix(),manifestSHA256=sha(manifest),records=inventory,counts=dict(manifestCanvases=129,newInstitutionJPEGBodies=12,previousPositionDerivatives=16,distinctRetainedPositions=28,positionsWithoutRetainedDerivativeInThisInventory=101),scope='129positionsofonephysicalitem;notentiresixjuanauthenticatedreadcoverage. Priorpositionsarepossessionlinks,notnewreadingclaims. V52Shugegallery17imagesandfull-res88/89duplicatesnotaddedasdistinctpositions.',wholeBookApplied=False))
state=read(b/'WORK_STATE.json');state.update(status='twelve-front-opening-images-read-source-inventory28of129-methods-open',actuallyViewedNewPositions=list(range(1,13)),newHTTP200JPEGDerivativeBodies=12,nativeCropsViewedPixelMatched=5,distinctRetainedItemPositions=28,remainingUnretainedItemPositions=101,sourceTextualJuanCountSeenInContents=6,sourceFullMethodsApplied=False,actualEngineCallsThisScope=0)
state['next']=['Continue from canvas13 through remaining opening-text span without repeating first12 images; locate complete chapter boundaries against contents.','Acquire item/body map for later juan; TOC six juan is not proof this upper physical item holds all six. Link prior74–92 method studies, do not rerun passed iztro comparisons.','Extract fully conditional rules from newly read text only when anchor/strength/effective combination premises can be justified; personality/health/fortune rhetoric remains historical.','Keep prior4718-file release intact until a complete source/function scope can be promoted, verified and packaged.']
write('WORK_STATE.json',state)
results=dict(date='2026-10-28',retainedJPEGBodyHashesVerified=12,HTTP200TLSBodies=12,headerSetsRetained=11,firstProbeHeadersUnavailable=1,priorPythonCertificateFailures=12,validationNeverDisabled=True,fullJPEGImagesActuallyViewed=12,nativeCropsViewedPixelMatched=5,canvasInventoryPositions=129,distinctRetainedPositions=28,remainingUnretainedPositions=101,originalJP2BodiesAcquired=0,engineCalls=0,consumerChanged=False,wholeBookApplied=False,wholeCatalogueCompleted=False)
write('SOURCE_RESULTS.json',results)
report='''# Tiếp tục Tử vi: đầu sách, mục lục và khoảng nội dung còn mở

Ngày28/10/2026. Đã nối lại quyền thao tác. Giữ gói V53 đã kiểm cuối4718tệp/2657400765byte; phạmvi đang làm ở staging, chưa sửa site hoặc mã phát hành.

12lượt Python thất bại xác thực local issuer được giữ trong REQUESTS.json,0body. Sau đó dùng Invoke-WebRequest với kho chứng thư chuẩn Windows:12ảnhJPEG2200×1659 từ National ArchivesofJapan nhậnHTTP200,giữSHA256byte/11bộheader;probeđầukhônggiữheader được ghi rõ. Không bỏxác thựcTLS. Đây là dẫn xuấtJPEG do cơquan phục vụ,khôngphải byteJP2gốc.

Đã xem12ảnh và5cropnativekhớppixel:ảnh1bìa上;ảnh2tên紫微斗數全書/陳希夷先生著/南陽堂較梓 và đầu mục lục;ảnh3–5giữcấu trúc六卷/đầu正文. Danhnghĩatácgiảin khôngxác minh nhân thân/nămxuấtbản. Mục lục6quyển khôngchứng minh item上129canvas chứađủ6quyển.

Phầnbody5–12đọcđầu có太微賦/形性賦/續形性賦/星垣論/斗數準繩/斗數發微論/增補太微賦 với ranh ởảnh5,7,8,9,10,11,12. Chưa khép mỗichương hoặc các điều kiện. Khôngđổi lời thể tướng/sức khỏe/tai họa/thứhạng thành kết quả người dùng; câu吉無絕吉/凶不皆凶đượcgiữ làgiới hạn phương pháp,tránh nhãn một sao thành đoán tuyệtđối.

Ma trận129canvas liên kết12ảnhmới+16vị trí cũ=28vịtrí códẫnxuất đãlưu,101chưalưu trongkiểm kê này. Không cộnggalleryShuge17ảnh vàcặp88/89fullres thànhvịtrí mới. Đây là độphủlưu ảnh,mọituyênbốđọc/toànquytắcđềutáchriêng.0enginecalls vìphạmvi này chưaso thuật tính;không đếm lạiiztrođã kiểm như chứng cứmới.

Tiếp từcanvas13,địnhvịranhchương,quyểnvàđủtiềnđềtrướcmãhóa;mọi phần chưađủvẫnactive. Nguồn/audit giữngoàisite,khôngtăngsốphiênbản hoặcxuấtbản.
'''
(b/'REPORT.md').write_text(report,encoding='utf-8')
p=w/'PENDING_RESEARCH_STATE.json';pending=read(p);pending['inProgressStaging']=dict(file='tmp/tuvi-full-volume-staging/WORK_STATE.json',status=state['status'],catalogueID='T01');pending['currentScopeChecks']=results;pending['currentTransportNote']='Windows standard certificate validation succeeded12HTTP200JPEGbodies; Python12localissuerfailuresretained;noTLSbypass';write_pending=json.dumps(pending,ensure_ascii=False,indent=2)+'\n';p.write_text(write_pending,encoding='utf-8')
p=w/'PROJECT_RESEARCH_STATE.md';old=p.read_text(encoding='utf-8-sig');p.write_text('Đang nối tiếp Tửvi28/10/2026:quyền đọc/ghi đã dùng;gói cuối4718tệp/2657400765byte đãkiểm. Staging `tmp/tuvi-full-volume-staging/WORK_STATE.json`:12ảnh đầu cơquanHTTP200/TLS đãxem/5cropkhớppixel,mục lục6quyển khôngphải6bodyđãđọc;item129canvas có28vịtrílưu/101chưa. Tiếpcanvas13. Pythonlocalissuer12lỗi giữaudit,Windowsstandardtrustthànhcông,khôngbỏTLS. ChưatiếpnhậnstagingvàoV53,chưaáphếtkho.\n\n'+old,encoding='utf-8')
print(json.dumps(results))
