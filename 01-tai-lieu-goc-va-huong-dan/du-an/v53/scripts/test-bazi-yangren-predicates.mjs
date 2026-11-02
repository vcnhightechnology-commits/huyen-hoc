import {readFile,writeFile}from'node:fs/promises';import{resolve}from'node:path';import{createHash}from'node:crypto';import vm from'node:vm';import assert from'node:assert/strict';
import {auditSelectedPredicates as inspect}from'../research/bazi-yangren-conditions/predicate-reference.mjs';
const w=process.cwd(),r=resolve(w,'v53'),b=resolve(r,'research/bazi-yangren-conditions'),q=resolve(r,'qa/bazi-yangren-conditions'),read=async p=>JSON.parse(await readFile(p,'utf8')),sha=x=>createHash('sha256').update(x).digest('hex');
const matrix=await read(resolve(b,'PREDICATE_MATRIX.json')),sub=await read(resolve(b,'SELECTED_SUBCONTEXTS.json')),parent=await read(resolve(b,'CONTEXT_REVIEW.json'));
const system=matrix.system,ctx=(declaredFacts={},dayPillar=null,hourPillar=null)=>({system,dayPillar,hourPillar,declaredFacts}),row=(x,id)=>x.rows.find(r=>r.id===id),checks=[];
async function check(name,fn){await fn();checks.push({name,ok:true});}
await check('59 subcontexts exactly partition1180codepoints across8 previously mixed contexts, with shared consequent and all59 dispositions retained',()=>{
 assert.equal(sub.subcontexts.length,59);assert.equal(sub.selectedCodepoints,1180);assert.equal(matrix.rules.length,28);
 for(const id of sub.parentContexts){const old=parent.records.find(x=>x.id===id),units=sub.subcontexts.filter(x=>x.parentContext===id);assert.equal(units.map(x=>x.retainedDigitalText).join(''),old.text);
  assert.equal(units[0].digitalStartCodepoint,old.startCodepoint);assert.equal(units.at(-1).digitalEndCodepoint,old.endCodepoint);
  for(let i=1;i<units.length;i++)assert.equal(units[i-1].digitalEndCodepoint,units[i].digitalStartCodepoint);assert(units.every(x=>x.disposition));
 }
 assert.deepEqual(matrix.rules.find(x=>x.id==='natal-sha-blade-repeat').sourceSubcontextIDs,['YR-15-04','YR-15-05']);
 assert.equal(matrix.automaticPrecedenceEstablished,false);assert.equal(matrix.allConditionalRulesCompiled,false);
});
let ternaryContexts=0;
await check('81 declared-presence contexts agree with Boolean-completion oracle; unknown seal stays unknown and narrower opposite source claim never wins by array order',()=>{
 const keys=['sourceNatalBlade','sourceNatalSha','sourceNatalSeal','sourceLuckSha'],states=[false,true,null];
 function oracle(f,specific){const unknown=keys.filter(k=>f[k]===null),answers=[];
  for(let mask=0;mask<1<<unknown.length;mask++){const x={...f};unknown.forEach((k,i)=>x[k]=Boolean(mask&(1<<i)));answers.push(x.sourceNatalBlade&&!x.sourceNatalSha&&x.sourceLuckSha&&(!specific||x.sourceNatalSeal));}
  return answers.every(x=>x===answers[0])?answers[0]:null;
 }
 for(const a of states)for(const b of states)for(const c of states)for(const d of states){const f=Object.fromEntries(keys.map((k,i)=>[k,[a,b,c,d][i]])),out=inspect(ctx(f));
  assert.equal(row(out,'blade-no-sha-luck-sha').localPremisesMatch,oracle(f,false));assert.equal(row(out,'blade-seal-no-sha-luck-sha').localPremisesMatch,oracle(f,true));
  assert.equal(out.sourcePrecedenceEstablished,false);assert.equal(out.practicalOutcome,null);ternaryContexts++;
 }
 const overlap=inspect(ctx({sourceNatalBlade:true,sourceNatalSha:false,sourceNatalSeal:true,sourceLuckSha:true}));
 assert(overlap.opposedLocalClaims.some(x=>x.positiveRule==='blade-seal-no-sha-luck-sha'&&x.negativeRule==='blade-no-sha-luck-sha'&&x.moreSpecificQualificationCandidate&&!x.sourcePrecedenceEstablished));
 const unknownSeal=inspect(ctx({sourceNatalBlade:true,sourceNatalSha:false,sourceLuckSha:true}));assert.equal(row(unknownSeal,'blade-no-sha-luck-sha').localPremisesMatch,true);assert.equal(row(unknownSeal,'blade-seal-no-sha-luck-sha').localPremisesMatch,null);
 assert.equal(ternaryContexts,81);
});
await check('Unresolved 原帶傷官財星 AND/OR alternatives use consensus without silently fixing the source reading',()=>{
 for(const [officer,wealth,expected,alternatives]of[[true,false,null,[false,true]],[true,true,true,[true,true]],[false,false,false,[false,false]]]){
  const r=row(inspect(ctx({sourceNatalHurtingOfficer:officer,sourceNatalWealth:wealth,sourceYearLuckStarRepeat:true})),'original-stars-repeat-ambiguous');
  assert.equal(r.localPremisesMatch,expected);assert.deepEqual(r.alternativeMatches,alternatives);assert.equal(r.sourceReadingResolved,false);
 }
});
await check('官旺 and 無官 remain different predicates: present-but-weak fits neither route; neither unknown nor failed strength selects an else branch',()=>{
 const cases=[[false,true,false,false],[null,true,null,false],[false,null,false,null],[true,true,true,false],[null,false,null,true]];
 for(const [strong,present,a,b]of cases){const out=inspect(ctx({sourceBingDingLiXunFrameEstablished:true,sourceOfficerStrong:strong,sourceOfficerPresent:present}));
  assert.equal(row(out,'officer-strong-trine-route').localPremisesMatch,a);assert.equal(row(out,'officer-absent-trine-route').localPremisesMatch,b);assert.equal(out.practicalOutcome,null);
 }
 assert.throws(()=>inspect(ctx({sourceOfficerStrong:true,sourceOfficerPresent:false})),TypeError);
});
let hhcCalls=0;const runtime=[];
await check('Two previously read printed examples execute real HHC again for the new projection; exact day facts are known while many/strength/pattern/control remain unknown',async()=>{
 const code=await readFile(resolve(r,'engine.js'));assert.equal(sha(code),'39f08bd1887faca4d35f7ad415ebf596621010d530b489212774d5cbf99040e6');const c={};c.window=c;vm.createContext(c);vm.runInContext(code.toString(),c);
 const examples=await read(resolve(q,'SOURCE_EXAMPLES_PROBE.json'));
 for(const e of examples.sourceExamples){const chart=c.HHC_ENGINE.bazi(e.fixtureInput);hhcCalls++;const actual=Array.from(chart.pillars,p=>p.han);assert.deepEqual(actual,e.sourcePillars);
  const out=inspect(ctx({},actual[2],actual[3]));assert.equal(out.coordinateFacts.dayIsWuWu,true);assert.equal(out.coordinateFacts.listedDayBlade,true);
  assert.equal(row(out,'day-blade-coordinate').localPremisesMatch,true);assert.equal(row(out,'wu-wu-fire-many-route').localPremisesMatch,null);
  assert.equal(row(out,'other-pattern-priority').localPremisesMatch,null);assert.equal(out.strength,null);assert.equal(out.fullBladePatternEstablished,null);
  assert.equal(out.usefulGodSelected,null);assert.equal(out.practicalOutcome,null);assert.equal(out.healthResult,null);assert.equal(out.lifespan,null);
  runtime.push({sourceContainerPage:218,sourcePillars:e.sourcePillars,fixtureInput:e.fixtureInput,actualHHCPillars:actual,knownCoordinateFacts:out.coordinateFacts,
   sourceManyFirePremise:row(out,'wu-wu-fire-many-route').localPremisesMatch,sourceOtherPatternPriorityPremise:out.sourceOtherPatternRoutePremiseMatched,sourceOutcomeValidated:false});
 }
 assert.equal(hhcCalls,2);
});
await check('Missing facts are unknown, false blocks conjunction, explicit other-pattern premise only matches source route, and exact coordinates cannot be overridden',()=>{
 const empty=inspect(ctx());assert.equal(empty.coordinateFacts.listedDayBlade,null);assert(empty.rows.every(x=>x.localPremisesMatch===null));
 const falseFire=inspect(ctx({sourceYearMonthFireMany:false},'戊午',null));assert.equal(row(falseFire,'wu-wu-fire-many-route').localPremisesMatch,false);
 const noDay=inspect(ctx({sourceYearMonthFireMany:true}));assert.equal(row(noDay,'wu-wu-fire-many-route').localPremisesMatch,null);
 const other=inspect(ctx({sourceOtherPatternEstablished:true},'戊午',null));assert.equal(other.sourceOtherPatternRoutePremiseMatched,true);assert.equal(other.fullBladePatternEstablished,null);
 for(const input of[null,{},[],{...ctx(),system:'yangren'},ctx({sourceBodyStrong:undefined}),ctx({sourceBodyStrong:1}),ctx({hasQi:true}),ctx({listedDayBlade:false}),{...ctx(),dayPillar:undefined},{...ctx(),dayPillar:'甲丑'},ctx({[Symbol('x')]:true})])assert.throws(()=>inspect(input),TypeError);
 const f={sourceNatalBlade:true},input=ctx(f),x=inspect(input);x.declaredFacts.sourceNatalBlade=false;x.rows[0].sourceSubcontextIDs.push('fake');x.coordinateFacts.listedDayBlade=true;
 const y=inspect(input);assert.equal(y.declaredFacts.sourceNatalBlade,true);assert(!y.rows[0].sourceSubcontextIDs.includes('fake'));assert.equal(y.coordinateFacts.listedDayBlade,null);assert.deepEqual(f,{sourceNatalBlade:true});
});
const out={date:'2026-10-28',checks,summary:{selectedParentContexts:8,selectedSubcontexts:59,selectedCodepoints:1180,localPredicateAudits:28,coordinateFacts:6,declaredOnlyFacts:55,ternaryDeclarationContexts:ternaryContexts,
 actualNewHHCBaziCalls:hhcCalls,previouslyReadPrintedExamplesReexecuted:2,newSourcePages:0,newHTTPRequests:0,newOriginalContainers:0,expandedPreviouslyReadSourcePositions:8},runtime,
 sourceReadingAutomaticallyResolved:false,fullBladePatternClassifier:false,automaticStrengthMethodValidated:false,automaticPrecedenceEstablished:false,realPersonDeclaredFactsValidated:false,practicalOutcomesValidated:false,consumerChanged:false,wholeCatalogueCompleted:false};
await writeFile(resolve(q,'RESULTS.json'),JSON.stringify(out,null,2)+'\n');console.log(JSON.stringify({checks:checks.length,...out.summary}));
