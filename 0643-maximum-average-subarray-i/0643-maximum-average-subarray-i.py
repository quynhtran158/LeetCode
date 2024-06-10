class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        wSum = 0
        mSum = float('-inf')

        for i in range(k):
            wSum += nums[i]
            mSum = wSum
        #  wSum = sum(nums[:k])  # Sum of the first 'k' elements
        for i in range(k, len(nums)):
            # why k not k-1? the third element in array has index 2, so it alr 
            wSum += nums[i] - nums[i - k]
            mSum = max(mSum, wSum)
        return mSum / k

#sliding window
        