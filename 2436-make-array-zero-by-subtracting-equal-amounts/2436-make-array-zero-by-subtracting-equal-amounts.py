class Solution:
    '''
    nums[0] =1
    len = 1
    '''
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        operation = 0
        for i in range(len(nums)):
            if nums[i] > 0 and (i == 0 or nums[i] != nums[i - 1]):
                operation += 1
        return operation