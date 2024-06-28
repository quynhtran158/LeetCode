class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums)):
            if nums[i] > 0: 
                break
            l, r = i+1, len(nums) - 1
            while l < r: 
                cur_sum = nums[l] + nums[r]
                if nums[i] + cur_sum == 0: 
                    res.add((nums[i], nums[l], nums[r]))
                    l += 1
                elif nums[i] + cur_sum < 0: 
                    l += 1
                else: 
                    r -= 1
        return res
