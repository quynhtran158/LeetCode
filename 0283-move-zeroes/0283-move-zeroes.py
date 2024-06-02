class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Index to place the next non-zero element.
        insertPos = 0
        
        # Move non-zero elements to the beginning of nums.
        for num in nums:
            if num != 0:
                nums[insertPos] = num
                insertPos += 1
        
        # Fill the remaining positions with zeroes.
        while insertPos < len(nums):
            nums[insertPos] = 0
            insertPos += 1