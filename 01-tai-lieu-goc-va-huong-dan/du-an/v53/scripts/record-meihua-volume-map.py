"""Retain bounded visual readings; no OCR, HTTP or consumer source mutation."""
from pathlib import Path
from hashlib import sha256
import json

root = Path(__file__).resolve().parent.parent
base = root / 'research/meihua-volume-map'
base.mkdir(parents=True, exist_ok=True)
read = lambda p: json.loads(p.read_text(encoding='utf-8-sig'))
def write(name, value):
    (base / name).write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')

notes = {
150: '玄黃歌 concludes;花押賦 begins. Signature/heart-seal and stroke/element/六神 analogies require the actual written form; not a Unicode-to-fortune formula.',
151: '花押賦 concludes and探玄賦 begins. Signature/stroke metaphors and social/family outcome claims are historical assertions, not validated predictions.',
152: '探玄賦 continuation: object/form/movement analogies, moral and social forecasts; observer judgments remain premises.',
153: '探玄賦 concludes;齊景至理論 heading at the left foot. Its body starts on154; chapter title is kept as a bounded reading.',
154: '齊景至理論: retrospective wordplay/anecdotes and heart/pen claims; not new empirical validation or an automatic glyph classifier.',
155: '齊景至理論 concludes;字畫經驗 starts. Five labelled glyph anecdotes:殿家判硯典. Context and timing belong to each narrative.',
156: '字畫經驗 continues with12labelled examples:果馬來癸但謙亨達奇俊常每. They are printed stories, not12independent successful forecasts.',
157: '字畫經驗 continues with城池春一盆田;字體詩訣 begins. The23labelled examples across155–157 are narrative examples, not stroke-count fixtures.',
158: '字體詩訣 continuation; character-specific seasonal/family/illness/death assertions. These do not define a general numeric casting method.',
159: '字體詩訣 continuation: subject-specific glyph components and family/travel/material outcome verses, with contextual judgment.',
160: '字體詩訣 concludes. 四季水筆 prints春水昏濁/夏水枯涸/秋水澄清/冬水凝結. 畫有陰陽 heading begins; seasonal brush metaphors are not meteorological measurements.',
161: '畫有陰陽 treats relative length, weight and mixed yin/yang qualities;八卦斷 includes an extra勾陳clause among trigram clauses. Do not add a ninth trigram or infer shape from stroke parity.',
162: '新訂指明心法 umbrella;相字心易,辨字式,筆法筌蹄. Character order and actual handwriting matter. Historical social-role generalizations are not product user classifications.',
163: '歌曰 is a poem within筆法筌蹄, with qualitative stroke/style outcomes; retain hierarchy rather than counting a new independent work.',
164: '奴婢,陰人,隔手,then a勢heading and象人 opening. 勢heading is visually uncertain between視勢/觀勢; no silently fixed reading. Historical gender/status assertions remain private.',
165: '象人 concludes;有所喜/有所忌/有所聞/有所見/以時而言 and以卦而斷 heading. Component, sound, rain/dog and season observations are explicit missing premises for typed text.',
166: '以卦而斷 continues;以禽獸而斷,取類而言,以次而言,當添亦添;當減亦減 heading. Whole-form/order/context may override component splitting.',
167: '當減亦減 continues;筆畫長短,偏旁侵客,字畫指迷 opening. 吉 differs by relative土/士shape, not by a code-point change; health/lifespan analogies are historical claims.',
168: '字畫指迷 offers alternative timing readings, including several incompatible辛dates;問婚姻 begins. Alternatives are not a unique calculated event date.',
169: '問婚姻 concludes;官事 and疾病. Stroke-element/illness/ghost claims are not a medical diagnosis engine.',
170: '疾病 concludes;六甲,求謀,行人遠信,官貴. Pregnancy/sex/death claims and travel-letter analogies are retained as historical material, not consumer determinations.',
171: '失物,問壽,功名,行人. 行人 is separate from行人遠信. Handwriting-to-lifespan assertions must not become a lifespan forecast.',
172: '反體 rejects a universally positive interpretation of喜/慶/星;六神筆法 shows glyph figures, then六神主事 begins. 螣蛇 has無正位here; not a missing cyclic day-stem row.',
173: '六神主事 continues with static/moved conditions;青龍形式/朱雀形式/勾陳形式 and螣蛇形式 heading. These forms are distinct from day-stem cyclic六神.',
174: '螣蛇形式 continuation;白虎形式/玄武形式;筆畫犯煞 figures with labels. Glyph-shaped煞categories require form observation; no numeric assignment from the displayed text.',
175: '玄黃筆法歌 begins: radical/stroke figures, positions and contextual warnings; the four-dot火claim is a handwriting interpretation, not scientific element recognition.',
176: '玄黃筆法歌 continues with glyph fragments and analogies, including person, curved/repeated strokes and door-like forms; keep contextual alternatives.',
177: '玄黃筆法歌 continues with卓/邑/禮/月骨/身/山-like figures; not a second independent glyph-recognition system.',
178: '玄黃筆法歌 concludes;五行體格式 opens with水筆式 and火筆式 figures. Shape-dependent categories continue on179.',
209: '後天時方 table continuation:12row keys庚辰through辛卯, each with12branch columns. Label entries read for navigation, not fully transcribed or validated as predictions.',
210: '後天時方 continuation:12row keys壬辰through癸卯. Printed branch glyph己in table columns must not silently substitute for the stem己in another context.',
211: '後天時方 continuation:12row keys甲辰through乙卯; several labels have short/variant forms. No interpolation from an assumed regular cycle.',
212: '後天時方 final8keys丙辰through癸亥;八反格 then四言獨步 heading. Table totals60rows over207–212, not60works or720verified prognoses.',
213: '四言獨步 body:下筆是我/其餘是他,用神末筆,relative strength/season and glyph analogies. This用神 is not the moving trigram of MaiHoa or the Bazi useful-god classifier.',
214: '四言獨步 concludes, including stroke-to-lifespan arithmetic and exceptions. Retain historical claims; do not ship deterministic lifespan values or count these as validated rules.',
215: '五言作用歌;別理論 heading at the left foot. Verse explicitly says十人寫一字筆法各不同and warns against rigid judgment; identical typed text lacks that observation.',
216: '別理論 continuation: same character/event may change outcome; component and role examples. Different premises are not permission to select only successful retrospective stories.',
217: '別理論 continues with大/小/赤子/香/田and social-role readings. Form, question and observer interpretation remain unprovided by ordinary text.',
218: '別理論 concludes;六言剖斷歌 begins with dry/sparse/small versus clear/strong brush distinctions and further stroke-to-age claims; not empirical age calculation.',
219: '六言剖斷歌 concludes;格物章 starts. Scale,weight and relative material/form analogies underpin lifespan/status claims; they are not the trượng–thước casting adapter.',
221: '格物章 concludes;物理論 begins. Classical cosmological/form analogies and respect-for-teacher claims are historical prose, not modern physical laws.',
222: '物理論 continues with water/weather/cloud/snow/fire/season analogies and context-dependent human outcomes. These are not weather data or a forecast API.',
223: '物理論 concludes with warnings about rigid single-ended judgment; object-use/transformation analogies have contextual premises, not a universal element score.',
224: '五行六神辨別論 begins. 五行first,六神second; season, shape, question, relational strength and exceptions matter. Do not turn co-occurring symbols into an unconditional good/bad score.',
225: '五行六神辨別論 concludes, followed by金聲章 opening. 宅uses本命and五行旺弱here, not a complete flying-star chart rule.',
226: '金聲章 continuation: cosmology,writing,animals/materials,sound and season metaphors; distinguishes light/heavy/clear/turbid contextual forms.',
227: '金聲章 concludes. Its closing望梅/鏡花水月and contextual writing metaphors do not introduce a new time/count casting algorithm or validate predicted human outcomes.'
}
expected = set(range(150,179)) | set(range(209,220)) | set(range(221,228))
assert set(notes) == expected and len(notes) == 47
records = []
for page, note in sorted(notes.items()):
    image = root / f'research/meihua/images/p{page}.png'
    records.append({'pdfPage': page, 'volume': 4 if page < 189 else 5,
                    'printedPage': page-144 if page < 189 else page-188,
                    'image': f'../meihua/images/p{page}.png', 'imageSHA256': sha256(image.read_bytes()).hexdigest(),
                    'readingLevel': 'visual-heading-boundary-and-bounded-clause-reading-not-full-transcription',
                    'note': note})
