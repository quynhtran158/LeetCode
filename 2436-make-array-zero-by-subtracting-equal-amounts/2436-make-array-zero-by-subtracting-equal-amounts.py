class Solution:
    '''
    edge case: 
    all 0
    empty array
    all same num 
    '''
    def minimumOperations(self, nums: List[int]) -> int:
        seen = set()
        operation = 0
        for num in nums:
            if num not in seen and num > 0:
                operation += 1
                seen.add(num)
        return operation
