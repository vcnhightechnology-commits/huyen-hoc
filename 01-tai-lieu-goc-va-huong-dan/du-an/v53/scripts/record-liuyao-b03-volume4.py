from pathlib import Path
from hashlib import sha256
import json, shutil

root = Path(__file__).resolve().parent.parent
base = root / 'research/liuyao-b03-volume4'
prior = root / 'research/liuyao-b03-volume3'
base.mkdir(parents=True, exist_ok=True)
(base / 'images').mkdir(exist_ok=True)
read = lambda p: json.loads(p.read_text(encoding='utf-8-sig'))
digest = lambda p: sha256(p.read_bytes()).hexdigest()
def write(name, value):
    (base / name).write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

a = read(prior / 'ACQUISITION.json')
assert digest(prior / a['file']) == 'c1e1027331d43769733c6011b4fe99e90928e9fde013fce563c8e9bad81c04bf'
topics = {
30: '卷之四 title, authorship lines, 黃金策總斷千金賦直解, 動靜陰陽反覆遷變',
31: '過不及, 生扶拱合; exceptions and relative strength rather than a fixed total score',
32: '克害刑沖, 長生帝旺, 死墓絕空, 日辰; strength qualifications and source criticisms',
33: '月建, 太歲, 卦身, 世應 and temporal scales; 卦身 kept distinct from 世身',
34: '動始變終, 世應 roles, 世應俱空, 內外競發; contextual subject selection',
35: '用神有傷須救, 無故勿空; 傷/有故/無故 qualifications, no unconditional void verdict',
36: '空逢沖而有用, 合遭破以無功, 自空化空, 刑合剋合; asking purpose changes interpretation',
37: '動逢合而絆住, 靜得沖而暗興, 入墓難剋帶旺匪空, 有助有扶; explicit 日辰 and 旺衰',
38: '貪生貪合, 別衰旺辨動靜, 併/沖; a day branch does not automatically make a weak line strong',
39: '三刑 and 三合 complete-member conditions, moving-line premise, 月建/令星, 飛伏提拔',
40: '日月制爻, 日傷爻/爻傷日, 墓中不沖不發, 世官, 德合 and harmful-line control',
41: '忌神受制, 土墓, 有用無用空化空, 十二長生 stages; no mechanical one-word verdict',
42: '沐浴/敗 qualifications, 回頭剋/生合, 日辰併起, 重疊/墓庫, 世應間爻',
43: '進退, 生合帶刑害, 刑害死絕, 動逢沖; intent and strength conditions retained',
44: '絕逢生, 合待沖, 休囚生旺, 應期; source explicitly calls for flexible 月/日 horizons',
45: '父/福/鬼/財/兄 roles by question; 卦身/月卦身, not blanket good/bad relatives',
46: '動變, 六獸, 龍虎玄朱; spirits alone cannot determine fortune, context of 生剋制化',
47: 'Relative weighting, six spirits and five elements, methodological/ritual claims; data not instructions',
48: '何幼子 quotation and 全篇總說; explicit 卜筮正宗卷之四終',
49: 'Final cover/stamp only; no new textual-volume content',
}
records = []
for n in range(30, 50):
    if n >= 33:
        src = root.parent / f'tmp/liuyao-b03-book2-rest/bushi-book2-{n}.png'
        target = base / f'images/bushi-book2-{n}.png'
        if not target.exists():
            shutil.copy2(src, target)
        assert digest(src) == digest(target)
        image_path = f'images/bushi-book2-{n}.png'
    else:
        target = prior / f'images/bushi-book2-{n}.png'
        image_path = f'../liuyao-b03-volume3/images/bushi-book2-{n}.png'
    records.append({'pdfPage': n, 'image': image_path, 'sha256': digest(target),
        'topic': topics[n], 'scope': 'cover-only' if n == 49 else 'full-first-pass-volume4-relevant-span',
        'newLocalRender': n >= 33, 'expandedEarlierBoundedReading': n < 33,
        'entirePageDiplomaticallyTranscribed': False})
