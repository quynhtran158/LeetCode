'''
array non-empty? no
what if nums doesn't contain val? 
can nums not contain val? yes
what if nums contain all val? what to return? return 0

time: O(n)
loop thru nums, compare each element, if nums[i] == val, skip, 
if nums[i] != val, k += 1

return k -> count of element in nums that not equal to val
'''
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k