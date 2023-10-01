/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    const map = new Map();
    
    for (let s of strs){
         let count = new Array(26).fill(0);
        for (let c of s){
            count[c.charCodeAt(0)-'a'.charCodeAt(0)] +=1;
        }
    
    const key = count.join(",");

    if (!map.has(key)){
        map.set(key,[]);
        }

    map.get(key).push(s);
    
    }

    return Array.from(map.values());
};