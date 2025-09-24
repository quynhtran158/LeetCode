'''
when s[l] != s[r] the first time, skip l or r, to check the rest 
count the mismatch, if mismatch <= 2 return true, false otherwise

'''
class Solution:
    def makePalindrome(self, s: str) -> bool:
        def isPalindrome(i,j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True 
            
        missMatch = 0
        l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
                missMatch += 1
                isPalindrome(l+1, r) or isPalindrome(l, r-1)
            l += 1
            r -= 1
        return True if missMatch <= 2 else False
                    
        