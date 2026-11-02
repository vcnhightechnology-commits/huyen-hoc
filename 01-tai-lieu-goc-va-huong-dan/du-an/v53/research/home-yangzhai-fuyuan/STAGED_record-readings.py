from pathlib import Path
import json

p = Path(__file__).resolve().parent
def write(name, value):
    (p/name).write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')

# The palace pairs below were entered by reading the displayed original JPEGs
# and native PNG crops, BEFORE computing any formula or consulting an engine.
# Each group is a printed vertical column: first, second, third year.
chunks = [
 ('upper',38,1,45,'''
 坎良 離乾 良兌 / 兌良 乾離 坤坎 / 異坤 震震 坤異 /
 坎良 離乾 良兌 / 兌良 乾離 坤坎 / 異坤 震震 坤異 /
 坎良 離乾 良兌 / 兌良 乾離 坤坎 / 異坤 震震 坤異 /
 坎良 離乾 良兌 / 兌良 乾離 坤坎 / 異坤 震震 坤異 /
 坎良 離乾 良兌 / 兌良 乾離 坤坎 / 異坤 震震 坤異'''),
 ('upper',39,46,60,'''
 坎良 離乾 良兌 / 兌良 乾離 坤坎 / 異坤 震震 坤異 /
 坎良 離乾 良兌 / 兌良 乾離 坤坎'''),
 ('middle',39,1,42,'''
 異坤 震震 坤異 / 坎良 離乾 良兌 / 兌良 乾離 坤坎 /
 異坤 震震 坤異 / 坎良 離乾 良兌 / 兌良 乾離 坤坎 /
 異坤 震震 坤異 / 坎良 離乾 良兌 / 兌良 乾離 坤坎 /
 異坤 震震 坤異 / 坎良 離乾 良兌 / 兌良 乾離 坤坎 /
 異坤 震震 坤異 / 坎良 離乾 良兌'''),
 ('middle',40,43,60,'''
 兌良 乾離 坤坎 / 異坤 震震 坤異 / 坎良 離乾 良兌 /
 兌良 乾離 坤坎 / 異坤 震震 坤異 / 坎良 離乾 良兌'''),
 ('lower',40,1,39,'''
 兌良 乾離 坤坎 / 異坤 震震 坤異 / 坎良 離乾 良兌 /
 兌良 乾離 坤坎 / 異坤 震震 坤異 / 坎良 離乾 良兌 /
 兌良 乾離 坤坎 / 異坤 震震 坤異 / 坎良 離乾 良兌 /
 兌良 乾離 坤坎 / 異坤 震震 坤異 / 坎良 離乾 良兌 /
 兌良 乾離 坤坎'''),
 ('lower',41,40,60,'''
 異坤 震震 坤異 / 坎良 離乾 良兌 / 兌良 乾離 坤坎 /
 異坤 震震 坤異 / 坎良 離乾 良兌 / 兌良 乾離 坤坎 /
 異坤 震震 坤異'''),
]
# Canonical transcription of the printed sexagenary labels. Reused as row
# identifiers; the independently entered palace values are never generated.
labels = '''甲子乙丑丙寅丁卯戊辰己巳庚午辛未壬申癸酉甲戌乙亥丙子丁丑戊寅己卯庚辰辛巳壬午癸未甲申乙酉丙戌丁亥戊子己丑庚寅辛卯壬辰癸巳甲午乙未丙申丁酉戊戌己亥庚子辛丑壬寅癸卯甲辰乙巳丙午丁未戊申己酉庚戌辛亥壬子癸丑甲寅乙卯丙辰丁巳戊午己未庚申辛酉壬戌癸亥'''
labels = [labels[i:i+2] for i in range(0,len(labels),2)]
assert len(labels)==60
central = {
 'upper': {'male':[6,15,24,33,42,51,60], 'female':[1,10,19,28,37,46,55]},
 'middle': {'male':[9,18,27,36,45,54], 'female':[4,13,22,31,40,49,58]},
 'lower': {'male':[3,12,21,30,39,48,57], 'female':[7,16,25,34,43,52]},
}
rows=[]
for era,page,start,end,text in chunks:
    pairs=text.replace('/',' ').split()
    assert len(pairs)==end-start+1
    for ordinal,pair in enumerate(pairs,start):
        assert len(pair)==2
        cells={}
        for sex,glyph in zip(['male','female'],pair):
            normalized={'良':'艮','異':'巽'}.get(glyph,glyph)
            cells[sex]={'workingGlyph':glyph,'normalizedTrigram':normalized,
                'normalization':None if glyph==normalized else glyph+'→'+normalized+'; local palace-name reading only',
                'printedCentralAnnotation':ordinal in central[era][sex]}
        rows.append({'era':era,'ordinal':ordinal,'sexagenary':labels[ordinal-1],
            'sourcePDFPage':page,'printedColumnReadingOrder':'top-middle-bottom; columns right-to-left',**cells})
