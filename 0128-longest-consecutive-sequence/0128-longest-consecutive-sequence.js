/**
* @param {number[]} nums
* @return {number}
*/
var longestConsecutive = function(nums) {
    let newNums = new Set(nums);
    let longest = 0;
    let length;

    for (const n of newNums){
        if (!newNums.has(n-1)){
            length = 1;
            while (newNums.has(n + length)){
                length += 1;
                
            }   
        
        longest = Math.max(length, longest);
        }
    }
    return longest;
};