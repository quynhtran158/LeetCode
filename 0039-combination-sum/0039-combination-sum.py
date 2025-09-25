class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res =[]
        def dfs(start, path, currSum):
            # Base cases
            if currSum == target:
                res.append(path[:])   # make a copy
                return
            if currSum > target:
                return  # invalid branch

            # Recursive exploration
            for i in range(start, len(candidates)): #this will make sure the repetition wont happend bc after the
            #first 1 is done exploring, it will start 
                path.append(candidates[i])
                dfs(i, path, currSum + candidates[i])  # reuse allowed → dfs(i,..)
                path.pop()  # backtrack

        dfs(0, [], 0)
        return res