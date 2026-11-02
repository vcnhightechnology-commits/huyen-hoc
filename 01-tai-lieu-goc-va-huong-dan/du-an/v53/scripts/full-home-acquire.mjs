import https from 'node:https';
import {mkdir,readFile,writeFile} from 'node:fs/promises';
import {resolve} from 'node:path';
import {createHash} from 'node:crypto';
const out=resolve(import.meta.dirname,'../research/full-study/home');
await mkdir(out,{recursive:true});
const sha=b=>createHash('sha256').update(b).digest('hex');
let records=[];try{records=JSON.parse(await readFile(resolve(out,'MANIFEST.json'),'utf8')).files;}catch{}
function get(url,chain=[]){return new Promise((done,fail)=>{const req=https.get(new URL(url),{headers:{'User-Agent':'HuyenHocCac-LocalResearch/1.0 (private source audit)','Accept-Encoding':'identity'}},r=>{const hop={url,status:r.statusCode};if([301,302,303,307,308].includes(r.statusCode)&&r.headers.location&&chain.length<5){r.resume();get(new URL(r.headers.location,url).href,[...chain,hop]).then(done,fail);return;}const tls={authorized:r.socket?.authorized===true,protocol:r.socket?.getProtocol?.()};const chunks=[];r.on('data',b=>chunks.push(b));r.on('end',()=>done({url,status:r.statusCode,headers:r.headers,tls,chain:[...chain,hop],body:Buffer.concat(chunks)}));r.on('error',fail);});req.setTimeout(20000,()=>req.destroy(Error('Request timeout')));req.on('error',fail);});}
async function capture(file,url,role){const prior=records.find(x=>x.file===file&&x.requestedURL===url);if(prior?.sha256){const body=await readFile(resolve(out,file));if(sha(body)!==prior.sha256)throw Error('Saved byte mismatch: '+file);return {record:prior,body};}try{const r=await get(url);const record={file,requestedURL:url,finalURL:r.url,retrievedUTC:new Date().toISOString(),status:r.status,bytes:r.body.length,sha256:sha(r.body),headers:r.headers,tls:r.tls,redirectChain:r.chain,usable:r.status===200,role,transport:'HTTPS with certificate validation; Accept-Encoding identity; response body saved as received, no text conversion'};await writeFile(resolve(out,file),r.body);records.push(record);console.log(file,r.status,r.body.length);return {record,body:r.body};}catch(e){const record={file,requestedURL:url,retrievedUTC:new Date().toISOString(),usable:false,error:e.message,role};records.push(record);console.log(file,e.message);return {record};}finally{await writeFile(resolve(out,'MANIFEST.json'),JSON.stringify({schema:'hhc.full-study.home.sources.v1',files:records},null,2)+'\n');}}
const ws='https://zh.wikisource.org/w/index.php?oldid=787335&title='+encodeURIComponent('欽定協紀辨方書_(四庫全書本)/卷02');
const commons='https://commons.wikimedia.org/wiki/File:'+encodeURIComponent('CADAL06056503_欽定協紀辨方書·卷二.djvu');
const title='File:CADAL06056503 欽定協紀辨方書·卷二.djvu';
const api='https://commons.wikimedia.org/w/api.php?action=query&format=json&prop=imageinfo&iiprop=url%7Csize%7Csha1%7Cextmetadata&titles='+encodeURIComponent(title);
await Promise.all([
 capture('wikisource-xieji-v02-oldid787335.html',ws,'Immutable Wikisource revision; Chinese transcription, not yet scan-verified'),
 capture('commons-cadal06056503-catalog.html',commons,'Public catalogue/file metadata; CADAL attribution is Commons metadata, not independent custody verification'),
 capture('commons-cadal06056503-imageinfo.json',api,'Commons API image metadata, file identity and direct URL'),
]);
const html=await readFile(resolve(out,'wikisource-xieji-v02-oldid787335.html'),'utf8');
await writeFile(resolve(out,'wikisource-links.json'),JSON.stringify([...html.matchAll(/(?:href|src)="([^"]+)"/g)].map(x=>x[1]).filter(x=>/commons|upload|thumb|Page:|二十四|SKQS/i.test(x)),null,2)+'\n');
const infoRecord=records.find(x=>x.file==='commons-cadal06056503-imageinfo.json');
if(infoRecord?.usable){const data=JSON.parse(await readFile(resolve(out,infoRecord.file),'utf8'));const info=Object.values(data.query?.pages||{})[0]?.imageinfo?.[0];if(info?.url){await writeFile(resolve(out,'CADAL_IDENTITY.json'),JSON.stringify(info,null,2)+'\n');await capture('CADAL06056503.djvu',info.url,'Whole public facsimile container; SHA confirms downloaded bytes, not complete reading');}}
if(process.argv.includes('--pages')){
 const html=await readFile(resolve(out,'commons-cadal06056503-catalog.html'),'utf8');
 const src=html.match(/src="([^"]+page1-500px[^"]+)"/)?.[1]?.replaceAll('&amp;','&');
 if(src)for(const n of [1,2,3,4,5,6,7,8]){const u=src.replace(/page1-500px/g,`page${n}-500px`);await capture(`CADAL06056503-page${String(n).padStart(3,'0')}-500.jpg`,u,'Commons rendered page at advertised standard width of the public DjVu facsimile, page ordinal '+n+'; derivative distinct from DjVu bytes');}
}
if(process.argv.includes('--reading-pages')){
 const html=await readFile(resolve(out,'commons-cadal06056503-catalog.html'),'utf8');
 const src=html.match(/src="([^"]+page1-500px[^"]+)"/)?.[1]?.replaceAll('&amp;','&');
 if(src)for(const n of [5,6,7])await capture(`CADAL06056503-page${String(n).padStart(3,'0')}-960.jpg`,src.replace(/page1-500px/g,`page${n}-960px`),'Commons rendered page at standard width960; page ordinal '+n+'; derivative distinct from the archived whole DjVu');
}
