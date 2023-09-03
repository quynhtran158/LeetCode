/**
 * @param {number[]} nums
 * @return {number}
 */

/**
Cac edge case:
- Empty array
- All negative numbers
- All 0 in array
- 1 element in array
 */


 /**
 What if the array is empty, what do you want me to return?
  */
var maxSubArray = function(nums) {
   let maxSub = nums[0]; //initialize the max sub arr with first element of the array
   let curSum = 0;

   for (i=0; i < nums.length ; i++){
       // if the curSum is negative, we set the current sum back to 0
       /** this will also right with the array contains all negative number 
    because */ 
       if (curSum < 0){
           curSum = 0;
       }

       curSum += nums[i]; //update the sum by adding more number to the current sum
       maxSub = Math.max(maxSub, curSum) // here, we will compare the maxSub with the curSum. If curSum is larger than maxSub, we update the maxSub with the curSum
   }
   return maxSub; 
};