write('MANUAL_READINGS.json', {'date': '2026-10-27', 'sourceID': 'B03-book2',
    'sourcePDF': '../liuyao-b03-volume3/' + a['file'], 'sourceSHA256': a['sha256'],
    'records': records, 'counts': {'manualRecords': 20, 'newLocalRenders': 17,
        'newContentPages': 16, 'newCoverPages': 1, 'expandedEarlierBoundedPages': 3,
        'volume4ContentSpanPages': 19},
    'opening': {'pdfPage': 30, 'literalTitle': '卜筮正宗卷之四',
        'literalSection': '黃金策總斷千金賦直解', 'boundedCompilerReading': '古吳洞庭西山王維德洪緒註'},
    'ending': {'pdfPage': 48, 'literalReading': '卜筮正宗卷之四終'},
    'physicalBook2PageCoverage': {'priorScopePages': list(range(1, 33)),
        'expandedPages': [30, 31, 32], 'newlyReadPages': list(range(33, 50)), 'unreadPages': []},
    'newOriginalPDFs': 0, 'newHTTPBodies': 0, 'ocrUsed': False,
    'firstPassRelevantSpanReadIsNotExhaustiveApplication': True,
    'wholePhysicalBookApplied': False, 'all14TextualVolumesApplied': False})

groups = [('water-trine', '三合', '申子辰'), ('fire-trine', '三合', '寅午戌'),
          ('metal-trine', '三合', '巳酉丑'), ('wood-trine', '三合', '亥卯未'),
          ('tiger-snake-monkey', '三刑', '寅巳申'), ('ox-dog-goat', '三刑', '丑戌未')]
write('TRIAD_TABLES.json', {'date': '2026-10-27', 'sourceID': 'B03-book2', 'pdfPage': 39,
    'groups': [{'id': i, 'kind': k, 'members': list(b)} for i, k, b in groups],
    'literalBoundedReading': '三刑三合之法皆須見全有兩爻動則刑合得成',
    'normalization': {'complete': 'One observed primary line for each distinct member branch.',
        'moving': 'At least two moving lines within that three-line witness.',
        'atLeastTwoIsOperationalInterpretationNotAnAdditionalLiteralQuote': True},
    'scope': 'Primary six-line structural prerequisites only; no changed-line/day/month completion.',
    'otherSourceExamplesNotCompiledHere': ['子卯相刑', '辰午酉亥自刑'],
    'effectiveFormationEstablished': False, 'consumerApplied': False})

