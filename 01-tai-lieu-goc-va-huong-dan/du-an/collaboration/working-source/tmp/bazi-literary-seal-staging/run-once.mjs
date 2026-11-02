import fs from'node:fs';import path from'node:path';import{createHash}from'node:crypto';import{createRequire}from'node:module';import assert from'node:assert/strict';
const b=import.meta.dirname,w=process.cwd(),out=path.join(b,'ACTUAL_RUNTIME.json');if(fs.existsSync(out))throw Error('Actual batch retained; do not rerun.');
const read=p=>JSON.parse(fs.readFileSync(p,'utf8').replace(/^\uFEFF/,'')),hash=p=>createHash('sha256').update(fs.readFileSync(p)).digest('hex');
const freeze=read(path.join(b,'FREEZE.json')),plan=read(path.join(b,'PLAN.json'));assert(freeze.referenceAndRuntimeAbsent);
for(const r of [...freeze.files,...plan.sources,...read(path.join(b,'IDENTITY_INPUTS.json')).files]){const p=path.join(w,r.file);assert.equal(fs.statSync(p).size,r.bytes);assert.equal(hash(p),r.sha256);}
const req=createRequire(import.meta.url),L=req(path.join(w,'v46/node_modules/lunar-typescript'));assert.equal(req(path.join(w,'v46/node_modules/lunar-typescript/package.json')).version,'1.8.6');
const nayin=plan.missingNaYin.map(e=>{const actual=L.LunarUtil.NAYIN[e.pillar];assert.equal(actual,e.expected);return{...e,actual,newCall:true};});
const elements=plan.missingStemElements.map(e=>{const actual=L.LunarUtil.WU_XING_GAN[e.stem];assert.equal(actual,e.expected);return{...e,actual,newCall:true};});
const result={executedUTC:new Date().toISOString(),scriptSHA256:hash(path.join(b,'run-once.mjs')),freezeSHA256:hash(path.join(b,'FREEZE.json')),
 librarySHA256:hash(path.join(w,'v46/node_modules/lunar-typescript/dist/index.cjs')),newNaYin:nayin,newStemElements:elements,
 reusedNaYin:plan.reuseNaYin.map(e=>({...e,actual:e.retained.actual,newCall:false})),reusedStemElements:plan.reuseStemElements.map(e=>({...e,actual:e.retained.actual,newCall:false})),
 reusedBranchPartners:plan.reuseBranchPartners,newNaYinQueries:nayin.length,newStemElementQueries:elements.length,newBranchPartnerQueries:0,actualCalendarObjects:0,actualNatalCharts:0,sourceMechanismsAdjudicated:false};
fs.writeFileSync(out,JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify({newNaYin:nayin.length,newStemElements:elements.length,reusedNaYin:plan.reuseNaYin.length,reusedStemElements:plan.reuseStemElements.length,newCharts:0}));
