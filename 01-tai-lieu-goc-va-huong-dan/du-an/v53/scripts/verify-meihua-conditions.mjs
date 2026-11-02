import {readFile,writeFile,mkdir} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {resolve} from 'node:path';
import vm from 'node:vm';import assert from 'node:assert/strict';
import {analyze,listDomains,relation,seasonEvidence} from '../research/meihua-conditions/conditions-reference.mjs';
const root=resolve(import.meta.dirname,'..'),base=resolve(root,'research/meihua-conditions'),qa=resolve(root,'qa/meihua-conditions');
const json=async p=>JSON.parse(await readFile(p,'utf8')),sha=b=>createHash('sha256').update(b).digest('hex');
const checks=[];function test(name,detail){checks.push({name,ok:true,detail});console.log('PASS',name);}
await mkdir(qa,{recursive:true});
const manual=await json(resolve(base,'MANUAL_READINGS.json')),index=await json(resolve(root,'research/meihua/EXTRACTED_PAGES.json')),baseline=await json(resolve(base,'SOURCE_BASELINE.json'));
assert.equal(sha(await readFile(resolve(base,manual.sourcePDF))),manual.sourcePDFSHA256);
assert.equal(index.pages.length,214);assert.equal(baseline.previousRenderedRecords.length,186);
for(const r of index.pages){let b=await readFile(resolve(root,'research/meihua',r.file));assert.equal(b.length,r.bytes);assert.equal(sha(b),r.sha256);}
for(const r of baseline.previousRenderedRecords)assert.deepEqual(index.pages.find(x=>x.pdfPage===r.pdfPage),r);
for(const r of manual.records)assert.equal(sha(await readFile(resolve(base,r.image))),r.imageSHA256);
for(const r of (await json(resolve(root,'research/meihua/REQUESTS.json'))).records){const b=await readFile(resolve(root,'research/meihua',r.file));assert.equal(b.length,r.bytes);assert.equal(sha(b),r.sha256);}
test('Original PDF,all214derivatives and48bounded reading images retain identity;186previous derivative records stay exact');

assert.deepEqual(manual.records.map(r=>r.pdfPage),Array.from({length:48},(_,i)=>55+i));
assert.equal(manual.records.filter(r=>r.kind==='content').length,44);
assert.equal(manual.records.filter(r=>r.kind==='content'&&!r.expandedEarlierReading).length,38);
assert.equal(manual.records.filter(r=>r.expandedEarlierReading).length,6);
assert.deepEqual(manual.records.filter(r=>r.kind==='advertisement').map(r=>r.pdfPage),[99,100]);
assert.equal(manual.records.at(-1).kind,'physical-book-cover');assert.equal(manual.wholeBookRead,false);
const units=await json(resolve(base,'UNIT_MAP.json'));assert.equal(units.units.length,52);assert.equal(units.endPDFPage,98);
assert.ok(units.units.every(u=>u.evidencePDFPages.every(p=>p>=55&&p<=98)&&!u.wholeUnitApplied));
const pages=new Set(units.units.flatMap(u=>u.evidencePDFPages));assert.equal(pages.size,44);
test('Volume2ends98/printed44;ads99–100,logo101andlower冊cover102are excluded;52units keep partialclause status');

const digital=await json(resolve(root,'research/meihua-reading/DIGITAL_UNIT_DISPOSITIONS.json'));
for(const u of units.units){const r=digital.records.find(r=>r.id===u.id);assert.equal(u.heading,r.heading);assert.equal(u.digitalSourceSliceSHA256,r.sourceSliceSHA256);}
const data=await json(resolve(base,'DOMAIN_RULES.json'));assert.equal(listDomains().length,18);assert.equal(data.domains.reduce((s,d)=>s+Object.keys(d.directRelations).length,0),85);
assert.deepEqual(data.domains.map(d=>d.ordinal),Array.from({length:18},(_,i)=>i+1));
assert.ok(data.domains.every(d=>!d.prognosticClaimsValidated));assert.equal(data.consumerApplied,false);
test('52physical-unit links retain pinned digital slices;18domainroles/85direct clauses are source assertions,notvalidatedoutcomes');

