/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {  
    let max_sum = nums[0];
    let curr_sum= nums[0];

    for (i = 1; i < nums.length; i++) {
        curr_sum = Math.max(curr_sum + nums[i], nums[i]);
        max_sum = Math.max(curr_sum, max_sum);
    }

    return max_sum;

};



