import {readFile,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import path from 'node:path';
const root=path.resolve('v53/research/full-study/yi');
const sha=b=>createHash('sha256').update(b).digest('hex');
const read=async f=>JSON.parse(await readFile(f,'utf8'));
const check=(ok,msg)=>{if(!ok)throw new Error(msg)};
const han=s=>s.normalize('NFC').replace(/[\p{P}\p{Z}\p{S}\s]/gu,'');
const manual=await read(path.join(root,'manual-readings.json'));
const anchors=await read(path.join(root,'manual-hexagram-anchors.json'));
const extracted=await read(path.join(root,'extracted-pages.json'));
const baselineBytes=await readFile('v49/data/yi_research.json');
const baseline=JSON.parse(baselineBytes);
const sources=[];
for(const f of ['NCPSSD-71014695_周易四卷_第一册.pdf.provenance.json','NCPSSD-71014696_周易四卷_第二册.pdf.provenance.json']) {
 const r=await read(path.join(root,f));
 const b=await readFile(path.join(root,r.file));
 check(b.length===r.bytes && sha(b)===r.sha256,'Source byte/hash mismatch '+r.file);
 const m=await readFile(path.join(root,r.metadataFile));
 check(sha(m)===r.metadataSha256,'Metadata hash mismatch '+r.metadataFile);
 sources.push(r);
}
for(const r of await read(path.join(root,'description-provenance.json'))) {
 const b=await readFile(path.join(root,r.file));
 check(b.length===r.bytes && sha(b)===r.sha256,'Description hash mismatch '+r.file);
}
const imageMap=new Map();
for(const r of extracted.pages) {
 const b=await readFile(path.join(root,r.image));
 check(b.length===r.bytes && sha(b)===r.sha256,'Page raster hash mismatch '+r.image);
 imageMap.set(r.book+':'+r.pdfPage,r);
}
check(extracted.pages.length===209,'Expected 97+112 PDF pages');
check(anchors.rows.length===64,'64 anchors required');
check(new Set(anchors.rows.map(r=>r[0])).size===64,'Duplicate hexagram anchor');
check(anchors.rows.every(r=>r[0]>=1&&r[0]<=64&&imageMap.has(r[1]+':'+r[2])&&r[3].length>0),'Invalid anchor');
const verifiedTargets=[];
for(const r of manual.readings) {
 const h=baseline.hexagrams.find(h=>h.hexagram===r.hexagram);
 const old=h.lines.find(l=>l.position===r.position);
 check(old.status==='explicit-glyph-variant','Target was not classified explicit-glyph-variant in V49: '+r.hexagram+'.'+r.position);
 check(imageMap.has(r.book+':'+r.pdfPage),'Missing target image');
 const scan=han(r.readingHanUnpunctuated);
 check(scan===r.readingHanUnpunctuated,'Manual diplomatic transcript includes punctuation');
 verifiedTargets.push({...r,sourceImageSha256:imageMap.get(r.book+':'+r.pdfPage).sha256,baselineOriginal:old.original,baselineWikisource:old.sourceLine,baselineWikisourceVariants:old.sourceVariants,baselineWikisourceSource:h.source,exactHanAgreesWithApp:scan===han(old.original),exactHanAgreesWithWikisource:scan===han(old.sourceLine)});
}
check(verifiedTargets.length===7 && new Set(verifiedTargets.map(r=>r.hexagram+'.'+r.position)).size===7,'Exactly seven distinct target readings required');
const lineQueue=baseline.hexagrams.flatMap(h=>h.lines.map(l=>{
 const target=verifiedTargets.find(r=>r.hexagram===h.hexagram&&r.position===l.position);
 const [id,book,pdfPage,anchorRead]=anchors.rows.find(r=>r[0]===h.hexagram);
 return {hexagram:id,han:h.han,position:l.position,lineLabel:l.sourceLineLabel,facsimileCollationStatus:target?'manually-read-and-collated':'not-yet-read-and-collated',...(target?{targetImage:target.image}:{}),navigationAnchor:{book,pdfPage,image:imageMap.get(book+':'+pdfPage).image,anchorRead},baselineV49PairStatus:l.status};
}));
check(lineQueue.length===384,'Expected 384 ordinary yao positions');
const enrichedAnchors=anchors.rows.map(([hexagram,book,pdfPage,anchorRead])=>({hexagram,han:baseline.hexagrams.find(h=>h.hexagram===hexagram).han,book,pdfPage,image:imageMap.get(book+':'+pdfPage).image,imageSha256:imageMap.get(book+':'+pdfPage).sha256,anchorRead,status:'visually-identified-witness-anchor-not-full-yao-collation',pdfUrl:sources.find(s=>s.title.includes(book===1?'第一册':'第二册')).binaryUrl+'#page='+pdfPage}));
const output={schema:'hhc.full-study.yi-facsimile-audit.v1',createdAt:new Date().toISOString(),baseline:{file:'v49/data/yi_research.json',sha256:sha(baselineBytes)},summary:{sourcePdfs:2,pdfPages:209,extractedImageHashesVerified:209,hexagramAnchorsVisuallyIdentified:64,ordinaryYaoPositions:384,completeYaoStatementsManuallyReadAndCollated:verifiedTargets.length,remainingYaoStatements:384-verifiedTargets.length,scanExactAgreesWithApp:verifiedTargets.filter(r=>r.exactHanAgreesWithApp).length,scanExactAgreesWithWikisource:verifiedTargets.filter(r=>r.exactHanAgreesWithWikisource).length,scanMatchesNeither:verifiedTargets.filter(r=>!r.exactHanAgreesWithApp&&!r.exactHanAgreesWithWikisource).length,publisherMetadataConflicts:1},limitations:['209 page rasters are extracted bytes, not 209 pages fully transcribed.','64 navigation anchors do not certify the six yao statements for each hexagram.','Seven full yao readings provide one historical witness; no claim of agreement of all editions.','No corpus/app character is changed by this research.','乾用九 and 坤用六 are outside the 384 six-line count and uncollated.','Institution source attribution is archived Commons metadata; direct institutional catalog access was unavailable.'],sources:sources.map(({metadata,...r})=>r),edition:manual.edition,verifiedTargets,hexagramAnchors:enrichedAnchors};
await writeFile(path.join(root,'facsimile-audit.json'),JSON.stringify(output,null,2)+'\n');
await writeFile(path.join(root,'yao-384-collation-queue.initial-seven.json'),JSON.stringify({schema:'hhc.full-study.yi-collation-queue.v1',countPolicy:manual.countPolicy,positions:lineQueue},null,2)+'\n');
await writeFile(path.join(root,'hexagram-64-page-matrix.csv'),'hexagram,han,book,pdfPage,status,image,anchorRead\n'+enrichedAnchors.map(r=>[r.hexagram,r.han,r.book,r.pdfPage,r.status,r.image,r.anchorRead].map(x=>'"'+String(x).replaceAll('"','""')+'"').join(',')).join('\n')+'\n');
console.log(JSON.stringify(output.summary,null,2));
