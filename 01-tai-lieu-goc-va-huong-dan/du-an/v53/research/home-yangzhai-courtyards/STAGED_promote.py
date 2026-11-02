from pathlib import Path
from hashlib import sha256
import json,shutil
w=Path.cwd();r=w/'v53';s=w/'tmp/home-yangzhai-courtyard-staging';b=r/'research/home-yangzhai-courtyards';q=r/'qa/home-yangzhai-courtyards'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
write=lambda p,o:p.write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
assert not b.exists()and not q.exists()
assert read(w/'archives/v53-before-home-yangzhai-courtyards/SNAPSHOT.json')['sourceManifestFiles']==4354
assert read(s/'NATIVE_RESULTS.json')['cropsVerified']==25
for name,n in [('REFERENCE_RESULTS.json',6),('CONTEXT_RESULTS.json',4)]:
 result=read(s/name);assert len(result['checks'])==n and all(x['ok']for x in result['checks'])
b.mkdir();q.mkdir();identities=[]
qnames=['NATIVE_RESULTS.json','QA_IMAGES.json','GJTS_QA_IMAGES.json','REFERENCE_RESULTS.json','CONTEXT_RESULTS.json']
def copy(p,d):
 d.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,d);assert p.read_bytes()==d.read_bytes()
 identities.append(dict(file=d.relative_to(w).as_posix(),stagingFile=p.relative_to(w).as_posix(),bytes=d.stat().st_size,sha256=sha256(d.read_bytes()).hexdigest()))
for p in sorted(s.rglob('*')):
 if not p.is_file():continue
 rel=p.relative_to(s)
 if rel.parts[0]=='qa':target=q/rel.name
 elif p.name in qnames:target=q/p.name
 elif p.name=='REPORT.md':target=r/'HOME_COURTYARDS_REPORT.md'
 elif p.suffix in ['.py','.mjs']and p.name not in ['courtyard-reference.mjs','courtyard-context-reference.mjs']:target=b/('STAGED_'+p.name)
 else:target=b/rel
 copy(p,target)
maps={
 'test-courtyard-reference.mjs':[("from './courtyard-reference.mjs'","from '../research/home-yangzhai-courtyards/courtyard-reference.mjs'"),("const b=import.meta.dirname,w=resolve(b,'../..'),system=COURTYARD_SYSTEM;","const b=resolve(import.meta.dirname,'../research/home-yangzhai-courtyards'),w=resolve(b,'../../..'),system=COURTYARD_SYSTEM;"),("resolve(b,'REFERENCE_RESULTS.json')","resolve(w,'v53/qa/home-yangzhai-courtyards/REFERENCE_RESULTS.json')")],
 'test-courtyard-context.mjs':[("from './courtyard-context-reference.mjs'","from '../research/home-yangzhai-courtyards/courtyard-context-reference.mjs'"),("new URL('./CONTEXT_RESULTS.json',import.meta.url)","new URL('../qa/home-yangzhai-courtyards/CONTEXT_RESULTS.json',import.meta.url)")]}
for name,pairs in maps.items():
 text=(s/name).read_text(encoding='utf-8')
 for old,new in pairs:assert text.count(old)==1;text=text.replace(old,new)
 (r/'scripts'/('test-home-'+name.removeprefix('test-'))).write_text(text,encoding='utf-8')
write(b/'PROMOTION_IDENTITIES.json',dict(date='2026-10-28',records=identities,moduleByteIdenticalToStaging=True,testsOnlyPathRelocated=True,passedRuntimeTestsNotRerunOnPromotion=True))
summary='P08:12đồraw82–93chép69ôtrực tiếp,bađồ5ô/bốnôsaođểtrống;10kiểm(6đồ+4ngữcảnh),75lờigọithànhphầntọađộthật/0chartlịch. C84neo木khác4ô/giảthuyếtThủykhác2ô,khôngép sửa. NămHTTP200TLSthêmDjVukhoCommons33681249byte/135vịtrí;4rendernative86–89địnhvị12đồ,6ôC84đối literal cùng木1/6;chưađộc lậphệbản hoặc63ôcònlại.25cropđãxem/khớppixel;0vịtrímớiPDFThiênNhấtCác. Khởilớpđòigốctường+cửa/chiềuđầunhà,khôngtựgántầngđứng/phòngcáthung. P08vẫn195/195đọcđầu/0mụcáphết;webnguyênbyte,toànkhoactive.'
nexts=['Tiếp63ônhânchứngvàcácđiềukiệntrungcung/phươngbên/cao-thấp/交門換象初爻;khôngtựsửaC84木từchu kỳ.12đồ/cửavàgốcphânviệnkhôngthayphépmặtbằnghoànchỉnh.',
 'Bảnggiờ132ô/12司命khácengine/12勾陳chưa nhập;tiếpnhânchứnghợp lệ,khoanhđúngphạmvi截路.720ôtháng/ma trận năm/tuổi/lịch/thướcvẫnmở.',
 'LuânphiênBáttựvượngsuy/cáchcục,Tửvi童限火鈴CanhNhâm/khởihạn,DịchB02/B03/MaiHoa;khônglặptảinguồnbịchặnhoặckiểmđãđạt.ỨngviênKiếnLộcchờbrowserQAkhảdụng;nghiêncứu/QAngoàisite,khôngxuấtbản.']
