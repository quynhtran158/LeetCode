class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo: Dict[int, bool] = {}

        def dfs(start_index):
            if start_index == len(s):
                return True

            if start_index in memo:
                return memo[start_index]

            ans = False
            for word in wordDict: #if false, keep iterating through word in worDict until have True to break, if end worđDict still false, add memo
                '''
                We iterate over words and check if the current substring s[start_index:] starts with word.
                If word matches, we call dfs(start_index + len(word)) recursively to check if the remaining part of s can be broken.
                If dfs(start_index + len(word)) returns True, we set ans = True and immediately break out of the loop.
                If none of the words lead to a successful segmentation, we return False.
                '''
                if s[start_index:].startswith(word): #check if the first word match
                    if dfs(start_index + len(word)): #check the remain part can be build up from worDict
                    #function children return value to function parent
                    #dfs(8) call dfs(13). dfs(13) true, return true to dfs(8)
                    #when do backtrack, at dfs(8) is true (since dfs(13) true, return) we break the loop and update memo. memo[8] = true 
                        '''
                    memo[8] store in memo so that next time we backtrack to dfs(8) we dont have to check other word vs the string
                    3rd Call: dfs(8) (Substring "apple")
                    Loop over words = ["apple", "pen"]:
                    Checking "apple" ✅ ("apple".startswith("apple"))
                    Call dfs(13)
                    **4th Call: dfs(13) (End of String)**
                    start_index == len(s), return True.
                    Backtracking: Where the break Happens
                    Back to dfs(8)
                    The recursion returned True → ans = True
                    Break out of the loop immediately → No need to check "pen" (in worđict))
                    Back to dfs(5)
                    The recursion returned True → ans = True
                    Break out of the loop immediately → No need to check "apple" again.
                        '''
                        ans = True
                        break

            memo[start_index] = ans
            return ans

        return dfs(0)
