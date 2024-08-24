'''
- is this array sorted? -> dont allow to sort array
- can this array be empty?
- if this array is not sorted. is their any time complexity constain that you want me to do? if not i will sort the array

plan:
have left and right pointers at front and back
check if left is 0, and right not 0, swap

happy case: 
nums = [1,3,0,0,12]
        l
        r
nums = [3,0,1,0,3,12]
          l
          r
edge case:
nums = [0,0,0,0,0]

nums =[o,o,o,o,1]

plan:
have 2 pointer at the beginning - index 0
move the right pointer until reach
'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for right in range(len(nums)):
            # if nums[left] != 0:
            #     left += 1
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        return nums