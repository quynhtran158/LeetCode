/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {

    const prevMap = new Map(); // val: index

    for (let i = 0; i < nums.length; i++) {
      const n = nums[i];
      const diff = target - n;

      if (prevMap.has(diff)) {
        return [prevMap.get(diff), i];
      }

      prevMap.set(n, i);
    }
 

};