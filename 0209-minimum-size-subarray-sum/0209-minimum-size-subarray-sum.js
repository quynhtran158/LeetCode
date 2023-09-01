/**
 * @param {number} target
 * @param {number[]} nums
 * @return {number}
 */

 //using 2 pointer
var minSubArrayLen = function(target, nums) {
    let L = 0;
    let total = 0;
    let ans = nums.length;
/** L for left pointer
R for right pointer
total for sum of subarray 
*/

let sum = 0;
for (let i = 0; i < nums.length; i++ ) {
  sum += nums[i];
}
if (nums.length === 0 || sum < target) {
    return 0;
}
for (R = 0; R < nums.length; R++){
    total += nums[R];
    if (total >= target)
        ans = Math.min(ans, R-L+1);
    while (total - nums[L] >= target && L < R) {
        total -= nums[L]
        L += 1
        ans = Math.min(ans, R-L+1);
    }
}
return ans;
}; 