write('MANUAL_READINGS.json', {
    'schema':'hhc.meihua.volume-map-readings.v1','date':'2026-10-26',
    'sourcePDF':'../meihua/NLC416-12jh005426-44577.pdf',
    'sourcePDFSHA256':'af608094ab11ae209eae91a9365565e7c9cff604aac3da5e753e04d1cc4598c0',
    'newHTTPResponses':0,'newRenderedDerivatives':0,'newPageRecords':47,
    'boundaryPagesReinspected':[207,208,220,228],
    'method':'Direct visual reading of retained full-page PNG derivatives. No OCR. Notes retain premises and uncertain headings; page navigation is not complete clause transcription or proven prediction.',
    'records':records,'wholeBookRead':False,'wholeBookApplied':False})

# Printed unit locations, not a flattened list of fully extracted algorithms.
new_units = [
('huaya','花押賦',150,151,'signature-form-premises'),
('tanxuan','探玄賦',151,153,'historical-form-and-outcome-verses'),
('qijing','齊景至理論',153,155,'methodological-and-narrative'),
('glyph-experience','字畫經驗',155,157,'23-labelled-historical-anecdotes'),
('glyph-verses','字體詩訣',157,160,'character-specific-historical-outcome-verses'),
('seasonal-water-brush','四季水筆',160,160,'four-literal-brush-metaphors-research-only'),
('stroke-yinyang','畫有陰陽',160,161,'relative-shape-not-stroke-parity'),
('trigram-judgments','八卦斷',161,161,'symbolic-clauses-including-extra-gouchen'),
('new-heart-method','新訂指明心法',162,178,'umbrella-not-separate-algorithm'),
('glyph-heart-yi','相字心易',162,162,'question-and-character-order-premises'),
('glyph-style','辨字式',162,162,'historical-social-stereotypes'),
('brush-quanti','筆法筌蹄',162,163,'qualitative-handwriting-premises'),
('brush-poem','歌曰',163,163,'subunit-of-brush-quanti'),
('servants','奴婢',164,164,'historical-status-claims'),
('yin-person','陰人',164,164,'historical-gender-claims'),
('indirect-hand','隔手',164,164,'writer-versus-questioner-premise'),
('form-momentum','視勢／觀勢',164,164,'heading-reading-uncertain'),
('person-analogy','象人',164,165,'glyph-component-and-person-analogy'),
('observed-favour','有所喜',165,165,'observed-form-and-subject-premises'),
('observed-taboo','有所忌',165,165,'observed-form-and-subject-premises'),
('observed-hearing','有所聞',165,165,'manual-external-sound-premise'),
('observed-sight','有所見',165,165,'manual-external-sight-premise'),
('according-to-time','以時而言',165,165,'season-premise-not-complete-strength-method'),
('according-to-trigram','以卦而斷',165,166,'season-and-trigram-premises'),
('according-to-animals','以禽獸而斷',166,166,'animal-analogy-not-animal-recognition'),
('by-class','取類而言',166,166,'whole-glyph-context-not-compulsory-splitting'),
('by-sequence','以次而言',166,166,'writing-order-premise'),
('adding-components','當添亦添',166,166,'contextual-component-addition'),
('removing-components','當減亦減',166,167,'contextual-component-subtraction'),
('stroke-length','筆畫長短',167,167,'relative-length-not-Unicode-or-numeric-parity'),
('component-invasion','偏旁侵客',167,167,'geometric-stroke-premises'),
('glyph-guide','字畫指迷',167,168,'multiple-alternative-readings-and-timings'),
('glyph-marriage','問婚姻',168,169,'historical-domain-claims'),
('glyph-litigation','官事',169,169,'historical-domain-claims'),
('glyph-illness','疾病',169,170,'historical-medical-claims-not-diagnosis'),
('glyph-pregnancy','六甲',170,170,'historical-pregnancy-sex-and-death-claims'),
('glyph-seeking','求謀',170,170,'subject-form-and-birth-element-premises'),
('traveller-letter','行人遠信',170,170,'historical-travel-letter-claims'),
('official-status','官貴',170,170,'historical-social-role-claims'),
('lost-object','失物',171,171,'historical-location-claims'),
('glyph-lifespan','問壽',171,171,'historical-lifespan-claims-not-forecast'),
('glyph-career','功名',171,171,'historical-social-role-claims'),
('traveller','行人',171,171,'distinct-heading-from-traveller-letter'),
('contrary-forms','反體',172,172,'counterexample-to-positive-word-classifier'),
('brush-six-spirits','六神筆法',172,172,'glyph-form-system-not-day-stem-cycle'),
('six-spirit-affairs','六神主事',172,173,'conditional-static-versus-moved-premise'),
('six-shape-subheadings','青龍形式至玄武形式',173,174,'six-grouped-glyph-form-subheadings'),
('stroke-sha','筆畫犯煞',174,174,'glyph-figure-premises'),
('xuanhuang-brush-song','玄黃筆法歌',175,178,'glyph-fragment-and-form-verses'),
('five-body-forms','五行體格式',178,179,'five-grouped-stroke-form-subheadings'),
('eight-reversals','八反格',212,212,'short-contrary-outcome-verse'),
('four-word-dubu','四言獨步',212,214,'last-stroke-use-premises-and-historical-lifespan-claims'),
('five-word-use','五言作用歌',215,215,'different-handwriting-and-conditional-use'),
('other-principles','別理論',215,218,'same-word-different-context-methodology'),
('six-word-analysis','六言剖斷歌',218,219,'form-strength-and-historical-lifespan-claims'),
('investigating-objects','格物章',219,221,'material-form-analogies-not-measurement-casting'),
('object-principles','物理論',221,223,'classical-cosmological-and-contextual-analogies'),
('elements-spirits-distinction','五行六神辨別論',224,225,'conditional-element-spirit-and-question-premises'),
('gold-sound','金聲章',225,227,'cosmological-writing-and-object-metaphors')]
prior = read(root/'research/meihua-witness/UNIT_MAP.json')
units = json.loads(json.dumps(prior['units']))
for u in units:
    u['provenance'] = '../meihua-witness/UNIT_MAP.json'
    u['fullClauseExtractionCompleted'] = False
    if u['id'] == 'xuanhuang-song':
        u['evidencePDFPages'] = [149,150]
        u['disposition'] = 'historical-form-and-outcome-verses'
        u['boundedUnitEndObserved'] = True
    if u['id'] == 'hour-directions':
        u['evidencePDFPages'] = list(range(207,213))
        u['disposition'] = '60-row-key-navigation-cell-transcription-open'
        u['boundedUnitEndObserved'] = True
