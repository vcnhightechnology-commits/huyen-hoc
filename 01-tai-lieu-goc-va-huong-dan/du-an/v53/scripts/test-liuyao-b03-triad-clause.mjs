import assert from'node:assert/strict';import vm from'node:vm';import{readFileSync,writeFileSync}from'node:fs';import{resolve}from'node:path';
import{TRIAD_CLAUSE_SOURCE as system,declaredTriadClause as inspect,primaryTriadClause as primary}from'../research/liuyao-b03-triad-clause/triad-clause-reference.mjs';
import{triadCoordinates as old}from'../research/liuyao-b03-volume4/triad-reference.mjs';
const b=resolve(import.meta.dirname,'../research/liuyao-b03-triad-clause'),w=resolve(b,'../../..'),table=JSON.parse(readFileSync(resolve(b,'FULL_CLAUSE.json'),'utf8')),checks=[],declarations=[],vectors=[];const c={};c.window=c;vm.createContext(c);vm.runInContext(readFileSync(resolve(w,'v53/engine.js'),'utf8'),c);
const check=(name,fn)=>{fn();checks.push({name,ok:true});};
check('162 ternary activity declarations keep exact-two pass,zero/one fail,three and unknown unresolved across six named groups',()=>{
 for(const group of table.groups)for(let i=0;i<27;i++){
  let n=i;const members=group.members.map(branch=>{const active=[false,true,null][n%3];n=Math.floor(n/3);return{branch,active};});
  const x=inspect({system,groupID:group.id,members}),active=members.filter(x=>x.active===true).length,unknown=members.some(x=>x.active===null);
  assert.equal(x.localPremisePass,unknown||active===3?null:active===2);assert.equal(x.sourceFormation,null);assert.equal(x.practicalOutcome,null);
  assert.equal(x.sourceRaisedMemberCoordinate,!unknown&&active===2?members.find(x=>!x.active).branch:null);declarations.push(x);
 }
 assert.equal(declarations.length,162);assert.equal(declarations.filter(x=>x.localPremisePass===true).length,18);assert.equal(declarations.filter(x=>x.localPremisePass===false).length,24);
});
check('Four mechanical Qian vectors reproduce source-coordinate motion cases with four actual HHC hexNumber calls',()=>{
 const definitions=[{values:[7,7,7,7,7,7],count:0,changed:1},{values:[9,7,7,7,7,7],count:1,changed:44},{values:[9,7,9,7,7,7],count:2,changed:6},{values:[9,7,9,7,9,7],count:3,changed:64}];
 const baseNumber=c.HHC_ENGINE.hexNumber(definitions[0].values);assert.equal(baseNumber,1);
 for(const [i,d]of definitions.entries()){
  const context={darkActivityByLine:Object.fromEntries(d.values.flatMap((v,k)=>[7,8].includes(v)?[[String(k+1),false]]:[]))},x=primary(d.values,context),z=x.groups.find(g=>g.groupID==='water-trine').witnesses[0];
  assert.deepEqual(z.lines,[5,1,3]);assert.equal(z.knownActiveCount,d.count);assert.equal(z.localPremisePass,d.count===3?null:d.count===2);assert.equal(z.raisedLine,d.count===2?5:null);
  assert.equal(x.chart.primary.number,baseNumber);const changed=i===0?baseNumber:c.HHC_ENGINE.hexNumber(d.values.map(v=>v===9?8:v===6?7:v));assert.equal(changed,d.changed);assert.equal(x.chart.changed.number,changed);
  vectors.push({kind:'editorial-mechanical-test-vector;notprintedsourcecast',values:d.values,declaredDarkActivity:context.darkActivityByLine,actualHHCPrimaryNumber:baseNumber,actualHHCChangedNumber:changed,sourceWitness:z});
 }
});
check('Static glyph is not silently equated with confirmed inactivity; dark status must be declared',()=>{
 const x=primary([9,7,9,7,7,7]),z=x.groups.find(g=>g.groupID==='water-trine').witnesses[0];assert.equal(z.localPremisePass,null);assert.equal(z.unknownActiveCount,1);assert.equal(z.raisedLine,null);
 const y=primary([9,7,9,7,7,7],{darkActivityByLine:{5:true}}).groups.find(g=>g.groupID==='water-trine').witnesses[0];assert.equal(y.knownActiveCount,3);assert.equal(y.localPremisePass,null);
 assert.throws(()=>primary([9,7,9,7,7,7],{darkActivityByLine:{1:true}}));assert.throws(()=>primary([7,7,7,7,7,7],{monthBranch:'子'}));
});
check('Previous >=2 operational gate is explicitly superseded for three-mover interpretation; old source files preserved',()=>{
 const prior=old([9,7,9,7,9,7]).groups.find(g=>g.id==='water-trine');assert.equal(prior.preliminaryGate,'structural-prerequisites-present');
 assert.equal(vectors[3].sourceWitness.status,'three-active-not-addressed-here');assert.equal(vectors[3].sourceWitness.localPremisePass,null);
 const previous=JSON.parse(readFileSync(resolve(w,'v53/research/liuyao-b03-volume4/TRIAD_TABLES.json'),'utf8'));assert(previous.literalBoundedReading.endsWith('刑合得成'));assert(table.literalReading.includes('刑合得一爻起'));
});
check('Missing distinct members,strict frames and copies cannot fabricate a source formation or consumer result',()=>{
 const base={system,groupID:'water-trine',members:[{branch:'申',active:true},{branch:'子',active:true},{branch:'辰',active:false}]};
 const bad=inspect({...base,members:[base.members[0],base.members[1],base.members[1]]});assert.equal(bad.completeDistinctMembership,false);assert.equal(bad.localPremisePass,false);
 const x=inspect(base);x.members[0].branch='亥';assert.equal(inspect(base).members[0].branch,'申');
 for(const input of[{...base,groupID:'all'},{...base,system:'B02'},{...base,members:[]},{...base,month:'子'}])assert.throws(()=>inspect(input));
 const html=readFileSync(resolve(w,'v53/Huyen_Hoc_Cac.html'));assert.equal(html.length,707411);assert(!html.includes(Buffer.from(system)));assert(html.equals(readFileSync(resolve(w,'Huyen_Hoc_Cac.html'))));assert(html.equals(readFileSync(resolve(w,'v53/site/index.html'))));
});
writeFileSync(resolve(w,'v53/qa/liuyao-b03-triad-clause/REFERENCE_RESULTS.json'),JSON.stringify({date:'2026-10-28',checks,declarations,vectors,summary:{declarationContexts:162,pass:18,fail:24,unknown:120,mechanicalVectors:4,printedSourceCastsNew:0,actualHHCHexNumberCalls:4,actualIztroCalls:0,oldOperationalGateComparedOnce:true,fullSourceFormationImplemented:false,consumerChanged:false}},null,2)+'\n');console.log(JSON.stringify({checksPassed:checks.length,declarations:162,vectors:4,actualHHCHexNumberCalls:4}));
