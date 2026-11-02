import{readFile,writeFile}from'node:fs/promises';import{resolve}from'node:path';import{createHash}from'node:crypto';import vm from'node:vm';import assert from'node:assert/strict';
const r=resolve(import.meta.dirname,'..'),w=resolve(r,'..'),b=resolve(r,'research/bazi-jianlu-context'),v=resolve(b,'volume3'),read=async p=>JSON.parse(await readFile(p,'utf8')),sha=x=>createHash('sha256').update(x).digest('hex');
const identity=await read(resolve(v,'IDENTITY.json')),renders=await read(resolve(v,'RENDERS.json')),raw=await readFile(resolve(v,'CADAL06066039.djvu')),code=await readFile(resolve(w,renders.decoder));
assert.equal(sha(raw),identity.actualSHA256);assert.equal(sha(code),renders.decoderSHA256);
globalThis.self=globalThis;globalThis.document={};globalThis.ImageData=class{constructor(a,b,c){if(typeof a==='number'){this.width=a;this.height=b;this.data=new Uint8ClampedArray(a*b*4)}else{this.data=a;this.width=b;this.height=c}}};
vm.runInThisContext(code.toString());const doc=new DjVu.Document(raw.buffer.slice(raw.byteOffset,raw.byteOffset+raw.length));assert.equal(doc.getPagesQuantity(),230);
const records=[];
for(const page of[113,119]){
 const im=(await doc.getPage(page)).getImageData(),expected=renders.records.find(x=>x.page===page);assert.equal(sha(Buffer.from(im.data)),expected.pixelRGBA_SHA256);assert.deepEqual([im.width,im.height],[expected.width,expected.height]);
 records.push({page,pixelRGBA_SHA256:expected.pixelRGBA_SHA256,actualUnmodifiedDecoderPixelMatch:true});
}
await writeFile(resolve(r,'qa/bazi-jianlu-context/VOLUME3_DECODE_RESULTS.json'),JSON.stringify({date:'2026-10-27',sourceSHA256:identity.actualSHA256,decoderSHA256:renders.decoderSHA256,actualContainerPages:230,records,newPNGFiles:0,newHTTPRequests:0},null,2)+'\n');
console.log('Unmodified decoder reproduced native113/119 pixels; no new image or HTTP.');
