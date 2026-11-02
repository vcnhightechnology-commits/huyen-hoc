import {readFile,writeFile} from 'node:fs/promises';
import {resolve} from 'node:path';
import vm from 'node:vm';
import assert from 'node:assert/strict';
import {createHash} from 'node:crypto';
const root=resolve(import.meta.dirname,'..'),out=resolve(root,'research/full-study/home');
const engineBytes=await readFile(resolve(root,'engine.js'));
const ctx={window:{}};vm.createContext(ctx);vm.runInContext(engineBytes.toString('utf8'),ctx);
const engine=ctx.window.HHC_ENGINE;
// Bits are bottom/middle/top weights1/2/4. This is a digital encoding of the named line changes,
// not an assumption that the cited work used binary arithmetic.
const palaces=[{kua:1,name:'坎',bits:2},{kua:2,name:'坤',bits:0},{kua:3,name:'震',bits:1},{kua:4,name:'巽',bits:6},{kua:6,name:'乾',bits:7},{kua:7,name:'兌',bits:3},{kua:8,name:'艮',bits:4},{kua:9,name:'離',bits:5}];
const targets=[{name:'Bắc',trigram:'坎',bits:2},{name:'Đông Bắc',trigram:'艮',bits:4},{name:'Đông',trigram:'震',bits:1},{name:'Đông Nam',trigram:'巽',bits:6},{name:'Nam',trigram:'離',bits:5},{name:'Tây Nam',trigram:'坤',bits:0},{name:'Tây',trigram:'兌',bits:3},{name:'Tây Bắc',trigram:'乾',bits:7}];
const relations={0:{han:'伏位',label:'Phục Vị'},1:{han:'禍害',label:'Họa Hại'},2:{han:'絶命',label:'Tuyệt Mệnh'},3:{han:'天醫',label:'Thiên Y'},4:{han:'生氣',label:'Sinh Khí'},5:{han:'六煞',label:'Lục Sát'},6:{han:'五鬼',label:'Ngũ Quỷ'},7:{han:'延年',label:'Diên Niên'}};
const results=[];
for(const p of palaces){let access;for(let year=1900;year<=2100&&!access;year++){const r=engine.directions({year,gender:'male'});if(r.number===p.kua)access={year,gender:'male',r};}assert(access,'No engine lookup for kua'+p.kua);for(const target of targets){const expected=relations[p.bits^target.bits],actual=access.r.all.find(r=>r.direction===target.name)?.label;results.push({kua:p.kua,sourceTrigram:p.name,target:target.name,targetTrigram:target.trigram,expectedHan:expected.han,expected:expected.label,actual,match:actual===expected.label,engineAccessInput:{year:access.year,gender:access.gender}});}}
assert(results.every(r=>r.match),'Mismatch between Chinese transcription line-change relation and engine label table');
const report={schema:'hhc.home.dayounian.engine-check.v1',executedUTC:new Date().toISOString(),engineFile:'v53/engine.js',engineSHA256:createHash('sha256').update(engineBytes).digest('hex'),source:'wikisource-xieji-v02-oldid787335.html, 大遊年變卦 and adjacent eight line-change paragraphs',sourceTier:'Chinese transcription witness read; this passage has not been facsimile-collated in this scope',method:'Actual window.HHC_ENGINE.directions execution under Node vm. Expected relation from named changed lines, represented as bitwise XOR. The input year only accesses a conditional kua row; its historical year→kua assignment is not validated.',cases:results.length,matches:results.filter(r=>r.match).length,verified:'64 conditional palace×direction labels only',notVerified:['Birth-year→kua, gender assignment, calendar boundary','Special kua5 rule','House sitting/facing or stove/bed/room-placement convention','Predictive effect'],results};
await writeFile(resolve(out,'DAYOUNIAN_ENGINE_CHECK.json'),JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({cases:report.cases,matches:report.matches,engineSHA256:report.engineSHA256}));
