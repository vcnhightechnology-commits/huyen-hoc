(()=>{'use strict';
const E=window.HHC_ENGINE,R=window.HHC_BAZI_RELATIONS;
const luBranches=[2,3,5,6,5,6,8,9,11,0];
const esc=x=>String(x).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
function inspect(r){
 if(!r?.dayP||!Array.isArray(r.all)||!r.all[1])throw Error('Chưa có Bát tự.');
 if(r.uncertainPillars?.some(Boolean))return{known:false,matched:null,year:null,hour:null};
 const day=r.dayP.s,month=r.all[1].b;
 if(!Number.isInteger(day)||day<0||day>9||!Number.isInteger(month)||month<0||month>11)throw Error('Can ngày hoặc chi tháng chưa hợp lệ.');
 const data=R.inspect(r),at=index=>data.pillars[index]?{stem:data.pillars[index].visible.name,relation:data.pillars[index].visible.god}:null;
 return{known:true,matched:month===luBranches[day],dayStem:E.stems[day],monthBranch:E.branches[month],
  year:at(0),hour:at(3),completeChart:!!r.all[3],patternEstablished:null,usefulGodSelected:null};
}
function render(r){
 const d=inspect(r);if(!d.known||!d.matched)return'';
 return`<details class="bazi-month-context relation-guide result-expand-export"><summary>Nhìn thêm từ tháng sinh · Kiến Lộc</summary><p>Can ngày <b>${esc(d.dayStem)}</b>, tháng <b>${esc(d.monthBranch)}</b>: tháng sinh ở vị trí Lâm Quan của can ngày, thường gọi là Kiến Lộc.</p><p>Để đọc bố cục này, cần xem thêm các trụ khác. Ở hai can năm và giờ của bạn:</p><ul><li><b>Can năm:</b> ${d.year?`${esc(d.year.stem)} · ${esc(d.year.relation)}`:'Chưa xác định.'}</li><li><b>Can giờ:</b> ${d.hour?`${esc(d.hour.stem)} · ${esc(d.hour.relation)}`:'Chưa có giờ sinh để xác định.'}</li></ul><p class="hint">Tên vị trí tháng này chưa đủ để kết luận cách cục hoàn chỉnh hoặc chọn hành cần bổ sung. Đọc các quan hệ cùng toàn bộ lá số và hoàn cảnh thực tế.</p></details>`;
}
window.HHC_BAZI_MONTH_CONTEXT={inspect,render};
})();
