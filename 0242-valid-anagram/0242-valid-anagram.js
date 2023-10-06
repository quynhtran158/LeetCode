/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    const map = new Map();
    
    if (s.length !== t.length){
        return false;
    }
    for (const c of s){
        console.log(c)
        if (!map.has(c)){
            map.set(c, 1);
        }
        else {
            map.set(c, map.get(c) + 1)
        }
    }
    // console.log(map)

    // console.log('----------')
    for ( const x of t){
        if (!map.has(x) || map.get(x) === 0){
            return false;
        }
        else{
            map.set(x, map.get(x) - 1)
        }
    }

    return true;
};