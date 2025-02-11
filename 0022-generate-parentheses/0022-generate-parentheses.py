class Solution:
    '''
    states need to track: closeCount, openCount and startInd
    start with an empty string, add ( or ) and continye to do so 
    until the length reach 2*n (n is num or pair parentheses)

    invalid when openCount > n and want to add ) but no matching ()

    '''
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []
        def dfs(start, openCount, closeCount):
            #base case
            if start == n*2:
                res.append("".join(path)) #path is string
                return
            
            if openCount < n:
                path.append("(")
                dfs(start + 1, openCount + 1, closeCount)
                path.pop() #backtrack
            if closeCount < openCount:
                path.append(")")
                dfs(start + 1, openCount, closeCount + 1)
                path.pop() #backtrack
        dfs(0,0,0)
        return res
            
