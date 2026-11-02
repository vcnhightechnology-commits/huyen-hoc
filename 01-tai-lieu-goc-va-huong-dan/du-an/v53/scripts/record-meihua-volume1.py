from pathlib import Path
from hashlib import sha256
import json
root=Path(__file__).resolve().parent.parent
base=root/'research/meihua-volume1';base.mkdir(exist_ok=True)
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
def write(name,d):(base/name).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
sha=lambda p:sha256(p.read_bytes()).hexdigest()
notes={
13:'卷一title/printed1. Eight numbers,elements,generation/control,seasonal strong/weak,ten stems/twelve branches. Attributed宋邵雍夫著 is a printed attribution,not historical authorship proof.',
14:'Eight trigram line mnemonics;占法/玩法;modulo8andmodulo6 rules begin. Printed secrecy statements are source content,not instructions to the developer.',
15:'Modulo6concludes;互卦起例 uses middlefour lines with special乾坤無互/互其變卦 wording. Date/time andobject-count arithmetic;calendar boundaries are not supplied.',
16:'Object-countconcludes;general聲音upper=count/lower=hour;字占 andone-characterstroke scheme. Two-group worked sound example is a separate premise,not silently merged.',
17:'Two/three/four/five/six/seven-character sections:split rule andhistoricaltone values. No automatic modern Vietnamese tone substitution.',
18:'Seven/eight/nine/ten/eleven-plus words;eleven-plus countcharacters withouttones;丈尺 usesmajor/minor,nohour. Existing implemented methods not counted anew asvalidation.',
19:'尺寸 upper尺/lower寸 plus hour,drop分;為人占 uses words/person/body/object/colour,withmanyalternativepremises. Notautomatic personalcharacter inference.',
20:'為人concludes,self-casting,animals/staticobjects. Animal group versus singleobjectselection,actualdirection andhour arepremises;birth/purchase/installationtime forstaticobjects. No invented time.',
21:'Staticobjectsconclude:unusual trigger/actualconstructiontime,otherwise無故不占. 後天object/directionrule andfirstsmalltrigramcorrespondences.',
22:'Smallcorrespondences巽坎離艮兌 anddirectiondiagram. Southtop/northbottom. Fullbody/animal/material words remain symbolic associations.',
23:'Directionconclusion;plumworkedexample49.1→31 already checkedearlier. Narrative injuryprediction not empirical validation.',
24:'Peonyworkedexample44.5→50alreadychecked;knocking/borrowingexamplebegins. Material/contextreasoning distinguishesaxe fromhoe,not a unique physicalidentitytest.',
25:'Borrowingexampleconcludes;今日動靜 six-word toneexamplebegins. Arithmetic fixtures already preserved,notrerun toinflatecoverage.',
26:'今日exampleconcludes;西林templeglyph/stroke example. Historical claimof preventing misfortune byediting acharacter is notvalidated andnot aninstruction toeditplaces/names.',
27:'Templeconcludes;oldmanworryexample. Response-scale seateddouble/walkinghalf/standingintermediate depends on localcontext;not a generaldatetimecalculator.',
28:'Timingconcludes;youngmanjoyexample andcowcry examplebegin. Pregnancy/health/death narratives are historical,notconsumerdeterminations.',
29:'Cowconcludes;chickencry andfallingbranch examples. Existing sourcearithmeticcases retained;no new outcomevalidation.',
30:'Branchconcludes;風覺鳥占 and風覺占. Direction,season,colour,sound intensity are explicitlycontextual;not modern weatherforecasting.',
31:'Windconcludes;鳥占/聽聲音占. Birdcount,callingcount andobservedform are alternatives;general聲音context isnot automaticallythetwo-groupknockingmethod.',
32:'Soundconcludes;形物占,驗色占 andcompact八卦內外動靜圖. Form/colour categories are local symbolicpremises,not universal image recognition.',
33:'Compactdiagramconcludes;八卦萬物類占 and乾palaceeightnames;乾table天時/地理 begin. Completepalacerow transcribed separately;fullfieldbodies notallcollated.',
34:'乾table人物through生產:traditional person/body/time/animal/material/home/marriage/food/birth assertions. Headernavigation only forfulltable,notvalidatedclinical/foodadvice.',
35:'乾table求名through五色. Printed謀望differsdigitalheading謀旺. Financial/legal/health/grave claims retainedas traditionalassertions.',
36:'乾姓字/數目/五味conclude;坤palaceeightnames andfirstseven坤fields. Names/phonology andstrokeassociations arenot automaticnameanalysis.',
37:'坤動物through謀望. Conditionalhome/birth/wealth/season claims notconvertedinto empiricallyvalidatedpredictions.',
38:'坤出行through五色conclude;震palaceeightnames. Sourcepalacenamegroup isnot the uppertrigram ofeverymember.',
39:'震firsttwelvefields. Person/body ordering differsfromdigitalpresentation;valuesarenotallphysicallytranscribed.',
40:'震求利through姓字. Historicalpregnancy/medical/legaldirections remainresearchonly;no outcomeweights.',
41:'震數目/方道/五味/五色conclude;巽palaceeightnames andfirstfivefields. Colour context includesmoretokens than驗色paragraph32.',
42:'巽時序through交易. Traditionaltrade/marriage/birth/food/officecategories remain assertionswithseason/context conditions.',
43:'巽謀望through五色conclude. Printedheading謀望notdigital謀旺;notanexcusetonormalizeoriginalbytes.',
44:'坎palaceeightnames andfirsttenfields through飲食. Physical動物=豕魚水中之物 ismissingasaseparatefieldfromthe214-fielddigitalindex.',
45:'坎飲食continuationthen家宅through疾病. Medical/legal/foodclaimsremainhistorical;sourcepresenceisnotvalidation.',
46:'坎官訟through五色conclude;離palaceeightnames,天時/地理begin. Firepalacecontainsmixedupper/lowertrigrams;do notoverwriteMaiHoa體element.',
47:'離地理continuation,人物through求名. Historicaldirection/season/health/foodclaims not automatic recommendations.',
48:'離求利through五色. Marriage/wealth/legal/health statements conditionalandunvalidated;no finalprognosiscompiled.',
49:'離五味concludes;艮palaceeightnames,firsteightfields. Genpalace tableitselfisdistinctfromthedininglocalrolepolicyinvolume3.',
50:'艮家宅through疾病. Physicaltablehasdistincthome/dwellingandtraditionalriskconditions;notacompletehouse-layoutmethod.',
51:'艮官訟/墳墓/姓字/數目/方道/五色/五味conclude;兌palaceeightnamesstart. Physical艮姓字宮音帶土字傍之姓氏行位五七ismissingfromdigital26-fieldGenindex.',
52:'兌palacelastlabel歸妹continuesacrosslayout;人物through求名. Explicitdining/birthclaimsnotconsumerdeterminations.',
53:'兌求利through五色. Printed謀望isoneofeightheadingpositionswherepinneddigitaluses謀旺. Preservebothsource layers.',
54:'兌五味辛辣,closingparagraph,卷一終andtailpiece,printed42. Thispagecontainsdoctrinaltext,notapureendleaf.'}
prior=set()
for folder in ['meihua','meihua-reading','meihua-witness','meihua-volume-map','meihua-conditions','meihua-external']:
 d=read(root/f'research/{folder}/MANUAL_READINGS.json')
 prior.update(r['pdfPage']for r in d.get('records',d.get('pageRecords',[])))
