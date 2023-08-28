/**
 * @param {character[]} s
 * @return {void} Do not return anything, modify s in-place instead.
 */
var reverseString = function(s) {
    let leftIndex = 0;
    let rightIndex = s.length-1;
    let attempt;

    while (leftIndex < rightIndex){
        attempt = s[leftIndex];
        s[leftIndex] = s[rightIndex];
        s[rightIndex]= attempt;
        leftIndex++;
        rightIndex--;
    }

};


// h e l l o
// 0 1 2 3 4
// ^

// attemp 0
// leftIndex 0
// rightIndex is 4

// 0 < 4
