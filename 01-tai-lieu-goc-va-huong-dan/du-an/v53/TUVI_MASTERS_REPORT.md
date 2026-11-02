# Tử vi: Mệnh chủ, Thân chủ và hai cách chọn mốc chi

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
