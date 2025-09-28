class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        
        def dfs(startIndex, currSum):
            if currSum > target:
                return
            if currSum == target:
                res.append(path[:])
                return
            for startIndex in range(startIndex,len(candidates)):
                if currSum < target:
                    path.append(candidates[startIndex])
                    dfs(startIndex, currSum +candidates[startIndex])
                    path.pop()
        dfs(0,0)
        return res
