(()=>{'use strict';
const readings={
 1:[
  {title:'Tích lũy trước khi xuất hiện',text:'Hình ảnh rồng còn ẩn gợi một giai đoạn có tiềm năng nhưng chưa thuận để đem ra dùng. Chăm nền tảng và quan sát thời cơ trước khi nhận vai trò lớn.',tip:'Chọn một năng lực cần rèn thêm; thử trong phạm vi nhỏ trước khi công bố hoặc cam kết.'},
  {title:'Bước ra và tìm người dẫn dắt',text:'Rồng xuất hiện ngoài đồng gợi khả năng bắt đầu được nhìn thấy. Sự gặp gỡ với người có kinh nghiệm và phẩm chất đáng tin giúp bạn định hướng cách dùng năng lực.',tip:'Chia sẻ việc đang làm với người phù hợp và xin một phản hồi cụ thể.'},
  {title:'Bền chí đi cùng tự xét',text:'Hào này gợi sự chuyên tâm ban ngày và thận trọng khi nhìn lại công việc. Nỗ lực cần đi cùng tỉnh táo trước chỗ dễ sai, nhất là lúc trách nhiệm đang tăng.',tip:'Rà một rủi ro quan trọng và giữ nhịp làm việc có nghỉ; không biến sự siêng năng thành làm quá sức.'},
  {title:'Thử bước chuyển, giữ đường lui',text:'Hình ảnh rồng có thể vươn lên từ vực sâu gợi một lúc đang cân nhắc tiến hay chờ. Chưa cần ép mình phải chọn một bước nhảy lớn ngay lập tức.',tip:'Thử một bước có thể điều chỉnh, đặt điều kiện rõ ràng để tiếp tục hoặc dừng.'},
  {title:'Dùng vị thế để tạo giá trị',text:'Rồng bay trên trời gợi năng lực có điều kiện phát huy ở vị trí rộng hơn. Lời nhắc về gặp người tài vẫn còn: chủ động không có nghĩa là làm mọi việc một mình.',tip:'Tìm cộng sự bổ sung cho điểm yếu và dùng quyền chủ động để giúp công việc chung tiến lên.'},
  {title:'Biết dừng trước khi vượt giới hạn',text:'Rồng lên quá cao gợi sự quá đà và khả năng hối tiếc. Khi mục tiêu, kỳ vọng hoặc vị thế vượt sức nâng đỡ hiện có, một bước lùi có thể giúp giữ điều đã xây.',tip:'Kiểm lại giới hạn nguồn lực và giảm một cam kết đang vượt sức.'}
 ],
 2:[
  {title:'Nhận ra thay đổi từ dấu hiệu nhỏ',text:'Dẫm lên sương mà nghĩ đến băng cứng gợi việc nhận ra một quá trình từ khi mới bắt đầu. Điều nhỏ lặp lại đáng được quan sát trước khi trở thành vấn đề khó đổi.',tip:'Ghi lại một dấu hiệu đang tái diễn và xử lý nguyên nhân sớm, thay vì suy đoán điều xấu chắc chắn sẽ đến.'},
  {title:'Ngay thẳng, có khuôn phép, rộng lòng',text:'Các hình ảnh ngay thẳng, vuông vắn và rộng lớn gợi cách làm rõ ràng, nhất quán và có sức dung chứa. Có thể bắt đầu từ việc giữ đúng điều căn bản trong cách ứng xử.',tip:'Làm rõ trách nhiệm và tiêu chuẩn chung; giữ nguyên tắc mà vẫn lắng nghe hoàn cảnh của người khác.'},
  {title:'Giữ chiều sâu, làm đến nơi đến chốn',text:'Giữ vẻ đẹp bên trong và cùng làm việc chung gợi năng lực không cần phô bày ngay. Giá trị nằm ở sự bền lòng và hoàn tất trách nhiệm, thay vì chỉ tìm phần công về mình.',tip:'Chọn một việc cần hoàn thành, ghi nhận đóng góp của cả nhóm và để chất lượng công việc lên tiếng.'},
  {title:'Thận trọng với điều đem ra ngoài',text:'Buộc miệng túi gợi một lúc cần giữ gìn lời nói và việc làm. Sự kín đáo có thể giúp tránh sơ suất, nhưng cũng không nhất thiết đem lại lời khen hay sự nổi bật.',tip:'Chỉ chia sẻ điều đã kiểm rõ với người cần biết; đừng dùng sự thận trọng để che giấu việc phải chịu trách nhiệm.'},
  {title:'Giữ sự khiêm nhường ở vị trí có ảnh hưởng',text:'Hình ảnh xiêm vàng gợi cách thể hiện chừng mực và giữ điều tốt ở bên trong. Khi có vai trò đáng chú ý, sự giản dị và tinh thần nâng đỡ giúp giữ cân bằng.',tip:'Chia sẻ công lao và chăm chất lượng phần việc của mình; màu vàng trong hình tượng không phải yêu cầu chọn màu để cầu may.'},
  {title:'Dừng vòng tranh chấp trước khi cùng tổn hao',text:'Hình ảnh rồng tranh ngoài đồng và máu hòa sắc gợi xung đột đã đi đến chỗ cả hai phía đều hao tổn. Đọc như lời nhắc về cái giá của việc tiếp tục hơn thua.',tip:'Tách vấn đề khỏi người đối diện, hạ mức đối đầu và tìm người trung gian khi cần.'}
 ]
};
const allMoving={
 1:{title:'Cùng góp sức, không tranh công đầu',text:'Khi cả sáu hào Càn cùng động, có thể đọc thêm hình ảnh nhiều rồng mà không con nào đứng đầu. Gợi mở ở đây là phối hợp năng lực và bớt tranh phần nổi trội.',tip:'Thống nhất mục tiêu chung và cách chia trách nhiệm; cùng tiến bộ thay vì chỉ tìm người hơn người.'},
 2:{title:'Giữ sự bền lòng qua thay đổi',text:'Khi cả sáu hào Khôn cùng động, lời nhắc bổ sung hướng đến sự bền lâu trong điều đúng đắn. Mềm dẻo khi hoàn cảnh thay đổi vẫn cần một nguyên tắc để tựa vào.',tip:'Chọn điều cốt lõi muốn giữ và điều có thể linh hoạt trong cách thực hiện.'}
};
function movingReading(number,positions){
 number=Number(number);if(!Number.isInteger(number)||number<1||number>64||!Array.isArray(positions)||positions.some(p=>!Number.isInteger(p)||p<1||p>6)||new Set(positions).size!==positions.length)throw Error('Quẻ hoặc vị trí hào chưa hợp lệ.');
 const selected=positions.slice().sort((a,b)=>a-b),entries=readings[number]||window.HHC_YI_COMPLETE_READINGS?.[number],specific=!!entries;
 return {number,specific,lines:selected.map(position=>({position,...(specific?entries[position-1]:{title:'Gợi ý theo vị trí hào',text:window.HHC_CONTENT.lineStages[position-1],tip:null})})),supplement:allMoving[number]&&selected.length===6?{...allMoving[number]}:null};
}
window.HHC_CONTENT.yiMovingReading=movingReading;
})();
