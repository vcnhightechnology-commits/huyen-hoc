from pathlib import Path
from hashlib import sha256
from PIL import Image
import json,re
s=Path(__file__).resolve().parent
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
raw=(s/'RETAINED_DIGITAL_SECTION.txt').read_text(encoding='utf-8')
units=read(s/'UNITS.json')['units']
# Exact manually chosen paragraph starts. No emendation, glyph substitution,
# mechanical rule inference or claim that each paragraph is an atomic rule.
starts=[
[
('論食神','heading','editorial-heading','Các nhãn đầu mục và lời tóm tắt không thay toàn bộ điều kiện thân/Thực.'),
('食神者日干所生','main','relation-coordinate','Định nghĩa từ nhật can, hai ví dụ 甲丙/乙丁; tách quan hệ cố định khỏi thành cách.'),
('甲生丙本為泄氣','main','conditional-source-claim','Chuỗi sinh Tài/chế Sát kèm điều kiện; hình ảnh cha con là phép ví của nguồn.'),
('此格要日主食神俱生旺','main','conditional-source-claim','Thân và Thực đều sinh vượng/không xung phá; các lời về giàu, cơ thể, con và thọ chưa kiểm chứng.'),
('四柱見財食在嵗月上','main','position-conditional','Phân năm/tháng và ngày/giờ trong lời luận gia đình của nguồn; không suy tài sản thực.'),
('怕母子俱衰絶','main-plus-citations','conditional-source-claim','Hai bên suy tuyệt và câu dẫn về sinh vượng; chưa có thuật toán mức lực.'),
('又曰食神大忌偏印','quoted-voice','conditional-source-claim','Thiên Ấn khắc Thực và chuỗi tác dụng; lời về ngoại hình/tính cách/thọ giữ nội bộ.'),
('又曰陽日食神暗合官星','quoted-voice','hidden-combination-open','Tách dương/âm và điều kiện Quan/Ấn không lộ; chưa đồng nhất ám hợp với can hợp đã thành.'),
('食神只宜一位','main-or-unattributed','quantity-conditional','Một/nhiều, Thực nhiều hợp Ấn vận, Thực ít khác; không đặt ngưỡng nhiều bằng phép đếm can.'),
('故食喜旺禄相助','main','strength-and-position','Nguyệt lộc/thời lộc và sinh vượng; khác việc chỉ thấy một tên Thực.'),
('柱中雖喜見財','main','quantity-conditional','Tài có mức nhiều/ít và điều kiện thuần; không suy số tiền.'),
('食神重見變為傷官','main-or-unattributed','pattern-label-not-relation-remap','Giữ nguyên mệnh đề biến tên trong luận cách; không đổi nhãn Thập thần của hai can Thực thành Thương.'),
('又曰甲日食丙','quoted-voice','specific-stem-season-context','Ví dụ 甲丙, các chữ nước/mùa/vận và Tài; không tự gán mùa là đã có đủ lực.'),
('又如庚以壬為食','quoted-voice','specific-stem-luck-context','庚壬/thuỷ/mộc và các địa vận; chuỗi tuổi/vận phụ thuộc bối cảnh, chưa là dự báo.'),
('又曰食神忌梟亦有不畏者','quoted-voice','counterexamples-with-glyphs-open','Nhiều ngoại lệ 不畏倒食; 己/巳 trong bản chép cần đối từng chữ, không chuẩn hóa hàng loạt.'),
('或問十干以隔一位為食神何也','question-and-Xiyin-answer','named-voice','Cách giải bằng hóa khí của 希尹 là lớp giải thích riêng, không thay quan hệ Thập thần.'),
('食神者十干福禄之會','main-or-unattributed','historical-status-claim','Quân tử/tiểu nhân, tụ phúc/tụ họa là diễn ngôn nguồn; không thành điểm phẩm chất con người.'),
('如以甲子論食丙子','main','pillar-examples','Sáu ví dụ 丙子/寅/辰/午/申/戌 có các nhãn khác; không coi mọi nhãn là bảng hiện đại đã thống nhất.'),
('若遇生旺庫印天乙','main','conditional-compound-open','Tập các nhãn phụ còn có điều kiện; chưa hợp thành điểm phúc/họa.'),
('又曰甲乙食丙丁加寅邜','quoted-voice','stem-branch-strength-examples','Các nhóm can/chi gọi sinh vượng, kèm văn/võ; không đủ xác lập lực hay nghề nghiệp.'),
('食神與禄全見','main-plus-Zhimi-citation','conditional-quotation','四柱順當 và so một/bội Thực; không đồng nhất phép đếm thô với khí lực.'),
('理愚歌云','Liyu-song-plus-gloss','named-voice','返哺/thiên ất/quan ấn, gloss dưới ăn trên; chưa chọn vị trí một cách mặc định.'),
('壺中子云','Huzhongzi','quantity-contrast','Có dư/thiếu và ví dụ hai ba 丙 so hai 甲/một 丙; không bỏ bối cảnh sức lực.'),
('又曰日主時干重叠相食者','quoted-voice','historical-health-family-claim','吞啖 và chuỗi 日時, hóa giải can hợp; không chẩn đoán hoặc dự đoán cái chết/con cái.'),
('獨歩云','Dubu','named-voice','清/濁/重 và nhãn 傷官; không thay nhãn quan hệ can theo số lần xuất hiện.'),
('相心賦云','Xiangxin','historical-personality-body-claim','Lời về ăn uống/cơ thể/ca hát của nguồn, không kiểm chứng đối với người dùng.'),
('口訣云','Koujue-and-Aozhi','named-voice','月令食/身健 và 吉曜; các kết quả vật chất chỉ là lời nguồn.'),
('又云食神旺處刼財多','quoted-voice','conditional-quotation','Tỷ kiếp/thiên Ấn; không đưa kết luận sức khỏe hoặc nghèo khó ra web.'),
('幽㣲賦云','Youwei-and-Yuanli','sequence-conditional','Thứ tự 食 trước 煞 sau khác chỉ hiện diện hai tên; lời thọ/công danh chưa kiểm.'),
('寳鑑賦云','Baojian','position-conditional','月食/時官 là vị trí riêng, không đồng nghĩa điều kiện chung cấm Quan.'),
('秘訣云','Mijue','specific-stem-conditional','戊日庚時/không hỏa vượng cùng câu một Thực; không đồng nhất có 丙 với hỏa vượng.'),
('三車云','Sanche','named-voice','耗/空/庫/祿 là các tiền đề chưa có quy tắc hiệu lực hoàn chỉnh.'),
('心鏡云','Xinjing','named-voice','Thọ tinh hợp và ngồi Quan, chưa xác định đủ phạm vi/hiệu lực.'),
('萬祺賦云','Wanqi','conditional-quotation','So thân mạnh/Thực vượng, Tài/Ấn, nhiều/ít; giữ giọng dẫn, không tự ưu tiên hơn đoạn trước.'),
('古歌云','ancient-song-sequence','parallel-verses','Chuỗi ca quyết có nhiều điều kiện Quan/Ấn/Sát/mùa/vận và lời đời sống; chưa là một thuật toán chung.'),
('合諸說觀食神喜忌盡矣','compiler-conclusion','source-closure-not-project-completion','Câu kết của tác giả không phải chứng cứ dự án đã áp dụng hết kiến thức.')
],
[
('飛天禄馬','heading','editorial-heading','Tên mục phụ riêng trong phần Thực thần.'),
('喜忌篇云','Xiji-citation-and-gloss','calendar-pattern-prerequisites','Bốn ngày 庚子壬子辛亥癸亥, tháng10/11, không Tài Quan và cùng chi; chưa đổi số tháng thành tiết khí mặc định.'),
('又須月時或年與日同支','main','position-and-activity','Chi tháng/giờ/năm hợp với ngày, lộ Quan/câu hợp/giữ lộc cần hiệu lực riêng.'),
('假令庚子日','main-example','gengzi-specific','子/午 và 寅戌未 so 丑; cặp xung/hợp danh nghĩa chưa đủ hiệu lực.'),
('壬子日壬以巳土為官','main-example','renzi-specific-glyph-open','Giữ bản số 巳土, không tự sửa 己 ở mọi chỗ; điều kiện dẫn chiếu với 庚子.'),
('辛亥日辛用丙火為官','main-example','xinhai-guihai-specific','亥/巳, nhóm 申酉丑 và 寅; phân một/hơn một và chữ lộ với chữ chi.'),
('又曰庚子壬子二日','quoted-voice','counterconditions','Nước quá vượng, 丑月/酉, Tài, các phạm vi 辛癸 khác; không gộp thành một cấm chung.'),
('又曰飛天無合','quoted-voice','combination-conflict-conditions','Không hợp/có xung/phạm cấm và vận; chưa tính tiền đồ/nghề nghiệp.'),
('古歌曰','ancient-song-sequence','parallel-verses','Các câu ca quyết trên ảnh đến cuối93b và phần bản số94a; đoạn thiếu ảnh giữ mở.'),
('按此格止庚子辛亥','compiler-commentary','explicit-disagreement','Lời bình chỉ 庚子辛亥 là 傷官, 壬子癸亥 không phải; không xóa bốn ngày nêu ở đầu, ảnh đoạn này chưa có.')
],
[
('倒衝禄','heading','digital-only-heading','Đề mục và đầu mục ở khoảng94a–95b thiếu giữa188/189; không coi đã có ảnh đối.'),
('傷官月建内有倒衝禄馬格','main','two-day-prerequisites-digital-only','Hai ngày 丙午丁巳, tháng hạ/thuần dương; các điều kiện xung lộc/câu hợp chỉ có bản số ở phần đầu.'),
('又曰丙午丁巳不論合禄','quoted-voice','parallel-prerequisites-digital-only','Không luận hợp lộc/chỉ hiềm câu và khác vị trí năm/tháng/ngày/giờ; không hợp nhất với đoạn trước.'),
('若月令亥子官煞合格','main-or-quoted','counterexample-digital-only','Không chuyên lấy nhật Nhận/lấp thực; 官煞 có khí và 丁巳/辛亥/己亥 là ngoại lệ có tiền đề.'),
('又曰此格有六日','quoted-voice','six-day-variant-digital-only','Sáu ngày 丙午丙寅丙戌丁巳丁未丁卯 khác bản hai ngày; không ép chung.'),
('古歌云','ancient-song-sequence','parallel-verses-mixed-availability','Ca quyết bắt đầu trước96a thiếu ảnh và tiếp trên189/190; không gọi toàn chuỗi ảnh đối.'),
('詳諸詩止言丙午丁巳','compiler-commentary','two-day-preference','Lời bình ưu tiên hai ngày từ các bài thơ; giữ sáu ngày dẫn riêng, không dựng chuẩn chung cho mọi truyền bản.')
],
[
('天衝食禄','heading','editorial-heading','Giữ đúng đề bản số, không đổi thành một tên cách khác.'),
('乃甲食丙丙禄在巳','main','explicit-coordinate-and-negative-cases','Ví dụ 甲/丙/巳, cần cả can và chi; có một thiếu một không phải, không hạn năm/tháng/giờ và không chỉ 戊日.'),
('人命五行有厨','main','conditional-source-claim','Thuần tháng/thuận thực/Tài khố cùng điều kiện; kết quả hưởng tài/quan lộc chưa xác minh.')
],
[
('福星貴人','heading','editorial-heading','Mục Phúc tinh của nguồn này riêng với các bảng Phúc tinh khác.'),
('乃甲人見丙寅丙子','main','explicit-two-stem-examples','甲→丙寅/丙子,乙→丁亥/丁丑; các can khác chỉ được yêu cầu suy, chưa là bảng mười hàng trực tiếp.'),
('前人作甲丙相邀入虎鄉歌','compiler-commentary','explicit-year-anchor','Nguồn nói 以年論/若以日遁則非; không mặc định theo nhật can.')
],
[
('食神同窠','heading','editorial-heading','Mục Đồng khoa/tổ hợp riêng, không tự thành nhãn hiện đại phổ quát.'),
('謂甲食丙甲子人見丙子','main','thirteen-position-example','十三位 và 甲子→丙子; không tự gắn mọi anchor là ngày/năm nếu chưa xác lập phạm vi.'),
('得此者不貴即富','main','position-and-source-examples','月不如日/日不如時, hỗ hoán/sinh vượng/lộc quý và ba ví dụ bốn trụ; thành tựu lịch sử chưa kiểm.'),
('如倒食本家甲子年','main','explicit-year-hour-counterexample','Đoạn này nêu rõ năm/giờ và đảo thực vẫn quý nhưng tổn con; không áp kết quả gia đình.')
],
[
('食神帶合','heading','editorial-heading','Mục Thực thần đới hợp riêng.'),
('謂甲人見丙有辛合','main','six-visible-stem-coordinates','Sáu bộ 甲丙辛/己辛丙/乙丁壬/庚壬丁/丙戊癸/辛癸戊. Ảnh192đọc己,bản số巳; giữ dị tự tường minh, hợp có hiệu lực chưa xác lập.')
],
[
('専食合禄','heading','editorial-heading','Giữ tên 専食 của bản số, không gộp với 専印.'),
('喜忌篇云','Xiji-citation','explicit-day-hour-and-year-month-scope','戊日/庚申時, can vượng; cấm 甲丙卯寅 nêu năm/tháng, không tự mở sang mọi vị trí/tàng can.'),
('戊以庚為食神','gloss','virtual-combination-open','Giải thích hư hợp 乙卯, 甲傷戊/卯填實/寅衝/丙傷庚; chưa tự tính hư hợp thành công.'),
('喜秋冬生日旺','main','season-and-strength-and-seal','Mùa thu/đông, nhật vượng, thích Tài/Ấn và xung hình; bài thơ sau nói không Quan/Ấn là lớp khác.'),
('戊午戊寅二日難作此格','main','two-difficult-days','Hai ngày khó thành cách chỉ là điều kiện nguồn, không là verdict cấm toàn bộ.'),
('月令若值財官當以財官論','main','source-priority-premise','Tài/Quan nguyệt lệnh được luận trước; có nhãn không tự là 值 hiệu lực.'),
('經云搢笏垂紳','Jing-and-Jingjian-citations','parallel-conditions','Câu dẫn 申時/寅卯/酉未, TàiẤn/官煞; giữ tiếng dẫn và ưu tiên chưa rõ.'),
('古歌曰合神庚申','ancient-song','parallel-conditions','Nhật mạnh/甲丙寅卯/xung phá và vận 丙戊; không dự đoán tai họa gia đình.'),
('詩曰戊日庚申','poem','seal-and-season-conflict','要無官印/喜秋冬 khác đoạn văn 愛財星印綬 và lời bình 不專秋冬; chưa tự chọn một lớp.'),
('按此格即天厨食神','compiler-commentary','named-classification-difference','Lời bình không cần coi là 合禄; giữ khác biệt diễn giải.'),
('王崇古尚書不犯','compiler-source-examples','raw-jia-counterexample','Bốn trụ 甲戌庚午戊辰庚申 có Giáp năm nhưng tháng Canh chế; rawpresence không đủ loại.'),
('又張光逺長史','compiler-comparison','season-not-exclusive','So ví dụ 王 và 張 khác tháng; 建禄身旺/不專秋冬 giữ rõ, không tự xác nhận tiểu sử.')
],
[
('紅鸞天印','heading','editorial-heading','Tên riêng trong mục Thực, không coi Hồng loan phổ quát.'),
('謂丙食戊而得戊戌','main','four-day-hour-target-examples','Bốn hàng 丙戊戌/辛癸丑/壬甲辰/乙丁未, mục tiêu ở ngày/giờ; gốc can không tự gán năm hay ngày. Kết quả chưa kiểm.')
],
[
('墨池涌泉','heading','editorial-heading','Tên riêng, không suy ngành nghề/học vị.'),
('謂辛巳得癸巳癸亥','main-example','example-and-target-role-open','Ví dụ 辛巳壬辰癸巳癸亥; 癸巳/癸亥 cần cả hay từng mục tiêu không được tự chọn.'),
('推此類丙寅愛戊寅','main','six-further-pillar-pairs','Sáu cặp khác, vị trí gốc/mục tiêu và yêu cầu thành cách còn mở; không thành bảng dự báo văn quý.')
],
[
('専印合禄','heading','editorial-heading','Tên riêng không phải cách cục Thực/Thương theo lời kết nguồn.'),
('乃六癸日申時','main-and-Jing','explicit-day-hour','Sáu 癸日/庚申時, lời dẫn hình/khắc; khác hệ 戊日.'),
('葢癸日見庚申時','gloss','virtual-combination-open','Hư hợp/ám hợp 戊乙/丙 và tài/quan, không suy từ bảng hợp danh nghĩa.'),
('忌戊巳己午及丙尅庚寅衝申','main','distinct-stem-branch-raw-coordinates','Phân 戊/己/丙 can và 巳/午/寅 chi; không thay tất cả 己 bằng 巳. Chưa là từ chối hiệu lực tự động.'),
('喜行身旺印旺','main','strength-and-luck','Thân vượng/Ấn vượng/kim thuỷ vận/kỵ hỏa; chưa lượng hóa sức lực hoặc diễn biến đời người.'),
('如胡懋功叅將','main-example','printed-four-pillars','丁酉甲辰癸酉庚申: chỉ kiểm tọa độ lịch hiện đại khả dĩ, không xác nhận ngày sinh/tiểu sử.'),
('歌曰專印是逄','song-sequence','parallel-verses','Ba bài, vận/không官煞丙/thu đông và xuân hạ; chưa áp nguyên bài thành dự đoán.'),
('按專印合禄雖非食傷','compiler-conclusion','explicit-classification-boundary','Nguồn nói không phải Thực/Thương nhưng cùng luận; không đổi quan hệ Thập thần cho hợp tên chương.')
]
]
assert len(starts)==len(units)==11
contexts=[];clean_units=[]
for unit,specs in zip(units,starts):
    a,b=unit['digitalStartCodepoint'],unit['digitalEndCodepoint']
    piece=raw[a:b];folio='005-84a';prefix=raw[:a]
    tags=list(re.finditer(r'<pb:KR3g0042_WYG_(005-\d+[ab])>',prefix))
    if tags:folio=tags[-1][1]
    chars=[];folios=[];i=0
    while i<len(piece):
        match=re.match(r'<pb:KR3g0042_WYG_(005-\d+[ab])>',piece[i:])
        if match:folio=match[1];i+=len(match[0]);continue
        c=piece[i]
        if c!='¶' and not c.isspace():chars.append(c);folios.append(folio)
        i+=1
    text=''.join(chars);pos=[]
    for anchor,voice,kind,note in specs:
        found=text.index(anchor,0 if not pos else pos[-1]+1)
        pos.append(found)
    assert pos[0]==0 and pos==sorted(set(pos))
    rows=[]
    for j,(start,spec) in enumerate(zip(pos,specs)):
        end=pos[j+1]if j+1<len(pos)else len(text)
        fs=list(dict.fromkeys(folios[start:end]));missing=[f for f in fs if f in ['005-94a','005-94b','005-95a','005-95b']]
        row={'id':f"{unit['id']}-C{j+1:02d}",'unit':unit['id'],'heading':unit['heading'],'startCleanCodepoint':start,'endCleanCodepoint':end,'text':text[start:end],'digitalFolios':fs,'digitalOnlyFoliosWithinKnownContinuityGap':missing,'voice':spec[1],'disposition':spec[2],'readingNote':spec[3],'firstPassRead':True,'allCharactersImageCollated':False,'fullConditionalRuleEncoded':False,'sourceOutcomeValidated':False,'consumerApplied':False}
        rows.append(row);contexts.append(row)
    assert ''.join(x['text']for x in rows)==text
    clean_units.append({'id':unit['id'],'cleanCodepoints':len(text),'contexts':len(rows),'textSHA256':sha256(text.encode()).hexdigest()})