const order=['Mộc','Hỏa','Thổ','Kim','Thủy'],keys=['same','body-generates-use','body-controls-use','use-controls-body','use-generates-body'];
for(let b=0;b<5;b++)for(let u=0;u<5;u++)assert.equal(relation(order[b],order[u]),keys[(u-b+5)%5]);
assert.throws(()=>relation('土','Thổ'));assert.throws(()=>relation('Kim',undefined));
test('All25directional element pairs agree with an independent cycle-distance classifier');

const c={};c.window=c;vm.createContext(c);for(const f of ['engine.js','meihua.js'])vm.runInContext(await readFile(resolve(root,f),'utf8'),c);
const cases=[],byRelation=new Map();let graphNodes=0,graphEdges=0;
for(let upper=1;upper<=8;upper++)for(let lower=1;lower<=8;lower++)for(let moving=1;moving<=6;moving++){
 const cast=c.HHC_MEIHUA.compose(upper,lower,moving),r=analyze(cast,{subject:'planning'});cases.push(cast);
 if(!byRelation.has(r.directRelation))byRelation.set(r.directRelation,cast);
 assert.equal(r.bodyReference,moving<=3?upper:lower);assert.equal(r.nodes.length,5);
 assert.equal(r.nodes.find(n=>n.id==='mutual-body-side').n,moving<=3?cast.mutual.upper.n:cast.mutual.lower.n);
 assert.equal(r.nodes.find(n=>n.id==='mutual-use-side').n,moving<=3?cast.mutual.lower.n:cast.mutual.upper.n);
 assert.equal(r.directRelation,cast.relation.key);
 for(const edge of r.edges){const a=r.nodes.find(n=>n.id===edge.from),b=r.nodes.find(n=>n.id===edge.to),dist=(order.indexOf(b.element)-order.indexOf(a.element)+5)%5;
  assert.equal(edge.kind,dist===0?'same':dist===1?'generates':'controls');assert.ok([0,1,2].includes(dist));}
 assert.ok(r.nodes.every(n=>n.season.missing&&n.season.overallState===null));
 assert.ok(r.qualifiers.every(q=>q.automaticCancellation===false));
 assert.deepEqual(r.limits,{prognosticValidityEstablished:false,score:null,finalVerdict:null,predictedDate:null,monthDayPriorityResolved:false});
 graphNodes+=r.nodes.length;graphEdges+=r.edges.length;
}
assert.equal(cases.length,384);assert.equal(byRelation.size,5);
test('384realcurrent-engine casts feed the new relation graph:bodyreference,sides,all edges and missingpremises stay explicit',{graphNodes,graphEdges});

let domainCells=0;
for(const domain of data.domains.filter(d=>d.id!=='weather'))for(const [key,cast]of byRelation){const r=analyze(cast,{subject:domain.id});
 assert.equal(r.directRelation,key);assert.equal(r.directClause.printedBoundedPhrase,domain.directRelations[key].printedBoundedPhrase);
 assert.equal(r.directClause.notFinalVerdict,true);assert.deepEqual(r.roles,{body:domain.bodyRole,use:domain.useRole});domainCells++;}
assert.equal(domainCells,85);
const controlled=byRelation.get('body-controls-use');
assert.equal(analyze(controlled,{subject:'dining'}).directClause.printedBoundedPhrase,'飲食有阻');
assert.equal(analyze(controlled,{subject:'trade'}).directClause.printedBoundedPhrase,'交易成遲');
assert.equal(analyze(controlled,{subject:'traveller'}).directClause.printedBoundedPhrase,'行人歸遲');
assert.equal(analyze(controlled,{subject:'travel'}).directClause.printedBoundedPhrase,'可行所至多得意');
assert.deepEqual(analyze(controlled,{subject:'birth'}).roles,{body:'母',use:'生'});
test('85historical clause selections keep subject-specific roles and fourcounterexamples to a universal body-controls-use verdict');

