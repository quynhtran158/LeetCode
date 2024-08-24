'''
plan:
- have 2 pointer next to each other, if both pointer is the same value, move left pointer 1 forward move right pointer forward until we reach the first different number
- reach different number -> we swap, then increase both pointer
- if after increasing still different -> sw


nums = [0,1,0,1,1,2,2,3,3,4]
          l
            r
nums = [0,1,2,1,0,1,2,3,3,4]
              l
                      r
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, right = 0, 0
        count = 1
        if not nums:
            return ""
        while right < len(nums):
            if nums[left] != nums[right]:
                left += 1
                nums[left] = nums[right]
                count += 1
            right += 1
        return count


        