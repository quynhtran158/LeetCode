'''
# TC: o(nlogs) 
goal of this problem is to find the minimum largest subarray sum with m subarrays.

- try to guest the possible minimum largest sum with m subarray
- we can find the minimum largest subarray sum needed to split nums into m subarrays:


feasibility function checks if we can split nums into at most k parts without any subarray’s sum exceeding that limit.

we checking on tổng lớn nhất được phép của một đoạn -> left right must be tổng lớn nhất được phép của một đoạn.

left must be max(arr), if limit < max(arr) this will always false because the largerst sum cannot store the max value 

kiểu như kêu tổng lớn nhắt là 2 nhưng số lớn nhất đag có lfa 3 vậy, vô lý
'''
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        #feasibility function checks if we can split nums into at most k parts without any subarray’s sum exceeding that limit.
        def feasible(nums, k, limit):
            currSum, subArray = 0,0
            for num in nums:
                if currSum + num > limit:
                    currSum = 0
                    subArray += 1 
                currSum += num 

            if currSum != 0: #checking if we have any leftover sum that need a new subarray
                subArray += 1
            return subArray <= k
        
        low, high = max(nums), sum(nums)
        while low <= high:
            mid = low + (high - low) // 2
            if feasible(nums, k, mid):
                ans = mid 
                high = mid - 1 #we are trying to find the minimum of the maximum sum, so we want to 
                #see if we can do better with less number in sum 
            else: 
                low = mid + 1 #not feasible mean we need more
        return ans
                

