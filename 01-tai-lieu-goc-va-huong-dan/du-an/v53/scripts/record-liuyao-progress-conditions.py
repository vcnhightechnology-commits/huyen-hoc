from pathlib import Path
from hashlib import sha256
import json,shutil
root=Path(__file__).resolve().parent.parent;w=root.parent;base=root/'research/liuyao-progress-conditions';stage=w/'tmp/liuyao-b02-ch29-staging'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
def write(n,d):(base/n).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
sha=lambda p:sha256(p.read_bytes()).hexdigest()
shutil.copyfile(stage/'motion-qa-131.png',base/'images/motion-qa-131.png')
old=read(stage/'READING_NOTES.json');units=[(29,'進神退神',116,124),(30,'隨鬼入墓',124,130),(31,'獨發',130,134),(32,'兩現',134,136),(33,'星煞',136,138)]
records=[]
for n in range(116,140):
 image=f'images/zengshan-{n}.png'
 records.append({'pdfPage':n,'image':image,'sha256':sha(base/image),'scope':'publisher-advertisement-only'if n==139 else'first-pass-complete-chapter-spans-not-all-clauses',
  'chapterGroups':[i for i,h,a,b in units if a<=n<=b],'inheritedPendingReading':n<=126,
  'expandedEarlierBoundedPage':n in[116,120],'newContentReadingThisRun':127<=n<=138,
  'entirePageDiplomaticallyTranscribed':False})
qa=[]
for n,file in[(117,'fixture-qa-117.png'),(123,'list-qa-123.png'),(124,'critique-qa-124.png'),(131,'motion-qa-131.png'),(134,'heading-qa-134.png'),(136,'stars-qa-136.png'),(137,'stars-qa-137.png'),(136,'noble-verse-example-qa.png')]:
 qa.append({'pdfPage':n,'image':'images/'+file,'sha256':sha(base/'images'/file),'dpi':360,'actuallyViewed':True,
  'kind':'crop'if file.startswith('noble-')else'full-source-QA-render','newSourcePage':False})
write('MANUAL_READINGS.json',{'date':'2026-10-27','sourceID':'B02-ch029-033','sourcePDF':'../liuyao-foundations/NLC416-12jh005345-45344.pdf',
 'sourceSHA256':old['sourceSHA256'],'sourcePDFBytes':11089308,'sourcePDFPages':394,'records':records,'qaImages':qa,
 'counts':{'manualRecords':24,'contentPages':23,'advertisementPages':1,'inheritedPendingPages':11,
 'inheritedPendingNewContentReadings':9,'expandedEarlierBoundedPages':2,'newContentReadingsThisRun':12,
 'newAdvertisementReadingsThisRun':1,'QAOnlySourceRenders':7,'QAImages':8,'QACrops':1,'firstPassChapterSpans':5},
 'additionalTOCAuditReadings':[{'pdfPage':14,'image':'../liuyao-hidden-spirits/images/zengshan-14.png',
 'sha256':sha(root/'research/liuyao-hidden-spirits/images/zengshan-14.png'),'scope':'expanded-TOC-volume-division-audit','newSourcePage':False}],
 'directEnd':{'pdfPage':138,'reading':'增刪卜易卷二終'},'newHTTPBodies':0,'newOriginalPDFs':0,'allSourceClausesApplied':False,
 'sourceInstructionsAreData':True,'historicalOutcomesValidated':False,'wholeBookApplied':False})
write('CHAPTER_SPANS.json',{'date':'2026-10-27','sourceID':'B02','units':[{'id':f'B02-ch{i:03}','normalizedHeading':h,
 'pdfPages':list(range(a,b+1)),'bodyTextualVolumeAsPrinted':2,'firstPassCompleteSpanRead':True,'entireUnitApplied':False,
 'printedHeadingAsRead':'兩現章第三十一'if i==32 else h+'章第'+{29:'二十九',30:'三十',31:'三十一',33:'三十三'}[i]}
 for i,h,a,b in units],'numberingConflict':{'canonicalUnitID':'B02-ch032','TOCNumber':32,'bodyPrintedNumberAsRead':31,
 'bodyPDFPage':134,'QAActuallyViewed':True,'silentlyRenumbered':False},
 'volumeMappingCorrection':{'unit':'B02-ch033','earlierLocalTOCMapVolume':3,'correctedTOCVolume':2,'bodyVolumeAsPrinted':2,
 'evidencePDFPages':[14,136,138],'status':'local-map-corrected-after-TOC-and-body-audit-not-a-source-volume-conflict'},
 'allClausesApplied':False})
