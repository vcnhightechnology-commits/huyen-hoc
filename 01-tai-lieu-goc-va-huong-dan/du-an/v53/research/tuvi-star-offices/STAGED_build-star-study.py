from pathlib import Path
from hashlib import sha256
from PIL import Image,ImageChops
import json
w=Path.cwd();b=w/'tmp/tuvi-full-volume-staging';read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));sha=lambda p:sha256(p.read_bytes()).hexdigest()
def write(n,x):(b/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
reqs=[]
for f in ['WINDOWS_TRUST_REQUESTS.json','WINDOWS_TRUST_REQUESTS_13_24.json','WINDOWS_TRUST_REQUESTS_25_30.json']:
 x=read(b/f)
 for z in x['records']:
  p=b/z['file'];assert z['status']==200 and z['TLSCertificateValidationEnabled'] and sha(p)==z['sha256'] and p.stat().st_size==z['bytes'];assert Image.open(p).size==(2200,1659);z['actuallyViewed']=True;reqs.append(z)
 write(f,x)
assert len(reqs)==30 and {x['canvas']for x in reqs}==set(range(1,31))
qa=read(b/'QA_STAR_IMAGES.json')
for x in qa['records']:
 assert sha(b/x['file'])==x['sha256'];assert ImageChops.difference(Image.open(b/x['sourceFile']).convert('RGB').crop(x['cropBox']),Image.open(b/x['file']).convert('RGB')).getbbox()is None;x['actuallyViewed']=True;x['pixelIdenticalToSourceCrop']=True
write('QA_STAR_IMAGES.json',qa)
old=read(b/'FIRST_PASS_READINGS.json')
notes={13:'增補太微賦 closes; 諸星問答論 begins with 紫微.',14:'紫微 Q&A continues; conditions and poem not all encoded.',15:'紫微 poem closes; 天機 Q&A starts.',16:'天機 poem closes; 太陽 Q&A starts.',17:'太陽 Q&A continues.',18:'太陽 poem ends; 武曲 Q&A starts.',19:'武曲 prose/verse ends; 天同 Q&A starts.',20:'天同 closes; 廉貞 Q&A (literal 屬木) then 天府 Q&A starts. Do not emend to 火 from a modern expectation.',21:'天府 prose/verse closes; 太陰 Q&A starts.',22:'太陰 closes; 貪狼 Q&A starts with 屬水.',23:'貪狼 attributed prose gives 氣屬木體屬水; 巨門 Q&A starts with 屬水金.',24:'巨門 closes; 天相 Q&A starts.',25:'天相 poem closes; 天梁 Q&A starts.',26:'天梁 poem closes; 七殺 Q&A starts with 屬火金.',27:'七殺 prose/verse closes; 破軍 Q&A starts.',28:'破軍 continues and 文昌 Q&A starts.',29:'文昌 ends; 文曲 then 流年昌曲 Q&A starts.',30:'流年昌曲 continues; 左輔 then 右弼 Q&A starts.'}
old['records'] += [dict(canvas=n,file=reqs[n-1]['file'],sha256=reqs[n-1]['sha256'],actuallyViewed=True,note=notes[n],allCharactersCollated=False,wholeConditionalRulesApplied=False)for n in range(13,31)]
assert len(old['records'])==30;write('FIRST_PASS_READINGS.json',old)
inv=read(b/'CURRENT_CANVAS_INVENTORY.json')
for x in inv['records']:
 n=x['canvas']
 if 13<=n<=30:
  z=reqs[n-1];x['retainedDerivatives']=[dict(file='v53/research/tuvi-star-offices/'+z['file'],sha256=z['sha256'],newThisScope=True)];x['newFirstPassReadThisScope']=True
 for z in x['retainedDerivatives']:z['file']=z['file'].replace('tmp/tuvi-full-volume-staging/','v53/research/tuvi-star-offices/')
inv['counts'].update(newInstitutionJPEGBodies=30,distinctRetainedPositions=46,positionsWithoutRetainedDerivativeInThisInventory=83);assert sum(bool(x['retainedDerivatives'])for x in inv['records'])==46
write('CURRENT_CANVAS_INVENTORY.json',inv)
system='NAJ-4468520-juan1-star-QA-selected-offices'
data=[
 ('紫微','紫微','Tử Vi',13,'紫微屬土',['土'],'常掌爵祿諸宮降福'),
 ('天機','天机','Thiên Cơ',15,'天機屬木',['木'],'天機兄弟主南斗正曜星'),
 ('太陽','太阳','Thái Dương',16,'太陽星屬火',['火'],'太陽原屬火正主官祿星'),
 ('武曲','武曲','Vũ Khúc',18,'武曲北斗第六星屬金',['金'],'乃財帛宮主財'),
 ('天同','天同','Thiên Đồng',19,'天同星屬水金',['水','金'],'為福德宮之主'),
 ('廉貞','廉贞','Liêm Trinh',20,'廉貞屬木',['木'],'在斗司品秩在數司權令'),
 ('天府','天府','Thiên Phủ',20,'天府屬土',['土'],'職掌財帛田宅衣祿之神'),
 ('太陰','太阴','Thái Âm',21,'太陰乃水之精',['水'],'為田宅主'),
 ('貪狼','贪狼','Tham Lang',22,'屬水',['水'],'乃主禍福之神'),
 ('巨門','巨门','Cự Môn',23,'巨門屬水金',['水','金'],'在數則掌執是非'),
 ('天相','天相','Thiên Tướng',24,'天相屬水',['水'],'是為官祿文星'),
 ('天梁','天梁','Thiên Lương',25,'天梁屬土',['土'],'乃父母之主'),
 ('七殺','七杀','Thất Sát',26,'屬火金',['火','金'],'掌生殺之權'),
 ('破軍','破军','Phá Quân',27,'破軍屬水',['水'],'司夫妻子息奴僕')]
officeCanvas={'天機':16,'太陽':18,'貪狼':23,'巨門':24,'天梁':25,'七殺':27,'破軍':28}
rows=[]
for i,(hn,iz,vn,n,literal,e,office)in enumerate(data,1):
 rows.append(dict(id=f'S{i:02d}',sourceName=hn,iztroName=iz,vietnameseStar=vn,headingCanvas=n,
  elementClaims=[dict(canvas=n,voice='Q&A answer',literal=literal,elements=e,roles=None)],
  officeClaim=dict(canvas=officeCanvas.get(hn,n),voice='attributed poem/prose'if hn in officeCanvas else'Q&A answer',literal=office),
  actualPlacementRule=False,elementWeights=None,singleElementResolved=len(e)==1,conditionalChapterFullyEncoded=False))
rows[8]['elementClaims'].append(dict(canvas=23,voice='希夷先生曰 attributed prose',literal='其氣屬木體屬水',elements=['木','水'],roles={'氣':'木','體':'水'}))
rows[8]['singleElementResolved']=False
rows[5]['readingNote']='Image reads 木. Provisional fire filename was a research mislabel, corrected before any table or consumer promotion. This study does not decide other editions.'
rows[0]['elementClaims'][0]['literal']='紫微屬土'
write('SOURCE_TABLES.json',dict(date='2026-10-28',system=system,scope='Fourteen selected principal-star element/office labels; not full Q&A conditional rule encoding.',rows=rows,voiceClaims=15,elementAndOfficeAreNotAnStarAlgorithm=True,consumerChanged=False,wholeBookApplied=False))
# Source-unit dispositions distinguish selected lookup use from complete text coverage.
units=[dict(title=t,startCanvas=a,endCanvas=z,status='first-pass-read-selected-only',wholeUnitApplied=False)for t,a,z in [('太微賦',5,7),('形性賦',7,8),('續形性賦',8,9),('星垣論',9,10),('斗數準繩',10,11),('斗數發微論',11,12),('增補太微賦',12,13)]]
units += [dict(title=hn+'問答',startCanvas=n,endCanvas=(data[i+1][3]if i+1<len(data)else 28),status='selected-element-office-lookup-only',wholeUnitApplied=False,remaining='All conditional strength, placement, combinations, era/sex and outcome premises; not reduced to one star label.')for i,(hn,iz,vn,n,li,e,of)in enumerate(data)]
units += [dict(title='文昌/文曲/流年昌曲/左輔/右弼問答',startCanvas=28,endCanvas=None,lastViewedCanvas=30,status='open-continuation',wholeUnitApplied=False)]
write('SOURCE_DISPOSITIONS.json',dict(date='2026-10-28',units=units,contentsSixJuanNotSixBodiesRead=True,wholeBookApplied=False))
write('SOURCE_MANIFEST.json',dict(date='2026-10-28',institution='National Archives of Japan',item='https://www.digital.archives.go.jp/item/4468520',catalogue='https://www.digital.archives.go.jp/file/1078787',manifestFile='v53/research/fortune-followup/official-manifest.json',manifestSHA256=sha(w/'v53/research/fortune-followup/official-manifest.json'),images=reqs,sourceKind='Institution-served 2200width JPEG derivatives, not original JP2',printedAttributionIsNotAuthenticatedAuthorship=True,editionYearEstablished=False,originalJP2BodiesAcquired=0))
write('READING_CORRECTIONS.json',dict(date='2026-10-28',corrections=[dict(stage='Before source table/engine test/consumer promotion',provisional='Liêm Trinh fire/possible fire-wood conflict',corrected='Canvas20 Q&A literal 木; no internal fire-wood conflict established.',reason='Direct native crop and full-page inspection; no modern label used to emend source.'),dict(provisional='canvas21 crop named lianzhen-wood-verse',corrected='Crop is 天府 verse; excluded as Liêm Trinh proof.',retainedFilenameForAudit=True)],consumerEverAffected=False))
module="""import {readFileSync} from 'node:fs';
const table=JSON.parse(readFileSync(new URL('./SOURCE_TABLES.json',import.meta.url),'utf8'));
const branches=[...'子丑寅卯辰巳午未申酉戌亥'];
const palaces=['命宮','兄弟','夫妻','子女','財帛','疾厄','遷移','交友','官祿','田宅','福德','父母'];
function rowFor({system,star}={}){
 if(system!==table.system||typeof star!=='string')throw new TypeError('Explicit named source and canonical Vietnamese star are required');
 const row=table.rows.find(x=>x.vietnameseStar===star);if(!row)throw new TypeError('Unknown source star');return row;
}
export function sourceStarProfile(input){
 const row=rowFor(input);return {...structuredClone(row),system:table.system,officeIsPlacementConstraint:false,physicalPalaceInferred:false,practicalOutcome:null,elementScore:null,fullChapterApplied:false};
}
export function attachDeclaredPlacement(input){
 const p=sourceStarProfile(input),{branch,palace}=input;
 if(branch===undefined||palace===undefined)throw new TypeError('Placement branch and palace must be explicit, including null');
 if(branch!==null&&!branches.includes(branch))throw new TypeError('Canonical branch or null required');
 if(palace!==null&&!palaces.includes(palace))throw new TypeError('Canonical palace or null required');
 if(branch===null&&palace!==null)throw new TypeError('A palace cannot be attached without a known branch');
 return {...p,declaredPlacement:{branch,palace,known:branch!==null,provenance:'caller-supplied, not inferred from symbolic office'},officeReplacesPhysicalPlacement:false};
}
"""
(b/'star-office-reference.mjs').write_text(module,encoding='utf-8')
print(json.dumps(dict(http200=30,headers=sum(bool(x.get('responseHeadersRetained'))for x in reqs),rows=len(rows),claims=15,readings=30,crops=len(qa['records']))))

