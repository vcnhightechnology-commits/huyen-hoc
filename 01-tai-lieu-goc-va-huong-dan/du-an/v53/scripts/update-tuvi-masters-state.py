from pathlib import Path
import json

r=Path(__file__).resolve().parent.parent;w=r.parent;b=r/'research/tuvi-masters';q=r/'qa/tuvi-masters'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
qa=read(q/'RESULTS.json');src=read(q/'SOURCE_RESULTS.json')
assert len(qa['checks'])==7 and all(x['ok']for x in qa['checks'])
assert src['nativePixelCropsVerified']==2 and qa['summary']['actualHHCTuviCalls']==144
report='TUVI_MASTERS_REPORT.md'
step=('Tử vi: đọc mụcMệnhchủ/Thânchủ ởcanvas80–81 đãgiữ, trích12tọađộMệnhchủ/10tọađộThânchủmột sao và2tọađộTýNgọliteral火鈴星 chưa phânđịnh. '
 '7kiểm đạt:144HHC Tửvi+288iztro2.6.2thật (144default/144zhongzhou);default lấychi cungMệnh,zhongzhou lấychi năm,122tênkhác/22têngiống trên144ngữcảnh. '
 'Thânchủ dưới quyước chi năm của thưviện có120tênkhớptrựctiếp/24ngữcảnh nguồnchưaphânđịnh, khôngcoi24làkhớp. '
 '2ảnhcũ đọc mởrộng/2cropnative,0HTTP/container/trangnguồn mới;4tệpruntime khớpbyte tgzđãgiữ. '
 'KhôngtựgánThânchủtheo cungThân,khônglấychếđộkhác làm lỗitính. Tuổi/cungkhởiđạihạn vàCanh/Nhâm vẫn mở. Web/site/ZIPweb nguyênbyte; toànkhochưa xong.')
nexts=[
 'Tửvi: cầnnhânchứngđộclập cho火鈴星 ởTý/Ngọ vàmốcchi năm choThânchủ;khônglấyruntime chọnchữ thaynguồn. Mệnhchủđãcótọađộvàvídụneo cungMệnh,khônglặp144lá số/288lượt nếu khôngđổi logic.',
 'Mục童限 cạnhMệnhchủ cócâu1–6/十五大命 nhưngchữdưniên vàquanhệđạihạn chưađịnh;khôngsuyra tuổi15hoặcsửađạihạnhiệnhành. Canh/Nhâm,5ôkhuyết/1ômâu thuẫn/15ôkhác iztro vàcácphúkết hợp vẫnmở.',
 'Báttự:50nhãnLộc/10kho/28ngữcảnhvàKiếnLộc44ngữcảnhđãghi;điềukiệncách/vượngsuy/dụngthầnchưađủ. Nhàở:PhiTinh/đoreal/TrạchKinhảnh;Dịch:B02từ191/B03phụ/MaiHoa/chữmở. Tránh lặp bảngđãđạt.',
 'ỨngviênUIKiếnLộc vẫn ngoài site chờbrowserQA/TXT/in/PDF;khôngvượtsetting. Danhmục40/whole0 cònactive;khôngxuấtbảnmạng.'
]
write(b/'WORK_STATE.json',{'date':'2026-10-27','status':'source-master-labels-and-real-engine-anchor-contrasts-verified-more-witnesses-active',
 'latestReport':'v53/'+report,'completedStep':step,'summary':qa['summary'],'sourceVerification':src,'next':nexts,
 'consumerChanged':False,'bodyBirthYearAnchorExplicitlyAttested':False,'bodyCompoundResolved':False,'majorPeriodStartResolved':False,'wholeBookApplied':False,'wholeCatalogueCompleted':False})
d=read(w/'EXHAUSTIVE_WORK_STATE.json')
d['currentWork'].update(catalogueID='T01',relatedCatalogueIDs=['T01'],work='紫微斗數全書 — Mệnh chủ/Thân chủ và mốc chọn chi',
 reason='Keep source coordinates and software anchor conventions separate before exposing new star labels.',
 sourceDirectory='v53/research/tuvi-masters',currentStep=step,latestResearchReport='v53/'+report,
 functionalBacklog='v53/research/tuvi-masters/WORK_STATE.json',internalTuviMasterReference='v53/research/tuvi-masters/master-reference.mjs',
 sourceLimits='24sourcecoordinates,22single-star/2unresolvedliteralcompound. Bodybirthyearadapter ismodernconvention,notexplicitlydatedbythispassage. Nooutcome/fullbook/majorperiodresolution.',
 nextSourceLead={'sourceID':'T01-independent-master-and-period-witness','status':'unresolved-source-compound-and-conditional-period-contexts','file':'v53/research/tuvi-masters/WORK_STATE.json','remaining':' '.join(nexts)})