for idn, heading, first, last, disposition in new_units:
    u = {'id':idn, 'heading':heading, 'evidencePDFPages':list(range(first,last+1)),
         'disposition':disposition,'boundedUnitEndObserved':True,
         'fullClauseExtractionCompleted':False,'wholeUnitApplied':False,
         'provenance':'MANUAL_READINGS.json'}
    if idn in ['new-heart-method','brush-poem']:
        u['unitKind'] = 'umbrella' if idn == 'new-heart-method' else 'poem-subunit'
    if idn == 'form-momentum':
        u['headingUncertain'] = True
        u['doNotSilentlyNormalize'] = True
    units.append(u)
assert len({u['id'] for u in units}) == len(units)
old_read = read(root/'research/meihua-witness/MANUAL_READINGS.json')
mapped = sorted(expected | {r['pdfPage'] for r in old_read['records'] if 145 <= r['pdfPage'] <= 228})
assert mapped == list(range(145,229))
write('UNIT_MAP.json', {
    'schema':'hhc.meihua.volume-map-units.v1', 'source':'../meihua/NLC416-12jh005426-44577.pdf',
    'previousUnitMap':'../meihua-witness/UNIT_MAP.json','priorUnitGroups':34,'newUnitGroups':len(new_units),
    'scope':'Printed volumes4/5 page navigation and bounded rule/premise disposition. Groups and nested units are not independent works or a complete clause inventory.',
    'units':units,'mappedPDFPages':mapped,'contentPages':82,'endleafPages':[188,228],
    'volumeFourFivePageNavigationComplete':True,'wholePrintedClauseInventoryCompleted':False,
    'wholePrintedInventoryCompleted':False,'wholeBookApplied':False,
    'stillUnmappedBodyPDFPages':[],
    'remaining':['Volumes1–3 need the same physical-page/unit/clause coverage, not only the three digital transcriptions.',
                 'Groupedstar191–194,shape subheadings and ambiguous headings still need line-level indexing and comparison.',
                 'Table207–212 needs literal cells/variants, input semantics and an identified comparison witness.',
                 'Every potentially reproducible rule needs complete conditions and explicit observer/handwriting premises; historical outcome claims are not validated predictions.']})