if read(root/'research/meihua-conditions/MANUAL_READINGS.json').get('boundaryPage54Reinspected'):prior.add(54)
records=[{'pdfPage':p,'printedPage':p-12,'kind':'content-and-closing'if p==54 else'content',
 'image':f'../meihua/images/p{p:03}.png','imageSHA256':sha(root/f'research/meihua/images/p{p:03}.png'),
 'expandedEarlierReading':p in prior,'earlierBoundaryReadingOnly':p==54,
 'readingLevel':'bounded-visual-clauses-and-complete-page-navigation-not-full-transcription','note':n}for p,n in notes.items()]
write('MANUAL_READINGS.json',{'schema':'hhc.meihua.volume1-readings.v1','date':'2026-10-27','sourcePDF':'../meihua/NLC416-12jh005426-44577.pdf',
 'sourcePDFSHA256':sha(root/'research/meihua/NLC416-12jh005426-44577.pdf'),'records':records,
 'counts':{'pageRecords':42,'contentPages':42,'newPageRecords':23,'expandedEarlierReadings':19,'includingEarlierBoundaryReadings':1,'newPNGDerivatives':18,'retainedPNGDerivatives':232,'newHTTPResponses':0},
 'method':'Directvisualreading ofretained/localPoppler2000pxrenders,noOCR;18missingrendersfromoriginalPDF,all214previousrecordsunchanged.',
 'allVolume1ClausesExtracted':False,'wholeBookApplied':False})
