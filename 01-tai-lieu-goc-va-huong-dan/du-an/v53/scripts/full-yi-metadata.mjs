import {writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import path from 'node:path';
const out=path.resolve('v53/research/full-study/yi');
const records=[];
for(const [key,title,prop] of [
 ['book1-description-wikitext','File:NCPSSD-71014695 周易四卷 第一册.pdf','wikitext'],
 ['book2-description-wikitext','File:NCPSSD-71014696 周易四卷 第二册.pdf','wikitext'],
 ['institution-link-template','Template:National Center for Philosophy and Social Sciences Documentation link','wikitext']
]) {
 const url='https://commons.wikimedia.org/w/api.php?action=parse&page='+encodeURIComponent(title)+'&prop='+prop+'&format=json';
 const r=await fetch(url);
 if(!r.ok)throw new Error(r.status+' '+url);
 const bytes=Buffer.from(await r.arrayBuffer());
 const filename='evidence/'+key+'.json';
 await writeFile(path.join(out,filename),bytes);
 records.push({key,title,url,file:filename,bytes:bytes.length,sha256:createHash('sha256').update(bytes).digest('hex'),retrievedAt:new Date().toISOString()});
}
await writeFile(path.join(out,'description-provenance.json'),JSON.stringify(records,null,2)+'\n');
console.log(JSON.stringify(records.map(({key,bytes,sha256})=>({key,bytes,sha256}))));