write(s/'CONTEXTS.json',{'date':'2026-10-28','basis':'Editorial exact contiguous partitions of retained digital text. Universal-newline decoding changes CRLF to LF for codepoint offsets;original file bytes preserved. Only PB markers,paragraphmarks and whitespace removed for clean contexts;no glyph emendation. Contexts may contain multiple propositions;not an atomic-rule completion count.','retainedSectionSHA256':sha256((s/'RETAINED_DIGITAL_SECTION.txt').read_bytes()).hexdigest(),'decodedTextSHA256AfterUniversalNewlines':sha256(raw.encode()).hexdigest(),'rawUTF8DecodedCodepointsIncludingCRLF':len((s/'RETAINED_DIGITAL_SECTION.txt').read_bytes().decode('utf-8')),'decodedCodepointsAfterUniversalNewlines':len(raw),'contextCount':len(contexts),'cleanCodepoints':sum(x['cleanCodepoints']for x in clean_units),'units':clean_units,'records':contexts,'everyRetainedDigitalCodepointAssignedExactlyOnceAfterExplicitMarkupRemoval':True,'allImageCharactersCollated':False,'fullConditionalCompiler':False,'wholeWorkApplied':False})
crops=read(s/'QA_CROPS.json')
for x in crops['records']:
    target=Image.open(s/x['file']).convert('RGBA');source=Image.open(s/x['sourceFile']).convert('RGBA').crop(x['box'])
    assert source.size==target.size and source.tobytes()==target.tobytes()
    assert sha256((s/x['file']).read_bytes()).hexdigest()==x['sha256']
    x.update(actuallyViewed=True,sourcePixelIdentityVerified=True,displayResizingDoesNotAlterSavedNativeCrop=True)
write(s/'QA_CROPS.json',crops)
print(json.dumps({'contexts':len(contexts),'cleanCodepoints':sum(x['cleanCodepoints']for x in clean_units),'digitalUnits':len(units),'cropsActuallyViewedAndPixelVerified':len(crops['records'])}))
