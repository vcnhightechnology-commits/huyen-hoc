import {readFile,writeFile,mkdir} from 'node:fs/promises';import {createHash} from 'node:crypto';
import {resolve} from 'node:path';import vm from 'node:vm';import assert from 'node:assert/strict';
import {printedRows,lookupHexagram,lookupBits,derivePalace,tableFieldEvidence} from '../research/meihua-volume1/palace-reference.mjs';
const root=resolve(import.meta.dirname,'..'),base=resolve(root,'research/meihua-volume1'),qa=resolve(root,'qa/meihua-volume1');
const json=async p=>JSON.parse(await readFile(p,'utf8')),sha=b=>createHash('sha256').update(b).digest('hex');
const checks=[];function pass(name,detail){checks.push({name,ok:true,detail});console.log('PASS',name);}
await mkdir(qa,{recursive:true});
const index=await json(resolve(root,'research/meihua/EXTRACTED_PAGES.json')),baseline=await json(resolve(base,'SOURCE_BASELINE.json'));
assert.deepEqual(index.pages.map(r=>r.pdfPage),Array.from({length:232},(_,i)=>i+1));assert.equal(baseline.previousRenderedRecords.length,214);
assert.equal(sha(await readFile(resolve(root,'research/meihua/NLC416-12jh005426-44577.pdf'))),'af608094ab11ae209eae91a9365565e7c9cff604aac3da5e753e04d1cc4598c0');
for(const r of index.pages){const b=await readFile(resolve(root,'research/meihua',r.file));assert.equal(b.length,r.bytes);assert.equal(sha(b),r.sha256);assert.equal(r.textLayerCharacters,0);}
for(const r of baseline.previousRenderedRecords)assert.deepEqual(index.pages.find(p=>p.pdfPage===r.pdfPage),r);
assert.equal(baseline.newRenderedPages.length,18);
pass('OriginalPDF/all232localrenders retainidentity;214priorrecords remainexact,18missingpagesfilledwithoutHTTP/OCR');

const manual=await json(resolve(base,'MANUAL_READINGS.json')),units=await json(resolve(base,'UNIT_MAP.json'));
assert.deepEqual(manual.records.map(r=>r.pdfPage),Array.from({length:42},(_,i)=>i+13));assert.equal(manual.counts.newPageRecords,23);
assert.equal(manual.records.filter(r=>r.expandedEarlierReading).length,19);assert.equal(manual.records.at(-1).kind,'content-and-closing');
for(const r of manual.records)assert.equal(sha(await readFile(resolve(base,r.image))),r.imageSHA256);
const digital=await json(resolve(root,'research/meihua-reading/DIGITAL_UNIT_DISPOSITIONS.json'));
const raw=await readFile(resolve(root,'research/meihua/volume-一.wiki')),str=Array.from(raw.toString('utf8'));
assert.equal(units.units.length,45);assert.equal(new Set(units.units.flatMap(u=>u.evidencePDFPages)).size,42);
for(const u of units.units){const d=digital.records.find(d=>d.id===u.id);assert.equal(u.heading,d.heading);assert.equal(u.digitalSourceSliceSHA256,d.sourceSliceSHA256);assert.equal(sha(raw),d.sourceFileSHA256);
 assert.equal(sha(Buffer.from(str.slice(d.start,d.end).join(''))),d.sourceSliceSHA256);assert.equal(u.fullClauseTranscriptionCompleted,false);}
pass('42boundedvolume1pages/45pinnedunitlinks:23new+19expandedincludingearlierboundary54,whichcontainslasttasteandclosingtext');

const fields=tableFieldEvidence(),oldFields=await json(resolve(root,'research/meihua-reading/TRIGRAM_TABLE_FIELDS.json'));
assert.equal(fields.length,216);let linked=0;
for(const row of printedRows()){
 const group=tableFieldEvidence({trigram:row.printedParent});assert.equal(group.length,27);assert.equal(new Set(group.map(f=>f.printedHeader)).size,27);
 for(const f of group){assert.ok(f.headerPDFPage>=33&&f.headerPDFPage<=54);assert.equal(f.fullBodyCollationCompleted,false);assert.equal(f.consumerApplied,false);
  if(f.digitalHeader!==null){const old=oldFields.tables.find(t=>t.trigram===f.trigram).fields.find(t=>t.field===f.digitalHeader);assert.equal(f.digitalBody,old.text);assert.equal(sha(Buffer.from(f.digitalBody)),f.digitalBodySHA256);linked++;}}
}
assert.equal(linked,214);
pass('216physicalheaderpositions,27pertable;214pinneddigitalbodies keep exactSHAanduncompletedphysical-bodycollationstatus');

