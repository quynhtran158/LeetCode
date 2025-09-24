'''
when s[l] != s[r] the first time, skip l or r, to check the rest 
count the mismatch, if mismatch <= 2 return true, false otherwise

'''
class Solution:
    def makePalindrome(self, s: str) -> bool:
        missMatch = 0
        l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
                missMatch += 1
            l += 1
            r -= 1
        return missMatch <= 2 
                    
        