d['inProgressScope']='v53/research/tuvi-masters/WORK_STATE.json';d['subsequentPriority'][0]=' '.join(nexts)
for p in[w/'EXHAUSTIVE_WORK_STATE.json',r/'research/EXHAUSTIVE_WORK_STATE.json']:write(p,d)
p=r/'research/full-study/WORK_STATE.json';d=read(p);d['latestResearchReport']=report;d['exhaustiveNext']=' '.join(nexts)
item=next(x for x in d['items']if x['id']=='tuvi')
if step not in item['completed']:item['completed'].append(step)
if ' '.join(nexts)not in item['remaining']:item['remaining'].append(' '.join(nexts))
item['latestScope']='../tuvi-masters/WORK_STATE.json';write(p,d)
p=r/'research/library-current/COVERAGE.json';d=read(p);entry=next(x for x in d['catalogue']if x['id']=='T01');entry['latestMasterScope']=step
for f in['v53/'+report]+['v53/research/tuvi-masters/'+n for n in['WORK_STATE.json','SOURCE_MANIFEST.json','SOURCE_TABLES.json','MANUAL_READINGS.json','CROPS.json','master-reference.mjs']]+['v53/qa/tuvi-masters/RESULTS.json','v53/qa/tuvi-masters/SOURCE_RESULTS.json']:
 if f not in entry['currentEvidence']:entry['currentEvidence'].append(f)
d['latestFollowup']=report+': '+step
d['latestAcquisitionCounts']={'scope':report,'newHTTPRequests':0,'newOriginalContainers':0,'newSourcePages':0,'expandedPreviouslyReadPages':2,
 'nativeQACrops':2,'sourceMingCoordinates':12,'sourceBodyCoordinates':12,'bodyResolvedSingleStarCoordinates':10,'bodyUnresolvedCoordinates':2,'wholeWorksApplied':0}
d['counts']['newDownloadsThisScope']=0;d['counts']['newDownloadsThisScopeBasis']='Two retained public institutional image derivatives read more closely;two native crops;no new HTTP/original/sourcepage.'
assert d['counts']['catalogueRecords']==40 and d['counts']['wholeWorkApplied']==0;write(p,d)
note='Mốc Tử vi — Mệnh chủ/Thân chủ và mốc chi, 27/10/2026: `'+report+'`. '+step+'\n\n'
for p in[w/'PROJECT_RESEARCH_STATE.md',r/'NEXT_STEPS.md',r/'research/library-current/COVERAGE.md']:
 t=p.read_text(encoding='utf-8-sig')
 if not t.startswith(note):p.write_text(note+t,encoding='utf-8')
write(w/'PENDING_RESEARCH_STATE.json',{'date':'2026-10-27','status':'Tuvi-masters-current-scope-active','workDirectory':'v53/research/tuvi-masters',
 'currentWorkState':'v53/research/tuvi-masters/WORK_STATE.json','latestReport':'v53/'+report,'next':nexts,'consumerChanged':False,'wholeCatalogueCompleted':False,
 'pendingConsumerCandidate':'v53/research/bazi-jianlu-context/CANDIDATE_STATUS.json'})
