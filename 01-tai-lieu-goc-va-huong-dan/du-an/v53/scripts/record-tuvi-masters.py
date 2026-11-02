from pathlib import Path
from hashlib import sha256
import json,shutil,tarfile
from PIL import Image

r=Path(__file__).resolve().parent.parent;w=r.parent;b=r/'research/tuvi-masters';q=r/'qa/tuvi-masters';s=w/'tmp/tuvi-masters-staging'
assert not b.exists()and not q.exists(),'One-shot source record'
b.mkdir();q.mkdir()
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
write=lambda p,o:p.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
sha=lambda p:sha256(p.read_bytes()).hexdigest()
for name in['CROPS.json','soul80-native.png','body81-native.png']:shutil.copyfile(s/name,b/name)
for x in read(b/'CROPS.json')['records']:
 assert sha(w/x['source'])==x['sourceSHA256']and sha(b/x['crop'])==x['cropSHA256']
 assert Image.open(w/x['source']).convert('RGB').crop(x['box']).tobytes()==Image.open(b/x['crop']).convert('RGB').tobytes()
soulGroups=[(['子'],'貪狼','贪狼','Tham Lang'),(['亥','丑'],'巨門','巨门','Cự Môn'),(['寅','戌'],'祿存','禄存','Lộc Tồn'),(['卯','酉'],'文曲','文曲','Văn Khúc'),(['申','辰'],'廉貞','廉贞','Liêm Trinh'),(['未','巳'],'武曲','武曲','Vũ Khúc'),(['午'],'破軍','破军','Phá Quân')]
bodyGroups=[(['子','午'],'火鈴星',None,None),(['丑','未'],'天相星','天相','Thiên Tướng'),(['寅','申'],'天梁星','天梁','Thiên Lương'),(['卯','酉'],'天同星','天同','Thiên Đồng'),(['辰','戌'],'文昌星','文昌','Văn Xương'),(['巳','亥'],'天機主','天机','Thiên Cơ')]
rows=[]
for branches,literal,canonical,vi in soulGroups:
 for branch in branches:rows.append({'kind':'ming-master','branch':branch,'sourceNameLiteral':literal,'canonicalSimplifiedStar':canonical,'vietnameseStar':vi,'sourceSingleStarResolved':True,'sourceCanvas':80})
for branches,literal,canonical,vi in bodyGroups:
 for branch in branches:rows.append({'kind':'body-master','branch':branch,'sourceNameLiteral':literal,'canonicalSimplifiedStar':canonical,'vietnameseStar':vi,'sourceSingleStarResolved':canonical is not None,'sourceCanvas':81,
  'editorialParseCandidates':['火星','铃星']if canonical is None else[],
  'parseCaveat':'Literal火鈴星 may name a compound/class or alternatives; one star vs both is not established. Do not select from iztro to fill source.'if canonical is None else None})
write(b/'SOURCE_TABLES.json',{'date':'2026-10-27','sourceInstructionsAreData':True,'system':'NAJ4468520-canvas80-81-master-labels','rows':rows,
 'soulGroups':7,'soulCoordinates':12,'bodyGroups':6,'bodyCoordinates':12,'bodySingleStarCoordinates':10,'bodyUnresolvedCompoundCoordinates':2,
 'sourceBranchRoles':{'ming-master':'The example explicitly anchors午宮安命 and子宮安命; not automatically birthyear.',
 'body-master':'Source says子午人 etc under安身主. Birth-year branch is the compared modern iztro convention; this short source passage does not explicitly spell out本生年 or calendar boundary.'},
 'bodyBirthYearAnchorExplicitlyAttested':False,'ordinarySourceTableNotStarPlacement':True,
 'historicalOutcomeValidated':False,'wholeBookApplied':False})
