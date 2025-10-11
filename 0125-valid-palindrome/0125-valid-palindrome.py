class Solution:
    def isPalindrome(self, s: str) -> bool:
        str = "".join(char for char in s if char.isalnum())
        left, right = 0, len(str)-1
        while left <= right:
            if str[left].lower() != str[right].lower():
                return False 
            left += 1
            right -=1 
        return True
    
