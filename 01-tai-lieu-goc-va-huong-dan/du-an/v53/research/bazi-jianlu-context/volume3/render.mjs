import{readFile,writeFile,mkdir}from'node:fs/promises';import{resolve}from'node:path';import{createHash}from'node:crypto';import{deflateSync}from'node:zlib';import assert from'node:assert/strict';import vm from'node:vm';
const s=import.meta.dirname,w=resolve(s,'../..'),sha=x=>createHash('sha256').update(x).digest('hex'),identity=JSON.parse(await readFile(resolve(s,'IDENTITY.json'),'utf8'));
const raw=await readFile(resolve(s,'CADAL06066039.djvu')),decoder='v53/research/bazi-pattern-extension/tooling/djvu.js',code=await readFile(resolve(w,decoder));
assert.equal(sha(raw),identity.actualSHA256);assert.equal(sha(code),'10a831d62cc7ced39c30c7350a11410402d082a0f0a5b073a88d3d7ca662add3');
globalThis.self=globalThis;globalThis.document={};globalThis.ImageData=class{constructor(a,b,c){if(typeof a==='number'){this.width=a;this.height=b;this.data=new Uint8ClampedArray(a*b*4)}else{this.data=a;this.width=b;this.height=c}}};
vm.runInThisContext(code.toString());const doc=new DjVu.Document(raw.buffer.slice(raw.byteOffset,raw.byteOffset+raw.length));assert.equal(doc.getPagesQuantity(),230);
function crc(buf){let c=0xffffffff;for(const x of buf){c^=x;for(let k=0;k<8;k++)c=(c>>>1)^((c&1)?0xedb88320:0)}return(c^0xffffffff)>>>0;}
function chunk(name,data){const type=Buffer.from(name),len=Buffer.alloc(4),check=Buffer.alloc(4);len.writeUInt32BE(data.length);check.writeUInt32BE(crc(Buffer.concat([type,data])));return Buffer.concat([len,type,data,check]);}
function png(im){const header=Buffer.alloc(13);header.writeUInt32BE(im.width);header.writeUInt32BE(im.height,4);header[8]=8;header[9]=6;const pixels=Buffer.from(im.data),scan=Buffer.alloc((im.width*4+1)*im.height);for(let y=0;y<im.height;y++)pixels.copy(scan,y*(im.width*4+1)+1,y*im.width*4,(y+1)*im.width*4);return Buffer.concat([Buffer.from([137,80,78,71,13,10,26,10]),chunk('IHDR',header),chunk('IDAT',deflateSync(scan)),chunk('IEND',Buffer.alloc(0))]);}
await mkdir(resolve(s,'images'),{recursive:true});const log=await readFile(resolve(s,'RENDERS.json'),'utf8').then(JSON.parse).catch(()=>({date:'2026-10-27',source:'CADAL06066039.djvu',sourceSHA256:sha(raw),decoder,decoderSHA256:sha(code),actualContainerPages:230,records:[],networkRequests:0}));
for(const page of process.argv[2].split(',').map(Number)){
 assert(Number.isInteger(page)&&page>=1&&page<=230);const old=log.records.find(x=>x.page===page);if(old){assert.equal(sha(await readFile(resolve(s,old.file))),old.sha256);continue;}
 const im=(await doc.getPage(page)).getImageData(),data=png(im),file=`images/p${String(page).padStart(3,'0')}.png`;await writeFile(resolve(s,file),data);
 log.records.push({page,file,bytes:data.length,width:im.width,height:im.height,sha256:sha(data),pixelRGBA_SHA256:sha(Buffer.from(im.data)),renderedNotAutomaticallyRead:true});
 await writeFile(resolve(s,'RENDERS.json'),JSON.stringify(log,null,2)+'\n');console.log('RENDER',page,im.width,im.height);
}