assert len(rows)==180
write('MANUAL_FUYUAN_TABLE.json',{'date':'2026-10-28','sourcePages':[38,39,40,41],
 'readingMethod':'Manual entry from original raw-DCT JPEGs and native lossless crops, before formula/engine comparison. Not OCR and not generated expected values.',
 'glyphPolicy':'Working readings rather than a complete diplomatic transcription. 良/異-shaped palace glyphs normalized individually to 艮/巽; 兌 read canonically despite print shape. Sexagenary labels canonical; all rows read in source order. No global source replacement.',
 'sexColumns':'Historical male/female counting categories in this named source.',
 'rows':rows,'sourceRows':180,'sexSpecificCells':360,'centralAnnotationsManuallyRead':central,
 'regnalHeadings':[{'era':'upper','page':38,'literal':'弘治十七年以後為上元'},
                   {'era':'middle','page':39,'literal':'嘉靖四十三年以後為中元'},
                   {'era':'lower','page':40,'literal':'萬曆五十二年以後為下元','unusualRegnalCountUnverified':True}],
 'modernYearAdapterEstablished':False,'birthYearBoundaryEstablished':False})

sequences=[('乾','乾六天五禍絕延生'),('坎','坎五天生延絕禍六'),
 ('艮','良六絕禍生延天五'),('震','震延生禍絕五天六'),
 ('巽','異天五六禍生絕延'),('離','離六五絕延禍生天'),
 ('坤','坤天延絕生禍五六'),('兌','兌生禍延絕六五天')]
write('MANUAL_YOUNIAN_SEQUENCES.json',{'date':'2026-10-28','sourcePDFPage':58,
 'readingMethod':'Eight compact lines manually transcribed from source58 before engine comparison. First token is origin, not an abbreviated star.',
 'rows':[{'origin':origin,'workingText':s,'tokens':list(s[1:])}for origin,s in sequences],
 'clockwiseOrder':['乾','坎','艮','震','巽','離','坤','兌'],
 'orderBasis':'Compass coordinate expansion corroborated by source60–65 diagrams; 64 expanded direction cells are derived, not 64 independently entered diagram readings.',
 'abbreviations':{'生':'生氣','天':'天乙','延':'延年','禍':'禍害','六':'六煞','五':'五鬼','絕':'絕命'},
 'selfRole':{'literal':'輔弼','alsoNamed':'伏位','sourcePDFPage':59},
 'comparisonAliases':{'天乙':'天醫','絕命':'絶命'},
 'anchorContexts':['birth-fuyuan','declared-source-gate'],
 'sourceOutcomeValidated':False})

