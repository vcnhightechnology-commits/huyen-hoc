from pathlib import Path
from hashlib import sha256
import json,shutil

r=Path(__file__).resolve().parent.parent;w=r.parent;b=r/'research/liuyao-life-context';q=r/'qa/liuyao-life-context';s=w/'tmp/liuyao-b02-life-staging'
assert not b.exists()and not q.exists(),'One-shot source promotion'
b.mkdir();(b/'images').mkdir();q.mkdir()
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
write=lambda p,d:p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
sha=lambda p:sha256(p.read_bytes()).hexdigest()
manual=read(s/'MANUAL_READINGS.json')
assert sha(w/manual['sourcePDF'])==manual['sourceSHA256']
for x in manual['records']:
 p=w/x['file'];assert sha(p)==x['sha256']
 if x['pdfPage']>=221:
  dest=b/'images'/p.name;shutil.copyfile(p,dest);x['file']=dest.relative_to(w).as_posix()
manual['oldSourceHashesReadMoreClosely']=[213,214,215,229];manual['sourceReadingStatusSupersedes']='v53/research/liuyao-weather/MANUAL_READINGS.json for214–220;oldfilepreservedaschronologicalrecord'
write(b/'MANUAL_READINGS.json',manual)
methods=[{'id':'B02-ch037-lifelong-wealth-structure','sourcePages':[214,215],'sourceVoice':'覺子 and chapter37 source, targeted structural roles only',
 'groups':[{'id':'wealth','kin':'妻財','sourceTerm':'財'},{'id':'blessing','kin':'子孫','sourceTerm':'福/子孫'}],
 'sourceReading':'世爻財爻子孫爻三者','groupingBasis':'Three explicit source actors:世,財,子孫. Whether旺相/無氣/失陷 applies is not inferred from presence.'},
 {'id':'B02-ch038-lifelong-career-structure','sourcePages':[229],'sourceVoice':'chapter38 opening, targeted structural roles only',
 'groups':[{'id':'office','kin':'官鬼','sourceTerm':'官'},{'id':'writing','kin':'父母','sourceTerm':'父'}],
 'sourceReading':'官父興隆文章見用','groupingBasis':'Parallel source role groups, not a claim that parent always generates官 or an automatically selected用神.'}]
write(b/'SOURCE_CONTEXTS.json',{'date':'2026-10-27','sourceInstructionsAreData':True,'methods':methods,
 'separateQuestionSource':{'sourcePages':[213,214],'focusCategories':['parents','siblings','wealth','career','marriage','children','longevity'],
 'sourceLimit':'Author critiques treatingonecastasalloflife;source ends及壽元俱宜分占. Categories not automatically derivedfromusertext,not permissiontoautocast.'},
 'structuralElementEdges':'Ordinary five-element生成/克 relations from retained foundations. Edges are derived, not source prose quotations, activity priorities or effective causal effects.',
 'wholeConditionalRulesCompiled':False,'practicalOutcomesValidated':False})
clauses=[
 ('one-cast-limit',[213,214],'覺子','Onecastdoesnotsettleparents/siblings/spouse/children/career/wealth/longevity;source advocatesseparatequestions.','scope-guard-only'),
 ('conflicting-kin-effects',[213],'author','Differentkinrolescanconstrainoneanother;sourcewarnsblanketbenefitforoneactorisnotbenefitforall.','conditional-open'),
 ('three-actors',[214],'覺子','Wealthfocususes世/財/子孫asdistinctactors. Source無一失陷/旺相requiresseparatepremises.','private-structural-groups'),
 ('source-of-wealth',[214],'source','子孫iscalled財之源;structuralgenerationedgesdonotestablisheffectivewealthoroutcome.','private-structural-edge'),
 ('wealth-vs-blessing',[214,215],'multiplevoices','財旺福空/福旺財衰/世旺 orunsupported canyielddifferentclaims;thresholdsandprioritynotcomplete.','conditional-open'),
 ('static-void-vs-active',[216],'覺子vsoldcommentary','世空 lifetimefailureclaimqualifiedbyvisiblemotion/dayclash/support;absenceofcalendarpremisesstaysunknown.','conditional-open'),
 ('grave-qualified',[217],'覺子vsoldcommentary','Self墓withsupport/wealth-blessinggenerationnotuniformlife-failure;墓needstargetednamedpremises.','conditional-open'),
 ('six-combinations',[218,219],'野鶴/覺子vs舊註','六合/六沖notautomaticfixeddecadesoffortune;sourcecounterexamplesdemand用神andcontext.','conditional-open'),
 ('unasked-meaning',[219,222],'sourceand覺子','Sourceanecdotesreassignquestiontounaskedcareer/familyharm;notpermissiontoinferprivateuserintent.','historical-narrative-not-runtime-rule'),
 ('parents-self',[220,225,226],'multiplevoices','父持世interpretedhardshipinwealthcontextbutliterature/workincareer;sourcecontextmatters.','context-separation'),
 ('wealth-not-actual-spouse',[226],'覺子','財roleinwealthquestiondoesnotautomaticallymeanspouse;do notturn克relationshipintomaritalclaims.','scope-guard-only'),
 ('profession-stereotypes',[221,223,227],'source','Six-spirit/social/profession/sex/healthnarrativeshistorical,notclassificationofrealpeople.','historical-claim'),
 ('return-control',[228],'source','六合doesnotnegatereturncontrol/changedghost/daymonthcontrol;efficacyrequiresmorepremises.','structural-fact-only'),
 ('office-writing',[229],'chapter38','官/父parallelrolefocus;sourceuses官動生世/父旺動生世withqualification.','private-structural-groups'),
 ('asset-office',[229],'source','財生官claimdependsactualgenerationandsupportedactors;notallwealthpresenceimpliesrank.','conditional-open'),
 ('supported-self',[230],'source','官/self/daymonthgenerationconditionscompared;notamodernadmission/careerprobability.','conditional-open'),
 ('children-career',[231,232],'source','Sourcechild持世careerexamplesarenotuniformprediction;question/positionandotheractorsstillrelevant.','conditional-open'),
 ('longevity-opening',[232],'source','壽元chapter39onlyopeningread;medical/death/lifespanclaimsnotvalidatedorimplemented.','historical-only'),
 ('blanket-cast-warning',[222,223,224],'multiplevoices','Retrospectivecasesarenotindependentvalidation;onecastcannotbecreditedforarbitraryunaskedoutcomes.','scope-limit'),
 ('source-glyph-open',[226],'sourceimage','Printedhexheadlooks允/兌;noemendationorfixtureuntiltargetedvisualcollation.','glyph-open')]
