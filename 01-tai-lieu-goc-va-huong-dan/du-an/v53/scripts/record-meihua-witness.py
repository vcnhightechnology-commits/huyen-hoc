"""Record bounded manual image readings, not OCR or a claim to exhaustive reading."""
from pathlib import Path
from hashlib import sha256
import json

root=Path(__file__).resolve().parent.parent
source=root/'research/meihua'
out=root/'research/meihua-witness'
out.mkdir(exist_ok=True)
sha=lambda p:sha256(p.read_bytes()).hexdigest()
write=lambda name,x:(out/name).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
extracted=json.loads((source/'EXTRACTED_PAGES.json').read_text(encoding='utf8'))
images={r['pdfPage']:r for r in extracted['pages']}
notes={
144:('endleaf','卷三終;printed42. Not an imprint.'),
145:('content','梅花易數卷四 title,printed1;opening distinguishes先天/後天 and observer position/motion. This is a printed volume start,not inferred from a later page.'),
146:('content','指迷賦 opening;character form,stroke and birth-element assumptions with historical social/outcome assertions. Not an automatic Unicode classifier.'),
147:('content','指迷賦 conclusion and玄黃剋應歌 opening;external observations are manually selected premises,not observations supplied by the app.'),
148:('content','玄黃剋應歌 continuation and next玄黃敘 heading;heading normalization remains provisional. Source verses on omens are not validated event rules.'),
149:('content','玄黃敘 continuation and玄黃歌 opening;word form and observer judgments,not a deterministic text-to-event mapping.'),
179:('content','土/金/木筆式,時辰斷 and起六神卦訣. The six-spirit clause explicitly says日:甲乙青龍,丙丁朱雀,戊勾陳,己螣蛇,庚辛白虎,壬癸玄武. Do not reinterpret preceding時辰 heading as hour-stem input.'),
180:('content','Six-spirit table has two explicitly printed rows only,甲乙日 and丙丁日,with headings初爻 through六爻 read right-to-left. 辨別五行歌 starts below. Other rows may be derived by rotation but are not separately printed here.'),
181:('content','辨別五行歌 conclusion,辨別六神歌 and五行歌括式 start. Glyph-shape classes depend on handwritten form;Mộc/Thổ/Hỏa/Thủy/Kim are not assigned from Unicode codepoints.'),
182:('content','Mộc-form commentary and干支辨. Long/upright versus short/weak strokes select named symbols. Source explicitly distinguishes陰陽;not a birth-chart day-stem calculation.'),
183:('content','火式:connected/disconnected dots and long/short strokes,then幹支解. Printed shapes and qualitative premises are essential.'),
184:('content','土式 and干支辨;hook/horizontal/vertical/isolated-point conditions and exceptions. No lossless modern font-independent automatic classifier follows from these examples.'),
185:('content','土式 continuation with章/求 examples;金式 starts. Explicit alternatives mean several strokes can change category by shape/context.'),
186:('content','金式 continuation with喜/扒 examples and干支辨;水式 starts. Named stem/branch correspondences are glyph analogies,not a standard calendrical mapping.'),
187:('content','水式 concludes:filled/short horizontal,走之,linked dots,isolated stroke;文/月/景 examples. End of bounded five-form discussion.'),
188:('endleaf','梅花易數卷四終,printed44. Contradicts the earlier guessed start of volume5 atPDF188.'),
189:('content','梅花易數卷五 title,printed1;五行全備 then六神形式/青龍. Full title-page evidence for startPDF189.'),
190:('content','六神形式:朱雀/螣蛇/勾陳/白虎/玄武;八卦辨 begins. Shape assignments and transformations are different from six-spirit day-stem rotation.'),
191:('content','八卦辨 conclusion and貴神/喜神/福星/文星/印星 examples. These named character components are not a Bazi useful-god classifier.'),
192:('content','馬星/祿神/會神/生神/亡神. 祿 has explicitstem→branch list;application here is character divination with stated本人年庚 premise,not automatic event prediction.'),
193:('content','家神/官符/災煞/文書/天狗煞. Illustrative glyphs remain visual evidence;not serialized as faithful Unicode reproductions.'),
194:('content','科名星/喪門/空亡/宜神/忌神. 空亡 example甲子旬戌亥 is retained as a clause;this page does not establish all6xun tables or all context rules.'),
195:('content','主神 distinguishes lifelong本人年干 fromnear-term本日納音 and last-stroke/body-element premises. 用神 selects bysubject;七言作用歌 starts. Do not merge these meanings of用神 with Bazi useful gods.'),
196:('content','七言作用歌 continuation,conditional glyph/stroke prognoses. Not a neutral outcome classifier.'),
197:('content','七言作用歌 conclusion and比例歌 firsttwoexamples;numerical and spatial analogy premises retained separately.'),
198:('content','比例歌 examples3/4,西江月,易理玄微 and斷扇占 start. Source is an interpretive narrative and does not prove a deterministic future event.'),
199:('content','斷扇占 conclusion;買香占 then古人相字. Incensecase contains年月日時 details and隨卦 symbolicreading;historicalstory not new empirical test.'),
200:('content','古人相字 anecdotes continue;printed12,not13. Earlier additional-scan record had off-by-one page identity.'),
201:('content','古人相字 continues through劉/裴/唐/宋/周 anecdotes;printed13. Narrative success reports are not independent validations.'),
202:('content','古人相字 conclusion then斷富貴貧賤要訣. Strokeformandmoral/social/medical assertions retained historically,not user judgments.'),
203:('content','斷富貴貧賤要訣 continues;五行四時旺相休囚例 begins at foot. These class labels are not an overall birth-chart strength score.'),
204:('content','Five-season table contains four namedrows旺/相/休/囚,20cells;no死row printed in this table. Then五行相生地支,天干地支屬五行,論八卦性情 and八卦取象. Do not silently add an unprinted fifth row.'),
205:('content','Eight-trigram symbolconclusion,complete六十甲子歌 and六十四卦次第歌 start.30nayinpairs read;路傍土/井泉水 names kept as printed.'),
206:('content','六十四卦次第歌 conclusion,繫辭八卦類象歌 and渾天甲子定局 firstfour陽palaces. Each line has explicitstem/branch/element andupper/lower label.'),
207:('content','渾天甲子定局 four陰palaces. Explicit右訣從下念上;48assignments across206–207. 後天時方 begins,followed by table that is not fully transcribed in thisscope.'),
208:('content','後天時方 table continuation;bounded reading/navigation only. Not all60rows transcribed or promoted to a prognosis classifier.'),
220:('content','Stroke/objectcorrespondenceverses;printed32,not33. Source includesmoral/sociallabels andmedicaloutcomes,notautomaticrecommendations.'),
228:('endleaf','梅花易數卷之五終,printed40.'),
229:('advertisement','上海文明書局發行;各種尺牘 advertisement. Not a MaiHoa rule or a separateworkread.'),
230:('advertisement','初學新文範/高等新文範 advertisements. Not additional MaiHoa chapters.'),
231:('colophon','Directpublication/distributionlines中華民國十四年十一月出版/發行;publisherandprinter文明書局;title梅花易數(全二冊). Confirms1925-11for thisimprint,not originalauthorshiporfirstedition.')
}
prior={r['pdfPage']for r in json.loads((source/'MANUAL_READINGS.json').read_text(encoding='utf8')).get('pageRecords',[])}
prior|={r['pdfPage']for r in json.loads((root/'research/meihua-reading/MANUAL_READINGS.json').read_text(encoding='utf8'))['records']}
prior|={r['pdfPage']for r in json.loads((root/'research/meihua-reading/ADDITIONAL_SCAN_NOTES.json').read_text(encoding='utf8'))['records']}
records=[]
for n,(kind,note)in sorted(notes.items()):
 r=images[n];assert sha(source/r['file'])==r['sha256']
 records.append({'pdfPage':n,'kind':kind,'image':'../meihua/'+r['file'],'imageSHA256':r['sha256'],'readingLevel':'bounded-manual-page-reading-not-complete-clause-transcription','previouslyRecordedPage':n in prior,'note':note})
