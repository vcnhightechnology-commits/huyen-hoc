// Literal top-to-bottom glyph readings in the retained edition, not an inferred forecast.
const rows={
 '艮':['100100','100101','100111','100011','101011','111011','110011','110100'],
 '坎':['010010','010011','010001','010101','011101','001101','000101','000010'],
 '乾':['111111','111110','111100','111000','110000','100000','101000','101111'],
 '兌':['011011','011010','011000','011100','010100','000100','001100','001011'],
 '坤':['000000','000001','000011','000111','001111','011111','010111','010000'],
 '離':['101101','101100','101110','101010','100010','110010','111010','111101'],
 '巽':['110110','110111','110101','110001','111001','101001','100001','100110'],
 '震':['001001','001000','001010','001110','000110','010110','011110','011001']};
const stages=['六爻不變','初世卦','二世卦','三世卦','四世卦','五世卦','遊魂卦','歸魂卦'];
const big=['伏位','禍害','天醫','延年','五鬼','生氣','六煞','絶命'],small=['輔弼','五鬼','福德','絶體','天醫','生氣','遊魂','絶命'];
const index=new Map(Object.entries(rows).flatMap(([palace,items])=>items.map((glyphs,stage)=>[glyphs,{palace,stage,sourcePage:['艮','坎','乾'].includes(palace)?107:108}])));
export function eightPalace({system,linesBottomToTop}={}){
 if(system!=='xieji-eight-palace-figures')throw new TypeError('Explicit named figure system required');
 if(linesBottomToTop===null)return{system,palace:null,stage:null,sourcePage:null,practicalOutcome:null};
 if(!Array.isArray(linesBottomToTop)||linesBottomToTop.length!==6||linesBottomToTop.some(x=>x!==0&&x!==1))throw new TypeError('Six explicit0/1polarities from bottom to top required');
 const glyphs=linesBottomToTop.slice().reverse().join(''),row=index.get(glyphs);
 return{system,...row,sourceStage:stages[row.stage],bigRelation:big[row.stage],smallRelation:small[row.stage],glyphsTopToBottom:glyphs,practicalOutcome:null};
}
