'''
all english? yes
case-insensitive
puntation, symbol? yes
has space?
number? yse

left pointer at head, right pointer at tail of array moving toward each other until l >= right
skip space, skip non-numeric, keep alphanumeric only



'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        #remove space, non-alphanumeric
        str = "".join(char for char in s if char.isalnum())
        l, r = 0, len(str)-1
        while l < r:
            if str[l].lower() != str[r].lower():
                return False
            l += 1
            r -= 1
        return True

        