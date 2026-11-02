import {readFile,writeFile,mkdir} from 'node:fs/promises';
import {createHash} from 'node:crypto';import vm from 'node:vm';
import assert from 'node:assert/strict';import {resolve} from 'node:path';
import {listMaterialCases,sourceContexts,materialEvidence,motionEvidence,inspectExternal} from '../research/meihua-external/external-reference.mjs';
import {analyze} from '../research/meihua-conditions/conditions-reference.mjs';
const root=resolve(import.meta.dirname,'..'),base=resolve(root,'research/meihua-external'),qa=resolve(root,'qa/meihua-external');
const json=async p=>JSON.parse(await readFile(p,'utf8')),sha=b=>createHash('sha256').update(b).digest('hex');
const checks=[];function pass(name,detail){checks.push({name,ok:true,detail});console.log('PASS',name);}
await mkdir(qa,{recursive:true});
const manual=await json(resolve(base,'MANUAL_READINGS.json')),index=await json(resolve(root,'research/meihua/EXTRACTED_PAGES.json'));
assert.equal(sha(await readFile(resolve(base,manual.sourcePDF))),manual.sourcePDFSHA256);
assert.equal(index.pages.length,214);
for(const r of manual.records){const b=await readFile(resolve(base,r.image));assert.equal(sha(b),r.imageSHA256);assert.equal(sha(b),index.pages.find(x=>x.pdfPage===r.pdfPage).sha256);}
assert.deepEqual(manual.records.map(r=>r.pdfPage),Array.from({length:42},(_,i)=>103+i));
assert.equal(manual.records.filter(r=>r.kind==='content').length,41);
assert.equal(manual.records.filter(r=>!r.expandedEarlierReading).length,27);
assert.equal(manual.records.at(-1).kind,'endleaf');assert.equal(manual.allClausesTranscribed,false);
pass('42boundedvisualrecords retain originalPDF/derivative identity:41content,27newcontent,14expandedcontent+1endleaf;0HTTP/0renders');

const units=await json(resolve(base,'UNIT_MAP.json')),digital=await json(resolve(root,'research/meihua-reading/DIGITAL_UNIT_DISPOSITIONS.json'));
assert.equal(units.units.length,26);assert.equal(units.lastContentPDFPage,143);assert.equal(units.endleafPDFPage,144);
assert.equal(new Set(units.units.flatMap(u=>u.evidencePDFPages)).size,41);
const digitalsource=await readFile(resolve(root,'research/meihua/volume-三.wiki'));
for(const u of units.units){const d=digital.records.find(d=>d.id===u.id);assert.equal(d.heading,u.heading);assert.equal(d.sourceSliceSHA256,u.digitalSourceSliceSHA256);assert.equal(u.wholeUnitApplied,false);
 assert.equal(sha(digitalsource),d.sourceFileSHA256);assert.equal(sha(Buffer.from(Array.from(digitalsource.toString('utf8')).slice(d.start,d.end).join(''))),d.sourceSliceSHA256);}
pass('26pinned digital units link all41physicalcontentpages,with143lasttext/144endleaf;fullclausecollation stays open');

const cases=listMaterialCases(),contexts=sourceContexts();assert.equal(cases.length,13);
assert.ok(cases.every(c=>!c.automaticObjectRecognition&&!c.empiricalEffectEstablished&&c.numericWeight===null));
assert.equal(contexts.tenResponseCount,10);assert.equal(contexts.tenResponseCategories.length,10);
assert.equal(new Set(contexts.tenResponseCategories.map(c=>c.heading)).size,10);
assert.deepEqual(contexts.tenResponseCategories.map(c=>c.heading),['正應','互應','變應','方應','日應','刻應','外應','天時應','地理應','人事應']);
const opening=digitalsource.toString('utf8').match(/蓋十應之說，有([^。]+)/)[1];
assert.equal(contexts.tenResponseCategories.filter(c=>opening.includes(c.heading)).length,9);assert.equal(opening.includes('方應'),false);
assert.equal(contexts.separateNumberedActionRows.count,10);assert.equal(contexts.volume2ElevenResponseGroupsUnchanged,true);
pass('13bounded material contrasts;ten physicalresponse names versusnine in digitalopening stay distinct fromtenactionrows andvolume2eleven-groups');

