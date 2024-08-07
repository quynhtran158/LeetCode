class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {} 
        #key is num, val is index
        for i, val in enumerate(nums):
            diff = target - val
            if diff in map:
                return [i, map[diff]]
            else:
                map[val] = i 
        return None