baseline=read(root.parent/'archives/v53-before-meihua-volume1/EXTRACTED_PAGES.json')
write('SOURCE_BASELINE.json',{'previousIndex':'../../../archives/v53-before-meihua-volume1/EXTRACTED_PAGES.json','previousRenderedRecords':baseline['pages'],'expectedPriorDerivatives':214,'newRenderedPages':[32,33,34,35,37,38,39,40,42,43,44,45,47,48,49,50,52,53]})
ranges=[(13,13)]*7+[(14,14)]*4+[(14,15),(15,15),(15,15),(15,16),(16,16),(16,16),(16,18),(18,18),(19,19),(19,20),(20,20),(20,20),(20,21),(21,21),(21,22),(22,23),(23,23),(24,24),(24,25),(25,26),(26,27),(27,28),(28,28),(28,29),(29,29),(29,30),(30,30),(30,31),(31,31),(31,32),(32,32),(32,32),(32,33),(33,54)]
digital=[r for r in read(root/'research/meihua-reading/DIGITAL_UNIT_DISPOSITIONS.json')['records']if r['volume']=='一']
assert len(digital)==len(ranges)==45
write('UNIT_MAP.json',{'schema':'hhc.meihua.volume1-unit-map.v1','titlePDFPage':13,'lastContentPDFPage':54,'lastPrintedPage':42,
 'units':[{'id':d['id'],'heading':d['heading'],'evidencePDFPages':list(range(a,b+1)),'digitalSourceSliceSHA256':d['sourceSliceSHA256'],
           'wholeUnitApplied':False,'fullClauseTranscriptionCompleted':False}for d,(a,b)in zip(digital,ranges)],
 'allConditionalClausesExtracted':False,'wholeBookApplied':False})

