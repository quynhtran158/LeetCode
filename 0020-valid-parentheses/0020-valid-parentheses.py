'''
correct order -> return false immediately if no matching order 
empty string?

cases:
start with closing bracket 
all open, all close
empty


idea:
add the opening bracket to stack
have a hashmap to pair the matching open and close bracket 
when reach the close bracket, pop the stack has opening bracket, check the hashmap 
to define whether the close and open bracket match 

at the end if the open bracket stack empty means all pairs are match

s = "[({})]
        |

stack = "[({
stack.pop = {

time: O(n) worst case loop thru all s 
space: O(n) worst case all open bracket
'''
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        #key is the closing since we check the value as opening when we pop stack
        mapping = {")": "(", "]":"[", "}":"{"}

        for c in s:
            if c not in mapping: #is opening
                stack.append(c)
            else:
                if not stack:
                    return False #the s starts with close bracket
                if c in mapping:
                    prev_open = stack.pop()
                    if mapping[c] != prev_open:
                        return False
        return not stack 
                    


        