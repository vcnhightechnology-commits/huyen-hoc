// Ordinary public HTTPS, TLS verification retained; bounded witness acquisition, no auth/bypass.
import https from'node:https';import{readFile,writeFile}from'node:fs/promises';import{resolve}from'node:path';import{createHash}from'node:crypto';
const out=resolve(import.meta.dirname,'../research/liuyao-void-motion');
const [url='https://www.digital.archives.go.jp/item/4756813',file='japan-volume1-item.html']=process.argv.slice(2);
if(!/^https:\/\/www\.digital\.archives\.go\.jp\//.test(url)||!/^[a-zA-Z0-9_.-]+$/.test(file))throw Error('Only named public archive witness URLs and flat retained files');
const sha=b=>createHash('sha256').update(b).digest('hex');
const records=await readFile(resolve(out,'REQUESTS.json'),'utf8').then(JSON.parse).then(d=>d.records).catch(()=>[]);
const prev=records.find(r=>r.file===file);
if(prev){if(prev.error)throw Error('Previously failed;no automatic retry');const b=await readFile(resolve(out,file));if(b.length!==prev.bytes||sha(b)!==prev.sha256)throw Error('retained bytes changed');console.log(JSON.stringify({cached:true,...prev}));}
else{
 let response;
 try{response=await new Promise((ok,no)=>{const q=https.get(url,{headers:{'Accept-Encoding':'identity','User-Agent':'HuyenHocCac local academic source comparison'}},r=>{const chunks=[];let n=0;const tls={authorized:r.socket.authorized,authorizationError:r.socket.authorizationError||null};r.on('data',b=>{n+=b.length;if(n>64*1024*1024){q.destroy(Error('64MBwitnesslimit'));return}chunks.push(b)});r.on('end',()=>ok({status:r.statusCode,headers:r.headers,tls,body:Buffer.concat(chunks)}));r.on('error',no)});q.setTimeout(35000,()=>q.destroy(Error('timeout')));q.on('error',no)})}
 catch(e){records.push({file,url,executed:true,error:e.message,responseBodyRetained:false,retrievedUTC:new Date().toISOString()});await writeFile(resolve(out,'REQUESTS.json'),JSON.stringify({schema:'hhc.source.http.v1',records},null,2)+'\n');throw e}
 await writeFile(resolve(out,file),response.body);const r={file,url,executed:true,status:response.status,headers:response.headers,tls:response.tls,bytes:response.body.length,sha256:sha(response.body),retrievedUTC:new Date().toISOString()};records.push(r);await writeFile(resolve(out,'REQUESTS.json'),JSON.stringify({schema:'hhc.source.http.v1',records},null,2)+'\n');console.log(JSON.stringify(r));if(r.status!==200||!r.tls.authorized)throw Error('unsuccessful HTTPS;retained status body only');
}
