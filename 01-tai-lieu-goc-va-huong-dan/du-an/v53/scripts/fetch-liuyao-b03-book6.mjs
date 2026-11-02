import https from'node:https';import{readFile,writeFile,mkdir}from'node:fs/promises';import{resolve}from'node:path';import{createHash}from'node:crypto';
const out=resolve(import.meta.dirname,'../research/liuyao-b03-book6');await mkdir(out,{recursive:true});const sha=(b,a='sha256')=>createHash(a).update(b).digest('hex');
let records=await readFile(resolve(out,'REQUESTS.json'),'utf8').then(JSON.parse).then(d=>d.records).catch(()=>[]);
async function get(url,file){
 if(!['commons.wikimedia.org','upload.wikimedia.org'].includes(new URL(url).hostname)||new URL(url).protocol!=='https:')throw Error('PublicCommonsHTTPSonly');
 const previous=records.find(r=>r.file===file);if(previous){if(previous.error)throw Error('Retainedfailedrequest;noautomaticretry');const b=await readFile(resolve(out,file));if(b.length!==previous.bytes||sha(b)!==previous.sha256||previous.status!==200||!previous.tls.authorized)throw Error('Cachedidentity/statusmismatch');return b}
 let r;try{r=await new Promise((ok,no)=>{const q=https.get(url,{headers:{'Accept-Encoding':'identity','User-Agent':'HuyenHocCac local academic source comparison'}},s=>{const chunks=[];let size=0;const tls={authorized:s.socket.authorized,authorizationError:s.socket.authorizationError||null};s.on('data',b=>{size+=b.length;if(size>128*1024*1024){q.destroy(Error('128MBboundedsourcelimit'));return}chunks.push(b)});s.on('end',()=>ok({status:s.statusCode,headers:s.headers,tls,body:Buffer.concat(chunks)}));s.on('error',no)});q.setTimeout(45000,()=>q.destroy(Error('timeout')));q.on('error',no)})}catch(e){records.push({file,url,executed:true,error:e.message,responseBodyRetained:false,retrievedUTC:new Date().toISOString()});await writeFile(resolve(out,'REQUESTS.json'),JSON.stringify({schema:'hhc.source.http.v1',records},null,2)+'\n');throw e}
 await writeFile(resolve(out,file),r.body);const item={file,url,executed:true,status:r.status,headers:r.headers,tls:r.tls,bytes:r.body.length,sha256:sha(r.body),sha1:sha(r.body,'sha1'),retrievedUTC:new Date().toISOString()};records.push(item);await writeFile(resolve(out,'REQUESTS.json'),JSON.stringify({schema:'hhc.source.http.v1',records},null,2)+'\n');if(r.status!==200||!r.tls.authorized)throw Error('UnsuccessfulHTTPS;bodyretainedasstatusonly');return r.body;
}
const title='File:NLC892-GBZX0301013045-259424 卜筮正宗 十四卷 第6冊.pdf',url='https://commons.wikimedia.org/w/api.php?'+new URLSearchParams({action:'query',format:'json',prop:'imageinfo|revisions',titles:title,iiprop:'url|size|sha1|metadata|extmetadata',rvprop:'ids|timestamp|content',rvslots:'main'});
const d=JSON.parse(await get(url,'b03-book6-commons-api.json')),page=Object.values(d.query.pages)[0];if(!page.imageinfo?.[0])throw Error('Missingfile');const info=page.imageinfo[0],b=await get(info.url,'NLC892-GBZX0301013045-259424.pdf');
if(b.subarray(0,5).toString()!=='%PDF-'||b.length!==info.size||sha(b,'sha1')!==info.sha1)throw Error('PDFbyte/APIidentitymismatch');
const result={date:'2026-10-27',sourceID:'B03-book6',file:'NLC892-GBZX0301013045-259424.pdf',title,descriptionRevision:page.revisions?.[0]?.revid,
 descriptionTimestamp:page.revisions?.[0]?.timestamp,commonsURL:'https://commons.wikimedia.org/wiki/'+encodeURIComponent(title.replaceAll(' ','_')),downloadURL:info.url,
 bytes:b.length,sha256:sha(b),sha1:sha(b,'sha1'),APIPages:info.metadata?.find(m=>m.name==='Pages')?.value,
 metadataEditionIsDirectImprintVerification:false,physicalBookOrdinal:6,wholeWorkRead:false,sourceInstructionsAreData:true};
await writeFile(resolve(out,'ACQUISITION.json'),JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify(result));



