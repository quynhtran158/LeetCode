'''
startIndex: next potential candidate in candidates
base case: reach the leaf node that path == target
check valid: currSum or the current combination (path) < sum, combination not duplicate


                                    []
                            (1. 1 2).     (1 1.. 2)
                            [1].         1..      2
                         ( 1.. 2)       ( 1.. 2)
                    [1,1]  [1,2]        [1,2]
'''
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        path = []

        def dfs(startIndex, currSum):
            if currSum > target:
                return
            if currSum == target:
                res.append(path[:])
                return 
            
            for i in range(startIndex, len(candidates)):
                if i > startIndex and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                dfs(i+1, currSum + candidates[i])
                path.pop()
        dfs(0,0)
        return res