write('MANUAL_READINGS.json',{'schema':'hhc.meihua.witness-reading.v1','date':'2026-10-26','sourcePDF':'../meihua/NLC416-12jh005426-44577.pdf','sourcePDFSHA256':extracted['pdfSHA256'],'newExternalResponses':0,'newRenderedDerivatives':87,'retainedRenderedDerivatives':186,'method':'Visual reading of full retained2000pxPNGpages;footer magnificationonly,noOCR.87new renders are not87read pages. TOC9–12reused separately.','records':records,'counts':{'targetedPageRecords':len(records),'contentPageRecords':sum(r['kind']=='content'for r in records),'newContentPageRecords':sum(r['kind']=='content'and not r['previouslyRecordedPage']for r in records),'expandedPriorContentPageRecords':sum(r['kind']=='content'and r['previouslyRecordedPage']for r in records),'endleaves':3,'advertisements':2,'colophon':1},'wholeBookRead':False})
write('EDITION_IDENTITY.json',{'schema':'hhc.meihua.edition-identity.v1','pdfSHA256':extracted['pdfSHA256'],'sourcePages':[145,188,189,228,229,230,231],'imprint':{'evidencePDFPage':231,'publicationLine':'中華民國十四年十一月出版','distributionLine':'中華民國十四年十一月發行','republicYear':14,'month':11,'gregorianYear':1925,'conversion':'Republicyear1=1912;1911+14=1925','dateStatus':'direct-imprint-reading','publisher':'文明書局','printer':'文明書局','publisherLocation':'上海','title':'梅花易數','physicalFormatAsPrinted':'全二冊','textualVolumes':5,'firstEditionEstablished':False,'historicalShaoYongAuthorshipEstablished':False,'catalogOriginIndependentlyVerified':False},'volumeAnchors':[{'volume':3,'endleafPDFPage':144,'printedEndleafPage':42},{'volume':4,'titlePDFPage':145,'printedTitlePage':1,'endleafPDFPage':188,'printedEndleafPage':44},{'volume':5,'titlePDFPage':189,'printedTitlePage':1,'endleafPDFPage':228,'printedEndleafPage':40}],'corrections':[{'target':'../meihua-reading/ADDITIONAL_SCAN_NOTES.json','prior':'Volume5startcandidate188;PDF200printed13;PDF220printed33','corrected':'Volume5titleat189printed1;PDF188isvolume4endleaf44;PDF200printed12;PDF220printed32','reason':'Directtitle/endleafreading andprintedmargins;earlieroffsetinferencewasonepageearly','changesOriginalSourceBytes':False}],'limits':['Thisdatebelongs tothisprintedwitness;not theorigin dateofeverycomponenttext.','Five卷aretextualdivisions;全二冊describesphysicalformat. Theyarenotfivedistinctbooks.','Thefailed directNLCcatalogTLSattempt remainsa failure;readingtheimprintdoesnotreplaceindependentcatalogauthentication.']})
units=[
('four-opening','卷四開篇',[145],'historical-methodological',False),
('zhimi','指迷賦',[146,147],'glyph-and-birth-element-premises',False),
('xuanhuang-response','玄黃剋應歌',[147,148],'observer-dependent-omens',False),
('xuanhuang-preface','玄黃敘',[148,149],'heading-normalization-provisional',False),
('xuanhuang-song','玄黃歌',[149],'partial-verses',False),
('time-passage','時辰斷',[179],'symbolic-time-premises',True),
('six-spirit-start','起六神卦訣',[179,180],'six-start-rules-and-two-explicit-rows-extracted',True),
('five-element-verse','辨別五行歌',[180,181],'glyph-form-rules-no-automatic-classifier',True),
('six-spirit-form-verse','辨別六神歌',[181],'glyph-form-correspondences',True),
('five-forms','五行歌括式',[181,182,183,184,185,186,187],'five-form-discussion-read-but-not-losslessly-transcribed',False),
('five-complete','五行全備',[189],'glyph-form-premises',True),
('six-spirit-forms','六神形式',[189,190],'glyph-forms-distinct-from-day-rotation',True),
('eight-trigram-forms','八卦辨',[190,191],'glyph-form-correspondences',True),
('glyph-stars','貴神至忌神',[191,192,193,194],'named-character-components-and-birth-context',False),
('principal-reference','主神',[195],'explicit-distinct-lifelong-versus-near-term-premises',True),
('use-reference','用神',[195],'subject-dependent-reference-not-Bazi-useful-god',True),
('seven-word-song','七言作用歌',[195,196,197],'historical-glyph-prognoses',False),
('analogy-song','比例歌',[197,198],'four-analogy-examples',True),
('xijiangyue','西江月',[198],'literary-methodological',True),
('subtle-principles','易理玄微',[198],'historical-anecdote',True),
('fan-case','斷扇占',[198,199],'historical-anecdote-not-validated',True),
('incense-case','買香占',[199],'historical-anecdote-not-validated',True),
('character-anecdotes','古人相字',[199,200,201,202],'historical-anecdotes-not-validated',False),
('wealth-social-maxims','斷富貴貧賤要訣',[202,203],'historical-social-medical-stereotypes-research-only',False),
('season-table','五行四時旺相休囚例',[203,204],'20literal-cells-four-rows-no-unprinted-dead-row',True),
('branch-birth','五行相生地支',[204],'separate-symbolic-method-not-strength-engine',True),
('stem-branch-elements','天干地支屬五行',[204],'named-correspondences',True),
('trigram-character','論八卦性情',[204],'symbolic-correspondences',True),
('trigram-symbols','八卦取象',[204,205],'symbolic-correspondences',True),
('nayin','六十甲子歌',[205],'30sourcepairs-cross-check-real-engine',True),
('hex-order','六十四卦次第歌',[205,206],'mnemonic-order-not-new-casting-algorithm',True),
('trigram-analogy','繫辭八卦類象歌',[206],'symbolic-correspondences',True),
('najia','渾天甲子定局',[206,207],'48literal-assignments-research-only-complete-table',True),
('hour-directions','後天時方',[207,208],'table-partial-not-complete60rows',False)
]
write('UNIT_MAP.json',{'schema':'hhc.meihua.witness-units.v1','scope':'34boundedunitgroups inselectedpages ofvolumes4/5;not acompleteprintedunitinventory. Groupedstarheadingsarekeptonegroup,notinflatedasfullyreadchapters.','units':[{'id':i,'heading':t,'evidencePDFPages':p,'disposition':d,'boundedUnitEndObserved':closed,'wholeUnitApplied':False}for i,t,p,d,closed in units],'stillUnmappedBodyPDFPages':list(range(150,179))+list(range(209,220))+list(range(221,228)),'wholePrintedInventoryCompleted':False})
names=['青龍','朱雀','勾陳','螣蛇','白虎','玄武']
starts={'甲':'青龍','乙':'青龍','丙':'朱雀','丁':'朱雀','戊':'勾陳','己':'螣蛇','庚':'白虎','辛':'白虎','壬':'玄武','癸':'玄武'}
write('SIX_SPIRITS.json',{'schema':'hhc.meihua.six-spirits.v1','context':'卷四character/stroke-divinationappendix;not acompletedLiuYaosystem. 六神形式in卷五isadifferentglyph-formclassification.','startSourcePDFPage':179,'tableSourcePDFPage':180,'order':names,'inputPremise':'Explicitdayheavenlystem;sourcewrites日,notarbitraryhourstemorbirthyear.','starts':starts,'literalPrintedRows':[{'dayStems':['甲','乙'],'linesBottomToTop':names},{'dayStems':['丙','丁'],'linesBottomToTop':['朱雀','勾陳','螣蛇','白虎','玄武','青龍']}],'derivedRowsArePrintedRows':False,'derivation':'Continue the six-name order cyclically from the explicitly prescribed firstline;fouradditionalrotationsareimplementationinference,separatefromthetwoprintedrows.','consumerApplied':False})
elements={'木':'Mộc','火':'Hỏa','土':'Thổ','金':'Kim','水':'Thủy'}
write('SEASON_TABLE.json',{'schema':'hhc.meihua.seasons.v1','sourcePDFPage':204,'heading':'五行四時旺相休囚例','columnOrder':['春','夏','秋','冬','四季之月'],'rows':{'旺':['木','火','金','水','土'],'相':['火','土','水','木','金'],'休':['水','木','土','金','火'],'囚':['土','金','木','火','水']},'literalCells':20,'unprintedRows':['死'],'premisesStillOpen':['Exact calendar boundaries for seasons/four-seasonmonths.','Priority ofmonth/day andotherconditionalrules.','Howthisnamedtableinteractswithotherstrengthtraditions.'],'consumerApplied':False,'notOverallLuckScore':True})
triples={
1:('乾',['甲子水','甲寅木','甲辰土'],['壬午火','壬申金','壬戌土']),
2:('兌',['丁巳火','丁卯木','丁丑土'],['丁亥水','丁酉金','丁未土']),
3:('離',['己卯木','己丑土','己亥水'],['己酉金','己未土','己巳火']),
4:('震',['庚子水','庚寅木','庚辰土'],['庚午火','庚申金','庚戌土']),
5:('巽',['辛丑土','辛亥水','辛酉金'],['辛未土','辛巳火','辛卯木']),
6:('坎',['戊寅木','戊辰土','戊午火'],['戊申金','戊戌土','戊子水']),
7:('艮',['丙辰土','丙午火','丙申金'],['丙戌土','丙子水','丙寅木']),
8:('坤',['乙未土','乙巳火','乙卯木'],['癸丑土','癸亥水','癸酉金'])}
write('NAJIA_TABLE.json',{'schema':'hhc.meihua.najia.v1','sourcePDFPages':[206,207],'heading':'渾天甲子定局','instructionAsRead':'右訣從下念上','orientation':'Each3-itemarrayisbottom-to-topwithinitsownhalf;lowerpopulateslines1..3,upperlines4..6. Printedtableisreadupward.','trigramNumbering':'CurrentMaiHoaQian1,Dui2,Li3,Zhen4,Xun5,Kan6,Gen7,Kun8;indexisappconvention,notnewsourceclaim.','records':[{'trigram':n,'han':t,'lowerBottomToTop':lo,'upperBottomToTop':up,'sourcePDFPage':206 if n in[1,4,6,7] else 207}for n,(t,lo,up)in triples.items()],'literalAssignments':48,'elementTranslation':elements,'consumerApplied':False,'remaining':['AnotheridentifiedwitnessandfullschoolpremisesbeforepublicLiuYaofunction.','Palace,世應,六親,伏神,moving/changedrelationsandconditionalreadingarenotestablishedbythistablealone.'],'wholeLiuYaoImplemented':False})
pairs=[('甲子乙丑','海中金'),('丙寅丁卯','爐中火'),('戊辰己巳','大林木'),('庚午辛未','路傍土'),('壬申癸酉','劍鋒金'),('甲戌乙亥','山頭火'),('丙子丁丑','澗下水'),('戊寅己卯','城頭土'),('庚辰辛巳','白蠟金'),('壬午癸未','楊柳木'),('甲申乙酉','井泉水'),('丙戌丁亥','屋上土'),('戊子己丑','霹靂火'),('庚寅辛卯','松柏木'),('壬辰癸巳','長流水'),('甲午乙未','沙中金'),('丙申丁酉','山下火'),('戊戌己亥','平地木'),('庚子辛丑','壁上土'),('壬寅癸卯','金箔金'),('甲辰乙巳','覆燈火'),('丙午丁未','天河水'),('戊申己酉','大驛土'),('庚戌辛亥','釵釧金'),('壬子癸丑','桑柘木'),('甲寅乙卯','大溪水'),('丙辰丁巳','沙中土'),('戊午己未','天上火'),('庚申辛酉','石榴木'),('壬戌癸亥','大海水')]
write('NAYIN_PAIRS.json',{'schema':'hhc.meihua.nayin-witness.v1','sourcePDFPage':205,'heading':'六十甲子歌','pairs':[{'index':i,'ganzhi':[g[:2],g[2:]],'printedName':name,'elementHan':name[-1],'elementVI':elements[name[-1]]}for i,(g,name)in enumerate(pairs)],'knownLabelVariants':[{'source':'路傍土','currentEngine':'路旁土','kind':'character-variant-in-label'},{'source':'井泉水','currentEngine':'泉中水','kind':'traditional-name-variant-not-element-conflict'}],'productChange':False,'predictionValidated':False})
print(json.dumps({'pageRecords':len(records),'unitGroups':len(units),'newDerivatives':87,'retainedDerivatives':186,'nayinPairs':len(pairs),'najiaAssignments':48,'seasonCells':20},ensure_ascii=False))