write(b/'BOUNDED_CLAUSES.json',{'date':'2026-10-27','clauses':[{'id':i,'sourcePages':p,'sourceVoice':v,'disposition':d,'status':status,'outcomeValidated':False}for i,p,v,d,status in clauses],
 'sourceInstructionsAreData':True,'allSubsidiaryClausesEnumerated':False,'wholeChaptersApplied':False})
fixture={'id':'B02-215-Fu-to-Yi','sourcePDFPage':215,'primaryHan':'復','changedHan':'頤','primary':24,'changed':27,
 'valuesBottomToTop':[7,8,8,8,8,6],'movingLine':6,'sourceBaseLabelsBottomToTop':[{'branch':'子','kin':'妻財'},{'branch':'寅','kin':'官鬼'},{'branch':'辰','kin':'兄弟'},{'branch':'丑','kin':'兄弟'},{'branch':'亥','kin':'妻財'},{'branch':'酉','kin':'子孫'}],
 'changedBranch':'寅','sourceProse':'獨嫌酉金福神破而化絕','sourceClaimNotAutomaticallyDerived':'破/絕 cannot be asserted from six role labels alone; calendar and source phase premises left open.',
 'numericEncoding':'Software6/7/8/9derivedexplicitlyfromsourcefigurelabels/headerandtopmotion;notahistoricalGregorianbirthdate.',
 'sourceOutcomeValidated':False,'calendarDateBound':False}
write(b/'PRINTED_FIXTURES.json',{'date':'2026-10-27','fixtures':[fixture],'fullOutcomeAlgorithm':False})
units=read(r/'research/liuyao-weather/B02_CURRENT_UNITS.json');units['priorTOCFile']='../liuyao-weather/B02_CURRENT_UNITS.json';units['priorTOCSHA256']=sha(r/'research/liuyao-weather/B02_CURRENT_UNITS.json')
spans={36:list(range(213,215)),37:list(range(214,230)),38:list(range(229,233)),39:[232]}
for u in units['units']:
 for num,pages in spans.items():
  if u['id']==f'B02-ch{num:03}':u.update(bodyPDFPages=pages,bodyTextualVolumeAsPrinted=4,disposition='first-pass-complete-span-read-partial-private-application'if num<39 else'partial-body-reading-application-open',latestEvidence='../liuyao-life-context/MANUAL_READINGS.json')
units['currentCounts'].update(headingOnlyBodyUnits=92,firstPassCompleteSpanUnits=36,otherPartialUnits=1)
units['latestScope']='36firstspan213–214,37firstspan214–229,38firstspan229–232;39onlyopening232.136registered/92headingonly/36firstspan/7foundationpartial/1otherpartial/0whole.'
write(b/'B02_CURRENT_UNITS.json',units)
write(b/'SOURCE_MANIFEST.json',{'date':'2026-10-27','sourcePDF':manual['sourcePDF'],'sourceSHA256':manual['sourceSHA256'],'sourceBytes':11089308,
 'images':manual['records'],'newReadPositions':19,'expandedPriorReadPositions':[213],'targetedExpandedReadPositions':[213,214,215,229],
 'newlyRenderedPositions':12,'previousRenderedNowReadPositions':7,'newHTTPRequests':0,'newOriginalContainers':0,
 'chapterSpans':{str(k):v for k,v in spans.items()},'wholeChaptersApplied':False,'wholeCatalogueCompleted':False})
print('Promoted20positions/3wholefirstspans,20boundedclauses,2structuralcontexts and1independentprintedfixture.')
