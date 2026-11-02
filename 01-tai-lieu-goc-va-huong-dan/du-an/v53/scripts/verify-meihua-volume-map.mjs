import {readFile,writeFile,mkdir} from 'node:fs/promises';
import {resolve} from 'node:path';
import {createHash} from 'node:crypto';
import vm from 'node:vm';
import assert from 'node:assert/strict';

const root=resolve(import.meta.dirname,'..'),base=resolve(root,'research/meihua-volume-map'),qa=resolve(root,'qa/meihua-volume-map');
const json=async p=>JSON.parse(await readFile(p,'utf8')), sha=b=>createHash('sha256').update(b).digest('hex');
const checks=[];const test=(name,detail)=>{checks.push({name,ok:true,detail});console.log('PASS',name)};
await mkdir(qa,{recursive:true});
const manual=await json(resolve(base,'MANUAL_READINGS.json')),prior=await json(resolve(root,'research/meihua-witness/MANUAL_READINGS.json'));
const pdf=await readFile(resolve(base,manual.sourcePDF));
assert.equal(pdf.length,5621631);assert.equal(sha(pdf),manual.sourcePDFSHA256);
for(const r of manual.records)assert.equal(sha(await readFile(resolve(base,r.image))),r.imageSHA256);
assert.equal(manual.records.length,47);assert.equal(manual.newHTTPResponses,0);assert.equal(manual.newRenderedDerivatives,0);
test('Retained original PDF and all47new bounded reading records have exact source-image hashes;no new HTTP or rendered image');

const expected=[...Array.from({length:29},(_,i)=>150+i),...Array.from({length:11},(_,i)=>209+i),...Array.from({length:7},(_,i)=>221+i)];
assert.deepEqual(manual.records.map(r=>r.pdfPage),expected);
assert.ok(manual.records.every(r=>r.printedPage===r.pdfPage-(r.volume===4?144:188)));
const all=[...new Set([...manual.records,...prior.records].filter(r=>r.pdfPage>=145&&r.pdfPage<=228).map(r=>r.pdfPage))].sort((a,b)=>a-b);
assert.deepEqual(all,Array.from({length:84},(_,i)=>145+i));
assert.equal(prior.records.length,41);assert.equal(manual.wholeBookRead,false);
test('47new pages plus retained35content/two endleaf records span all84pages of printed volumes4/5;navigation is not full reading');

const units=await json(resolve(base,'UNIT_MAP.json')),old=await json(resolve(root,'research/meihua-witness/UNIT_MAP.json'));
assert.equal(units.units.length,93);assert.equal(units.newUnitGroups,59);
assert.equal(new Set(units.units.map(u=>u.id)).size,93);
for(const u of old.units)assert.ok(units.units.some(v=>v.id===u.id));
assert.ok(units.units.every(u=>!u.wholeUnitApplied&&!u.fullClauseExtractionCompleted));
assert.equal(units.volumeFourFivePageNavigationComplete,true);assert.equal(units.wholePrintedInventoryCompleted,false);assert.equal(units.wholeBookApplied,false);
assert.deepEqual(units.mappedPDFPages,all);assert.equal(units.contentPages,82);
const unitPages=new Set(units.units.flatMap(u=>u.evidencePDFPages));
assert.ok(all.filter(p=>![188,228].includes(p)).every(p=>unitPages.has(p)));
test('All82content pages have a bounded unit location;93groups retain34prior IDs, hierarchy and unfinished clause coverage');

const byID=id=>units.units.find(u=>u.id===id);
assert.equal(byID('form-momentum').headingUncertain,true);assert.equal(byID('form-momentum').doNotSilentlyNormalize,true);
assert.equal(byID('new-heart-method').unitKind,'umbrella');assert.equal(byID('brush-poem').unitKind,'poem-subunit');
assert.notEqual(byID('traveller').id,byID('traveller-letter').id);
assert.deepEqual(byID('hour-directions').evidencePDFPages,[207,208,209,210,211,212]);
test('Uncertain勢heading, nested poem/umbrella and distinct traveller headings remain explicit;table boundary extends through212');

