from pathlib import Path
from hashlib import sha256
import json, shutil
from PIL import Image

r = Path(__file__).resolve().parent.parent
w = r.parent
b = r / 'research/home-rings'
q = r / 'qa/home-rings'
s = w / 'tmp/home-rings-staging'
read = lambda p: json.loads(p.read_text(encoding='utf-8-sig'))
sha = lambda p: sha256(p.read_bytes()).hexdigest()
assert len(read(w / 'archives/v53-before-home-rings/PACKAGE_MANIFEST.json')['files']) == 3139
b.mkdir(exist_ok=False)
q.mkdir(exist_ok=False)

def write(name, data):
    (b / name).write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

# Each sequence was read from its own native diagram, in four lossless
# orientations. The engine is not used to reconstruct unread source labels.
diagrams = [
    {'page': 11, 'ring': 'middle', 'outerRole': '正針', 'innerRole': '中針',
     'outerFromZi': list('子癸丑艮寅甲卯乙辰巽巳丙午丁未坤申庚酉辛戌乾亥壬'),
     'innerFromZi': list('子癸丑艮寅甲卯乙辰巽巳丙午丁未坤申庚酉辛戌乾亥壬'),
     'innerPairArcs': ['壬子','癸丑','艮寅','甲卯','乙辰','巽巳','丙午','丁未','坤申','庚酉','辛戌','乾亥'],
     'sourceOffsetHalfPositions': -1, 'ziBetweenRegularLabels': ['壬','子'], 'sourceUse': '格龍',
     'directVisualQA': True},
    {'page': 13, 'ring': 'seam', 'outerRole': '正針', 'innerRole': '縫針',
     'outerFromZi': list('子癸丑艮寅甲卯乙辰巽巳丙午丁未坤申庚酉辛戌乾亥壬'),
     'innerFromZi': list('子癸丑艮寅甲卯乙辰巽巳丙午丁未坤申庚酉辛戌乾亥壬'),
     'innerPairArcs': ['壬子','癸丑','艮寅','甲卯','乙辰','巽巳','丙午','丁未','坤申','庚酉','辛戌','乾亥'],
     'sourceOffsetHalfPositions': 1, 'ziBetweenRegularLabels': ['子','癸'], 'sourceUse': '消砂納水',
     'directVisualQA': True}
]
write('DIAGRAM_LABELS.json', {
    'date': '2026-10-27', 'status': '96-directly-read-ring-labels-and24-pair-arcs',
    'sourceContainer': 'v53/research/full-study/home/CADAL06056503.djvu',
    'sourceSHA256': 'bfd3b76c55d62324919ab161c8c2ba2ecb129b3b2c59a3ab0428807e8f8278db',
    'order': 'Begin at printed 子 on each ring; follow 子→癸→丑, not screenshot top.',
    'diagrams': diagrams, 'directLabels': 96, 'directPairArcs': 24,
    'intersectingInteriorTriadPathsFullyTraced': False,
    'triadMembershipEvidence': 'Prose14–15 independently states all four six-mountain groups.'
})

passages = [
    {'id':'R12-01','page':12,'text':'圖外層所列為正針乃二十四山之正位內層所列為中針',
     'disposition':'Outer/inner role explicitly named; preserve each ring coordinate.'},
    {'id':'R12-02','page':12,'text':'其子位在正針壬子二位之間比正針先半位',
     'disposition':'Middle Zi precedes regular Zi by half a position; degrees are separately derived.'},
    {'id':'R12-03','page':12,'text':'其雙取者為雙山其取三合者為雙山五行',
     'disposition':'Pair then combine triads; not a universal regular five-element lookup.'},
    {'id':'R12-04','page':12,'text':'地理家格龍用之蓋龍為來脈故用先至者承之乃無失也',
     'disposition':'Source application/reasoning recorded as source claim, not observed outcome.'},
    {'id':'R14-01','page':14,'text':'圖外層所列為正針內層所列為縫針',
     'disposition':'Seam is inner, regular is outer.'},
    {'id':'R14-02','page':14,'text':'其子位在正針子癸二位之間比正針後半位',
     'disposition':'Seam Zi follows regular Zi by half a position.'},
    {'id':'R14-03','page':14,'text':'其雙取三合者為三合五行與雙山同特比中針正差一位耳',
     'disposition':'Same named pair/element system but middle/seam positions differ by one regular position.'},
    {'id':'R14-04','page':14,'text':'地理家用以消砂納水蓋砂水為去路故用後至者收之乃無遺也',
     'disposition':'Separate source use for sand/water; no room, true/magnetic north, or practical outcome inferred.'},
    {'id':'R14-05','page':14,'text':'按雙山五行即三合五行也地支十二取生旺墓三者為三合局而四卦八干各在支前一位今以支前一位之卦干與支雙並而同取地支三合之五行故曰雙山五行',
     'disposition':'Twelve branch life/prosperity/tomb positions pair with preceding four trigrams/eight stems.'},
    {'id':'R14-06','page':14,'text':'坤申壬子乙辰合水局六山皆屬水乾亥甲卯丁',
     'continuesOnPage':15,'disposition':'Water group complete; wood group continues across leaf.'},
    {'id':'R15-01','page':15,'text':'未合木局六山皆屬木艮寅丙午辛戌合火局六山皆屬火巽巳庚酉癸丑合金局六山皆屬金',
     'continuesFromPage':14,'disposition':'Wood/fire/metal six-mountain groups explicit.'},
    {'id':'R15-02','page':15,'text':'地理書曰正五行乃五行之質雙山五行乃五行之氣故推龍氣之生旺用雙山而不用正五行也',
     'disposition':'Quoted traditional distinction 質/氣 retained; not an empirical mechanism.'},
    {'id':'R15-03','page':15,'text':'又地理家有三針一曰正針乃二十四山之正位定向用之一曰中針其子位在正針壬子二位之中格龍用之一曰縫針其子位在正針子癸二位之縫消砂納水用之',
     'disposition':'All three uses and Zi anchors explicitly enumerated.'},
    {'id':'R15-04','page':15,'text':'故中針與縫針差一位雙山五行在中針則曰雙山五行在縫針則曰三合五行其實皆',
     'continuesOnPage':16,'disposition':'Names depend on ring; common paired method does not equate physical positions.'},
    {'id':'R16-01','page':16,'text':'雙山法也','continuesFromPage':15,
     'disposition':'Final four characters read; rest of page is ruled blank.'}
]
write('SOURCE_CLAUSES.json', {'status':'all-printed-prose-of-headings-XJ2-03-and04-enumerated',
    'sourceInstructionsAreData': True, 'passages':passages, 'passageCount':15,
    'punctuation':'Editorial segmentation; continuous image text preserved without invented punctuation.',
    'quotedHistoricalClaimsEmpiricallyValidated':False})

