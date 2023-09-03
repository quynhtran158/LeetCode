/**
@param {number[]} nums
 * @param {number} target
 * 
 * @return {number}
 */

// funtction (nums, target) thi bi sai -> tai sao?
var minSubArrayLen = function (target, nums){
    let l = 0;
    var total=0;
    let res = Infinity;

    for (r = 0; r < nums.length; r++){
        total += nums[r];
        while (total >= target){
            res = Math.min(res, r-l+1);
            total -= nums[l];
            l++;
        }
    }
     return res === Infinity ? 0 : res // if the array is empty, res is infinity so the function will return 0, otherwise, function will return ans
}