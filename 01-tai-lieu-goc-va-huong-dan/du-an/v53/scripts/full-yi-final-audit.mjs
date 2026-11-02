import {readFile,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import path from 'node:path';
const root=path.resolve('v53/research/full-study/yi');
const sha=b=>createHash('sha256').update(b).digest('hex');
const read=async f=>JSON.parse(await readFile(path.join(root,f),'utf8'));
const check=(ok,msg)=>{if(!ok)throw new Error(msg)};
const han=s=>s.normalize('NFC').replace(/[\p{P}\p{Z}\p{S}\s]/gu,'');
const progress=await read('full-384-progress.json');
const initial=await read('facsimile-audit.json');
const supplementary=await read('supplementary-readings.json');
const pages=(await read('extracted-pages.json')).pages;
const imageMap=new Map(pages.map(p=>[p.book+':'+p.pdfPage,p]));
const baseline=await readFile('v49/data/yi_research.json');
check(sha(baseline)===initial.baseline.sha256,'V49 baseline changed');
for(const s of initial.sources){const b=await readFile(path.join(root,s.file));check(b.length===s.bytes&&sha(b)===s.sha256,'PDF hash mismatch '+s.file)}
for(const p of pages){const b=await readFile(path.join(root,p.image));check(b.length===p.bytes&&sha(b)===p.sha256,'Image hash mismatch '+p.image)}
const transcript=new Map();
for(const c of progress.checkpoints){
 const b=await readFile(path.join(root,c.file));check(sha(b)===c.sha256,'Checkpoint changed: rerun full-yi-progress first');
 for(const r of JSON.parse(b).rows){const [h,pos,book,ns,text]=r;const key=h+'.'+pos;check(!transcript.has(key),'Duplicate '+key);transcript.set(key,{book,ns,text})}
}
check(transcript.size===384&&progress.summary.manuallyReadAndCollated===384,'384 complete transcriptions required');
for(const r of progress.positions){
 const t=transcript.get(r.hexagram+'.'+r.position);check(t&&t.text===r.readingHanUnpunctuated,'Transcript mismatch');
 check(r.method.startsWith('manual-visual-transcription')&&r.status==='manually-read-and-collated','Read status mismatch');
 check(r.sourceImages.length===t.ns.length,'Reference count mismatch');
 for(const s of r.sourceImages){const p=imageMap.get(s.book+':'+s.pdfPage);check(p&&p.sha256===s.sha256,'Image reference mismatch')}
 check(han(r.baselineApp)===r.readingHanUnpunctuated===r.exactHanAgreesWithApp,'App comparison mismatch');
 check(han(r.baselineWikisource)===r.readingHanUnpunctuated===r.exactHanAgreesWithWikisource,'Wikisource comparison mismatch');
}
check(supplementary.readings.length===2,'Two supplementary readings required');
const extras=supplementary.readings.map(r=>{const p=imageMap.get(r.book+':'+r.pdfPage);check(p&&r.readingHanUnpunctuated===han(r.readingHanUnpunctuated),'Invalid supplementary row');return {...r,method:supplementary.method,sourceImage:p.image,sourceImageSha256:p.sha256}});
check(extras[0].label==='用九'&&extras[0].readingHanUnpunctuated==='見羣龍无首吉','用九 reading changed');
check(extras[1].label==='用六'&&extras[1].readingHanUnpunctuated==='利永貞','用六 reading changed');
const rows=progress.positions.map(r=>({...r,facsimileCollationStatus:r.status}));
const differences=rows.filter(r=>!r.exactHanAgreesWithApp||!r.exactHanAgreesWithWikisource);
const summary={...progress.summary,supplementaryStatementsManuallyRead:extras.length,sourcePdfs:2,independentHistoricalEditions:1,pdfPages:209,pageImageHashesVerified:pages.length,checkpointFilesVerified:progress.checkpoints.length,rowsDifferingFromApp:rows.filter(r=>!r.exactHanAgreesWithApp).length,rowsDifferingFromWikisource:rows.filter(r=>!r.exactHanAgreesWithWikisource).length,rowsDifferingFromEither: differences.length};
const output={schema:'hhc.full-study.yi-facsimile-384-audit.v1',createdAt:new Date().toISOString(),summary,baseline:initial.baseline,sources:initial.sources,edition:initial.edition,checkpoints:progress.checkpoints,method:supplementary.method,comparisonPolicy:'NFC, punctuation/spacing removed, no allograph folding. A mismatch is not automatically a source error.',scope:'Six ordinary yao for each of 64 hexagrams; supplementary 用九/用六 separate. One visually inspected edition only; no full commentary transcription.',limitations:(await read('manual-review-notes.json')).limitations,supplementary:extras,differences};
await writeFile(path.join(root,'facsimile-384-audit.json'),JSON.stringify(output,null,2)+'\n');
await writeFile(path.join(root,'yao-384-collation-queue.json'),JSON.stringify({schema:'hhc.full-study.yi-collation-queue.v2',countPolicy:output.scope,summary,positions:rows},null,2)+'\n');
const csv=xs=>xs.map(x=>'"'+String(x).replaceAll('"','""')+'"').join(',');
await writeFile(path.join(root,'yao-384-transcription.csv'),'hexagram,han,position,label,book,pdfPages,readingHan,method,imageSHA256,agreesWithApp,agreesWithWikisource\n'+rows.map(r=>csv([r.hexagram,r.han,r.position,r.lineLabel,r.sourceImages[0].book,r.sourceImages.map(s=>s.pdfPage).join('|'),r.readingHanUnpunctuated,r.method,r.sourceImages.map(s=>s.sha256).join('|'),r.exactHanAgreesWithApp,r.exactHanAgreesWithWikisource])).join('\n')+'\n');
await writeFile(path.join(root,'variant-review.csv'),'hexagram,position,book,pdfPages,scan,app,wikisource\n'+differences.map(r=>csv([r.hexagram,r.position,r.sourceImages[0].book,r.sourceImages.map(s=>s.pdfPage).join('|'),r.readingHanUnpunctuated,r.baselineApp,r.baselineWikisource])).join('\n')+'\n');
console.log(JSON.stringify({result:'PASS',...summary}));
