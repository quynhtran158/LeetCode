class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map = {}
        for i in range(len(nums)):
            if nums[i] not in map:
                map[nums[i]] = 1
            else:
                map[nums[i]] += 1
        
        for num, count in map.items():
            if count > len(nums) // 2:
                return num
                
        
        
        