branches = '子丑寅卯辰巳午未申酉戌亥'
# Literal row headers read right-to-left on each image, not filled from a cycle.
row_pages = [(207,'甲子 乙丑 丙寅 丁卯'),
             (208,'戊辰 己巳 庚午 辛未 壬申 癸酉 甲戌 乙亥 丙子 丁丑 戊寅 己卯'),
             (209,'庚辰 辛巳 壬午 癸未 甲申 乙酉 丙戌 丁亥 戊子 己丑 庚寅 辛卯'),
             (210,'壬辰 癸巳 甲午 乙未 丙申 丁酉 戊戌 己亥 庚子 辛丑 壬寅 癸卯'),
             (211,'甲辰 乙巳 丙午 丁未 戊申 己酉 庚戌 辛亥 壬子 癸丑 甲寅 乙卯'),
             (212,'丙辰 丁巳 戊午 己未 庚申 辛酉 壬戌 癸亥')]
rows = []
for page, keys in row_pages:
    for key in keys.split():
        n = len(rows)
        rows.append({'ordinal':n+1,'ganzhi':key, 'pdfPage':page,
                     'readingStatus':'row-key-verified-against-full-page-image','cellLabelsTranscribed':False})
write('HOUR_TABLE_INDEX.json', {
    'heading':'後天時方','evidencePDFPages':list(range(207,213)),
    'method':'Manual full-page check of row-key sequence and page transitions; sexagenary spelling normalized with explicit 己/巳 caution. No cell-label inference.',
    'branchColumns':list(branches),'rows':rows,'rowKeys':60,'labelCellPositions':720,
    'literalLabelCellsTranscribed':0,'completeCastingOrPredictionAlgorithm':False,
    'sourceIntroBoundedReading':'PDF207:子日子罡起;子/辰/丑/戌qualifications occur in the short introduction. Input scope and all label glosses are not established by a row heading alone.',
    'ambiguities':['Printed己-shapedbranch column stands where normalized巳belongs; do not confuse with the stem己.',
                   'Multi-character and short/variant labels occur,especially the first rows; no forced one-label vocabulary.',
                   'Do not calculate all720labels from one assumed rotation.'],
    'consumerApplied':False})
