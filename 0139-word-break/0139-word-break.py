'''
need to keep track of the current index in s (to check current start and the remain)

target = "aaab"
words = ["a","aa","aaa"]
-> have dupicate, might check the same index in s multiple time in multiple branch -> use memoization to store the result of the recursive function for each value of start_index.

memo[4] = true/false => all paths lead to dfs(4) = true/false

plan:
startIndex: current index of s, purpose iterate thru s and check the current char vs remaining char
memo dict = map key startIndex w/ value result of the recursion call

at each index s will check with words[0], if true, keep checking with next index in s, if wrong, move to the next word in words

As soon as you find one successful segmentation, you stop trying other words at that index.
'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def dfs(startIndex):
        #base case: at the end of the target s, no remaing char to check with words

            if startIndex == len(s):
                return True #reach the end of string
            if startIndex in memo:
                return memo[startIndex]
            ans = False
            for word in wordDict:
                if s[startIndex:].startswith(word): #true then recursion on the remaining s, with the same word in words
                    if dfs(startIndex + len(word)):
                        ans = True #after the recursion return true by base case, go back to prev dfs() set ans = true
                        break

            memo[startIndex] = ans #outside for looop to store the final result computed by recursion of the curretn start_index after we've tried all possible options.
            return ans
        return dfs(0)

               
        