/**
 * @param {character[]} s
 * @return {void} Do not return anything, modify s in-place instead.
 */
var reverseString = function(s) {
    let leftIndex = 0;
    let rightIndex = s.length-1;

   
    for (i=0; i<s.length-1; i++){
         if (leftIndex < rightIndex){
        const temp = s[leftIndex];
        s[leftIndex] = s[rightIndex];
        s[rightIndex]= temp;
        leftIndex++;
        rightIndex--;
    }
    }
};

// h e l l o.  L 0, R 4, t h
// o e l l h.  L 1 R 3 t e
// o l l e h

