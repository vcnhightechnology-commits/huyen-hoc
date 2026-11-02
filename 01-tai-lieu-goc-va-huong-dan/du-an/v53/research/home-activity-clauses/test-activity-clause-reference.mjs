import fs from 'node:fs';
import path from 'node:path';
import assert from 'node:assert/strict';
import {fileURLToPath} from 'node:url';
import {createHash} from 'node:crypto';
import {SOURCE_ID,FRAME_ID,sourceActivityClause} from './activity-clause-reference.mjs';
const root=path.dirname(fileURLToPath(import.meta.url));
const read=n=>JSON.parse(fs.readFileSync(path.join(root,n),'utf8').replace(/^\uFEFF/,''));
const e=read('EXPECTED_BEFORE_IMPLEMENTATION.json'),base={sourceID:SOURCE_ID,frameID:FRAME_ID};
let manual=0,contexts=0,invariants=0,badFrames=0,missingPremises=0,rejected=0;
function check(o) {
 const r=sourceActivityClause({...base,...o});assert.ok(r);
 for(const k of ['overallSuitability','permissionToBuild','harmPrediction','calendarDate'])assert.equal(r[k],null);
 assert.equal(r.sourceEfficacyValidated,false);assert.equal(r.explicitLocalException,r.localAvoidance===false);
 invariants+=6;return r;
}
for(const c of e.manualCases){assert.equal(check(c.input).localAvoidance,c.expectedLocalAvoidance,c.id);manual++;}
for(const kind of ['dasha','leiting'])for(const starPosition of ['central-palace','other-palace','unknown'])
 for(const locationRole of ['hall-middle','hall-other','outside-hall','unknown'])for(const activity of ['repair-hall','music-or-noisy-guests','modern-kitchen','other']) {
  const r=check({clauseID:'white-tiger',activity,kind,starPosition,locationRole});contexts++;
  if(starPosition!=='central-palace'||locationRole==='unknown')assert.equal(r.localAvoidance,null);
 }
for(const dayKind of ['regular','lateral','unknown'])for(const beneficPresent of [true,false,null])
 for(const activity of ['start-building','all-miscellaneous-work','coffin','other']){
 check({clauseID:'four-waste',activity,dayKind,beneficPresent});contexts++;
 }
for(const markerStatus of [true,false,null])for(const beneficPresent of [true,false,null])
 for(const activity of ['start-building','erect-pillars','make-fire-drying-kiln','build-thatch-hut','modern-gas-stove','other']) {
  const r=check({clauseID:'wantong-fire',activity,markerStatus,beneficPresent});contexts++;
  if(markerStatus===true&&activity==='start-building')assert.equal(r.localAvoidance,true);
 }
for(const markerStatus of [true,false,null])for(const voice of ['official-calendar','reported-other-almanacs'])
 for(const activity of ['thatch-cover','cover-house','cover-hut','cover-boat','other']) {
 check({clauseID:'tianhuo',activity,markerStatus,voice});contexts++;
 }
for(const markerStatus of [true,false,null])for(const beneficPresent of [true,false,null])
 for(const activity of ['inherit-title','receive-investiture','take-office','submit-memorial','burial','start-building','other']){
 check({clauseID:'received-death',activity,markerStatus,beneficPresent});contexts++;
 }
for(const markerStatus of [true,false,null])for(const huangdaoQualified of [true,false,null])
 for(const activity of ['travel','seek-office','submit-memorial','present-petition','other']){
 const r=check({clauseID:'tiange',activity,markerStatus,huangdaoQualified});contexts++;
 if(huangdaoQualified!==true)assert.equal(r.localAvoidance,null);
 }
for(const markerStatus of [true,false,null])for(const marriageDayQualified of [true,false,null])
 for(const activity of ['marry-wife','admit-household-member','family-compatibility','other']){
 const r=check({clauseID:'renge',activity,markerStatus,marriageDayQualified});contexts++;
 if(marriageDayQualified!==true)assert.equal(r.localAvoidance,null);
 }
for(const clauseID of ['fire-ge','water-ge'])for(const markerStatus of [true,false,null])for(const activity of ['smelt-or-kiln-stove','open-pond','release-fish','other']){
 assert.equal(check({clauseID,activity,markerStatus}).localAvoidance,null);contexts++;
 }
const typical={...base,...e.manualCases[0].input};
for(const x of [null,[],{},'2026-10-29',{...typical,sourceID:'P08'},{...typical,frameID:'modern-floor-plan'},
 {...typical,frameID:'gregorian-calendar'},{...typical,date:'2026-10-29'},{...typical,timeZone:'Asia/Bangkok'},
 {...typical,longitude:105},{...typical,kind:'dasha',floorArea:80},{...typical,dayGanzhi:'乙未'}]){
 assert.equal(sourceActivityClause(x),null);badFrames++;
}
for(const c of e.manualCases)for(const key of Object.keys(c.input)){
 const o={...base,...c.input};delete o[key];assert.equal(sourceActivityClause(o),null);missingPremises++;
}
for(const [key,value] of [['kind','white-tiger'],['starPosition',true],['locationRole','geometric-centre'],['activity',null]]){
 assert.throws(()=>sourceActivityClause({...typical,[key]:value}));rejected++;
}
for(const key of ['markerStatus','beneficPresent'])for(const value of ['true',1,undefined]){
 assert.throws(()=>sourceActivityClause({...base,clauseID:'wantong-fire',activity:'start-building',markerStatus:true,beneficPresent:true,[key]:value}));rejected++;
}
const freeze=read('PREIMPLEMENTATION_FREEZE.json');assert.equal(freeze.implementationExists,false);
for(const x of freeze.files){const b=fs.readFileSync(path.join(root,x.file));assert.equal(b.length,x.bytes);assert.equal(createHash('sha256').update(b).digest('hex'),x.sha256);}
console.log(JSON.stringify({passed:true,groups:10,manualSourceCases:manual,finiteContexts:contexts,nonPredictionInvariants:invariants,unsupportedFramesRejected:badFrames,missingPremisesReturnedNull:missingPremises,invalidInputsRejected:rejected,preimplementationFilesUnchanged:freeze.files.length,implementedClauseGroups:7,fireWaterPredicatesImplemented:false,newCalendarEngineCalls:0,newChartEngineCalls:0,wholeWorkApplied:false}));
