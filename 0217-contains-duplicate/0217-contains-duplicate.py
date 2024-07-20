class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #use hashmap, key as the number, value is their frequency
        map = {}
        for num in nums:
            if num in map:
                return True
            else:
                map[num] = 1
        return False

        #use set(), if in set return true -> space O(n)
        seen = set()
        nums.sort() #this will set time complexity into O(nlogn) but can save time complexity
        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            else:
                seen.add(nums[i])
        return False
