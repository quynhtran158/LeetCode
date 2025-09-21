class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(startIdx, path):
            res.append(path[:])
            for i in range(startIdx, len(nums)):
                path.append(nums[i])
                dfs(i + 1, path)
                path.pop()
        dfs(0,[])
        return res