import https from'node:https';
import{readFile,writeFile,mkdir}from'node:fs/promises';
import{resolve}from'node:path';
import{createHash}from'node:crypto';
const out=resolve(import.meta.dirname,'../research/fortune-followup');await mkdir(out,{recursive:true});
let records=[];try{records=JSON.parse(await readFile(resolve(out,'REQUESTS.json'),'utf8')).records}catch{}
async function save(url,filename,depth=0){
 const file=filename+(depth?'-'+depth:'')+(/\.(json|jpg|png|pdf)$/.test(filename)?'':'.html');let record=records.find(x=>x.url===url&&x.file===file),body;
 if(record)body=await readFile(resolve(out,file));
 else{
  const r=await new Promise((ok,no)=>{const q=https.get(url,{headers:{'User-Agent':'HuyenHocCac-LocalResearch/1.0','Accept-Encoding':'identity'}},res=>{const tls={authorized:res.socket.authorized,protocol:res.socket.getProtocol()};const chunks=[];res.on('data',b=>chunks.push(b));res.on('end',()=>ok({status:res.statusCode,headers:res.headers,tls,body:Buffer.concat(chunks)}))});q.setTimeout(20000,()=>q.destroy(Error('timeout')));q.on('error',no)});
  body=r.body;await writeFile(resolve(out,file),body);record={url,file,status:r.status,headers:r.headers,tls:r.tls,bytes:body.length,sha256:createHash('sha256').update(body).digest('hex'),retrievedUTC:new Date().toISOString()};records.push(record);await writeFile(resolve(out,'REQUESTS.json'),JSON.stringify({records},null,2)+'\n');
 }
 console.log(record.status,url,record.bytes);
 if(record.status>=300&&record.status<400&&record.headers.location&&depth<4){const next=new URL(record.headers.location,url);if(next.protocol!=='https:')throw Error('Non-HTTPS redirect requires a separate decision');return save(next.href,filename,depth+1)}
 if(record.status===200&&/text\/html/.test(record.headers['content-type']||''))console.log([...new Set([...body.toString().matchAll(/href=["']([^"']+)/g)].map(m=>m[1]))].filter(u=>/shuge|pdf|drive|cloud|pan\./.test(u)).slice(0,22).join('\n'));
}
for(const[url,name]of [['https://s.shuge.org/zwdsqs','download-links'],['https://www.digital.archives.go.jp/file/1078787','official-catalog'],['https://f.shuge.org/dl/script.js?v=20260925e','download-page-script'],['https://www.digital.archives.go.jp/img/4468520','official-viewer'],['https://www.digital.archives.go.jp/api/iiif/4468520/manifest.json','official-manifest.json']])try{await save(url,name)}catch(e){console.log(name,e.message)}
const pageArg=process.argv.find(x=>x.startsWith('--pages='));
if(pageArg){const manifest=JSON.parse(await readFile(resolve(out,'official-manifest.json'),'utf8')),viewer=await readFile(resolve(out,'official-viewer.html'),'utf8'),content=JSON.parse(viewer.match(/var najContentList = (\[.*?\]);/s)[1]);for(const page of pageArg.slice(8).split(',').map(Number)){if(!Number.isInteger(page)||page<1||page>manifest.sequences[0].canvases.length)throw Error('Invalid canvas number');if(content[page-1].restricted)throw Error('Restricted image skipped');const resource=manifest.sequences[0].canvases[page-1].images[0].resource;await save(resource.service['@id']+'/full/2200,/0/native.jpg',`official-${String(page).padStart(3,'0')}.jpg`)}}
