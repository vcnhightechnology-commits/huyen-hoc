import fs from 'node:fs';
import path from 'node:path';
import {createHash} from 'node:crypto';
import {createRequire} from 'node:module';
import vm from 'node:vm';
import assert from 'node:assert/strict';
const base=import.meta.dirname,out=path.join(base,'ACTUAL_RUNTIME.json');
if(fs.existsSync(out))throw Error('One-time retained batch exists; verify it read-only instead of reexecuting.');
const hash=b=>createHash('sha256').update(b).digest('hex');
const read=n=>JSON.parse(fs.readFileSync(path.join(base,n),'utf8'));
const freeze=read('PREIMPLEMENTATION_FREEZE.json');assert.equal(freeze.implementationExists,false);
for(const x of freeze.files){const b=fs.readFileSync(path.join(base,x.file));assert.equal(b.length,x.bytes);assert.equal(hash(b),x.sha256);}
let w=base;while(!fs.existsSync(path.join(w,'v53/engine.js'))){const p=path.dirname(w);if(p===w)throw Error('workspace');w=p;}
const engine=fs.readFileSync(path.join(w,'v53/engine.js')),relations=fs.readFileSync(path.join(w,'v53/bazi-relations.js'));
assert.equal(hash(engine),'39f08bd1887faca4d35f7ad415ebf596621010d530b489212774d5cbf99040e6');
assert.equal(hash(relations),'a1599a0ddbe716f02111e56f5da82943bd2878356fc3959a411fbffc8bd8e6d0');
const c={};c.window=c;vm.createContext(c);vm.runInContext(engine.toString(),c);vm.runInContext(relations.toString(),c);
const req=createRequire(import.meta.url),pkg=req(path.join(w,'v46/node_modules/lunar-typescript/package.json'));assert.equal(pkg.version,'1.8.6');
const L=req(path.join(w,'v46/node_modules/lunar-typescript')),fixture=read('EXPECTED_BEFORE_IMPLEMENTATION.json');
const stems=Array.from('甲乙丙丁戊己庚辛壬癸'),pairs=[];
for(const x of fixture.enginePairs) {
 const hhc=c.HHC_BAZI_RELATIONS.god(stems.indexOf(x.root),stems.indexOf(x.target));
 const lunar=L.LunarUtil.SHI_SHEN[x.root+x.target];
 assert.equal(hhc,x.hhcTenGod);assert.equal(lunar,x.lunarTenGod);
 pairs.push({root:x.root,target:x.target,actualHHCTenGod:hhc,actualLunarTenGod:lunar});
}
const stemElements={};for(const s of Object.keys(fixture.stemElements)){stemElements[s]=L.LunarUtil.WU_XING_GAN[s];assert.equal(stemElements[s],fixture.stemElements[s]);}
const runtime={date:'2026-10-29',executedUTC:new Date().toISOString(),engineSHA256:hash(engine),relationsSHA256:hash(relations),
 lunarLibrarySHA256:hash(fs.readFileSync(path.join(w,'v46/node_modules/lunar-typescript/dist/index.cjs'))),lunarVersion:pkg.version,
 scriptSHA256:hash(fs.readFileSync(import.meta.filename)),freezeSHA256:hash(fs.readFileSync(path.join(base,'PREIMPLEMENTATION_FREEZE.json'))),
 pairs,stemElements,summary:{actualHHCGodCalls:11,actualLunarTenGodTableQueries:11,actualLunarStemElementTableQueries:5,
 actualHHCNatalCharts:0,actualLunarCalendarObjects:0,actualIztroCharts:0,newIndependentPrintedBirthCharts:0,
 sourceRelationCoordinatesCompared:true,sourceEllipsisMeaningValidated:false,sourceSuppressionEffectivenessValidated:false,
 sourceOutcomeValidated:false,consumerChanged:false}};
fs.writeFileSync(out,JSON.stringify(runtime,null,2)+'\n');console.log(JSON.stringify(runtime.summary));
