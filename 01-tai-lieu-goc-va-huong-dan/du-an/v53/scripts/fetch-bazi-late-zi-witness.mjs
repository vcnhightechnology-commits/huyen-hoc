import https from 'node:https';
import {readFile,writeFile,mkdir} from 'node:fs/promises';
import {resolve} from 'node:path';
import {createHash} from 'node:crypto';
const out=resolve(import.meta.dirname,'../research/bazi-late-zi-witness');
await mkdir(out,{recursive:true});
const sha=(b,alg='sha256')=>createHash(alg).update(b).digest('hex');
let records=await readFile(resolve(out,'REQUESTS.json'),'utf8').then(JSON.parse).then(j=>j.records).catch(()=>[]);
async function get(url,file){
 const prior=records.find(r=>r.file===file);
 if(prior){const b=await readFile(resolve(out,file));if(b.length!==prior.bytes||sha(b)!==prior.sha256)throw Error('Cache mismatch '+file);if(prior.status!==200||!prior.tls.authorized)throw Error('Cached response is not successful HTTPS');return b;}
 const r=await new Promise((ok,no)=>{const q=https.get(url,{headers:{'Accept-Encoding':'identity','User-Agent':'HuyenHocCac local textual comparison'}},res=>{const tls={authorized:res.socket.authorized,authorizationError:res.socket.authorizationError||null},chunks=[];res.on('data',b=>chunks.push(b));res.on('end',()=>ok({status:res.statusCode,headers:res.headers,tls,body:Buffer.concat(chunks)}));res.on('error',no)});q.setTimeout(45000,()=>q.destroy(Error('timeout')));q.on('error',no)});
 await writeFile(resolve(out,file),r.body);const record={file,url,status:r.status,headers:r.headers,tls:r.tls,bytes:r.body.length,sha256:sha(r.body),sha1:sha(r.body,'sha1'),retrievedUTC:new Date().toISOString()};records.push(record);await writeFile(resolve(out,'REQUESTS.json'),JSON.stringify({schema:'hhc.source.http.v1',records},null,2)+'\n');console.log(file,r.status,record.bytes,record.sha256);
 if(r.status!==200||!r.tls.authorized)throw Error('Unsuccessful public HTTPS '+file);return r.body;
}
const title='File:NCL-000002203 新命理探原.pdf';
const info=JSON.parse(await get('https://commons.wikimedia.org/w/api.php?'+new URLSearchParams({action:'query',format:'json',titles:title,prop:'imageinfo',iiprop:'url|size|sha1|extmetadata'}),'commons-imageinfo.json'));
const item=Object.values(info.query.pages)[0].imageinfo[0];
await get('https://commons.wikimedia.org/w/index.php?'+new URLSearchParams({title,oldid:'1029746256'}),'commons-description.html');
await get('https://taiwanebook.ncl.edu.tw/zh-tw/book/NCL-000002203','ncl-catalog.html');
const b=await get(item.url,'NCL-000002203.pdf');
if(b.length!==item.size||sha(b,'sha1')!==item.sha1||b.subarray(0,5).toString()!=='%PDF-')throw Error('PDF/API identity mismatch');
console.log(JSON.stringify({bytes:b.length,sha256:sha(b),sha1:sha(b,'sha1'),url:item.url}));