d=read(root/'research/liuyao-void-motion/B02_CURRENT_UNITS.json')
for i,h,a,b in units:
 r=next(x for x in d['units']if x['id']==f'B02-ch{i:03}');r.update(bodyPDFPages=list(range(a,b+1)),
 disposition='first-pass-complete-span-read-partial-private-application',latestEvidence='../liuyao-progress-conditions/MANUAL_READINGS.json',bodyTextualVolumeAsPrinted=2,tocVolume=2)
 if i==32:r.update(bodyPrintedHeadingAsRead='兩現章第三十一',headingVariantNote='TOC unit32 retained;body134 prints31. QA confirms duplicate numbering,not a new unit.')
d['priorTOCFile']='../liuyao-void-motion/B02_CURRENT_UNITS.json';d['priorTOCSHA256']=sha(root/'research/liuyao-void-motion/B02_CURRENT_UNITS.json')
d['currentCounts'].update(headingOnlyBodyUnits=98,firstPassCompleteSpanUnits=31)
d['latestScope']='Five complete first-pass source spans29..33;source clauses only partially compiled. Current source map136/98heading-only/31firstpass/7partialfoundations/0fullunits.'
write('B02_CURRENT_UNITS.json',d)
verse={s:list(b)for ss,b in [('甲戊','丑未'),('乙己','子申'),('丙丁','亥酉'),('壬癸','卯巳'),('庚辛','午寅')]for s in ss}
write('STAR_COORDINATES.json',{'date':'2026-10-27','sourceID':'B02-ch033','pdfPages':[136,137],
 'nobleman':{'verseRows':verse,'proseExampleGeng':list('丑未'),'gengStatus':'within-page-conflict-not-resolved',
 'verseReading':'庚辛逢馬虎','proseExampleBoundedReading':'假令甲□庚日…見丑未者即是貴人',
 'middleGlyphInExample':'戊/戌 shape unresolved;not used as a new day coordinate','fullNoblemanTableUnambiguouslyEstablished':False},
 'salary':{'explicitRows':{'甲':'寅','乙':'卯','丙':'巳','己':'午','庚':'申','辛':'酉'},'notExplicitInTheseSixStemLines':list('丁戊壬癸'),
 'missingFourRowsFilledFromRuntime':False},
 'horse':{'groups':[{'dayBranches':list(g),'target':b}for g,b in [('申子辰','寅'),('巳酉丑','亥'),('寅午戌','申'),('亥卯未','巳')]]},
 'joy':{'explicitSeasonRows':dict(zip('春夏秋冬','戌丑辰未')),'modernCalendarSeasonAdapterEstablished':False},
 'sourceChapterCaution':'Stars can assist the useful line;the source explicitly denies their independent control of outcomes. Quoted polemical/medical claims are not validated facts.',
 'sourceInstructionsAreData':True,'consumerApplied':False,'wholeChapterApplied':False})
write('PRINTED_FIXTURES.json',{'date':'2026-10-27','sourceID':'B02-ch029-033','sourceDatesConvertedToGregorian':False,
 'historicalOutcomesValidated':False,'fixtures':[
 {'id':'b02-progress-exam','page':117,'sourceHeading':'申月癸卯日占鄉試得恒變大過','values':[8,7,7,7,6,8],
 'primary':32,'changed':28,'movingLines':[5],'selectedChanges':[{'line':5,'primaryBranch':'申','changedBranch':'酉'}],
 'additionalSourceDarkMotionNotConvertedToCastMark':{'line':3,'reason':'source discusses卯日沖酉 as暗動;not another printed6/9 castmark'}},
 {'id':'b02-single-motion-rain','page':131,'sourceHeading':'午月甲申日防漲水沖去麥子占何日晴',
 'values':[7,8,7,7,7,9],'primary':13,'changed':49,'movingLines':[6],'selectedChanges':[],
 'sourcePrimaryTopBranch':'戌','sourcePrimaryTopKin':'子孫','figureNumbersEditorialFromReadDiagramNotPrintedNames':True,'sourceOutcomeValidated':False}
 ]})
