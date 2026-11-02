from pathlib import Path
from hashlib import sha256
from PIL import Image
import json
s=Path(__file__).resolve().parent;w=s.parent.parent
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
m=read(s/'NATIVE_IMAGES.json')
for x in m['records']:x['actuallyViewed']=True;x['readingLevel']='firstpasswholespread;notallglyphsdiplomaticallycollated';x['newSourceReadPosition']=True
write(s/'NATIVE_IMAGES.json',m)
units=[('P08-01','論宅外形第一',6,34,'partial',list(range(6,13))),('P08-02','論福元第二',34,58,'bookmark-only',[]),('P08-03','論大遊年第三',58,81,'bookmark-only',[]),('P08-04','論穿宫九星第四',81,94,'firstpass-span',list(range(81,94))),('P08-05','論玄空装卦訣第五',94,100,'opening-only',[94]),('P08-06','論開門修造門第六',100,105,'bookmark-only',[]),('P08-07','論放水第七',105,111,'closing-boundary-only',[111]),('P08-08','論宅内形第八',111,124,'firstpass-span',list(range(111,124))),('P08-09','論選擇第九',124,168,'opening-only',[124]),('P08-10','論符鎮第十',168,195,'bookmark-only',[])]
write(s/'UNIT_MAP.json',{'date':'2026-10-28','basis':'Ten numbered論headingsmanuallyreadinprintedTOC3–5. Bodyintervalstartsguidedbyrepositorybookmarks;4/8andopenings1/5/9confirmedbydirectimages. Endpointsinclude sharedboundarypages;notallbookmarksmanuallyvalidated. Four卷arenotfourbooks,nor10volumes.','prefacePositions':[1,2],'printedTOCPositions':[3,4,5],'records':[{'id':id,'heading':h,'startPDFPage':a,'nextUnitStartPDFPageOrDocumentEnd':b,'status':st,'actuallyViewedPositions':ps,'allClausesApplied':False}for id,h,a,b,st,ps in units],'numberedMainUnits':10,'fullFirstPassBodySpans':2,'wholeUnitsApplied':0,'all195PositionsRead':False})
contexts=[
 (1,'preface-1','引','Preface criticizes transmitted obscurity/speculation and mentions分房/玄空掛卦. Literary framing,notproofallrules correct.'),
 (2,'preface-2','萬曆庚寅春二月上浣','Preface date directlyprinted,notanindependentlyprovedimprintdate;何洛文namevisible.'),
 (6,'external-over-internal','若大形不善總内形得法終不全吉','Source hierarchyrequiresexternalcontext;doesnotempiricallyvalidategood/badsiteorallowroom-onlyoverallrating.'),
 (81,'height-versus-position','方位雖吉而層數之中若宜高者下宜下者高則凶','Sourcepreviouspositionruleisnotsolecriterion;chapterrequiresseparatelayercontext.'),
 (81,'two-methods','大門止是遊年一節','Compiler criticizesmaingate-onlymethod;doesnotinvalidateothernamedtraditionsglobally.'),
 (81,'separate-courtyard-origin','有牆隔斷牆間開有門','Sourceexpresslyresetsfromthatplaceandseparatesother院;do notmakemoderneachstoreyorroomanequivalent院.'),
 (81,'main-yimen-distinct','大門在巽儀門在离','Sourceexamplekeepsmaingate/yimen/firstlayersseparate;donotcollapsegatedirectionandhousefacing.'),
 (81,'unpartitioned-frame','無牆無門隔斷','Sourcehasdistinctunpartitionedcase;amixedwall-only/door-onlystateisnotexplicitlyadjudicatedbythisfragment.'),
 (82,'partition-note','若房層數中間但有門牆隔斷','Diagramnoteexplicitlyreferstoboundaryrule,notmerelyastandardcompassgrid.'),
 (82,'toward-inside-outside','頭一層房朝内開門','Inward-facing/outward-facingdoorchangescountbeginningincommentary;notanorientationallyunqualifieddepthcounter.'),
 (83,'center-caveat','木入中宮','Nominalpositive貪狼canberejectedwithcenterpremise;nolabel-alonefortuneverdict.'),
 (84,'shape-specific-countercase','不宜正當艮字','Sourcequalifiedplacementratherthangloballyall艮-relatedlocationsgood.'),
 (85,'center-caveat-repeat','貪狼乃吉星宜高大','Evencalledgoodstarhascenterqualification;notautomaticallyroomheightadvice.'),
 (86,'diagram-6','坐北朝南開巽門圖','Nativefigurehasupside-downinteriorlabelsrelativetext. Viewedwholespreadbutalldiagramcellsnotyettranscribed.'),
 (87,'diagram-7','坐北朝南開离門圖','Water/fireandheightcompoundcriteria;historicalfamilywealthclaimsnotvalidated.'),
 (88,'diagram-8','坐東朝西開兑門圖','Namedlayoutplusheightnumbers,notonlyentrancetrigram.'),
 (89,'diagram-9','坐東朝西開坤門圖','Same坤entranceappearslaterwithdifferenthouseorientation;do notselectrowsbydoornamealone.'),
 (90,'diagram-10','坐北朝南開坤門圖','Differentlayoutframefrom89. Exactcellsnotallcollated.'),
 (91,'diagram-11','坐南朝北開艮門圖','Differentframefrom84;requiresnamedfigurecoordinate,notjust艮.'),
 (92,'diagram-12','坐東朝西開乾門圖','Differentframefrom82;keepseparate.'),
 (93,'diagram-13','坐西朝東開巽門圖','Differentframefrom86;keepseparate.'),
 (93,'horizontal-jin-frame','一進二進四進五進至十進','Sourceusing進andorderedlayers,notexplicitmodernverticalfloors. Buildingadapterunestablished.'),
 (93,'five-element-cycle','頭層水二層木三層火四層土五層金','Explicitwaterstart+orderedfivecycleand周而復始. Itdoesnotestablisheverylayoutfirstelement,originorheight.'),
 (93,'star-height-qualification','切不可凶星作高房吉星作低房','Sourceheightprescriptionrequiresstarframepluscoordinates;notamodernconstructioninstruction.'),
 (93,'nominal-good-needs-position','若吉星在凶方亦不可高大','Positionalqualificationwith木金/土中宮example;neitherstarsnorelementsalonewholejudgment.'),
 (111,'internal-heading','論宅内形第八','Sourcehouseformmetaphors/roof/bodycomparisonsandhistoricaloutcomes;notdiagnosticinformation.'),
 (112,'ancient-bay-count','假如堂屋作九間分作三','Source間/bayandthresholdlevelproportionsarenotmodernroomcountbyarbitrarypartition.'),
 (112,'paired-door-comment','兩邊相開門最不宜','Historicalparticularframecannotbeimportedastwomoderndoorsalwaysbad.'),
 (112,'water-routing','水不可分兩路','Compoundsiteanddoor/drainagecontext;notengineeringhydrologyorsafetyevidence.'),
 (113,'separate-branches-households','兄弟各路行別方造得門','Familybranchesandroutesarepartofsourcecontext,notpurepolygon geometry.'),
 (113,'mill-position','礱磨必須居左腹右腹','Oldhouseequipment/dragon-tigersymbolsandphysicalusearenotequivalentmodernappliances.'),
 (114,'cardinal-corner-gates','子午坤艮四方','Sourceframeandhousegeometryneeded;donotmergewithother24mountainsoralltraditions.'),
 (114,'occupant-and-additions','家長長房','Sourcefamilyrolesandbuildingmodificationclaimsunvalidated;notpersonalityorhealthmodel.'),
 (115,'fire-an-definition','火唵即是廚房廚竈','Compilerexplicitsubjectiskitchen/stove;otherreportedinterpretationsfirstnewhousebay/ancestorhall/伏位福德arecriticized. Do notsilentlytreatfire-anastemple.'),
 (115,'fire-an-rule','宜在宅凶方不宜在吉方','Namedsourcekitchen/stoverulewithmethod-dependent吉凶;notempiricaladviceorautomaticroomrecommendation.'),
 (115,'fire-an-versus-fulude','宮福徳人之生氣不宜立火唵','Twoframesandvoicecritique;needsfull福元/遊年premisesbeforeanymapping.'),
 (116,'interior-figures-1','單耳房雙耳房','6figurecolumns/tree-shrineformsandcourtyardcase;keepillustrationandinterpretationdistinct,notmetricgeometry.'),
 (117,'interior-figures-2','孤獨房','6figurecolumnsinclude孤獨/露星/單側耳/暗箭/再補焦尾/露骨;nomeasureddistanceorroom-boundarytolerance.'),
 (118,'interior-figures-3','曬屍房丁字房','6figurecolumns;exactshapeclassificationrequiresmorethanhandfulroomcoordinates,nothealthdiagnosis.'),
 (119,'interior-figures-4','水字房王字房','6figurecolumns,source辛fatewordsnotfunctionalvalidation.'),
 (120,'interior-figures-5','重陰房','6figurecolumnsinclorientationalfamilies;namedbirth-houseframesnotautomaticallybazi/natalyearmodernkua.'),
 (121,'interior-figures-6','工字房','6figurecolumns;borrowedlettershapesarenotsinglepolygonnorms.'),
 (122,'interior-figures-7','前高中高後低','6figurecolumns;3Dheight/sourcefront/backmustbedeclared,not2Dfootprintonly.'),
 (123,'interior-figures-8','左右兩屋低中高','6figurecolumns;sourcebadresult/harmclaimsnotapplied.'),
 (124,'compiler-caution','歌解率皆鄙俚不叶','Closingunit8compilercriticizesphrasing,invokes因仍舊言/子不弗取以已意;retainthisvoiceinsteadtreatallverses asoneverifiedrule.'),
 (124,'selection-boundary','論選擇第九','Unit9openingnotreadaswhole;calendarand命前五神notimplementedfromopeningalone.')
]
write(s/'CONTEXT_READINGS.json',{'date':'2026-10-28','basis':'Manualfirstpassgroupingandselectedworkinganchorsfrom40nativespreads. Anchorsmaystopwithincolumns;notfulldiplomatictranscription,notsourceOCR,andnoalleffectsvalidated.','records':[{'id':f'P08-C{i+1:02d}','pdfPage':p,'key':k,'workingAnchor':a,'note':n,'actuallyViewed':True,'allGlyphsDiplomaticallyCollated':False,'fullConditionSetEncoded':False,'practicalOutcomesValidated':False}for i,(p,k,a,n)in enumerate(contexts)],'contextGroups':len(contexts),'all195PagesRead':False,'allRulesApplied':False})
crops=[]
for page,name,box in [(81,'partition-origin-prose.png',[130,300,1150,1860]),(93,'five-cycle-prose.png',[100,290,1150,1870]),(115,'fire-an-definition-prose.png',[1230,300,2370,1840]),(124,'compiler-caution-prose.png',[1490,300,2390,1830])]:
    p=s/f'p{page:03d}.jpg';f=s/name;Image.open(p).crop(box).save(f)
    crops.append({'pdfPage':page,'sourceFile':p.name,'sourceSHA256':sha256(p.read_bytes()).hexdigest(),'file':name,'sha256':sha256(f.read_bytes()).hexdigest(),'box':box,'nativeNoResize':True,'actuallyViewed':False})
