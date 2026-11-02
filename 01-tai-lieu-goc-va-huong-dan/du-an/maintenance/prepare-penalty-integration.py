from pathlib import Path
import json
W=Path(__file__).resolve().parent.parent
for name in ['bazi-true-ghost-context','bazi-branch-penalty']:
 s=W/'tmp'/(name+'-staging');test='test-official-context.mjs' if name=='bazi-true-ghost-context' else 'test-penalty-reference.mjs'
 p=s/test;p.write_text(p.read_text(encoding='utf-8').replace(',privateWorkingScopeNotPromoted:true',''),encoding='utf-8')
 p=s/'verify-source.py';p.write_text(p.read_text(encoding='utf-8').replace(",'privateWorkingScopeNotPromoted':True",''),encoding='utf-8')
s=W/'tmp/bazi-branch-penalty-staging';p=s/'WORK_STATE.json';d=json.loads(p.read_text(encoding='utf-8'))
d.update(status='whole-chapter-first-pass-six-source-functions-and-literal-comparison-verified',sourceChecks='SOURCE_RESULTS.json',referenceTests='REFERENCE_RESULTS.json',reference='penalty-reference.mjs',preimplementationFreeze='PREIMPLEMENTATION_FREEZE.json',newEngineCalls=8,reusedNaYinQueries=1,wholeChapterApplied=False,sourceLimits=['Names無恩/恃勢varybyvoice;no silentcurrentfolklorelabelcorrection.','Literal卯寅子retained;卯刑子coordinatecomesfromseparateexplicit219clause.','Full三刑/太歲participation,entry,福聚,官印,benefics,control/priorityremainunresolvedunlessdeclared.','Noinjury,death,gender,morality,rankorfortuneclassifier.'])
d['next']=['Integrate together with verified官鄉/真五行context;keeponecomprehensivelatestpackage.','Continue論衝擊from227alreadyviewedboundary;228–232notyetreadinthisscope.','Closeentryandcontrolsourcepremisesbeforecalendaradapter;retainliteralexamplesanddirection.']
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(s/'README.md').write_text('''# Tam Mệnh quyển2: 論三刑

Đọc lượt đầu14vị trí214–227 gồm214tái dùng/13mới;227có ranh sang衝擊. 56đơn vị biên tập phủ2140codepoint/2148UTF16,không56quy tắc nguyên tử hoàn chỉnh. 14PNGnativevà6cropchấpnhậnkhớppixel;1crop226cắt cột được giữ nhưtrialbịloại,trướcfreeze đã cócropđủba vai. 0HTTP/container/nhânchứngđộclập mới.

Sáu hàm riêng giữ12cạnh có hướng/kể cả4cặp tự hình phải làhai vị trí khác nhau;hai giọng đặt tên無恩/恃勢ngược nhau,khôngghiđè. 卯寅子còn nguyên trongảnh215/bảnsố;đường卯→子dựa câu所以卯刑子ở219,chưasửa chữ đầu. Sáu phép đếm gồm đầu đều10theo danh sách được nêu,khôngmởthànhmọicặpphép刑. Bốn chiều giá trị của tiền đề三刑全/主客/刑入chỉ nhận khai báo;giữ福聚之地vàcácnhánhkhácchưa xét,nhãn貴/賤là lời văn lịch sử,khôngdựđoánđịavịngườidùng.

Giữ5ví dụ乙丑→庚戌/丙戌/壬戌/戊戌/甲戌,dòngliteralEntrychỉhaicặp nguồn nói rõ;ngoàidanh sáchkhôngsuybảng刑入đầyđủ. Ví dụ癸巳năm/戊寅ngày/庚申giờgiữđúng3vai,khôngtựdựngngàysinh. Hàm4chi辰午酉亥đủkhácnhauvàtiềnđề吉神壓之kháccặpchi lặplại;mọihiệulực/kếtquảvẫnnull.

Freeze6tệp trước triểnkhai/runtime. TámNạpâmthật mới/1戊戌tái dùng khớp;sohành thườnglàphépđốichiếutọađộ,khôngchứngminhthuật刑入đầyđủhoặc ứngnghiệm. Chínnhómkiểmđạt338khungcạnh/6đếmsố/18khungchủkhách/3721cặptrụ/194khungba vai/20736khung4chiđủvà369khungchưarõ,63315nhánhbatrị;473123bấtbiếnnull.42khungkhônghỗtrợ/15đầuvàosai;khôngchạylạienginetrongtest.

Cònmở:từngchitiếtvượngsuy,cátthần/官印/年月日時/太歲,刑得入/福聚,以煞止煞,七mệnhđề玉井vàlờithaythếcuối. Ngônngữsứckhỏe/tửvong/giớitính/đạođức/địavịlànộidunglịchsửchưaxácminh,khôngluậncho ngườidùng. Tiếp衝擊từ227đãxemranh,khôngđếmnhìnlượtđầuthànháp trọnchương/toàntácphẩm.
''',encoding='utf-8')
s=W/'tmp/bazi-true-ghost-context-staging'
(s/'README.md').write_text('''# Tam Mệnh quyển5: 官鄉 và 真官/真鬼 theo ngữ cảnh

Năm vị trí19–23/tờ9a–11a đã đọc lượt đầu trong論正官;tách12đơn vị biên tập/439codepoint,khôngđọc/áp hếtchương. Nguồn/decoder giữSHA;3cropđã xemkhớpRGB. Ảnh21đọctheo vaitrò甲己為真土,bảnsố甲巳giữnguyên byte. Câu同受克故不作真官而作真鬼斷之ở22kếthừahai ví dụở21,khôngtáchnhãnkhỏitiềnđề.

Bốn hàm nội bộ riêng:20tọađộ Thiên quan hương và24Địa quan hương theo bảngnguồn;Chân quan hương dùng月干與命干合/前三辰,ví dụ丙子→辛卯làcơsởbiêntậpđếmtiến3;phânbiệtcuốicủa真五行克納音và本干同受克chỉnhậnhai tiềnđềkhai báo;4gốctrụ己酉/己卯/壬子/壬午vàcặpcan丁壬/乙庚chỉlàkhớpvídụ. 60ứngviêntrụthángsuytừtọađộkhônglà60dòngnguồnin,lịchsinhkhảthihoặc60cáchđãthành.

Hai tiềnđề真五行/本干khôngđượctựsuytừThậpthầncanngày,Nạpâmđơnlẻhaytên真鬼của六害. Chỉgiữnhãnnguồn真官/真鬼trongđoạncuốiđượcchọn;chưađánhgiátoànphươngpháp,thaythế/khuyếtcấu hình,三五分力,thái tuế/vaitrụhaygiảiưu tiên. Mọi kếtquả/vượngsuy/biếnhóa/lịch/thànhtổhợpsinhthậtvẫnnull.

Freeze6tệp trước triểnkhai/runtime. Tái dùng6kếtquảHE_GAN_5đãthựcthi,cócùngSHAthưviện;chỉgọi4đốitácchưacóvà6Nạpâmtrụnguồn,10đốichiếumới khớp,0calendar/lásố. Nạpâmthườngkhôngxácminhtoànnghĩa真五行. Chínnhómkiểmđạt286khungvùng,3721khungChânquanhương/60ứngviênsuy,7381khungcặpliteral/8khớpđảothứtựcancùngcặp/33chưarõ,9khunghaipahtiềnđề;125367bấtbiếnnull,29khungkhônghỗtrợ/22đầuvàosai. KhônglặpruntimekhiQA.

Chưakếtluậnsứckhỏe,tửvong,đạođức,địavịhoặchiệulựctiênđoán. Nguồn/chứngcứ/QAngoàisite;tiếptừnggiọngnguồnhoặcluânphiênnhánhđộclập,khôngcoi12xửtrílà12quytắchoànchỉnh.
''',encoding='utf-8')
print('Prepared source scope notes and promotion-neutral QA outputs.')
