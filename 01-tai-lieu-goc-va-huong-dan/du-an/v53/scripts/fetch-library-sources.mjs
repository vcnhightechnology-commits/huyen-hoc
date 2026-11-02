import https from 'node:https';
import {mkdir,readFile,writeFile} from 'node:fs/promises';
import {resolve} from 'node:path';
import {createHash} from 'node:crypto';
const root=resolve(import.meta.dirname,'..'),out=resolve(root,'research/library-audit/new-sources');await mkdir(out,{recursive:true});
const sha=b=>createHash('sha256').update(b).digest('hex');let records=[];try{records=JSON.parse(await readFile(resolve(out,'MANIFEST.json'),'utf8')).files}catch{}
function get(url,count=0){return new Promise((done,fail)=>{const req=https.get(encodeURI(url),{headers:{'User-Agent':'HuyenHocCac-LocalResearch/1.0','Accept-Encoding':'identity'}},r=>{if([301,302,303,307,308].includes(r.statusCode)&&r.headers.location&&count<5){r.resume();get(new URL(r.headers.location,url).href,count+1).then(done,fail);return}const tls={authorized:r.socket?.authorized===true,protocol:r.socket?.getProtocol?.()};const chunks=[];r.on('data',b=>chunks.push(b));r.on('end',()=>done({url,status:r.statusCode,headers:r.headers,tls,body:Buffer.concat(chunks)}));r.on('error',fail)});req.setTimeout(20000,()=>req.destroy(Error('Request timeout')));req.on('error',fail)})}
async function capture(file,url,role){const prior=records.find(x=>x.file===file&&x.requestedURL===url);if(prior){if(prior.sha256){const b=await readFile(resolve(out,file));if(sha(b)!==prior.sha256)throw Error('Saved body changed: '+file);return{record:prior,body:b}}return{record:prior}}
try{const r=await get(url),record={file,requestedURL:url,finalURL:r.url,retrievedUTC:new Date().toISOString(),status:r.status,bytes:r.body.length,sha256:sha(r.body),headers:r.headers,tls:r.tls,usable:r.status===200,role,transport:'HTTPS certificate validation enabled; Accept-Encoding identity; body saved without text conversion'};await writeFile(resolve(out,file),r.body);records.push(record);console.log(file,r.status,r.body.length);return{record,body:r.body}}catch(e){const record={file,requestedURL:url,retrievedUTC:new Date().toISOString(),usable:false,error:e.message,role};records.push(record);console.log(file,e.message);return{record}}finally{await writeFile(resolve(out,'MANIFEST.json'),JSON.stringify({schema:'hhc.library.additional-sources.v1',files:records},null,2)+'\n')}}
await Promise.allSettled([
 capture('ndl-760737-catalog.html','https://ndlsearch.ndl.go.jp/books/R100000039-I760737','Institutional catalogue; Japanese adaptation, not the Chinese original'),
 capture('ndl-760737-iiif.json','https://dl.ndl.go.jp/api/iiif/760737/manifest.json','IIIF manifest linked by institutional catalogue; not itself a book image'),
 capture('archive-06066037-metadata.json','https://archive.org/metadata/06066037.cn','Metadata for the old M02 catalogue link; not a downloaded book'),
 capture('wikisource-zhaijing.html','https://zh.wikisource.org/zh-hant/宅經','Digital witness for old P03; not yet facsimile-verified'),
 capture('wikisource-yuanhai.html','https://zh.wikisource.org/wiki/淵海子平','Quality audit of cited digital text; check incomplete/source-warning labels')
]);
const repositories=[];
for(const [repo,branch]of [['KR3g0019','WYG'],['KR5a0294','HFL']]){
 const commit=await capture(`${repo}-commit.json`,`https://api.github.com/repos/kanripo/${repo}/commits/${branch}`,'Maintainer commit metadata for a named text edition');
 if(!commit.record.usable)continue;const data=JSON.parse(commit.body),revision=data.sha;if(!/^[a-f0-9]{40}$/.test(revision))throw Error('No immutable commit');repositories.push({repo,branch,revision});
 for(const file of ['Readme.org',...['000','001','002'].map(n=>`${repo}_${n}.txt`)])await capture(`${repo}-${file}`,`https://raw.githubusercontent.com/kanripo/${repo}/${revision}/${file}`,'Edition-labeled transcription at immutable commit; not independently authenticated facsimile');
}
const ndl=records.find(x=>x.file==='ndl-760737-iiif.json');if(ndl?.usable){const m=JSON.parse(await readFile(resolve(out,ndl.file),'utf8')),canvases=m.sequences?.[0]?.canvases?.map((c,i)=>({index:i,label:c.label,id:c['@id'],image:c.images?.[0]?.resource}))||m.items||[];await writeFile(resolve(out,'ndl-760737-canvas-index.json'),JSON.stringify(canvases,null,2)+'\n');for(let i=0;i<canvases.length;i+=3)await Promise.all(canvases.slice(i,i+3).map(c=>capture(`ndl-760737-${String(c.index+1).padStart(2,'0')}.jpg`,c.image['@id'],'Original IIIF JPEG from the institutional manifest; canvas label '+c.label+'; not a physical leaf number')))}
await writeFile(resolve(out,'MANIFEST.json'),JSON.stringify({schema:'hhc.library.additional-sources.v1',files:records},null,2)+'\n');
await writeFile(resolve(out,'REVISIONS.json'),JSON.stringify({repositories,note:'Edition identity is that declared by the maintainer. An immutable commit plus SHA establishes reproducibility, not textual correctness or predictive validity.'},null,2)+'\n');