const c={};c.window=c;vm.createContext(c);for(const f of ['engine.js','meihua.js'])vm.runInContext(await readFile(resolve(root,f),'utf8'),c);
const trigramElements=[null,'Kim','Kim','Hỏa','Mộc','Mộc','Thủy','Thổ','Thổ'];
const trigramByElement={Kim:1,Hỏa:3,Mộc:4,Thủy:6,Thổ:7};
let actualCastCases=0,matchedMaterialClauses=0;
for(const source of cases)for(let body=1;body<=8;body++){
 const cast=c.HHC_MEIHUA.compose(body,1,1),before=JSON.stringify(cast);
 const observed={id:'external-material',trigram:trigramByElement[source.otherElement],observed:'Explicit manual source-case observation',caseId:source.id,externalState:'unknown'};
 const r=inspectExternal(cast,{subject:'planning',observations:[observed]});
 const evidence=r.evidence[0].material,applicable=trigramElements[body]===source.bodyElement;
 assert.equal(evidence.applicable,applicable);assert.equal(evidence.historicalQualification,applicable?source.historicalQualification:null);
 assert.equal(evidence.printedBoundedPhrase,applicable?source.printedBoundedPhrase:null);
 const expected=analyze(cast,{subject:'planning',observations:[{id:observed.id,trigram:observed.trigram,observed:observed.observed}]});
 assert.deepEqual(r.symbolic,expected);assert.equal(r.materialQualificationsAppliedToGraph,false);
 assert.equal(r.limits.numericWeight,null);assert.equal(r.limits.finalVerdict,null);assert.equal(r.limits.predictedDate,null);
 assert.equal(JSON.stringify(cast),before);actualCastCases++;if(applicable)matchedMaterialClauses++;
}
assert.equal(actualCastCases,104);assert.equal(matchedMaterialClauses,22);
pass('104actualcast/context combinations gate13materialclauses by explicit body and preserve the symbolicgraph exactly',{actualCastCases,matchedMaterialClauses});

const grade=id=>materialEvidence({bodyElement:'Kim',caseId:id});
assert.equal(grade('large-fire').historicalQualification,'stronger-asserted-control');
assert.equal(grade('small-fire').historicalQualification,'small-adverse-qualification');
assert.equal(grade('fire-colour-form').historicalQualification,'literal-control-not-asserted');
assert.equal(new Set(['large-fire','small-fire','fire-colour-form'].map(id=>grade(id).relationToBody)).size,1);
const metal=id=>materialEvidence({bodyElement:'Mộc',caseId:id});
assert.equal(metal('noncutting-metal').historicalQualification,'literal-cutting-not-asserted');
assert.equal(metal('cutting-metal').historicalQualification,'stronger-asserted-control');
assert.equal(metal('noncutting-metal').relationToBody,metal('cutting-metal').relationToBody);
assert.equal(grade('soil-metal').relationToBody,grade('pottery-metal').relationToBody);
assert.notEqual(grade('soil-metal').historicalQualification,grade('pottery-metal').historicalQualification);
pass('Threefiregrades,cutting/noncuttingmetal andsoil/pottery have identicalsymbolicrelations butdistinct historicalmaterial qualifications');

let paceCases=0;
for(const externalState of ['still','carried-or-moving','unknown'])for(const observerState of ['seated','walking','standing','unknown']){
 const r=motionEvidence({externalState,observerState});
 assert.equal(r.combinedPace,null);assert.equal(r.predictedDate,null);assert.equal(r.numericalMultiplier,null);assert.equal(r.combinedPriorityResolved,false);
 assert.equal(r.observationsComplete,externalState!=='unknown'&&observerState!=='unknown');paceCases++;
}
assert.equal(paceCases,12);
const contradictory=motionEvidence({externalState:'still',observerState:'walking'});
assert.equal(contradictory.externalQualifier,'later-or-not-yet-apparent');assert.equal(contradictory.observerQualifier,'faster');assert.equal(contradictory.combinedPace,null);
assert.equal(motionEvidence({observerState:'standing'}).observerQualifier,'intermediate');
pass('12motion/observer combinations retain separate and conflictingqualifiers;standing is not 0.5 and no datetime is calculated');

const cast=c.HHC_MEIHUA.compose(1,1,1),silent=inspectExternal(cast,{subject:'dining'});
assert.equal(silent.evidence.length,0);assert.equal(silent.noExternalObservationInvented,true);
assert.equal(silent.sourceRolePolicy,'general-static-body-moving-use');
assert.equal(silent.alternativeLocalPoliciesNotApplied.length,3);
const weather=inspectExternal(cast,{subject:'weather',observations:[{id:'external-water',trigram:6,observed:'Explicit water observation',caseId:'true-water-fire'}]});
assert.equal(weather.symbolic.bodyUseApplicable,false);assert.equal(weather.evidence[0].material.applicable,false);
assert.equal(weather.evidence[0].material.reason,'subject-does-not-divide-body-use');
assert.equal(weather.evidence[0].material.historicalQualification,null);
assert.equal(materialEvidence({bodyElement:'Kim'}).missing,true);
pass('Quietcontext inventsnothing;weather stays outside body/use;three local role policies never silently replace the released policy');

