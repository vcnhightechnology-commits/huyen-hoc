from pathlib import Path
import json
p=Path(__file__).resolve().parent
def write(n,d):(p/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
# Manual source reading, not generated from a trigram, engine, formula or prior
# edition. Marginal alternatives remain a separate printed layer.
data=[
 ('壬',109,'甲乙','巨門',None,None,'寬深'),
 ('子',109,'甲乙','巨門',None,None,'深寬'),
 ('癸',109,'甲乙','巨門',None,None,'平坦'),
 ('丑',109,'丙丁','祿存',None,None,'寬闊'),
 ('艮',109,'丙丁','祿存',None,None,'坦平'),
 ('寅',109,'壬癸','廉貞','甲乙','六煞','闊深聚'),
 ('甲',109,'壬癸','巨門',None,None,'坦平'),
 ('卯',109,'庚辛','破軍',None,None,'聚水'),
 ('乙',110,'壬癸','巨門',None,None,'平坦'),
 ('辰',110,'乾','祿存',None,None,'深聚'),
 ('巽',110,'庚辛','六煞','丙丁','巨門','闊深聚'),
 ('巳',110,'庚辛','六煞','丙丁','巨門','闊深聚'),
 ('丙',110,'庚辛','廉貞',None,None,'平坦'),
 ('午',110,'乾','破軍',None,None,'闊深'),
 ('丁',110,'庚辛','廉貞',None,None,'平坦'),
 ('未',110,'壬癸','破軍','甲乙','禍害','寬深'),
 ('坤',110,'壬癸','破軍','甲乙','禍害','平坦'),
 ('申',110,'壬癸','破軍','甲乙','禍害','寬深'),
 ('庚',110,'丙丁','廉貞',None,None,'平坦'),
 ('酉',110,'丙丁','廉貞',None,None,'深聚'),
 ('辛',110,'丙丁','廉貞',None,None,'平坦'),
 ('戌',110,'甲乙','廉貞','壬癸','六煞','寬深'),
 ('乾',110,'甲乙','廉貞','壬癸','六煞','平坦'),
 ('亥',110,'丙丁','破軍',None,None,'深聚')]
rows=[]
for mountain,page,targets,star,alt,altstar,well in data:
 rows.append({'mountain':mountain,'sourcePDFPage':page,'mainText':{'targets':list(targets),'star':star},
 'marginalText':None if alt is None else {'targets':list(alt),'star':altstar},
 'courtyardWorkingText':'天井宜'+well+'吉','courtyardMeaningEncoded':False})
write('MANUAL_WATER_TABLE.json',{'date':'2026-10-28','sourcePDFPages':[109,110],
 'readingMethod':'24 rows manually entered from raw JPEGs and native crops, not calculated from software or a generated expected table.',
 'sourceHeading':'二十四山放水定局','frameStatement':{'page':109,
 'workingText':'此段是以山龍為主故論山向若脫龍就局則不論陰陽只以福元及門向為局耳',
 'scope':'The table labels 山; source distinguishes mountain-dragon frame from departing it for a 福元/門向局. Automatic conversion between those frames is unresolved.'},
 'directionGranularity':'Literal stem/trigram target marks as printed. No degree sectors, true/magnetic north or geometry inferred.',
 'glyphPolicy':'Canonical 艮/巽/巳 names in working transcription; source images unchanged. Source 祿存 print shape preserved by canonical reading; not full diplomatic transcription.',
 'rows':rows,'mainRows':24,'mainTargetMarkEntries':sum(len(x['mainText']['targets'])for x in rows),
 'marginalRows':sum(x['marginalText']is not None for x in rows),
 'marginalTargetMarkEntries':sum(len(x['marginalText']['targets'])for x in rows if x['marginalText']),
 'sourceOutcomesValidated':False,'hydraulicEngineeringValidated':False})
write('MANUAL_SOURCE_POLARITY.json',{'date':'2026-10-28','sourcePDFPage':107,'sourceHeading':'陰陽山水法',
 'yangWorkingText':'乾甲坤乙坎癸申辰離壬寅戌俱陽也',
 'yinWorkingText':'艮丙巽辛兌丁巳丑震庚亥未俱陰也',
 'yangMarks':list('乾甲坤乙坎癸申辰離壬寅戌'),
 'yinMarks':list('艮丙巽辛兌丁巳丑震庚亥未'),
 'mappingToMountainMarks':{'坎':'子','離':'午','震':'卯','兌':'酉'},
 'normalizationBasis':'The prose sometimes names cardinal trigram 坎/離/震/兌 where the24山 table uses子/午/卯/酉; this conversion is explicit, not a new literal character in source.',
 'notUniversalYinYangSystem':True,'sourceOutcomesValidated':False})
write('MANUAL_ROOM_PAIR_ANCHORS.json',{'date':'2026-10-28','sourcePDFPage':95,
 'rows':[{'rooms':list(pair),'printedRelation':'延年'}for pair in ['乾坤','震巽','坎離','艮兌']],
 'scope':'Four unordered opposite room-trigram pairs explicitly named in the commentary. Both orders are a declared comparison projection, not8 independent printed cases. Not a full first-draw exchange or room geometry adapter.',
 'openingGroups':{'sourcePDFPage':94,'yang':list('乾坎艮震'),'yin':list('巽離坤兌'),
 'scope':'Source own four-yang/four-yin grouping in this passage, not generic trigram sex categories.'},
 'fullFirstDrawExchangeEncoded':False,'sourceOutcomesValidated':False})
notes={
94:'Mở論玄空裝卦訣第五; 帶去三爻呼/入宅為三相/氣口還為初. Chú初 là khí khẩu/cửa; phân乾坎艮震陽 với巽離坤兌陰 trong khung này. Chuyển nhà/phòng và thứ tự hào cần tách; không tự gọi Phi tinh.',
95:'Phân năm chỗ giao門 với năm chỗ換象; có giọng nguồn/chú riêng. Bốn cặp乾坤/震巽/坎離/艮兌 gọi延年; câu金存丙番八卦返復旋 không phải chỉ dẫn mở cửa tùy ý. Chưa chốt toàn phép換象.',
96:'Các ví dụ乾兌/震巽/坤艮/坎 và sinh khắc; có năm/tháng hội局 nhưng chưa thành thuật lịch. Giữ người/phòng/gốc quái riêng.',
97:'Ví dụ thiên-trạch, sinh khắc và hội局; không lấy tênquẻ thiên-trạch thay cung gốc của người. Đọc đầu/chưa đối từng chữ hoặc dự đoán gia đình.',
98:'Các lớp cát hung/cùng âm–dương; giọng phê bình誇張/胡譚. Chuyển sang七卦例, từ生氣/天乙; chú天乙không nằmtrong裝卦nội màtrongkhẩuquyếtkhác.',
99:'Tiếp các例延年/五鬼/六煞/禍害/絕命; các lời rắn/rết/bệnh là lịch sử biểu tượng, chưa xác minh thực tế.',
100:'Kết例 tuyệt命; mở論開門修造門第六, phân gốc cửa với ngày/tháng và kích thước尺. Danh sách忌 nhiều lớp, không tự cộng thành một điểm. Mở門tứmùa là lời nguồn, chưa thành khuyến nghị xây dựng.',
101:'Tiếp mùa tránh cửa; bản年度theocannăm chia vị trí khác tháng. 胎神/月小耗/牛胎/豬胎/天貢/紅嘴朱雀 là bảngkhác, chưa áp mọi lớp lịch.',
102:'門尺 mặttrước/trên và mặttrước/dưới, mặt sau/trên và mặt sau/dưới có nhãn khác;8saochính khôngđược gộp với bảngsau. Chưa chépđủ mọi ô/kíchthước/thướcchuẩn.',
103:'門光星, vòng trắngđen, ngàythánglớn/nhỏ khác chiều; chữ人/Yhình và門戶歌. Không xác lập đơnvịđo/Bắcthực/tọa độ từhình. Bảng ngày cần nhập trực tiếp trước engine.',
104:'用門尺法/尺 trước–sau/8 và10đoạn phân loại; cógiọngphêbình các loại thước truyền trong nước, dẫn魯班. Không quy đổi cm hoặc dùng để chỉ sửa nhà.',
105:'Mởquyểnba/論放水第七. Tách nướctrongnhà/ngoài nhà,中堂/天井 và nướcđến/đi;山陽放陽/陰山放陰 và vídụ dòng nướcxiên. Chưa mặtbằng/độdốc/thủy lực.',
106:'九星水法吉凶斷例; tên sao gắn nướcđến/đi khác nhau. 比喻 miệng/ngũtạng làgiọngnguồn, không lờiykhoa. 巨門/輔弼 cần ngữcảnh, không bảngtốt/xấuphổquát.',
107:'陰陽山水法 có12dấu mỗi nhóm, cặp陰/陽tách rõ. Các quái chínhphương trong câu được ánh xạ cókhai báo sangTý/Ngọ/Mão/Dậu của24sơn. Không nhập mọi hệâm-dươngtừsáchkhác.',
108:'四路黃泉có辰戌丑未水pháquân/巨門phâncát-hung; 九星來朝ảnhhưởngđến/đi. Các lời bệnh/thânthuộc chưa xác minh; không đoántheongườithật.',
109:'Kết nướcđến/đi;二十四山放水定局 mở. Văn nói以山龍為主,脱龍就局thì以福元及門向為局. Nhập8hàng壬–卯 từnguồn, giữ phương chú bên ở寅. Không tự đổi山thànhhướngcửa.',
110:'Tiếp16hàng乙–亥;8hàngtoànbảngcóchúphươngthaythế. 寅main壬癸廉貞;巽/巳main庚辛六煞/chú丙丁巨門;khôngsửatheobảngsuyra. Kếtmở陰陽生命說ghi12chi/6mỗinhóm, chưa gộpvớinhómsơn24.',
111:'Vịtríranhđãđọctrước:圖24山水方向 và mở宅內形. Khôngtínhnguồnmới; chưađốihếtnétchữcủađồvớibảng.'}
write('CONTEXT_READINGS.json',{'date':'2026-10-28','groups':[{'sourcePDFPage':n,'editorialVietnameseSummary':notes[n],
 'fullGlyphCollation':False,'allClausesApplied':False}for n in range(94,112)],
 'newSourceReadPositions':16,'alreadyReadBoundariesExpanded':[94,111],
 'newHTTPRequests':0,'newOriginalContainers':0,'newIndependentWitnesses':0})
qa=json.loads((p/'QA_IMAGES.json').read_text(encoding='utf-8'))
for a in qa:a['actuallyViewed']=True
write('QA_IMAGES.json',qa)
print('24 main drainage rows /46 target entries;8 marginal rows /16 target entries;24 polarity marks;4 printed room pairs.')