for(const cast of [cases[0],cases.at(-1)]){const r=analyze(cast,{subject:'weather'});assert.equal(r.bodyUseApplicable,false);assert.equal(r.roles,null);assert.equal(r.directClause,null);assert.deepEqual(r.nodes,[]);assert.deepEqual(r.qualifiers,[]);}
test('Weathersectiondoesnotdividebody/use and neverfalls through to ordinarydomainverdicts');

const season=await json(resolve(base,'SEASON_PREMISES.json'));let seasonalPairs=0;
for(const [s,row]of Object.entries(season.seasons)){assert.equal(seasonEvidence(row.strong,{season:s}).observations[0].state,'strong');assert.equal(seasonEvidence(row.oppressed,{season:s}).observations[0].state,'oppressed');
 assert.equal(order.filter(e=>seasonEvidence(e,{season:s}).observations[0].state==='unspecified').length,3);seasonalPairs+=2;}
for(const [branch,element]of Object.entries(season.branchStrong))assert.equal(seasonEvidence(element,{monthBranch:branch}).observations[0].state,'strong');
const conflict=seasonEvidence('Hỏa',{monthBranch:'午',dayBranch:'子'});assert.deepEqual(conflict.observations.map(o=>o.state),['strong','oppressed']);assert.equal(conflict.overallState,null);assert.equal(conflict.priorityResolved,false);
for(const x of [{date:'2026-10-26'},{season:'__proto__'},{season:'constructor'},{dayBranch:'Tý'},{monthBranch:0}])assert.throws(()=>seasonEvidence('Mộc',x));
test('10seasonstatuscells/12branchanchors preserve unspecified states and conflictingmonth/dayevidence;no date/boundary/priority invented');

const well=c.HHC_MEIHUA.compose(6,5,5),wr=analyze(well,{subject:'dwelling'});
assert.equal(well.primary,48);assert.equal(well.changed,46);
assert.ok(wr.qualifiers.some(q=>q.actor==='mutual-use-side'&&q.target==='mutual-body-side'&&q.kind==='controller-controlled'));
assert.ok(wr.qualifiers.some(q=>q.actor==='changed-use'&&q.target==='use'&&q.kind==='supporter-controlled'));
assert.equal(wr.limits.finalVerdict,null);assert.equal(wr.limits.score,null);
test('Printed井example48→46retainsfirecontrollingmetal and potentialearthcontrollingwatersupport simultaneously;no cancellation or finalscore');

const goldWood=analyze(c.HHC_MEIHUA.compose(4,1,1),{subject:'human',observations:[{id:'external-gold',trigram:1,observed:'Manually selected metal symbol'}]});
const bladeWater=analyze(c.HHC_MEIHUA.compose(6,1,1),{subject:'human',observations:[{id:'external-blade',trigram:1,observed:'Manually selected metal implement'}]});
assert.equal(goldWood.nodes.at(-1).relationToBody,'use-controls-body');assert.equal(bladeWater.nodes.at(-1).relationToBody,'use-generates-body');
assert.equal(analyze(cases[0],{subject:'human'}).externalObservations.length,0);
for(const obs of [[{id:'external-a',trigram:1,observed:''}],[{id:'external-a',trigram:9,observed:'x'}],[{id:'external-a',trigram:1,observed:'x'},{id:'external-a',trigram:2,observed:'y'}]])assert.throws(()=>analyze(cases[0],{subject:'human',observations:obs}));
test('Explicitmetalobservations reverse relationship underwoodversuswaterbody;quiet/no-observationinputinventsnothing');

const bad=JSON.parse(JSON.stringify(cases[0]));bad.mutual.upper.bits[0]=1-bad.mutual.upper.bits[0];
assert.throws(()=>analyze(bad,{subject:'planning'}));
for(const options of [undefined,{}, {subject:'unknown'},{subject:'planning',year:2026}])assert.throws(()=>analyze(cases[0],options));
const fresh=analyze(cases[0],{subject:'planning'});fresh.directClause.printedBoundedPhrase='mutated';fresh.nodes[0].n=99;
assert.notEqual(analyze(cases[0],{subject:'planning'}).directClause.printedBoundedPhrase,'mutated');
test('Referencecompilerrejectsinconsistentactualcasts,missing/unknownsubjects andundeclaredpremises;outputs do not mutate source tables');