write(b/'MANUAL_READINGS.json',{'date':'2026-10-27','locationPolicy':'One-based IIIF canvas ordinals, not printed folios or PDF pages. Native full spreads2200x1659; repository-server derivatives, not originalJP2.',
 'readings':[{'canvas':80,'region':'left spread lower安命主 plusexample throughnextcanvas81right','workingReading':'貪狼子宮 巨門亥丑二宮 祿存寅戌宮 文曲卯酉宮 廉貞申辰宮 武曲未巳宮 破軍午宮','example':'假如午宮安命尋破軍星在何宮即命主星也子宮安命 / 尋貪狼星即命主也','disposition':'12directnamecoordinates;explicit命宮anchor;candidate star location can be looked up on actual chart;no outcome.'},
 {'canvas':81,'region':'right spread 安身主','workingReading':'子午人火鈴星 丑未人天相星 寅申人天梁星 卯酉人天同星 辰戌人文昌星 巳亥人天機主','disposition':'10unambiguoussingle-starcoordinates;2literal火鈴星 coordinatesnotresolvedbychoosingmodernsoftware;bodycalendaranchor isseparate.'},
 {'canvas':80,'region':'left安童限訣 adjacent','workingReading':None,'disposition':'Newcontextobserved only:one-to-six agepalaceverse,余年glyph and十五大命 interpretationunresolved. Not evidence tochange currentmajorperiod start/age;needs ownwholepassage/witness.'},
 {'canvas':81,'region':'rightfirstcontinuation andfollowingleftsections','workingReading':'左輔隨丑至午 右弼隨亥至午','disposition':'Neighboringstatement relationship to命主 remainsuncompiled. 金鎖鐵蛇/竹羅三限/強弱宮/閒宮 sections onlylocalized, not allclausesapplied; no health/deathforecasts.'}],
 'normalization':'Working readings canonicalize巳 asbranch,traditional/simplified staraliasesexplicit;notallfacsimileglyphsdiplomaticallytranscribed.',
 'directNativeCropsViewed':2,'whole80And81Applied':False,'wholeCatalogueCompleted':False})
tgz=w/'v46/evidence/npm/iztro-2.6.2.tgz';assert sha(tgz)=='d44e96631c0506424c3aef25a7bba8e43e01729102d6a703720cbe224aec5403'
runtime=[]
with tarfile.open(tgz,'r:gz')as tar:
 for name in['lib/astro/astro.js','lib/data/earthlyBranches.js','lib/data/stars.js','package.json']:
  p=w/'v46/node_modules/iztro'/name;assert p.read_bytes()==tar.extractfile('package/'+name).read()
  runtime.append({'file':p.relative_to(w).as_posix(),'bytes':p.stat().st_size,'sha256':sha(p),'byteIdenticalToRetainedPackage':True})
request80=next(x for x in read(r/'research/fortune-followup/WITNESS_AUDIT.json')['officialImages']['pages']if x['sequenceNumber']==80)['request']
requests81=read(r/'research/fortune-table/REQUESTS.json')
requests81=requests81['records']if isinstance(requests81,dict)else requests81
request81=next(x for x in requests81 if x['file']=='official-081.jpg')
write(b/'SOURCE_MANIFEST.json',{'date':'2026-10-27','institution':'National ArchivesofJapan','catalogue':'https://www.digital.archives.go.jp/file/1078787','item':'https://www.digital.archives.go.jp/item/4468520',
 'images':[{'canvas':80,'file':'v53/research/fortune-followup/official-080.jpg','sha256':sha(r/'research/fortune-followup/official-080.jpg'),'retainedRequest':request80},
 {'canvas':81,'file':'v53/research/fortune-table/official-081.jpg','sha256':sha(r/'research/fortune-table/official-081.jpg'),'retainedRequest':request81}],
 'retainedManifest':'v53/research/fortune-followup/official-manifest.json','retainedManifestSHA256':sha(r/'research/fortune-followup/official-manifest.json'),
 'runtimeTarball':'v46/evidence/npm/iztro-2.6.2.tgz','runtimeTarballSHA256':sha(tgz),'runtime':runtime,
 'newHTTPRequests':0,'newOriginalContainers':0,'newSourcePages':0,'expandedPreviouslyReadPages':2,'nativeQACrops':2,
 'sourceTier':'Targeted readingofretainedinstitutionalimage-derivatives;noindependentneweditionororiginalJP2.',
 'publicWebsiteChanged':False,'sourceOutcomesValidated':False})
write(s/'WORK_STATE.json',{'date':'2026-10-27','status':'source-master-tables-recorded-runtime-verification-next','integratedSourceDirectory':'v53/research/tuvi-masters',
 'sourceCoordinates':24,'unresolvedBodyCompoundCoordinates':2,'consumerChanged':False,'wholeCatalogueCompleted':False})
print('Recorded12Ming-master/10singleBody-master/2unresolvedcompoundcoordinates;retainedsource/runtimebytesverified.')
