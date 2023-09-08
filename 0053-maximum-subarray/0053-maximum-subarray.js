/**
* @param {number[]} nums
* @return {number}
*/
var maxSubArray = function(nums) {
let curSub = 0;
let maxSub = nums[0];

for ( let i = 0; i < nums.length; i++){
    if (curSub < 0){
        curSub = 0;
    }
    
    curSub += nums[i];
    maxSub = Math.max(maxSub, curSub);
    
    }
    return maxSub;
    
    
}

