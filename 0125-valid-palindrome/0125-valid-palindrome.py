class Solution:
    '''
    understand
    - what is the maximum length of the string?
    - can the string be empty? if yes what should i return?
    - can i assume all english alphabet?
    - is the string case sensitive?
    
    plan:
    keep track of the front and the back of the string
    keep track of non-alphanumeric character, if non-alphanumeric char skip, is alpha continue checking
    if iterating through the array, all character is the same as the front and the back then true, otherwise false

    implement:
    have two pointer to keep track of the front and the back of the string
    if non-alpha, skip, if is alpha continue checking



    '''
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        #check if the character is alphabet char
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
        #at this point, both char at L and R are character
        #check if the current alphabet char, lowercase is the same
            #same char, moving on
            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False
        return True
               
            
            




        