const table=await json(resolve(base,'HOUR_TABLE_INDEX.json')),stems='甲乙丙丁戊己庚辛壬癸',branches='子丑寅卯辰巳午未申酉戌亥';
assert.equal(table.rows.length,60);assert.equal(new Set(table.rows.map(r=>r.ganzhi)).size,60);
for(let n=0;n<60;n++)assert.equal(table.rows[n].ganzhi,stems[n%10]+branches[n%12]);
for(const [page,count,first,last] of [[207,4,'甲子','丁卯'],[208,12,'戊辰','己卯'],[209,12,'庚辰','辛卯'],[210,12,'壬辰','癸卯'],[211,12,'甲辰','乙卯'],[212,8,'丙辰','癸亥']]){
 const rows=table.rows.filter(r=>r.pdfPage===page);assert.equal(rows.length,count);assert.equal(rows[0].ganzhi,first);assert.equal(rows.at(-1).ganzhi,last);
}
assert.equal(table.labelCellPositions,720);assert.equal(table.literalLabelCellsTranscribed,0);
assert.ok(table.rows.every(r=>r.cellLabelsTranscribed===false));assert.equal(table.completeCastingOrPredictionAlgorithm,false);
test('60literal row headers have valid sexagenary order and six page-transition controls;720positions are not720transcribed rules');

const extracts=await json(resolve(base,'BOUNDED_EXTRACTS.json'));
assert.deepEqual(extracts.seasonalWaterBrush.rows.map(r=>r.waterMetaphor),['昏濁','枯涸','澄清','凝結']);
const sourceSeason=await json(resolve(root,'research/meihua-witness/SEASON_TABLE.json'));
assert.equal(extracts.seasonalWaterBrush.pdfPage,160);assert.deepEqual(Object.keys(sourceSeason.rows),['旺','相','休','囚']);
assert.equal(extracts.glyphAnecdoteLabels.flatMap(r=>r.glyphs).length,23);
assert.equal(extracts.anecdotesAreIndependentValidation,false);assert.equal(extracts.newPredictiveAccuracyEstablished,false);
test('Four brush-season metaphors stay separate from the20cell season table;23glyph anecdotes remain narrative evidence');

assert.equal(extracts.brushSpirits.rows.length,6);
const snake=extracts.brushSpirits.rows.find(r=>r.name==='螣蛇');assert.equal(snake.element,null);assert.equal(snake.printedQualification,'無正位');
const cyclic=await json(resolve(root,'research/meihua-witness/SIX_SPIRITS.json'));
assert.equal(cyclic.starts['己'],'螣蛇');assert.ok(extracts.negativeControls.some(r=>r.pages.includes(213)));
assert.equal(extracts.consumerApplied,false);
test('Glyph六神無正位is not a missing cyclic day-stem assignment;glyph用神and moving-trigram use remain distinct');

const context={};context.window=context;vm.createContext(context);
for(const f of ['engine.js','meihua.js'])vm.runInContext(await readFile(resolve(root,f),'utf8'),context);
const trigrams=context.HHC_MEIHUA.trigrams();assert.equal(trigrams.length,8);
assert.throws(()=>context.HHC_MEIHUA.compose(9,1,1));
for(let n=1;n<=8;n++){const cast=context.HHC_MEIHUA.compose(n,1,1);assert.equal(cast.upper.n,n);}
test('Actual released MaiHoa engine keeps eight trigrams and rejects an invented ninth after the printed extra勾陳clause',{realEngineControls:9});

const archived=await json(resolve(root,'../archives/v53-before-meihua-layers/PACKAGE_MANIFEST.json'));
for(const f of archived.files.filter(f=>!f.file.includes('/')&&/\.(js|css)$/.test(f.file)))assert.equal(sha(await readFile(resolve(root,f.file))),f.sha256,f.file);
const html=await readFile(resolve(root,'Huyen_Hoc_Cac.html'));
assert.equal(html.length,703410);assert.equal(sha(html),archived.product.sha256);
assert.equal(sha(await readFile(resolve(root,'site/index.html'))),sha(html));assert.equal(sha(await readFile(resolve(root,'../Huyen_Hoc_Cac.html'))),sha(html));
const pending=await json(resolve(root,'research/meihua-layers/PENDING.json'));
assert.equal(pending.released,false);assert.equal(pending.browserChecksExecuted,0);assert.equal(pending.pdfCreated,false);
for(const f of pending.candidateFiles)assert.equal(sha(await readFile(resolve(root,'research/meihua-layers/candidate',f.file))),f.sha256);
test('Consumer HTML/JS/CSS keep released bytes;pending candidate remains separate without claiming browser or PDF passes');

await writeFile(resolve(qa,'SOURCE_RESULTS.json'),JSON.stringify({checks,summary:{newPageRecords:47,pageNavigationCovered:84,contentPages:82,priorUnitGroups:34,newUnitGroups:59,totalUnitGroups:93,hourTableRowHeaders:60,labelCellPositions:720,literalLabelCellsTranscribed:0,brushSeasonRows:4,glyphSpirits:6,anecdoteLabels:23,newHTTPResponses:0,newRenderedDerivatives:0,realEngineControls:9,consumerChanged:false,wholeBookRead:false,wholeBookApplied:false},htmlSHA256:sha(html)},null,2)+'\n');
console.log(checks.length+'/'+checks.length,'passed');
