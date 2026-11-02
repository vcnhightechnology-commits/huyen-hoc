(()=>{'use strict';
const E=window.HHC_ENGINE,F=window.HHC_FORTUNE,dayMS=86400000;
const esc=v=>String(v??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const stamp=s=>Date.UTC(s.y,s.m-1,s.d),civil=t=>{const d=new Date(t);return{y:d.getUTCFullYear(),m:d.getUTCMonth()+1,d:d.getUTCDate()}},iso=s=>`${s.y}-${String(s.m).padStart(2,'0')}-${String(s.d).padStart(2,'0')}`,short=s=>`${s.d}/${s.m}/${s.y}`;
function inspect(chart,value){
 const selected=F.inspect(chart,value),year=selected.lunar.y,rows=[];
 if(year<1900||year>2100)return{year,yearName:selected.yearName,rows,unavailable:'Lịch các tháng chỉ hỗ trợ năm âm từ 1900 đến 2100.'};
 const birthStamp=stamp(chart.originalSolar),selectedStamp=stamp(selected.date),policy=chart.input.leapPolicy||'same';
 for(let month=1;month<=12;month++)for(const leap of [false,true]){
  let first,last,lastDay;
  try{first=E.lunarToSolar(1,month,year,leap,chart.tz)}catch(e){
   if(/1900|2100/.test(e.message))rows.push({key:`${month}-${leap?1:0}-outside`,month,leap,available:false,active:false,reason:'Khoảng này nằm ngoài lịch dương 1900–2100 được hỗ trợ.'});
   continue;
  }
  try{last=E.lunarToSolar(30,month,year,leap,chart.tz);lastDay=30}catch(e){if(/1900|2100/.test(e.message)){rows.push({key:`${month}-${leap?1:0}-outside`,month,leap,available:false,active:false,reason:'Khoảng này vượt quá lịch dương 1900–2100 được hỗ trợ.'});continue}try{last=E.lunarToSolar(29,month,year,leap,chart.tz);lastDay=29}catch(rangeError){rows.push({key:`${month}-${leap?1:0}-outside`,month,leap,available:false,active:false,reason:/1900|2100/.test(rangeError.message)?'Khoảng này vượt quá lịch dương 1900–2100 được hỗ trợ.':'Chưa thể xác định đủ khoảng ngày trong phạm vi lịch hỗ trợ.'});continue}}
  const parts=leap&&policy==='split16'?[[1,15],[16,lastDay]]:[[1,lastDay]];
  for(const[from,to]of parts){
   const start=from===1?first:E.lunarToSolar(from,month,year,leap,chart.tz),end=to===lastDay?last:E.lunarToSolar(to,month,year,leap,chart.tz),endStamp=stamp(end),fromStamp=Math.max(stamp(start),birthStamp),active=selectedStamp>=stamp(start)&&selectedStamp<=endStamp;
   const row={key:`${month}-${leap?1:0}-${from}`,month,leap,fromDay:from,toDay:to,first:start,last:end,active,available:false,partial:from!==1||to!==lastDay};
   if(endStamp<birthStamp){row.reason='Trước ngày sinh.';rows.push(row);continue}
   const candidate=civil(fromStamp);row.readFrom=candidate;row.value=iso(candidate);
   if(fromStamp>stamp(start)){row.fromDay=E.solarToLunar(candidate.d,candidate.m,candidate.y,chart.tz).d;row.partial=true}
   let review=false;for(let t=fromStamp;t<=endStamp;t+=dayMS)if(E.calendarNeedsReview(civil(t))){review=true;break}
   if(review){row.reason='Một phần khoảng này cần xác nhận lịch. Có thể chọn ngày trực tiếp ở trên.';rows.push(row);continue}
   try{const r=F.inspect(chart,row.value);row.monthly={idx:r.monthly.idx,name:r.monthly.name,branch:r.monthly.branch};row.available=true}catch(e){row.reason=e.message}
   rows.push(row);
  }
 }
 return{year,yearName:selected.yearName,rows,splitLeap:policy==='split16'&&rows.some(r=>r.leap)};
}
function render(chart,result){
 const data=inspect(chart,result.value);
 return `<details class="fortune-months"><summary>Các tháng trong năm ${esc(data.yearName)} · ${data.year}</summary><p class="hint">Chọn một khoảng để đọc từ ngày đầu của khoảng đó. Mỗi dòng ghi tháng âm và ngày dương tương ứng.${data.splitLeap?' Tháng nhuận chia hai khoảng theo lựa chọn từ ngày 16.':''}</p>${data.unavailable?`<p>${esc(data.unavailable)}</p>`:`<div class="fortune-month-grid">${data.rows.map(r=>`<button type="button" class="fortune-month ${r.active?'current':''} ${r.available?'':'unavailable'}" ${r.available?`data-forecast-date="${r.value}"`:'disabled'} ${r.active?'aria-current="true"':''}><b>Tháng ${r.month}${r.leap?' nhuận':''}${r.partial?` · ngày ${r.fromDay}–${r.toDay}`:''}</b>${r.first&&r.last?`<small>${short(r.readFrom||r.first)} – ${short(r.last)}</small>`:''}${r.available?`<span>${esc(r.monthly.name)} · ${esc(r.monthly.branch)}</span>`:`<span>${esc(r.reason)}</span>`}${r.active?'<em>Đang xem</em>':''}</button>`).join('')}</div>`}</details>`;
}
window.HHC_FORTUNE_MONTHS={inspect,render};
})();
