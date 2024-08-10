class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkPalindrome(s, left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True      

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return checkPalindrome(s, left + 1, right) or checkPalindrome(s, left, right - 1)
                #because the pair of index left and right is not matching so with this line of code we will check if the character inside of this 2 pair of char (which are not matching) is palindrom or not. If either removing the current left index or the right index make the string palindrom then the helper will return True, if not they will return false and end the program.

            left += 1
            right -= 1

            # the code will keep running if there is no mismatch character, then the increment and decremtn the pointer
            # if the keep incrementing and decrementing the index and nothing happens which means that this is a checkPalindrome
            #then it will break the while loop and return True
        return True      