class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # ans = nums + nums
        # return ans #time O(n), space O(n)
        ans = []
        for _ in range(2):
            for i in range(len(nums)):
                ans.append(nums[i])
        return ans