# Literal printed header positions,with digital values kept in their own layer.
pages={
 '乾':[(33,'天時 地理'),(34,'人物 人事 身體 時序 動物 靜物 屋舍 家宅 婚姻 飲食 生產'),(35,'求名 謀望 交易 求利 出行 謁見 疾病 官訟 墳墓 方道 五色'),(36,'姓字 數目 五味')],
 '坤':[(36,'天時 地理 人物 人事 身體 時序 靜物'),(37,'動物 屋舍 家宅 飲食 婚姻 生產 求名 交易 求利 謀望'),(38,'出行 謁見 疾病 官訟 墳墓 姓字 數目 方道 五味 五色')],
 '震':[(39,'天時 地理 身體 人事 人物 時序 靜物 動物 屋舍 家宅 飲食 婚姻'),(40,'求利 求名 生產 疾病 謀望 交易 官訟 謁見 出行 墳墓 姓字'),(41,'數目 方道 五味 五色')],
 '巽':[(41,'天時 地理 人物 人事 身體'),(42,'時序 靜物 動物 屋舍 家宅 飲食 婚姻 生產 求名 求利 交易'),(43,'謀望 出行 謁見 疾病 姓字 官訟 墳墓 數目 方道 五味 五色')],
 '坎':[(44,'天時 地理 人物 人事 身體 時序 靜物 動物 屋舍 飲食'),(45,'家宅 婚姻 生產 求名 求利 交易 謀望 出行 謁見 疾病'),(46,'官訟 墳墓 姓字 數目 方道 五味 五色')],
 '離':[(46,'天時 地理'),(47,'人物 人事 身體 時序 靜物 動物 屋舍 家宅 飲食 婚姻 生產 求名'),(48,'求利 交易 謀望 出行 謁見 官訟 疾病 墳墓 姓字 數目 方道 五色'),(49,'五味')],
 '艮':[(49,'天時 地理 人物 人事 身體 時序 靜物 動物'),(50,'家宅 屋舍 飲食 婚姻 求名 求利 生產 交易 謀望 出行 謁見 疾病'),(51,'官訟 墳墓 姓字 數目 方道 五色 五味')],
 '兌':[(51,'天時 地理'),(52,'人物 人事 身體 時序 靜物 動物 屋舍 家宅 飲食 婚姻 生產 求名'),(53,'求利 出行 交易 謀望 謁見 疾病 墳墓 官訟 姓字 數目 方道 五色'),(54,'五味')]}
tables=read(root/'research/meihua-reading/TRIGRAM_TABLE_FIELDS.json')['tables'];header_records=[]
manual_omissions={('坎','動物'):'豕魚水中之物',('艮','姓字'):'宮音帶土字傍之姓氏行位五七'}
for t,groups in pages.items():
 fields=[(h,p)for p,heads in groups for h in heads.split()];assert len(fields)==27
 table=next(x for x in tables if x['trigram']==t)
 for order,(heading,p)in enumerate(fields,1):
  dh='謀旺'if heading=='謀望'else heading;d=next((f for f in table['fields']if f['field']==dh),None)
  r={'trigram':t,'printedHeader':heading,'physicalOrderInTable':order,'headerPDFPage':p,'bodyPDFPages':[p],
     'digitalHeader':d['field']if d else None,'digitalBodySHA256':d['textSHA256']if d else None,
     'digitalBody':d['text']if d else None,'fullBodyCollationCompleted':False,'consumerApplied':False}
  if(t,heading)in manual_omissions:r.update(printedBoundedBody=manual_omissions[t,heading],boundedBodyVisuallyTranscribed=True)
  if(t,heading)==('坎','飲食'):r['bodyPDFPages']=[44,45]
  if(t,heading)==('離','地理'):r['bodyPDFPages']=[46,47]
  header_records.append(r)
write('TABLE_FIELDS.json',{'schema':'hhc.meihua.physical-table-fields.v1','source':'../meihua/NLC416-12jh005426-44577.pdf',
 'records':header_records,'counts':{'physicalHeaderPositions':216,'perTable':27,'pinnedDigitalFields':214,'missingDigitalFields':2,'differentHeaderSlots':8,'fullyBodyCollatedAllFields':False},
 'policy':'Headerpositionisphysicallyread;digitalbodyretainsitsownSHAandisnotassertedidenticaltoprint. Onlytwomissingfields haveboundedmanualbodytranscription. Noautomaticprognosisorname/health/foodclaims.'})

