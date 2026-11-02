import {mkdir, readFile, writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {resolve, relative} from 'node:path';
import https from 'node:https';

const root=resolve(import.meta.dirname,'../..');
const out=resolve(root,'v53/research/full-study/bazi');
await mkdir(resolve(out,'sources'),{recursive:true});
const rows=[];
async function fetchBytes(url,file,redirects=0){
  if(redirects>4)throw new Error('Too many redirects');
  const r=await new Promise((res,rej)=>https.get(url,{headers:{'User-Agent':'HHC-local-research/1.0','Accept':'application/json,text/html,text/plain;q=0.9,*/*;q=0.1'}},res).on('error',rej));
  if(r.statusCode>=300&&r.statusCode<400&&r.headers.location){r.resume();return fetchBytes(new URL(r.headers.location,url).href,file,redirects+1);}
  const tlsAuthorized=r.socket?.authorized??null;
  const chunks=[];for await(const c of r)chunks.push(c);const bytes=Buffer.concat(chunks);
  if(r.statusCode!==200)throw new Error(`${url}: HTTP ${r.statusCode}`);
  const path=resolve(out,'sources',file);await writeFile(path,bytes);
  const row={file:relative(out,path).replaceAll('\\','/'),url,status:r.statusCode,bytes:bytes.length,sha256:createHash('sha256').update(bytes).digest('hex'),retrievedUTC:new Date().toISOString(),tlsAuthorized,headers:{'content-type':r.headers['content-type'],etag:r.headers.etag,'last-modified':r.headers['last-modified']}};
  rows.push(row);return bytes;
}
const ts=JSON.parse((await fetchBytes('https://registry.npmjs.org/lunar-typescript/1.8.6','npm-lunar-typescript-1.8.6.json')).toString());
const js=JSON.parse((await fetchBytes('https://registry.npmjs.org/lunar-javascript/1.7.7','npm-lunar-javascript-1.7.7.json')).toString());
await fetchBytes('https://6tail.cn/calendar/lunar.bazi.html','6tail-lunar-bazi.html');
const tsRef=ts.gitHead;
if(!tsRef)throw new Error('Exact npm release has no gitHead');
const tree=JSON.parse((await fetchBytes(`https://api.github.com/repos/6tail/lunar-typescript/git/trees/${tsRef}?recursive=1`,'typescript-tree.json')).toString());
for(const suffix of ['Yun.ts','DaYun.ts','Solar.ts','EightCharTest.ts']){
  const entry=tree.tree.find(x=>x.path.endsWith('/'+suffix));
  if(entry)await fetchBytes(`https://raw.githubusercontent.com/6tail/lunar-typescript/${tsRef}/${entry.path}`,suffix);
}
await fetchBytes(`https://raw.githubusercontent.com/6tail/lunar-typescript/${tsRef}/README.md`,'typescript-README.md');
if(js.gitHead)await fetchBytes(`https://raw.githubusercontent.com/6tail/lunar-javascript/${js.gitHead}/lunar.js`,'javascript-lunar.js');
const inherited=JSON.parse(await readFile(resolve(root,'v53/research/four-items/sources/MANIFEST.json'),'utf8'));
const reused=[];
for(const name of ['KR3g0042_002.txt','KR3g0042_005.txt','yuanhai-NTL-v1.pdf','yuanhai-p54.png']){
  const path=resolve(root,'v53/research/four-items/sources',name),bytes=await readFile(path);
  const old=inherited.files.find(x=>x.file===name);
  reused.push({file:relative(out,path).replaceAll('\\','/'),bytes:bytes.length,sha256:createHash('sha256').update(bytes).digest('hex'),url:old?.url??null,reusedWithoutNewDownload:true});
}
const local=[];
for(const name of ['v46/node_modules/lunar-typescript/package.json','v46/node_modules/lunar-typescript/dist/index.cjs','v47/bazi/node_modules/lunar-javascript/package.json','v47/bazi/node_modules/lunar-javascript/lunar.js']){
  const path=resolve(root,name),bytes=await readFile(path);local.push({file:name,bytes:bytes.length,sha256:createHash('sha256').update(bytes).digest('hex')});
}
const manifest={scope:'Private research evidence; not part of site release',createdUTC:new Date().toISOString(),packageSourceRefs:{lunarTypescript:{version:ts.version,gitHead:ts.gitHead},lunarJavascript:{version:js.version,gitHead:js.gitHead}},downloads:rows,reused,local};
await writeFile(resolve(out,'SOURCE_MANIFEST.json'),JSON.stringify(manifest,null,2)+'\n');
console.log(JSON.stringify({downloads:rows.length,reused:reused.length,local:local.length,packageSourceRefs:manifest.packageSourceRefs}));
