import https from'node:https';import{writeFile,readFile}from'node:fs/promises';import{resolve}from'node:path';import{createHash}from'node:crypto';
const base=import.meta.dirname,sha=b=>createHash('sha256').update(b).digest('hex');
let ledger;try{ledger=JSON.parse(await readFile(resolve(base,'REQUESTS.json'),'utf8'));}catch{ledger={date:'2026-10-27',records:[]};}
async function fetchRaw(url,file){
 if(ledger.records.some(r=>r.url===url))throw Error('Already attempted;review retained result before another request.');
 const r=await new Promise(resolveRequest=>{
  const request=https.get(url,{headers:{'User-Agent':'HuyenHocCac-SourceResearch/1.0','Accept':'application/json,text/html,image/*;q=0.9,*/*;q=0.8'}},res=>{
   const tlsSnapshot={authorized:res.socket?.authorized??null,authorizationError:res.socket?.authorizationError??null};
   const chunks=[];res.on('data',b=>chunks.push(b));res.on('end',()=>resolveRequest({status:res.statusCode,
    headers:{'content-type':res.headers['content-type'],'content-length':res.headers['content-length'],etag:res.headers.etag,'last-modified':res.headers['last-modified']},
    tls:tlsSnapshot,body:Buffer.concat(chunks)}));
  });request.setTimeout(45000,()=>request.destroy(Error('45secondtimeout')));request.on('error',e=>resolveRequest({error:e.message}));
 });
 const record={url,file,executed:true,retrievedUTC:new Date().toISOString(),status:r.status??null,error:r.error??null,headers:r.headers??null,
  tls:r.tls??null,nodeHTTPSDefaultCertificateValidationEnforced:true};
 if(r.body){record.bytes=r.body.length;record.sha256=sha(r.body);await writeFile(resolve(base,file),r.body);}
 ledger.records.push(record);await writeFile(resolve(base,'REQUESTS.json'),JSON.stringify(ledger,null,2)+'\n');
 console.log(JSON.stringify({file,status:record.status,bytes:record.bytes,tlsAuthorized:record.tls?.authorized,error:record.error}));
 return record;
}
if(process.argv[2]==='metadata'){
 await fetchRaw('https://www.digital.archives.go.jp/item/4756814','japan-volume2-item.html');
 const r=await fetchRaw('https://www.digital.archives.go.jp/api/iiif/4756814/manifest.json','japan-volume2-manifest.json');
 if(r.status===200){const m=JSON.parse(await readFile(resolve(base,r.file),'utf8')),canvases=m.sequences[0].canvases;
  const nav=canvases.map((c,i)=>({ordinal1:i+1,id:c['@id'],label:c.label,width:c.width,height:c.height,resource:c.images[0].resource['@id']}));
  await writeFile(resolve(base,'CANVASES.json'),JSON.stringify({manifestLabel:m.label,canvases:nav},null,2)+'\n');
  console.log(JSON.stringify({label:m.label,count:nav.length,last:nav.slice(-6)}));
 }
}else{
 const nav=JSON.parse(await readFile(resolve(base,'CANVASES.json'),'utf8')).canvases;
 for(const arg of process.argv.slice(2)){const n=Number(arg),c=nav.find(c=>c.ordinal1===n);if(!c)throw Error('Unknown retained canvas ordinal.');
  await fetchRaw(c.resource,`japan-volume2-spread-${n}-returned.jpg`);
 }
}