# Names are directly read; KingWenIDs/upper/lower IDs are editorial identification,
# independently checked with the actual engine,not numbers printed in this row.
rows=[
 ('乾',1,'Kim',[33],[('乾為天',1,1,1),('天風姤',1,5,44),('天山遯',1,7,33),('天地否',1,8,12),('風地觀',5,8,20),('山地剝',7,8,23),('火地晉',3,8,35),('火天大有',3,1,14)]),
 ('坤',8,'Thổ',[36],[('坤為地',8,8,2),('地雷復',8,4,24),('地澤臨',8,2,19),('地天泰',8,1,11),('雷天大壯',4,1,34),('澤天夬',2,1,43),('水天需',6,1,5),('水地比',6,8,8)]),
 ('震',4,'Mộc',[38],[('震為雷',4,4,51),('雷地豫',4,8,16),('雷水解',4,6,40),('雷風恒',4,5,32),('地風升',8,5,46),('水風井',6,5,48),('澤風大過',2,5,28),('澤雷隨',2,4,17)]),
 ('巽',5,'Mộc',[41],[('巽為風',5,5,57),('風天小畜',5,1,9),('風火家人',5,3,37),('風雷益',5,4,42),('天雷无妄',1,4,25),('火雷噬嗑',3,4,21),('山雷頤',7,4,27),('山風蠱',7,5,18)]),
 ('坎',6,'Thủy',[44],[('坎為水',6,6,29),('水澤節',6,2,60),('水雷屯',6,4,3),('水火既濟',6,3,63),('澤火革',2,3,49),('雷火豐',4,3,55),('地火明夷',8,3,36),('地水師',8,6,7)]),
 ('離',3,'Hỏa',[46],[('離為火',3,3,30),('火山旅',3,7,56),('火風鼎',3,5,50),('火水未濟',3,6,64),('山水蒙',7,6,4),('風水渙',5,6,59),('天水訟',1,6,6),('天火同人',1,3,13)]),
 ('艮',7,'Thổ',[49],[('艮為山',7,7,52),('山火賁',7,3,22),('山天大畜',7,1,26),('山澤損',7,2,41),('火澤睽',3,2,38),('天澤履',1,2,10),('風澤中孚',5,2,61),('風山漸',5,7,53)]),
 ('兌',2,'Kim',[51,52],[('兌為澤',2,2,58),('澤水困',2,6,47),('澤地萃',2,8,45),('澤山咸',2,7,31),('水山蹇',6,7,39),('地山謙',8,7,15),('雷山小過',4,7,62),('雷澤歸妹',4,2,54)])]
wiki=(root/'research/meihua/volume-一.wiki').read_text(encoding='utf-8-sig')
digital_names={}
for name,_,_,_,_ in rows:
 section=wiki.split("'''"+name+"卦'''",1)[1].split('天時',1)[0]
 lines=[s.strip()for s in section.splitlines()if s.strip()]
 digital_names[name]=' '.join(lines[1:]).split()
 assert len(digital_names[name])==8
palace_rows=[{'printedParent':name,'parentTrigram':tri,'palaceElement':el,'evidencePDFPages':ps,
 'members':[{'ordinal':i,'printedName':label,'digitalName':digital_names[name][i-1],'upper':u,'lower':l,'number':kw}for i,(label,u,l,kw)in enumerate(members,1)]}for name,tri,el,ps,members in rows]
name_variants=[{'parent':r['printedParent'],'ordinal':m['ordinal'],'printedName':m['printedName'],'digitalName':m['digitalName'],'numberEditoriallyIdentified':m['number'],'evidencePDFPages':r['evidencePDFPages']}for r in palace_rows for m in r['members']if m['printedName']!=m['digitalName']]
assert len(name_variants)==7
write('PALACE_ROWS.json',{'schema':'hhc.meihua.eight-palace-rows.v1','rows':palace_rows,
 'pinnedDigitalSHA256':sha(root/'research/meihua/volume-一.wiki'),'nameVariants':name_variants,'differentNamePositions':7,
 'nameSequence':'literalprintedrows;notachronologicalmoving-lineevent','numbersAndTrigrams':'editorialidentificationofnamedhexagrams,checkedagainstactualengine','derivationMasksBottomLSB':[0,1,3,7,15,31,23,16],
 'maskStatus':'developerinferencefitsall64printednames;notprintedbitnotationoracompletesourceprescription','notEstablished':['世應positions','納甲assignment','六親or六神rules','LụcHàoverdicts','universalpalaceelementasMaiHoabodyelement','houseeight-sectorfortune'],
 'consumerApplied':False,'wholeBookApplied':False})
