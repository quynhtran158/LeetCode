'''
array non-empty? no
what if nums doesn't contain val? 
can nums not contain val? yes
what if nums contain all val? what to return? return 0

2 pointers:
nums = [1,2,2,3,6,5] (original)
nums = [1,3,6,5,6,5] (removed)
              k
                 i
val = 2

k = 0, i = 0, increase k when replace nums[k] with a nums[i] != val, i will loop through len(nums)
we replace the nums[k] where it different from val, so that different value still there in nums, so we still need to replace that -> this is where nums[k] != val work 

return k -> count of element in nums that not equal to val and nums shouldn't contain val
'''
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k