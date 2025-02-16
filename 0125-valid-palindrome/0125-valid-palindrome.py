class Solution:
    '''
    is the string contain all english alphabet? -> yes
    does it contain number? -> no
    does it contain non-alphanumeric char? -> yes ( #!#$)
    is the string case sensitive? ->  no
    does the string has space between 2 words? -> yes
    does the string has multiple space between 2 word? -> no
    is the palidrome space sensitive? -> no
    is the string never emtpy?

    plan:
    has 2 pointer l at the head and r at the tail of the string
    move 2 pointes toward each other, stop when l > r
    when the curren pointer at space, skip the space, dont count the space in the comparision

    - remove all non-alphanumeric in the string
    '''
    def isPalindrome(self, s: str) -> bool:
        str = "".join(char for char in s if char.isalnum()) #remove all non-alphanumeric char
        l, r = 0, len(str)-1
        while l < r:
            print ("str[l]",str[l])
            print ("str[r]",str[r])

            if str[l].lower() != str[r].lower():
                return False
            l += 1
            r -= 1
        return True