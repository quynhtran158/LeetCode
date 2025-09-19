class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #map. key: num in array, val: the index of that number 
        map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in map:
                return [i, map[complement]]
            else:
                map[num] = i
        return None