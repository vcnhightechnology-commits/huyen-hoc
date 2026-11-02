from pathlib import Path
from hashlib import sha256
import json,shutil

r=Path(__file__).resolve().parent.parent;w=r.parent;s=w/'tmp/bazi-yangren-conditions-staging';b=r/'research/bazi-yangren-conditions';q=r/'qa/bazi-yangren-conditions'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'));sha=lambda p:sha256(p.read_bytes()).hexdigest()
def write(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
assert not b.exists()and not q.exists(),'One-shot promotion; preserve original staging'
assert (w/'archives/v53-before-bazi-yangren-conditions/Huyen_Hoc_Cac_V53_source.zip').stat().st_size==2070081817
b.mkdir();(b/'images').mkdir();q.mkdir()
container=r/'research/bazi-pattern-witness/CADAL06066041.djvu';digital=r/'research/four-items/sources/KR3g0042_005.txt';decoder=r/'research/bazi-pattern-extension/tooling/djvu.js'
assert sha(container)=='013ce4861680a2bf08b811050c45a45bb2d3ce9d164f7e2341d7070bd5cb2c1a'
assert sha(digital)=='1ebdd92feaa57496b702f962ad6fafd4f19c17e98c38a94b40f626ef321dd997'
assert sha(decoder)=='10a831d62cc7ced39c30c7350a11410402d082a0f0a5b073a88d3d7ca662add3'
for name in ['RETAINED_DIGITAL_SECTION.txt','NORMALIZED_DIGITAL_BODY.txt','CONTEXT_REVIEW.json','SELECTED_SUBCONTEXTS.json','SOURCE_COORDINATES.json','PREDICATE_MATRIX.json','coordinate-reference.mjs','predicate-reference.mjs']:
 shutil.copyfile(s/name,b/name)
manual=read(s/'MANUAL_READINGS.json')
for x in manual['records']:
 old=w/x['file'];assert sha(old)==x['sha256']
 if x['newSourceReadPosition']:
  dest=b/'images'/old.name;shutil.copyfile(old,dest);x['inheritedStagingFile']=x['file'];x['file']=dest.relative_to(w).as_posix()
 x['targetedRereadThisPromotion']=x['containerPage']in[204,205,206,207,208,209,215,216]
manual['readingCountsBasis']='21first-passpositions inherited from staging;this scope reread8retainedpositions.13first-read positions newlyenterpackage,not13newdownloadsornewfirstreads thisheartbeat.'
write(b/'MANUAL_READINGS.json',manual)
renders=read(s/'LOCAL_RENDERS.json')
for x in renders['records']:x['inheritedStagingFile']=x['file'];x['file']='images/'+x['file']
renders['inheritedStaging']='tmp/bazi-yangren-conditions-staging/LOCAL_RENDERS.json';write(b/'LOCAL_RENDERS.json',renders)
crops=read(s/'PAIR_DETAIL_CROPS.json')
for x in crops['records']:
 shutil.copyfile(s/x['file'],q/x['file'])
 if x['page']==205:x['source']=(b/'images/p205.png').relative_to(w).as_posix()
write(b/'PAIR_DETAIL_CROPS.json',crops)
for old,new in [('COORDINATE_RESULTS.json','COORDINATE_RESULTS.json'),('SOURCE_EXAMPLES_PROBE.json','SOURCE_EXAMPLES_PROBE.json'),('PREDICATE_RESULTS.json','RESULTS.json')]:shutil.copyfile(s/old,q/new)
identities=[]
for name in['coordinate-reference.mjs','predicate-reference.mjs','PREDICATE_MATRIX.json','SOURCE_COORDINATES.json','SELECTED_SUBCONTEXTS.json']:
 assert(b/name).read_bytes()==(s/name).read_bytes()
 identities.append({'file':(b/name).relative_to(w).as_posix(),'inheritedStagingFile':(s/name).relative_to(w).as_posix(),'sha256':sha(b/name)})
for old,new in [('COORDINATE_RESULTS.json','COORDINATE_RESULTS.json'),('SOURCE_EXAMPLES_PROBE.json','SOURCE_EXAMPLES_PROBE.json'),('PREDICATE_RESULTS.json','RESULTS.json')]:
 assert(q/new).read_bytes()==(s/old).read_bytes()
 identities.append({'file':(q/new).relative_to(w).as_posix(),'inheritedStagingFile':(s/old).relative_to(w).as_posix(),'sha256':sha(q/new)})
write(b/'PROMOTION_IDENTITIES.json',{'date':'2026-10-28','basis':'Local identity hashes recorded at byte-identical promotion,not publisher signatures. Verification reads packaged files,not the unreleased tmp directory.','records':identities})
for old,new,imp in [('test-coordinate-reference.mjs','test-bazi-yangren-coordinates.mjs','coordinate-reference'),('test-predicate-reference.mjs','test-bazi-yangren-predicates.mjs','predicate-reference')]:
 text=(s/old).read_text(encoding='utf-8-sig').replace("from'./"+imp+".mjs'","from'../research/bazi-yangren-conditions/"+imp+".mjs'")
 if old.startswith('test-coordinate'):
  text=text.replace("b=import.meta.dirname,req=", "b=resolve(r,'research/bazi-yangren-conditions'),q=resolve(r,'qa/bazi-yangren-conditions'),req=")
  text=text.replace("resolve(b,'COORDINATE_RESULTS.json')","resolve(q,'COORDINATE_RESULTS.json')")
 else:
  text=text.replace("const b=import.meta.dirname,w=process.cwd(),r=resolve(w,'v53'),read=", "const w=process.cwd(),r=resolve(w,'v53'),b=resolve(r,'research/bazi-yangren-conditions'),q=resolve(r,'qa/bazi-yangren-conditions'),read=")
  text=text.replace("resolve(b,'SOURCE_EXAMPLES_PROBE.json')","resolve(q,'SOURCE_EXAMPLES_PROBE.json')").replace("resolve(b,'PREDICATE_RESULTS.json')","resolve(q,'RESULTS.json')")
 (r/'scripts'/new).write_text(text,encoding='utf-8')
probe=read(q/'SOURCE_EXAMPLES_PROBE.json')
write(b/'PRINTED_EXAMPLES.json',{'date':'2026-10-28','sourceContainerPage':218,'examples':[{'sourcePillars':x['sourcePillars'],'sourceOutcomeValidated':False,'historicalDateKnown':False}for x in probe['sourceExamples']]})
matrix=read(r/'research/full-study/bazi/PATTERN_READING_MATRIX.json');matrix['supersedesForCurrentWork']='research/full-study/bazi/PATTERN_READING_MATRIX.json;historicalmatrixretained'
yang=next(x for x in matrix['records']if x['section']=='論陽刃');yang['currentFullFirstPassSpan']={'containerPages':[198,218],'uniquePositions':21,'newReadPositionsPromotedFromStaging':13,'expandedPriorReadPositionsInStaging':8,'wholeSectionFirstPassRead':True,'allCharactersCollated':False,'editorialContexts':55,'selectedMixedContexts':8,'selectedSubcontexts':59,'selectedCodepoints':1180,'localPredicateAudits':28,'fullConditionalClassifier':False,'evidence':'../bazi-yangren-conditions/WORK_STATE.json'}
matrix['next']='Do not repeat passing coordinate fixtures withoutchange. Remaining47editorialcontexts andunresolvedsubordinatepremises/voices needextraction;selected28localpredicateaudits do notestablishstrength/usefulgod/clinicalorfinancialoutcomes. Keep other9sections fullconditions active.'
write(b/'CURRENT_PATTERN_READING_MATRIX.json',matrix)
write(b/'SOURCE_MANIFEST.json',{'date':'2026-10-28','sourceContainer':container.relative_to(w).as_posix(),'sourceBytes':container.stat().st_size,'sourceSHA256':sha(container),
 'retainedDigitalSource':digital.relative_to(w).as_posix(),'digitalSHA256':sha(digital),'decoder':decoder.relative_to(w).as_posix(),'decoderSHA256':sha(decoder),'actualContainerPages':226,
 'provenance':'Inherited original/TLS/identity records inbazi-pattern-witness andbazi-pattern-extension. Local unmodified NodeVM decoder,not browser or new independentwitness.',
 'nativeImages':manual['records'],'inheritedNativeRendersPromoted':13,'inheritedPriorPositionsExpanded':8,'targetedPriorPositionsRereadThisScope':8,
 'newHTTPRequests':0,'newOriginalContainers':0,'newSourcePositionsThisHeartbeat':0,'newIndependentWitnesses':0,'sourceEmended':False,'sourceInstructionsAreData':True})
print('Promoted staged source data and unchanged tested references;28localpredicateaudits/59subcontexts added,fullconditions open.')
