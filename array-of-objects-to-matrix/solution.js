/**
 * @param {Array} arr
 * @return {Matrix}
 */
var jsonToMatrix = function(arr) {
    const data={};
    function addCol(obj,prefix,row){
        for(const k of Object.keys(obj)){
            const col=prefix+k;
            const val=obj[k]
            if(typeof val=='object' && val!==null) 
                addCol(val,col+'.',row)
            else {
                if(!data[col]) data[col]=Array(arr.length).fill('')
                data[col][row]=val
            }
        }
    }
    for(let row=0;row<arr.length;row++) addCol(arr[row],'',row)
    const cols=Object.keys(data).sort()
    const res=[cols]
    for(let row=0;row<arr.length;row++) res.push(cols.map(c=>data[c][row]))
    return res;
};