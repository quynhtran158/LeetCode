'''
understand:
- what is the maximum length of the string?
- can the string be empty? how should i return the output?
- can i assume the string all contains english alphabet?
- does the string contain non-alphanumeric character?

s = "abca"
return True (remove either b or c)

s = "abcba"
return True

s = "abd"
return True

s= "abdecba"
return False

s="ebab"
return True

s="ebadab"
     l
        r
return True

method:

plan 
- bc of having palindrome, want to have front and end pointer to keep track of the character
- when we see a different pair, we might want to skip that char and test the rest of the string to see if the string is palindrome if after 1 time skipping, the rest of string still palindrome then return true, ottherwiswe false



'''
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                skip_left = isPalindrome(left+1, right) 
                skip_right = isPalindrome(left, right-1)
                return skip_left or skip_right
            left +=1
            right -=1
        return True
            