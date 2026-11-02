from pathlib import Path
from hashlib import sha256
import json,shutil

r=Path(__file__).resolve().parent.parent;w=r.parent;b=r/'research/liuyao-weather';q=r/'qa/liuyao-weather';s=w/'tmp/liuyao-b02-weather-staging'
assert not b.exists()and not q.exists(),'One-shot source promotion'
b.mkdir();q.mkdir();(b/'images').mkdir()
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
write=lambda p,d:p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
sha=lambda p:sha256(p.read_bytes()).hexdigest()
staged=read(s/'MANUAL_READINGS.json')
assert sha(w/staged['sourcePDF'])==staged['sourceSHA256']
for x in staged['records']:
 assert sha(s/x['file'])==x['sha256'];shutil.copyfile(s/x['file'],b/'images'/x['file']);x['file']='images/'+x['file']
x=staged['highResolutionQA'];assert sha(s/x['file'])==x['sha256'];shutil.copyfile(s/x['file'],b/x['file'])
staged['previousStagingRecord']='tmp/liuyao-b02-weather-staging/MANUAL_READINGS.json'
write(b/'MANUAL_READINGS.json',staged)
prefix=[]
for n in[188,189,190]:
 p=r/f'research/liuyao-b02-jinqian/images/zengshan-{n}.png';prefix.append({'page':n,'file':p.relative_to(w).as_posix(),'sha256':sha(p),'expandedRead':True})
write(b/'SOURCE_MANIFEST.json',{'date':'2026-10-27','sourcePDF':staged['sourcePDF'],'sourceBytes':staged['sourceBytes'],'sourceSHA256':staged['sourceSHA256'],
 'expandedPriorPages':prefix,'newlyReadWeatherPages':list(range(191,212)),'newParatextPage':212,'newNextChapterOpeningPage':213,
 'actuallyViewedSourcePositions':23,'renderedButNotReadPages':list(range(214,221)),'newHTTPRequests':0,'newOriginalContainers':0,
 'sourcePDFByteChanges':0,'fullWeatherRange':[188,211],'allWeatherClausesApplied':False})
methods=[{'id':'B02-ch035-JueZi-191','sourceVoice':'覺子曰','sourcePages':[191],'selectors':[{'question':'rain','desiredKin':['父母']},{'question':'clear','desiredKin':['子孫']}],
 'sourceReading':'占雨用父爻占晴用子孫爻財爻與世應何干','qualification':'Source criticizes using財/世應 as universal premises. Keep this voice separate from the quoted verse.'},
 {'id':'B02-ch035-quoted-summary-201','sourceVoice':'quoted/summary passage; not silently attributed to覺子191','sourcePages':[201],
 'selectors':[{'question':'rain','desiredKin':['父母']},{'question':'clear','desiredKin':['子孫','妻財']},{'question':'cloud-thunder','desiredKin':['官鬼']}],
 'sourceReading':'父母主雨官鬼主濃雲雷電子孫財爻主晴','qualification':'Historical symbolic role assignment only; no claim these roles forecast weather.'}]
write(b/'QUESTION_ROLES.json',{'date':'2026-10-27','sourceInstructionsAreData':True,'methods':methods,'automaticQuestionParsing':False,'wholeChapterApplied':False,'practicalWeatherModelEstablished':False})
clauses=[
 ('geographic-question-scope',[189],'unnamedauthor','Question should identify location and desiredrain/clear/snow/frost; source broadvsnarrow semantics not interchangeable.','explicit-scope-only'),
 ('wealth-not-alone',[188,190],'authorand覺子','Wealthmotion alone doesnot imply all-daysun:childinactive/hiddennot qualified;source sayswealthis元神 forchild.','conditional-open'),
 ('rain-parent-clear-child',[191],'覺子','Selectparentsforrainandchildrenforclear;wealthand世應 rejectedasuniversalweatherpremises.','private-selector'),
 ('nothing-moving',[191],'覺子','Source advocatesanothercastwhenstatic;historicalpracticeadvice,notpermissiontoautocast/reinterpretuserrequest.','historical-practice'),
 ('strength-disagreement',[192,193,196,197],'覺子vsoldcommentary/野鶴','Voices disagreeaboutseasonalelementstrengthandwhether旺衰shouldcontrolweatherreading.','conflicting-premises-open'),
 ('snow-frost',[192,193],'覺子vs舊註','Blanketchild→snow/frost challenged;season/light/fog/wind distinctions unresolved.','historical-claim-not-forecast'),
 ('ghost-not-always-thunder',[190,194,195,200],'multiplevoices','Ghostmayinterpretedascloud/fog/thunderbycontext;presenceormotionalonecannotclassifyobservedweather.','conditional-open'),
 ('shared-combinations',[194],'oldcommentaryandcountercommentary','財/父/鬼三合 descriptions areconditional,not a newcompletecombination-strengthmethod.','conditional-open'),
 ('motion-order',[195,206,207],'multiplevoices','Parent/brother/child/wealthcoactivity canreferdifferentdays/hours;do notcollapseonepatternintooneeventtime.','conditional-open'),
 ('parent-month',[196,197],'野鶴vsoldcommentary','Parentmonthlystrength doesnotunconditionallymeanpersistentall-dayrain;sourceexamplesandrebuttalretained.','conflicting-premises-open'),
 ('retreat',[198,199],'sourceexamples','Motion/changetoretreatinterpretedrainstopping butpriority/availability/timingpremises notcompiled.','structural-fact-only'),
 ('question-relative-summary',[201],'quotedsummary','Rainparent/clearwealth-or-child/cloudthunderghost;keepapartfromJueZi191.','private-selector'),
 ('void-fullness',[199,201,202],'multiplevoices','Void/static/darkmotion/monthbreak fill/clash timingrequirescalendar/usefulnesspremises;donotderivepracticaldate.','conditional-open'),
 ('repeat-cast',[202,207,208,209,210],'author','Repeatcasts andreportedoutcomes keptasdistincthistoricalcasts;notindependentlyvalidatedweatherobservations.','historical-claim-not-forecast'),
 ('weather-vs-human-affairs',[209],'author','Usingweatherasananalogyforhumanfortuneisthesourceargument,notestablishedequivalenceoroutcomeproof.','historical-argument'),
 ('closing-flexibility',[211],'author','Source closeswithflexibility ratherthanfixeduniversalverdict;noarbitrarypriorityinvented.','scope-limit')]
