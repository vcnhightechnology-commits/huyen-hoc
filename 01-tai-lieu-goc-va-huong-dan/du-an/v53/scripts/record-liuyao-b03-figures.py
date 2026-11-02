from pathlib import Path
from hashlib import sha256
import json
root=Path(__file__).resolve().parent.parent;base=root/'research/liuyao-b03-figures'
sha=lambda p:sha256(p.read_bytes()).hexdigest()
def write(n,d):(base/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
records=[]
for n in range(34,61):
 folder='liuyao-b03-boundaries'if n<39 else'liuyao-b03-figures';p=root/f'research/{folder}/images/bushi-{n}.png'
 records.append({'pdfPage':n,'image':f'../{folder}/images/{p.name}'if n<39 else f'images/{p.name}','sha256':sha(p),'newLocalRender':n>=39,
 'scope':'endleaf-only'if n==60 else'full-first-pass-figure-heading-and-context-span-not-full-diplomatic-line-transcription',
 'entirePageApplied':False})
write('MANUAL_READINGS.json',{'date':'2026-10-27','sourcePDF':'../liuyao-foundations/NLC892-GBZX0301013045-259368.pdf',
 'sourceSHA256':'5dcd7b5005b1e86f441a9350eefb7c0e9e628c47ab926b2a7d1bdd6691a4773d','records':records,
 'counts':{'manualImageRecords':27,'newLocalRenders':22,'expandedPriorRecords':5,'completeVolume2RelevantSpanPages':26,'newContentPages':21,'newEndleafPages':1},
 'boundaries':'卷二beginsinsidePDF34andendsinside59;60isbackcover/endleafwithlibrarymark,notdatedimprint. 64figureheadingsandpositionsread,notall384lineglyphsdiplomaticallycollated.',
 'qaCrops':[{'file':f'qa-crops/{n}.png','sha256':sha(base/f'qa-crops/{n}.png'),'scope':'expandedPDF59availabilityandchanged卯case'}for n in['bushi-59-availability','bushi-59-availability-context']],
 'additionalGlyphQA':{'file':'qa-crops/bushi-49-heading.png','sha256':sha(base/'qa-crops/bushi-49-heading.png'),'pdfPage':49,'renderDPI':360,'cropBoxPixels':[1300,300,2280,1100],
 'reading':'火雷筮嗑','normalization':'Figure21normalized噬嗑;literalheadingkeeps筮. Independenteditioncollationstillopen.','additionalQAPageRenders':1},
 'wholePhysicalBookRead':False,'prefacesAndIntroductoryPagesStillPartial':True,'allClausesApplied':False,'newHTTPResponses':0,'newOriginalPDFs':0})
# Manually located actual printed headings; pages are not inferred from eight-palace arithmetic.
palaces=[('乾','金',[(1,'乾',34),(44,'姤',34),(33,'遯',35),(12,'否',35),(20,'觀',36),(23,'剝',36),(35,'晉',37),(14,'大有',37)]),
 ('坎','水',[(29,'坎',37),(60,'節',38),(3,'屯',38),(63,'既濟',38),(49,'革',39),(55,'豐',39),(36,'明夷',39),(7,'師',40)]),
 ('艮','土',[(52,'艮',40),(22,'賁',40),(26,'大畜',41),(41,'損',41),(38,'睽',42),(10,'履',42),(61,'中孚',42),(53,'漸',43)]),
 ('震','木',[(51,'震',43),(16,'豫',44),(40,'解',44),(32,'恒',44),(46,'升',45),(48,'井',45),(28,'大過',46),(17,'隨',47)]),
 ('巽','木',[(57,'巽',47),(9,'小畜',47),(37,'家人',48),(42,'益',48),(25,'无妄',48),(21,'噬嗑',49),(27,'頤',49),(18,'蠱',49)]),
 ('離','火',[(30,'離',50),(56,'旅',50),(50,'鼎',51),(64,'未濟',51),(4,'蒙',52),(59,'渙',52),(6,'訟',52),(13,'同人',53)]),
 ('坤','土',[(2,'坤',53),(24,'復',53),(19,'臨',54),(11,'泰',54),(34,'大壯',54),(43,'夬',55),(5,'需',55),(8,'比',56)]),
 ('兌','金',[(58,'兌',56),(47,'困',56),(45,'萃',57),(31,'咸',57),(39,'蹇',57),(15,'謙',58),(62,'小過',58),(54,'歸妹',59)])]
figures=[{'palace':palace,'palaceElement':element,'stageIndex':i,'stageOrdinal1':i+1,'number':number,'normalizedHeading':name,'headingPDFPage':page,
 'annotationScope':'Literalheading/palacesequencechecked;linekin/hiddenfieldsselectedfixturesonly;卦身keptseparate.'}for palace,element,items in palaces for i,(number,name,page)in enumerate(items)]
assert len(figures)==64 and len({r['number']for r in figures})==64
write('FIGURE_LOCATOR.json',{'date':'2026-10-27','sourceID':'B03','figureCount':64,'figures':figures,
 'literalHeadingVariantNotes':[{'number':25,'reading':'天雷无妄','normalization':'Retain无inthislocator,notan assertionalltitlesuse無.'},{'number':21,'reading':'火雷筮嗑','normalization':'360DPIglyphQAreadstitle筮嗑;normalized噬嗑andfigure21identityseparate. Independenteditioncomparisonopen.'}],
 'limits':'64headings/figuresidentified,notindependentcomplete384lineannotationsorallparagraphrules. Physicalbookfirstonly,wholework14volumesnotapplied.'})
cases=[
 ('ge-wealth',39,49,'妻財',3,'午','亥','flying-controls-hidden'),
 ('lu-wealth',42,10,'妻財',5,'子','申','flying-generates-hidden'),
 ('jian-wealth',43,53,'妻財',5,'子','巳','hidden-controls-flying'),
 ('sheng-child',45,46,'子孫',4,'午','丑','hidden-generates-flying'),
 ('jiaren-officer',48,37,'官鬼',3,'酉','亥','hidden-generates-flying'),
 ('yi-child',49,27,'子孫',5,'巳','子','flying-controls-hidden'),
 ('ding-parent',51,50,'父母',1,'卯','丑','hidden-controls-flying'),
 ('meng-wealth',52,4,'妻財',4,'酉','戌','flying-generates-hidden'),
 ('song-officer',53,6,'官鬼',3,'亥','午','hidden-controls-flying'),
 ('fu-parent',54,24,'父母',2,'巳','寅','flying-generates-hidden'),
 ('xian-wealth',57,31,'妻財',2,'卯','午','hidden-generates-flying'),
 ('xiaoguo-child',58,62,'子孫',4,'亥','午','hidden-controls-flying'),
 ('guimei-child',59,54,'子孫',4,'亥','午','hidden-controls-flying')]
write('SOURCE_FIXTURES.json',{'date':'2026-10-27','hiddenCases':[{'id':id,'pdfPage':page,'number':num,'desiredKin':kin,'line':line,'branch':branch,'flyingBranch':cover,'relation':rel}for id,page,num,kin,line,branch,cover,rel in cases],
 'changedAvailabilityCase':{'id':'dun-to-tongren-prefers-shown-wealth','pdfPage':59,'values':[6,8,7,7,7,7],'number':33,'changedNumber':13,'desiredKin':'妻財',
 'originalLine1':{'branch':'辰','kin':'父母'},'changedLine1':{'branch':'卯','kin':'妻財'},'purePalaceHiddenWealth':{'line':2,'branch':'寅'},
 'meaning':'Sourceexplicitlyuseschanged卯wealthratherthanhidden寅inthiscase. Notpermissiontoinferallprioritybetweenmultipleprimary/changedlines.'},
 'noHistoricalOutcomeValidation':True})
write('AVAILABILITY_RULES.json',{'date':'2026-10-27','sourcePDFPage':59,'literalBoundedAnchors':['如六爻安靜及動變之爻又無用神者當推此例','不必再查伏神矣','當以卯木妻財為用神不必看寅木矣'],
 'scope':'Questiondesiredkinexplicitlychosen. Figurelayeravailabilitygateonly;notautomaticquestion/usegod/strength/hiddenusefulnessselection.',
 'rule':'When any primary or actually changed line shows the desired kin,mark source instruction not to initiate default pure-palacehidden search. If none are shown,the purepalace table is a search candidate. Do not invent precedence between multiple primary and changed candidates.',
 'calendarAvailabilityNotAdjudicated':True,'overallUsefulnessNotAdjudicated':True,'B02AgreementNotAssumed':True,
 '卦身Caveat':'Paragraphalsomentions卦身;newAPIonlyimplementscommonexplicitprimary/changedclauses andprinted33→13example,notB03卦身method.',
 'consumerApplied':False})
write('WORK_STATE.json',{'date':'2026-10-27','status':'active-B03figure-locator-and-shown-candidate-gate','sourceID':'B03','newContentPages':21,
 'newEndleafPages':1,'newLocalRenders':22,'expandedPriorRecords':5,'figureHeadings':64,'lineAnnotationCollationComplete':False,
 'wholePhysicalBookRead':False,'wholeBookApplied':False,'wholeCatalogueCompleted':False,'consumerChanged':False})
print('27image records/22newrenders/5expanded;64headinglocators/13hiddenfixtures/onechanged-usecase;noentirebookclaim.')