(r/report).write_text('''# Tử vi: Mệnh chủ, Thân chủ và hai cách chọn mốc chi

Ngày27/10/2026. Đã đối mục tiêu hai mục anMệnhchủ/Thânchủ trong ảnh cơ quan đãgiữ, làm bộ tra riêng và thực thi iztro thật ở hai cấu hình. **7kiểm đạt**. Ảnh xác nhận một bảng Mệnhchủ neo cungMệnh trong ví dụ; hai tọa độ Thânchủ Tý/Ngọ ghi火鈴星 cònchưa phânđịnh. Chưa đưa chức năng hay kết luận mới lên web.

## Đọc ảnh và giới hạn nguồn

Tái dùng [新鋟希夷陳先生紫微斗数全書, hồ sơ1078787](https://www.digital.archives.go.jp/file/1078787), viewer4468520. Canvas80 ở`research/fortune-followup/official-080.jpg`,canvas81 ở`research/fortune-table/official-081.jpg`. Đó làthứtựcanvas trongmanifest129vịtrí, khôngphảitrangin/PDF. Cảhai đềupublic trongviewerđãgiữ;requestđãgiữ200/TLSauthorized. JPEG2200×1659px làảnhdẫnxuấtmáychủ,khôngphảibyteJP2gốc.

**0HTTP/container/trangnguồn mới**. Haiảnh cũ đọc mởrộng;hai cropnative khôngphóng/khôngnộisuy đượcxemtrựctiếp vàso lạitừngpixel vớiảnh gốc. Metadata/bytes/hashes giữ theo hồsơ trước,khôngtả cácJPEG này là bảnin mới hoặc nguồnđộclập. Khôngnhậnđãápdụngtoàncanvas80–81/129canvas/haiquyểnđóng.

AnMệnhchủ nằmcuốikhungtrái80,câuvídụvắt sangđầu81. Bảynhóm/12tọađộ:子貪狼、亥丑巨門、寅戌祿存、卯酉文曲、申辰廉貞、未巳武曲、午破軍. Ví dụ nói午宮安命 tìmPháQuân ởcungnào;子宮安命 tìmThamLang. Vìvậy phải tách **chi cungMệnh** với **chi năm sinh**; tênMệnhchủ không mặcđịnhlàsaođangđồngcungMệnh. Bộthamchiếu chỉtrảtên theo chi nguồnkhai báo;vịtrí sao trênlá số đượctra riêng.

AnThânchủ ởkhungphải81:sáunhóm12tọađộ,10tọađộmộtsao rõ(丑未天相、寅申天梁、卯酉天同、辰戌文昌、巳亥天機). Tý/Ngọ đọcđượcliteral **子午人火鈴星**. DùphầnmềmhiệnđạidùngHỏaTinh,khônglấyđápánấyđểxóachữ鈴 củaảnh. Chưarõ cụmtừchỉmộtloạisao,hailựachọnhaycảhai;danh sáchHỏa/Linh chỉlàkhả năngtáchchữ biêntập,khôngphảihaitọađộsaođộc lập đượcnguồn inra. Kếtquảhaiô vẫn `sourceStarName:null`, khôngtựchọn.

MụcThânchủ nói“子午人”v.v.,khôngviếtlạirõ“本生年”hayranhlịchnăm trongchínhđoạnngắn. Dùngchinămsinhởphépsophầnmềmlàquyướciztro2.6.2 được địnhdanh;khônggọilànguồnnàyđãxácnhậnranhTết/LậpXuân. Cũngkhôngtựlấychi cungThânthaychinăm. CácaliasHánphồn/thểgiản/tênViệtvà巳theovaichideclaredriêng,khôngsửabyteảnh.

## Đối chiếu engine thật

Tarballiztro2.6.2đãgiữ/SHA256`d44e96631c0506424c3aef25a7bba8e43e01729102d6a703720cbe224aec5403`. Bốnfileastro.js/earthlyBranches.js/stars.js/package.json đượcđối đúngbyte vớitarball;khôngtảcodeđãghimlàbảnmới nhất. `astro.js` địnhnghĩadefault dùngchi cungMệnh,zhongzhou dùngchinăm choMệnhchủ;Thânchủ dùngchinăm trongcảhai.

Thực thi **144lá số HHC Tửvi**,cùng144đầuvào chạy **144iztrodefault +144iztrozhongzhou**. 12năm1984–1995×12giờchi,thángGiêngâmngày15/thángthường,UTC+8,quyướcngàyhiện hành,giớitínhluânphiên. MỗicungMệnhvàchinămđủ12vịtrí. Phépsodùngchivậtlý,cáctênsaoHHC giữvịtrígốccủachúng.

Mệnhchủdefault khớp12tọađộnguồnqua neo cungMệnh trêncả144ngữcảnh;zhongzhou khớp cùngbảngqua neochinăm. Hai cách có **122tênkhác/22têngiống**,khôngphải122lỗitính. Mộtvàinhómdùngchungtênsao,nêntêngiốngkhôngchứngminhchi/mốclấygiốngnhau. Khôngdùngphépsohaiengine làmchứngcứứngnghiệm hoặcđồngthuậncổbản.

Thânchủ theoquyướcchinămhiệnđạicó **120ngữcảnh khớptênmộtsao trựctiếp**;24ngữcảnhTý/Ngọ iztrotrảHỏaTinh cònảnhchưaphânđịnh. Khôngcộng24ôấyvàosốkhớp. `masterLabel` buộctênhệ/loạinhãn/chinguồn;từchối trườngthiếu/chitiếngViệtkhôngkhaibáo;nulltrảchưabiết. Nguồnkhôngđủđểgán“sứcmạnh”,tínhcách,sứckhỏehaycát hung;chỉtrảtênnhãn.

Cácmụccạnhnhau đượcđịnhvịđểtiếp tục:安童限訣 cómốc1–6,câudưniên và“十五大命”cònphảilàmrõ;khôngsuyranăm15làtuổikhởiđạihạn. 左輔/右弼 cạnhcâuvídụvà金鎖鐵蛇關/竹羅三限/強弱宮/閒宮 chưaápđủ;tuyênbốbệnh/thọyểucủanguồngiữlịchsử. Cung/tuổikhởiđạihạn,Canh/Nhâm,bảngtrạngtháisao cònbacklogriêng.

## Bảo toàn và nối tiếp

Snapshottrước`archives/v53-before-tuvi-masters/`giữ3278tệp/sourceZIP2055899168byte. HTMLroot/V53/site707411byte/SHA`549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857`,ZIPweb344047bytegiữnguyên;sitechỉindex.html. Khôngtăngphiênbản/xuấtbảnmạng. Bộtranguồn/QA/góichỉởngoàisite. ỨngviênKiếnLộctrước cònđợitrìnhduyệtQA,khôngđượcgọilàđãpháthành.

Tái kiểm:`node v53/scripts/test-tuvi-masters.mjs`;`python v53/scripts/verify-tuvi-masters-sources.py`;`python v53/scripts/verify-tuvi-masters-release.py --no-write`. Kho40hồsơ/whole0,nguồnbốnngànhvàcácđiềukiệnmở vẫnđanglàm.
''',encoding='utf-8')
print('Source master labels and real dual-config iztro comparisons recorded; remaining witnesses/period rules stay active.')