state=read(b/'WORK_STATE.json');state.update(status='bounded-courtyard-reference-and-selected-witness-verified',sourceDirectory=b.relative_to(w).as_posix(),latestReport='v53/HOME_COURTYARDS_REPORT.md',completedStep=summary,next=nexts);write(b/'WORK_STATE.json',state)
p=w/'EXHAUSTIVE_WORK_STATE.json';ex=read(p);ex['previousHomeFinalSpansWork']=ex['currentWork']
ex['currentWork']=dict(catalogueID='P08',work='陽宅十書 — 穿宮十二宅圖與語境',sourceDirectory=b.relative_to(w).as_posix(),currentStep=summary,latestResearchReport=state['latestReport'],sourceLimits='69literalcells/6selectedwitnesscells;twoexplicitfacingclauses;63witnesscells/fullgeometrypremisesopen;0wholeunitsapplied')
ex['inProgressScope']=b.relative_to(w).as_posix()+'/WORK_STATE.json';ex['subsequentPriority']=[' '.join(nexts)]+ex['subsequentPriority'];write(p,ex);(r/'research/EXHAUSTIVE_WORK_STATE.json').write_bytes(p.read_bytes())
p=r/'research/full-study/WORK_STATE.json';full=read(p);full['latestResearchReport']=state['latestReport'];full['exhaustiveNext']=' '.join(nexts)
x=next(x for x in full['items']if x['id']=='home');x['completed'].append(summary);x['latestResearchReport']=state['latestReport'];x['latestScope']='../home-yangzhai-courtyards/WORK_STATE.json';x['nextFile']='../home-yangzhai-courtyards/SOURCE_DISPOSITIONS.json';write(p,full)
p=r/'research/library-current/COVERAGE.json';c=read(p);c['counts']['newDownloadsThisScope']=5;c['counts']['newDownloadsThisScopeBasis']='5HTTP200TLSbodies incl1repositoryDjVu;4nativecomparisonpositions/6selectedcells,notindependentworkorwholepagecollation.'
x=next(x for x in c['catalogue']if x['id']=='P08');x['scope']='195/195firstpass/0wholeunits;12courtyards69cells/10checks,6selectedsecondwitnesscellsagreeincludingunresolved木;fullpremisesand63witnesscellsopen.';x['latestSourceScope']=summary
x['currentSourceUnitCounts'].update(manualCourtyardCells=69,selectedSecondWitnessCells=6,newComparisonWitnessPositions=4,totalDistinctPositionsRead=195,wholeUnitsApplied=0)
x['currentEvidence'] += [state['latestReport'],b.relative_to(w).as_posix()+'/WORK_STATE.json',b.relative_to(w).as_posix()+'/REQUESTS.json',b.relative_to(w).as_posix()+'/MANUAL_DIAGRAM_CELLS.json',b.relative_to(w).as_posix()+'/SELECTED_WITNESS_COLLATION.json',b.relative_to(w).as_posix()+'/courtyard-context-reference.mjs',q.relative_to(w).as_posix()+'/REFERENCE_RESULTS.json',q.relative_to(w).as_posix()+'/CONTEXT_RESULTS.json'];write(p,c)
for p,title in [(r/'NEXT_STEPS.md','Mốc đồ phân viện'),(r/'research/library-current/COVERAGE.md','Mốc độ phủ đồ phân viện'),(w/'PROJECT_RESEARCH_STATE.md','Mốc đồ phân viện/nhân chứng')]:
 old=p.read_text(encoding='utf-8-sig');p.write_text(f'{title},28/10/2026: `HOME_COURTYARDS_REPORT.md`. {summary}\n\nTiếp: '+' '.join(nexts)+'\n\n'+old,encoding='utf-8')
p=w/'PENDING_RESEARCH_STATE.json';pending=read(p);pending.update(status=state['status'],workDirectory=b.relative_to(w).as_posix(),currentWorkState=b.relative_to(w).as_posix()+'/WORK_STATE.json',latestReport=state['latestReport'],next=nexts,packageVerification='courtyard-promotion-awaiting-final-no-write',inProgressStaging=dict(file='tmp/home-yangzhai-courtyard-staging/WORK_STATE.json',status='promoted;packageverificationpending',catalogueID='P08'));write(p,pending)
print(json.dumps(dict(promotionIdentities=len(identities),runtimeChecks=10,actualExistingLayerCalls=75,consumerChanged=False)))