const absent=fields.filter(f=>f.digitalHeader===null);assert.equal(absent.length,2);
assert.deepEqual(absent.map(f=>[f.trigram,f.printedHeader,f.headerPDFPage,f.printedBoundedBody]),[['坎','動物',44,'豕魚水中之物'],['艮','姓字',51,'宮音帶土字傍之姓氏行位五七']]);
const renamed=fields.filter(f=>f.digitalHeader&&f.digitalHeader!==f.printedHeader);assert.equal(renamed.length,8);
assert.ok(renamed.every(f=>f.printedHeader==='謀望'&&f.digitalHeader==='謀旺'));
assert.equal(tableFieldEvidence({printedHeader:'謀望'}).length,8);
assert.throws(()=>tableFieldEvidence({printedHeader:'謀旺'}));
pass('Twoactualdigitalomissions andeight謀望/謀旺headingpositions stay separated;raw214-fieldindexnotrewritten');

const c={};c.window=c;vm.createContext(c);for(const f of ['engine.js','meihua.js'])vm.runInContext(await readFile(resolve(root,f),'utf8'),c);
const rows=printedRows(),seen=new Set();let memberCases=0;
for(const row of rows)for(const m of row.members){const cast=c.HHC_MEIHUA.compose(m.upper,m.lower,1);assert.equal(cast.primary,m.number);
 const got=lookupHexagram(m.number);assert.equal(got.parentTrigram,row.parentTrigram);assert.equal(got.ordinal,m.ordinal);assert.equal(got.printedName,m.printedName);
 assert.deepEqual(lookupBits([...cast.lower.bits,...cast.upper.bits]),got);seen.add(m.number);memberCases++;
 assert.equal(got.bodyElementInferred,false);assert.equal(got.shiYing,null);assert.equal(got.naJia,null);assert.equal(got.liuQin,null);assert.equal(got.predictedEvent,null);}
assert.equal(memberCases,64);assert.equal(seen.size,64);
const palaceSource=await json(resolve(base,'PALACE_ROWS.json'));assert.equal(palaceSource.pinnedDigitalSHA256,sha(raw));assert.equal(palaceSource.nameVariants.length,7);
assert.deepEqual(palaceSource.nameVariants.map(v=>[v.printedName,v.digitalName]),[['天山遯','天山遁'],['地雷復','地雷複'],['澤天夬','澤天決'],['天雷无妄','天雷無妄'],['火水未濟','火水末濟'],['兌為澤','兌為金'],['澤山咸','澤山鹹']]);
for(const row of printedRows()){
 const section=raw.toString('utf8').split("'''"+row.printedParent+"卦'''")[1].split('天時')[0].trim().split(/\r?\n/).map(s=>s.trim()).filter(Boolean).slice(1).join(' ').split(/\s+/);
 assert.deepEqual(section,row.members.map(m=>m.digitalName));}
pass('64literalprintedmembers identifiedwith64actualenginecompositions;sevenphysical/digitalnamepositions preservebothlayers withoutrewritingsource');

// Independent sequential toggles,rather than the mask formula in the reference.
for(const row of rows){const b=c.HHC_MEIHUA.compose(row.parentTrigram,row.parentTrigram,1),v=[...b.lower.bits,...b.upper.bits],generated=derivePalace(row.parentTrigram);
 for(let stage=0;stage<8;stage++){
  if(stage>=1&&stage<=5)v[stage-1]^=1;
  else if(stage===6)v[3]^=1;
  else if(stage===7)for(let i=0;i<3;i++)v[i]^=1;
  assert.deepEqual(generated[stage].bits,v);assert.equal(generated[stage].number,row.members[stage].number);assert.equal(generated[stage].notAMovingLineEvent,true);
 }}
pass('Inferredmaskformula matchesindependentsequentialtoggles andall64printedmembers;noeventorunprinted世應rule asserted');