groups = [
    {'element':'水','sourceMountains':'坤申壬子乙辰','branchesInSourceLifeProsperityTombOrder':'申子辰','pairs':['坤申','壬子','乙辰'],'pages':[14]},
    {'element':'木','sourceMountains':'乾亥甲卯丁未','branchesInSourceLifeProsperityTombOrder':'亥卯未','pairs':['乾亥','甲卯','丁未'],'pages':[14,15]},
    {'element':'火','sourceMountains':'艮寅丙午辛戌','branchesInSourceLifeProsperityTombOrder':'寅午戌','pairs':['艮寅','丙午','辛戌'],'pages':[15]},
    {'element':'金','sourceMountains':'巽巳庚酉癸丑','branchesInSourceLifeProsperityTombOrder':'巳酉丑','pairs':['巽巳','庚酉','癸丑'],'pages':[15]}
]
write('PAIRED_ELEMENT_ROWS.json', {'system':'xieji-double-mountain','coordinateRequirement':'The mountain label belongs to the explicitly selected ring.',
    'rows':groups,'ringAssignments':48,'distinctNamedMountains':24,'earthGroupInThisTable':False,
    'doNotSubstitute':'正五行/洪範/月生氣/八宅生氣 are separate systems.', 'practicalOutcome':None})
write('ANGULAR_MODEL.json', {'system':'xieji-three-needles','model':'equal24-zi-zero-clockwise',
    'sourceHalfPositionOffsets':{'regular':0,'middle':-1,'seam':1},
    'derivedStepDegrees':15,'derivedHalfStepDegrees':7.5,
    'derivation':'360°/24 equal model positions; middle precedes and seam follows regular by half a position. Degrees are a software geometry convention, not numerals quoted from pages12–15.',
    'endpointPolicy':'both-at-touch','endpointPolicyTier':'Software convention: source does not prescribe half-open endpoints.',
    'regularCoordinateOrigin':'Zi=0°, increasing 子→癸→丑 in an explicitly chosen ideal model.',
    'physicalNorthCalibration':None,'magneticDeclinationAdapter':None,
    'sourceUse':{'regular':'定向','middle':'格龍','seam':'消砂納水'},
    'modernFieldMeasurementValidated':False,'practicalOutcome':None})

derivatives=[]
for rec in read(s/'CROP_BOXES.json'):
    page=rec['page']; filename=f'p{page:03}-native-ring.png'
    shutil.copy2(s/filename,b/filename)
    derivatives.append({'file':filename,'sourceFile':f'v53/research/home-you-nian/images/p{page:03}.png','cropBox':rec['box'],'operation':'native-crop','sha256':sha(b/filename)})
    for rotation in [90,180,270]:
        filename=f'p{page:03}-native-ring-rot{rotation}.png'
        shutil.copy2(s/filename,b/filename)
        derivatives.append({'file':filename,'sourceCrop':f'p{page:03}-native-ring.png','operation':f'transposeROTATE_{rotation}','sha256':sha(b/filename)})
write('MANUAL_READINGS.json', {'date':'2026-10-27','sourceContainer':'v53/research/full-study/home/CADAL06056503.djvu',
    'sourceSHA256':'bfd3b76c55d62324919ab161c8c2ba2ecb129b3b2c59a3ab0428807e8f8278db',
    'readings':[{'page':n,'file':f'v53/research/home-you-nian/images/p{n:03}.png','sha256':sha(r/f'research/home-you-nian/images/p{n:03}.png'),'directVisualQA':True}for n in [11,12,13,14,15,16]],
    'qaDerivatives':derivatives,'expandedPreviouslyReadPages':6,'newSourcePages':0,'newHTTPRequests':0,'newOriginalContainers':0,
    'manualDiagramLabels':96,'manualPairArcs':24,'sourceProseSegments':15,'allSourceClausesApplied':False,'wholeCatalogueCompleted':False,
    'limits':'Two source headings enumerated; interior crossing paths not all traced. Degree/north/date/outcome adapters not supplied by these six pages.'})
print('Recorded two named rings,96 source labels,24 pair arcs,15 source prose segments and explicit derived geometry model.')