clauses=[]
for c in old['directEightModeListAt123']:clauses.append({'id':c['id'],'pdfPages':[123],'sourceLayer':'printed-list-野鶴曰','boundedReading':c['reading'],
 'compiled':'three-valued-explicit-premise-clause-match-only','sourcePriorityInvented':False,'consumerApplied':False})
more=[('later-day-month',[123,124],'later-commentary-李我平日','臨日月與化空破不可機械否定進退；保留原爻及後續旺衰，不給覆蓋次序。'),
 ('tomb-distinct-types',[124,125,126,127],'chapter30','日墓/動墓/化墓及世/身/命、用神條件分開；此處不編成醫療或生死裁決。'),
 ('tomb-strength',[127,128,129,130],'chapter30-and-later-critique','旺相與休囚空破、沖墓以及所問不同，不能僅見墓位即定吉凶。'),
 ('visible-motion',[130],'chapter31-definition','一爻明動為獨發，五爻明動一爻靜為獨靜；暗動另需日辰條件。'),
 ('quoted-use-dispute',[130,133,134],'chapter31-quotation-and-critique','易冒所述重動輕用與後文仍須看用神並列；不把引文當成本書無條件捨用神指令。'),
 ('multiple-old-priority',[134],'chapter32-quoted-old-method','舍休囚用旺相/舍靜用動/舍破用不破/舍空用不空/舍傷用不傷是所引古法。'),
 ('multiple-counterexamples',[134,135,136],'chapter32-source-examples','後文有取空破之用、兩現之外實際三現及同一人再占的例；尚無自動唯一排序。'),
 ('noble-conflict',[136],'chapter33-verse-and-prose','庚的歌訣午寅與同頁例丑未分開保留；不暗改一層來求一致。'),
 ('salary-partial',[136],'chapter33-six-stem-lines','只見甲乙丙己庚辛六干祿位；丁戊壬癸不由其他表補入來源欄。'),
 ('horse-joy',[137],'chapter33-coordinate-verses','驛馬以明示日支組，天喜以明示季節；不自選曆法年/月界。'),
 ('stars-no-verdict',[137,138],'chapter33-source-caution','貴祿馬喜可輔用，不能獨操禍福；後文批評星煞之說仍是來源立場，非實際病死證據。')]
clauses.extend({'id':i,'pdfPages':p,'sourceLayer':l,'boundedReading':t,'consumerApplied':False,'historicalOutcomesValidated':False}for i,p,l,t in more)
write('OPERATIONAL_CLAUSES.json',{'date':'2026-10-27','sourceID':'B02-ch029-033','clauses':clauses,
 '有一InclusiveReadingIsEditorial':True,'eightModesAreNotExclusiveCategories':True,'laterCritiqueNotMadeAutomaticOverride':True,
 'sourceInstructionsAreData':True,'allChapterClausesCompiled':False})
write('SOURCE_AUDIT.json',{'date':'2026-10-27','sourceID':'B02','sourcePDFBytes':11089308,'sourcePDFPages':394,
 'sourceSHA256':old['sourceSHA256'],'newHTTPBodies':0,'newOriginalPDFs':0,'existingRawBytesReused':True,
 'sameEditionNotIndependentWitness':True,'fiveCompleteFirstPassSpansNotWholeChapterApplication':True,
 'noblemanWithinPageConflictAt136':True,'salaryFourStemRowsNotExplicitAt136':True,'bodyNumberDuplicateAt134':True,
 'bodyVolume2EndAt138':True,'chapter33EarlierLocalVolumeMapCorrectedFrom3To2':True,'TOC14AndBodyVolume2Agree':True,'prefaceDateDoesNotProvePrintDate':True,
 'unreleasedDraftCorrection':'QA131 removed an invented 得剝卦 suffix/incorrect draft values;source has no named-figure title in this paragraph. Actual diagram/top戌子孫/sole6thmoving mark gives13.6→49. This was never released.',
 'wholeBookApplied':False,'wholeCatalogueCompleted':False})
print(json.dumps({'manualRecords':24,'firstPassChapters':5,'boundedClauses':len(clauses),'B02Counts':d['currentCounts']},ensure_ascii=False))
