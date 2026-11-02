from pathlib import Path
from hashlib import sha256
from PIL import Image, ImageChops
import json

w = Path.cwd()
b = w / 'tmp/bazi-food-appendices-staging'
read = lambda p: json.loads(p.read_text(encoding='utf-8-sig'))
write = lambda name, x: (b/name).write_text(json.dumps(x, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
ctx_path = w/'v53/research/bazi-food-source/CONTEXTS.json'
ctx = read(ctx_path)
units = {'FOOD-03', 'FOOD-04', 'FOOD-05', 'FOOD-06', 'FOOD-08', 'FOOD-09'}
rows = [x for x in ctx['records'] if x['unit'] in units]
assert len(rows) == 17
write('SELECTED_CONTEXTS.json', dict(date='2026-10-28', source=ctx_path.relative_to(w).as_posix(),
    sha256=sha256(ctx_path.read_bytes()).hexdigest(), records=rows,
    exactSourceContextsNotAtomicRuleCount=True, allCharactersImageCollated=False))

records=[]
def add(id, system, parent, anchor, targets, kind='pillar', positions=[0,1,2,3], frame='source-declared', **extra):
    records.append(dict(id=id,system=system,parentContext=parent,anchor=anchor,targets=targets,
        targetKind=kind,targetPositions=positions,requiredAnchorFrame=frame,
        canonicalReadingsAreEditorial=True,fullClauseApplied=False,consumerApplied=False,**extra))
add('kitchen-jia','tianchu','FOOD-03-C02','甲',['丙','巳'],'stem-and-branch',[0,1,3],
    presenceIsNecessaryOnly=True,stemBranchColocationResolved=False)
add('fortune-jia','fuxing','FOOD-04-C02','甲',['丙寅','丙子'],positions=[1,2,3],frame='year',
    targetJoinUnresolved=True,originalXunDerivationEstablished=False)
add('fortune-yi','fuxing','FOOD-04-C02','乙',['丁亥','丁丑'],positions=[1,2,3],frame='year',
    targetJoinUnresolved=True,originalXunDerivationEstablished=False)
add('nest-jiazi','tongke','FOOD-05-C02','甲子',['丙子'])
add('owl-nest-jiazi','tongke-owl','FOOD-05-C04','甲子',['壬子'],positions=[3],frame='year')
add('owl-nest-gengzi','tongke-owl','FOOD-05-C04','庚子',['戊子'],positions=[3],frame='year')
for a,food,partner in [('甲','丙','辛'),('己','辛','丙'),('乙','丁','壬'),('庚','壬','丁'),('丙','戊','癸'),('辛','癸','戊')]:
    add('bound-'+a,'daihe','FOOD-06-C02',a,[food,partner],'stems',
        effectiveCombinationEstablished=False)
for a,target in [('丙','戊戌'),('辛','癸丑'),('壬','甲辰'),('乙','丁未')]:
    add('red-seal-'+a,'hongluan-tianyin','FOOD-08-C02',a,[target],positions=[2,3],
        notTuviHongLoan=True)
add('ink-xinsi','mochi','FOOD-09-C02','辛巳',['癸巳','癸亥'],targetJoinUnresolved=True)
for a,target in [('丙寅','戊寅'),('戊申','庚申'),('己巳','辛亥'),('庚午','壬申'),('甲戌','丙寅'),('壬辰','甲申')]:
    add('ink-'+a,'mochi','FOOD-09-C03',a,[target])
assert len(records)==23
write('EXPLICIT_COORDINATES.json',dict(date='2026-10-28',systemPrefix='TMTH005-appendix-',
    records=records,sourceRuleUnits=6,namedCoordinateSystems=7,
    tablesAreNotCompleteTraditionalCatalogues=True,sourceRoleInferenceNotAutomatic=True,
    sourceOutcomeValidated=False))

dispositions={
 'FOOD-03-C01':('heading','Title 天衝食祿, not a separate executable rule.'),
 'FOOD-03-C02':('partial-coordinate','甲→丙 and 巳 must both appear; 年月時 scope and 戊日 contrast retained. No automatic extrapolation to ten stems, no ruling on colocation.'),
 'FOOD-03-C03':('unresolved-conditions-and-historical-outcome','月令純粹/四柱順食/財庫 require a named complete method. Historical wealth and parental inheritance are not validated predictions.'),
 'FOOD-04-C01':('heading','福星貴人 title, not the current universal star table.'),
 'FOOD-04-C02':('partial-coordinate','Four listed target tokens, two anchor stems. 本旬 derivation, remaining 餘例推 and target join are not supplied by assumption.'),
 'FOOD-04-C03':('explicit-anchor-constraint','Source says 以年論 and 若以日遁則非. Year anchor required for coordinate audit; no day-stem substitution.'),
 'FOOD-05-C01':('heading','食神同窠 title.'),
 'FOOD-05-C02':('literal-plus-declared-mathematical-derivation','Literal 甲子→丙子 retained. 十三位 is modeled as an explicitly editorial inclusive +12 cycle step; sixty derived rows are separate from the one printed example.'),
 'FOOD-05-C03':('historical-ranking-and-conditions','月不如日/日不如時 recorded as source ordering only. 互換生旺帶祿貴 not automatically derived. Three historical charts are not calendar or outcome evidence in this scope.'),
 'FOOD-05-C04':('partial-coordinate-historical-outcome-excluded','Two explicit year→hour inverse-food examples; Thiên Ấn stays Thiên Ấn. Harm-to-children rhetoric excluded from interpretation.'),
 'FOOD-06-C01':('heading','食神帶合 title.'),
 'FOOD-06-C02':('partial-coordinate','Six printed anchor/food/partner triples only. Existence of a 合 partner does not establish effective combination, transformation, office or authority.'),
 'FOOD-08-C01':('heading','紅鸞天印 is a named Bazi source passage, not Tuvi Hong Loan.'),
 'FOOD-08-C02':('partial-coordinate','Four complete target pillars, day/hour target scope. Anchor role is not explicitly equated with day master. No remainder-table invention or fortune prediction.'),
 'FOOD-09-C01':('heading','墨池涌泉 title.'),
 'FOOD-09-C02':('partial-coordinate-and-historical-example','辛巳 lists 癸巳/癸亥; keep individual presence, do not silently choose OR versus AND. 陳朝議 chart is a literal example only here.'),
 'FOOD-09-C03':('partial-coordinate','Six further anchor/target pairs exactly retained. 己巳→辛亥 and 庚午→壬申 prevent automatic same-branch unification; 文貴 remains a source claim.'),
}
assert set(dispositions)=={x['id'] for x in rows}
write('CLAUSE_DISPOSITIONS.json',dict(date='2026-10-28',records=[dict(parentContext=x['id'],
    digitalCodepoints=len(x['text']),disposition=dispositions[x['id']][0],note=dispositions[x['id']][1],
    wholeClauseApplied=False,practicalOutcomeValidated=False) for x in rows],
    headings=6,nonHeadingContexts=11,wholeSourceUnitsApplied=0))

qa=read(b/'QA_IMAGES.json')
for x in qa['records']:
    x['actuallyViewed']=True
    assert ImageChops.difference(Image.open(w/x['sourceFile']).convert('RGB').crop(x['cropBox']),
        Image.open(b/x['file']).convert('RGB')).getbbox() is None
qa['viewScope']='Five native crops and five full-page expanded views actually inspected; not a whole-character diplomatic collation.'
write('QA_IMAGES.json',qa)
print(json.dumps(dict(contexts=len(rows),coordinateRecords=len(records),crops=len(qa['records']),newSourcePositions=0)))
