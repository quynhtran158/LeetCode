class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        map = {}
        for i in range(len(nums)):
            if nums[i] not in map:
                map[nums[i]] = 1
            else:
                map[nums[i]] += 1

            if map[nums[i]] == 2:
                return True
        return False
            
            