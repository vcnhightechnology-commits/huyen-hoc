import {readFile,writeFile} from 'node:fs/promises';
import {resolve} from 'node:path';
import {createHash} from 'node:crypto';
import {deflateSync} from 'node:zlib';
import vm from 'node:vm';
import assert from 'node:assert/strict';
const w=process.cwd(),b=resolve(w,'tmp/bazi-ten-stem-life-staging'),sha=x=>createHash('sha256').update(x).digest('hex');
const raw=await readFile(resolve(w,'v53/research/bazi-season-strength/CADAL06066038.djvu')),code=await readFile(resolve(w,'v53/research/bazi-pattern-extension/tooling/djvu.js'));
assert.equal(sha(raw),'7a53f35982f0b946281d0e393c5d6ddcce1fd091aea83c11af6a06bcdfe6a85e');assert.equal(sha(code),'10a831d62cc7ced39c30c7350a11410402d082a0f0a5b073a88d3d7ca662add3');
globalThis.self=globalThis;globalThis.document={};globalThis.ImageData=class{constructor(a,b,c){if(typeof a==='number'){this.width=a;this.height=b;this.data=new Uint8ClampedArray(a*b*4)}else{this.data=a;this.width=b;this.height=c}}};
vm.runInThisContext(code.toString());const doc=new DjVu.Document(raw.buffer.slice(raw.byteOffset,raw.byteOffset+raw.length));assert.equal(doc.getPagesQuantity(),232);
const crcTable=Array.from({length:256},(_,n)=>{for(let k=0;k<8;k++)n=n&1?0xedb88320^(n>>>1):n>>>1;return n>>>0});
function chunk(type,data){const tag=Buffer.from(type),len=Buffer.alloc(4),crc=Buffer.alloc(4);len.writeUInt32BE(data.length);let v=0xffffffff;for(const x of Buffer.concat([tag,data]))v=crcTable[(v^x)&255]^(v>>>8);crc.writeUInt32BE((v^0xffffffff)>>>0);return Buffer.concat([len,tag,data,crc])}
function png(im){const head=Buffer.alloc(13);head.writeUInt32BE(im.width);head.writeUInt32BE(im.height,4);head[8]=8;head[9]=6;const stride=im.width*4,pixels=Buffer.from(im.data),rows=Buffer.alloc((stride+1)*im.height);for(let y=0;y<im.height;y++)pixels.copy(rows,y*(stride+1)+1,y*stride,(y+1)*stride);return Buffer.concat([Buffer.from([137,80,78,71,13,10,26,10]),chunk('IHDR',head),chunk('IDAT',deflateSync(rows)),chunk('IEND',Buffer.alloc(0))])}
const records=[];
for(const page of[11,12,13,14,16,18,20,21,23,25,27,29,30,31,34]){const im=(await doc.getPage(page)).getImageData(),p=png(im),file=`p${page}.png`;await writeFile(resolve(b,file),p);records.push({page,file,bytes:p.length,sha256:sha(p),width:im.width,height:im.height,pixelRGBA_SHA256:sha(Buffer.from(im.data)),actuallyViewed:false});}
await writeFile(resolve(b,'CLAUSE_RENDERS.json'),JSON.stringify({date:'2026-10-29',source:'v53/research/bazi-season-strength/CADAL06066038.djvu',sourceSHA256:sha(raw),decoder:'v53/research/bazi-pattern-extension/tooling/djvu.js',decoderSHA256:sha(code),containerPages:232,method:'Unmodified retained decoder in NodeVM with ImageData value holder; native RGBA to lossless PNG via local zlib/CRC chunks. No browser, DOM canvas, OCR or HTTP.',records,newHTTPRequests:0,newOriginalContainers:0},null,2)+'\n');console.log('Decoded15targeted-clausepositions;unread until visual inspection.');
