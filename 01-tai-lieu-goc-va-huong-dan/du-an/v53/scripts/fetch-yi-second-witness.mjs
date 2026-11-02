import https from 'node:https';
import {readFile,writeFile,mkdir} from 'node:fs/promises';
import {resolve} from 'node:path';
import {createHash} from 'node:crypto';
const out=resolve(import.meta.dirname,'../research/yi-second-witness');
await mkdir(out,{recursive:true});
const sha=(b,alg='sha256')=>createHash(alg).update(b).digest('hex');
let records=await readFile(resolve(out,'REQUESTS.json'),'utf8').then(JSON.parse).then(j=>j.records).catch(()=>[]);
async function get(url,file){
  const prior=records.find(r=>r.file===file);
  if(prior){const b=await readFile(resolve(out,file));if(b.length!==prior.bytes||sha(b)!==prior.sha256)throw Error('Cache mismatch '+file);return b;}
  const r=await new Promise((ok,no)=>{const q=https.get(url,{headers:{'Accept-Encoding':'identity','User-Agent':'HuyenHocCac local academic comparison'}},res=>{const tls={authorized:res.socket.authorized,authorizationError:res.socket.authorizationError||null},chunks=[];res.on('data',b=>chunks.push(b));res.on('end',()=>ok({status:res.statusCode,headers:res.headers,tls,body:Buffer.concat(chunks)}));res.on('error',no)});q.setTimeout(60000,()=>q.destroy(Error('timeout')));q.on('error',no)});
  await writeFile(resolve(out,file),r.body);
  const record={file,url,status:r.status,headers:r.headers,tls:r.tls,bytes:r.body.length,sha256:sha(r.body),sha1:sha(r.body,'sha1'),retrievedUTC:new Date().toISOString()};
  records.push(record);await writeFile(resolve(out,'REQUESTS.json'),JSON.stringify({schema:'hhc.source.http.v1',records},null,2)+'\n');
  console.log(file,r.status,record.bytes,record.sha256);
  if(r.status>=300&&r.status<400)return get(new URL(r.headers.location,url).href,file+'.redirect');
  if(r.status!==200||!r.tls.authorized)throw Error('Unsuccessful public HTTPS '+file);
  return r.body;
}
const title='File:NCL-00037 周易本義.pdf';
const info=JSON.parse(await get('https://commons.wikimedia.org/w/api.php?'+new URLSearchParams({action:'query',format:'json',titles:title,prop:'imageinfo',iiprop:'url|size|sha1|extmetadata'}),'commons-imageinfo.json'));
const image=Object.values(info.query.pages)[0].imageinfo[0];
await get('https://commons.wikimedia.org/w/index.php?'+new URLSearchParams({title,oldid:'1285710879'}),'commons-description.html');
const b=await get(image.url,'NCL-00037.pdf');
if(b.length!==image.size||sha(b,'sha1')!==image.sha1||b.subarray(0,5).toString()!=='%PDF-')throw Error('PDF public metadata mismatch');
console.log(JSON.stringify({bytes:b.length,sha256:sha(b),sha1:sha(b,'sha1'),url:image.url,metadata:image.extmetadata.ImageDescription?.value||image.extmetadata.ObjectName?.value}));
for(const [file,url] of [
 ['ncl-catalog.html','https://rbook.ncl.edu.tw/NCLSearch/Search/SearchDetail?HasImage=&SourceID=3&item=990664bd049b45f1bf5cc9775a73bce9fDUwMTYyNA2.vwK1HHFWUJf4slhqIHlmqkMaC0bDgiYTT5WZ6A_Mov0_&page=2751&sourceWhereString=&whereString=IChOVUxMSUYoRGF0ZV9DcmVhdGVkLCAnICcpIGlzIE5VTEwgYW5kIE5VTExJRihEb2N1bWVudF9ZZWFyLCAnICcpIGlzIE5VTEwgKSA1.uQrV5XxqrHh4fOCXMwOuuzssvPVRwJbumFyT4mFEUCA_'],
 ['union-catalog.html','https://catalog.digitalarchives.tw/item/00/08/62/69.html']
]){try{await get(url,file)}catch(e){console.log('Catalog fetch retained as limited evidence:',file,e.message)}}
