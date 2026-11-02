import{readFile,writeFile}from'node:fs/promises';import{resolve}from'node:path';import{pathToFileURL}from'node:url';import{createRequire}from'node:module';import assert from'node:assert/strict';
const r=resolve(import.meta.dirname,'..'),q=resolve(r,'qa/bazi-jianlu-context'),req=createRequire(import.meta.url),{chromium}=req('C:/Users/Administrator.DESKTOP-98TGIBL/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const checks=[],errors=[],http=[],test=(name,ok,detail)=>{checks.push({name,ok,detail});assert(ok,name);console.log('PASS',name);};
const browser=await chromium.launch({headless:true});try{
 const p=await browser.newPage({viewport:{width:1440,height:1000},acceptDownloads:true});
 p.on('pageerror',x=>errors.push(x.message));p.on('request',x=>{if(/^https?:/.test(x.url()))http.push(x.url());});
 await p.goto(pathToFileURL(resolve(r,process.argv.includes('--candidate')?'research/bazi-jianlu-context/consumer-candidate/Huyen_Hoc_Cac.html':'Huyen_Hoc_Cac.html')).href+'#bazi');
 const fill=async x=>{for(const k of['y','m','d','hour','minute'])if(x[k]!==undefined)await p.locator(`[name=${k}]`).fill(String(x[k]));await p.locator('.form-details').evaluate(x=>x.open=true);if(x.tz!==undefined)await p.locator('[name=tz]').selectOption(String(x.tz));};
 const compute=()=>p.getByRole('button',{name:'Xem Bát tự',exact:true}).click(),details=p.locator('.bazi-month-context');
 const fixture={y:2020,m:2,d:21,hour:16,minute:30,tz:8};await fill(fixture);await compute();
 test('Known Jianlu chart has a collapsed optional reading after month hidden stems',await details.count()===1&&!await details.evaluate(x=>x.open)&&await details.evaluate(x=>x.previousElementSibling.classList.contains('bazi-month-stems')));
 await details.locator('summary').focus();await p.keyboard.press('Enter');
 test('Keyboard Enter opens the reading and retains visible summary focus',await details.evaluate(x=>x.open)&&await details.locator('summary').evaluate(x=>x===document.activeElement));
 const known=await details.innerText();test('Result displays real day/month and separate year/hour roles',known.includes('Giáp')&&known.includes('Dần')&&known.includes('Canh · Thất Sát')&&known.includes('Nhâm · Thiên Ấn'));
 test('Interpretation does not assert a completed pattern or select an element',known.includes('chưa đủ để kết luận cách cục hoàn chỉnh')&&known.includes('chọn hành cần bổ sung'));
 await details.locator('summary').focus();await p.keyboard.press('Space');test('Keyboard Space closes the same native disclosure',!await details.evaluate(x=>x.open));
 const download=async name=>{const event=p.waitForEvent('download');await p.locator('#download-result').click();await(await event).saveAs(resolve(q,name));return readFile(resolve(q,name),'utf8');};
 const txt=await download('jianlu-closed.txt');test('TXT includes the entire closed month interpretation and year/hour roles then restores closed state',txt.includes('Nhìn thêm từ tháng sinh · Kiến Lộc')&&txt.includes('Nhâm · Thiên Ấn')&&!await details.evaluate(x=>x.open));
 await details.locator('summary').click();await download('jianlu-open.txt');test('TXT preserves an already-open month reading',await details.evaluate(x=>x.open));
 await p.locator('#save-result').click();await p.locator('[name=noTime]').check();await compute();await details.locator('summary').click();
 test('Unknown-hour result keeps known month and year, with no invented hour relation',await details.innerText().then(t=>t.includes('Canh · Thất Sát')&&t.includes('Chưa có giờ sinh để xác định.')&&!t.includes('Nhâm · Thiên Ấn')));
 await p.locator('#profiles-open').click();await p.locator('[data-profile-open]').first().click();
 test('Saved result recomputes the month reading and restores known birth-hour inputs',!await p.locator('[name=noTime]').isChecked()&&await details.count()===1&&!await details.evaluate(x=>x.open));
 await details.locator('summary').click();test('Reopened saved result has the same actual interpretation',await details.innerText()===known);
 await details.locator('summary').click();await p.evaluate(()=>dispatchEvent(new Event('beforeprint')));await p.emulateMedia({media:'print'});
 test('Print expands the month interpretation and hides inputs',await details.evaluate(x=>x.open)&&await details.isVisible()&&!await p.locator('#form-panel').isVisible());
 await p.emulateMedia({media:'screen'});await p.evaluate(()=>dispatchEvent(new Event('afterprint')));test('After print restores the collapsed month reading',!await details.evaluate(x=>x.open));
 await p.emulateMedia({media:'print'});await p.pdf({path:resolve(q,'jianlu-result.pdf'),format:'A4',printBackground:true,preferCSSPageSize:true});await p.emulateMedia({media:'screen'});
 test('Actual PDF lifecycle also restores the collapsed reading',!await details.evaluate(x=>x.open));
 for(const width of[320,390,768,1440]){
  await p.setViewportSize({width,height:1050});await details.evaluate(x=>x.open=true);
  const size=await p.evaluate(()=>({width:innerWidth,scroll:document.documentElement.scrollWidth}));test(`${width}px: explanation fits the page`,size.scroll<=size.width,size);
  if([390,1440].includes(width)){await p.locator('#toast').evaluate(x=>x.hidden=true);await details.screenshot({path:resolve(q,`jianlu-${width}.png`)});}
 }
 await p.setViewportSize({width:1440,height:1000});await fill({...fixture,d:22});await compute();test('Nonmatching day/month has no Jianlu label or leftover interpretation',await details.count()===0);
 await fill({y:2024,m:2,d:4});await p.locator('[name=noTime]').check();await compute();test('Uncertain pillars suppress the optional month reading',await details.count()===0);
 await p.locator('[name=noTime]').uncheck();await fill(fixture);await compute();await p.locator('[name=hour]').fill('18');test('Editing an input removes the old month reading and export controls',await details.count()===0&&await p.locator('#download-result').count()===0);
 test('Consumer text and TXT do not contain raw sources, research panels or blade predictions',!/CADAL|KR3g0042|SOURCE_MANIFEST|SHA-256|WYG003|夭折|羊刃/.test(known+txt));
 test('Standalone runs offline without JavaScript errors or HTTP requests',!errors.length&&!http.length,{errors,http});
}finally{await browser.close();await writeFile(resolve(q,'BROWSER_RESULTS.json'),JSON.stringify({checks,errors,http,pdfCreated:true},null,2)+'\n');console.log(checks.length+' browser checks passed');}
