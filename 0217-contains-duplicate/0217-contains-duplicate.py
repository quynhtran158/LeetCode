class Solution:
    """
    first approach 
    i
    j 
    
    
    """

    # def containsDuplicate(self, nums: List[int]) -> bool:
        # i, j = 0, 0
        # N = len(nums)
        # for i in range(N):
        #     count = 0
        #     if i == j and j < N:
        #         j += 1
        #     for j in range(N):
        #         if nums[j] == nums[i]:
        #             count += 1
        #     if count >= 2:
        #         return True
        # return False

    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        N = len(nums)

        for i in range(N):
            if nums[i] in seen:
                return True 
            else:
                seen.add(nums[i])
        return False
        
