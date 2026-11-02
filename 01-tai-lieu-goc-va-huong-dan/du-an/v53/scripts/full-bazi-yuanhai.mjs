import {readFile,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {createRequire} from 'node:module';
import {resolve} from 'node:path';
import vm from 'node:vm';
import assert from 'node:assert/strict';

const root=resolve(import.meta.dirname,'../..'),out=resolve(root,'v53/research/full-study/bazi');
const req=createRequire(resolve(root,'v46/package.json')),{LunarUtil,Solar}=req('lunar-typescript');
const ctx={window:{HHC_ENGINE:{}}};vm.createContext(ctx);vm.runInContext(await readFile(resolve(root,'v53/bazi-relations.js'),'utf8'),ctx);
const GAN='甲乙丙丁戊己庚辛壬癸';
const records=[
  {kind:'正官',vi:'Chính Quan',page:96,printedPage:'卷二 一五',heading:'正官論',pairs:['甲辛','乙庚','丙癸','丁壬','戊乙','己甲','庚丁','辛丙','壬己','癸戊'],quote:'夫正官者甲見辛之類',limits:'The paragraph requires month command and other pillars; the adjacent annotation gives the ten fixed stem relationships. It does not certify a chart solely from the primary month hidden stem.'},
  {kind:'正印',vi:'Chính Ấn',page:101,additionalPages:[102,103],printedPage:'卷二 二〇–二二',heading:'論印綬',pairs:['甲癸','乙壬','丙乙','丁甲','戊丁','己丙','庚己','辛戊','壬辛','癸庚'],quote:'所謂印生我者即印綬也',limits:'The chapter discusses both 正印 and 偏印; page102 explicitly distinguishes opposite versus same polarity. Do not call every 生我 stem 正印.'},
  {kind:'正财',vi:'Chính Tài',page:104,additionalPages:[105,106],printedPage:'卷二 二三–二五',heading:'論正財',pairs:['甲己','乙戊','丙辛','丁庚','戊癸','己壬','庚乙','辛甲','壬丁','癸丙'],quote:'是陰見陽財陽見陰財',limits:'Page105 explicitly says 財不論偏正 while discussing broader wealth cases. The chapter heading is not the classification of every stem in every example.'},
  {kind:'食神',vi:'Thực Thần',page:108,additionalPages:[107],printedPage:'卷二 二六–二七',heading:'論食神',pairs:['甲丙','乙丁','丙戊','丁己','戊庚','己辛','庚壬','辛癸','壬甲','癸乙'],quote:'如甲屬木丙屬火',limits:'The phrase 生我財神 refers to the food stem producing wealth (甲→丙→戊), not 食神 generating the day master. Same-polarity 我生 is the ten-god classification.'}
];
const checks=[];
for(const record of records)for(const pair of record.pairs){
  const reference=LunarUtil.SHI_SHEN[pair],actual=ctx.window.HHC_BAZI_RELATIONS.god(GAN.indexOf(pair[0]),GAN.indexOf(pair[1]));
  assert.equal(reference,record.kind);assert.equal(actual,record.vi);
  checks.push({pair,expected:record.kind,expectedVi:record.vi,lunar:reference,hhc:actual,matched:true,page:record.page});
}
const examples=[
  {page:103,printedPage:'卷二 二二',pillarHan:['戊戌','庚申','癸酉','庚申'],focus:'癸日、庚申月，庚为正印；正文举“官印两全”之例',limit:'Reconstruct compatible dates within1800..currentLibraryYear only to verify calendar and relationships, not the historical subject/date or predicted life.'},
  {page:105,printedPage:'卷二 二四',pillarHan:['辛丑','丁酉','丁巳','丁未'],focus:'丁日、酉月藏辛是偏财；巳中庚是正财。此例在论正财中，但正文说明偏正并论。',limit:'Chapter title does not imply every wealth relationship is 正财 or establish a complete 正财格.'},
  {page:108,printedPage:'卷二 二七',pillarHan:['己未','己巳','丁未','辛丑'],focus:'丁见己为食神（年干、月干）；巳月本气丙是劫财，不应单凭章节标题称食神格。',limit:'The passage discusses food and its conversion to wealth; only the explicit stem relationships are verified here.'}
];
for(const e of examples){
  const day=e.pillarHan[2][0];e.visibleGods=e.pillarHan.map((p,i)=>i===2?'日主':LunarUtil.SHI_SHEN[day+p[0]]);
  e.compatibleCalendarReconstructions=Solar.fromBaZi(...e.pillarHan,2,1800).map(s=>{
    const ec=s.getLunar().getEightChar(),actual=[ec.getYear(),ec.getMonth(),ec.getDay(),ec.getTime()];
    assert.deepEqual(actual,e.pillarHan);
    return {solarUTC8:s.toYmdHms(),fourPillars:actual,monthHidden:ec.getMonthHideGan(),monthHiddenGods:ec.getMonthShiShenZhi()};
  });
  assert.ok(e.compatibleCalendarReconstructions.length>0);
}
const pageNums=[96,97,101,102,103,104,105,106,107,108];
const pageImages=[];
for(const page of pageNums){
  const file=`sources/yuanhai-reading-${String(page).padStart(3,'0')}.png`,data=await readFile(resolve(out,file));
  pageImages.push({page,file,bytes:data.length,sha256:createHash('sha256').update(data).digest('hex'),method:'Rendered from archived PDF using pdftoppm; relevant page and annotations manually visually inspected, no OCR claim.'});
}
const clamping=[
  {input:'2000-02-29',operations:'nextYear(1).nextMonth(1)',actual:Solar.fromYmd(2000,2,29).nextYear(1).nextMonth(1).toYmd(),expected:'2001-03-28'},
  {input:'2024-01-31',operations:'nextMonth(1)',actual:Solar.fromYmd(2024,1,31).nextMonth(1).toYmd(),expected:'2024-02-29'},
  {input:'2023-01-31',operations:'nextMonth(1)',actual:Solar.fromYmd(2023,1,31).nextMonth(1).toYmd(),expected:'2023-02-28'},
  {input:'2020-02-29',operations:'nextYear(10)',actual:Solar.fromYmd(2020,2,29).nextYear(10).toYmd(),expected:'2030-02-28'}
];
for(const r of clamping)assert.equal(r.actual,r.expected);
const source={title:'評註淵海子平',edition:'1926 scan catalogued by National Taiwan Library',pdf:'../../four-items/sources/yuanhai-NTL-v1.pdf',pdfSHA256:'664bccd1ea4706c609df8ea6cd69a4565db97dc277e876fc22eb125ea41dcc9f',catalogue:'https://taiwanebook.ncl.edu.tw/zh-tw/book/NTL-9900014379',readingMethod:'Manual visual reading of selected passages and marginal annotations; not whole-book OCR or line-by-line collation.'};
const result={createdUTC:new Date().toISOString(),source,records,checks,examples,pageImages,clamping,summary:{classicalCategories:4,manuallyTranscribedStemPairs:40,libraryAndHhcMatches:40,classicalFourPillarExamples:3,compatibleCalendarDates:examples.reduce((n,x)=>n+x.compatibleCalendarReconstructions.length,0),clampingTests:clamping.length},notEstablished:['Full formal pattern recognition','Useful-god selection','Complete strength/weakness evaluation','Historical identity/date reconstruction','Empirical predictive accuracy','Entire book fully applied']};
await writeFile(resolve(out,'YUANHAI_FOUR_RELATIONS.json'),JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({summary:result.summary,examples,clamping},null,2));
