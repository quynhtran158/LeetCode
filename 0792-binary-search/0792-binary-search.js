/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */

var search = function (nums, target){
    let l = 0;
    let r = nums.length-1;
    
    while (l <= r){
      var  m = Math.floor((l + r) /2);
        if (nums[m]> target){
            r = m-1; //m > target means that the target is in the left side of the array. we need to move the r pointer before the m so that we can look throught the life side of the array
        }

        else if (nums[m] < target){
            l = m+1;  // m < target means that the target is in the right side of the array. We need to move the l pointer after the m so that we can look through the right side of the array
        }

        else{
            return m;
        }
    }
    return -1;
}