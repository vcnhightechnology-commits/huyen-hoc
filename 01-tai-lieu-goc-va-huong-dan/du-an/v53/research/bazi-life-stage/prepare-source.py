from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone, timedelta
from PIL import Image, ImageChops
import json

s = Path(__file__).resolve().parent
w = s.parent.parent
read = lambda p: json.loads(p.read_text(encoding='utf-8-sig'))
write = lambda name, d: (s / name).write_text(json.dumps(d, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
digest = lambda p: sha256(p.read_bytes()).hexdigest()
assert not (s / 'life-stage-reference.mjs').exists()
assert not (s / 'PREIMPLEMENTATION_FREEZE.json').exists()
images = []
for page, box, name in [(112, (300, 280, 560, 2860), 'main-list-start'),
                        (113, (300, 270, 2070, 2845), 'main-tail-and-quoted-first-five'),
                        (114, (300, 270, 2090, 2820), 'quoted-six-to-twelve-and-qualifier'),
                        (115, (1690, 270, 2070, 2800), 'broad-groups-and-qualifier')]:
    p = w / f'v53/research/bazi-season-strength/p{page}.png'
    crop = s / (name + '.png')
    a = Image.open(p).convert('RGB')
    b = Image.open(crop).convert('RGB')
    assert ImageChops.difference(a.crop(box), b).getbbox() is None
    images.append({'source': p.relative_to(w).as_posix(), 'sourceBytes': p.stat().st_size,
                   'sourceSHA256': digest(p), 'sourceDimensions': list(a.size), 'boxXYXY': list(box),
                   'crop': crop.name, 'cropBytes': crop.stat().st_size, 'cropSHA256': digest(crop),
                   'nativeCropActuallyViewed': True, 'RGBPixelMatched': True, 'resampled': False})
write('NATIVE_CROPS.json', {'date': '2026-10-29', 'records': images, 'newSourcePositions': 0})
main = ['長生', '沐浴', '冠帶', '臨官', '帝旺', '衰', '病', '死', '墓', '絶', '胎', '養']
definitions = [
    ('受氣', ['絶', '胞'], '萬物在地中未有其象', [113], '002-56a'),
    ('受胎', [], '天地氣交氤氲造物其物在地中萌芽始有其氣', [113], '002-56a'),
    ('成形', [], '萬物在地中成形', [113], '002-56a'),
    ('長生', [], '萬物發生向榮', [113], '002-56a'),
    ('沐浴', ['敗'], '萬物始生形體柔脆易為所損', [113, 114], '002-56a/56b'),
    ('冠帶', [], '萬物漸榮秀', [114], '002-56b'),
    ('臨官', [], '萬物既秀實', [114], '002-56b'),
    ('帝旺', [], '萬物成熟', [114], '002-56b'),
    ('衰', [], '萬物形衰', [114], '002-56b'),
    ('病', [], '萬物病', [114], '002-56b'),
    ('死', [], '萬物死', [114], '002-56b'),
    ('墓', ['庫'], '萬物成功而藏之庫', [114], '002-56b'),
]
records = [{'sourceOrdinal': i, 'literalName': name, 'explicitSourceAliases': aliases,
            'sourceDefinition': text, 'containerPages': pages, 'printedFolio': folio,
            'definitionUsesHistoricalMetaphor': True}
           for i, (name, aliases, text, pages, folio) in enumerate(definitions, 1)]
manual = {'schema': 'hhc.bazi.life-stage.source-terms.v1', 'date': '2026-10-29',
          'entryMethod': 'Manually read retained native images112–115; exact terms and explicit aliases before implementation/runtime.',
          'mainSystem': 'TMTH002-main-twelve-enumeration', 'quotedSystem': 'TMTH002-reported-sanming-tiyao',
          'mainOrder': main, 'mainListImages': [112, 113], 'quotedRows': records,
          'quotedVoice': '三命提要云 as reported inside Tam Menh; separate historical book not independently acquired.',
          'explicitAliasAnchors': {'受氣': '一曰受氣又曰絶曰胞', '沐浴': '五曰沐浴又曰敗', '墓': '十二曰墓又曰庫'},
          'editorialAlignmentCandidatesNotAcceptedAliases': [
              {'quotedTerm': '受胎', 'mainTerm': '胎', 'basis': 'semantic/ordinal alignment inference, not 又曰 in this clause'},
              {'quotedTerm': '成形', 'mainTerm': '養', 'basis': 'cyclic position inference, not explicit printed alias'}],
          'reportedBroadGroups': {'四貴': ['胎', '生', '旺', '庫'], '四忌': ['死', '絶', '病', '敗']},
          'broadGroupQualifier': '亦大槩言之',
          'noAutomaticOutcomeAnchors': ['見生旺者未必便作吉論', '見休囚死絶未必便作凶言'],
          'sourceCoordinatesNotEstablished': ['ten-stem start branches', 'yin/yang direction', 'date-to-branch adapter', 'source 生 and 旺 shorthand binding'],
          'allChapterCharactersCollated': False, 'fullNatalStrengthEstablished': False,
          'newHTTPBodies': 0, 'newSourcePositions': 0, 'consumerApplied': False}
write('MANUAL_TERMS.json', manual)
fixture = {'writtenBeforeImplementationAndRuntime': True, 'date': '2026-10-29',
           'mainOrder': main,
           'quotedOrder': ['受氣', '受胎', '成形', '長生', '沐浴', '冠帶', '臨官', '帝旺', '衰', '病', '死', '墓'],
           'explicitAliasQueries': [{'term': '絶', 'canonicalSourceName': '受氣', 'sourceOrdinal': 1},
                                    {'term': '胞', 'canonicalSourceName': '受氣', 'sourceOrdinal': 1},
                                    {'term': '敗', 'canonicalSourceName': '沐浴', 'sourceOrdinal': 5},
                                    {'term': '庫', 'canonicalSourceName': '墓', 'sourceOrdinal': 12}],
           'notImplicitQuotedAliases': ['胎', '養', '生', '旺', '长生', '绝', '冠带', '临官'],
           'allMainNameQuotedOrdinal': [4, 5, 6, 7, 8, 9, 10, 11, 12, 1, None, None],
           'expectedLunarSimplifiedSequence': ['长生', '沐浴', '冠带', '临官', '帝旺', '衰', '病', '死', '墓', '绝', '胎', '养'],
           'explicitComparisonNormalizationOnly': {'长生': '長生', '冠带': '冠帶', '临官': '臨官', '绝': '絶', '养': '養'},
           'calendarOrNatalChartsExpected': 0,
           'sourceTermsNotDiagnosesOrForecasts': True}
write('EXPECTED_BEFORE_IMPLEMENTATION.json', fixture)
identities = []
for rel in ['v53/research/bazi-season-strength/CADAL06066038.djvu',
            'v53/research/bazi-season-strength/RETAINED_DIGITAL_STRENGTH_SECTION.txt',
            'v53/research/bazi-season-strength/season-label-reference.mjs',
            'v46/node_modules/lunar-typescript/dist/index.cjs', 'v46/node_modules/lunar-typescript/package.json',
            'v53/engine.js', 'v53/Huyen_Hoc_Cac.html', 'Huyen_Hoc_Cac_V53_web.zip']:
    p = w / rel
    identities.append({'file': rel, 'bytes': p.stat().st_size, 'sha256': digest(p)})
write('SOURCE_IDENTITIES.json', {'date': '2026-10-29', 'files': identities,
                                'previousByteProvenance': 'v53/research/bazi-season-strength/ACQUISITION.json'})
files = []
for name in ['MANUAL_TERMS.json', 'EXPECTED_BEFORE_IMPLEMENTATION.json', 'NATIVE_CROPS.json']:
    p = s / name
    files.append({'file': name, 'bytes': p.stat().st_size, 'sha256': digest(p)})
write('PREIMPLEMENTATION_FREEZE.json', {'date': '2026-10-29',
    'frozenAt': datetime.now(timezone(timedelta(hours=7))).isoformat(timespec='seconds'),
    'implementationExists': False, 'runtimeExists': False, 'files': files})
write('WORK_STATE.json', {'date': '2026-10-29', 'status': 'source-read-and-fixtures-frozen;before-implementation',
    'catalogueID': 'M01', 'scope': 'Twelve-term source lexicon and distinct quoted enumeration; not natal-strength classifier',
    'retainedSourceImagesReexamined': [112, 113, 114, 115], 'acceptedNativeCrops': 4,
    'newHTTPBodies': 0, 'newSourcePositions': 0, 'newEngineCalls': 0,
    'relatedUnresolvedScope': 'tmp/bazi-food-position-staging/WORK_STATE.json',
    'activeFoodMatrixUnchanged': '44/46/0', 'consumerChanged': False, 'wholeCatalogueCompleted': False})
print(json.dumps({'manualLists': 2, 'explicitQuotedDefinitions': 12, 'explicitAliasTokens': 4,
                  'nativeCropsRGBMatched': 4, 'preimplementationFrozenFiles': len(files)}))
