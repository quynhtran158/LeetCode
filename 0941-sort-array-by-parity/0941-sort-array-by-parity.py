'''
plan:
- need to move even to the front and odd number followed by even number
- have 2 pointers, once is the index to move the event the the front, the right pointer is to iterating through the array and compare the value 

nums = [3,1,2,4]

nums = [6,3,1,2,4]

nums = [0]

nums = [1,3,5,7]
return nums = [1,3,5,7]

nums = [2,4,6,8]
'''

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left = 0
        for right in range(len(nums)):
            if nums[right] % 2 == 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        return nums