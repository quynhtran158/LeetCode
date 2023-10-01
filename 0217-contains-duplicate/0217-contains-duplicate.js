/**
* @param {number[]} nums
* @return {boolean}
*/

// //brute force TLE
// var containsDuplicate = function(nums) {
//     for (let right = 0; right < nums.length; right){
//         for (let left = 0; left < right; left++){
//             if (nums[left]=== nums[right]){
//                 return true;
//             }
//     }
//     }
//     return false;
// };

//hashset
var containsDuplicate= function(nums){
    let set = new Set();
    for ( let x of nums){
        if (set.has(x)){
            return true;
        }
        set.add(x);
    }
    return false;
}
