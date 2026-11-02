import fs from 'node:fs';import path from 'node:path';import{createHash}from'node:crypto';
import{createRequire}from'node:module';import assert from'node:assert/strict';
const b=import.meta.dirname,w=path.resolve(b,'../..'),out=path.join(b,'ACTUAL_RUNTIME.json');
assert(!fs.existsSync(out),'Retained actual batch exists; verify it instead of rerunning.');
const sha=x=>createHash('sha256').update(x).digest('hex');
const read=name=>JSON.parse(fs.readFileSync(path.join(b,name),'utf8'));
for(const x of read('PREIMPLEMENTATION_FREEZE.json').files){const raw=fs.readFileSync(path.join(b,x.file));assert.equal(raw.length,x.bytes);assert.equal(sha(raw),x.sha256);}
const modulePath=path.join(w,'v46/node_modules/lunar-typescript');
const L=createRequire(import.meta.url)(modulePath),version=JSON.parse(fs.readFileSync(path.join(modulePath,'package.json'),'utf8')).version;
assert.equal(version,'1.8.6');
const expected=read('EXPECTED_BEFORE_IMPLEMENTATION.json').actualLunarExpected;
const branches=[...'子丑寅卯辰巳午未申酉戌亥'];
const partners=branches.map((branch,index)=>{const actual=L.LunarUtil.HE_ZHI_6[index];return{branch,index,actual,expected:expected.orderedPartners[branch],matches:actual===expected.orderedPartners[branch]};});
const lu={stem:'甲',actual:L.LunarUtil.LU['甲'],expected:expected.luJia};lu.matches=lu.actual===lu.expected;
const report={date:'2026-10-29',executedUTC:new Date().toISOString(),libraryVersion:version,
 libraryFile:'v46/node_modules/lunar-typescript/dist/index.cjs',librarySHA256:sha(fs.readFileSync(path.join(modulePath,'dist/index.cjs'))),
 scriptSHA256:sha(fs.readFileSync(import.meta.filename)),freezeSHA256:sha(fs.readFileSync(path.join(b,'PREIMPLEMENTATION_FREEZE.json'))),
 method:'Execute the retained official library in Node and query its exported HE_ZHI_6 table12 times plus its LU table once. No reimplementation used for this comparison.',
 partners,lu,actualPartnerTableQueries:12,actualLuQueries:1,actualCalendarObjects:0,actualNatalCharts:0,
 untested:'Hidden-horse formula, source month station astronomy, directional fortune claims and effective combination are not validated by this coordinate batch.',
 sourceEfficacyValidated:false};
fs.writeFileSync(out,JSON.stringify(report,null,2)+'\n');
assert(partners.every(x=>x.matches)&&lu.matches);console.log(JSON.stringify({actualPartnerTableQueries:12,actualLuQueries:1,matches:13,actualCalendarObjects:0,actualNatalCharts:0}));