write(s/'CROPS.json',{'date':'2026-10-28','records':crops,'noGlyphReconstruction':True})
write(s/'WORK_STATE.json',{'date':'2026-10-28','catalogueID':'P08','status':'newrepositorysource40nativespreads-firstpass-read-twochapterspans-privatefunctionpending','sourcePDF': 'Tianyige-330000-1705-0007405-yangzhai-shishu.pdf','sourceSHA256':m['pdfSHA256'],'sourceBytes':m['pdfBytes'],'sourceContainerPages':195,'actualNativePositionsViewed':len(m['records']),'sourceIndependentInstitutionCatalogItemValidated':False,'PDFRepositoryProcessingNotOriginalInstitutionDownload':True,'prefaceDateNotImprintDate':True,'printedTOCMainUnits':10,'fullFirstPassMainSpans':['P08-04','P08-08'],'allGlyphsCollated':False,'allSourceRulesApplied':False,'consumerChanged':False,'wholeCatalogueCompleted':False,'newRequests':4,'newOriginalRepositoryContainers':1,'newIndependentWitnessComparisons':0,'latestReleaseVerified':{'manifestFiles':3948,'sourceZIPBytes':2107772251,'report':'v53/BAZI_FOOD_CORE_REPORT.md'},'next':['View4QA crops;verifyembeddedJPEGidentityfor40positionsandrawstreamreextractions.','Sourcecounted進layersnotmodernfloors;deriveboundedprivateoriginapplicability/fivecyclecomponentfrom93,withseparateresetpremises81.','Inspectfire-anmeans廚房廚竈/sourcecriticizedothermeanings;noautomatic吉凶roomplacement.','Remaining155positions and8mainunits/fullconditionalrulesactive;do notcall10chapterheadings10booksread.','Promotewhenscopeuseful;preserve3948packagefirst,source/QAoutside site.']})
print(json.dumps({'nativePositionsViewed':len(m['records']),'contextGroups':len(contexts),'printedMainUnits':10,'firstPassMainSpans':2,'pendingUnviewedCrops':4}))
