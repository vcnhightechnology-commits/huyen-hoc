import {mkdir, writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import path from 'node:path';

const out=path.resolve('v53/research/full-study/yi');
await mkdir(path.join(out,'evidence'),{recursive:true});
const titles=process.argv.slice(2);
for (const title of titles) {
 const stem=title.replace(/^File:/,'').replace(/ /g,'_');
 const api='https://commons.wikimedia.org/w/api.php?action=query&titles='+encodeURIComponent(title)+'&prop=imageinfo&iiprop=url%7Csize%7Cextmetadata&format=json';
 const metadataBytes=Buffer.from(await (await fetch(api)).arrayBuffer());
 const j=JSON.parse(metadataBytes);
 const p=Object.values(j.query.pages)[0];
 const ii=p.imageinfo[0];
 const binaryUrl=ii.url.split('?')[0];
 const response=await fetch(binaryUrl);
 if(!response.ok) throw new Error(response.status+' '+binaryUrl);
 const bytes=Buffer.from(await response.arrayBuffer());
 const record={retrievedAt:new Date().toISOString(),commonsPageId:p.pageid,title:p.title,metadataUrl:api,metadataFile:'evidence/'+stem+'.metadata.json',metadataSha256:createHash('sha256').update(metadataBytes).digest('hex'),binaryUrl,descriptionUrl:ii.descriptionurl,file:'evidence/'+stem,bytes:bytes.length,sha256:createHash('sha256').update(bytes).digest('hex'),pageCount:ii.pagecount,width:ii.width,height:ii.height,contentType:response.headers.get('content-type'),metadata:ii.extmetadata};
 await writeFile(path.join(out,'evidence',stem+'.metadata.json'),metadataBytes);
 await writeFile(path.join(out,'evidence',stem),bytes);
 await writeFile(path.join(out,stem+'.provenance.json'),JSON.stringify(record,null,2)+'\n');
 console.log(JSON.stringify({file:record.file,bytes:record.bytes,sha256:record.sha256,pageCount:record.pageCount}));
}
