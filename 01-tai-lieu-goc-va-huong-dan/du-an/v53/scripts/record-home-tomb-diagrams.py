from pathlib import Path
from hashlib import sha256
import json,shutil

r=Path(__file__).resolve().parent.parent;w=r.parent;b=r/'research/home-tomb-diagrams';q=r/'qa/home-tomb-diagrams';s=w/'tmp/home-tomb-diagrams-staging'
assert not b.exists()and not q.exists(),'One-shot source record'
b.mkdir();q.mkdir()
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
write=lambda p,d:p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
sha=lambda p:sha256(p.read_bytes()).hexdigest()
for p in s.iterdir():
 if p.is_file():shutil.copyfile(p,b/p.name)
groups=[{'id':'water-earth','sourceGroupName':'水土山','mountains':list('甲寅辰巽戌坎辛申丑癸坤庚未'),'count':13,'movementElements':list('木金水火土'),'readOrientation':'p041-native; p049-r90'},
 {'id':'fire','sourceGroupName':'火山','mountains':list('離壬丙乙'),'count':4,'movementElements':list('火土木金水'),'readOrientation':'p041-r180; p049-r270'},
 {'id':'wood','sourceGroupName':'木山','mountains':list('震艮巳'),'count':3,'movementElements':list('土木金水火'),'readOrientation':'p041-r90; p049-r180'},
 {'id':'metal','sourceGroupName':'金山','mountains':list('乾亥兌丁'),'count':4,'movementElements':list('金水火土木'),'readOrientation':'p041-r270; p049-native'}]
stemGroups=['甲己','乙庚','丙辛','丁壬','戊癸']
yearLists={
 'water-earth':[['甲子','甲午'],['乙巳','乙亥'],['丙辰','丙戌','辛丑','辛未'],['丁丑','丁未','壬辰','壬戌'],['戊辰','戊戌','癸丑','癸未']],
 'fire':[['甲寅','甲申'],['庚寅','庚申'],['辛巳','辛亥'],['丁卯','丁酉'],['戊寅','戊申']],
 'wood':[['己巳','己亥'],['乙丑','乙未','庚辰','庚戌'],['丙寅','丙申'],['丁巳','丁亥'],['癸巳','癸亥']],
 'metal':[['甲辰','甲戌','己丑','己未'],['庚子','庚午'],['丙子','丙午'],['壬子','壬午'],['癸卯','癸酉']]}
monthSets={'water-earth':[[7,8],[11,12],None,[5,6],[7,8]],'fire':[[11,12],[5,6],[5,6],[3,4],[3,4]],'wood':[[3,4],[3,4],[7,8],[7,8],[1,2,9,10]],'metal':[[1,2,9,10],[1,2,9,10],[3,4],[11,12],[11,12]]}
rows=[]
for g in groups:
 for i,stems in enumerate(stemGroups):
  months=monthSets[g['id']][i]
  rows.append({'id':g['id']+'-'+stems,'mountainGroup':g['id'],'sourceYearStems':stems,'sourceMovementElement41':g['movementElements'][i],
   'sourceYearPillars49':yearLists[g['id']][i],'sourceMonthOrdinals49':months,'monthReadingResolved':months is not None,
   'monthReadingAlternatives':[[12],[11,12]]if months is None else[],
   'monthReadingCaveat':'Native water-earth/丙辛 outerlabel appears十二月尅 or compressed十一二月尅; preserve ambiguity. Prior formula is not used to restore an unread stroke.'if months is None else None,
   'monthNotationPolicy':'正二/三四/五六/七八/九十 are paired ordinals;十一二/一二within11/12context normalized explicitly. Named source month coordinates, not an astronomical instant.'})
