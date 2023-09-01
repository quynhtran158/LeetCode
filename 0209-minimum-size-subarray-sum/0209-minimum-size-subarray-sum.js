/**
 * @param {number} target
 * @param {number[]} nums
 * @return {number}
 */
var minSubArrayLen = function(target, n) {
    let l =0;
    let sum = 0;
    let ans= Infinity;

    for (r = 0 ; r < n.length; r++){
        sum += n[r];
        while (sum >= target){
            ans = Math.min (ans, r-l+1);
            sum -= n[l];
            l++;

        }
    }
    //ans = infinity means array is empty
        return ans === Infinity ? 0 : ans;
};