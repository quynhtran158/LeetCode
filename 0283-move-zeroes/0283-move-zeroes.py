'''
[1,3,12,0,0]
     l 
          r
[1,0,0,0,3,12]
   l
         r 


write pointer at 0, read pointer iterate thru the array, if read reach non-zero, put non-zero to write, after have all non-zero at front, fill the rest (start from write + 1) will 0
'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # if not nums:
        #     return 0
        # l = 0
        # for r in range(1, len(nums)):
        #     #if nums[l] = 0: swap the number at r with num at l, just swap, we dont have o care if the num at r is or is not 0, the checking will be handle by l pointer
        #     #only move the l when the number at l != 0, keep iterate thru the array by r
        #     if nums[l] != 0:
        #         l += 1
        # #nums[l] = 0: always swap, to move r fwd
        #     nums[l], nums[r] = nums[r], nums[l]
        # return nums
        
        if not nums:
            return 0 
        write = 0
        for read in range(len(nums)):
            if nums[read] != 0:
                nums[write] = nums[read]
                write += 1
        for i in range(write, len(nums)):
            nums[i] = 0
        return nums