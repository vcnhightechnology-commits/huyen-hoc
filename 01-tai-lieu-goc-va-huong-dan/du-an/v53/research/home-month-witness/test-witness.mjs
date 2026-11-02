import{readFileSync,writeFileSync}from'node:fs';
import{resolve,basename}from'node:path';
import{createHash}from'node:crypto';
import assert from'node:assert/strict';
import{MONTH_COMPARISON_SYSTEM as system,compareMonthGodWitnesses as compare}from'./monthly-witness-reference.mjs';
const b=import.meta.dirname,w=process.cwd(),read=p=>JSON.parse(readFileSync(p,'utf8').replace(/^\uFEFF/,'')),hash=p=>createHash('sha256').update(readFileSync(p)).digest('hex');
const manual=read(resolve(b,'MANUAL_WITNESS_TABLE.json')),expected=read(resolve(b,'MANUAL_EXPECTATIONS.json')),actual=read(resolve(b,'ACTUAL_RUNTIME.json')),freeze=read(resolve(b,'TRANSCRIPTION_FREEZE.json')),checks=[];
const check=(name,fn)=>{fn();checks.push({name,ok:true});};
const input=(god,monthOrdinal,monthBasis='declared-source-ordinal')=>({system,god,monthOrdinal,monthBasis});
check('Manual84-cell grid, expected contrasts, eight native crops and13retained HTTP bodies frozen before successful batch',()=>{
 for(const x of freeze.files){const p=resolve(b,basename(x.file));assert.equal(hash(p),x.sha256);assert.equal(readFileSync(p).length,x.bytes);}
 assert.equal(hash(resolve(b,'TRANSCRIPTION_FREEZE.json')),actual.freezeSHA256);assert(Date.parse(freeze.frozenAt)<=Date.parse(actual.executedAt));assert(freeze.originalManualAndExpectedDataUnchanged);
 const req=read(resolve(b,'REQUESTS.json'));assert.equal(req.length,13);for(const x of req){assert.equal(x.status,200);assert(x.standardTLSValidation);assert.equal(hash(resolve(b,x.file)),x.sha256);assert.equal(readFileSync(resolve(b,x.file)).length,x.bytes);}
});
check('84literal comparisons retain77equal, five centre-stem differences and two unresolved P08 cells',()=>{
 let same=0,diff=0,unknown=0;
 for(const row of manual.records)for(const cell of row.cells){const x=compare(input(row.id,cell.monthOrdinal)),saved=actual.comparisons.find(r=>r.right.god===row.id&&r.right.monthOrdinal===cell.monthOrdinal);assert.deepEqual(x,saved);assert.equal(x.right.literal,cell.literal);
  if(x.status==='same-literal')same++;else if(x.status==='different-literal')diff++;else unknown++;
 }
 assert.deepEqual([same,diff,unknown],[77,5,2]);
 for(const e of expected.explicitDifferences){const x=compare(input(e.god,e.month));assert.equal(x.left.literal,e.P08);assert.equal(x.right.literal,e.ITKC);assert.equal(x.left.coordinateType,'stem');assert.equal(x.right.coordinateType,'centre');assert.equal(x.centreStemReplacement,null);}
 for(const e of expected.P08OpenCells){const x=compare(input(e.god,e.month));assert.equal(x.left.literal,null);assert.equal(x.right.literal,'乙');assert.equal(x.right.coordinateType,'stem');assert.equal(x.status,'not-comparable');assert.equal(x.automaticEmendation,null);}
});
check('Image month-de fourth cell is Geng while ITKC/WSdigital both read Yin; duplicate wording not independent corroboration',()=>{
 const digital=read(resolve(b,'DIGITAL_TABLE_EXTRACTS.json'));assert.equal(digital.files.length,2);
 for(const file of digital.files){let different=0;
  for(const row of manual.records){const r=file.records.find(x=>x.title===row.title);assert.equal(r.cells.length,12);
   for(let i=0;i<12;i++)if(r.cells[i]!==row.cells[i].literal){different++;assert.equal(row.id,'yue-de');assert.equal(i,3);assert.equal(r.cells[i],'寅');assert.equal(row.cells[i].literal,'庚');}
  }
  assert.equal(different,1);
 }
 assert.deepEqual(digital.files[0].records,digital.files[1].records);assert.equal(digital.independentWitnessCountForSameDigitalReadings,0);
});
check('Four unsupported bases and missing month do not select calendar rows, centres or trigrams',()=>{
 let n=0;for(const basis of ['calendar-date','birth-year','door-direction','unknown'])for(const row of manual.records)for(let month=1;month<=12;month++){const x=compare(input(row.id,month,basis));assert.equal(x.left.literal,null);assert.equal(x.right.literal,null);assert.equal(x.status,'not-comparable');n++;}assert.equal(n,336);
 for(const row of manual.records){const x=compare(input(row.id,null));assert.equal(x.status,'not-comparable');assert.equal(x.right.literal,null);}
 for(const month of [2,5,8,11])assert.equal(compare(input('tian-de',month)).right.coordinateType,'trigram');
});
check('Explicit input domains, isolated results and null downstream claims prevent silent witness promotion',()=>{
 const base=input('yue-cai',2);
 for(const x of [null,{},[],{...base,system:'all-sources'},{...base,god:'month-wealth'},{...base,monthOrdinal:0},{...base,monthOrdinal:13},{...base,monthOrdinal:'2'},{...base,monthBasis:'solar-term'},{...base,chooseBetter:true},Object.create(base)])assert.throws(()=>compare(x),TypeError);
 const x=compare(base);x.left.unresolvedCandidates.push('假');assert(!compare(base).left.unresolvedCandidates.includes('假'));
 for(const x of actual.comparisons)for(const k of ['preferredWitness','automaticEmendation','calendarMonthAdapter','trigramBranchReplacement','centreStemReplacement','exactBearingAssignment','overallRecommendation'])assert.equal(x[k],null);
});
check('Two successful compass calls plus two from failed mapping batch are disclosed; no additional engine execution in replay',()=>{
 const f=read(resolve(b,'FAILED_BATCH_AUDIT.json'));assert.equal(f.actualHHCCompassCallsBeforeFailure,2);assert.equal(f.completedLiteralComparisonsBeforeFailure,24);assert.equal(f.failedBatchCountedAsPassing,false);
 for(const x of f.retainedPreFixFiles){const p=resolve(b,x.file);assert.equal(hash(p),x.sha256);assert.equal(readFileSync(p).length,x.bytes);}
 const before=read(resolve(b,'pre-fix/TRANSCRIPTION_FREEZE.json'));for(const x of before.files){const name=basename(x.file),old=['monthly-witness-reference.mjs','run-actual-once.mjs'].includes(name),p=resolve(b,old?'pre-fix/'+name:name);assert.equal(hash(p),x.sha256);}
 assert.equal(actual.summary.successfulRuntimeBatches,1);assert.equal(actual.summary.previousFailedRuntimeBatches,1);assert.equal(actual.summary.totalActualHHCCompassCallsIncludingFailure,4);
 assert.deepEqual(actual.mountainProbes.map(x=>[x.actual.selected.name,x.actual.selected.center]),[['Ất',105],['Sửu',30]]);assert.equal(actual.summary.realSourceCellExactBearingsAssigned,0);
});
check('Stable consumer and original P08table preserve their bytes',()=>{
 for(const x of read(resolve(b,'SOURCE_IDENTITIES.json')).retainedFiles){const p=resolve(w,x.file);assert.equal(hash(p),x.sha256);assert.equal(readFileSync(p).length,x.bytes);}
 for(const p of ['Huyen_Hoc_Cac.html','v53/Huyen_Hoc_Cac.html','v53/site/index.html'])assert.equal(hash(resolve(w,p)),'549cb415c1a7785e92be25b407d965ea0abd4d3affc54696b784f84d87601857');
});
const result={date:'2026-10-29',checks,summary:{completeChecks:7,manualCells:84,sourceComparisonsReplayed:84,sameLiterals:77,differentLiterals:5,P08Unresolved:2,unknownBasisFrames:336,missingMonthFrames:7,institutionDigitalImageDiscrepancies:1,wikisourceDigitalImageDiscrepancies:1,distinctFacsimileDiscrepancyCoordinates:1,retainedHTTP200Bodies:13,newHHCCompassCallsThisTest:0,totalActualCompassCallsIncludingPriorFailure:4,successfulBatchCompassCalls:2,failedBatchCompassCalls:2,successfulRuntimeBatches:1,failedRuntimeBatches:1,consumerChanged:false,wholeCatalogueCompleted:false}};
if(!process.argv.includes('--no-write'))writeFileSync(resolve(b,'TEST_RESULTS.json'),JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify(result.summary));
