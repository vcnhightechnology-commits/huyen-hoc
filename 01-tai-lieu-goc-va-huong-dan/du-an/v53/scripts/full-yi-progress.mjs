import {readFile,writeFile,readdir} from 'node:fs/promises';
import path from 'node:path';
import {createHash} from 'node:crypto';
const root=path.resolve('v53/research/full-study/yi');
const read=async f=>JSON.parse(await readFile(f,'utf8'));
const sha=b=>createHash('sha256').update(b).digest('hex');
const han=s=>s.normalize('NFC').replace(/[\p{P}\p{Z}\p{S}\s]/gu,'');
const fail=(ok,msg)=>{if(!ok)throw new Error(msg)};
const b=await read('v49/data/yi_research.json');
const pages=(await read(path.join(root,'extracted-pages.json'))).pages;
const imageMap=new Map(pages.map(p=>[p.book+':'+p.pdfPage,p]));
const seen=new Map();
const checkpoints=[];
for(const f of (await readdir(root)).filter(f=>/^checkpoint-\d+\.json$/.test(f)).sort()) {
 const bytes=await readFile(path.join(root,f));const j=JSON.parse(bytes);
 const batch=new Map();
 for(const [h,pos,book,ns,text] of j.rows) {
  const key=h+'.'+pos;
  fail(!seen.has(key),'Duplicate '+key);
  fail(h>=1&&h<=64&&pos>=1&&pos<=6&&ns.length>0,'Bad position '+key);
  fail(text.length>0&&han(text)===text,'Bad transcript '+key);
  const refs=[];
  for(const n of ns) {
   const p=imageMap.get(book+':'+n);fail(p,'Missing image '+key);
   const bytes=await readFile(path.join(root,p.image));fail(sha(bytes)===p.sha256,'Changed image '+p.image);
   refs.push({book,pdfPage:n,image:p.image,sha256:p.sha256});
  }
  const old=b.hexagrams.find(x=>x.hexagram===h).lines.find(x=>x.position===pos);
  seen.set(key,{hexagram:h,position:pos,readingHanUnpunctuated:text,method:j.method,checkpoint:f,sourceImages:refs,baselineApp:old.original,baselineWikisource:old.sourceLine,exactHanAgreesWithApp:han(old.original)===text,exactHanAgreesWithWikisource:han(old.sourceLine)===text});
  batch.set(h,(batch.get(h)||0)+1);
 }
 fail([...batch.values()].every(n=>n===6),'Checkpoint must complete all six yao for each included hexagram: '+f);
 checkpoints.push({file:f,sha256:sha(bytes),rows:j.rows.length,hexagrams:[...batch.keys()]});
}
const positions=b.hexagrams.flatMap(h=>h.lines.map(l=>({hexagram:h.hexagram,han:h.han,position:l.position,lineLabel:l.sourceLineLabel,status:seen.has(h.hexagram+'.'+l.position)?'manually-read-and-collated':'not-yet-read-and-collated',...seen.get(h.hexagram+'.'+l.position)})));
const completedHexagrams=b.hexagrams.filter(h=>h.lines.every(l=>seen.has(h.hexagram+'.'+l.position))).map(h=>h.hexagram);
const summary={ordinaryYao:384,manuallyReadAndCollated:seen.size,remaining:384-seen.size,completeHexagrams:completedHexagrams.length,completeHexagramIds:completedHexagrams,ocrOnly:0,exactHanAgreesWithApp:[...seen.values()].filter(r=>r.exactHanAgreesWithApp).length,exactHanAgreesWithWikisource:[...seen.values()].filter(r=>r.exactHanAgreesWithWikisource).length,neitherExact:[...seen.values()].filter(r=>!r.exactHanAgreesWithApp&&!r.exactHanAgreesWithWikisource).length};
await writeFile(path.join(root,'full-384-progress.json'),JSON.stringify({schema:'hhc.full-study.yi-384-progress.v1',updatedAt:new Date().toISOString(),summary,checkpoints,policy:'Every completed checkpoint contains six visually read yao per hexagram. No OCR-only row is presented as manual. No public corpus is modified. 用九/用六 excluded from ordinary384.',positions},null,2)+'\n');
await writeFile(path.join(root,'FULL_384_CHECKPOINT.md'),'# Checkpoint hiệu khảo đủ384hào\n\n'+`${seen.size}/384 hào đọc trực tiếp và chép đủ; ${384-seen.size} chưa hiệu khảo; ${completedHexagrams.length}/64 quẻ đủ6hào. OCR-only:0.\n\n`+'Quẻ đã hoàn tất: '+completedHexagrams.join(', ')+'.\n\n'+"Chạy `node v53/scripts/full-yi-progress.mjs` rồi `node v53/scripts/full-yi-final-audit.mjs` để kiểm tra hash ảnh, tính duy nhất và checkpoint đủ6hào. Chi tiết trong full-384-progress.json; checkpoint giữ nguyên chữ đọc, trang PDF bắt đầu từ1. README_INITIAL_SEVEN.md/facsimile-audit.json ghi phạm vi7hào ban đầu; README.md/facsimile-384-audit.json là báo cáo hiện hành. 用九/用六 ghi riêng ngoài384 trong supplementary-readings.json. Một truyền bản, không phải đọc toàn bộ chú giải.\n");
console.log(JSON.stringify(summary));
