import{readFile,writeFile}from'node:fs/promises';import{resolve}from'node:path';import{createHash}from'node:crypto';import vm from'node:vm';import assert from'node:assert/strict';
const r=resolve(import.meta.dirname,'..'),w=resolve(r,'..'),b=resolve(r,'research/bazi-jianlu-context'),d=JSON.parse(await readFile(resolve(b,'SOURCE_MANIFEST.json'),'utf8')),sha=x=>createHash('sha256').update(x).digest('hex');
const raw=await readFile(resolve(w,d.sourceContainer)),code=await readFile(resolve(w,d.decoder));assert.equal(sha(raw),d.sourceSHA256);assert.equal(sha(code),d.decoderSHA256);
globalThis.self=globalThis;globalThis.document={};globalThis.ImageData=class{constructor(a,b,c){if(typeof a==='number'){this.width=a;this.height=b;this.data=new Uint8ClampedArray(a*b*4)}else{this.data=a;this.width=b;this.height=c}}};
vm.runInThisContext(code.toString());const doc=new DjVu.Document(raw.buffer.slice(raw.byteOffset,raw.byteOffset+raw.length));assert.equal(doc.getPagesQuantity(),226);
const im=(await doc.getPage(226)).getImageData(),expected=d.newEndTitlePage;assert.equal(sha(Buffer.from(im.data)),expected.pixelRGBA_SHA256);assert.deepEqual([im.width,im.height],[expected.width,expected.height]);
await writeFile(resolve(r,'qa/bazi-jianlu-context/DECODE_RESULTS.json'),JSON.stringify({date:'2026-10-27',sourceSHA256:d.sourceSHA256,decoderSHA256:d.decoderSHA256,page:226,pixelRGBA_SHA256:expected.pixelRGBA_SHA256,actualUnmodifiedDecoderPixelMatch:true,newPNGFiles:0,newHTTPRequests:0},null,2)+'\n');
console.log('Unmodified decoder reproduced ending226 pixels; no new image or HTTP request.');