# The first reading of the small month numeral remains explicitly unresolved.
write(b/'DIAGRAM_TABLES.json',{'date':'2026-10-28','sourceInstructionsAreData':True,'sourceImages':[41,49],'sourceYearGroups':stemGroups,'groups':groups,'rows':rows,
 'directMovementCoordinates41':20,'directYearPillarEntries49':sum(len(x['sourceYearPillars49'])for x in rows),'directResolvedMonthSets49':19,'unresolvedMonthSets49':1,
 'allSourceImageCharactersDiplomaticallyTranscribed':False,'calendarAdapterEstablished':False,'wholeUnitsApplied':False,'outcomesValidated':False})
extra=[]
for n in[50,51,52]:
 p=r/f'research/home-you-nian/images/p{n:03}.png';extra.append({'page':n,'file':p.relative_to(w).as_posix(),'sha256':sha(p),'expandedTargetedRead':True})
write(b/'SOURCE_MANIFEST.json',{'date':'2026-10-28','sourceContainer':'v53/research/full-study/home/CADAL06056503.djvu','sourceSHA256':'bfd3b76c55d62324919ab161c8c2ba2ecb129b3b2c59a3ab0428807e8f8278db',
 'nativeDiagramPages':read(b/'CROPS.json')['records'],'additionalProsePages':extra,'expandedPreviouslyReadPages':5,'newHTTPRequests':0,'newOriginalContainers':0,'newSourcePages':0,
 'QADerivatives':{'nativeCrops':2,'losslessRotations':6,'nativeSectorCrops':8,'nativeDetailCrops':2},
 'directVisualQADerivativesViewed':18,'derivativeCountDoesNotMeanSourcePageCount':True,'ordinaryPublicHomeGeometryChanged':False})
write(b/'MANUAL_READINGS.json',{'date':'2026-10-28','sourceInstructionsAreData':True,
 'readings':[{'page':41,'scope':'Two rings:fourmountaingroups/24labelsand20yeargroup-movementassignments;allfourorientationsandlowersectorsviewed.','disposition':'Comparewithpreviousprose25rows;ordinaryringonly,nosolsticechangeexplicitinthefigure.'},
 {'page':49,'scope':'Fourmountaingroups,20yeargroupcolumns/50yearpillars,19resolvedmonthsets/1unresolvednumeralrange;allfourorientationsandlowersectorsviewed.','disposition':'Sourcecoordinatequeryonly;do notconvertmonthlabelsintoGregorian/lunar dateswithoutdeclaredadapter.'},
 {'page':50,'scope':'Conditionsnewbuilding/newgrave/repairfoundationunchanged/existinggrave and甲子example;sourcecalendarcoordinates.','disposition':'Existingboundedapplicabilityreferenceunchanged;notphysicalriskprediction.'},
 {'page':51,'scope':'MonthNaYinexamplesandwinter-solsticeexceptionformetal;readwithpage52.','disposition':'49ordinarydiagramcannotresolveafter-solsticewithoutprosecontext;do notoverwrite5exceptionrows.'},
 {'page':52,'scope':'Year/month/day/hour sourcefiveZi/墓coordinatecomparisonconclusion.','disposition':'Sourceanalogyandday/hourstatementnotcompleteastronomicaldateadapter.'}],
 'scopeWarnings':['Directmanualyearlistsrecordedbeforeactualruntimecomparison;sourcegrouppairordercanonicalized,butnotallprintedwordorderdiplomaticallytranscribed.',
 'A candidateyearnotlistedmeansnot-listed-in-this-diagram;notanassuranceofsafeconstruction.',
 'Monthambiguitywater-earth/丙辛keptopen;derivedexpectedmonthsareseparatecomparison,notemendation.',
 'Diagram41small丁壬年columninterleavesadjacent火運label;do notmisreadthe壬glyphas土orclaimsourcecontradictionfromlayout.'],
 'wholeSourceUnitsApplied':False,'practicalOutcomesValidated':False})
print('Recorded20movementrows/50yearentries/19resolvedmonthsets+1unresolved;5expandedsourcepages,noHTTP.')
