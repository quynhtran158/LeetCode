class Solution:
    '''
    - append only open bracket to the stack, wwhen wwe reach a close bracket, we will check if the current top stack is the matching open with the current close bracket or not
    - have a hashmap to check if the top of the stack if the match open bracket when we we reach an close bracket
    - if we find a match close-open, pop the stack (open bracket)
    - if the stack is empty when we are in the middle of iterating process, we return false since we run out of open bracket
    - if after iterating the str, the stack is empty -> return true since all match pairs have been found
    '''

    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {"(": ")", "{":"}", "[":"]"}
        for c in s:
            if c in mapping:
                stack.append(c)
            else: #is the clos bracket
                if not stack:
                    return False
                prev_open = stack.pop()
                if mapping[prev_open] != c:
                    return False
        return not stack
                    