notes={
34:'論福元第二 mở; 福元 lấy năm sinh người ở; Đông tứ 震巽坎離, Tây tứ 乾坤艮兌; nam5寄坤/nữ5寄艮. Không đồng nhất với tọa hoặc hướng nhà.',
35:'野馬跳澗訣 và sơ đồ tay; vị trí chi trên bàn tay khác tên quái/cung của nhà. Chưa chép hết hình tay.',
36:'Nam khởi trên1坎, giữa巳位即巽, dưới兌位即申; nghịch. Nữ trên5/giữa2/dưới8; thuận. Đối bảng/ghi chú41 xác định số cung nam1/4/7. Không đọc 巳 thành六 hoặc兌 thành八.',
37:'Cung của cha không thay cho cung năm sinh con/anh em. Viện/tường/cửa và nhánh gia đình ảnh hưởng phạm vi khởi; không chỉ lấy một đại môn cho mọi người.',
38:'Bảng trên năm1–45; ba ô năm mỗi cột, đọc trên–giữa–dưới và phải sang trái. Có chú trung ký riêng từng giới.',
39:'Bảng trên46–60 rồi giữa1–42; 嘉靖四十三年以後為中元. Chuyển nguyên không đặt lại cùng một số cung.',
40:'Bảng giữa43–60 rồi dưới1–39; giữ nguyên niên hiệu 萬曆五十二年, chưa xác minh độc lập; không tự sửa lịch sử.',
41:'Bảng dưới40–60; ghi chu kỳ180 lặp và tóm tắt cung nam1/4/7, nữ5/2/8, nam5坤/nữ5艮. Mở 東四位宅圖說 với điều kiện gia đình/phòng.',
42:'坎宮: khẩu quyết 坎五天生延絕禍六; đặt cửa/phòng/giếng/bếp/chuồng/cối/thoát nước theo nhiều tọa độ, không phải một nhãn chung.',
43:'離宮: 離六五絕延禍生天; quy tắc hạng mục và vị trí cụ thể. Không biến lời về thoát nước thành chỉ dẫn kỹ thuật hiện đại.',
44:'震宮: 震延生禍絕五天六; giữ tọa độ 24sơn riêng với tám hướng.',
45:'巽宮: 巽天五六禍生絕延; các hạng mục không cùng một phép chọn tốt-xấu.',
46:'Hai đồ: 坐北向南巽門宅, 坐南向北坎門宅; lớp/đường/cao thấp có chú riêng, chưa nhập từng ô hình.',
47:'Hai đồ: 坐北向南離門宅 và 坐西向東震門宅; cổng ngăn/đường đi/cao thấp cần topology, không phải đa giác đo được.',
48:'Đồ 巽門 và một phương án 權宜造法 với nhà tọa Đông hướng Tây; giữ phương án tình thế riêng, chưa đối mọi chữ hình.',
49:'西四位宅圖說; 乾坤艮兌 theo 福元 và các hoàn cảnh gia đình/nhánh/phòng riêng.',
50:'乾宮: 乾六天五禍絕延生. Cửa chính phương 艮 bị nhắc riêng theo 別法; không nhập mọi truyền bản thành luật chung.',
51:'坤宮: 坤天延絕生禍五六; hành lang/phòng/cửa/hạng mục riêng, chưa chép tất cả tọa độ.',
52:'艮宮: 艮六絕禍生延天五; chữ cung có dạng良. Khẩu quyết kiểm lại ở58.',
53:'兌宮: 兌生禍延絕六五天; chưa chuyển toàn bộ lời đặt hạng mục thành bộ máy.',
54:'Hai đồ tọa Bắc hướng Nam坤門 / tọa Nam hướng Bắc乾門; năm lớp và cao thấp riêng.',
55:'Hai đồ tọa Đông hướng Tây乾門/坤門; 截路分房, cửa/tường khởi lại; chưa chép hết ô.',
56:'Hai đồ tọa Nam hướng Bắc艮門 / tọa Tây hướng Đông艮門; đường và cửa ngăn viện, lớp cao thấp.',
57:'Kết quyển trên; lời biên tập nêu cách Đông–Tây tứ vị ở đây còn sơ lược, viện dẫn sách khác, nhận trách nhiệm lời diễn. Không coi toàn phần là chuẩn thống nhất.',
58:'Mở quyển hai/論大遊年第三; tám khẩu quyết và bảy ánh xạ sao; mở đầu nhấn mạnh 吉星不得地亦反凶, cần điều kiện vị trí.',
59:'Tiếp 絕命破軍金; 輔弼一名伏位二木; 興廢年 theo nhóm chi. Các niên ứng chưa thành bộ lịch sự kiện hiện đại.',
60:'Hai đồ tọa Bắc hướng Nam: 離門/巽門; vị trí sao chạy quanh cung cửa, cùng tọa hướng có thể khác gốc cửa.',
61:'Hai đồ: tọa Bắc hướng Nam坤門 và tọa Nam hướng Bắc乾門; không khởi từ tọa nhà khi đang đọc đồ cửa.',
62:'Hai đồ tọa Nam hướng Bắc坎門/艮門; tám vị trí theo cửa. Chưa đối toàn bộ glyph từng sao/tiểu chú.',
63:'Hai đồ tọa Đông hướng Tây坤門/兌門; phân rõ sao và hành của cung.',
64:'Hai đồ tọa Đông hướng Tây乾門 và tọa Tây hướng Đông震門; hình bị mờ một phần, chưa độc lập chép64 ô từ hình.',
65:'Hai đồ tọa Tây hướng Đông艮門/巽門; đọc đầu hình, không nhận toàn bộ ô đã chép.',
66:'Văn giải cao thấp theo sao/cung, ví dụ乾門坎六煞 và震五鬼; cùng nhãn sao khác cao thấp/cung sinh khắc. 九星禍福訣 và đầu 搖鞭斷宅訣, giới hạn chỉ氣口與房方位高卑.',
67:'Vè sao vào cung, dự đoán thân thuộc/bệnh/tử vong/tài sản lịch sử. Chỉ ghi ngữ cảnh, chưa xác minh kết quả hoặc đưa vào web.',
68:'Tiếp vè sao/cung và 五鬼制爻; sức mạnh/vị trí không chỉ dựa tên sao; các kết quả người thật chưa xác minh.',
69:'Tiếp vè 五鬼 và 伏陰衰陽; không có ngưỡng định lượng hiện đại để tự phân từ số phòng.',
70:'五鬼點頭 / 五鬼穿宮; nội–ngoại khắc, sinh và thứ tự; các lời tổn hại không làm dự báo người dùng.',
71:'破軍凶煞 / 九星斷宅; nhiều sao và tầng lời ứng khác nhau, không ghép một bộ điểm phổ quát.',
72:'Cuối 九星斷宅 / 九星明斷訣; giữ các nhóm giọng thơ riêng; chưa áp hết điều kiện.',
73:'Tiếp 九星明斷; phụ thân/nam nữ/hôn phối/lời thiện ác là nội dung truyền thống, chưa chứng minh quan hệ nhân quả.',
74:'五行生剋訣: 金入木宮/水宮/火宮/土宮; rõ 星在上、宮在下. 武曲 và破軍 đều金 nhưng lời ứng khác nhau; không suy kết quả từ hành đơn thuần.',
75:'金入金 rồi 木入金/木; có phân đầu/sau, mốc ba mươi năm là lời nguồn, chưa xác minh hoặc gắn lịch.',
76:'木入水/火/土 và 水入金; phân 宮剋星根身受剋/宮生星, quan hệ có chiều.',
77:'水入木/水/火/土; duy trì chiều sao-cung, không dùng lời bệnh thành đánh giá y khoa.',
78:'火入金/木/水; cao/thấp/trên/dưới và sinh/khắc là điều kiện lớp văn, chưa làm kết luận thực tế.',
79:'火入火/土 rồi 土入金/木; 巨門 vs祿存 cùng土 có lời ứng khác; không rút gọn thành hành tốt/xấu.',
80:'土入水/火/土; sao/cung bằng hành không bảo đảm cùng kết luận; tiếp câu kết81.',
81:'Đọc mở rộng vị trí đã đọc trước: kết 大遊年, mở 穿宮九星/附截路分房. Tường+cửa ngăn viện làm đổi gốc; không đổi thành tầng đứng. Không tính là trang nguồn mới.'}
write('CONTEXT_READINGS.json',{'date':'2026-10-28','groups':[{'sourcePDFPage':n,'editorialVietnameseSummary':notes[n],
 'fullGlyphCollation':False,'allClausesApplied':False}for n in range(34,82)],
 'scope':'First-pass source spans, not complete transcription or empirical validation.',
 'newSourceReadPositions':47,'alreadyReadBoundaryExpanded':1,'newHTTPRequests':0,'newOriginalContainers':0})
write('READING_CORRECTION_AUDIT.json',{'date':'2026-10-28','stage':'Before promotion or any engine/consumer use',
 'initialStagingNote':'36maleupper1,middle6,lower8reverse',
 'reason':'Misread hand-position words 巳/兌 as palace numerals and conflated coordinate systems.',
 'rawSourceReading':{'page36':['男上元甲子起一位即坎即寅','中元甲子起巳位即巽','下元甲子起兌位即申'],
 'page41':'上元男一;中元男四;下元男兌;女五/二/八;五位男坤女艮'},
 'correctPalaceNumbers':{'male':[1,4,7],'female':[5,2,8]},
 'sourceChanged':False,'engineChanged':False,'consumerChanged':False,'initialMisreadingRetained':True})
qa=json.loads((p/'QA_IMAGES.json').read_text(encoding='utf-8'))
for a in qa:a['actuallyViewed']=True
write('QA_IMAGES.json',qa)
print('Manual table180 rows/360 cells; eight source sequences;48 contextual first-pass groups. No engine queried yet.')