write(b/'BOUNDED_CLAUSES.json',{'date':'2026-10-27','sourceInstructionsAreData':True,'clauses':[{'id':i,'sourcePages':p,'sourceVoice':v,'disposition':d,'status':status,'outcomeValidated':False}for i,p,v,d,status in clauses],
 'allClausesEnumerated':False,'allSourceImageCharactersCollated':False,'wholeChapterApplied':False})
fixture={'id':'B02-191-Heng-to-DaGuo','sourcePDFPage':191,'qaImage':'qa360-191.png','primaryHan':'恒','changedHan':'大過','primary':32,'changed':28,
 'valuesBottomToTop':[8,7,7,7,6,8],'movingLine':5,
 'sourceBaseLabelsBottomToTop':[{'branch':'丑','kin':'妻財'},{'branch':'亥','kin':'父母'},{'branch':'酉','kin':'官鬼'},{'branch':'午','kin':'子孫'},{'branch':'申','kin':'官鬼'},{'branch':'戌','kin':'妻財'}],
 'sourceMovingProse':'申鬼明動化進神','sourceShiProse':'世爻酉鬼暗動','expectedChangedBranch':'酉',
 'movingPositionBasis':'Unique申鬼 atline5 inprintedbranchlist plus source申鬼明動 and恒→大過. Numeric6/7/8/9encoding derivedexplicitly;notallprintedlineglyphsalignmentcollated.',
 'calendarDateBound':False,'historicalWeatherOutcomeValidated':False}
write(b/'PRINTED_FIXTURES.json',{'date':'2026-10-27','fixtures':[fixture],'dateOrRealWeatherAdapterEstablished':False})
units=read(r/'research/liuyao-b02-jinqian/B02_CURRENT_UNITS.json');units['priorTOCFile']='../liuyao-b02-jinqian/B02_CURRENT_UNITS.json';units['priorTOCSHA256']=sha(r/'research/liuyao-b02-jinqian/B02_CURRENT_UNITS.json')
for x in units['units']:
 if x['id']=='B02-ch035':x.update(bodyPDFPages=list(range(188,212)),disposition='first-pass-complete-span-read-partial-private-application',bodyTextualVolumeAsPrinted=3,latestEvidence='../liuyao-weather/MANUAL_READINGS.json',volumeVariantNote='TOC15places35under卷四;body188–211卷三/end212;卷四actuallyopens213. PreserveTOC/bodydifference.')
 if x['id']=='B02-ch036':x.update(bodyPDFPages=[213],disposition='partial-body-reading-application-open',bodyTextualVolumeAsPrinted=4,latestEvidence='../liuyao-weather/MANUAL_READINGS.json')
units['currentCounts'].update(headingOnlyBodyUnits=95,firstPassCompleteSpanUnits=33,otherPartialUnits=1)
units['latestScope']='Chapter35firstpass188–211/bodyvol3/end212;chapter36opens213vol4,onlyfirstpageread.136registered/95headingonly/33firstpass/7foundationpartial/1otherpartial/0whole.'
write(b/'B02_CURRENT_UNITS.json',units)
write(b/'SOURCE_BOUNDARIES.json',{'chapter35':{'pages':[188,211],'tocVolume':4,'bodyVolume':3,'wholeFirstPass':True,'wholeApplied':False},'volume3EndingPage':212,'volume4OpeningPage':213,'chapter36OpeningPage':213,'renderedNotRead':list(range(214,221)),'TOCEmended':False})
print('Recorded source35whole-span reading,16boundedclauses,5namedrole selectors and1printedcase;noforecast.')
