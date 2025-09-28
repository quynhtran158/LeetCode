class Solution:
    '''
    states need to track: closeCount, openCount and startInd
    start with an empty string, add ( or ) and continye to do so 
    until the length reach 2*n (n is num or pair parentheses)
       start index: the curretn position of the str being build
    invalid when openCount > n and want to add ) but no matching ()
 
    '''
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []
        def dfs(startIndex, openCount, closeCount):
            #base case reach the max len of str 
            if startIndex == 2*n: 
                res.append("".join(path))
                return 
            if openCount < n: #valid check, prune if not valide
                path.append("(")
                dfs(startIndex + 1, openCount + 1, closeCount)
                path.pop()
            if closeCount < openCount:
                path.append(")")
                dfs(startIndex + 1, openCount , closeCount+ 1)
                path.pop()
        dfs(0,0,0)
        return res

    