write('VARIANTS_AND_GAPS.json',{'schema':'hhc.meihua.volume1-gaps.v1','records':[
 {'id':'kan-animal-omission','evidencePDFPages':[44],'printedHeader':'動物','printedBoundedBody':'豕魚水中之物','digitalFieldMissing':True},
 {'id':'gen-name-omission','evidencePDFPages':[51],'printedHeader':'姓字','printedBoundedBody':'宮音帶土字傍之姓氏行位五七','digitalFieldMissing':True},
 {'id':'mou-heading','evidencePDFPages':[35,37,40,43,45,48,50,53],'printedHeader':'謀望','pinnedDigitalHeader':'謀旺','positions':8,'policy':'keeppinneddigitalbytesandphysicalreadingsseparate'},
 {'id':'palace-name-copy-variants','differentNamePositions':7,'positions':name_variants,'policy':'Includesglyph/readings遯/遁,復/複,夬/決,无/無,未/末,兌為澤/兌為金,咸/鹹. Keepbothlayers;engineidentificationfollowsprintedname/structure,notunannouncedrawsourcecorrection.'},
 {'id':'sound-premises','evidencePDFPages':[16,24,25,31,32],'policy':'generalcount/hourandtwo-groupknockingareseparatenamedpremises;notoneuniversalmethod'},
 {'id':'colour-contexts','evidencePDFPages':[32,35,38,41,43,46,48,51,53],'policy':'驗色localmappingandfulltable五色arecontextspecific;Qian大赤/玄,Kun黃/黑etcpreventauniversalcolour-to-onetrigramclassifier'},
 {'id':'all-fields-not-body-collated','evidencePDFPages':list(range(33,55)),'physicalHeaders':216,'digitalFields':214,'policy':'Allheaderspositioned,butfullvalues/variantsnotallcollated. Do notclaim216fullyverifiedpredictions.'}],
 'remaining':['Allsubsidiaryclauseandtablebodycollationacrossfivevolumes','Independentwitnessfordiagram/nuclear/seasonvariants','FullLụcHàopremisesrequireseparateidentifiedwitnesses','PendingconsumerUIcandidateactualbrowser/PDFvalidation'],'wholeBookApplied':False})
write('FIVE_VOLUME_NAVIGATION.json',{'schema':'hhc.meihua.five-volume-navigation.v1','volumes':[
 {'volume':1,'first':13,'lastContent':54,'last':54,'map':'UNIT_MAP.json','digitalUnits':45,'fullClauseExtractionCompleted':False},
 {'volume':2,'first':55,'lastContent':98,'last':98,'map':'../meihua-conditions/UNIT_MAP.json','digitalUnits':52,'fullClauseExtractionCompleted':False},
 {'volume':3,'first':103,'lastContent':143,'last':144,'map':'../meihua-external/UNIT_MAP.json','digitalUnits':26,'fullClauseExtractionCompleted':False},
 {'volume':4,'first':145,'lastContent':187,'last':188,'map':'../meihua-volume-map/UNIT_MAP.json','fullClauseExtractionCompleted':False},
 {'volume':5,'first':189,'lastContent':227,'last':228,'map':'../meihua-volume-map/UNIT_MAP.json','fullClauseExtractionCompleted':False}],
 'counts':{'volumeSpanPages':212,'contentPagesIncludingTitleAndClosing':209,'endleaves':3,'threeDigitalVolumeUnits':123,'volume4and5GroupedNestedUnits':93},
 'excluded':{'frontMatter':list(range(1,13)),'advertisements':[99,100,229,230],'logo':[101],'physicalLowerBookCover':[102],'imprint':[231],'backMatter':[232]},
 'policy':'CompletepagenavigationandretainedrendersareNOTfullclausereading/application. 93groupednestedunitsareNOTdirectlycomparablewith123digitalsectionsorindependentworks.',
 'all232PDFPagesRendered':True,'wholeBookApplied':False,'wholeCatalogueCompleted':False})
print('42boundedpages,45unitlinks,216physicalheaders/2digitalomissions,64palacenames;all232rendersretained,notwholeworkcomplete.')