const piCases=[];
for(let moving=1;moving<=6;moving++){
 const cast=c.HHC_MEIHUA.compose(1,8,moving),bits=cast.values.map(v=>v===6||v===7?1:0);
 const ts=c.HHC_MEIHUA.trigrams(),find=b=>ts.find(t=>t.bits.every((v,i)=>v===b[i]));
 piCases.push({moving,primary:cast.primary,changed:cast.changed,body:cast.body.n,use:cast.use.n,changedUse:cast.changedUse.n,
              mainNuclear:{upper:cast.mutual.upper.n,lower:cast.mutual.lower.n,number:cast.mutual.number},
              changedNuclear:{upper:find(bits.slice(2,5)).n,lower:find(bits.slice(1,4)).n,number:c.HHC_ENGINE.hexNumber([...bits.slice(1,4),...bits.slice(2,5)].map(b=>b?7:8))}});
}
assert.deepEqual(piCases.map(r=>r.changed),[25,6,33,20,35,45]);
assert.deepEqual(piCases[1].mainNuclear,{upper:5,lower:7,number:53});assert.deepEqual(piCases[1].changedNuclear,{upper:5,lower:3,number:37});
test('SixactualBĩ12changesretainmainnuclear53;sourcecase2巽離matcheschangednuclear37,recordedascontextvariantnotuniversalrule',{piCases});

const variants=await json(resolve(base,'VARIANTS_AND_GAPS.json'));assert.equal(variants.variants.length,5);
assert.equal(variants.variants.find(v=>v.id==='midday-dui').printed,'離之時坤兌為體則吉');
assert.equal(relation('Kim','Hỏa'),'use-controls-body');
test('Fiveboundedtext/contextvariantsretainmidday兌contradictionandtrade/branch/burialdifferenceswithoutrepairingrawwitness');

const archive=resolve(root,'../archives/v53-before-meihua-conditions'),old=await json(resolve(archive,'PACKAGE_MANIFEST.json'));
const html=await readFile(resolve(root,'Huyen_Hoc_Cac.html'));assert.equal(sha(html),old.product.sha256);assert.equal(html.length,703410);
for(const f of old.files.filter(f=>!f.file.includes('/')&&/\.(js|css)$/.test(f.file)))assert.equal(sha(await readFile(resolve(root,f.file))),f.sha256);
assert.equal(sha(await readFile(resolve(root,'site/index.html'))),sha(html));assert.equal(sha(await readFile(resolve(root,'../Huyen_Hoc_Cac.html'))),sha(html));
assert.ok(!html.includes(Buffer.from('conditions-reference')));
const pending=await json(resolve(root,'research/meihua-layers/PENDING.json'));assert.equal(pending.released,false);assert.equal(pending.browserChecksExecuted,0);assert.equal(pending.pdfCreated,false);
for(const f of pending.candidateFiles)assert.equal(sha(await readFile(resolve(root,'research/meihua-layers/candidate',f.file))),f.sha256);
test('ResearchcompilerisnotloadedbyconsumerHTML;allreleasedmodulesandparkedcandidatebytesremainexact');

await writeFile(resolve(qa,'ENGINE_RESULTS.json'),JSON.stringify({checks,summary:{sourcePageRecords:48,contentPages:44,newContentPageRecords:38,expandedContentPageRecords:6,physicalUnits:52,domains:18,directRelationCells:85,elementPairs:25,realCastGraphStructures:384,graphNodes,graphEdges,seasonStatusCells:10,branchAnchors:12,piContextCases:6,textContextVariants:5,newPNGDerivatives:28,retainedPNGDerivatives:214,newHTTPResponses:0,consumerChanged:false,predictiveAccuracyEstablished:false,wholeVolumeClausesCompleted:false,wholeBookApplied:false},piCases,htmlSHA256:sha(html)},null,2)+'\n');
console.log(checks.length+'/'+checks.length,'passed');