clauses = [
('over-under', [31], '過與不及須按問事、動靜及日月等分辨；不可把扶合或沖剋固定加減分。'),
('support-combine', [31], '生扶拱合包括五行與三合六合；休囚得助、旺遇幫扶等不直接等於事成。'),
('clash-control', [32], '剋害刑沖須辨用神、旺衰及救護，不單看關係字面。'),
('phase-relative', [32], '長生與帝旺分有氣/有力，墓絕空等仍須看扶救，不以階段名包辦。'),
('day-month', [32,33], '日辰能合住/沖實/沖散等，月建為提綱；不能混作同一時間尺度。'),
('year-body', [33], '太歲、卦身、世應各有上下文，卦身與卷三所辯世身不合併。'),
('question-roles', [34], '應位可代表所問他人，但具體親屬依父兄妻子等取用；沒有一律應代所有人的捷徑。'),
('both-void', [34], '世應俱空虛諾等屬特定謀事文本；不做所有問題的誠信或心理判斷。'),
('injury-rescue', [35], '有傷須救以用神受傷及救護之神為前提；沒有日月和動爻資訊就保留未知。'),
('void-cause', [35,36], '有故/無故之空分辨生扶、刑沖、月日及問事，不從一個旬空旗標推出無用。'),
('combine-break', [36], '欲合成事遇破與欲解散而遇合的意義相反，保留問事目的。'),
('self-void', [36,41], '自空化空與有用無用有後文限定；不能截句覆蓋旺動/出旬等條件。'),
('moving-bound', [36,37], '動爻被日辰合住則受絆，待沖之日有應期說；不直接生成公曆日期。'),
('static-dark', [37,38], '靜爻旺而得日沖可暗動；衰弱及救護條件不能省略。'),
('tomb-use', [37,40], '入墓受阻有沖墓等條件，能否剋他爻與旺衰不能只由墓名定。'),
('greed', [37,38], '貪生/貪合忘剋等須有具體生合對象，作者論例不作全圖永久刪邊。'),
('day-parity', [38], '日辰併爻不自動使衰弱爻成旺，還須動靜/生扶等完整條件。'),
('complete-triads', [38,39], '三刑三合見全及兩爻動另設結構前提；兩支不補想像第三支。'),
('partial-groups', [39], '子卯與自刑另列；本次三成員算法不擅用三支門檻覆蓋它們。'),
('hidden-rescue', [39], '伏神與飛神、用神是否已現、日月提拔須並看，承接既有顯現/飛伏研究。'),
('calendar-controls', [40,41], '日月制忌與忌來傷用分層，受制忌不等於所有忌永久失效。'),
('functional-void', [41], '有用無用空化空段分動靜、出旬與進退等，不提供無條件真空判定。'),
('return-control', [42], '回頭剋/生合及扶人須區分用/忌、自/他、問事，非所有生合都吉。'),
('movement', [42,43], '進退、交重、變爻與先後各分，不將進神固定等於吉。'),
('benefit-with-harm', [43], '生合可能兼刑害；兩種關係可同現，不能互相抹去。'),
('timing', [44], '合待沖、休囚待生旺、動靜緩速等要求時間尺度，原文反對拘執單一月日。'),
('question-kin', [45], '父/官/財/子/兄與問事相對，福德/忌神不能固定為同一六親。'),
('spirits-not-verdict', [46,47], '龍虎玄朱等須從五行用神生剋制化，不能只按六獸名斷吉凶。'),
('ritual-not-instruction', [47,48], '誠心/神明/代占等屬作者方法與信念，保存為史料，不作使用者必須遵行的命令。'),
('end-and-limits', [48], '卷四有明確終行；讀完相關篇幅不等於每個命題均已編碼或應驗已驗證。'),
]
write('OPERATIONAL_CLAUSES.json', {'date': '2026-10-27', 'sourceID': 'B03-book2',
    'textualVolume': 4, 'clauses': [{'id': i, 'pdfPages': p, 'boundedParaphrase': s,
        'consumerApplied': False, 'historicalOutcomesValidated': False} for i,p,s in clauses],
    'sourceInstructionsAreData': True, 'historicalMedicalClaimsNotClinicalAdvice': True,
    'allVolume4ClausesCompiled': False})
write('SOURCE_AUDIT.json', {'date': '2026-10-27', 'sourceID': 'B03-book2',
    'sourcePDF': '../liuyao-b03-volume3/' + a['file'], 'sourceSHA256': a['sha256'],
    'acquisitionRecord': '../liuyao-b03-volume3/ACQUISITION.json',
    'APIAndTLSRecord': '../liuyao-b03-volume3/REQUESTS.json',
    'metadataIsNotAdditionalImprintProof': True, 'newHTTPBodies': 0,
    'firstPassVolume4RelevantSpan': list(range(30,49)), 'unreadPhysicalBook2Pages': [],
    'notEstablished': ['All source clauses compiled', 'Whole six physical books / fourteen textual volumes',
        'Full strength and functional void model', 'Date adapter and timing outcomes',
        'Independent pedigree / all polemic quotations collated', 'B02 PDF52 date-void inconsistency resolved'],
    'sourceIsNotUserInstruction': True, 'wholeBookApplied': False})
print('Recorded 19 content pages, one cover, 17 new renders and three expanded readings; 30 bounded clauses.')