write('BOUNDED_EXTRACTS.json', {
    'scope':'Literal small extracts and negative controls; historical source claims, not empirical human predictions.',
    'seasonalWaterBrush':{'pdfPage':160,'rows':[
        {'season':'春','waterMetaphor':'昏濁'}, {'season':'夏','waterMetaphor':'枯涸'},
        {'season':'秋','waterMetaphor':'澄清'}, {'season':'冬','waterMetaphor':'凝結'}],
        'notEquivalentTo':'旺相休囚table204 or meteorological data'},
    'brushSpirits':{'pdfPage':172,'rows':[
        {'name':'青龍','element':'木'}, {'name':'朱雀','element':'火'}, {'name':'勾陳','element':'土'},
        {'name':'螣蛇','element':None,'printedQualification':'無正位'},
        {'name':'白虎','element':'金'}, {'name':'玄武','element':'水'}],
        'notEquivalentTo':'day-stem cyclic六神179–180; the printed螣蛇qualification is not a missing day-stem assignment'},
    'glyphAnecdoteLabels':[{'pdfPage':155,'glyphs':list('殿家判硯典')},
                          {'pdfPage':156,'glyphs':list('果馬來癸但謙亨達奇俊常每')},
                          {'pdfPage':157,'glyphs':list('城池春一盆田')}],
    'anecdotesAreIndependentValidation':False,
    'negativeControls':[
        {'pages':[161],'premise':'八卦斷alsohas勾陳clause','prohibitedInference':'a ninth trigram'},
        {'pages':[167],'premise':'吉 土/士relative stroke proportions','prohibitedInference':'typed code point or total-stroke parity fully specifies the form'},
        {'pages':[168],'premise':'Several alternative辛timings','prohibitedInference':'unique event-date algorithm'},
        {'pages':[172],'premise':'反體context can reverse喜/慶/星','prohibitedInference':'positive-word fortune classifier'},
        {'pages':[215],'premise':'十人寫一字筆法各不同','prohibitedInference':'same typed character supplies all handwriting observations'},
        {'pages':[213],'premise':'末筆用神in glyph chapter','prohibitedInference':'same reference as MaiHoa moving trigram or Bazi useful god'},
        {'pages':[214,218,219],'premise':'Stroke/material-to-lifespan claims','prohibitedInference':'validated lifespan forecasts'}],
    'consumerApplied':False,'newPredictiveAccuracyEstablished':False})
print(json.dumps({'newPageRecords':47,'allVolume4and5Pages':len(mapped),'contentPages':82,
                  'newUnitGroups':len(new_units),'totalUnitGroups':len(units),'rowKeys':len(rows)},ensure_ascii=False))
