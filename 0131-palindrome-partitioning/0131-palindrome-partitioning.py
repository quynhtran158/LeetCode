class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        n = len(s)
        def isPalindrome(word):
            return word == word[::-1]
        def dfs( start, currPath):
            if start == n: 
            # '=" to know that we alr visited all word in the s, 
            #not "<" bc we check end of s or not
                ans.append(currPath.copy()) 
                # ans.append(currPath[:])
                #to not modify the original path after adjusting in the backtracking later
                return 
            for end in range(start+1, n+1):
                prefix = s[start:end] 
                if isPalindrome(prefix):
                    dfs(end, currPath + [prefix]) #update new choice 
        dfs(0, [])
        return ans
        