const inverse=new Set();for(let n=0;n<64;n++){const b=Array.from({length:6},(_,i)=>(n>>i)&1),r=lookupBits(b);assert.deepEqual(r.bits,b);inverse.add(r.number);}
assert.equal(inverse.size,64);
const small=c.HHC_MEIHUA.compose(5,1,1),palace=lookupHexagram(small.primary);assert.equal(small.primary,9);assert.equal(small.body.element,'Mộc');
// Different moving line:body=lower乾Kim butpalace stays巽Mộc.
const upperMoves=c.HHC_MEIHUA.compose(5,1,4);assert.equal(upperMoves.body.element,'Kim');assert.equal(lookupHexagram(upperMoves.primary).palaceElement,'Mộc');
assert.equal(lookupHexagram(11).palaceElement,'Thổ');assert.equal(c.HHC_MEIHUA.compose(8,1,4).body.element,'Kim');
pass('All64bitkeys formabijection;twoactualcounterexamplespreventpalaceelementfromsilentlyoverwritingMaiHoabodyelement');

for(const n of [0,65,NaN,1.5,'1',null])assert.throws(()=>lookupHexagram(n));
for(const n of [0,9,NaN,'1'])assert.throws(()=>derivePalace(n));
for(const b of [[],new Array(6),[0,0,0,0,0],[true,0,0,0,0,0],[0,0,0,0,0,2],'111111'])assert.throws(()=>lookupBits(b));
for(const q of [null,[],{trigram:'__proto__'},{trigram:1},{printedHeader:'unknown'},{date:'2026-10-27'}])assert.throws(()=>tableFieldEvidence(q));
const mutated=lookupHexagram(1);mutated.bits[0]=0;mutated.evidencePDFPages.push(999);rows[0].members[0].number=999;fields[0].digitalBody='modified';
assert.equal(lookupHexagram(1).bits[0],1);assert.equal(lookupHexagram(1).evidencePDFPages.includes(999),false);assert.equal(printedRows()[0].members[0].number,1);assert.notEqual(tableFieldEvidence()[0].digitalBody,'modified');
pass('Invalidnumbers,bits,querypremises andprototype-likevalues rejected;returnvalues cannotmutate sourcecatalogue');

const nav=await json(resolve(base,'FIVE_VOLUME_NAVIGATION.json')),spans=[];
for(const v of nav.volumes){for(let p=v.first;p<=v.last;p++)spans.push(p);assert.equal(v.fullClauseExtractionCompleted,false);assert.ok((await readFile(resolve(base,v.map))).length>0);}
assert.equal(spans.length,212);assert.equal(new Set(spans).size,212);assert.equal(nav.counts.contentPagesIncludingTitleAndClosing,209);
assert.equal(nav.counts.endleaves,3);assert.equal(nav.counts.threeDigitalVolumeUnits,123);
assert.equal(new Set([...spans,...Object.values(nav.excluded).flat()]).size,232);assert.equal(spans.length+Object.values(nav.excluded).flat().length,232);
assert.equal(nav.wholeBookApplied,false);assert.equal(nav.wholeCatalogueCompleted,false);
pass('Fivevolumescover212spanpages/209content+3endleaves;front/ads/logo/cover/imprint/backaccountforall232withoutclaimingfullclauseapplication');

const html=await readFile(resolve(root,'Huyen_Hoc_Cac.html'));assert.equal(html.length,703410);assert.equal(sha(html),'3800162854742c915d60f0051c65cadb0eb9a1c803f9f937bf1b6a593c96d268');
for(const token of ['palace-reference','PALACE_ROWS','TABLE_FIELDS.json','FIVE_VOLUME_NAVIGATION'])assert.equal(html.includes(Buffer.from(token)),false);
pass('Printedpalacereference andbody/headerresearchstayoutsidetheunchanged703410byteconsumerHTML');
const out={schema:'hhc.meihua.volume1.qa.v1',checks,summary:{sourcePageRecords:42,newPageRecords:23,expandedEarlierReadings:19,newPNGDerivatives:18,retainedPNGDerivatives:232,digitalUnitLinks:45,physicalHeaderPositions:216,pinnedDigitalFields:214,missingDigitalFields:2,differentHeaderSlots:8,differentPalaceNamePositions:7,printedPalaceRows:8,printedPalaceMembers:64,actualEngineCompositions:64,inverseBitKeys:64,fullBodyCollationCompleted:false,newHTTPResponses:0,consumerChanged:false,predictiveAccuracyEstablished:false,wholeBookApplied:false},htmlSHA256:sha(html)};
await writeFile(resolve(qa,'ENGINE_RESULTS.json'),JSON.stringify(out,null,2)+'\n');console.log(JSON.stringify(out.summary));