const observation={id:'external-fire',trigram:3,observed:'A manually selected candle',caseId:'small-fire'};
for(const o of [{...observation,trigram:6},{...observation,caseId:'constructor'},{...observation,observed:''},{...observation,score:1},{...observation,externalState:'moving-fast'}])assert.throws(()=>inspectExternal(cast,{subject:'planning',observations:[o]}));
for(const options of [{subject:'planning',date:'2026-10-27'},{subject:'planning',observerState:'standing-half'},{subject:'planning',observations:[observation,{...observation}]}])assert.throws(()=>inspectExternal(cast,options));
for(const value of [null,[],{bodyElement:'土'},{bodyElement:'Kim',caseId:'__proto__'},{bodyElement:'Kim',caseId:'small-fire',weight:0.5}])assert.throws(()=>materialEvidence(value));
for(const value of [null,[],{externalState:'constructor'},{observerState:'__proto__'},{date:'tomorrow'}])assert.throws(()=>motionEvidence(value));
const altered=JSON.parse(JSON.stringify(cast));altered.changedUse.n=8;assert.throws(()=>inspectExternal(altered,{subject:'planning'}));
pass('Unestablishedcase/trigram,motion,date,weight,duplicateIDs and inconsistentactualcast are rejected');

cases[0].examples.push('test mutation');contexts.rolePolicies[0].policy='modified';
assert.equal(listMaterialCases()[0].examples.includes('test mutation'),false);assert.notEqual(sourceContexts().rolePolicies[0].policy,'modified');
let first=inspectExternal(cast,{subject:'planning',observations:[observation]});first.evidence[0].material.evidencePDFPages.push(999);
assert.equal(inspectExternal(cast,{subject:'planning',observations:[observation]}).evidence[0].material.evidencePDFPages.includes(999),false);
pass('Returnedsourcecases,contexts and evidence are isolated from caller mutation');

const tai=c.HHC_MEIHUA.compose(8,1,1);assert.equal(tai.primary,11);assert.equal(tai.changed,46);
const ding=c.HHC_MEIHUA.compose(3,5,6),heng=c.HHC_MEIHUA.compose(4,5,1);
assert.equal(ding.primary,50);assert.equal(ding.changed,32);assert.equal(heng.primary,32);
const bits=x=>[...x.lower.bits,...x.upper.bits],different=bits(ding).flatMap((v,i)=>v===bits(heng)[i]?[]:[i+1]);
assert.deepEqual(different,[6]);const possible=Array.from({length:6},(_,i)=>c.HHC_MEIHUA.compose(3,5,i+1).changed);
assert.equal(possible[5],32);assert.equal(possible[0],14);
const examples=await json(resolve(base,'WORKED_EXAMPLES.json'));
for(const e of examples.examples){const x=c.HHC_MEIHUA.compose(e.upper,e.lower,e.moving);assert.equal(x.primary,e.main);assert.equal(x.changed,e.target);assert.equal(e.narrativeOutcomeValidated,false);}
assert.equal(examples.researchCorrection.status,'hypothesis-rejected-before-publication');
pass('Two newly inspected printed examples use actualengine:泰11.1→46 and鼎50.6→32;provisionaltwo-linehypothesis rejected',{dingSingleLineTargets:possible});

const variants=await json(resolve(base,'VARIANTS_AND_GAPS.json'));assert.equal(variants.records.length,7);
assert.equal(variants.records.find(r=>r.id==='dining-verse-prose').printedProse,'飲食有阻');
assert.equal(variants.wholeBookApplied,false);
const html=await readFile(resolve(root,'Huyen_Hoc_Cac.html'));
assert.equal(html.length,703410);assert.equal(sha(html),'3800162854742c915d60f0051c65cadb0eb9a1c803f9f937bf1b6a593c96d268');
for(const word of ['external-reference','MATERIAL_PREMISES','CONTEXT_PREMISES','VARIANTS_AND_GAPS'])assert.equal(html.includes(Buffer.from(word)),false);
pass('Seven text/contextissues remain unresolved;private historicalreference is absentfrom703410byte releasedHTML');

const out={schema:'hhc.meihua.external.qa.v1',checks,summary:{sourcePageRecords:42,contentPages:41,newContentPageRecords:27,physicalUnitLinks:26,materialClauses:13,actualCastContexts:actualCastCases,matchedMaterialClauses,motionContexts:paceCases,newPrintedArithmeticExamples:2,openVariants:7,newHTTPResponses:0,newDerivatives:0,consumerChanged:false,predictiveAccuracyEstablished:false,wholeBookApplied:false},htmlSHA256:sha(html)};
await writeFile(resolve(qa,'ENGINE_RESULTS.json'),JSON.stringify(out,null,2)+'\n');console.log(JSON.stringify(out.summary));
