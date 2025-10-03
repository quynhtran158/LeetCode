'''
[1,2,3,1,2,3,3,4]
     l 
            r
plan:
- have 2 pointers: both at head of array
- use the right pointer to iterate through the array
- keep moving the right pointer until we reach the different number 
- increase left pointer by 1, then update the value at left pointer with value at right pointer if we detact the change/find of new number



'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        for right in range(len(nums)):
            if nums[left] != nums[right]:
                left += 1
                nums[left] = nums[right]
        return left + 1        