'''
sliding window len = k
store the max average, reutrn the max
'''
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window = sum(nums[0:k])
        maxAvg = window/k
        for right in range(k, len(nums)):
            left = right - k
            window += nums[right] - nums[left]
            maxAvg = max(maxAvg, (window/k))
        return maxAvg

        