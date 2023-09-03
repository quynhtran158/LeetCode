/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

var twoSum = function(nums, target){
    const prevMap = new Map();

    for (i = 0; i < nums.length; i++){
        const n = nums[i];
        let diff = target - n;

        if (prevMap.has(diff)){
            return [prevMap.get(diff),i]; //[] to create an array with index of the diff
        }
    prevMap.set(n,i); //neu ma diff chua xuat hien trong hash ma thi set de bo vo hashmap
    }
}