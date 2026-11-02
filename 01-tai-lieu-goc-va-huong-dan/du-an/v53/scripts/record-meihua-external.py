from pathlib import Path
from hashlib import sha256
import json

root=Path(__file__).resolve().parent.parent
base=root/'research/meihua-external';base.mkdir(exist_ok=True)
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
def write(name,data):
 (base/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
sha=lambda p:sha256(p.read_bytes()).hexdigest()
notes={
103:'卷三title and八卦方位之圖. Later-heaven arrangement has south at top/north below. Library barcode is not printing-date evidence.',
104:'觀梅數訣序 and八卦定陰陽次序. Eight numbers乾1兌2離3震4巽5坎6艮7坤8 and father/mother/three sons/three daughters; attributed authorship is not independently proven.',
105:'變卦式八則 begins:革→咸 and復→臨 diagrams. 動為用/靜為體; these previously examined arithmetic examples are not counted as new engine validation.',
106:'履→乾/革→噬嗑/歸妹→睽 and夬diagram. Printed inconsistent change labels remain open; do not rewrite a one-moving-line engine to match a multi-line difference.',
107:'Diagrams conclude with夬/plum革→咸 and訟-related upper-trigram text. Near-body/far-object anatomy/animal correspondences remain historical; a trigram label need not name the entire changed hexagram.',
108:'占卦訣 and體用互變之訣. Immediate/intermediate/later layer language and numerical delay claims do not establish a unique calendar date. Mutual sides follow the main body position.',
109:'Mutual-side conclusion,printed觀梅恒卦 unresolved context;體用生剋之訣 distinguishes actual large fire from colour/form symbols. Symbolic relations alone are not literal material effects.',
110:'Small lamp/candle versus large fire; non-cutting metal versus blade/axe/saw; true water versus black/wet/blood symbols; soil versus pottery; firewood versus uncut trees; true water versus pig/blood wood-support symbols. 體用衰旺之訣 begins. Relative source judgements are not measured probabilities or physical laws.',
111:'Strength conclusion retains illness/litigation claims as historical. 體用動靜之訣:body/mutual static,use/changed moving internally; direction/weather/terrain static externally,carried water/earth/stone and animals moving. Static evidence is not automatically manifested.',
112:'Motion concludes:seated observer slow,walking fast,standing half-slow/half-fast qualitatively. 占卜坐端之訣 uses observer-centred directions,not a complete house architecture/flying-star method.',
113:'坐端 concludes with bodily/health/pregnancy claims;占卜剋應之訣 opens. Timing units depend on subject and contextual scale,not hexagram numbers alone.',
114:'Timing material-durability analogies:years/months/days can be reinterpreted by context. No unique conversion,building expiry or human lifespan estimate is justified.',
115:'Timing concludes;萬物賦 begins. Ear/eye/heart and concrete observations are premises; health/ghost narratives are source assertions only.',
116:'萬物賦 continues with colours/shapes/animal sounds and conditional number/day analogies. No independent event-time or predictive validation.',
117:'萬物賦 concludes;飲食篇 begins with乾/坤 symbolic foods/social/seasonal readings. Not nutrition advice or food-safety determination.',
118:'飲食篇 continues坤巽艮坎. Food/material/hot-cold associations remain historical; no validated edibility or treatment function. Some glyphs are not fully collated.',
119:'飲食篇坎震離兌 and a local role scheme:lower=self,upper=other,mutual upper=wine,mutual lower=food,changed=guest. Do not silently replace the general moving-use/static-body policy.',
120:'飲食篇 concludes;觀物玄妙歌訣 begins乾坤震. Material/shape/colour categories are conditional alternatives,not unique automatic object recognition.',
121:'巽/坎 and a printed離heading with earth/mountain attributes,then兌with西澤. Keep heading/content conflict and digital凱撒variant uncorrected pending another witness.',
122:'觀物玄妙歌訣 concludes;諸事響應歌 begins. Compressed verses cover weather,persons,house,birth,marriage and dining; genre compression does not override full prose conditions.',
123:'諸事響應歌 continues/concludes. Diningverse剋用必無 is stronger than volume2prose飲食有阻; both retained. Health/drug/ghost/grave/financial statements remain historical,not consumer determinations.',
124:'諸卦反對性情 then占物類例. Antithetical hexagram phrases and line-text object analogies require context; not an object lookup guaranteed by a single label.',
125:'占物類例 and又訣:body/use relations and mutual/change used for object hypotheses. Claims of可食/quantity are not safe edibility tests; no automatic classification implemented.',
126:'物數為體訣 can treat repeated-element trigrams as body in object guessing;觀物看變爻為主 and觀物剋應法 emphasize changed line and source-based form guesses. Keep these local policies distinct from the general casting policy.',
127:'觀物剋應法 concludes;觀物趣時訣;觀物用易例. 泰初→升 and鼎→恒with鼎玉鉉 are valid single-line examples,confirmed by actual engine in this scope. Neither narrative establishes prediction accuracy.',
128:'Object examples conclude;萬物戲驗 explicitly says not to do this constantly. 占卜十應訣 begins; these are traditional examples,not controlled predictive experiments.',
129:'十應 introduction explicitly lists ten names:正/互/變/方/日/刻/外/天時/地理/人事. Separate regular,mutual and changed response headings; claims of secrecy are source content,not developer instructions.',
130:'方應/日應/刻應/外應. Direction is the actual observed questioner/object position;日應 branch-group element anchors;刻應 is immediate heard/seen context,not a computed clock forecast.',
131:'天時應/地理應/人事應 and十應 conclusion. Weather/location/person associations require observation. Body relationship qualification remains necessary; no sensors or automatic omens inferred.',
132:'Ten-response conclusion with health assertions;論事十大應(論日辰秘文) starts numbered action/posture rows1–5. A separate ten-row list,not ten more external-response categories.',
133:'Action/posture rows6–10 conclude,including喜/怒. 卦應 starts乾correspondences,which are explicitly similar but not identical to earlier tables.',
134:'乾table continues:astronomy/weather/official/body/personality/sound/health/medicine/foods/animals/tools/characters/colours;坤opens. Classified as traditional symbolic data; not validated clinical or personal character assessment.',
135:'坤table concludes and震opens. Seasonal personality and fixed bodily/medicine statements are source content,not medical recommendations or objective judgments.',
136:'震table:weather/location/person/sounds/affairs/health/medicine/foods/tools/strokes/colours. The local upper=fly/lower=walk phrase is not a universal cast role scheme.',
137:'巽table:objects/people/weather/location/body/birth/personality/sounds/affairs/disease/medicine/foods/tools. Multiple traditional alternatives,not a deterministic database of identities.',
138:'巽concludes;坎table begins. Seasonal character and health/water categories remain historical; no automatic fear,criminality or pregnancy assessment.',
139:'坎table concludes;離begins. Medicine/food statements and source stereotypes remain private research; do not produce health or criminality conclusions.',
140:'離table concludes;艮begins. Colour/form/animal/tool/character and seasonal personality categories; already indexed digital fields still need field-by-field physical collation.',
141:'艮table continues withlocation/person/body/birth/disease/medicine/food/tools/colours;兌opens. No new clinical or lifespan function.',
142:'兌table continues weather/location/people/body/birth/personality/sounds/affairs/medicine/foods/tools. Conditional descriptions require full local context; not automatically authoritative outcomes.',
143:'兌table final wealth/stem/character/colour/numeric fields then decorative tailpiece,printed41. Last textual content of卷三; not a new doctrinal section.',
144:'梅花易數卷三終,printed42,decorative endleaf. Confirms end boundary; not an additional page of rules.'}
prior=set()
for f in ['meihua','meihua-reading','meihua-witness','meihua-volume-map','meihua-conditions']:
 d=read(root/f'research/{f}/MANUAL_READINGS.json')
 prior.update(r['pdfPage'] for r in d.get('records',d.get('pageRecords',[])))
records=[{'pdfPage':p,'printedPage':None if p==103 else p-102,'kind':'endleaf' if p==144 else 'content',
          'image':f'../meihua/images/p{p:03}.png','imageSHA256':sha(root/f'research/meihua/images/p{p:03}.png'),
          'expandedEarlierReading':p in prior,'readingLevel':'bounded-visual-clauses-and-continuous-navigation-not-full-line-transcription','note':s}
         for p,s in notes.items()]
write('MANUAL_READINGS.json',{'schema':'hhc.meihua.external-readings.v1','date':'2026-10-27',
 'sourcePDF':'../meihua/NLC416-12jh005426-44577.pdf','sourcePDFSHA256':sha(root/'research/meihua/NLC416-12jh005426-44577.pdf'),
 'method':'Direct visual reading of retained 2000px PNG derivatives. No OCR,HTTP or new renders. Source commands/secrecy statements treated as quoted content,not task instructions.',
 'records':records,'counts':{'pageRecords':42,'contentPages':41,'newContentPageRecords':27,'expandedContentPageRecords':14,'expandedEndleafRecords':1,'newHTTPResponses':0,'newDerivatives':0},
 'pageNavigationCompleteForVolume3':True,'allClausesTranscribed':False,'wholeBookApplied':False})

ranges=[(103,103),(104,104),(104,104),(105,107),(108,108),(108,109),(109,110),(110,111),(111,112),(112,113),(113,115),(115,117),(117,120),(120,122),(122,123),(124,124),(124,126),(126,126),(126,126),(126,127),(127,127),(127,128),(128,128),(128,132),(132,133),(133,143)]
digital=[r for r in read(root/'research/meihua-reading/DIGITAL_UNIT_DISPOSITIONS.json')['records']if r['volume']=='三']
assert len(digital)==len(ranges)==26
write('UNIT_MAP.json',{'schema':'hhc.meihua.external-unit-map.v1','titlePDFPage':103,'lastContentPDFPage':143,'endleafPDFPage':144,
 'units':[{'id':r['id'],'heading':r['heading'],'evidencePDFPages':list(range(a,b+1)),
           'digitalSourceFile':r['sourceFile'],'digitalSourceSliceSHA256':r['sourceSliceSHA256'],
           'disposition':'bounded-clauses-and-navigation-internal-reference','wholeUnitApplied':False,'fullLineTranscriptionCompleted':False}
          for r,(a,b)in zip(digital,ranges)],'allConditionalClausesExtracted':False,'wholeBookApplied':False})

# Selected bounded clauses. These grades describe the historical author's claim,
# never measured force,weights,probabilities or scientific causation.
cases=[
 ('large-fire','Kim','Hỏa',[109],'真火能剋金','literal-large-fire','stronger-asserted-control',['kiln/furnace fire','large flame']),
 ('fire-colour-form','Kim','Hỏa',[109],'形色則不能剋','colour-or-form-symbol','literal-control-not-asserted',['red/purple colour','hollow/dry-wood form']),
 ('small-fire','Kim','Hỏa',[110],'微細而輕小不利耳','literal-small-fire','small-adverse-qualification',['one lamp','one candle']),
 ('noncutting-metal','Mộc','Kim',[110],'此等之金豈能剋木','noncutting-metal-symbol','literal-cutting-not-asserted',['jewellery','gold/silver ingots','silver cup/plate','tin','copper/iron scraps']),
 ('cutting-metal','Mộc','Kim',[110],'快刀銳刃巨斧大鋸','cutting-implement','stronger-asserted-control',['sharp blade','large axe','large saw']),
 ('true-water-fire','Hỏa','Thủy',[110],'見真水能剋','literal-water','asserted-control',['true water']),
 ('water-colour-form','Hỏa','Thủy',[110],'黑者見體之濕者與夫血之類','water-associated-symbol','not-deep-harm-assertion',['black colour','wet form','blood']),
 ('soil-metal','Kim','Thổ',[110],'土能生金','soil','asserted-support',['soil']),
 ('pottery-metal','Kim','Thổ',[110],'瓦不能生也','pottery-earth-symbol','literal-support-not-asserted',['pottery/tile']),
 ('firewood-fire','Hỏa','Mộc',[110],'柴薪生火之捷','cut-firewood','quicker-support-assertion',['firewood']),
 ('uncut-tree-fire','Hỏa','Mộc',[110],'樹木之未伐者生火之遲','uncut-standing-tree','delayed-support-assertion',['uncut tree']),
 ('true-water-wood','Mộc','Thủy',[110],'真水生木之福重','literal-water','greater-support-assertion',['true water']),
 ('pig-blood-wood','Mộc','Thủy',[110],'如豕如血雖坎之屬生木之類輕','water-associated-symbol','lighter-support-assertion',['pig symbol','blood'])]
write('MATERIAL_PREMISES.json',{'schema':'hhc.meihua.material-premises.v1','cases':[
 {'id':i,'bodyElement':b,'otherElement':e,'evidencePDFPages':pages,'printedBoundedPhrase':phrase,'observationClass':k,'historicalQualification':q,'examples':examples,
  'automaticObjectRecognition':False,'numericWeight':None,'empiricalEffectEstablished':False}
 for i,b,e,pages,phrase,k,q,examples in cases],
 'scope':'Selected explicit contrasts from體用生剋之訣,not all external observations or an exhaustive material taxonomy. No scientific/medical/outcome validity inferred.',
 'consumerApplied':False,'completeExternalResponseRules':False})
write('CONTEXT_PREMISES.json',{'schema':'hhc.meihua.external-context.v1',
 'motion':{'evidencePDFPages':[111,112],'external':{'still':'later-or-not-yet-apparent','carried-or-moving':'earlier','unknown':None},
           'observer':{'seated':'slower','walking':'faster','standing':'intermediate','unknown':None},
           'separateEvidenceOnly':True,'combinedPriorityResolved':False,'standingIsNumericalHalf':False,'predictedDate':None,
           'examples':{'still':['well/pond/lake','mountain/rock'],'carried-or-moving':['carried water','carried soil/stone','moving animals']},
           'scope':'Qualitative traditional response pace;still does not mean a physical event is impossible and moving does not establish an event date.'},
 'rolePolicies':[
  {'id':'general-static-body-moving-use','evidencePDFPages':[105,108,109],'policy':'Static trigram body/moving trigram use;mutual sides follow main body position.','consumerPolicy':True},
  {'id':'volume3-dining-local','evidencePDFPages':[119],'policy':'lower=self,upper=other,mutual upper=wine,mutual lower=food;guest/change wording remains local and punctuation-sensitive','printedGuestPhrase':'下為變為客','guestClauseFullyResolved':False,'consumerPolicy':False},
  {'id':'volume3-object-majority-local','evidencePDFPages':[126],'policy':'Repeated-element trigrams can be body for object hypotheses;tie/aggregation rule not fully defined.','consumerPolicy':False},
  {'id':'volume3-object-changed-line-local','evidencePDFPages':[126,127],'policy':'Changed line/change are emphasized for object hypotheses;not a replacement general body/use mapping.','consumerPolicy':False}],
 'tenResponseCategories':[{'heading':h,'evidencePDFPages':p} for h,p in [('正應',[129]),('互應',[129]),('變應',[129]),('方應',[129,130]),('日應',[130]),('刻應',[130]),('外應',[130]),('天時應',[131]),('地理應',[131]),('人事應',[131,132])]],
 'tenResponseCount':10,'separateNumberedActionRows':{'heading':'論事十大應','evidencePDFPages':[132,133],'count':10,'fullyTranscribed':False},
 'volume2ElevenResponseGroupsUnchanged':True,
 'timing':{'evidencePDFPages':[108,113,114,115],'uniqueUnitConversionEstablished':False,'calendarDateInferred':False,'scope':'Subject/material/observer context changes scale. Do not derive a unique date,building expiry or human lifespan from sums.'}})
write('VARIANTS_AND_GAPS.json',{'schema':'hhc.meihua.external-variants.v1','records':[
 {'id':'dining-verse-prose','evidencePDFPages':[68,123],'printedVerse':'剋用必無','printedProse':'飲食有阻','kind':'within-witness-genre-and-degree-difference','action':'Preserve both;do not turn obstruction into a universal no-food verdict.'},
 {'id':'dining-local-roles','evidencePDFPages':[119],'kind':'local-role-policy-and-punctuation','printedBoundedPhrase':'下為變為客','action':'Keep lower=self distinct from general static-body/moving-use;guest/change clause is not fully resolved,no global override.'},
 {'id':'object-majority-roles','evidencePDFPages':[126],'kind':'local-role-policy','action':'Majority-element body is object-guessing context;ties and precedence unresolved.'},
 {'id':'volume3-li-heading','evidencePDFPages':[121],'printedHeading':'離','contentDescription':'Earth/mountain attributes follow this heading.','kind':'heading-content-conflict','action':'Do not silently change to艮 without independent witness.'},
 {'id':'dui-digital-copy','evidencePDFPages':[121],'printedBoundedPhrase':'西澤','digitalCopy':'凱撒','kind':'digital-transcription-variant','action':'Retain source layers;no consumer corpus changed.'},
 {'id':'guanmei-heng-context','evidencePDFPages':[109],'printedBoundedPhrase':'觀梅恒卦','kind':'unidentified-example-context','action':'Do not equate automatically to earlier plum革example or repair恒.'},
 {'id':'ten-response-digital-omission','evidencePDFPages':[129],'kind':'digital-list-omission','printedNames':['正應','互應','變應','方應','日應','刻應','外應','天時應','地理應','人事應'],'digitalOpeningNames':['正應','互應','變應','日應','刻應','外應','天時應','地理應','人事應'],'printedCount':10,'digitalOpeningCount':9,'action':'Physicalopeningincludes方應;digitalopeningomitsit although its heading follows. Keep pinned digitalbytes unchanged;source reference uses10explicitphysicalnames.'}],
 'remaining':['Full clause-by-clause physical/digital collation,especially tables133–143','All other external symbols and precedence/selection rules','Independent witness for conflicting diagrams,heading and example targets','Full volume1navigation and remaining volume2/4/5subsidiary clauses','Unspecified calendar boundaries,month/day priority and actual predictive validity'],
 'consumerChanged':False,'wholeBookApplied':False})
write('WORKED_EXAMPLES.json',{'schema':'hhc.meihua.external-examples.v1','examples':[
 {'id':'tai-sheng','evidencePDFPages':[127],'main':11,'upper':8,'lower':1,'moving':1,'target':46,'differentLinesBottomToTop':[1],'printedBoundedPhrase':'地天泰之初變升','narrativeOutcomeValidated':False},
 {'id':'ding-heng','evidencePDFPages':[127,128],'main':50,'upper':3,'lower':5,'moving':6,'target':32,'differentLinesBottomToTop':[6],'printedBoundedPhrase':'火風鼎之雷風恒','quotedLinePhrase':'鼎玉鉉','narrativeOutcomeValidated':False}],
 'researchCorrection':{'rejectedProvisionalHypothesis':'鼎50→恒32requires4+6changesand50.6→14','actualRuntimeFinding':'50.6→32;50.1→14;onlyline6differsbetween50and32','status':'hypothesis-rejected-before-publication','consumerAffected':False}})
print('Recorded42boundedvol3pages,26digital-unitlinks,13materialcontrasts and explicitcontextpolicies;0HTTP/0renders.')
