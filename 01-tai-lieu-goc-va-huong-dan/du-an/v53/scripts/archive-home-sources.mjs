import https from 'node:https';
import {mkdir,writeFile,readFile,copyFile} from 'node:fs/promises';
import {resolve} from 'node:path';
import {createHash} from 'node:crypto';
const root=resolve(import.meta.dirname,'..'),out=resolve(root,'research/home');
await mkdir(out,{recursive:true});
const before=resolve(root,'../archives/v53-before-home-guide');
await mkdir(before,{recursive:true});
for(const [src,name] of [['Huyen_Hoc_Cac.html','Huyen_Hoc_Cac.html'],['../Huyen_Hoc_Cac_V53_web.zip','Huyen_Hoc_Cac_V53_web.zip'],['../Huyen_Hoc_Cac_V53_source.zip','Huyen_Hoc_Cac_V53_source.zip'],['PACKAGE_MANIFEST.json','PACKAGE_MANIFEST.json']]){
  try{await readFile(resolve(before,name))}catch{await copyFile(resolve(root,src),resolve(before,name))}
}
const base='https://zh.wikisource.org/wiki/Page:Sibu_Congkan1822-孫星衍-孫淵如詩文集-8-1.djvu/';
const img='https://thumb.wikimedia.org/wikipedia/commons/thumb/0/01/Sibu_Congkan1822-孫星衍-孫淵如詩文集-8-1.djvu/';
const sources=[
 ['epa-air.html','https://www.epa.gov/indoor-air-quality-iaq/care-your-air-guide-indoor-air-quality'],
 ['cdc-mold.html','https://www.cdc.gov/mold-health/about/index.html'],
 ['cdc-sleep.html','https://www.cdc.gov/sleep/about/'],
 ['usfa-escape.html','https://www.usfa.fema.gov/prevention/home-fires/prepare-for-fire/home-fire-escape-plans/index.html'],
 ['usfa-candle.html','https://www.usfa.fema.gov/prevention/home-fires/prevent-fires/candle/'],
 ['yourhome-climate.html','https://www.yourhome.gov.au/passive-design/design-climate'],
 ['doe-daylight.html','https://bsesc.energy.gov/energy-basics/natural-light-and-daylighting'],
 ...[60,61].flatMap(n=>[[`sun-preface-${n}.html`,base+n],[`sun-preface-${n}.jpg`,img+`page${n}-1920px-Sibu_Congkan1822-孫星衍-孫淵如詩文集-8-1.djvu.jpg`]])
];
function get(url,redirects=0){return new Promise((done,fail)=>{
 const req=https.get(encodeURI(url),{headers:{'User-Agent':'HuyenHocCac-LocalResearch/1.0 (private source audit)','Accept-Encoding':'identity'}},r=>{
  if([301,302,303,307,308].includes(r.statusCode)&&r.headers.location&&redirects<5){r.resume();get(new URL(r.headers.location,url).href,redirects+1).then(done,fail);return}
  const chunks=[];r.on('data',b=>chunks.push(b));r.on('end',()=>done({url,status:r.statusCode,headers:r.headers,body:Buffer.concat(chunks)}));r.on('error',fail);
 });req.setTimeout(25000,()=>req.destroy(Error('Request timeout')));req.on('error',fail);
})}
let previous=[];try{previous=JSON.parse(await readFile(resolve(out,'SOURCE_MANIFEST.json'),'utf8')).sources}catch{}
const audit=[];
for(const [file,url] of sources){
 const prior=previous.find(s=>s.file===file&&s.requestedURL===url);
 if(prior){if(prior.sha256){const b=await readFile(resolve(out,file));if(createHash('sha256').update(b).digest('hex')!==prior.sha256)throw Error('Archived source changed: '+file)}audit.push(prior);console.log(file,'preserved existing record');continue}
 try{
  const r=await get(url),sha256=createHash('sha256').update(r.body).digest('hex');
  await writeFile(resolve(out,file),r.body);
  audit.push({file,requestedURL:url,finalURL:r.url,retrievedUTC:new Date().toISOString(),status:r.status,bytes:r.body.length,sha256,headers:r.headers,transport:'Node HTTPS; certificate validation enabled; Accept-Encoding identity; response body saved without text transformation',usable:r.status===200});
  console.log(file,r.status,r.body.length,sha256);
 }catch(e){audit.push({file,requestedURL:url,error:e.message,usable:false});console.log(file,e.message)}
}
await writeFile(resolve(out,'SOURCE_MANIFEST.json'),JSON.stringify({scope:'Housing layout research; original HTTP response bodies, not publisher signatures',sources:audit},null,2)+'\n');
const preserved=[];for(const name of ['Huyen_Hoc_Cac.html','Huyen_Hoc_Cac_V53_web.zip','Huyen_Hoc_Cac_V53_source.zip','PACKAGE_MANIFEST.json']){const b=await readFile(resolve(before,name));preserved.push({file:name,bytes:b.length,sha256:createHash('sha256').update(b).digest('hex')})}
await writeFile(resolve(before,'PRESERVED.json'),JSON.stringify(preserved,null,2)+'\n');
