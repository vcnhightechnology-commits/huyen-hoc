import assert from 'node:assert/strict';
import vm from 'node:vm';
import {readFileSync,writeFileSync} from 'node:fs';
import {resolve} from 'node:path';
import {createHash} from 'node:crypto';
import {ROOM_LINE_SYSTEM as system,sourceCarryPair as carry,sourceLastFiveRoomLines as lines} from './source-room-lines.mjs';
const b=import.meta.dirname,w=resolve(b,'../..'),ctx={};ctx.window=ctx;vm.createContext(ctx);
vm.runInContext(readFileSync(resolve(w,'v53/engine.js'),'utf8'),ctx);
const checks=[],coordinates=[];const check=(name,fn)=>{fn();checks.push({name,ok:true});};
const unit=(id,sourceSide,workKind='new')=>({id,sourceSide,workKind});
const base=units=>({system,frame:'declared-source-counted-room-units',tailComplete:true,sourceOrderEstablished:true,distinctSourceUnitsEstablished:true,gateLine:1,units});
check('Two literal source relocation examples retain origin before destination without assigning final gate positions',()=>{
 assert.deepEqual(carry({system,originLabel:'乾',destinationLabel:'巽'}).carriedPair,[1,0]);
 assert.deepEqual(carry({system,originLabel:'坤',destinationLabel:'艮'}).carriedPair,[0,1]);
 assert.deepEqual(carry({system,originLabel:null,destinationLabel:'艮'}).carriedPair,[null,1]);
 assert.equal(carry({system,originLabel:'乾',destinationLabel:'巽'}).positionsAfterGateInsertion,null);
});
check('Ten and twenty declared source units discard all earlier units and keep five ordered units above the separately declared gate',()=>{
 for(const n of [5,10,20]){
  const units=Array.from({length:n},(_,i)=>unit('room-'+i,['east','north','west','south'][i%4],i%2?'repair':'new'));
  const out=lines(base(units));assert.deepEqual(out.selectedSourceUnitIDs,units.slice(-5).map(x=>x.id));
  assert.equal(out.omittedEarlierUnitIDs.length,n-5);assert.equal(out.linesBottomToTop.length,6);assert.equal(out.linesBottomToTop[0],1);
  assert.deepEqual(out.upperFiveLines,units.slice(-5).map(x=>['east','north'].includes(x.sourceSide)?1:0));
 }
 const units=Array.from({length:6},(_,i)=>unit('r'+i,i===0?'unknown':'east'));
 assert.equal(lines(base(units)).sixBitsKnown,true);assert.equal(lines(base(units.slice(1))).sixBitsKnown,true);
});
check('Repair and new count one declared unit each, while duplicate IDs and an unknown count unit never become multiple rooms',()=>{
 const units=Array.from({length:5},(_,i)=>unit('r'+i,'east'));
 const repaired=units.map(x=>({...x,workKind:'repair'}));assert.deepEqual(lines(base(units)).linesBottomToTop,lines(base(repaired)).linesBottomToTop);
 assert.throws(()=>lines(base([...units,units[4]])));
 assert.equal(lines(base([...units.slice(0,4),unit('u','east','unknown')])).sourcePremisesReady,false);
 assert.equal(lines({...base(units),distinctSourceUnitsEstablished:null}).linesBottomToTop,null);
});
check('Fewer than five rooms do not borrow the relocation pair to manufacture a complete hexagram',()=>{
 for(let n=0;n<5;n++){
  const out=lines(base(Array.from({length:n},(_,i)=>unit('r'+i,'east'))));assert.equal(out.upperFiveLines,null);assert.equal(out.linesBottomToTop,null);assert.equal(out.initialPhaseWithFewerThanFiveRoomsImplemented,false);
 }
});
check('Declared room sides never classify diagonal measured sectors, floor counts or area; unknown current tail stays unknown',()=>{
 const units=Array.from({length:5},(_,i)=>unit('r'+i,i===4?'unknown':'east'));
 assert.deepEqual(lines(base(units)).linesBottomToTop,[1,1,1,1,1,null]);assert.equal(lines(base(units)).sixBitsKnown,false);
 for(const frame of ['modern-vertical-storeys','area-weighted','unknown'])assert.equal(lines({...base(units),frame}).linesBottomToTop,null);
 for(const field of ['tailComplete','sourceOrderEstablished','distinctSourceUnitsEstablished'])for(const v of [false,null])assert.equal(lines({...base(units),[field]:v}).linesBottomToTop,null);
 assert.equal(lines({...base(units),gateLine:null}).linesBottomToTop[0],null);
 assert.throws(()=>lines(base([...units.slice(0,4),unit('u','northeast')])));
});
check('Sixty-four actual HHC hexNumber calls verify bit encoding only, with independent Qian/Kun/Jiji/Weiji orientation anchors',()=>{
 for(let n=0;n<64;n++){
  const bits=Array.from({length:6},(_,i)=>(n>>i)&1),units=bits.slice(1).map((v,i)=>unit('r'+i,v?'east':'west'));
  const out=lines({...base(units),gateLine:bits[0]});assert.deepEqual(out.linesBottomToTop,bits);
  const values=out.linesBottomToTop.map(v=>v?7:8),actual=ctx.HHC_ENGINE.hexNumber(values);
  coordinates.push({bitsBottomToTop:bits.join(''),actualHHCHexagramNumber:actual,sourceHouseInterpretationValidated:false});
 }
 assert.deepEqual([...new Set(coordinates.map(x=>x.actualHHCHexagramNumber))].sort((a,b)=>a-b),Array.from({length:64},(_,i)=>i+1));
 for(const [bits,num]of [['111111',1],['000000',2],['101010',63],['010101',64]])assert.equal(coordinates.find(x=>x.bitsBottomToTop===bits).actualHHCHexagramNumber,num);
});
check('Gate is never automatically complemented, caller objects remain independent, and strict fields reject hidden calendar or outcome coercion',()=>{
 const x=base(Array.from({length:5},(_,i)=>unit('r'+i,'east'))),a=lines(x);
 assert.equal(a.gateLineSuppliedNotInferred,1);assert.equal(a.automaticGateComplement,null);assert.equal(a.sourceExchangeMethodCompleted,false);assert.equal(a.practicalOutcome,null);
 a.selectedSourceUnitIDs[0]='changed';a.linesBottomToTop[0]=0;assert.equal(lines(x).selectedSourceUnitIDs[0],'r0');assert.equal(lines(x).linesBottomToTop[0],1);
 for(const bad of [null,{},[],{...x,units:Array(5)},{...x,gateLine:'1'},{...x,outcome:'吉'},{...x,[Symbol('s')]:true},Object.create(x)])assert.throws(()=>lines(bad));
});
const out={date:'2026-10-28',checks,coordinates,summary:{completeChecks:7,sourcePrintedRelocationExamples:2,
 actualHHCHexNumberCalls:64,newCalendarChartCalls:0,newHHCDirectionsCalls:0,newIztroCalls:0,
 fullXuanKongExchangeMethodApplied:false,modernPlanAdapterImplemented:false,consumerChanged:false,wholeCatalogueCompleted:false},
 actualEngine:{file:'v53/engine.js',sha256:createHash('sha256').update(readFileSync(resolve(w,'v53/engine.js'))).digest('hex')}};
writeFileSync(resolve(b,'REFERENCE_RESULTS.json'),JSON.stringify(out,null,2)+'\n');console.log(JSON.stringify(out.summary));
