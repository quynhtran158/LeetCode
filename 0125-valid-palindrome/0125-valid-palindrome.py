class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.replace(" ","") 
        i, j = 0, len(s) - 1

       
        while i < j:
            while i < j and not s[i].isalnum(): #not a alphanumeric char then skip it for i
                i += 1
            while i < j and not s[j].isalnum(): #not a alphanumeric char then skip it for j
                j -= 1
            
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True 