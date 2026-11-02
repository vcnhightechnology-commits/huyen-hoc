import https from'node:https';import{readFile,writeFile}from'node:fs/promises';import{resolve}from'node:path';import{createHash}from'node:crypto';
const s=import.meta.dirname,sha=(x,alg='sha256')=>createHash(alg).update(x).digest('hex');
const log=await readFile(resolve(s,'REQUESTS.json'),'utf8').then(JSON.parse).catch(()=>({records:[],errors:[]}));
async function get(url,file){
 const prior=log.records.find(x=>x.url===url);if(prior){const raw=await readFile(resolve(s,prior.file));if(sha(raw)!==prior.sha256)throw Error('Cache mismatch');if(prior.status!==200)throw Error('Previously failed URL; no repeat');return raw;}
 let result;
 try{result=await new Promise((yes,no)=>{const req=https.get(url,{headers:{'Accept-Encoding':'identity','User-Agent':'HuyenHocCac local source audit'}},res=>{const data=[],tls={authorized:res.socket.authorized,authorizationError:res.socket.authorizationError??null,protocol:res.socket.getProtocol?.()??null};res.on('data',x=>data.push(x));res.on('error',no);res.on('end',()=>yes({body:Buffer.concat(data),status:res.statusCode,headers:res.headers,tls}));});req.on('error',no);req.setTimeout(35000,()=>req.destroy(Error('timeout')));});}
 catch(error){log.errors.push({url,file,error:String(error),retrievedUTC:new Date().toISOString(),tlsBypassUsed:false});await writeFile(resolve(s,'REQUESTS.json'),JSON.stringify(log,null,2)+'\n');throw error;}
 await writeFile(resolve(s,file),result.body);log.records.push({url,file,status:result.status,bytes:result.body.length,sha256:sha(result.body),sha1:sha(result.body,'sha1'),headers:result.headers,tls:result.tls,retrievedUTC:new Date().toISOString()});await writeFile(resolve(s,'REQUESTS.json'),JSON.stringify(log,null,2)+'\n');
 if(result.status!==200||!result.tls.authorized)throw Error('HTTP/TLS source not accepted');return result.body;
}
const description='https://commons.wikimedia.org/wiki/File:CADAL06066039_%E4%B8%89%E5%91%BD%E9%80%9A%E6%9C%83%C2%B7%E5%8D%B7%E4%B8%89.djvu';
const original='https://upload.wikimedia.org/wikipedia/commons/8/86/CADAL06066039_%E4%B8%89%E5%91%BD%E9%80%9A%E6%9C%83%C2%B7%E5%8D%B7%E4%B8%89.djvu';
// Both links/identity fields were independently observed on Commons via web.
// Download the original once even if this environment cannot read description.
try{await get(description,'commons-description.html');}catch(error){console.log('Description unavailable:',String(error));}
const raw=await get(original,'CADAL06066039.djvu');
if(raw.length!==10619960||sha(raw,'sha1')!=='61fee880e39b5df646278c51d1b62532a47e4422')throw Error('Observed catalogue identity mismatch');
await writeFile(resolve(s,'IDENTITY.json'),JSON.stringify({date:'2026-10-27',description,original,observedCatalogueRevision:1207461000,catalogueBytes:10619960,catalogueSHA1:'61fee880e39b5df646278c51d1b62532a47e4422',cataloguePages:230,actualBytes:raw.length,actualSHA1:sha(raw,'sha1'),actualSHA256:sha(raw),metadataAttribution:'Commons describes CADAL06066039/四庫全書/卷三; direct institutional record not yet fetched.',independentEditionEstablished:false,status:'bytes-verified-reading-pending',sourceInstructionsAreData:true},null,2)+'\n');
console.log(JSON.stringify({bytes:raw.length,sha256:sha(raw),catalogueSHA1Match:true,requests:log.records.length}));
